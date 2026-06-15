"""
MDI-QKD Simulation Runner
=========================
Executes the MDI-QKD NetSquid simulation and prints per-run and aggregate metrics.

Usage:
    python scripts/raw/mdi_script.py [--config PATH] [--runtimes N] [--fibre F]
                                     [--loss F] [--det-eff F] [--dark-count N] [--init-loss F]

Defaults (no --config):
    fibre_loss_db_per_km    0.2  dB/km
    detector_efficiency     1.0
    dark_count_rate         0    cps
    init_loss               0.0  (linear fraction)
    fibre                   20   km
    runtimes                10
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser



def qber(keyA, keyB):
    if not keyA or not keyB:
        return None
    length = min(len(keyA), len(keyB))
    errors = sum(a != b for a, b in zip(keyA[:length], keyB[:length]))
    return errors / length


def print_run_summary(run_idx, keyA, keyB, keyRate):
    if keyA != "nan":
        q = qber(keyA, keyB)
        q_str = f"{q*100:.2f}%" if q is not None else "N/A"
        print(f"  MDI run {run_idx+1:>3}:  key_len={len(keyA):>5} | QBER={q_str:>7} | key_rate={keyRate:.4f}")
    else:
        print(f"  MDI run {run_idx+1:>3}:  did not complete")


def print_aggregate_summary(KeyListA, KeyListB, KeyRateList):
    qbers, key_rates, key_lengths = [], [], []
    for i, (keyA, keyB) in enumerate(zip(KeyListA, KeyListB)):
        if keyA == "nan":
            continue
        q = qber(keyA, keyB)
        if q is not None:
            qbers.append(q)
            key_rates.append(KeyRateList[i])
            key_lengths.append(min(len(keyA), len(keyB)))

    avg_qber    = sum(qbers) / len(qbers)             if qbers      else float('nan')
    avg_kr      = sum(key_rates) / len(key_rates)     if key_rates  else float('nan')
    avg_key_len = sum(key_lengths) / len(key_lengths) if key_lengths else float('nan')

    print()
    print("=" * 65)
    print("  Aggregate Results")
    print("=" * 65)
    print(f"  Runs completed  : {len(qbers)} / {len(KeyListA)}")
    print(f"  Avg key length  : {avg_key_len:.1f}")
    print(f"  Avg QBER        : {avg_qber*100:.2f}%")
    print(f"  Avg key rate    : {avg_kr:.4f} bps")
    print("=" * 65)


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes",   type=int,   default=10)
    parser.add_argument("--photons",    type=int,   default=1024)
    parser.add_argument("--fibre",      type=float, default=20,   help="Fibre length (km)")
    parser.add_argument("--freq",       type=float, default=1e7,  help="Source frequency (Hz)")
    parser.add_argument("--speed",      type=float, default=0.8,  help="Speed of light fraction")
    parser.add_argument("--loss",       type=float, default=None, help="Fibre loss (dB/km)")
    parser.add_argument("--det-eff",    type=float, default=None, dest="det_eff",    help="Detector efficiency [0-1]")
    parser.add_argument("--dark-count", type=int,   default=None, dest="dark_count", help="Dark count rate (cps)")
    parser.add_argument("--init-loss",  type=float, default=None, dest="init_loss",  help="Insertion loss, linear fraction [0-1]")
    parser.add_argument("--node-loss",  type=float, default=None, dest="node_loss",  help="Receiver node insertion loss (dB)")
    parser.add_argument("--source-err",     type=float, default=None, dest="source_err",     help="Source bit error rate [0-1]")
    parser.add_argument("--dephasing-rate", type=float, default=None, dest="dephasing_rate", help="Dephasing rate per km")
    parser.add_argument("--bs-eff",         type=float, default=None, dest="bs_eff",         help="Beam splitter efficiency at relay [0-1]")
    args = parser.parse_args()
    cfg  = load_config(args.config)
    if args.loss is not None:           cfg["fibre_loss_db_per_km"] = args.loss
    if args.det_eff is not None:        cfg["detector_efficiency"]  = args.det_eff
    if args.dark_count is not None:     cfg["dark_count_rate"]      = args.dark_count
    if args.init_loss is not None:      cfg["init_loss"]            = args.init_loss
    if args.node_loss is not None:      cfg["node_loss_db"]         = args.node_loss
    if args.source_err is not None:     cfg["source_error_rate"]    = args.source_err
    if args.dephasing_rate is not None: cfg["dephasing_rate"]       = args.dephasing_rate
    if args.bs_eff is not None:         cfg["bs_eff"]               = args.bs_eff

    print()
    print("=" * 65)
    print("  MDI-QKD Simulation")
    print("=" * 65)
    print(f"  Fibre      : {args.fibre} km")
    print(f"  Loss       : {cfg['fibre_loss_db_per_km']} dB/km")
    print(f"  Det. eff.  : {cfg['detector_efficiency']}")
    print(f"  Dark count : {cfg['dark_count_rate']} cps")
    print(f"  Init loss  : {cfg['init_loss']} (linear)")
    print(f"  Runtimes   : {args.runtimes}")
    print("=" * 65)
    print()

    KeyListA, KeyListB, KeyRateList = run_mdi_sims(
        runtimes    = args.runtimes,
        fibreLen    = args.fibre,
        photonCount = args.photons,
        sourceFreq  = args.freq,
        qSpeed      = args.speed,
        lenLoss     = cfg["fibre_loss_db_per_km"],
        initLoss    = cfg["init_loss"],
        detectorEffZ = cfg["detector_efficiency"],
        darkCount   = cfg["dark_count_rate"],
        nodeLossDb    = cfg["node_loss_db"],
        sourceErrRate = cfg["source_error_rate"],
        dephasingRate = cfg["dephasing_rate"],
        bsEff         = cfg["bs_eff"],
    )

    print("  Per-run results:")
    print("-" * 65)
    for i, (keyA, keyB) in enumerate(zip(KeyListA, KeyListB)):
        print_run_summary(i, keyA, keyB, KeyRateList[i])

    print_aggregate_summary(KeyListA, KeyListB, KeyRateList)
