"""Figures of Chapter 4 of the thesis that do not already exist in results/figures (Times New Roman, text width).

Every number is read from the result files of the PP-FedData repository; nothing is typed by hand.

Usage (from the Latex_FinalCapstone folder):
    python scripts/make_thesis_figures.py --results ../results --mia analysis/mia_bootstrap.json

    python scripts/make_thesis_figures.py --results ../results --only tstr_vs_eps     # one figure

Inputs:  <results>/scorecard.json (epsilon by honest clients, the TSTR configuration and test macro-F1 of each row),
         <results>/summary.csv (per-class F1, validation macro-F1, the real-data references B0 and B1b),
         analysis/mia_bootstrap.json (AUC of the attack on the released tables with its interval).
Outputs: graphics/chapter4/tstr_vs_eps.pdf, graphics/chapter4/f1_vs_traffic.pdf, graphics/chapter4/eps_by_honest.pdf,
         graphics/chapter4/mia_tables.pdf, graphics/chapter4/per_class_f1.pdf
The other two figures of Chapter 4, f1_by_config.png and partition_alpha0.5_seed0.png, are copies of the files of the same name
in <results>/figures, written by `python -m ppfeddata.cli aggregate` and by the B3 run.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

BLUE, RED, PURPLE, GRAY, GREEN = "#1F77B4", "#D62728", "#9467BD", "#595959", "#2CA02C"
EPS = (1.0, 5.0, 10.0)
MAIN_MG = {1.0: "MGs-eps1", 5.0: "MGr-eps5", 10.0: "MGs-eps10"}      # the framework's configurations (Chapter 4, MG-eps1/5/10)
FIGURES = ("tstr_vs_eps", "f1_vs_traffic", "eps_by_honest", "mia_tables", "per_class_f1")
OUT = Path("graphics/chapter4")
PREVIEW: Path | None = None


def save(fig, name: str) -> None:
    fig.savefig(OUT / f"{name}.pdf")
    if PREVIEW:
        fig.savefig(PREVIEW / f"{name}.png", dpi=110)
    plt.close(fig)


def setup() -> None:
    plt.rcParams.update({
        "font.family": "Times New Roman", "mathtext.fontset": "stix", "font.size": 11, "axes.labelsize": 11,
        "xtick.labelsize": 10, "ytick.labelsize": 10, "legend.fontsize": 10, "axes.spines.top": False,
        "axes.spines.right": False, "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "pdf.fonttype": 42,
    })


def cvae_route(rows: dict, val: dict, eps: float) -> dict:
    """The valid CVAE route (M1 or M3, any search round) whose chosen classifier has the highest validation macro-F1 at this
    epsilon, as in ppfeddata.interpret_report._pivot_facts: chosen on validation, never on test (SPEC_DEVIATIONS R.13)."""
    cands = [r for r in rows.values() if r.get("valid") and not r.get("reference") and r.get("dp") and r.get("method") in ("M1", "M3")
             and abs(float(r.get("eps_target") or 0) - eps) < 1e-9 and r.get("tstr_config") in val]
    return max(cands, key=lambda r: val[r["tstr_config"]])


def tstr_vs_eps(rows: dict, summary: Path) -> None:
    with summary.open(encoding="utf8") as f:
        table = {r["config"]: r for r in csv.DictReader(f)}
    val = {c: float(r["val_macro_f1_mean"]) for c, r in table.items() if r.get("val_macro_f1_mean") not in (None, "", "nan")}
    xs = {1.0: 0, 5.0: 1, 10.0: 2, "inf": 3}
    series = [("FedDP-Marginal, distributed DP", [MAIN_MG[e] for e in EPS] + ["MGs-nodp"], BLUE, "o", -0.06),
              ("FedDP-Marginal, client-side DP", [f"MGl-eps{e:g}" for e in EPS], GREEN, "s", 0.0),
              ("Federated CVAE (route chosen on validation)", [cvae_route(rows, val, e)["label"] for e in EPS] + ["B3"], RED, "^", 0.06)]
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    for name, ref, color in (("B1b-rf", "pooled real data + SMOTE (B1b)", GRAY), ("B0-rf", "pooled real data (B0)", GRAY)):
        y = float(table[name]["macro_f1_mean"])
        ax.axhline(y, color=color, linewidth=0.9, linestyle=":" if name.startswith("B1b") else "--")
        ax.text(-0.35, y + 0.004, ref, ha="left", va="bottom", fontsize=10, color=color)
    for label, configs, color, marker, dx in series:
        pts = [(xs[EPS[i] if i < 3 else "inf"] + dx, rows[c]["tstr_f1"], rows[c]["tstr_f1_std"]) for i, c in enumerate(configs)]
        ax.errorbar([p[0] for p in pts], [p[1] for p in pts], yerr=[p[2] for p in pts], color=color, marker=marker, markersize=5,
                    linewidth=1.4, capsize=2.5, elinewidth=0.9, label=label)
    ax.set_xticks(range(4))
    ax.set_xticklabels(["1", "5", "10", r"$\infty$"])
    ax.set_xlim(-0.4, 3.4)
    ax.set_ylim(0.1, 0.55)
    ax.set_xlabel(r"Privacy budget $\varepsilon$ ($\delta = 10^{-5}$)")
    ax.set_ylabel("TSTR macro-F1 (test)")
    ax.grid(axis="y", color="0.88", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    save(fig, "tstr_vs_eps")


def f1_vs_traffic(rows: dict) -> None:
    """TSTR macro-F1 against the total traffic of a run (bytes summed over the whole federation), one point per valid scorecard
    row that has a traffic count; filled markers are the rows on the Pareto front of the scorecard."""
    from matplotlib.lines import Line2D

    groups = [("MG, distributed DP", BLUE, "o", lambda r: r["method"] == "MG" and r.get("dp_mode") == "distributed"),
              ("MG, client-side DP", GREEN, "s", lambda r: r["method"] == "MG" and r.get("dp_mode") == "local"),
              ("MG, no DP", PURPLE, "D", lambda r: r["method"] == "MG" and not r.get("dp")),
              ("Federated CVAE", RED, "^", lambda r: r["method"] in ("B3", "M1", "M2", "M3"))]
    pts = [r for r in rows.values() if r.get("valid") and not r.get("reference") and r.get("bytes_total")]
    fig, ax = plt.subplots(figsize=(5.6, 4.3))
    for _, color, marker, keep in groups:
        for r in (r for r in pts if keep(r)):
            ax.plot(r["bytes_total"] / 1e6, r["tstr_f1"], marker=marker, markersize=6, linestyle="none", color=color,
                    markerfacecolor=color if r.get("pareto") else "none", markeredgewidth=1.3)
    notes = {"MGs-eps10": (2.2, 0.445), "MGr-eps5": (2.2, 0.405), "MGs-eps1": (2.2, 0.355), "B3": (45, 0.465),
             "M2": (210, 0.37), "M3o-eps5": (3.5, 0.29), "M1-eps1": (30, 0.12)}
    for label, (tx, ty) in notes.items():
        r = rows[label]
        ax.annotate(label, (r["bytes_total"] / 1e6, r["tstr_f1"]), xytext=(tx, ty), textcoords="data", fontsize=10, color="0.15",
                    ha="left", va="center", arrowprops={"arrowstyle": "-", "color": "0.55", "linewidth": 0.7, "shrinkA": 0, "shrinkB": 3})
    ax.set_xscale("log")
    ax.set_xlim(0.25, 450)
    ax.set_ylim(0.05, 0.5)
    ax.set_xlabel("Total traffic per run (MB, log scale)")
    ax.set_ylabel("TSTR macro-F1 (test)")
    ax.grid(color="0.88", linewidth=0.6)
    ax.set_axisbelow(True)
    handles = [Line2D([], [], marker=m, linestyle="none", color=c, markerfacecolor="none" if i != 2 else c, markeredgewidth=1.3,
                      markersize=6, label=n) for i, (n, c, m, _) in enumerate(groups)]
    handles.append(Line2D([], [], marker="o", linestyle="none", color="0.35", markersize=6, label="filled: Pareto front"))
    ax.legend(handles=handles, frameon=False, ncol=2, loc="lower center", bbox_to_anchor=(0.5, 1.0), columnspacing=1.2, handletextpad=0.4)
    fig.tight_layout()
    save(fig, "f1_vs_traffic")


def eps_by_honest(rows: dict) -> None:
    series = [("MGs-eps10", "target 10 (MGs)", PURPLE, "s"), ("MGr-eps5", "target 5 (MGr)", RED, "^"), ("MGs-eps1", "target 1 (MGs)", BLUE, "o")]
    fig, ax = plt.subplots(figsize=(5.6, 3.3))
    for key, label, color, marker in series:
        curve = {int(h): float(v) for h, v in rows[key]["eps_honest"].items() if int(h) <= 5}
        hs = sorted(curve)
        ys = [curve[h] for h in hs]
        ax.plot(hs, ys, color=color, marker=marker, markersize=5, linewidth=1.4, label=label)
        ax.annotate(f"{ys[0]:.1f}", (hs[0], ys[0]), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=10, color="0.15")
    ax.set_yscale("log")
    ax.set_yticks([1, 2, 5, 10, 20, 50])
    ax.set_yticklabels(["1", "2", "5", "10", "20", "50"])
    ax.set_xticks(range(1, 6))
    ax.set_xlabel("Honest gateways $h$ of $K = 5$")
    ax.set_ylabel(r"Effective $\varepsilon$ (log scale)")
    ax.grid(axis="y", color="0.88", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    save(fig, "eps_by_honest")


def mia_tables(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf8"))["configs"]
    items = [("MGs-eps1", r"DP, $\varepsilon = 1$ (MGs)"), ("MGr-eps5", r"DP, $\varepsilon = 5$ (MGr)"), ("MGs-eps10", r"DP, $\varepsilon = 10$ (MGs)"), ("MGs-nodp", "No DP (MGs-nodp)")]
    fig, ax = plt.subplots(figsize=(5.6, 2.5))
    for y, (key, _) in enumerate(items):
        auc, (lo, hi) = data[key]["auc"], data[key]["auc_ci95"]
        ax.plot([lo, hi], [y, y], color=BLUE, linewidth=1.4, solid_capstyle="round")
        ax.plot([auc], [y], marker="o", markersize=6, color=BLUE)
        ax.annotate(f"{auc:.3f}", (hi, y), xytext=(6, 0), textcoords="offset points", va="center", fontsize=10, color="0.15")
    ax.axvline(0.5, color=GRAY, linewidth=0.8, linestyle=":")
    ax.axvline(0.55, color=GRAY, linewidth=0.8, linestyle="--")
    ax.text(0.501, len(items) - 0.42, "chance", ha="left", va="bottom", fontsize=10, color=GRAY)
    ax.text(0.551, len(items) - 0.42, "detection threshold", ha="left", va="bottom", fontsize=10, color=GRAY)
    ax.set_yticks(range(len(items)))
    ax.set_yticklabels([label for _, label in items])
    ax.set_ylim(-0.5, len(items) - 0.1)
    ax.set_xlim(0.49, 0.60)
    ax.set_xlabel("Calibrated membership-inference AUC (95% bootstrap interval)")
    ax.grid(axis="x", color="0.88", linewidth=0.6)
    ax.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "mia_tables")


def per_class_f1(rows: dict, summary: Path) -> None:
    with summary.open(encoding="utf8") as f:
        table = {r["config"]: r for r in csv.DictReader(f)}
    classes = ["NORMAL", "BCF", "DELAYED", "SYN", "INVALID", "WILL"]
    series = [("B0-rf", "Real data only (B0, RF)", GRAY), (rows["B3"]["tstr_config"], "CVAE, no DP (B3)", PURPLE),
              (rows["M3o-eps5"]["tstr_config"], r"CVAE, $\varepsilon = 5$ (M3o)", RED), (rows["MGr-eps5"]["tstr_config"], r"FedDP-Marginal, $\varepsilon = 5$ (MGr)", BLUE)]
    fig, ax = plt.subplots(figsize=(6.0, 3.3))
    width = 0.19
    for i, (config, label, color) in enumerate(series):
        xs = [c + (i - 1.5) * (width + 0.015) for c in range(len(classes))]
        ax.bar(xs, [float(table[config][f"f1_{c}_mean"]) for c in classes], width=width, color=color, label=label, linewidth=0)
    ax.set_xticks(range(len(classes)))
    ax.set_xticklabels(classes)
    ax.set_ylabel("Test F1 of the class")
    ax.set_ylim(0, 0.75)
    ax.grid(axis="y", color="0.88", linewidth=0.6)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.2), columnspacing=1.2, handlelength=1.2)
    fig.tight_layout()
    save(fig, "per_class_f1")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=Path("../results"))
    parser.add_argument("--mia", type=Path, default=Path("analysis/mia_bootstrap.json"))
    parser.add_argument("--preview", type=Path, default=None, help="also write PNG copies to this folder")
    parser.add_argument("--only", nargs="+", choices=FIGURES, default=list(FIGURES), help="figures to write (default: all)")
    args = parser.parse_args()
    global PREVIEW
    PREVIEW = args.preview
    OUT.mkdir(parents=True, exist_ok=True)
    setup()
    rows = {r["label"]: r for r in json.loads((args.results / "scorecard.json").read_text(encoding="utf8"))["rows"]}
    if "tstr_vs_eps" in args.only:
        tstr_vs_eps(rows, args.results / "summary.csv")
    if "f1_vs_traffic" in args.only:
        f1_vs_traffic(rows)
    if "eps_by_honest" in args.only:
        eps_by_honest(rows)
    if "mia_tables" in args.only:
        mia_tables(args.mia)
    if "per_class_f1" in args.only:
        per_class_f1(rows, args.results / "summary.csv")


if __name__ == "__main__":
    main()
