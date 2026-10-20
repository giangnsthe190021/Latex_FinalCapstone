"""Decision rule (9) for the RQ2 comparisons of Table IV (reviewer comment 1.1).

For each budget, FedDP-Marginal with client-side noise (MGl, the CVAE's trust model) and with distributed noise (MG) is compared with the best
CVAE configuration, each with the classifier chosen on validation (the `tstr_config` of results/scorecard.json). The difference of test
macro-F1 (and of rare-class recall) is judged with the study's rule: the 95 % paired-bootstrap interval excludes 0 AND |difference| exceeds
the larger seed standard deviation; the bootstrap is repeated over whole TCP streams. Same code as the report (ppfeddata.eval.compare), same
resamples (seed 0, n from the config).

Run from the PP-FedData repository root:
    python Latex_FinalCapstone/analysis/rule9_rq2.py
Writes Latex_FinalCapstone/analysis/rule9_rq2.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from ppfeddata.eval.compare import MACRO_F1, PairedBootstrap, compare_runs, recall_of  # noqa: E402
from ppfeddata.eval.runs import load_predictions, run_id  # noqa: E402
from ppfeddata.interpret import BOOT_SEED, load_test_split  # noqa: E402
from ppfeddata.utils import load_config  # noqa: E402

PAIRS = {  # budget: (CVAE label, MGl label, MG distributed label), as in Table IV (round R: final_report 9.9b, 9.12)
    "1": ("M1-eps1", "MGl-eps1", "MGs-eps1"),
    "5": ("M3o-eps5", "MGl-eps5", "MGr-eps5"),
    "10": ("M1o-eps10", "MGl-eps10", "MGs-eps10"),
}
RARE = ("DELAYED", "SYN", "INVALID", "WILL")


def main() -> None:
    cfg = load_config()
    card = {r["label"]: r for r in json.loads((ROOT / "results" / "scorecard.json").read_text(encoding="utf-8"))["rows"]}
    y, streams, _, classes = load_test_split(cfg)
    k, mode, seeds = len(classes), cfg["label_mode"], [int(s) for s in cfg["seeds"]]
    nb = int(cfg["eval"]["bootstrap"])
    names = sorted({card[lab]["tstr_config"] for trio in PAIRS.values() for lab in trio})
    preds = {(n, s): load_predictions(cfg, run_id(n, s, mode))["y_pred"] for n in names for s in seeds}
    boots = {"rows": PairedBootstrap(y, k, nb, BOOT_SEED, "rows"), "streams": PairedBootstrap(y, k, nb, BOOT_SEED, "streams", streams)}
    for b in boots.values():
        b.add(preds)
    rare = recall_of(*[classes.index(c) for c in RARE])
    out = {"n_boot": nb, "boot_seed": BOOT_SEED, "seeds": seeds, "rule": "CI95 excludes 0 and |delta| > max seed std (ddof 0)", "comparisons": []}
    for eps, (cvae, mgl, mgd) in PAIRS.items():
        for mg in (mgl, mgd):
            a, b = card[mg]["tstr_config"], card[cvae]["tstr_config"]
            ka, kb = [(a, s) for s in seeds], [(b, s) for s in seeds]
            row = {"eps": eps, "a": mg, "b": cvae, "a_run": a, "b_run": b}
            for mname, metric in (("macro_f1", MACRO_F1), ("rare_recall", rare)):
                c = compare_runs(boots["rows"], ka, kb, metric)
                st = compare_runs(boots["streams"], ka, kb, metric)
                row[mname] = {x: c[x] for x in ("delta", "lo", "hi", "sigma", "mean_a", "mean_b", "effect")}
                row[mname]["stream"] = {x: st[x] for x in ("lo", "hi", "effect")}
            out["comparisons"].append(row)
            m = row["macro_f1"]
            print(f"eps {eps:>2}: {mg:10s} - {cvae:17s} macro-F1 {m['delta']:+.3f} [{m['lo']:+.3f}, {m['hi']:+.3f}] sd {m['sigma']:.3f} "
                  f"-> {m['effect']} (streams: {m['stream']['effect']}); rare recall {row['rare_recall']['delta']:+.3f} -> {row['rare_recall']['effect']}")
    Path(__file__).with_name("rule9_rq2.json").write_text(json.dumps(out, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
