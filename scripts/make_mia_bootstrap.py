"""Bootstrap intervals of the membership attack on the released FedDP-Marginal tables (Table 4.15, Figure 4.x).

Writes analysis/mia_bootstrap.json. The attack is the one of ppfeddata.mia_marginal (log-likelihood under the released
tables, calibrated by a reference model fitted on the other half of the training pool, mean over the two directions);
it is deterministic, so the point estimates equal results/mia_marginal.json. The interval resamples records with
replacement inside each class x membership group of each seed, with the same resampled records for every
configuration (paired), and averages the calibrated AUC (mean over classes) and the TPR at 1% FPR over the seeds.

    python scripts/make_mia_bootstrap.py --repo .. --out analysis/mia_bootstrap.json

Run from the thesis folder with the PP-FedData package installed (pip install -e <repo>) and the processed data present.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np

CONFIGS = ["MGs-nodp", "MGs-eps1", "MGr-eps5", "MGs-eps10"]


def scores(X, y, schema, setting, K, delta, seed):
    """Calibrated scores of both directions for one configuration and one seed (as in mia_marginal.run_one)."""
    from ppfeddata.mia_marginal import fit_score
    from ppfeddata.mia_model import halves

    h1, h2 = halves(len(y), seed)
    keep = np.concatenate([h1, h2])
    eps = None if setting["eps"] is None else float(setting["eps"])
    La = -fit_score(X, y, h1, schema, eps, delta, setting, K, seed)[keep]
    Lb = -fit_score(X, y, h2, schema, eps, delta, setting, K, seed + 1)[keep]
    in_a = np.zeros(len(keep), bool)
    in_a[: len(h1)] = True
    return Lb - La, La - Lb, in_a, y[keep]


def stats(sa, sb, in_a, yk, classes):
    """Calibrated AUC (mean over classes, mean of the two directions) and TPR at 1% FPR, as in mia_model.attack."""
    from ppfeddata.mia_model import class_auc, tpr_at

    d1, d2 = class_auc(sa, in_a, yk, classes), class_auc(sb, ~in_a, yk, classes)
    auc = float(np.mean([0.5 * (d1[c] + d2[c]) for c in d1 if c in d2]))
    tpr = 0.5 * (tpr_at(sa, in_a, 0.01) + tpr_at(sb, ~in_a, 0.01))
    return auc, tpr


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path(".."), help="PP-FedData repository (for configs/ and data/)")
    ap.add_argument("--out", type=Path, default=Path("analysis/mia_bootstrap.json"))
    ap.add_argument("--n-boot", type=int, default=1000)
    ap.add_argument("--rng", type=int, default=0, help="seed of the bootstrap resampling")
    a = ap.parse_args()
    out = a.out.resolve()
    os.chdir(a.repo)

    from ppfeddata.data.preprocess import processed_dir
    from ppfeddata.mia_marginal import default_settings
    from ppfeddata.utils import load_config

    cfg = load_config(None)
    settings = default_settings(cfg)
    d = processed_dir(cfg)
    schema = json.loads((d / "feature_schema.json").read_text(encoding="utf-8"))
    classes = [c for c, _ in sorted(schema["label_map"].items(), key=lambda kv: kv[1])]
    tr = np.load(d / "train.npz", allow_pickle=True)
    X, y = tr["X"], tr["y"].astype(np.int64)
    K, delta, seeds = int(cfg["fl"]["num_clients"]), float(cfg["dp"]["delta"]), [int(s) for s in cfg["seeds"]]

    S = {c: {s: scores(X, y, schema, settings[c], K, delta, s) for s in seeds} for c in CONFIGS}
    point = {c: np.mean([stats(*S[c][s], classes) for s in seeds], axis=0) for c in CONFIGS}

    rng = np.random.default_rng(a.rng)
    boot = {c: np.zeros((a.n_boot, 2)) for c in CONFIGS}
    for s in seeds:
        in_a, yk = S[CONFIGS[0]][s][2], S[CONFIGS[0]][s][3]
        groups = [np.flatnonzero((yk == k) & (in_a == m)) for k in range(len(classes)) for m in (True, False)]
        groups = [g for g in groups if len(g)]
        for b in range(a.n_boot):
            idx = np.concatenate([rng.choice(g, len(g), replace=True) for g in groups])        # same records for every configuration
            for c in CONFIGS:
                sa, sb, _, _ = S[c][s]
                boot[c][b] += np.array(stats(sa[idx], sb[idx], in_a[idx], yk[idx], classes)) / len(seeds)

    res = {"n_boot": a.n_boot, "seeds": seeds, "rng": a.rng,
           "resampling": "records with replacement inside each class x membership group, paired across configurations", "configs": {}}
    ci = lambda v: [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))]          # noqa: E731
    for c in CONFIGS:
        r = {"auc": float(point[c][0]), "auc_ci95": ci(boot[c][:, 0]), "tpr_1pct": float(point[c][1]), "tpr_1pct_ci95": ci(boot[c][:, 1])}
        if c != "MGs-nodp":
            diff = boot["MGs-nodp"][:, 0] - boot[c][:, 0]
            lo, hi = ci(diff)
            r.update(auc_nodp_minus_this=float(point["MGs-nodp"][0] - point[c][0]), diff_ci95=[lo, hi], diff_excludes_zero=bool(lo > 0 or hi < 0))
        res["configs"][c] = r
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res["configs"], indent=1))


if __name__ == "__main__":
    main()
