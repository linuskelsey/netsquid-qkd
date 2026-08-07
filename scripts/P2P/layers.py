"""
Key Rate vs Distance — Cumulative Modelling Layers
===================================================
Sweeps Alice-Bob distance (1–100 km) for each config layer, building up from the ideal
case to a fully realistic physical model. Each layer adds one parameter at its
industry-typical value on top of all previous layers.

BB84 runs layers 0–8 (no beam splitter); MDI runs layers 0–9.
Error bars show min/max across Monte Carlo runs at each distance point.
Both protocols produce separate figures.

Usage:
    python scripts/P2P/layers.py [options]

Options:
    --runtimes INT      Monte Carlo runs per distance point (default: 100)
    --protocol STR      Protocol(s) to run: bb84, mdi, or both (default: both)
    --workers INT       Worker processes per distance point (default: 80% of CPU cores)
    --no-db             Disable DB writing
    --output-dir PATH   Save figure bundle {plot.png, plot.tex, assumptions.md} to directory instead of displaying

Layers:
    Layer 0   Ideal (no physical noise)
    Layer 1   + fibre attenuation         0.18 dB/km
    Layer 2   + detector efficiency       0.90
    Layer 3   + dark count rate           50 cps
    Layer 4   + init/coupling loss        L_i = 0.10
    Layer 5   + node/connector loss       2.0 dB
    Layer 6   + source error rate         0.015
    Layer 7   + fibre dephasing           3.2e-7 /km
    Layer 8   + X-basis detector bias     η_X = 0.715
    Layer 9   + beam splitter efficiency  0.97  (MDI only)

Examples:
    python scripts/P2P/layers.py
    python scripts/P2P/layers.py --runtimes 50 --protocol mdi
    python scripts/P2P/layers.py --runtimes 200 --workers 7
"""

import sys
import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from lib.plotting import apply_thesis_style, save_bundle
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH

apply_thesis_style()

LAYERS = [
    ("layer0_ideal.json",       "Layer 0: Ideal"),
    ("layer1_loss.json",        "Layer 1: + fibre loss @ 0.18 dB/km"),
    ("layer2_eff.json",         "Layer 2: + detector efficiency @ 0.90"),
    ("layer3_dark.json",        "Layer 3: + dark count rate @ 50 cps"),
    ("layer4_init_loss.json",   "Layer 4: + init loss @ 0.10"),
    ("layer5_node_loss.json",   "Layer 5: + node loss @ 2.0 dB"),
    ("layer6_source_err.json",  "Layer 6: + source error @ 0.015"),
    ("layer7_dephasing.json",   "Layer 7: + dephasing @ 3.2e-7/km"),
    ("layer8_basis_bias.json",  "Layer 8: + basis bias @ 0.715"),
    ("layer9_bs_eff.json",      "Layer 9: + BS efficiency @ 0.97"),
]

Dx = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def aggregate(KeyListA, KeyListB, KeyRateList, QBERList):
    rates, qbers, lengths = [], [], []
    for i, (keyA, keyB, q) in enumerate(zip(KeyListA, KeyListB, QBERList)):
        if q is not None:
            qbers.append(q)
        if keyA != "nan":
            rates.append(KeyRateList[i])
            lengths.append(min(len(keyA), len(keyB)))
    avg = sum(rates) / len(rates) if rates else float('nan')
    return avg, rates, qbers, lengths


def run_layer_bb84(cfg, runtimes, workers=None, db_path=DEFAULT_DB_PATH):
    rates, mins, maxs = [], [], []
    for d in Dx:
        KA, KB, KR, KQ = run_BB84_sims(
            runtimes      = runtimes,
            fibreLen      = d,
            photonCount   = 1024,
            sourceFreq    = 1e7,
            qSpeed        = 0.8,
            lenLoss       = cfg["fibre_loss_db_per_km"],
            initLoss      = cfg["init_loss"],
            detectorEffZ  = cfg["detector_efficiency"],
            detectorEffX  = cfg["det_eff_x"],
            darkCount     = cfg["dark_count_rate"],
            nodeLossDb    = cfg["node_loss_db"],
            sourceErrRate = cfg["source_error_rate"],
            dephasingRate = cfg["dephasing_rate"],
            workers       = workers,
            db_path       = db_path,
        )
        avg, raw_rates, raw_qbers, raw_lengths = aggregate(KA, KB, KR, KQ)
        rates.append(avg)
        nz = [r for r in raw_rates if r > 0]
        mins.append(min(nz) if nz else float('nan'))
        maxs.append(max(raw_rates) if raw_rates else float('nan'))
    k = 1000
    return [r / k for r in rates], [r / k for r in mins], [r / k for r in maxs]


