"""Mock-up of Fig. 2 (three-release protocol) in one IEEE column, 88 x 47 mm, for redrawing it in ConceptDraw.

It is a guide, not the figure of the paper (the diagrams are drawn in ConceptDraw). It fixes what the review of 14/10/2026 found in the
current Fig. 2: every label >= 8 pt Times New Roman, T* instead of T, the Skellam noise share shown, and the drawing fitted to one column
instead of a page-wide float that is half empty.

Usage (from the Latex_FinalCapstone folder):
    python scripts/make_fig2_mockup.py
Writes huong_dan/minh_hoa/fig2_mot_cot_88x47mm.pdf and .png (600 dpi).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

MM = 1 / 25.4
W, H = 88.0, 47.0
GW = ("#DCE9F7", "#1F4E79")          # gateway boxes: fill, border
SA = ("#D9F0EC", "#11736B")          # SecAgg+
SV = ("#F8DEDA", "#9C2B1F")          # server
ROWS = [(6.0, 17.0), (21.0, 32.0), (36.0, 47.0)]   # top, bottom (mm from the top)
LEFT, MID, RIGHT = (0.5, 33.5), (37.0, 51.0), (54.5, 87.5)


def style() -> None:
    plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman"], "font.size": 8,
                         "mathtext.fontset": "custom", "mathtext.rm": "Times New Roman", "mathtext.it": "Times New Roman:italic",
                         "mathtext.bf": "Times New Roman:bold", "pdf.fonttype": 42})


def box(ax, x, y, fill, edge, lw=0.75):
    (x0, x1), (y0, y1) = x, y
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=1.5",
                                facecolor=fill, edgecolor=edge, linewidth=lw))


def text(ax, x, y, lines, bold_first=True):
    n = len(lines)
    for i, s in enumerate(lines):
        ax.text(x, y + (i - (n - 1) / 2) * 3.1, s, ha="center", va="center", fontsize=8,
                fontweight="bold" if (bold_first and i == 0) else "normal")


def arrow(ax, p, q, dashed=False, color="black"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=6, linewidth=0.75, color=color,
                                 linestyle=(0, (3, 2)) if dashed else "-", shrinkA=0, shrinkB=0))


def main() -> None:
    style()
    fig = plt.figure(figsize=(W * MM, H * MM))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    # column titles
    ax.text(sum(LEFT) / 2, 2.6, "Gateways $k = 1, \\ldots, K$", ha="center", va="center", fontsize=8, fontweight="bold")
    ax.text(sum(MID) / 2, 2.6, "SecAgg$^{+}$", ha="center", va="center", fontsize=8, fontweight="bold")
    ax.text(sum(RIGHT) / 2, 2.6, "Server (no extra $\\varepsilon$)", ha="center", va="center", fontsize=8, fontweight="bold")
    left = [["Release 1", "1-way tables per class", "fine bins + share $\\xi_k$"],
            ["Release 2", "2-way tables, 666 pairs,", "coarse, pooled + share $\\xi_k$"],
            ["Release 3", "(root, $y$), (parent, child, $y$)", "37 tables + share $\\xi_k$"]]
    right = [["noisy histograms", "$\\rightarrow$ coarse cut points"],
             ["noisy mutual information", "$\\rightarrow$ Chow–Liu tree $T^{\\star}$"],
             ["conditional tables", "$\\rightarrow$ sample along $T^{\\star}$"]]
    for (y0, y1), lt, rt in zip(ROWS, left, right):
        box(ax, LEFT, (y0, y1), *GW)
        text(ax, sum(LEFT) / 2, (y0 + y1) / 2, lt)
        box(ax, RIGHT, (y0, y1), *SV)
        text(ax, sum(RIGHT) / 2, (y0 + y1) / 2, rt, bold_first=False)
        ym = (y0 + y1) / 2
        arrow(ax, (LEFT[1], ym), (MID[0], ym))
        arrow(ax, (MID[1], ym), (RIGHT[0], ym))
    box(ax, MID, (ROWS[0][0], ROWS[-1][1]), *SA)
    # the SecAgg+ text sits inside the row bands, so the dashed broadcasts (in the gaps) never cross it
    for (y0, y1), lines in zip(ROWS, (["sum", "mod $2^{32}$"], ["uint32,", "exact"], ["no", "rounding"])):
        text(ax, sum(MID) / 2, (y0 + y1) / 2, lines, bold_first=False)
    # broadcasts back to the gateways (dashed), in the gaps between rows; labels in the free gap on the right
    for (r_top, r_bot), nxt, lab in ((ROWS[0], ROWS[1], "cut points"), (ROWS[1], ROWS[2], "tree $T^{\\star}$")):
        yg = (r_bot + nxt[0]) / 2
        arrow(ax, (RIGHT[0] + 4, r_bot), (LEFT[1] - 6, nxt[0]), dashed=True, color="#2E7D32")
        ax.text(RIGHT[0] + 18, yg, lab, ha="center", va="center", fontsize=8, style="italic", color="#2E7D32")
    out = Path("huong_dan/minh_hoa")
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / "fig2_mot_cot_88x47mm.pdf")
    fig.savefig(out / "fig2_mot_cot_88x47mm.png", dpi=600)
    print("written:", *(p.as_posix() for p in sorted(out.glob("fig2_*"))))


if __name__ == "__main__":
    main()
