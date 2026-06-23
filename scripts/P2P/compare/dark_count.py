"""
Key Rate vs Dark Count Rate Comparison
========================================
Sweeps dark count rate (0-10000 cps). Fixed fibre length, loss, and detector efficiency.
Note: dark_count_rate in --config is ignored; d_c is the sweep axis.

Usage:
    python scripts/compare/dark_count.py [--config PATH] [--runtimes N] [--fibre F]
                                         [--loss F] [--det-eff F] [--init-loss F]
                                         [--workers N]

Defaults (no --config):
    dark_count_rate         swept 0-250 cps  (sweep axis — config value ignored)
    fibre_loss_db_per_km    0.2  dB/km  — pass --config configs/layer0_ideal.json for idealised run
    detector_efficiency     1.0
    init_loss               0.0  dB
    fibre                   20   km
    runtimes                100
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser
import time
from lib.progress import Progress

import matplotlib.pyplot as plt
import math
import statistics
import numpy as np



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


def aggregate_summary(KeyListA, KeyListB, KeyRateList, QBERList):
    qbers, key_rates, key_lengths = [], [], []
    for i, (keyA, keyB, q) in enumerate(zip(KeyListA, KeyListB, QBERList)):
        if q is not None:
            qbers.append(q)
        if keyA != "nan":
            key_rates.append(KeyRateList[i])
            key_lengths.append(min(len(keyA), len(keyB)))
    avg_qber    = sum(qbers) / len(qbers)             if qbers      else float('nan')
    avg_kr      = sum(key_rates) / len(key_rates)     if key_rates  else float('nan')
    avg_key_len = sum(key_lengths) / len(key_lengths) if key_lengths else float('nan')
    return len(key_rates), avg_key_len, avg_qber, avg_kr, key_rates, qbers, key_lengths


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


def main(runtimes=10, photons=1024, fibre=100, freq=1e7, speed=0.8, lenLoss=0, initLoss=0, detEff=1, darkCount=0, nodeLossDb=0.0, sourceErrRate=0.0, dephasingRate=0.0, bsEff=1.0, workers=None):
    # BB84 run ==================================================
    KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, QBERList_bb84 = run_BB84_sims(
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
        workers       = workers,
    )

    # MDI run ===================================================
    KeyListA_mdi, KeyListB_mdi, KeyRateList_mdi, QBERList_mdi = run_mdi_sims(
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
        workers       = workers,
    )

    # Aggregate stats ===========================================
    bb84_stats = aggregate_summary(KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, QBERList_bb84)
    mdi_stats  = aggregate_summary(KeyListA_mdi,  KeyListB_mdi,  KeyRateList_mdi,  QBERList_mdi)

    return bb84_stats, mdi_stats

if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes",  type=int,   default=100)
    parser.add_argument("--fibre",     type=float, default=20,   help="Fixed fibre length (km)")
    parser.add_argument("--loss",      type=float, default=None, help="Fibre loss (dB/km)")
    parser.add_argument("--det-eff",   type=float, default=None, dest="det_eff",   help="Detector efficiency [0-1]")
    parser.add_argument("--init-loss", type=float, default=None, dest="init_loss", help="Insertion loss, linear fraction [0-1] (e.g. 0.1 = 10%%)")
    parser.add_argument("--node-loss",  type=float, default=None, dest="node_loss",  help="Receiver node insertion loss (dB)")
    parser.add_argument("--source-err", type=float, default=None, dest="source_err", help="Source bit error rate [0-1]")
    parser.add_argument("--workers",    type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--error",    choices=["bars", "shade", "sigma", "iqr", "sem"], default="bars",
                        help="Error display: bars=min/max whiskers (default), shade=±1 std dev band")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to save figure into (skips interactive display)")
    args = parser.parse_args()
    cfg  = load_config(args.config)
    if args.loss is not None:        cfg["fibre_loss_db_per_km"] = args.loss
    if args.det_eff is not None:     cfg["detector_efficiency"]  = args.det_eff
    if args.init_loss is not None:   cfg["init_loss"]            = args.init_loss
    if args.node_loss is not None:   cfg["node_loss_db"]         = args.node_loss
    if args.source_err is not None:  cfg["source_error_rate"]    = args.source_err

    print()
    if args.config is not None and cfg["dark_count_rate"] != 0:
        print(f"Note: dark_count_rate={cfg['dark_count_rate']} from config ignored — d_c is the sweep axis")
    print(f"Sweep: d_c [0-250 cps]  |  Fixed: L={args.fibre} km  α={cfg['fibre_loss_db_per_km']} dB/km  η_d={cfg['detector_efficiency']}")

    DCx = [0, 1, 5, 10, 25, 50, 75, 100, 150, 200, 250]

    total_start = time.time()
    prog = Progress(len(DCx))
    step = 0

    lengths_bb84 = []
    lengths_mdi  = []
    qbers_bb84   = []
    qbers_mdi    = []
    rates_bb84   = []
    rates_mdi    = []
    mins_bb84    = []
    maxs_bb84    = []
    stds_bb84    = []
    mins_mdi     = []
    maxs_mdi     = []
    stds_mdi     = []
    q25s_bb84    = []
    q75s_bb84    = []
    sems_bb84    = []
    q25s_mdi     = []
    q75s_mdi     = []
    sems_mdi     = []

    for dc in DCx:
        prog.update(step, f"Dark count: {dc}/{DCx[-1]} cps  BB84+MDI running...")
        bb84, mdi = main(runtimes=args.runtimes, fibre=args.fibre,
                         lenLoss=cfg["fibre_loss_db_per_km"], initLoss=cfg["init_loss"],
                         detEff=cfg["detector_efficiency"], darkCount=dc,
                         nodeLossDb=cfg["node_loss_db"], sourceErrRate=cfg["source_error_rate"],
                         dephasingRate=cfg["dephasing_rate"], bsEff=cfg["bs_eff"],
                         workers=args.workers)

        lengths_bb84.append(bb84[1])
        qbers_bb84.append(bb84[2])
        rates_bb84.append(bb84[3])

        lengths_mdi.append(mdi[1])
        qbers_mdi.append(mdi[2])
        rates_mdi.append(mdi[3])

        for rs, mins, maxs, stds, q25s, q75s, sems in [
                (bb84[4], mins_bb84, maxs_bb84, stds_bb84, q25s_bb84, q75s_bb84, sems_bb84),
                (mdi[4],  mins_mdi,  maxs_mdi,  stds_mdi,  q25s_mdi,  q75s_mdi,  sems_mdi)]:
            nz = [r for r in rs if r > 0]
            mins.append(min(nz) if nz else float('nan'))
            maxs.append(max(rs) if rs else float('nan'))
            stds.append(statistics.stdev([math.log(r) for r in nz]) if len(nz) > 1 else 0.0)
            q25s.append(float(np.percentile(nz, 25)) if nz else float('nan'))
            q75s.append(float(np.percentile(nz, 75)) if nz else float('nan'))
            sems.append(statistics.stdev(nz) / math.sqrt(len(nz)) if len(nz) > 1 else 0.0)
        step += 1
        prog.update(step, f"Dark count: {dc}/{DCx[-1]} cps  BB84 {bb84[3]/1000:.2f} | MDI {mdi[3]/1000:.2f} kbps")

    prog.stop()
    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    # Store absolute rates before normalising
    abs_rates_bb84 = [r / 1000 for r in rates_bb84]  # convert to kbps
    abs_rates_mdi  = [r / 1000 for r in rates_mdi]

    # Then normalise for relative
    base           = rates_bb84[0]
    rel_rates_bb84 = [r / base for r in rates_bb84]
    rel_rates_mdi  = [r / base for r in rates_mdi]

    fig, ax1 = plt.subplots()

    # Primary axis — absolute scale
    abs_mins_bb84 = [r / 1000 for r in mins_bb84]
    abs_maxs_bb84 = [r / 1000 for r in maxs_bb84]
    abs_mins_mdi  = [r / 1000 for r in mins_mdi]
    abs_q25s_bb84 = [r / 1000 for r in q25s_bb84]
    abs_q75s_bb84 = [r / 1000 for r in q75s_bb84]
    abs_sems_bb84 = [r / 1000 for r in sems_bb84]
    abs_q25s_mdi  = [r / 1000 for r in q25s_mdi]
    abs_q75s_mdi  = [r / 1000 for r in q75s_mdi]
    abs_sems_mdi  = [r / 1000 for r in sems_mdi]
    abs_maxs_mdi  = [r / 1000 for r in maxs_mdi]

    if args.error in ('bars', 'sigma', 'iqr', 'sem'):
        if args.error == 'bars':
            yerr_bb84 = [
                [max(r - m, 0) for r, m in zip(abs_rates_bb84, abs_mins_bb84)],
                [max(m - r, 0) for r, m in zip(abs_rates_bb84, abs_maxs_bb84)],
            ]
            yerr_mdi = [
                [max(r - m, 0) for r, m in zip(abs_rates_mdi, abs_mins_mdi)],
                [max(m - r, 0) for r, m in zip(abs_rates_mdi, abs_maxs_mdi)],
            ]
        elif args.error == 'sigma':
            yerr_bb84 = [
                [r * (1 - math.exp(-s)) for r, s in zip(abs_rates_bb84, stds_bb84)],
                [r * (math.exp(s) - 1)  for r, s in zip(abs_rates_bb84, stds_bb84)],
            ]
            yerr_mdi = [
                [r * (1 - math.exp(-s)) for r, s in zip(abs_rates_mdi, stds_mdi)],
                [r * (math.exp(s) - 1)  for r, s in zip(abs_rates_mdi, stds_mdi)],
            ]
        elif args.error == 'iqr':
            yerr_bb84 = [
                [max(r - q25, 0) for r, q25 in zip(abs_rates_bb84, abs_q25s_bb84)],
                [max(q75 - r, 0) for r, q75 in zip(abs_rates_bb84, abs_q75s_bb84)],
            ]
            yerr_mdi = [
                [max(r - q25, 0) for r, q25 in zip(abs_rates_mdi, abs_q25s_mdi)],
                [max(q75 - r, 0) for r, q75 in zip(abs_rates_mdi, abs_q75s_mdi)],
            ]
        elif args.error == 'sem':
            yerr_bb84 = [abs_sems_bb84, abs_sems_bb84]
            yerr_mdi  = [abs_sems_mdi,  abs_sems_mdi]
        ax1.errorbar(DCx, abs_rates_bb84, yerr=yerr_bb84, fmt='o-', label="BB84", capsize=3)
        ax1.errorbar(DCx, abs_rates_mdi,  yerr=yerr_mdi,  fmt='s-', label="MDI",  capsize=3)
    else:
        line1, = ax1.plot(DCx, abs_rates_bb84, 'o-', label="BB84")
        line2, = ax1.plot(DCx, abs_rates_mdi,  's-', label="MDI")
        lo1 = [r * math.exp(-s) for r, s in zip(abs_rates_bb84, stds_bb84)]
        hi1 = [r * math.exp(+s) for r, s in zip(abs_rates_bb84, stds_bb84)]
        lo2 = [r * math.exp(-s) for r, s in zip(abs_rates_mdi,  stds_mdi)]
        hi2 = [r * math.exp(+s) for r, s in zip(abs_rates_mdi,  stds_mdi)]
        ax1.fill_between(DCx, lo1, hi1, alpha=0.15, color=line1.get_color())
        ax1.fill_between(DCx, lo2, hi2, alpha=0.15, color=line2.get_color())
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

    REALISTIC_MIN, REALISTIC_MAX = 1, 100
    ax1.axvspan(REALISTIC_MIN, REALISTIC_MAX, alpha=0.08, color='red', zorder=0)
    ax1.axvline(REALISTIC_MIN, color='black', linestyle=':', linewidth=1.2)
    ax1.axvline(REALISTIC_MAX, color='black', linestyle=':', linewidth=1.2)
    _ticks  = ax1.get_xticks()
    _xlim   = ax1.get_xlim()
    _dx     = 0.012 * abs(_xlim[1] - _xlim[0])
    _inv    = _xlim[0] > _xlim[1]
    _ha_min = 'left'  if _inv else 'right'
    _ha_max = 'right' if _inv else 'left'
    for _xv, _lbl, _ha in [(REALISTIC_MIN, "1", _ha_min), (REALISTIC_MAX, "100", _ha_max)]:
        if not any(abs(_xv - _t) < max(abs(_xv), 1e-9) * 1e-3 + 1e-9 for _t in _ticks):
            _xpos = _xv - _dx if _xv < (REALISTIC_MIN + REALISTIC_MAX) / 2 else _xv + _dx
            ax1.text(_xpos, 0.01, _lbl, transform=ax1.get_xaxis_transform(),
                     ha=_ha, va='bottom', fontsize=7, color='dimgray')
    ax1.text((REALISTIC_MIN + REALISTIC_MAX) / 2, 0.97, "Realistic hardware regime",
             transform=ax1.get_xaxis_transform(),
             ha='center', va='top', fontsize=7, color='darkred', alpha=0.7, style='italic')

    plt.title(f"Key rate vs dark count rate: BB84 and MDI-QKD\n"
              f"$L$={args.fibre} km  |  $\\alpha$={cfg['fibre_loss_db_per_km']} dB/km  |  $\\eta_d$={cfg['detector_efficiency']}\n"
              f"$L_i$={cfg['init_loss']}  |  $L_n$={cfg['node_loss_db']} dB  |  $\\varepsilon_s$={cfg['source_error_rate']}  |  $\\beta$={cfg['dephasing_rate']} /km  |  $\\eta_{{bs}}$={cfg['bs_eff']}")
    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        fig_name = os.path.splitext(os.path.basename(__file__))[0] + ".png"
        plt.savefig(os.path.join(args.output_dir, fig_name), dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