def run_layer_mdi(cfg, runtimes, workers=None, db_path=DEFAULT_DB_PATH):
    rates, mins, maxs = [], [], []
    for d in Dx:
        KA, KB, KR, KQ = run_mdi_sims(
            runtimes      = runtimes,
            fibreLen      = d,
            photonCount   = 1024,
            sourceFreq    = 1e7,
            qSpeed        = 0.8,
            lenLoss       = cfg["fibre_loss_db_per_km"],
            initLoss      = cfg["init_loss"],
            detectorEffZ  = cfg["detector_efficiency"],
            detectorEffX  = cfg["det_eff_x"],
            darkCount     = cfg["dark_count_rate"],
            nodeLossDb    = cfg["node_loss_db"],
            sourceErrRate = cfg["source_error_rate"],
            dephasingRate = cfg["dephasing_rate"],
            bsEff         = cfg["bs_eff"],
            workers       = workers,
            db_path       = db_path,
        )
        avg, raw_rates, raw_qbers, raw_lengths = aggregate(KA, KB, KR, KQ)
        rates.append(avg)
        nz = [r for r in raw_rates if r > 0]
        mins.append(min(nz) if nz else float('nan'))
        maxs.append(max(raw_rates) if raw_rates else float('nan'))
    k = 1000
    return [r / k for r in rates], [r / k for r in mins], [r / k for r in maxs]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtimes",   type=int, default=100)
    parser.add_argument("--protocol",   choices=["bb84", "mdi", "both"], default="both",
                        help="Protocol(s) to run: bb84, mdi, or both (default: both)")
    parser.add_argument("--no-db",     action="store_true", help="Disable DB writing")
    parser.add_argument("--workers",   type=int, default=None, help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to save figures into (skips interactive display)")
    args = parser.parse_args()

    run_bb84 = args.protocol in ("bb84", "both")
    run_mdi  = args.protocol in ("mdi",  "both")

    if run_bb84:
        colours_bb84 = plt.cm.viridis(np.linspace(0.0, 0.85, 9))
        fig_bb84, ax_bb84 = plt.subplots()
        for i, (cfg_file, label) in enumerate(LAYERS[:9]):
            cfg = load_config(os.path.join(ROOT, "configs", cfg_file))
            print(f"BB84 {label}...")
            rates, mins, maxs = run_layer_bb84(cfg, args.runtimes, workers=args.workers, db_path=None if args.no_db else DEFAULT_DB_PATH)
            yerr = [
                [max(r - m, 0) for r, m in zip(rates, mins)],
                [max(m - r, 0) for r, m in zip(rates, maxs)],
            ]
            ax_bb84.errorbar(Dx, rates, yerr=yerr, fmt='o-', color=colours_bb84[i], label=label, capsize=3)
        ax_bb84.set_xlabel("Separation between Alice and Bob (km)")
        ax_bb84.set_ylabel("Secure key rate (kbps)")
        ax_bb84.set_yscale("log")
        ax_bb84.grid(True, alpha=0.3)
        ax_bb84.legend(fontsize=7)
        ax_bb84.set_title("BB84: Cumulative Modelling Layers")
        if args.output_dir:
            save_bundle(
                fig_bb84, args.output_dir, "layers_bb84",
                title="BB84: Cumulative Modelling Layers",
                assumptions={
                    "Distance sweep points (km)": Dx,
                    "Runtimes per point": args.runtimes,
                    "Layers (cumulative)": {label: fname for fname, label in LAYERS[:9]},
                },
                notes=["Each layer adds one parameter at its realistic value on top of all previous layers.",
                       "BB84 runs layers 0-7 (no beam splitter)."],
            )
            plt.close(fig_bb84)

    if run_mdi:
        colours_mdi = plt.cm.Oranges(np.linspace(0.3, 0.95, 10))
        fig_mdi, ax_mdi = plt.subplots()
        for i, (cfg_file, label) in enumerate(LAYERS):
            cfg = load_config(os.path.join(ROOT, "configs", cfg_file))
            print(f"MDI {label}...")
            rates, mins, maxs = run_layer_mdi(cfg, args.runtimes, workers=args.workers, db_path=None if args.no_db else DEFAULT_DB_PATH)
            yerr = [
                [max(r - m, 0) for r, m in zip(rates, mins)],
                [max(m - r, 0) for r, m in zip(rates, maxs)],
            ]
            ax_mdi.errorbar(Dx, rates, yerr=yerr, fmt='o-', color=colours_mdi[i], label=label, capsize=3)
        ax_mdi.set_xlabel("Separation between Alice and Bob (km)")
        ax_mdi.set_ylabel("Secure key rate (kbps)")
        ax_mdi.set_yscale("log")
        ax_mdi.grid(True, alpha=0.3)
        ax_mdi.legend(fontsize=7)
        ax_mdi.set_title("MDI: Cumulative Modelling Layers")
        if args.output_dir:
            save_bundle(
                fig_mdi, args.output_dir, "layers_mdi",
                title="MDI: Cumulative Modelling Layers",
                assumptions={
                    "Distance sweep points (km)": Dx,
                    "Runtimes per point": args.runtimes,
                    "Layers (cumulative)": {label: fname for fname, label in LAYERS},
                },
                notes=["Each layer adds one parameter at its realistic value on top of all previous layers.",
                       "MDI runs layers 0-9 (includes beam splitter efficiency)."],
            )
            plt.close(fig_mdi)

    if not args.output_dir:
        plt.show()
