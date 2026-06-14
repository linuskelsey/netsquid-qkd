"""
Key Rate vs Distance — Cumulative Modelling Layers
===================================================
Sweeps Alice-Bob distance for each config layer (layer0 ideal → layer8 fully realistic).
Each layer adds one physical parameter at its industry-typical value to the previous layer.
BB84 shows layers 0–7; MDI shows layers 0–8 (layer 8 adds beam splitter efficiency).

Usage:
    python scripts/compare/layers.py [--runtimes N]
"""

import sys
import os
import argparse

import numpy as np
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config
from lib.db import init_db, save_sweep_point, DEFAULT_DB_PATH

LAYERS = [
    ("layer0_ideal.json",      r"Layer 0: Ideal",                       "Layer 0: Ideal"),
    ("layer1_loss.json",       r"Layer 1: + $\alpha$=0.20 dB/km",       "Layer 1: + fibre loss @ 0.20 dB/km"),
    ("layer2_eff.json",        r"Layer 2: + $\eta_d$=0.65",             "Layer 2: + detector efficiency @ 0.65"),
    ("layer3_dark.json",       r"Layer 3: + $d_c$=100 cps",             "Layer 3: + dark count rate @ 100 cps"),
    ("layer4_init_loss.json",  r"Layer 4: + $L_i$=0.10",                "Layer 4: + init loss @ 0.10"),
    ("layer5_node_loss.json",  r"Layer 5: + $L_n$=2.0 dB",             "Layer 5: + node loss @ 2.0 dB"),
    ("layer6_source_err.json", r"Layer 6: + $\varepsilon_s$=0.005",     "Layer 6: + source error @ 0.005"),
    ("layer7_dephasing.json",  r"Layer 7: + $\beta$=1e-4/km",           "Layer 7: + dephasing @ 1e-4/km"),
    ("layer8_bs_eff.json",     r"Layer 8: + $\eta_{bs}$=0.97",          "Layer 8: + BS efficiency @ 0.97"),
]

Dx = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def qber(keyA, keyB):
    if not keyA or not keyB:
        return None
    length = min(len(keyA), len(keyB))
    if length == 0:
        return None
    errors = sum(a != b for a, b in zip(keyA[:length], keyB[:length]))
    return errors / length


def aggregate(KeyListA, KeyListB, KeyRateList):
    rates, qbers, lengths = [], [], []
    for i, (keyA, keyB) in enumerate(zip(KeyListA, KeyListB)):
        q = qber(keyA, keyB)
        if q is not None and keyA != "nan":
            rates.append(KeyRateList[i])
            qbers.append(q)
            lengths.append(min(len(keyA), len(keyB)))
    avg = sum(rates) / len(rates) if rates else float('nan')
    return avg, rates, qbers, lengths


def run_layer_bb84(cfg, runtimes, db_conn=None, layer_name=""):
    rates = []
    for d in Dx:
        KA, KB, KR = run_BB84_sims(
            runtimes      = runtimes,
            fibreLen      = d,
            photonCount   = 1024,
            sourceFreq    = 1e7,
            qSpeed        = 0.8,
            lenLoss       = cfg["fibre_loss_db_per_km"],
            initLoss      = cfg["init_loss"],
            detectorEffZ  = cfg["detector_efficiency"],
            darkCount     = cfg["dark_count_rate"],
            nodeLossDb    = cfg["node_loss_db"],
            sourceErrRate = cfg["source_error_rate"],
            dephasingRate = cfg["dephasing_rate"],
        )
        avg, raw_rates, raw_qbers, raw_lengths = aggregate(KA, KB, KR)
        rates.append(avg)
        if db_conn is not None:
            params = {
                "fibre_len":  d,
                "fibre_loss": cfg["fibre_loss_db_per_km"],
                "det_eff":    cfg["detector_efficiency"],
                "dark_count": cfg["dark_count_rate"],
                "init_loss":  cfg["init_loss"],
                "node_loss":  cfg["node_loss_db"],
                "source_err": cfg["source_error_rate"],
                "dephasing":  cfg["dephasing_rate"],
                "bs_eff":     cfg["bs_eff"],
            }
            save_sweep_point(db_conn, "BB84", params, raw_rates, raw_qbers, raw_lengths,
                             script=f"layers/{layer_name}", runtimes=runtimes, photons=1024)
    return [r / 1000 for r in rates]


