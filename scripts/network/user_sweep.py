"""
Experiment 2 — user count sweep.

Fixed K relays (positions optimised at ref-N), vary user count N. Plots average key rate vs N
for BB84 and MDI-QKD. Relay positions are re-optimised per seed when --seeds > 1.
Error bars show std across Monte Carlo runs (--seeds 1) or across random topologies
(--seeds N). Topology visualisation only produced when --seeds 1.

MDI uses the relay topology per N; BB84 uses a direct mesh.

Usage:
    python scripts/network/user_sweep.py [options]

Options:
    --k INT          Number of relays fixed for sweep (default: 3)
    --ref-n INT      N used to optimise relay positions (default: n-max)
    --n-min INT      Min user count (default: 4)
    --n-max INT      Max user count (default: 20)
    --n-step INT     User count step size (default: 2)
    --area FLOAT     Area side length in km (default: 10.0)
    --seed INT       Base random seed; random if omitted
    --seeds INT      Random topologies to average over (default: 1)
    --runtimes INT   Monte Carlo runs per pair (default: 20)
    --config PATH    JSON config preset
    --tortuosity FLOAT  Mean fibre tortuosity, cable/Euclidean ratio (default: 1.2; 1.0 = off)
    --error          Error style: bars (default), shade (±1σ fill), or iqr (Q1/Q3 fill)
    --workers INT    Worker processes (default: 80% of CPU cores; use nproc in command line to see maximum)
    --output-dir DIR Save figure bundle {plot.png, plot.tex, assumptions.md} to directory instead of displaying
    --placement STR  User placement mode: random (default) or clustered
                     (clustered: each user drawn uniformly within the
                      Voronoi-aware catchment circle of a randomly chosen relay)
    --real NAME      Load fixed relay positions from data/real_topologies/NAME.json;
                     K is determined by the file, not --k (no files currently checked in)

Examples:
    python scripts/network/user_sweep.py --k 3 --n-max 20 --runtimes 20
    python scripts/network/user_sweep.py --seeds 5 --seed 42 --output-dir results/
    python scripts/network/user_sweep.py --placement clustered --k 3 --n-max 20
"""
import argparse
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

import time
from lib.plotting import apply_thesis_style, save_bundle
from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH
from lib.progress import Progress
from topology import place_users, place_users_clustered, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from real_topology import load_real_topology
from visualise_network import draw_mdi, draw_bb84

apply_thesis_style()


