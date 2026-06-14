"""
Key Rate vs Node/Connector Loss Comparison
===========================================
Sweeps receiver-side node loss (0-6 dB). Fixed fibre length, loss, and detector parameters.
Note: node_loss_db in --config is ignored; L_node is the sweep axis.

Usage:
    python scripts/compare/node_loss.py [--config PATH] [--runtimes N] [--fibre F]
                                        [--loss F] [--det-eff F] [--dark-count N] [--init-loss F]
                                        [--source-err F]

Defaults (no --config):
    node_loss_db            swept 0-6 dB  (sweep axis — config value ignored)
    fibre_loss_db_per_km    0.2  dB/km
    detector_efficiency     1.0
    dark_count_rate         0    cps
    init_loss               0.0
    source_error_rate       0.0
    fibre                   50   km
    runtimes                100
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append("BB84/")
sys.path.append("MDI/")
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser
from lib.db import init_db, save_sweep_point, DEFAULT_DB_PATH

import matplotlib.pyplot as plt
import math
import statistics


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
    return len(qbers), avg_key_len, avg_qber, avg_kr, key_rates, qbers, key_lengths


def main(runtimes=10, photons=1024, fibre=100, freq=1e7, speed=0.8, lenLoss=0, initLoss=0, detEff=1, darkCount=0, nodeLossDb=0.0, sourceErrRate=0.0, dephasingRate=0.0, bsEff=1.0):
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
    bb84_stats = aggregate_summary(KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, "BB84")
    mdi_stats  = aggregate_summary(KeyListA_mdi,  KeyListB_mdi,  KeyRateList_mdi,  "MDI")
    return bb84_stats, mdi_stats


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes",   type=int,   default=100)
    parser.add_argument("--fibre",      type=float, default=50,   help="Fixed fibre length (km)")
    parser.add_argument("--loss",       type=float, default=None, help="Fibre loss (dB/km)")
    parser.add_argument("--det-eff",    type=float, default=None, dest="det_eff",    help="Detector efficiency [0-1]")
    parser.add_argument("--dark-count", type=int,   default=None, dest="dark_count", help="Dark count rate (cps)")
    parser.add_argument("--init-loss",  type=float, default=None, dest="init_loss",  help="Insertion loss, linear fraction [0-1]")
    parser.add_argument("--source-err", type=float, default=None, dest="source_err", help="Source bit error rate [0-1]")
    parser.add_argument("--no-save",  action="store_true", help="Skip saving results to DB")
    parser.add_argument("--db",       type=str, default=DEFAULT_DB_PATH, help="Path to results SQLite DB")
    parser.add_argument("--error",    choices=["bars", "shade"], default="bars",
                        help="Error display: bars=min/max whiskers (default), shade=±1 std dev band")
    args = parser.parse_args()
    cfg  = load_config(args.config)
    if args.loss is not None:        cfg["fibre_loss_db_per_km"] = args.loss
    if args.det_eff is not None:     cfg["detector_efficiency"]  = args.det_eff
    if args.dark_count is not None:  cfg["dark_count_rate"]      = args.dark_count
    if args.init_loss is not None:   cfg["init_loss"]            = args.init_loss
    if args.source_err is not None:  cfg["source_error_rate"]    = args.source_err

    if args.config is not None:
        print(f"Note: node_loss_db from config ignored — L_node is the sweep axis")
    print(f"Sweep: L_node [0-6 dB]  |  Fixed: L={args.fibre} km  α={cfg['fibre_loss_db_per_km']} dB/km  η_d={cfg['detector_efficiency']}")

    db_conn = None if args.no_save else init_db(args.db)

    NLx = [0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]

    rates_bb84 = []
    rates_mdi  = []
    mins_bb84  = []
    maxs_bb84  = []
    stds_bb84  = []
    mins_mdi   = []
    maxs_mdi   = []
    stds_mdi   = []

    for nl in NLx:
        bb84, mdi = main(runtimes=args.runtimes, fibre=args.fibre,
                         lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
                         detEff=cfg["detector_efficiency"], darkCount=cfg["dark_count_rate"],
                         nodeLossDb=nl, sourceErrRate=cfg["source_error_rate"],
                         dephasingRate=cfg["dephasing_rate"], bsEff=cfg["bs_eff"])
        rates_bb84.append(bb84[3])
        rates_mdi.append(mdi[3])

        for rs, mins, maxs, stds in [(bb84[4], mins_bb84, maxs_bb84, stds_bb84),
                                     (mdi[4],  mins_mdi,  maxs_mdi,  stds_mdi)]:
            nz = [r for r in rs if r > 0]
            mins.append(min(nz) if nz else float('nan'))
            maxs.append(max(rs) if rs else float('nan'))
            stds.append(statistics.stdev([math.log(r) for r in nz]) if len(nz) > 1 else 0.0)

        if db_conn is not None:
            params = {
                "fibre_len":  args.fibre,
                "fibre_loss": cfg["fibre_loss_db_per_km"],
                "det_eff":    cfg["detector_efficiency"],
                "dark_count": cfg["dark_count_rate"],
                "init_loss":  cfg["init_loss"],
                "node_loss":  nl,
                "source_err": cfg["source_error_rate"],
                "dephasing":  cfg["dephasing_rate"],
                "bs_eff":     cfg["bs_eff"],
            }
            save_sweep_point(db_conn, "BB84", params, bb84[4], bb84[5], bb84[6],
                             script="node_loss", runtimes=args.runtimes, photons=1024)
            save_sweep_point(db_conn, "MDI",  params, mdi[4],  mdi[5],  mdi[6],
                             script="node_loss", runtimes=args.runtimes, photons=1024)

    if db_conn is not None:
        db_conn.close()

    abs_rates_bb84 = [r / 1000 for r in rates_bb84]
    abs_rates_mdi  = [r / 1000 for r in rates_mdi]

    base           = rates_bb84[0]
    rel_rates_bb84 = [r / base for r in rates_bb84]
    rel_rates_mdi  = [r / base for r in rates_mdi]

    fig, ax1 = plt.subplots()
    abs_mins_bb84 = [r / 1000 for r in mins_bb84]
    abs_maxs_bb84 = [r / 1000 for r in maxs_bb84]
    abs_mins_mdi  = [r / 1000 for r in mins_mdi]
    abs_maxs_mdi  = [r / 1000 for r in maxs_mdi]

    if args.error == 'bars':
        yerr_bb84 = [
            [max(r - m, 0) for r, m in zip(abs_rates_bb84, abs_mins_bb84)],
            [max(m - r, 0) for r, m in zip(abs_rates_bb84, abs_maxs_bb84)],
        ]
        yerr_mdi = [
            [max(r - m, 0) for r, m in zip(abs_rates_mdi, abs_mins_mdi)],
            [max(m - r, 0) for r, m in zip(abs_rates_mdi, abs_maxs_mdi)],
        ]
        ax1.errorbar(NLx, abs_rates_bb84, yerr=yerr_bb84, fmt='o-', label="BB84", capsize=3)
        ax1.errorbar(NLx, abs_rates_mdi,  yerr=yerr_mdi,  fmt='s-', label="MDI",  capsize=3)
    else:
        line1, = ax1.plot(NLx, abs_rates_bb84, 'o-', label="BB84")
        line2, = ax1.plot(NLx, abs_rates_mdi,  's-', label="MDI")
        lo1 = [r * math.exp(-s) for r, s in zip(abs_rates_bb84, stds_bb84)]
        hi1 = [r * math.exp(+s) for r, s in zip(abs_rates_bb84, stds_bb84)]
        lo2 = [r * math.exp(-s) for r, s in zip(abs_rates_mdi,  stds_mdi)]
        hi2 = [r * math.exp(+s) for r, s in zip(abs_rates_mdi,  stds_mdi)]
        ax1.fill_between(NLx, lo1, hi1, alpha=0.15, color=line1.get_color())
        ax1.fill_between(NLx, lo2, hi2, alpha=0.15, color=line2.get_color())
    ax1.set_xlabel("Node/connector loss (dB)")
    ax1.set_ylabel("Absolute secure key rate (kbps)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(NLx, rel_rates_bb84, 'o-', alpha=0)
    ax2.plot(NLx, rel_rates_mdi,  's-', alpha=0)
    ax2.set_ylabel("Relative secure key rate")
    ax2.set_yscale("log")

    ax1.legend()

    REALISTIC_MIN, REALISTIC_MAX = 0.5, 4.0
    ax1.axvspan(REALISTIC_MIN, REALISTIC_MAX, alpha=0.08, color='red', zorder=0)
    ax1.axvline(REALISTIC_MIN, color='black', linestyle=':', linewidth=1.2)
    ax1.axvline(REALISTIC_MAX, color='black', linestyle=':', linewidth=1.2)
    _ticks  = ax1.get_xticks()
    _xlim   = ax1.get_xlim()
    _dx     = 0.012 * abs(_xlim[1] - _xlim[0])
    _inv    = _xlim[0] > _xlim[1]
    _ha_min = 'left'  if _inv else 'right'
    _ha_max = 'right' if _inv else 'left'
    for _xv, _lbl, _ha in [(REALISTIC_MIN, "0.5", _ha_min), (REALISTIC_MAX, "4.0", _ha_max)]:
        if not any(abs(_xv - _t) < max(abs(_xv), 1e-9) * 1e-3 + 1e-9 for _t in _ticks):
            _xpos = _xv - _dx if _xv < (REALISTIC_MIN + REALISTIC_MAX) / 2 else _xv + _dx
            ax1.text(_xpos, 0.01, _lbl, transform=ax1.get_xaxis_transform(),
                     ha=_ha, va='bottom', fontsize=7, color='dimgray')
    ax1.text((REALISTIC_MIN + REALISTIC_MAX) / 2, 0.97, "Realistic hardware regime",
             transform=ax1.get_xaxis_transform(),
             ha='center', va='top', fontsize=7, color='darkred', alpha=0.7, style='italic')

    plt.title(f"Key rate vs node/connector loss: BB84 and MDI-QKD\n"
              f"$L$={args.fibre} km  |  $\\alpha$={cfg['fibre_loss_db_per_km']} dB/km  |  $\\eta_d$={cfg['detector_efficiency']}  |  $d_c$={cfg['dark_count_rate']} cps\n"
              f"$L_i$={cfg['init_loss']}  |  $\\varepsilon_s$={cfg['source_error_rate']}  |  $\\beta$={cfg['dephasing_rate']} /km  |  $\\eta_{{bs}}$={cfg['bs_eff']}")
    plt.show()
