"""
Key Rate vs Charlie Position
=============================
Sweeps Charlie's position along the Alice-Bob link (0.1 → 0.9 fraction from Alice).
MDI key rate shown vs position. BB84 plotted as flat dashed reference — unaffected by relay placement.
Total Alice-Bob distance is fixed; only the relay split changes.

Usage:
    python scripts/P2P/compare/charlie_pos.py [--config PATH] [--runtimes N] [--fibre F]
                                               [--error {bars,shade}] [--no-save] [--db PATH]
"""

import math
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims
from lib.functions import load_config, config_arg_parser
from lib.db import init_db, save_sweep_point, DEFAULT_DB_PATH

import matplotlib.pyplot as plt


Cx = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def aggregate(key_rates):
    numeric = [r for r in key_rates if r != "nan"]
    valid   = [r for r in numeric if r > 0]
    avg     = sum(numeric) / len(numeric) if numeric else float('nan')
    mn      = min(valid)   if valid   else float('nan')
    mx      = max(numeric) if numeric else float('nan')
    std     = statistics.stdev([math.log(r) for r in valid]) if len(valid) > 1 else 0.0
    return avg, mn, mx, std, numeric


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--runtimes", type=int,   default=100)
    parser.add_argument("--fibre",    type=float, default=50,  help="Fixed total Alice-Bob distance (km)")
    parser.add_argument("--error",    choices=["bars", "shade"], default="bars",
                        help="Error display: bars=min/max whiskers (default), shade=±1σ log-space band")
    parser.add_argument("--no-save",  action="store_true", help="Skip saving results to DB")
    parser.add_argument("--db",       type=str, default=DEFAULT_DB_PATH, help="Path to results SQLite DB")
    args = parser.parse_args()
    cfg  = load_config(args.config)

    print(f"Sweep: Charlie position [0.1–0.9]  |  Fixed: L={args.fibre} km  "
          f"α={cfg['fibre_loss_db_per_km']} dB/km  η_d={cfg['detector_efficiency']}  d_c={cfg['dark_count_rate']} cps")

    db_conn = None if args.no_save else init_db(args.db)

    # BB84 — run once; rate is independent of Charlie position
    KA_bb84, KB_bb84, KR_bb84 = run_BB84_sims(
        runtimes      = args.runtimes,
        fibreLen      = args.fibre,
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
    bb84_avg, bb84_min, bb84_max, bb84_std, bb84_rates = aggregate(KR_bb84)

    avgs_mdi, mins_mdi, maxs_mdi, stds_mdi = [], [], [], []

    for cp in Cx:
        _, _, KR_mdi = run_mdi_sims(
            runtimes      = args.runtimes,
            fibreLen      = args.fibre,
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
            charliePos    = cp,
        )
        avg, mn, mx, std, mdi_rates = aggregate(KR_mdi)
        avgs_mdi.append(avg)
        mins_mdi.append(mn)
        maxs_mdi.append(mx)
        stds_mdi.append(std)

        if db_conn is not None:
            params = {
                "fibre_len":   args.fibre,
                "fibre_loss":  cfg["fibre_loss_db_per_km"],
                "det_eff":     cfg["detector_efficiency"],
                "dark_count":  cfg["dark_count_rate"],
                "init_loss":   cfg["init_loss"],
                "node_loss":   cfg["node_loss_db"],
                "source_err":  cfg["source_error_rate"],
                "dephasing":   cfg["dephasing_rate"],
                "bs_eff":      cfg["bs_eff"],
                "charlie_pos": cp,
            }
            # BB84 saved at each sweep point so analyse.py can reconstruct the flat reference line
            save_sweep_point(db_conn, "BB84", params, bb84_rates, [], [],
                             script="charlie_pos", runtimes=args.runtimes, photons=1024)
            save_sweep_point(db_conn, "MDI",  params, mdi_rates,  [], [],
                             script="charlie_pos", runtimes=args.runtimes, photons=1024)

    if db_conn is not None:
        db_conn.close()

    # Convert to kbps
    abs_avg_mdi  = [r / 1000 for r in avgs_mdi]
    abs_min_mdi  = [r / 1000 for r in mins_mdi]
    abs_max_mdi  = [r / 1000 for r in maxs_mdi]
    abs_avg_bb84 = bb84_avg / 1000
    abs_min_bb84 = bb84_min / 1000
    abs_max_bb84 = bb84_max / 1000

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
    else:
        lo_mdi = [r * math.exp(-s) for r, s in zip(abs_avg_mdi, stds_mdi)]
        hi_mdi = [r * math.exp(+s) for r, s in zip(abs_avg_mdi, stds_mdi)]
        line_mdi, = ax1.plot(Cx, abs_avg_mdi, 's-', label="MDI")
        ax1.fill_between(Cx, lo_mdi, hi_mdi, alpha=0.15, color=line_mdi.get_color())
        ax1.axhspan(abs_avg_bb84 * math.exp(-bb84_std),
                    abs_avg_bb84 * math.exp(+bb84_std), alpha=0.10, color='steelblue')

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
    plt.show()