def _pair_avgs(pair_rates):
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def main():
    parser = argparse.ArgumentParser(description="User count sweep (Experiment 2)")
    parser.add_argument("--k",        type=int,   default=3,    help="Number of relays (fixed)")
    parser.add_argument("--ref-n",    type=int,   default=None, help="N used to optimise relay positions (default: n-max)")
    parser.add_argument("--n-min",    type=int,   default=4,    help="Min user count")
    parser.add_argument("--n-max",    type=int,   default=20,   help="Max user count")
    parser.add_argument("--n-step",   type=int,   default=2,    help="User count step size")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--seeds",    type=int,   default=1,    help="Number of random topologies to average over")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",     type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--tortuosity", type=float, default=1.2,
                        help="Mean fibre tortuosity (cable/Euclidean ratio). 1.0 = Euclidean; ~1.2 typical urban.")
    parser.add_argument("--error",     type=str,   default="bars", choices=["bars", "shade", "iqr"])
    parser.add_argument("--output-dir", type=str,   default=None, help="Directory to save figures into (skips interactive display)")
    parser.add_argument("--placement",  type=str,   default="random", choices=["random", "clustered"],
                        help="User placement mode: random (uniform grid) or clustered (Voronoi catchment areas)")
    parser.add_argument("--real",       type=str,   default=None, metavar="NAME",
                        help="Load fixed relay positions from data/real_topologies/NAME.json; K is determined by file")
    parser.add_argument("--no-figure", action="store_true", help="Skip all figure output (no show, no save)")
    parser.add_argument("--no-p2p-db", action="store_true", help="Disable P2P DB writing")
    parser.add_argument("--no-net-db", action="store_true", help="Disable network DB writing")
    parser.add_argument("--workers",  type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100000

    cfg      = load_config(args.config)
    cfg["tortuosity_mean"] = args.tortuosity
    N_values = list(range(args.n_min, args.n_max + 1, args.n_step))
    ref_n    = args.ref_n if args.ref_n is not None else args.n_max

    # resolve real-topology fixed relays (if requested)
    if args.real:
        _rt_path = os.path.join(_root, "data", "real_topologies", f"{args.real}.json")
        _rt_topo, _rt_meta = load_real_topology(_rt_path)
        _fixed_relay_pos = _rt_topo.relay_pos
        _w, _h = _rt_meta["bbox_km"]
        _area_km    = max(_w, _h) + 60.0   # 30 km buffer on each side
        _max_radius = 30.0
        _K          = _rt_topo.K
        _protocols  = _rt_meta["protocols"]
        print(f"Real topology '{args.real}': {_K} relays, bbox {_w:.1f}×{_h:.1f} km → area={_area_km:.1f} km")
        print(f"  Protocols: {_protocols}")
    else:
        _fixed_relay_pos = None
        _area_km    = args.area
        _max_radius = None
        _K          = args.k
        _protocols  = ["BB84", "MDI"]

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    area_label = f"{args.real}" if args.real else f"{_area_km}×{_area_km} km"

    bb84_per_seed        = {N: [] for N in N_values}
    mdi_per_seed         = {N: [] for N in N_values}
    tbb84_per_seed       = {N: [] for N in N_values}
    bb84_ok_per_seed     = {N: [] for N in N_values}
    mdi_ok_per_seed      = {N: [] for N in N_values}
    tbb84_ok_per_seed    = {N: [] for N in N_values}
    bb84_fibre_per_seed  = {N: [] for N in N_values}
    mdi_fibre_per_seed   = {N: [] for N in N_values}
    tbb84_fibre_per_seed = {N: [] for N in N_values}

    seed_total  = len(N_values)
    total_start = time.time()

    _user_pos_by_seed  = {}
    _relay_pos_by_seed = {}

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog = Progress(seed_total)
        step = 0
        if _fixed_relay_pos is not None:
            relay_pos = _fixed_relay_pos
        else:
            ref_pos   = place_users(ref_n, area_km=_area_km, seed=seed)
            relay_pos = optimise_relays(ref_pos, _K, seed=seed)

        # generate all users up front; slice [:N] per data point for incremental placement
        if args.placement == "clustered":
            all_user_pos = place_users_clustered(args.n_max, relay_pos, area_km=_area_km,
                                                 seed=seed, max_radius_km=_max_radius)
        else:
            all_user_pos = place_users(args.n_max, area_km=_area_km, seed=seed)

        _user_pos_by_seed[seed]  = np.round(all_user_pos, 3).tolist()
        _relay_pos_by_seed[seed] = np.round(np.array(relay_pos), 3).tolist()

        for N in N_values:
            if N < _K:
                step += 1
                continue

            prog.update(step, f"User count: {N}/{N_values[-1]}  Both protocols running...")
            user_pos = all_user_pos[:N]
            topo_bb84 = Topology(user_pos)
            topo_mdi  = Topology(user_pos, relay_pos)

            if args.output_dir and not args.no_figure:
                _topo_dir = os.path.join(args.output_dir, "user_sweep", f"seed{seed}", "topologies")
                os.makedirs(_topo_dir, exist_ok=True)
                fig_m, ax_m = plt.subplots(figsize=(6, 5))
                draw_mdi(ax_m, topo_mdi, tortuosity_mean=args.tortuosity)
                plt.tight_layout()
                fig_m.savefig(os.path.join(_topo_dir, f"N{N}_mdi.png"), dpi=150, bbox_inches="tight")
                plt.close(fig_m)

                fig_b, ax_b = plt.subplots(figsize=(6, 5))
                draw_bb84(ax_b, topo_mdi, tortuosity_mean=args.tortuosity)
                plt.tight_layout()
                fig_b.savefig(os.path.join(_topo_dir, f"N{N}_bb84.png"), dpi=150, bbox_inches="tight")
                plt.close(fig_b)

            bb84_res = run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers,
                              p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                              net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                              experiment="user_sweep", seed=seed, area_km=_area_km,
                              config_preset=args.config)
            mdi_res  = run_mdi_network(topo_mdi,  cfg, runtimes=args.runtimes, workers=args.workers,
                                       p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                                       net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                                       experiment="user_sweep", seed=seed, area_km=_area_km,
                                       config_preset=args.config)

            bp = _pair_avgs(bb84_res["pair_rates"])
            mp = _pair_avgs(mdi_res["pair_rates"])

            bb84_per_seed[N].append(np.mean(bp) if bp else 0.0)
            mdi_per_seed[N].append(np.mean(mp)  if mp else 0.0)
            bb84_ok_per_seed[N].append(bb84_res["success_rate"] * 100)
            mdi_ok_per_seed[N].append(mdi_res["success_rate"] * 100)
            bb84_fibre_per_seed[N].append(bb84_res["total_fibre_km"])
            mdi_fibre_per_seed[N].append(mdi_res["total_fibre_km"])

            if "TBB84" in _protocols:
                tbb84_res = run_trusted_bb84_network(
                    topo_mdi, cfg, runtimes=args.runtimes, workers=args.workers,
                    p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                    net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                    experiment="user_sweep", seed=seed, area_km=_area_km,
                    config_preset=args.config)
                tp = _pair_avgs(tbb84_res["pair_rates"])
                tbb84_per_seed[N].append(np.mean(tp) if tp else 0.0)
                tbb84_ok_per_seed[N].append(tbb84_res["success_rate"] * 100)
                tbb84_fibre_per_seed[N].append(tbb84_res["total_fibre_km"])

            step += 1
            prog.update(step, f"User count: {N}/{N_values[-1]}  BB84 {bb84_per_seed[N][-1]/1000:.2f} | MDI {mdi_per_seed[N][-1]/1000:.2f} kbps")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

        if args.output_dir and not args.no_figure:
            _seed_N = [N for N in N_values if bb84_per_seed[N]]
            seed_bb84 = [bb84_per_seed[N][s_idx] for N in _seed_N]
            seed_mdi  = [mdi_per_seed[N][s_idx]  for N in _seed_N]
            fig_s, ax_s = plt.subplots(figsize=(8, 5))
            ax_s.plot(_seed_N, np.array(seed_bb84) / 1000, '--', color="#377eb8", lw=1.5, label="BB84")
            ax_s.plot(_seed_N, np.array(seed_mdi)  / 1000, color="#e41a1c", marker="o", lw=1.5, label="MDI")
            _seed_assumptions = {
                "Seed": seed,
                "Relay count (fixed)": _K,
                "User count sweep range": f"{args.n_min}-{args.n_max} (step {args.n_step})",
                "Area": area_label,
                "Placement mode": args.placement,
                "Tortuosity mean": args.tortuosity,
                "Runtimes per pair": args.runtimes,
                "BB84 key rate (bps) per N": dict(zip(_seed_N, seed_bb84)),
                "MDI key rate (bps) per N": dict(zip(_seed_N, seed_mdi)),
            }
            if "TBB84" in _protocols:
                seed_tbb84 = [tbb84_per_seed[N][s_idx] for N in _seed_N]
                ax_s.plot(_seed_N, np.array(seed_tbb84) / 1000, ':', color="#4daf4a", marker="s", lw=1.5, label="TBB84")
                _seed_assumptions["TBB84 key rate (bps) per N"] = dict(zip(_seed_N, seed_tbb84))
            ax_s.set_yscale("log")
            ax_s.set_xlabel("User count N")
            ax_s.set_ylabel("Avg key rate (kbps)")
            ax_s.set_xticks(_seed_N)
            ax_s.legend()
            ax_s.grid(True, alpha=0.3)
            ax_s.set_title(f"Key Rate vs User Count (seed={seed})", fontsize=10)
            plt.tight_layout()
            save_bundle(
                fig_s, os.path.join(args.output_dir, "user_sweep"), f"seed{seed}",
                title=f"Key Rate vs User Count (seed={seed})",
                assumptions=_seed_assumptions,
            )

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    N_arr_final    = [N for N in N_values if bb84_per_seed[N]]
    bb84_means     = [np.mean(bb84_per_seed[N])         for N in N_arr_final]
    bb84_stds      = [np.std(bb84_per_seed[N])          for N in N_arr_final]
    bb84_ok        = [np.mean(bb84_ok_per_seed[N])      for N in N_arr_final]
    bb84_fibre     = [np.mean(bb84_fibre_per_seed[N])   for N in N_arr_final]
    mdi_means      = [np.mean(mdi_per_seed[N])          for N in N_arr_final]
    mdi_stds       = [np.std(mdi_per_seed[N])           for N in N_arr_final]
    mdi_ok         = [np.mean(mdi_ok_per_seed[N])       for N in N_arr_final]
    mdi_fibre      = [np.mean(mdi_fibre_per_seed[N])    for N in N_arr_final]
    _run_tbb84 = "TBB84" in _protocols
    if _run_tbb84:
        tbb84_means = [np.mean(tbb84_per_seed[N])        for N in N_arr_final]
        tbb84_stds  = [np.std(tbb84_per_seed[N])         for N in N_arr_final]
        tbb84_ok    = [np.mean(tbb84_ok_per_seed[N])     for N in N_arr_final]
        tbb84_fibre = [np.mean(tbb84_fibre_per_seed[N])  for N in N_arr_final]

    if _run_tbb84:
        print(f"\n{'N':>3}  {'BB84 kbps':>10}  {'MDI kbps':>9}  {'TBB84 kbps':>11}  {'BB84 ok%':>9}  {'MDI ok%':>8}  {'TBB84 ok%':>10}")
        print("-" * 88)
        for i, N in enumerate(N_arr_final):
            print(
                f"{N:>3}  {bb84_means[i]/1000:>10.2f}  {mdi_means[i]/1000:>9.2f}  "
                f"{tbb84_means[i]/1000:>11.2f}  {bb84_ok[i]:>8.0f}%  {mdi_ok[i]:>7.0f}%  {tbb84_ok[i]:>9.0f}%"
            )
    else:
        print(f"\n{'N':>3}  {'BB84 kbps':>10}  {'MDI kbps':>9}  {'BB84 ok%':>9}  {'MDI ok%':>8}  {'BB84 km':>8}  {'MDI km':>7}")
        print("-" * 68)
        for N, b_r, m_r, b_ok, m_ok, b_km, m_km in zip(
                N_arr_final, bb84_means, mdi_means,
                bb84_ok, mdi_ok, bb84_fibre, mdi_fibre):
            print(
                f"{N:>3}  {b_r/1000:>10.2f}  {m_r/1000:>9.2f}  "
                f"{b_ok:>8.0f}%  {m_ok:>7.0f}%  "
                f"{b_km:>8.1f}  {m_km:>7.1f}"
            )

    N_arr  = np.array(N_arr_final)
    b_mean = np.array(bb84_means) / 1000
    b_std  = np.array(bb84_stds)  / 1000
    b_q1   = np.array([np.percentile(bb84_per_seed[N], 25) for N in N_arr_final]) / 1000
    b_q3   = np.array([np.percentile(bb84_per_seed[N], 75) for N in N_arr_final]) / 1000
    m_mean = np.array(mdi_means)  / 1000
    m_std  = np.array(mdi_stds)   / 1000
    m_q1   = np.array([np.percentile(mdi_per_seed[N], 25) for N in N_arr_final]) / 1000
    m_q3   = np.array([np.percentile(mdi_per_seed[N], 75) for N in N_arr_final]) / 1000
    if _run_tbb84:
        t_mean = np.array(tbb84_means) / 1000
        t_std  = np.array(tbb84_stds)  / 1000
        t_q1   = np.array([np.percentile(tbb84_per_seed[N], 25) for N in N_arr_final]) / 1000
        t_q3   = np.array([np.percentile(tbb84_per_seed[N], 75) for N in N_arr_final]) / 1000

    bb84_ref = b_mean[0] if b_mean[0] > 0 else 1.0

    # --- Figure 1: key rate vs N ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    if args.error == "bars":
        ax1.errorbar(N_arr, b_mean, yerr=b_std, label="BB84", color="#377eb8",
                     linestyle="--", capsize=4, lw=1.5)
        ax1.errorbar(N_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                     marker="o", capsize=4, lw=1.5)
        if _run_tbb84:
            ax1.errorbar(N_arr, t_mean, yerr=t_std, label="TBB84", color="#4daf4a",
                         marker="s", capsize=4, lw=1.5, linestyle=":")
    elif args.error == "shade":
        ax1.plot(N_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
        ax1.fill_between(N_arr, b_mean - b_std, b_mean + b_std, alpha=0.2, color="#377eb8")
        ax1.plot(N_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(N_arr, m_mean - m_std, m_mean + m_std, alpha=0.2, color="#e41a1c")
        if _run_tbb84:
            ax1.plot(N_arr, t_mean, ':', color="#4daf4a", marker="s", lw=1.5, label="TBB84")
            ax1.fill_between(N_arr, t_mean - t_std, t_mean + t_std, alpha=0.2, color="#4daf4a")
    else:  # iqr
        ax1.plot(N_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
        ax1.fill_between(N_arr, b_q1, b_q3, alpha=0.2, color="#377eb8")
        ax1.plot(N_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(N_arr, m_q1, m_q3, alpha=0.2, color="#e41a1c")
        if _run_tbb84:
            ax1.plot(N_arr, t_mean, ':', color="#4daf4a", marker="s", lw=1.5, label="TBB84")
            ax1.fill_between(N_arr, t_q1, t_q3, alpha=0.2, color="#4daf4a")

    ax1.set_yscale("log")
    ax1.set_xlabel("User count N")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(N_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(N_arr, b_mean / bb84_ref, alpha=0)
    ax2.plot(N_arr, m_mean / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed}): {seeds}"
    plt.title("Key Rate vs User Count", fontsize=10)
    plt.tight_layout()

    if not args.no_figure:
        if args.output_dir:
            save_bundle(
                fig, args.output_dir, "user_sweep",
                title="Key Rate vs User Count",
                assumptions={
                    "Relay count (fixed)": _K,
                    "User count sweep range": f"{args.n_min}-{args.n_max} (step {args.n_step})",
                    "Reference N for relay placement": ref_n,
                    "Area": area_label,
                    "Placement mode": args.placement,
                    "Seed": seed_label,
                    "Tortuosity mean": args.tortuosity,
                    "Runtimes per pair": args.runtimes,
                    "Error display": args.error,
                    "Real topology": args.real if args.real else "none (synthetic)",
                    "Final user positions (N=n_max, km, per seed)": _user_pos_by_seed,
                    "Final relay positions (km, per seed)": _relay_pos_by_seed,
                    "BB84 key rate (bps) per N per seed": {
                        N: dict(zip(seeds, bb84_per_seed[N])) for N in N_arr_final
                    },
                    "MDI key rate (bps) per N per seed": {
                        N: dict(zip(seeds, mdi_per_seed[N])) for N in N_arr_final
                    },
                },
            )
            print(f"Saved to {os.path.join(args.output_dir, 'user_sweep')}")
        else:
            plt.show()

    if args.output_dir and not args.no_figure:
        print(f"Per-seed plots + topologies saved under {os.path.join(args.output_dir, 'user_sweep')}/seed<seed>/")


if __name__ == "__main__":
    main()
