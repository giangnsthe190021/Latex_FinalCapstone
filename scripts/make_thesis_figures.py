"""Figures of Chapter 4 of the thesis that do not already exist in results/figures (Times New Roman, text width).

Every number is read from the result files of the PP-FedData repository; nothing is typed by hand.

Usage (from the Latex_FinalCapstone folder):
    python scripts/make_thesis_figures.py --results ../results --mia analysis/mia_bootstrap.json

Inputs:  <results>/scorecard.json (epsilon by honest clients, the TSTR configuration of each row),
         <results>/summary.csv (per-class F1),
         analysis/mia_bootstrap.json (AUC of the attack on the released tables with its interval).
Outputs: graphics/chapter4/eps_by_honest.pdf, graphics/chapter4/mia_tables.pdf, graphics/chapter4/per_class_f1.pdf
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

BLUE, RED, PURPLE, GRAY = "#1F77B4", "#D62728", "#9467BD", "#595959"
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
    args = parser.parse_args()
    global PREVIEW
    PREVIEW = args.preview
    OUT.mkdir(parents=True, exist_ok=True)
    setup()
    rows = {r["label"]: r for r in json.loads((args.results / "scorecard.json").read_text(encoding="utf8"))["rows"]}
    eps_by_honest(rows)
    mia_tables(args.mia)
    per_class_f1(rows, args.results / "summary.csv")


if __name__ == "__main__":
    main()
