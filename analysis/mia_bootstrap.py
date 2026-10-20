"""Bootstrap confidence intervals for the membership attack on the released FedDP-Marginal tables (reviewer comment 1.8).

The attack of `ppfeddata.mia_marginal` is deterministic: for each seed it fits model A on half H1 and reference B on half H2 and scores every
record of H1 u H2. This script recomputes those per-record scores for the configurations reported in the paper (no DP, MGs-eps1, MGr-eps5,
MGs-eps10), checks that the AUCs equal results/mia_marginal.json, and resamples the records (with replacement, inside each class and
membership group, the same resamples for every configuration so differences are paired) to get 95 % intervals of:
  - the calibrated AUC (mean over classes and over the two directions, averaged over the seeds),
  - the TPR at 1 % FPR,
  - the difference AUC(no DP) - AUC(DP).

Run from the PP-FedData repository root:
    python Latex_FinalCapstone/analysis/mia_bootstrap.py [--n-boot 1000]
Writes Latex_FinalCapstone/analysis/mia_bootstrap.json.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from sklearn.metrics import roc_auc_score, roc_curve  # noqa: E402

from ppfeddata.mia_marginal import default_settings, fit_score  # noqa: E402
from ppfeddata.mia_model import halves  # noqa: E402
from ppfeddata.utils import load_config  # noqa: E402

LABELS = {"none": "MGs-nodp", "eps1": "MGs-eps1", "eps5": "MGr-eps5", "eps10": "MGs-eps10"}  # round R headline (final_report 9.12)


def tpr_at(score, member, fpr=0.01):
    f, t, _ = roc_curve(member, score)
    return float(np.interp(fpr, f, t))


def metrics(sa, sb, in_a, y, k, idx=None):
    """Calibrated AUC (mean over classes of the two directions) and TPR at 1 % FPR, on the rows `idx` (all rows if None)."""
    if idx is not None:
        sa, sb, in_a, y = sa[idx], sb[idx], in_a[idx], y[idx]
    aucs = []
    for c in range(k):
        m = y == c
        if m.any() and 0 < in_a[m].sum() < m.sum():
            aucs.append(0.5 * (roc_auc_score(in_a[m], sa[m]) + roc_auc_score(~in_a[m], sb[m])))
    return float(np.mean(aucs)), 0.5 * (tpr_at(sa, in_a) + tpr_at(sb, ~in_a))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--n-boot", type=int, default=1000)
    a = ap.parse_args()
    cfg = load_config()
    from ppfeddata.data.preprocess import processed_dir

    d = processed_dir(cfg)
    schema = json.loads((d / "feature_schema.json").read_text(encoding="utf-8"))
    tr = np.load(d / "train.npz", allow_pickle=True)
    X, y = tr["X"], tr["y"].astype(np.int64)
    K, delta, k = int(cfg["fl"]["num_clients"]), float(cfg["dp"]["delta"]), len(schema["label_map"])
    settings = default_settings(cfg)
    stored = json.loads((ROOT / "results" / "mia_marginal.json").read_text(encoding="utf-8"))["configs"]
    seeds = [int(s) for s in cfg["seeds"]]

    scores = {}                                              # (label, seed) -> (sa, sb, in_a, y_keep)
    for key, label in LABELS.items():
        setting = settings[label]
        eps = None if setting["eps"] is None else float(setting["eps"])
        for s in seeds:
            t0 = time.time()
            h1, h2 = halves(len(y), s)
            keep = np.concatenate([h1, h2])
            La = -fit_score(X, y, h1, schema, eps, delta, setting, K, s)[keep]
            Lb = -fit_score(X, y, h2, schema, eps, delta, setting, K, s + 1)[keep]
            in_a = np.zeros(len(keep), bool)
            in_a[: len(h1)] = True
            sa, sb = Lb - La, La - Lb
            auc, tpr = metrics(sa, sb, in_a, y[keep], k)
            ref = stored[label]["per_seed"][seeds.index(s)]["calibrated"]["auc_mean"]
            print(f"{label} seed {s}: AUC {auc:.6f} (stored {ref:.6f}), TPR@1% {tpr:.4f}, {time.time() - t0:.0f}s", flush=True)
            if abs(auc - ref) > 1e-6:                            # the JSON stores the AUC rounded to 8 decimals
                sys.exit(f"recomputed AUC differs from results/mia_marginal.json for {label} seed {s}")
            scores[(key, s)] = (sa, sb, in_a, y[keep])

    rng = np.random.default_rng(20261014)
    boot = {key: {"auc": [], "tpr": []} for key in LABELS}
    for b in range(a.n_boot):
        per = {key: {"auc": [], "tpr": []} for key in LABELS}
        for s in seeds:
            _, _, in_a, ys = scores[("none", s)]                 # the same records for every configuration of a seed
            idx = np.concatenate([rng.choice(np.flatnonzero((ys == c) & (in_a == g)), ((ys == c) & (in_a == g)).sum(), replace=True)
                                  for c in range(k) for g in (True, False) if ((ys == c) & (in_a == g)).any()])
            for key in LABELS:
                sa, sb, ia, yy = scores[(key, s)]
                auc, tpr = metrics(sa, sb, ia, yy, k, idx)
                per[key]["auc"].append(auc)
                per[key]["tpr"].append(tpr)
        for key in LABELS:
            boot[key]["auc"].append(np.mean(per[key]["auc"]))
            boot[key]["tpr"].append(np.mean(per[key]["tpr"]))
        if (b + 1) % 100 == 0:
            print(f"bootstrap {b + 1}/{a.n_boot}", flush=True)

    def ci(v):
        return [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))]

    out = {"n_boot": a.n_boot, "seeds": seeds, "resampling": "records with replacement inside each class x membership group, paired across configurations",
           "configs": {}}
    point = {key: (np.mean([metrics(*scores[(key, s)], k)[0] for s in seeds]), np.mean([metrics(*scores[(key, s)], k)[1] for s in seeds]))
             for key in LABELS}
    for key, label in LABELS.items():
        auc = np.array(boot[key]["auc"])
        tpr = np.array(boot[key]["tpr"])
        diff = np.array(boot["none"]["auc"]) - auc
        out["configs"][label] = {"auc": float(point[key][0]), "auc_ci95": ci(auc), "tpr_1pct": float(point[key][1]), "tpr_1pct_ci95": ci(tpr),
                                 **({} if key == "none" else {"auc_nodp_minus_this": float(point["none"][0] - point[key][0]),
                                                              "diff_ci95": ci(diff), "diff_excludes_zero": bool(ci(diff)[0] > 0 or ci(diff)[1] < 0)})}
    p = Path(__file__).with_name("mia_bootstrap.json")
    p.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(json.dumps(out["configs"], indent=1))


if __name__ == "__main__":
    main()
