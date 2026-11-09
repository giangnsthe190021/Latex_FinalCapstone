"""Appendix tables of the thesis, written from results/scorecard.json so that no number is typed by hand.

Usage (from the Latex_FinalCapstone folder):
    python scripts/make_thesis_tables.py --results ../results

Outputs: chapters/back/scorecard_table.tex, chapters/back/eps_honest_table.tex
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def num(value) -> float | None:
    if value is None:
        return None
    if isinstance(value, str):
        if value in ("inf", "Infinity"):
            return math.inf
        try:
            return float(value)
        except ValueError:
            return None
    return float(value)


def eps_text(value) -> str:
    v = num(value)
    if v is None:
        return "n/a"
    return r"$\infty$" if math.isinf(v) else f"{v:.2f}"


def gain_text(value) -> str:
    v = num(value)
    if v is None:
        return "n/a"
    return "0.000" if abs(v) < 0.0005 else f"{v:+.3f}".replace("-", "$-$")


def mb(value) -> str:
    v = num(value)
    return "n/a" if v is None else f"{v / 1e6:.2f}"


def scorecard_table(rows: list[dict]) -> str:
    head = (r"\textbf{Configuration} & \textbf{Clf.} & \textbf{Front} & \textbf{Macro-F1} & \textbf{Binary F1} & \textbf{Rare recall} & "
            r"\textbf{TAug gain} & $\boldsymbol{\varepsilon}$ & $\boldsymbol{\varepsilon}$ \textbf{($h{=}1$)} & \textbf{SecAgg$^+$} & "
            r"\textbf{MB/round} & \textbf{Rounds} & \textbf{MB/run} \\")
    out = [r"\begin{landscape}", r"\scriptsize", r"\begin{longtable}{lccccccccccc c}",
           r"\caption{Scorecard of all configurations (TSTR on the real test split, classifier chosen on validation). Configurations marked with a dagger use statistics outside $\varepsilon$ and are excluded from the Pareto front.}\label{tab:app_scorecard}\\",
           r"\toprule", head, r"\midrule", r"\endfirsthead", r"\toprule", head, r"\midrule", r"\endhead", r"\bottomrule", r"\endfoot"]
    for r in rows:
        if r.get("tstr_f1") is None or not r.get("tstr_classifier"):
            continue
        name = r["label"] + ("" if r.get("valid") else r" $\dagger$")
        f1 = f"${r['tstr_f1']:.3f} \\pm {r['tstr_f1_std']:.3f}$"
        out.append(" & ".join([name, r["tstr_classifier"].upper(), "yes" if r.get("pareto") else "no", f1, f"{r['bin_f1']:.3f}", f"{r['rare_recall']:.3f}",
                               gain_text(r.get("taug_gain")), eps_text(r.get("eps")), eps_text(r.get("eps_one_honest")), "yes" if r.get("secagg") else "no",
                               mb(r.get("bytes_per_round")), f"{int(r['rounds'])}", mb(r.get("bytes_total"))]) + r" \\")
    out += [r"\end{longtable}", r"\end{landscape}", ""]
    return "\n".join(out)


def honest_table(rows: list[dict]) -> str:
    wanted = [r for r in rows if r.get("dp_mode") == "distributed" and r.get("eps_honest")]
    out = [r"\begin{longtable}{lccccc}",
           r"\caption{Effective $\varepsilon$ of the distributed configurations as a function of the number of honest gateways $h$ ($K = 5$)}\label{tab:app_honest}\\",
           r"\toprule", r"\textbf{Configuration} & $h = 1$ & $h = 2$ & $h = 3$ & $h = 4$ & $h = 5$ \\", r"\midrule", r"\endfirsthead", r"\toprule",
           r"\textbf{Configuration} & $h = 1$ & $h = 2$ & $h = 3$ & $h = 4$ & $h = 5$ \\", r"\midrule", r"\endhead", r"\bottomrule", r"\endfoot"]
    for r in wanted:
        curve = r["eps_honest"]
        out.append(r["label"] + " & " + " & ".join(f"{float(curve[str(h)]):.2f}" for h in range(1, 6)) + r" \\")
    out += [r"\end{longtable}", ""]
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=Path("../results"))
    args = parser.parse_args()
    rows = json.loads((args.results / "scorecard.json").read_text(encoding="utf8"))["rows"]
    Path("chapters/back/scorecard_table.tex").write_text(scorecard_table(rows), encoding="utf8")
    Path("chapters/back/eps_honest_table.tex").write_text(honest_table(rows), encoding="utf8")


if __name__ == "__main__":
    main()
