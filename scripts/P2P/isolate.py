"""
Key Rate vs Distance — Isolated Parameter Impact
=================================================
Sweeps Alice-Bob distance (1-100 km). Baseline is fully ideal (layer 0: no loss,
perfect detectors, no noise). Each subsequent curve sets exactly one physical
parameter to its realistic value while all others remain ideal.

Complements layers.py (cumulative): here you see the independent impact of each
hardware imperfection in isolation, without interaction effects from other parameters.

BB84 runs 8 isolated parameters (fibre loss through basis bias).
MDI runs 9 (includes beam splitter efficiency).

Usage:
    python scripts/P2P/isolate.py [options]

Options:
    --runtimes INT   Monte Carlo runs per distance point (default: 100)
    --protocol STR   Protocol(s) to run: bb84, mdi, or both (default: both)
    --workers INT    Worker processes (default: 80%% of CPU cores)
    --no-db          Disable DB writing
    --output-dir DIR Save figures to directory instead of displaying

Examples:
    python scripts/P2P/isolate.py
    python scripts/P2P/isolate.py --protocol mdi --runtimes 50
    python scripts/P2P/isolate.py --output-dir docs/figures
"""

import os
import sys
import argparse

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.db import DEFAULT_DB_PATH, new_run_id, init_db, insert_p2p_rows

_Dx = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

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

# (config_key, realistic_value, legend_label)
# Order: loosely by expected impact magnitude at typical metropolitan distances.
_PARAMS = [
    ("fibre_loss_db_per_km", 0.2,    r"Fibre loss  $\alpha$=0.20 dB/km"),
    ("detector_efficiency",  0.65,   r"Detector eff  $\eta_d$=0.65"),
    ("dark_count_rate",      100,    r"Dark count  $d_c$=100 cps"),
    ("init_loss",            0.1,    r"Init loss  $L_i$=0.10"),
    ("node_loss_db",         2.0,    r"Node loss  $L_n$=2.0 dB"),
    ("source_error_rate",    0.005,  r"Source error  $\varepsilon_s$=0.005"),
    ("dephasing_rate",       0.0001, r"Dephasing  $\beta$=10$^{-4}$/km"),
    ("det_eff_x",            0.85,   r"Basis bias  $\eta_X$=0.85"),
    ("bs_eff",               0.97,   r"BS eff  $\eta_{bs}$=0.97  (MDI only)"),
]

_BB84_IDX = [i for i, p in enumerate(_PARAMS) if p[0] != "bs_eff"]
_MDI_IDX  = list(range(len(_PARAMS)))


