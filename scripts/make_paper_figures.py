"""Figures 3 and 4 of the paper: reference renderings and coordinate tables for redrawing them in ConceptDraw.

The paper's figures are drawn in ConceptDraw. This script reads the result files of the PP-FedData repository (no number
typed by hand) and writes, for each chart:
  - a reference rendering (PDF and PNG) whose page and plot frame have exactly the sizes given in the tables, so it can be
    placed as a locked background layer in ConceptDraw and traced;
  - the position in millimetres of every marker, error bar, tick, reference line and label (huong_dan/SO_LIEU_HINH_3_4.md).

Usage (from the Latex_FinalCapstone folder):
    python scripts/make_paper_figures.py --results ../results --out huong_dan/tham_chieu --table huong_dan/SO_LIEU_HINH_3_4.md

Inputs:  <results>/scorecard.json (TSTR macro-F1, its seed std, bytes per run, validity, Pareto front),
         <results>/summary.csv (TRTR references B0-rf and B1b-rf).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

MM = 1 / 25.4  # inches per millimetre

# Page and plot frame of each figure, in mm from the top-left corner of the page (y grows downwards, as in ConceptDraw).
LAYOUT = {
    "fig3": {"w": 88.0, "h": 60.0, "x0": 14.0, "x1": 86.0, "y0": 3.0, "y1": 48.0,
             "xlim": (-0.4, 3.4), "ylim": (0.05, 0.55), "xlog": False},
    "fig4": {"w": 88.0, "h": 70.0, "x0": 14.0, "x1": 86.0, "y0": 15.0, "y1": 58.0,
             "xlim": (0.25, 400.0), "ylim": (0.10, 0.50), "xlog": True},
}

COLOR = {"blue": "#1F77B4", "green": "#2CA02C", "red": "#D62728", "purple": "#9467BD", "gray": "#595959"}

# The configurations of Table IV: the best CVAE route on validation at each epsilon, and the headline FedDP-Marginal ones
MG_DIST = {"1": "MGr-eps1", "5": "MGs-eps5", "10": "MGs-eps10", "inf": "MGs-nodp"}
MG_LOCAL = {"1": "MGl-eps1", "5": "MGl-eps5", "10": "MGl-eps10"}
CVAE = {"1": "M1-eps1", "5": "M1o-eps5 (plain)", "10": "M1o-eps10", "inf": "B3"}
EPS_ORDER = ["1", "5", "10", "inf"]
EPS_LABEL = {"1": "1", "5": "5", "10": "10", "inf": "∞"}
SERIES3 = [  # name, configurations, colour, marker, horizontal offset (category units)
    ("FedDP-Marginal, distributed DP", MG_DIST, "blue", "o", -0.08),
    ("FedDP-Marginal, local DP", MG_LOCAL, "green", "s", 0.0),
    ("Federated CVAE (best config.)", CVAE, "red", "^", 0.08),
]
FAMILY4 = {  # family -> (legend text, colour, marker)
    "dist": ("MG, distributed DP", "blue", "o"),
    "local": ("MG, local DP", "green", "s"),
    "nodp": ("MG, no DP", "purple", "D"),
    "cvae": ("Federated CVAE", "red", "^"),
}
# labelled points of Fig. 4: configuration, text position (MB, macro-F1)
LABELS4 = [("MGs-eps10", 3.2, 0.462), ("MGs-eps5", 3.2, 0.405), ("MGr-eps1", 3.2, 0.350),
           ("B3", 40.0, 0.462), ("M2", 230.0, 0.372), ("M1-eps1", 150.0, 0.24)]
MARKER_NAME = {"o": "tròn", "s": "vuông", "^": "tam giác", "D": "thoi"}


def to_mm(fig: str, x: float, y: float) -> tuple[float, float]:
    L = LAYOUT[fig]
    if L["xlog"]:
        fx = (math.log10(x) - math.log10(L["xlim"][0])) / (math.log10(L["xlim"][1]) - math.log10(L["xlim"][0]))
    else:
        fx = (x - L["xlim"][0]) / (L["xlim"][1] - L["xlim"][0])
    fy = (y - L["ylim"][0]) / (L["ylim"][1] - L["ylim"][0])
    return L["x0"] + fx * (L["x1"] - L["x0"]), L["y1"] - fy * (L["y1"] - L["y0"])


def frame_md(fig: str) -> str:
    L = LAYOUT[fig]
    return (f"- **Khung đồ thị** (hình chữ nhật không nền, viền đen 0.2 mm): tâm ({(L['x0'] + L['x1']) / 2:.1f}, "
            f"{(L['y0'] + L['y1']) / 2:.1f}) mm, rộng {L['x1'] - L['x0']:.0f} mm, cao {L['y1'] - L['y0']:.0f} mm. "
            f"Nhãn trục x căn giữa tại X = {(L['x0'] + L['x1']) / 2:.1f} mm, Y ≈ {L['h'] - 3:.0f} mm; "
            f"nhãn trục y xoay 90°, tâm tại X ≈ 3 mm, Y = {(L['y0'] + L['y1']) / 2:.1f} mm.")


def style() -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        # IEEE conference template: figure labels in about 8 pt Times New Roman at the printed size; no text below 8 pt
        "font.size": 8,
        "axes.labelsize": 8.5,
        "legend.fontsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "axes.linewidth": 0.6,
        "lines.linewidth": 1.1,
        "pdf.fonttype": 42,
    })


def frame(fig: str):
    L = LAYOUT[fig]
    f = plt.figure(figsize=(L["w"] * MM, L["h"] * MM))
    ax = f.add_axes([L["x0"] / L["w"], 1 - L["y1"] / L["h"], (L["x1"] - L["x0"]) / L["w"], (L["y1"] - L["y0"]) / L["h"]])
    if L["xlog"]:
        ax.set_xscale("log")
    ax.set_xlim(*L["xlim"])
    ax.set_ylim(*L["ylim"])
    return f, ax


def family(label: str) -> str:
    if label in ("MGp-nodp", "MGs-nodp"):
        return "nodp"
    if label.startswith("MGl"):
        return "local"
    if label.startswith("MG"):
        return "dist"
    return "cvae"


def load(results: Path) -> tuple[dict[str, dict], dict[str, float]]:
    card = json.loads((results / "scorecard.json").read_text(encoding="utf-8"))
    rows = {r["label"]: r for r in card["rows"]}
    refs = {}
    with open(results / "summary.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["config"] in ("B0-rf", "B1b-rf"):
                refs[r["config"]] = float(r["macro_f1_mean"])
    return rows, refs


def fig3(rows: dict[str, dict], refs: dict[str, float], out: Path, md: list[str]) -> None:
    f, ax = frame("fig3")
    pts = []
    for name, cfg, col, marker, dx in SERIES3:
        eps = [e for e in EPS_ORDER if e in cfg]
        xs = [EPS_ORDER.index(e) + dx for e in eps]
        ys = [rows[cfg[e]]["tstr_f1"] for e in eps]
        sd = [rows[cfg[e]]["tstr_f1_std"] for e in eps]
        ax.errorbar(xs, ys, yerr=sd, color=COLOR[col], marker=marker, markersize=4, capsize=2, elinewidth=0.7, label=name)
        pts += [(name, e, cfg[e], x, y, s, col, marker) for e, x, y, s in zip(eps, xs, ys, sd)]
    for key, ls, text in (("B0-rf", "--", "pooled real data (B0)"), ("B1b-rf", ":", "pooled real data + SMOTE (B1b)")):
        ax.axhline(refs[key], color=COLOR["gray"], linestyle=ls, linewidth=0.8)
        ax.text(-0.35, refs[key] + 0.004, text, ha="left", va="bottom", fontsize=8, color=COLOR["gray"])
    ax.set_xticks(range(len(EPS_ORDER)), [EPS_LABEL[e] for e in EPS_ORDER])
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_xlabel(r"Privacy budget $\varepsilon$ ($\delta = 10^{-5}$)")
    ax.set_ylabel("TSTR macro-F1 (test)")
    ax.grid(axis="y", linewidth=0.4, alpha=0.5)
    ax.legend(loc="lower right", frameon=False)
    for ext, kw in (("pdf", {}), ("png", {"dpi": 600})):
        f.savefig(out / f"fig3_tstr_vs_eps_reference.{ext}", **kw)
    plt.close(f)

    L = LAYOUT["fig3"]
    md += ["## Hình 3: `fig3_tstr_vs_eps` (TSTR macro-F1 theo ε)", "",
           f"- Trang: **{L['w']:.0f} × {L['h']:.0f} mm**. Khung đồ thị: x từ {L['x0']:.0f} đến {L['x1']:.0f} mm, "
           f"y từ {L['y0']:.0f} (trên) đến {L['y1']:.0f} mm (dưới).",
           frame_md("fig3"),
           f"- Trục y: {L['ylim'][0]}–{L['ylim'][1]}; trục x là 4 hạng mục ε cách đều nhau.", "",
           "**Vạch chia trục**", "", "| Trục | Giá trị / nhãn | X (mm) | Y (mm) |", "|---|---|---|---|"]
    for i, e in enumerate(EPS_ORDER):
        md.append(f"| x | {EPS_LABEL[e]} | {to_mm('fig3', i, L['ylim'][0])[0]:.1f} | {L['y1']:.1f} |")
    for v in (0.1, 0.2, 0.3, 0.4, 0.5):
        md.append(f"| y | {v:.1f} | {L['x0']:.1f} | {to_mm('fig3', 0, v)[1]:.1f} |")
    md += ["", "**Đường tham chiếu** (đường ngang 0.3 mm, màu xám #595959, kéo hết chiều rộng khung đồ thị; kiểu nét ở cột bên)", "",
           "| Đường | Giá trị | Y (mm) | Kiểu nét | Nhãn (đặt sát trên đường, căn trái tại X = 15 mm) |",
           "|---|---|---|---|---|",
           f"| B0 | {refs['B0-rf']:.3f} | {to_mm('fig3', 0, refs['B0-rf'])[1]:.1f} | gạch (dashed) | pooled real data (B0) |",
           f"| B1b | {refs['B1b-rf']:.3f} | {to_mm('fig3', 0, refs['B1b-rf'])[1]:.1f} | chấm (dotted) | "
           "pooled real data + SMOTE (B1b) |", "",
           "**Điểm và thanh sai số** (X, Y là tâm marker; thanh sai số dọc từ Y trên đến Y dưới, có gạch ngang ở hai "
           "đầu rộng 1.4 mm; các điểm cùng chuỗi nối bằng đường liền 0.4 mm)", "",
           "| Chuỗi | ε | Cấu hình | macro-F1 | std | X (mm) | Y (mm) | Y trên (mm) | Y dưới (mm) | Màu | Marker |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, e, cfg, x, y, s, col, marker in pts:
        X, Y = to_mm("fig3", x, y)
        md.append(f"| {name} | {EPS_LABEL[e]} | {cfg} | {y:.3f} | {s:.3f} | {X:.1f} | {Y:.1f} | "
                  f"{to_mm('fig3', x, y + s)[1]:.1f} | {to_mm('fig3', x, y - s)[1]:.1f} | {COLOR[col]} | "
                  f"{MARKER_NAME[marker]} |")
    md += ["", "**Chú giải (legend):** góc dưới bên phải trong khung đồ thị, không viền, 3 dòng theo thứ tự trên, mỗi "
           "dòng gồm một đoạn thẳng có marker giữa và tên chuỗi (8 pt). Xem vị trí trong ảnh tham chiếu.", ""]


def fig4(rows: dict[str, dict], out: Path, md: list[str]) -> None:
    f, ax = frame("fig4")
    pts = []
    for r in rows.values():
        if not r["valid"] or not r.get("bytes_total"):
            continue
        fam = family(r["label"])
        _, col, marker = FAMILY4[fam]
        mb = r["bytes_total"] / 1e6
        ax.scatter(mb, r["tstr_f1"], s=16, marker=marker, linewidths=0.8,
                   facecolors=COLOR[col] if r["pareto"] else "none", edgecolors=COLOR[col], zorder=3)
        pts.append((r["label"], fam, mb, r["tstr_f1"], bool(r["pareto"])))
    for lab, tx, ty in LABELS4:
        r = rows[lab]
        ax.annotate(lab, (r["bytes_total"] / 1e6, r["tstr_f1"]), xytext=(tx, ty), fontsize=8, color="0.2",
                    ha="center", va="center", arrowprops={"arrowstyle": "-", "color": "0.5", "linewidth": 0.5})
    handles = [Line2D([], [], linestyle="none", marker=m, markersize=4.5, markerfacecolor="none",
                      markeredgecolor=COLOR[c], label=t) for t, c, m in FAMILY4.values()]
    handles.append(Line2D([], [], linestyle="none", marker="o", markersize=4.5, color="0.3", label="filled: Pareto front"))
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_xlabel("Total traffic per run (MB, log scale)")
    ax.set_ylabel("TSTR macro-F1 (test)")
    ax.grid(linewidth=0.4, alpha=0.5)
    ax.legend(handles=handles, loc="lower center", frameon=False, ncol=2, bbox_to_anchor=(0.5, 1.0),
              columnspacing=0.8, handletextpad=0.3, borderaxespad=0.3)
    for ext, kw in (("pdf", {}), ("png", {"dpi": 600})):
        f.savefig(out / f"fig4_utility_vs_traffic_reference.{ext}", **kw)
    plt.close(f)

    L = LAYOUT["fig4"]
    md += ["## Hình 4: `fig4_utility_vs_traffic` (macro-F1 theo tổng lưu lượng, trục x logarit)", "",
           f"- Trang: **{L['w']:.0f} × {L['h']:.0f} mm**. Khung đồ thị: x từ {L['x0']:.0f} đến {L['x1']:.0f} mm, "
           f"y từ {L['y0']:.0f} đến {L['y1']:.0f} mm. Chú giải nằm phía trên khung (y khoảng 1–14 mm).",
           frame_md("fig4"),
           f"- Trục x **logarit** từ {L['xlim'][0]} đến {L['xlim'][1]:.0f} MB; trục y {L['ylim'][0]}–{L['ylim'][1]}. "
           "Mọi vị trí dưới đây đã được quy đổi sẵn sang mm, nên chỉ cần đặt hình đúng toạ độ.", "",
           "**Vạch chia trục** (vạch chính có nhãn; vạch phụ của trục x ngắn hơn, không nhãn)", "",
           "| Trục | Giá trị | Nhãn | X (mm) | Y (mm) |", "|---|---|---|---|---|"]
    for v in (1, 10, 100):
        md.append(f"| x chính | {v} | 10^{int(math.log10(v))} | {to_mm('fig4', v, 0.3)[0]:.1f} | {L['y1']:.1f} |")
    minors = [m * 10 ** k for k in (-1, 0, 1, 2) for m in range(2, 10)]
    minors = [v for v in minors if L["xlim"][0] <= v <= L["xlim"][1]]
    md.append("| x phụ | " + ", ".join(f"{v:g}" for v in minors) + " | – | "
              + ", ".join(f"{to_mm('fig4', v, 0.3)[0]:.1f}" for v in minors) + f" | {L['y1']:.1f} |")
    for v in (0.1, 0.2, 0.3, 0.4, 0.5):
        md.append(f"| y | {v:.1f} | {v:.1f} | {L['x0']:.1f} | {to_mm('fig4', 1, v)[1]:.1f} |")
    md += ["", "**Điểm** (X, Y là tâm marker, cỡ marker 1.8 mm; *tô đặc* = nằm trên mặt Pareto, còn lại chỉ có viền)", "",
           "| Cấu hình | Nhóm (chú giải) | MB/lượt | macro-F1 | X (mm) | Y (mm) | Tô đặc | Màu | Marker |",
           "|---|---|---|---|---|---|---|---|---|"]
    for lab, fam, mb, y, filled in sorted(pts, key=lambda p: (p[1], p[2])):
        t, col, marker = FAMILY4[fam]
        X, Y = to_mm("fig4", mb, y)
        md.append(f"| {lab} | {t} | {mb:.2f} | {y:.3f} | {X:.1f} | {Y:.1f} | {'có' if filled else 'không'} | "
                  f"{COLOR[col]} | {MARKER_NAME[marker]} |")
    md += ["", "**Nhãn điểm** (chữ 8 pt, màu xám đậm; đường dẫn mảnh 0.2 mm màu xám nối tâm chữ tới tâm marker)", "",
           "| Nhãn | Tâm chữ X (mm) | Tâm chữ Y (mm) | Đầu đường dẫn tại marker X, Y (mm) |", "|---|---|---|---|"]
    for lab, tx, ty in LABELS4:
        r = rows[lab]
        X, Y = to_mm("fig4", tx, ty)
        px, py = to_mm("fig4", r["bytes_total"] / 1e6, r["tstr_f1"])
        md.append(f"| {lab} | {X:.1f} | {Y:.1f} | {px:.1f}, {py:.1f} |")
    md += ["", "**Chú giải (legend):** phía trên khung đồ thị, 2 cột, không viền: (cột 1) MG, distributed DP · "
           "MG, local DP · MG, no DP; (cột 2) Federated CVAE · filled: Pareto front (một chấm tròn đặc màu xám). "
           "Marker trong chú giải chỉ vẽ viền.", ""]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--results", type=Path, default=Path("../results"))
    ap.add_argument("--out", type=Path, default=Path("huong_dan/tham_chieu"))
    ap.add_argument("--table", type=Path, default=Path("huong_dan/SO_LIEU_HINH_3_4.md"))
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    style()
    rows, refs = load(a.results)
    md = ["# Số liệu và toạ độ để vẽ Hình 3 và Hình 4 bằng ConceptDraw", "",
          "Tự sinh bởi `scripts/make_paper_figures.py` từ `results/scorecard.json` và `results/summary.csv` của dự án; "
          "**không sửa tay**. Chạy lại script nếu kết quả thay đổi.", "",
          "Toạ độ tính bằng **mm từ góc trên bên trái trang**, trục Y hướng **xuống**. Nếu ConceptDraw của nhóm đo Y từ "
          "dưới lên, dùng Y' = (chiều cao trang) − Y. X, Y là **tâm** của hình (pin), không phải góc.", "",
          f"Ảnh tham chiếu cùng khung: `{a.out.as_posix()}/fig3_tstr_vs_eps_reference.png` và "
          f"`{a.out.as_posix()}/fig4_utility_vs_traffic_reference.png` (600 dpi, đúng kích thước trang ở dưới).", ""]
    fig3(rows, refs, a.out, md)
    fig4(rows, a.out, md)
    a.table.write_text("\n".join(md), encoding="utf-8")
    print("written:", a.table.as_posix(), *sorted(p.name for p in a.out.glob("fig[34]_*")))


if __name__ == "__main__":
    main()
