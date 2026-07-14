"""
Key Rate vs Detector Basis Bias Comparison
===========================================
Sweeps X-basis detector efficiency η_X (1.0->0.5) with η_Z fixed at detector_efficiency.
Note: detector_efficiency in --config sets η_Z (fixed axis); η_X is the sweep axis.

Usage:
    python scripts/compare/basis_bias.py [--config PATH] [--runtimes N] [--fibre F]
                                         [--loss F] [--det-eff-z F] [--dark-count N]
                                         [--init-loss F] [--node-loss F] [--source-err F]
                                         [--workers N]

Defaults (no --config):
    detector_eff_x          swept 1.0->0.5  (sweep axis)
    detector_eff_z          1.0             (fixed; set via --det-eff-z or config detector_efficiency)
    fibre_loss_db_per_km    0.2  dB/km
    dark_count_rate         0    cps
    init_loss               0.0
    node_loss_db            0.0  dB
    source_error_rate       0.0
    fibre                   20   km
    runtimes                100
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append("BB84/")
sys.path.append("MDI/")
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.db import DEFAULT_DB_PATH
from lib.functions import load_config, config_arg_parser
import time
from lib.progress import Progress

import matplotlib.pyplot as plt
import math
import statistics
import numpy as np


def qber(keyA, keyB):
    if not keyA or not keyB:
        return None
    length = min(len(keyA), len(keyB))
    if length == 0:
        return None
    errors = sum(a != b for a, b in zip(keyA[:length], keyB[:length]))
    return errors / length


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


def main(runtimes=10, photons=1024, fibre=100, freq=1e7, speed=0.8, lenLoss=0, initLoss=0, detEffZ=1, detEffX=1, darkCount=0, nodeLossDb=0.0, sourceErrRate=0.0, dephasingRate=0.0, bsEff=1.0, workers=None, no_db=False):
    KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, QBERList_bb84 = run_BB84_sims(
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
        workers       = workers,
        db_path       = None if no_db else DEFAULT_DB_PATH,
    )
    KeyListA_mdi, KeyListB_mdi, KeyRateList_mdi, QBERList_mdi = run_mdi_sims(
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
        workers       = workers,
        db_path       = None if no_db else DEFAULT_DB_PATH,
    )
    bb84_stats = aggregate_summary(KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, QBERList_bb84)
    mdi_stats  = aggregate_summary(KeyListA_mdi,  KeyListB_mdi,  KeyRateList_mdi,  QBERList_mdi)
    return bb84_stats, mdi_stats


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes",    type=int,   default=100)
    parser.add_argument("--fibre",       type=float, default=20,   help="Fixed fibre length (km)")
    parser.add_argument("--loss",        type=float, default=None, help="Fibre loss (dB/km)")
    parser.add_argument("--det-eff-z",   type=float, default=None, dest="det_eff_z", help="Fixed Z-basis detector efficiency η_Z [0-1]")
    parser.add_argument("--dark-count",  type=int,   default=None, dest="dark_count", help="Dark count rate (cps)")
    parser.add_argument("--init-loss",   type=float, default=None, dest="init_loss",  help="Insertion loss, linear fraction [0-1]")
    parser.add_argument("--node-loss",   type=float, default=None, dest="node_loss",  help="Receiver node insertion loss (dB)")
    parser.add_argument("--source-err",  type=float, default=None, dest="source_err", help="Source bit error rate [0-1]")
    parser.add_argument("--no-db",     action="store_true", help="Disable DB writing")
    parser.add_argument("--workers",     type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--error",    choices=["bars", "shade", "sigma", "iqr", "sem"], default="bars",
                        help="Error display: bars=min/max whiskers (default), shade=±1 std dev band")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to save figure into (skips interactive display)")
    parser.add_argument("--compare-configs", nargs="+", metavar="PATH", dest="compare_configs",
                        help="2–4 config paths; overlay same basis bias sweep under each preset on one figure")
    args = parser.parse_args()
    cfg  = load_config(args.config)
    if args.loss is not None:       cfg["fibre_loss_db_per_km"] = args.loss
    if args.det_eff_z is not None:  cfg["detector_efficiency"]  = args.det_eff_z
    if args.dark_count is not None: cfg["dark_count_rate"]      = args.dark_count
    if args.init_loss is not None:  cfg["init_loss"]            = args.init_loss
    if args.node_loss is not None:  cfg["node_loss_db"]         = args.node_loss
    if args.source_err is not None: cfg["source_error_rate"]    = args.source_err

    print()
    det_eff_z = cfg["detector_efficiency"]
    print(f"Sweep: η_X [1.0->0.5]  |  Fixed: η_Z={det_eff_z}  L={args.fibre} km  α={cfg['fibre_loss_db_per_km']} dB/km")

    Bx = [1.0, 0.99, 0.95, 0.9, 0.8, 0.7, 0.65, 0.6, 0.5]

    def _run_sweep(sweep_cfg, label=""):
        _det_eff_z = sweep_cfg["detector_efficiency"]
        prog = Progress(len(Bx))
        step = 0
        r_bb84, r_mdi = [], []
        mins_b, maxs_b, stds_b, q25s_b, q75s_b, sems_b = [], [], [], [], [], []
        mins_m, maxs_m, stds_m, q25s_m, q75s_m, sems_m = [], [], [], [], [], []
        for ex in Bx:
            tag = f"[{label}] " if label else ""
            prog.update(step, f"{tag}Basis bias: {ex}/{Bx[-1]}  BB84+MDI running...")
            bb84, mdi = main(runtimes=args.runtimes, fibre=args.fibre,
                             lenLoss=sweep_cfg["fibre_loss_db_per_km"], initLoss=sweep_cfg["init_loss"],
                             detEffZ=_det_eff_z, detEffX=ex,
                             darkCount=sweep_cfg["dark_count_rate"],
                             nodeLossDb=sweep_cfg["node_loss_db"], sourceErrRate=sweep_cfg["source_error_rate"],
                             dephasingRate=sweep_cfg["dephasing_rate"], bsEff=sweep_cfg["bs_eff"],
                             workers=args.workers, no_db=args.no_db)
            r_bb84.append(bb84[3]); r_mdi.append(mdi[3])
            for rs, mins, maxs, stds, q25s, q75s, sems in [
                    (bb84[4], mins_b, maxs_b, stds_b, q25s_b, q75s_b, sems_b),
                    (mdi[4],  mins_m, maxs_m, stds_m, q25s_m, q75s_m, sems_m)]:
                nz = [r for r in rs if r > 0]
                mins.append(min(nz) if nz else float('nan'))
                maxs.append(max(rs) if rs else float('nan'))
                stds.append(statistics.stdev([math.log(r) for r in nz]) if len(nz) > 1 else 0.0)
                q25s.append(float(np.percentile(nz, 25)) if nz else float('nan'))
                q75s.append(float(np.percentile(nz, 75)) if nz else float('nan'))
                sems.append(statistics.stdev(nz) / math.sqrt(len(nz)) if len(nz) > 1 else 0.0)
            step += 1
            prog.update(step, f"{tag}Basis bias: {ex}/{Bx[-1]}  BB84 {bb84[3]/1000:.2f} | MDI {mdi[3]/1000:.2f} kbps")
        prog.stop()
        return dict(
            rates_bb84=r_bb84, rates_mdi=r_mdi,
            mins_bb84=mins_b, maxs_bb84=maxs_b, stds_bb84=stds_b,
            q25s_bb84=q25s_b, q75s_bb84=q75s_b, sems_bb84=sems_b,
            mins_mdi=mins_m,  maxs_mdi=maxs_m,  stds_mdi=stds_m,
            q25s_mdi=q25s_m,  q75s_mdi=q75s_m,  sems_mdi=sems_m,
        )

    if args.compare_configs:
        cc_paths = args.compare_configs
        if not (2 <= len(cc_paths) <= 4):
            parser.error("--compare-configs requires 2–4 paths")
        colors = [plt.cm.tab10(i) for i in range(len(cc_paths))]
        fig, ax1 = plt.subplots()
        names = []
        for ci, path in enumerate(cc_paths):
            cc_cfg = load_config(path)
            if args.loss is not None:        cc_cfg["fibre_loss_db_per_km"] = args.loss
            if args.dark_count is not None:  cc_cfg["dark_count_rate"]      = args.dark_count
            if args.init_loss is not None:   cc_cfg["init_loss"]            = args.init_loss
            if args.node_loss is not None:   cc_cfg["node_loss_db"]         = args.node_loss
            if args.source_err is not None:  cc_cfg["source_error_rate"]    = args.source_err
            if args.det_eff_z is not None:   cc_cfg["detector_efficiency"]  = args.det_eff_z
            name = os.path.splitext(os.path.basename(path))[0]
            names.append(name)
            print(f"\n--- Config {ci+1}/{len(cc_paths)}: {name} ---")
            _ts = time.time()
            res = _run_sweep(cc_cfg, label=name)
            _m, _s = divmod(int(time.time() - _ts), 60)
            print(f"✓ {name} complete  {_m}m {_s:02d}s")
            c = colors[ci]
            ax1.plot(Bx, [r/1000 for r in res["rates_bb84"]], '--', color=c, lw=1.5, label=f"BB84 — {name}")
            ax1.plot(Bx, [r/1000 for r in res["rates_mdi"]],  '-',  color=c, lw=1.5, label=f"MDI  — {name}")
        ax1.set_yscale("log")
        ax1.invert_xaxis()
        ax1.set_xlabel(r"X-basis detector efficiency $\eta_X$")
        ax1.set_ylabel("Secure key rate (kbps)")
        ax1.legend(fontsize=8)
        ax1.grid(True, alpha=0.3)
        plt.title(f"Key rate vs detector basis bias — config comparison\n(BB84 dashed, MDI solid)\n{', '.join(names)}")
        plt.tight_layout()
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)
            fn = os.path.splitext(os.path.basename(__file__))[0] + "_compare.png"
            plt.savefig(os.path.join(args.output_dir, fn), dpi=150, bbox_inches="tight")
            plt.close()
        else:
            plt.show()
        sys.exit(0)

    total_start = time.time()
    res = _run_sweep(cfg)
    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    rates_bb84 = res["rates_bb84"]; rates_mdi = res["rates_mdi"]
    mins_bb84  = res["mins_bb84"];  maxs_bb84 = res["maxs_bb84"]; stds_bb84 = res["stds_bb84"]
    mins_mdi   = res["mins_mdi"];   maxs_mdi  = res["maxs_mdi"];  stds_mdi  = res["stds_mdi"]
    q25s_bb84  = res["q25s_bb84"];  q75s_bb84 = res["q75s_bb84"]; sems_bb84 = res["sems_bb84"]
    q25s_mdi   = res["q25s_mdi"];   q75s_mdi  = res["q75s_mdi"];  sems_mdi  = res["sems_mdi"]

    abs_rates_bb84 = [r / 1000 for r in rates_bb84]
    abs_rates_mdi  = [r / 1000 for r in rates_mdi]

    base           = rates_bb84[0]
    rel_rates_bb84 = [r / base for r in rates_bb84]
    rel_rates_mdi  = [r / base for r in rates_mdi]

    fig, ax1 = plt.subplots()
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
        ax1.errorbar(Bx, abs_rates_bb84, yerr=yerr_bb84, fmt='o-', label="BB84", capsize=3)
        ax1.errorbar(Bx, abs_rates_mdi,  yerr=yerr_mdi,  fmt='s-', label="MDI",  capsize=3)
    else:
        line1, = ax1.plot(Bx, abs_rates_bb84, 'o-', label="BB84")
        line2, = ax1.plot(Bx, abs_rates_mdi,  's-', label="MDI")
        lo1 = [r * math.exp(-s) for r, s in zip(abs_rates_bb84, stds_bb84)]
        hi1 = [r * math.exp(+s) for r, s in zip(abs_rates_bb84, stds_bb84)]
        lo2 = [r * math.exp(-s) for r, s in zip(abs_rates_mdi,  stds_mdi)]
        hi2 = [r * math.exp(+s) for r, s in zip(abs_rates_mdi,  stds_mdi)]
        ax1.fill_between(Bx, lo1, hi1, alpha=0.15, color=line1.get_color())
        ax1.fill_between(Bx, lo2, hi2, alpha=0.15, color=line2.get_color())
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

    REALISTIC_MIN, REALISTIC_MAX = 0.65, 0.90
    ax1.axvspan(REALISTIC_MIN, REALISTIC_MAX, alpha=0.08, color='red', zorder=0)
    ax1.axvline(REALISTIC_MIN, color='black', linestyle=':', linewidth=1.2)
    ax1.axvline(REALISTIC_MAX, color='black', linestyle=':', linewidth=1.2)
    _ticks  = ax1.get_xticks()
    _xlim   = ax1.get_xlim()
    _dx     = 0.012 * abs(_xlim[1] - _xlim[0])
    _inv    = _xlim[0] > _xlim[1]
    _ha_min = 'left'  if _inv else 'right'
    _ha_max = 'right' if _inv else 'left'
    for _xv, _lbl, _ha in [(REALISTIC_MIN, "0.65", _ha_min), (REALISTIC_MAX, "0.90", _ha_max)]:
        if not any(abs(_xv - _t) < max(abs(_xv), 1e-9) * 1e-3 + 1e-9 for _t in _ticks):
            _xpos = _xv - _dx if _xv < (REALISTIC_MIN + REALISTIC_MAX) / 2 else _xv + _dx
            ax1.text(_xpos, 0.01, _lbl, transform=ax1.get_xaxis_transform(),
                     ha=_ha, va='bottom', fontsize=7, color='dimgray')
    ax1.text((REALISTIC_MIN + REALISTIC_MAX) / 2, 0.97, "Realistic hardware regime",
             transform=ax1.get_xaxis_transform(),
             ha='center', va='top', fontsize=7, color='darkred', alpha=0.7, style='italic')

    plt.title(f"Key rate vs detector basis bias: BB84 and MDI-QKD\n"
              f"$\\eta_Z$={det_eff_z}  |  $L$={args.fibre} km  |  $\\alpha$={cfg['fibre_loss_db_per_km']} dB/km  |  $d_c$={cfg['dark_count_rate']} cps\n"
              f"$L_i$={cfg['init_loss']}  |  $L_n$={cfg['node_loss_db']} dB  |  $\\varepsilon_s$={cfg['source_error_rate']}  |  $\\beta$={cfg['dephasing_rate']} /km  |  $\\eta_{{bs}}$={cfg['bs_eff']}")
    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        fig_name = os.path.splitext(os.path.basename(__file__))[0] + ".png"
        plt.savefig(os.path.join(args.output_dir, fig_name), dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