def _plot_proto(proto_name, param_indices, runtimes, workers, db_path):
    is_mdi = proto_name == "MDI"
    proto  = "MDI" if is_mdi else "BB84"

    all_cfgs   = [_IDEAL] + [dict(_IDEAL, **{_PARAMS[pi][0]: _PARAMS[pi][1]}) for pi in param_indices]
    all_labels = ["Ideal (baseline)"] + [_PARAMS[pi][2] for pi in param_indices]
    colours    = plt.cm.tab10(np.linspace(0, 0.9, len(param_indices)))

    print(f"{proto_name}  {len(all_cfgs)} curves × {len(_Dx)} distances...")

    conn      = init_db(db_path) if db_path else None
    timestamp = datetime.now().isoformat()
    fig, ax   = plt.subplots()

    for ci, (cfg, label) in enumerate(zip(all_cfgs, all_labels)):
        rates, mins, maxs = [], [], []
        for d in _Dx:
            if is_mdi:
                KA, KB, KR, KQ = run_mdi_sims(
                    runtimes=runtimes, fibreLen=d, photonCount=1024, sourceFreq=1e7,
                    qSpeed=0.8, lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
                    detectorEffZ=cfg["detector_efficiency"], detectorEffX=cfg["det_eff_x"],
                    darkCount=cfg["dark_count_rate"], nodeLossDb=cfg["node_loss_db"],
                    sourceErrRate=cfg["source_error_rate"], dephasingRate=cfg["dephasing_rate"],
                    bsEff=cfg["bs_eff"], charliePos=0.5, workers=workers, db_path=None,
                )
            else:
                KA, KB, KR, KQ = run_BB84_sims(
                    runtimes=runtimes, fibreLen=d, photonCount=1024, sourceFreq=1e7,
                    qSpeed=0.8, lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
                    detectorEffZ=cfg["detector_efficiency"], detectorEffX=cfg["det_eff_x"],
                    darkCount=cfg["dark_count_rate"], nodeLossDb=cfg["node_loss_db"],
                    sourceErrRate=cfg["source_error_rate"], dephasingRate=cfg["dephasing_rate"],
                    workers=workers, db_path=None,
                )

            if conn is not None:
                db_params = {
                    "protocol": proto, "fibre_len": d, "photon_count": 1024,
                    "source_freq": 1e7, "q_speed": 0.8, "q_delay": 0,
                    "len_loss": cfg["fibre_loss_db_per_km"], "init_loss": cfg["init_loss"],
                    "detector_eff_z": cfg["detector_efficiency"], "detector_eff_x": cfg["det_eff_x"],
                    "dark_count": cfg["dark_count_rate"], "node_loss_db": cfg["node_loss_db"],
                    "source_err_rate": cfg["source_error_rate"], "dephasing_rate": cfg["dephasing_rate"],
                    "runtimes": runtimes,
                }
                if is_mdi:
                    db_params["bs_eff"]      = cfg["bs_eff"]
                    db_params["charlie_pos"] = 0.5
                key_lens = [len(a) if a != "nan" else None for a in KA]
                insert_p2p_rows(conn, new_run_id(), timestamp, db_params, key_lens, KR, KQ)

            raw = [r for kA_i, r in zip(KA, KR) if kA_i != "nan" and r > 0]
            avg = sum(raw) / len(raw) if raw else float("nan")
            rates.append(avg / 1000)
            mins.append(min(raw) / 1000 if raw else float("nan"))
            maxs.append(max(raw) / 1000 if raw else float("nan"))

        yerr = [
            [max(r - lo, 0) for r, lo in zip(rates, mins)],
            [max(hi - r, 0) for r, hi in zip(rates, maxs)],
        ]
        if ci == 0:
            ax.errorbar(_Dx, rates, yerr=yerr, fmt='-', color="black", lw=1.2,
                        elinewidth=0.6, capsize=0, label=label, zorder=10)
        else:
            ax.errorbar(_Dx, rates, yerr=yerr, fmt='-', color=colours[ci - 1],
                        lw=0.9, elinewidth=0.5, capsize=0, label=label)

    if conn is not None:
        conn.close()

    ax.set_xlabel("Separation between Alice and Bob (km)")
    ax.set_ylabel("Secure key rate (kbps)")
    ax.set_yscale("log")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7)
    ax.set_title(
        f"Key rate vs distance: {proto_name} — isolated parameter impact\n"
        f"Each curve: ideal config with exactly one parameter at its realistic value"
    )
    return fig


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot key rate vs distance for each isolated physical parameter.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--runtimes", type=int, default=100,
                        help="Monte Carlo runs per distance point")
    parser.add_argument("--protocol", choices=["bb84", "mdi", "both"], default="both",
                        help="Protocol(s) to run")
    parser.add_argument("--workers",  type=int, default=None,
                        help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--no-db",   action="store_true",
                        help="Disable DB writing")
    parser.add_argument("--output-dir", metavar="DIR", default=None,
                        help="Save figures to directory instead of displaying")
    args = parser.parse_args()

    db_path  = None if args.no_db else DEFAULT_DB_PATH
    run_bb84 = args.protocol in ("bb84", "both")
    run_mdi  = args.protocol in ("mdi",  "both")

    figs = []
    if run_bb84:
        figs.append(("bb84", _plot_proto("BB84", _BB84_IDX, args.runtimes, args.workers, db_path)))
    if run_mdi:
        figs.append(("mdi",  _plot_proto("MDI",  _MDI_IDX,  args.runtimes, args.workers, db_path)))

    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        for name, fig in figs:
            path = os.path.join(args.output_dir, f"isolate_{name}.png")
            fig.savefig(path, dpi=150, bbox_inches="tight")
            print(f"Saved to {path}")
        plt.close("all")
    else:
        plt.show()