def run_layer_mdi(cfg, runtimes, db_conn=None, layer_name=""):
    rates = []
    for d in Dx:
        KA, KB, KR = run_mdi_sims(
            runtimes      = runtimes,
            fibreLen      = d,
            photonCount   = 1024,
            sourceFreq    = 1e7,
            qSpeed        = 0.8,
            lenLoss       = cfg["fibre_loss_db_per_km"],
            initLoss      = cfg["init_loss"],
            detectorEffZ  = cfg["detector_efficiency"],
            darkCount     = cfg["dark_count_rate"],
            nodeLossDb    = cfg["node_loss_db"],
            sourceErrRate = cfg["source_error_rate"],
            dephasingRate = cfg["dephasing_rate"],
            bsEff         = cfg["bs_eff"],
        )
        avg, raw_rates, raw_qbers, raw_lengths = aggregate(KA, KB, KR)
        rates.append(avg)
        if db_conn is not None:
            params = {
                "fibre_len":  d,
                "fibre_loss": cfg["fibre_loss_db_per_km"],
                "det_eff":    cfg["detector_efficiency"],
                "dark_count": cfg["dark_count_rate"],
                "init_loss":  cfg["init_loss"],
                "node_loss":  cfg["node_loss_db"],
                "source_err": cfg["source_error_rate"],
                "dephasing":  cfg["dephasing_rate"],
                "bs_eff":     cfg["bs_eff"],
            }
            save_sweep_point(db_conn, "MDI", params, raw_rates, raw_qbers, raw_lengths,
                             script=f"layers/{layer_name}", runtimes=runtimes, photons=1024)
    return [r / 1000 for r in rates]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtimes",  type=int, default=100)
    parser.add_argument("--protocol",  choices=["bb84", "mdi", "both"], default="both",
                        help="Protocol(s) to run: bb84, mdi, or both (default: both)")
    parser.add_argument("--no-save",  action="store_true", help="Skip saving results to DB")
    parser.add_argument("--db",       type=str, default=DEFAULT_DB_PATH, help="Path to results SQLite DB")
    args = parser.parse_args()

    run_bb84 = args.protocol in ("bb84", "both")
    run_mdi  = args.protocol in ("mdi",  "both")

    db_conn = None if args.no_save else init_db(args.db)

    if run_bb84:
        colours_bb84 = plt.cm.viridis(np.linspace(0.0, 0.85, 8))
        fig_bb84, ax_bb84 = plt.subplots()
        for i, (cfg_file, label, label_plain) in enumerate(LAYERS[:8]):
            cfg = load_config(os.path.join(ROOT, "configs", cfg_file))
            print(f"BB84 {label_plain}...")
            rates = run_layer_bb84(cfg, args.runtimes, db_conn=db_conn, layer_name=cfg_file.replace(".json", ""))
            ax_bb84.plot(Dx, rates, 'o-', color=colours_bb84[i], label=label)
        ax_bb84.set_xlabel("Separation between Alice and Bob (km)")
        ax_bb84.set_ylabel("Secure key rate (kbps)")
        ax_bb84.set_yscale("log")
        ax_bb84.grid(True, alpha=0.3)
        ax_bb84.legend(fontsize=8)
        ax_bb84.set_title("Key rate vs distance: BB84 — cumulative modelling layers")

    if run_mdi:
        colours_mdi = plt.cm.Oranges(np.linspace(0.3, 0.95, 9))
        fig_mdi, ax_mdi = plt.subplots()
        for i, (cfg_file, label, label_plain) in enumerate(LAYERS):
            cfg = load_config(os.path.join(ROOT, "configs", cfg_file))
            print(f"MDI {label_plain}...")
            rates = run_layer_mdi(cfg, args.runtimes, db_conn=db_conn, layer_name=cfg_file.replace(".json", ""))
        ax_mdi.set_xlabel("Separation between Alice and Bob (km)")
        ax_mdi.set_ylabel("Secure key rate (kbps)")
        ax_mdi.set_yscale("log")
        ax_mdi.grid(True, alpha=0.3)
        ax_mdi.legend(fontsize=8)
        ax_mdi.set_title("Key rate vs distance: MDI-QKD — cumulative modelling layers")

    if db_conn is not None:
        db_conn.close()

    plt.show()
