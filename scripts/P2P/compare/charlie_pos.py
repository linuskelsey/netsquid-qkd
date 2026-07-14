"""
Key Rate vs Charlie Position
=============================
Sweeps Charlie's position along the Alice-Bob link (0.1 → 0.9 fraction from Alice).
MDI key rate shown vs position. BB84 plotted as flat dashed reference — unaffected by relay placement.
Total Alice-Bob distance is fixed; only the relay split changes.

Usage:
    python scripts/P2P/compare/charlie_pos.py [--config PATH] [--runtimes N] [--fibre F]
                                               [--error {bars,shade,sigma,iqr,sem}] [--workers N]
"""

import math
import os
import statistics
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser
from lib.db import DEFAULT_DB_PATH
import time
from lib.progress import Progress

import matplotlib.pyplot as plt


Cx = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def aggregate(key_rates):
    numeric = [r for r in key_rates if r != "nan"]
    valid   = [r for r in numeric if r > 0]
    avg     = sum(numeric) / len(numeric) if numeric else float('nan')
    mn      = min(valid)   if valid   else float('nan')
    mx      = max(numeric) if numeric else float('nan')
    std     = statistics.stdev([math.log(r) for r in valid]) if len(valid) > 1 else 0.0
    q25     = float(np.percentile(valid, 25)) if valid else float('nan')
    q75     = float(np.percentile(valid, 75)) if valid else float('nan')
    sem     = (statistics.stdev(valid) / math.sqrt(len(valid))) if len(valid) > 1 else 0.0
    return avg, mn, mx, std, q25, q75, sem, numeric


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes", type=int,   default=100)
    parser.add_argument("--fibre",    type=float, default=20,  help="Fixed total Alice-Bob distance (km)")
    parser.add_argument("--error",    choices=["bars", "shade", "sigma", "iqr", "sem"], default="bars",
                        help="Error display: bars=min/max whiskers (default), shade=±1σ log-space band, "
                             "sigma=±1σ whiskers, iqr=IQR 25–75th percentile, sem=±1 SEM")
    parser.add_argument("--no-db",     action="store_true", help="Disable DB writing")
    parser.add_argument("--workers",   type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory to save figure into (skips interactive display)")
    parser.add_argument("--compare-configs", nargs="+", metavar="PATH", dest="compare_configs",
                        help="2–4 config paths; overlay same Charlie position sweep under each preset on one figure")
    args = parser.parse_args()
    cfg  = load_config(args.config)

    print()
    print(f"Sweep: Charlie position [0.1–0.9]  |  Fixed: L={args.fibre} km  "
          f"α={cfg['fibre_loss_db_per_km']} dB/km  η_d={cfg['detector_efficiency']}  d_c={cfg['dark_count_rate']} cps")

    def _run_sweep(sweep_cfg, label=""):
        tag = f"[{label}] " if label else ""
        prog = Progress(1 + len(Cx))
        step = 0
        prog.update(step, f"{tag}BB84 reference running...")
        KA_bb84, KB_bb84, KR_bb84, KQ_bb84 = run_BB84_sims(
            runtimes=args.runtimes, fibreLen=args.fibre, photonCount=1024,
            sourceFreq=1e7, qSpeed=0.8,
            lenLoss=sweep_cfg["fibre_loss_db_per_km"], initLoss=sweep_cfg["init_loss"],
            detectorEffZ=sweep_cfg["detector_efficiency"], darkCount=sweep_cfg["dark_count_rate"],
            nodeLossDb=sweep_cfg["node_loss_db"], sourceErrRate=sweep_cfg["source_error_rate"],
            dephasingRate=sweep_cfg["dephasing_rate"],
            workers=args.workers, db_path=None if args.no_db else DEFAULT_DB_PATH,
        )
        _bb84_avg, _bb84_min, _bb84_max, _bb84_std, _bb84_q25, _bb84_q75, _bb84_sem, _ = aggregate(KR_bb84)
        step = 1
        prog.update(step, f"{tag}BB84 {_bb84_avg/1000:.2f} kbps  MDI running...")
        avgs_mdi, mins_mdi, maxs_mdi, stds_mdi, q25s_mdi, q75s_mdi, sems_mdi = [], [], [], [], [], [], []
        for cp in Cx:
            prog.update(step, f"{tag}Charlie pos: {cp}/{Cx[-1]}  MDI running...")
            _, _, KR_mdi, _ = run_mdi_sims(
                runtimes=args.runtimes, fibreLen=args.fibre, photonCount=1024,
                sourceFreq=1e7, qSpeed=0.8,
                lenLoss=sweep_cfg["fibre_loss_db_per_km"], initLoss=sweep_cfg["init_loss"],
                detectorEffZ=sweep_cfg["detector_efficiency"], darkCount=sweep_cfg["dark_count_rate"],
                nodeLossDb=sweep_cfg["node_loss_db"], sourceErrRate=sweep_cfg["source_error_rate"],
                dephasingRate=sweep_cfg["dephasing_rate"], bsEff=sweep_cfg["bs_eff"],
                charliePos=cp, workers=args.workers,
                db_path=None if args.no_db else DEFAULT_DB_PATH,
            )
            avg, mn, mx, std, q25, q75, sem, _ = aggregate(KR_mdi)
            avgs_mdi.append(avg); mins_mdi.append(mn); maxs_mdi.append(mx)
            stds_mdi.append(std); q25s_mdi.append(q25); q75s_mdi.append(q75); sems_mdi.append(sem)
            step += 1
            prog.update(step, f"{tag}Charlie pos: {cp}/{Cx[-1]}  MDI {avg/1000:.2f} kbps")
        prog.stop()
        return dict(
            bb84_avg=_bb84_avg, bb84_min=_bb84_min, bb84_max=_bb84_max,
            bb84_std=_bb84_std, bb84_q25=_bb84_q25, bb84_q75=_bb84_q75, bb84_sem=_bb84_sem,
            avgs_mdi=avgs_mdi, mins_mdi=mins_mdi, maxs_mdi=maxs_mdi,
            stds_mdi=stds_mdi, q25s_mdi=q25s_mdi, q75s_mdi=q75s_mdi, sems_mdi=sems_mdi,
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
            name = os.path.splitext(os.path.basename(path))[0]
            names.append(name)
            print(f"\n--- Config {ci+1}/{len(cc_paths)}: {name} ---")
            _ts = time.time()
            res = _run_sweep(cc_cfg, label=name)
            _m, _s = divmod(int(time.time() - _ts), 60)
            print(f"✓ {name} complete  {_m}m {_s:02d}s")
            c = colors[ci]
            ax1.plot(Cx, [r/1000 for r in res["avgs_mdi"]], '-', color=c, lw=1.5, label=f"MDI  — {name}")
            ax1.axhline(res["bb84_avg"]/1000, linestyle='--', color=c, lw=1.2, label=f"BB84 — {name}")
        ax1.set_yscale("log")
        ax1.set_xlabel("Charlie position (fraction from Alice)")
        ax1.set_ylabel("Secure key rate (kbps)")
        ax1.legend(fontsize=8)
        ax1.grid(True, alpha=0.3)
        plt.title(f"Key rate vs Charlie position — config comparison\n(BB84 dashed, MDI solid)\n{', '.join(names)}")
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

    bb84_avg = res["bb84_avg"]; bb84_min = res["bb84_min"]; bb84_max = res["bb84_max"]
    bb84_std = res["bb84_std"]; bb84_q25 = res["bb84_q25"]; bb84_q75 = res["bb84_q75"]; bb84_sem = res["bb84_sem"]
    avgs_mdi = res["avgs_mdi"]; mins_mdi = res["mins_mdi"]; maxs_mdi = res["maxs_mdi"]
    stds_mdi = res["stds_mdi"]; q25s_mdi = res["q25s_mdi"]; q75s_mdi = res["q75s_mdi"]; sems_mdi = res["sems_mdi"]

    # Convert to kbps
    abs_avg_mdi  = [r / 1000 for r in avgs_mdi]
    abs_min_mdi  = [r / 1000 for r in mins_mdi]
    abs_max_mdi  = [r / 1000 for r in maxs_mdi]
    abs_q25_mdi  = [r / 1000 for r in q25s_mdi]
    abs_q75_mdi  = [r / 1000 for r in q75s_mdi]
    abs_sem_mdi  = [r / 1000 for r in sems_mdi]
    abs_avg_bb84 = bb84_avg / 1000
    abs_min_bb84 = bb84_min / 1000
    abs_max_bb84 = bb84_max / 1000
    abs_q25_bb84 = bb84_q25 / 1000
    abs_q75_bb84 = bb84_q75 / 1000
    abs_sem_bb84 = bb84_sem / 1000

    base         = bb84_avg
    rel_mdi      = [r / base for r in avgs_mdi]
    rel_bb84     = bb84_avg / base  # = 1.0

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    if args.error == 'bars':
        yerr_mdi = [
            [max(r - m, 0) for r, m in zip(abs_avg_mdi, abs_min_mdi)],
            [max(m - r, 0) for r, m in zip(abs_avg_mdi, abs_max_mdi)],
        ]
        ax1.errorbar(Cx, abs_avg_mdi, yerr=yerr_mdi, fmt='s-', label="MDI", capsize=3)
        ax1.axhspan(abs_min_bb84, abs_max_bb84, alpha=0.10, color='steelblue')
    elif args.error == 'shade':
        lo_mdi = [r * math.exp(-s) for r, s in zip(abs_avg_mdi, stds_mdi)]
        hi_mdi = [r * math.exp(+s) for r, s in zip(abs_avg_mdi, stds_mdi)]
        line_mdi, = ax1.plot(Cx, abs_avg_mdi, 's-', label="MDI")
        ax1.fill_between(Cx, lo_mdi, hi_mdi, alpha=0.15, color=line_mdi.get_color())
        ax1.axhspan(abs_avg_bb84 * math.exp(-bb84_std),
                    abs_avg_bb84 * math.exp(+bb84_std), alpha=0.10, color='steelblue')
    elif args.error == 'sigma':
        lo_mdi = [r * (1 - math.exp(-s)) for r, s in zip(abs_avg_mdi, stds_mdi)]
        hi_mdi = [r * (math.exp(s) - 1)  for r, s in zip(abs_avg_mdi, stds_mdi)]
        yerr_mdi = [lo_mdi, hi_mdi]
        ax1.errorbar(Cx, abs_avg_mdi, yerr=yerr_mdi, fmt='s-', label="MDI", capsize=3)
        ax1.axhspan(abs_avg_bb84 * (1 - math.exp(-bb84_std)),
                    abs_avg_bb84 * (math.exp(bb84_std) - 1), alpha=0.10, color='steelblue')
    elif args.error == 'iqr':
        yerr_mdi = [
            [max(r - q, 0) for r, q in zip(abs_avg_mdi, abs_q25_mdi)],
            [max(q - r, 0) for r, q in zip(abs_avg_mdi, abs_q75_mdi)],
        ]
        ax1.errorbar(Cx, abs_avg_mdi, yerr=yerr_mdi, fmt='s-', label="MDI", capsize=3)
        ax1.axhspan(abs_q25_bb84, abs_q75_bb84, alpha=0.10, color='steelblue')
    else:  # sem
        yerr_mdi = [abs_sem_mdi, abs_sem_mdi]
        ax1.errorbar(Cx, abs_avg_mdi, yerr=yerr_mdi, fmt='s-', label="MDI", capsize=3)
        ax1.axhspan(abs_avg_bb84 - abs_sem_bb84, abs_avg_bb84 + abs_sem_bb84,
                    alpha=0.10, color='steelblue')

    ax1.axhline(abs_avg_bb84, linestyle='--', color='steelblue', label="BB84 (reference)")

    ax2.plot(Cx, rel_mdi, 's-', alpha=0)
    ax2.axhline(rel_bb84, linestyle='--', alpha=0)

    ax1.set_xlabel("Charlie position (fraction from Alice)")
    ax1.set_ylabel("Absolute secure key rate (kbps)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3)
    ax2.set_ylabel("Relative secure key rate")
    ax2.set_yscale("log")
    ax1.legend()

    REALISTIC_MIN, REALISTIC_MAX = 0.4, 0.6
    ax1.axvspan(REALISTIC_MIN, REALISTIC_MAX, alpha=0.08, color='red', zorder=0)
    ax1.axvline(REALISTIC_MIN, color='black', linestyle=':', linewidth=1.2)
    ax1.axvline(REALISTIC_MAX, color='black', linestyle=':', linewidth=1.2)
    _ticks = ax1.get_xticks()
    _xlim  = ax1.get_xlim()
    _dx    = 0.012 * abs(_xlim[1] - _xlim[0])
    for _xv, _lbl, _ha in [(REALISTIC_MIN, "0.4", 'right'), (REALISTIC_MAX, "0.6", 'left')]:
        if not any(abs(_xv - _t) < max(abs(_xv), 1e-9) * 1e-3 + 1e-9 for _t in _ticks):
            _xpos = _xv - _dx if _xv < 0.5 else _xv + _dx
            ax1.text(_xpos, 0.01, _lbl, transform=ax1.get_xaxis_transform(),
                     ha=_ha, va='bottom', fontsize=7, color='dimgray')
    ax1.text(0.5, 0.97, "Near-symmetric regime",
             transform=ax1.get_xaxis_transform(),
             ha='center', va='top', fontsize=7, color='darkred', alpha=0.7, style='italic')

    plt.title(f"Key rate vs Charlie position: MDI-QKD (BB84 reference)\n"
              f"$L$={args.fibre} km  |  $\\alpha$={cfg['fibre_loss_db_per_km']} dB/km  |  "
              f"$\\eta_d$={cfg['detector_efficiency']}  |  $d_c$={cfg['dark_count_rate']} cps\n"
              f"$L_i$={cfg['init_loss']}  |  $L_n$={cfg['node_loss_db']} dB  |  "
              f"$\\varepsilon_s$={cfg['source_error_rate']}  |  $\\beta$={cfg['dephasing_rate']} /km  |  "
              f"$\\eta_{{bs}}$={cfg['bs_eff']}")
    plt.tight_layout()
    if args.output_dir:
        os.makedirs(args.output_dir, exist_ok=True)
        fig_name = os.path.splitext(os.path.basename(__file__))[0] + ".png"
        plt.savefig(os.path.join(args.output_dir, fig_name), dpi=150, bbox_inches="tight")
        plt.close()
    else:
        plt.show()
