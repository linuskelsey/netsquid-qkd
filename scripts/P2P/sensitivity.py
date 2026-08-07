"""
Parameter Sensitivity Ranking
==============================
Quantifies the independent impact of each physical parameter on key rate at a
fixed operating distance. Baseline is fully ideal (layer 0). Each parameter is
then set to its realistic value one at a time; all others remain ideal.

Sensitivity = (R_ideal - R_param) / R_ideal × 100%

Higher value = that parameter degrades key rate more at this operating point.
bs_eff is MDI-only (BB84 bar set to 0). Results sorted by BB84 impact descending.

Usage:
    python scripts/P2P/sensitivity.py [options]

Options:
    --distance FLOAT    Operating distance in km (default: 25)
    --runtimes INT      MC runs per point (default: 200)
    --workers INT       Worker processes (default: 80% of cores)
    --no-db             Disable DB writing
    --output-dir DIR    Save figure to directory instead of displaying
"""

import os
import sys
import argparse

import numpy as np
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from lib.plotting import apply_thesis_style, save_bundle
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.db import DEFAULT_DB_PATH

apply_thesis_style()

_IDEAL = {
    "fibre_loss_db_per_km": 0.0,
    "init_loss":            0.0,
    "detector_efficiency":  1.0,
    "dark_count_rate":      0,
    "node_loss_db":         0.0,
    "source_error_rate":    0.0,
    "dephasing_rate":       0.0,
    "det_eff_x":            1.0,
    "bs_eff":               1.0,
}

_PARAMS = [
    ("fibre_loss_db_per_km", 0.2,    r"Fibre loss ($\alpha$=0.20 dB/km)"),
    ("detector_efficiency",  0.65,   r"Detector eff ($\eta_d$=0.65)"),
    ("dark_count_rate",      100,    r"Dark count ($d_c$=100 cps)"),
    ("init_loss",            0.1,    r"Init loss ($L_i$=0.10)"),
    ("node_loss_db",         2.0,    r"Node loss ($L_n$=2.0 dB)"),
    ("source_error_rate",    0.005,  r"Source error ($\varepsilon_s$=0.005)"),
    ("dephasing_rate",       3.2e-7, r"Dephasing ($\beta$=3.2$\times10^{-7}$/km)"),
    ("det_eff_x",            0.715,  r"Basis bias ($\eta_X$=0.715)"),
    ("bs_eff",               0.97,   r"BS eff ($\eta_{bs}$=0.97, MDI only)"),
]


def _run(cfg, distance, runtimes, workers, db_path, is_mdi):
    kw = dict(
        runtimes=runtimes, fibreLen=distance, photonCount=1024, sourceFreq=1e7,
        qSpeed=0.8, lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
        detectorEffZ=cfg["detector_efficiency"], detectorEffX=cfg["det_eff_x"],
        darkCount=cfg["dark_count_rate"], nodeLossDb=cfg["node_loss_db"],
        sourceErrRate=cfg["source_error_rate"], dephasingRate=cfg["dephasing_rate"],
        workers=workers, db_path=db_path,
    )
    if is_mdi:
        KA, KB, KR, KQ = run_mdi_sims(**kw, bsEff=cfg["bs_eff"])
    else:
        KA, KB, KR, KQ = run_BB84_sims(**kw)
    valid = [r for kA, r in zip(KA, KR) if kA != "nan" and r > 0]
    return sum(valid) / len(valid) if valid else 0.0


def _sensitivity(r_ideal, r_param):
    if r_ideal <= 0:
        return float("nan")
    return max(0.0, (r_ideal - r_param) / r_ideal * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parameter sensitivity ranking at a fixed distance.")
    parser.add_argument("--distance",   type=float, default=25,  help="Operating distance in km (default: 25)")
    parser.add_argument("--runtimes",   type=int,   default=200, help="MC runs per point (default: 200)")
    parser.add_argument("--workers",    type=int,   default=None)
    parser.add_argument("--no-db",      action="store_true", help="Disable DB writing")
    parser.add_argument("--output-dir", metavar="DIR", default=None, help="Save figure to directory")
    args = parser.parse_args()

    db_path = None if args.no_db else DEFAULT_DB_PATH

    print(f"\nOperating distance: {args.distance} km  |  runtimes: {args.runtimes}")

    print("Running ideal baseline (BB84 + MDI)...")
    r_ideal_bb84 = _run(_IDEAL, args.distance, args.runtimes, args.workers, db_path, is_mdi=False)
    r_ideal_mdi  = _run(_IDEAL, args.distance, args.runtimes, args.workers, db_path, is_mdi=True)
    print(f"  Ideal BB84: {r_ideal_bb84/1000:.2f} kbps  |  Ideal MDI: {r_ideal_mdi/1000:.2f} kbps")

    sens_bb84, sens_mdi, labels = [], [], []
    for key, val, label in _PARAMS:
        cfg = dict(_IDEAL, **{key: val})
        print(f"Running {label}...")
        if key == "bs_eff":
            s_bb84 = 0.0
        else:
            r = _run(cfg, args.distance, args.runtimes, args.workers, db_path, is_mdi=False)
            s_bb84 = _sensitivity(r_ideal_bb84, r)
        r_mdi = _run(cfg, args.distance, args.runtimes, args.workers, db_path, is_mdi=True)
        s_mdi = _sensitivity(r_ideal_mdi, r_mdi)
        sens_bb84.append(s_bb84)
        sens_mdi.append(s_mdi)
        labels.append(label)
        print(f"  BB84: {s_bb84:.1f}%  |  MDI: {s_mdi:.1f}%")

    # Sort by BB84 sensitivity descending
    order       = sorted(range(len(labels)), key=lambda i: sens_bb84[i], reverse=True)
    labels_s    = [labels[i]    for i in order]
    sens_bb84_s = [sens_bb84[i] for i in order]
    sens_mdi_s  = [sens_mdi[i]  for i in order]

    y, h = np.arange(len(labels_s)), 0.35
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(y + h/2, sens_bb84_s, h, label="BB84", color="steelblue")
    ax.barh(y - h/2, sens_mdi_s,  h, label="MDI",  color="darkorange")
    ax.set_yticks(y)
    ax.set_yticklabels(labels_s, fontsize=9)
    ax.set_xlabel("Key rate reduction from ideal (%)")
    ax.set_xlim(0, 105)
    ax.set_title("Parameter Sensitivity Ranking")
    ax.legend()
    ax.grid(True, axis="x", alpha=0.3)
    plt.tight_layout()

    if args.output_dir:
        save_bundle(
            fig, args.output_dir, "sensitivity",
            title="Parameter Sensitivity Ranking",
            assumptions={
                "Operating distance": f"{args.distance} km",
                "Runtimes per point": args.runtimes,
                "Baseline": "fully ideal (layer 0): " + ", ".join(f"{k}={v}" for k, v in _IDEAL.items()),
                "Realistic values tested (one at a time)": {p[0]: p[1] for p in _PARAMS},
                "Ideal BB84 key rate": f"{r_ideal_bb84/1000:.2f} kbps",
                "Ideal MDI key rate": f"{r_ideal_mdi/1000:.2f} kbps",
            },
            notes=["Sensitivity = (R_ideal - R_param) / R_ideal x 100%.",
                   "bs_eff is MDI-only (BB84 bar set to 0).",
                   "Results sorted by BB84 impact descending."],
        )
        print(f"Saved to {os.path.join(args.output_dir, 'sensitivity')}")
        plt.close()
    else:
        plt.show()
