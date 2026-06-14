"""
Key Rate vs Detector Basis Bias Comparison
===========================================
Sweeps X-basis detector efficiency η_X (1.0->0.5) with η_Z fixed at detector_efficiency.
Note: detector_efficiency in --config sets η_Z (fixed axis); η_X is the sweep axis.

Usage:
    python scripts/compare/basis_bias.py [--config PATH] [--runtimes N] [--fibre F]
                                         [--loss F] [--det-eff-z F] [--dark-count N]
                                         [--init-loss F] [--node-loss F] [--source-err F]

Defaults (no --config):
    detector_eff_x          swept 1.0->0.5  (sweep axis)
    detector_eff_z          1.0             (fixed; set via --det-eff-z or config detector_efficiency)
    fibre_loss_db_per_km    0.2  dB/km
    dark_count_rate         0    cps
    init_loss               0.0
    node_loss_db            0.0  dB
    source_error_rate       0.0
    fibre                   50   km
    runtimes                100
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append("BB84/")
sys.path.append("MDI/")
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser

import matplotlib.pyplot as plt


def qber(keyA, keyB):
    if not keyA or not keyB:
        return None
    length = min(len(keyA), len(keyB))
    if length == 0:
        return None
    errors = sum(a != b for a, b in zip(keyA[:length], keyB[:length]))
    return errors / length


def aggregate_summary(KeyListA, KeyListB, KeyRateList, protocol):
    qbers, key_rates, key_lengths = [], [], []
    for i, (keyA, keyB) in enumerate(zip(KeyListA, KeyListB)):
        q = qber(keyA, keyB)
        if q is not None and keyA != "nan":
            qbers.append(q)
            key_rates.append(KeyRateList[i])
            key_lengths.append(min(len(keyA), len(keyB)))
    avg_qber    = sum(qbers) / len(qbers)             if qbers      else float('nan')
    avg_kr      = sum(key_rates) / len(key_rates)     if key_rates  else float('nan')
    avg_key_len = sum(key_lengths) / len(key_lengths) if key_lengths else float('nan')
    return len(qbers), avg_key_len, avg_qber, avg_kr


def main(runtimes=10, photons=1024, fibre=100, freq=1e7, speed=0.8, lenLoss=0, initLoss=0, detEffZ=1, detEffX=1, darkCount=0, nodeLossDb=0.0, sourceErrRate=0.0, dephasingRate=0.0, bsEff=1.0):
    KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84 = run_BB84_sims(
        runtimes      = runtimes,
        fibreLen      = fibre,
        photonCount   = photons,
        sourceFreq    = freq,
        qSpeed        = speed,
        lenLoss       = lenLoss,
        initLoss      = initLoss,
        detectorEffZ  = detEffZ,
        detectorEffX  = detEffX,
        darkCount     = darkCount,
        nodeLossDb    = nodeLossDb,
        sourceErrRate = sourceErrRate,
        dephasingRate = dephasingRate,
    )
    KeyListA_mdi, KeyListB_mdi, KeyRateList_mdi = run_mdi_sims(
        runtimes      = runtimes,
        fibreLen      = fibre,
        photonCount   = photons,
        sourceFreq    = freq,
        qSpeed        = speed,
        lenLoss       = lenLoss,
        initLoss      = initLoss,
        detectorEffZ  = detEffZ,
        detectorEffX  = detEffX,
        darkCount     = darkCount,
        nodeLossDb    = nodeLossDb,
        sourceErrRate = sourceErrRate,
        dephasingRate = dephasingRate,
        bsEff         = bsEff,
    )
    bb84_stats = aggregate_summary(KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, "BB84")
    mdi_stats  = aggregate_summary(KeyListA_mdi,  KeyListB_mdi,  KeyRateList_mdi,  "MDI")
    return bb84_stats, mdi_stats


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes",    type=int,   default=100)
    parser.add_argument("--fibre",       type=float, default=50,   help="Fixed fibre length (km)")
    parser.add_argument("--loss",        type=float, default=None, help="Fibre loss (dB/km)")
    parser.add_argument("--det-eff-z",   type=float, default=None, dest="det_eff_z", help="Fixed Z-basis detector efficiency η_Z [0-1]")
    parser.add_argument("--dark-count",  type=int,   default=None, dest="dark_count", help="Dark count rate (cps)")
    parser.add_argument("--init-loss",   type=float, default=None, dest="init_loss",  help="Insertion loss, linear fraction [0-1]")
    parser.add_argument("--node-loss",   type=float, default=None, dest="node_loss",  help="Receiver node insertion loss (dB)")
    parser.add_argument("--source-err",  type=float, default=None, dest="source_err", help="Source bit error rate [0-1]")
    args = parser.parse_args()
    cfg  = load_config(args.config)
    if args.loss is not None:       cfg["fibre_loss_db_per_km"] = args.loss
    if args.det_eff_z is not None:  cfg["detector_efficiency"]  = args.det_eff_z
    if args.dark_count is not None: cfg["dark_count_rate"]      = args.dark_count
    if args.init_loss is not None:  cfg["init_loss"]            = args.init_loss
    if args.node_loss is not None:  cfg["node_loss_db"]         = args.node_loss
    if args.source_err is not None: cfg["source_error_rate"]    = args.source_err

    det_eff_z = cfg["detector_efficiency"]
    print(f"Sweep: η_X [1.0->0.5]  |  Fixed: η_Z={det_eff_z}  L={args.fibre} km  α={cfg['fibre_loss_db_per_km']} dB/km")

    Bx = [1.0, 0.99, 0.95, 0.9, 0.8, 0.7, 0.6, 0.5]

    rates_bb84, rates_mdi = [], []

    for ex in Bx:
        bb84, mdi = main(runtimes=args.runtimes, fibre=args.fibre,
                         lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
                         detEffZ=det_eff_z, detEffX=ex,
                         darkCount=cfg["dark_count_rate"],
                         nodeLossDb=cfg["node_loss_db"], sourceErrRate=cfg["source_error_rate"],
                         dephasingRate=cfg["dephasing_rate"], bsEff=cfg["bs_eff"])
        rates_bb84.append(bb84[3])
        rates_mdi.append(mdi[3])

    abs_rates_bb84 = [r / 1000 for r in rates_bb84]
    abs_rates_mdi  = [r / 1000 for r in rates_mdi]

    base           = rates_bb84[0]
    rel_rates_bb84 = [r / base for r in rates_bb84]
    rel_rates_mdi  = [r / base for r in rates_mdi]

    fig, ax1 = plt.subplots()
    ax1.plot(Bx, abs_rates_bb84, 'o-', label="BB84")
    ax1.plot(Bx, abs_rates_mdi,  's-', label="MDI")
    ax1.set_xlabel(r"X-basis detector efficiency $\eta_X$")
    ax1.set_ylabel("Absolute secure key rate (kbps)")
    ax1.set_yscale("log")
    ax1.invert_xaxis()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(Bx, rel_rates_bb84, 'o-', alpha=0)
    ax2.plot(Bx, rel_rates_mdi,  's-', alpha=0)
    ax2.set_ylabel("Relative secure key rate")
    ax2.set_yscale("log")

    ax1.legend()
    plt.title(f"Key rate vs detector basis bias: BB84 and MDI-QKD\n"
              f"$\\eta_Z$={det_eff_z}  |  $L$={args.fibre} km  |  $\\alpha$={cfg['fibre_loss_db_per_km']} dB/km  |  $d_c$={cfg['dark_count_rate']} cps\n"
              f"$L_i$={cfg['init_loss']}  |  $L_n$={cfg['node_loss_db']} dB  |  $\\varepsilon_s$={cfg['source_error_rate']}  |  $\\beta$={cfg['dephasing_rate']} /km  |  $\\eta_{{bs}}$={cfg['bs_eff']}")
    plt.show()
