"""
Key Rate vs Dark Count Rate Comparison
========================================
Sweeps dark count rate (0-10000 cps). Fixed fibre length, loss, and detector efficiency.
Note: dark_count_rate in --config is ignored; d_c is the sweep axis.

Usage:
    python scripts/compare/dark_count.py [--config PATH] [--runtimes N] [--fibre F]
                                         [--loss F] [--det-eff F] [--init-loss F]

Defaults (no --config):
    dark_count_rate         swept 0-10000 cps  (sweep axis — config value ignored)
    fibre_loss_db_per_km    0.2  dB/km  — pass --config configs/layer0_ideal.json for idealised run
    detector_efficiency     1.0
    init_loss               0.0  dB
    fibre                   50   km
    runtimes                100
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append("BB84/") # For BB84 protocols
sys.path.append("MDI/") # For MDI protocols
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser

import matplotlib.pyplot as plt



def qber(keyA, keyB):
    """Compute QBER between two key lists."""
    if not keyA or not keyB:
        return None
    length = min(len(keyA), len(keyB))
    if length == 0:
        return None
    errors = sum(a != b for a, b in zip(keyA[:length], keyB[:length]))
    return errors / length


def print_run_summary(run_idx, keyA, keyB, keyRate, protocol):
    """Print per-run metrics."""
    if keyA != "nan":
        q = qber(keyA, keyB)
        q_str = f"{q*100:.2f}%" if q is not None else "N/A"
        print(f"  {protocol} run {run_idx+1:>3}:  key_len={len(keyA):>5} | QBER={q_str:>7} | key_rate={keyRate:.4f}")
    else:
        print(f"  {protocol} run {run_idx+1:>3}:  did not complete")


def aggregate_summary(KeyListA, KeyListB, KeyRateList, protocol):
    """Print aggregate metrics across all runs."""
    qbers       = []
    key_rates   = []
    key_lengths = []

    for i, (keyA, keyB) in enumerate(zip(KeyListA, KeyListB)):
        q = qber(keyA, keyB)
        if q is not None and keyA != "nan":
            qbers.append(q)
            key_rates.append(KeyRateList[i])
            key_lengths.append(min(len(keyA), len(keyB)))

    avg_qber     = sum(qbers) / len(qbers) if qbers else float('nan')
    avg_kr       = sum(key_rates) / len(key_rates) if key_rates else float('nan')
    avg_key_len  = sum(key_lengths) / len(key_lengths) if key_lengths else float('nan')

    return len(qbers), avg_key_len, avg_qber, avg_kr


def comparative_stats(stats1, stats2):
    print()
    print("=" * 65)
    print(f" Aggregate Results     |    BB84    |     MDI    |")
    print("=" * 65)
    print(f"  Runs completed       |    {stats1[0]:>3}     |    {stats2[0]:>3}     |")
    print(f"  Avg key length       |   {stats1[1]:.2f}   |   {stats2[1]:.2f}   |")
    print(f"  Avg QBER             |    {stats1[2]*100:.2f}%   |    {stats2[2]*100:.2f}%   |")
    print(f"  Avg key rate (kbps)  |   {stats1[3]/1000:.2f}  |   {stats2[3]/1000:.2f}  |")
    return


def main(runtimes=10, photons=1024, fibre=100, freq=1e7, speed=0.8, lenLoss=0, initLoss=0, detEff=1, darkCount=0, nodeLossDb=0.0, sourceErrRate=0.0, dephasingRate=0.0, bsEff=1.0):
    # BB84 run ==================================================
    KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84 = run_BB84_sims(
        runtimes      = runtimes,
        fibreLen      = fibre,
        photonCount   = photons,
        sourceFreq    = freq,
        qSpeed        = speed,
        lenLoss       = lenLoss,
        initLoss      = initLoss,
        detectorEffZ  = detEff,
        darkCount     = darkCount,
        nodeLossDb    = nodeLossDb,
        sourceErrRate = sourceErrRate,
        dephasingRate = dephasingRate,
    )

    # MDI run ===================================================
    KeyListA_mdi, KeyListB_mdi, KeyRateList_mdi = run_mdi_sims(
        runtimes      = runtimes,
        fibreLen      = fibre,
        photonCount   = photons,
        sourceFreq    = freq,
        qSpeed        = speed,
        lenLoss       = lenLoss,
        initLoss      = initLoss,
        detectorEffZ  = detEff,
        darkCount     = darkCount,
        nodeLossDb    = nodeLossDb,
        sourceErrRate = sourceErrRate,
        dephasingRate = dephasingRate,
        bsEff         = bsEff,
    )

    # Aggregate stats ===========================================
    bb84_stats = aggregate_summary(KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, "BB84")
    mdi_stats  = aggregate_summary(KeyListA_mdi,  KeyListB_mdi,  KeyRateList_mdi,  "MDI")

    return bb84_stats, mdi_stats

if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes",  type=int,   default=100)
    parser.add_argument("--fibre",     type=float, default=50,   help="Fixed fibre length (km)")
    parser.add_argument("--loss",      type=float, default=None, help="Fibre loss (dB/km)")
    parser.add_argument("--det-eff",   type=float, default=None, dest="det_eff",   help="Detector efficiency [0-1]")
    parser.add_argument("--init-loss", type=float, default=None, dest="init_loss", help="Insertion loss, linear fraction [0-1] (e.g. 0.1 = 10%%)")
    parser.add_argument("--node-loss",  type=float, default=None, dest="node_loss",  help="Receiver node insertion loss (dB)")
    parser.add_argument("--source-err", type=float, default=None, dest="source_err", help="Source bit error rate [0-1]")
    args = parser.parse_args()
    cfg  = load_config(args.config)
    if args.loss is not None:        cfg["fibre_loss_db_per_km"] = args.loss
    if args.det_eff is not None:     cfg["detector_efficiency"]  = args.det_eff
    if args.init_loss is not None:   cfg["init_loss"]            = args.init_loss
    if args.node_loss is not None:   cfg["node_loss_db"]         = args.node_loss
    if args.source_err is not None:  cfg["source_error_rate"]    = args.source_err

    if args.config is not None and cfg["dark_count_rate"] != 0:
        print(f"Note: dark_count_rate={cfg['dark_count_rate']} from config ignored — d_c is the sweep axis")
    print(f"Sweep: d_c [0-10000 cps]  |  Fixed: L={args.fibre} km  α={cfg['fibre_loss_db_per_km']} dB/km  η_d={cfg['detector_efficiency']}")

    DCx = [0, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

    lengths_bb84 = []
    lengths_mdi  = []
    qbers_bb84   = []
    qbers_mdi    = []
    rates_bb84   = []
    rates_mdi    = []

    for dc in DCx:
        bb84, mdi = main(runtimes=args.runtimes, fibre=args.fibre,
                         lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
                         detEff=cfg["detector_efficiency"], darkCount=dc,
                         nodeLossDb=cfg["node_loss_db"], sourceErrRate=cfg["source_error_rate"],
                         dephasingRate=cfg["dephasing_rate"], bsEff=cfg["bs_eff"])

        lengths_bb84.append(bb84[1])
        qbers_bb84.append(bb84[2])
        rates_bb84.append(bb84[3])

        lengths_mdi.append(mdi[1])
        qbers_mdi.append(mdi[2])
        rates_mdi.append(mdi[3])

    # Store absolute rates before normalising
    abs_rates_bb84 = [r / 1000 for r in rates_bb84]  # convert to kbps
    abs_rates_mdi  = [r / 1000 for r in rates_mdi]

    # Then normalise for relative
    base           = rates_bb84[0]
    rel_rates_bb84 = [r / base for r in rates_bb84]
    rel_rates_mdi  = [r / base for r in rates_mdi]

    fig, ax1 = plt.subplots()

    # Primary axis — absolute scale
    ax1.plot(DCx, abs_rates_bb84, 'o-', label="BB84")
    ax1.plot(DCx, abs_rates_mdi,  's-', label="MDI")
    ax1.set_xlabel("Dark count rate (cps)")
    ax1.set_ylabel("Absolute secure key rate (kbps)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3)

    # Secondary axis — relative scale
    ax2 = ax1.twinx()
    ax2.plot(DCx, rel_rates_bb84, 'o-', alpha=0)
    ax2.plot(DCx, rel_rates_mdi,  's-', alpha=0)
    ax2.set_ylabel("Relative secure key rate")
    ax2.set_yscale("log")

    ax1.legend()
    plt.title(f"Key rate vs dark count rate: BB84 and MDI-QKD\n"
              f"$L$={args.fibre} km  |  $\\alpha$={cfg['fibre_loss_db_per_km']} dB/km  |  $\\eta_d$={cfg['detector_efficiency']}\n"
              f"$L_i$={cfg['init_loss']}  |  $L_n$={cfg['node_loss_db']} dB  |  $\\varepsilon_s$={cfg['source_error_rate']}  |  $\\beta$={cfg['dephasing_rate']} /km  |  $\\eta_{{bs}}$={cfg['bs_eff']}")
    plt.show()
