"""
Experiment 2 — user count sweep.

Provider-growth model: relay positions are optimised once at n-min per the
chosen strategy (centroid/boundary/weiszfeld), then frozen; the network grows
one user at a time (uniform-random catchment, catchment membership fixed
once assigned) up to n-max. Plots average key rate vs N for BB84 (SNSPD and
SPAD detector variants) and MDI-QKD (one curve per --k value), showing how
key rate degrades as organic growth outpaces relay infrastructure sized for
the initial deployment. Relay positions are re-optimised per seed when
--seeds > 1.

--k accepts a comma-separated list (e.g. --k 2,3) to compare multiple relay
counts on the same graph. User positions are drawn once from the first K in
the list (K_ref); every other K reuses that same layout, just relabelled by
nearest anchor for its own catchment/relay count — a like-for-like
comparison. K_ref's draw also serves as the BB84 mesh reference (BB84 is a
mesh and doesn't depend on K).

Error bars show std across Monte Carlo runs (--seeds 1) or across random topologies
(--seeds N). Topology visualisation only produced when --seeds 1.

MDI uses the relay topology per N; BB84 uses a direct mesh.

Usage:
    python scripts/network/user_sweep.py [options]

Options:
    --k INT[,INT...] Relay count(s), comma-separated for multi-K comparison (default: 2)
    --strategy STR   Relay placement strategy: centroid, boundary, or weiszfeld (default: weiszfeld)
    --n-min INT      Min user count; also N at which relays are placed (default: 4)
    --n-max INT      Max user count (default: 20)
    --n-step INT     User count step size (default: 2)
    --area FLOAT     Area side length in km (default: 10.0)
    --spread FLOAT   Catchment Gaussian std in km (default: area/5)
    --seed INT       Base random seed; random if omitted
    --seeds INT      Random topologies to average over (default: 1)
    --runtimes INT   Monte Carlo runs per pair (default: 20)
    --config PATH    JSON config preset
    --tortuosity FLOAT  Mean fibre tortuosity, cable/Euclidean ratio (default: 1.2; 1.0 = off)
    --error          Error style: bars (default), shade (±1σ fill), or iqr (Q1/Q3 fill)
    --workers INT    Worker processes (default: 80% of CPU cores; use nproc in command line to see maximum)
    --output-dir DIR Save figure bundle {plot.png, plot.tex, assumptions.md} to directory instead of displaying
    --real NAME      Load fixed relay positions from data/real_topologies/NAME.json;
                     K is determined by the file, not --k (no files currently checked in).
                     Growth is still incremental, anchored on the real relay positions.

Examples:
    python scripts/network/user_sweep.py --k 2 --n-max 20 --runtimes 20
    python scripts/network/user_sweep.py --k 2,3 --n-max 20 --runtimes 20
    python scripts/network/user_sweep.py --seeds 5 --seed 42 --output-dir results/
    python scripts/network/user_sweep.py --strategy centroid --k 3 --n-max 20
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
from topology import grow_catchments, RELAY_STRATEGIES, Topology, catchment_anchors, assign_nearest_catchment
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from real_topology import load_real_topology
from visualise_network import draw_mdi, draw_bb84

apply_thesis_style()

# BB84 detector variants swept on every run: (label, detector_efficiency)
DETECTOR_VARIANTS = [("SNSPD", 0.90), ("SPAD", 0.20)]
BB84_COLORS = {"SNSPD": "#377eb8", "SPAD": "#ff7f00"}
MDI_COLORS  = ["#e41a1c", "#984ea3", "#a65628", "#f781bf", "#999999"]
MDI_MARKERS = ["o", "s", "^", "D", "v"]


def _pair_avgs(pair_rates):
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def main():
    parser = argparse.ArgumentParser(description="User count sweep (Experiment 2)")
    parser.add_argument("--k",        type=str,   default="2",
                        help="Relay count(s), comma-separated for multi-K comparison (e.g. 2,3)")
    parser.add_argument("--strategy", type=str,   default="weiszfeld", choices=list(RELAY_STRATEGIES),
                        help="Relay placement strategy, applied once at n-min then frozen")
    parser.add_argument("--n-min",    type=int,   default=4,    help="Min user count; also N at which relays are placed")
    parser.add_argument("--n-max",    type=int,   default=20,   help="Max user count")
    parser.add_argument("--n-step",   type=int,   default=2,    help="User count step size")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--spread",   type=float, default=None, help="Catchment Gaussian std in km (default: area/5); ignored if --catchment-radius given")
    parser.add_argument("--catchment-radius", type=float, default=None,
                        help="Hard catchment radius in km, uniform disc instead of Gaussian spread "
                             "(default: 15 km when --real is given, else Gaussian)")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--seeds",    type=int,   default=1,    help="Number of random topologies to average over")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",     type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--tortuosity", type=float, default=1.2,
                        help="Mean fibre tortuosity (cable/Euclidean ratio). 1.0 = Euclidean; ~1.2 typical urban.")
    parser.add_argument("--error",     type=str,   default="bars", choices=["bars", "shade", "iqr"])
    parser.add_argument("--output-dir", type=str,   default=None, help="Directory to save figures into (skips interactive display)")
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

    # resolve real-topology fixed relays (if requested)
    if args.real:
        _rt_path = os.path.join(_root, "data", "real_topologies", f"{args.real}.json")
        _rt_topo, _rt_meta = load_real_topology(_rt_path)
        _fixed_relay_pos = _rt_topo.relay_pos
        _w, _h = _rt_meta["bbox_km"]
        _area_km    = max(_w, _h) + 60.0   # 30 km buffer on each side
        _spread     = args.spread if args.spread is not None else 15.0
        _catchment_radius = args.catchment_radius if args.catchment_radius is not None else 30.0
        K_list      = [_rt_topo.K]
        _protocols  = _rt_meta["protocols"]
        print(f"Real topology '{args.real}': {_rt_topo.K} relays, bbox {_w:.1f}×{_h:.1f} km → area={_area_km:.1f} km")
        print(f"  Protocols: {_protocols}")
    else:
        _fixed_relay_pos = None
        _area_km    = args.area
        _spread     = args.spread if args.spread is not None else args.area / 5
        _catchment_radius = args.catchment_radius
        K_list      = sorted({int(k) for k in args.k.split(",")})
        _protocols  = ["BB84", "MDI"]

    K_ref  = K_list[0]
    K_tag  = "-".join(str(k) for k in K_list)

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    area_label = f"{args.real}" if args.real else f"{_area_km}×{_area_km} km"

    bb84_per_seed        = {v: {N: [] for N in N_values} for v, _ in DETECTOR_VARIANTS}
    bb84_ok_per_seed     = {v: {N: [] for N in N_values} for v, _ in DETECTOR_VARIANTS}
    bb84_fibre_per_seed  = {v: {N: [] for N in N_values} for v, _ in DETECTOR_VARIANTS}
    mdi_per_seed         = {K: {N: [] for N in N_values} for K in K_list}
    mdi_ok_per_seed      = {K: {N: [] for N in N_values} for K in K_list}
    mdi_fibre_per_seed   = {K: {N: [] for N in N_values} for K in K_list}
    tbb84_per_seed       = {N: [] for N in N_values}
    tbb84_ok_per_seed    = {N: [] for N in N_values}
    tbb84_fibre_per_seed = {N: [] for N in N_values}

    seed_total  = len(N_values)
    total_start = time.time()

    _user_pos_by_seed  = {}
    _relay_pos_by_seed = {K: {} for K in K_list}

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog = Progress(seed_total)
        step = 0

        # User positions are drawn ONCE (via K_ref's catchment growth) and
        # reused for every K in K_list, so each K only changes the
        # catchment/relay assignment (nearest-anchor relabel) on the same
        # physical layout — a like-for-like relay-count comparison.
        ref_user_pos, _, ref_anchors = grow_catchments(
            args.n_min, args.n_max, K_ref, _area_km, _spread, seed,
            anchors=_fixed_relay_pos, catchment_radius_km=_catchment_radius)
        _user_pos_by_seed[seed] = np.round(ref_user_pos, 3).tolist()

        _draws = {}
        for K in K_list:
            if _fixed_relay_pos is not None:
                anchors = np.array(_fixed_relay_pos)
            elif K == K_ref:
                anchors = ref_anchors
            else:
                anchors = catchment_anchors(K, _area_km)
            all_labels = assign_nearest_catchment(ref_user_pos, anchors, min_covered=args.n_min)
            if _fixed_relay_pos is not None:
                relay_pos = _fixed_relay_pos
            else:
                relay_pos = RELAY_STRATEGIES[args.strategy](
                    ref_user_pos[:args.n_min], all_labels[:args.n_min], K)
            _draws[K] = (ref_user_pos, all_labels, relay_pos)
            _relay_pos_by_seed[K][seed] = np.round(np.array(relay_pos), 3).tolist()

        for N in N_values:
            if N < K_ref:
                step += 1
                continue

            prog.update(step, f"User count: {N}/{N_values[-1]}  Running...")

            topo_bb84 = Topology(ref_user_pos[:N])

            if args.output_dir and not args.no_figure:
                _topo_dir = os.path.join(args.output_dir, f"user_sweep_K{K_tag}", f"seed{seed}", "topologies")
                os.makedirs(_topo_dir, exist_ok=True)
                fig_b, ax_b = plt.subplots(figsize=(6, 5))
                draw_bb84(ax_b, topo_bb84, tortuosity_mean=args.tortuosity, seed=seed)
                plt.tight_layout()
                fig_b.savefig(os.path.join(_topo_dir, f"N{N}_bb84.png"), dpi=150, bbox_inches="tight")
                plt.close(fig_b)

            for variant, det_eff in DETECTOR_VARIANTS:
                cfg_v = dict(cfg)
                cfg_v["detector_efficiency"] = det_eff
                bb84_res = run_bb84_network(
                    topo_bb84, cfg_v, runtimes=args.runtimes, workers=args.workers,
                    p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                    net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                    experiment="user_sweep", seed=seed, area_km=_area_km,
                    config_preset=args.config)
                bp = _pair_avgs(bb84_res["pair_rates"])
                bb84_per_seed[variant][N].append(np.mean(bp) if bp else 0.0)
                bb84_ok_per_seed[variant][N].append(bb84_res["success_rate"] * 100)
                bb84_fibre_per_seed[variant][N].append(bb84_res["total_fibre_km"])

            topo_mdi_ref = None
            for K in K_list:
                all_user_pos, all_labels, relay_pos = _draws[K]
                user_pos = all_user_pos[:N]
                labels   = all_labels[:N]
                topo_mdi = Topology(user_pos, relay_pos, user_relay=labels)
                if K == K_ref:
                    topo_mdi_ref = topo_mdi

                if args.output_dir and not args.no_figure:
                    _mdi_dir = os.path.join(_topo_dir, f"K{K}")
                    os.makedirs(_mdi_dir, exist_ok=True)
                    fig_m, ax_m = plt.subplots(figsize=(6, 5))
                    draw_mdi(ax_m, topo_mdi, tortuosity_mean=args.tortuosity,
                             strategy=None if _fixed_relay_pos is not None else args.strategy.capitalize(),
                             seed=seed)
                    plt.tight_layout()
                    fig_m.savefig(os.path.join(_mdi_dir, f"N{N}_mdi.png"), dpi=150, bbox_inches="tight")
                    plt.close(fig_m)

                mdi_res = run_mdi_network(
                    topo_mdi, cfg, runtimes=args.runtimes, workers=args.workers,
                    p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                    net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                    experiment="user_sweep", seed=seed, area_km=_area_km,
                    config_preset=args.config)
                mp = _pair_avgs(mdi_res["pair_rates"])
                mdi_per_seed[K][N].append(np.mean(mp) if mp else 0.0)
                mdi_ok_per_seed[K][N].append(mdi_res["success_rate"] * 100)
                mdi_fibre_per_seed[K][N].append(mdi_res["total_fibre_km"])

            if "TBB84" in _protocols:
                tbb84_res = run_trusted_bb84_network(
                    topo_mdi_ref, cfg, runtimes=args.runtimes, workers=args.workers,
                    p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                    net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                    experiment="user_sweep", seed=seed, area_km=_area_km,
                    config_preset=args.config)
                tp = _pair_avgs(tbb84_res["pair_rates"])
                tbb84_per_seed[N].append(np.mean(tp) if tp else 0.0)
                tbb84_ok_per_seed[N].append(tbb84_res["success_rate"] * 100)
                tbb84_fibre_per_seed[N].append(tbb84_res["total_fibre_km"])

            step += 1
            _snspd_last = bb84_per_seed["SNSPD"][N][-1] / 1000
            _mdi_last   = mdi_per_seed[K_ref][N][-1] / 1000
            prog.update(step, f"User count: {N}/{N_values[-1]}  BB84-SNSPD {_snspd_last:.2f} | MDI K={K_ref} {_mdi_last:.2f} kbps")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

        if args.output_dir and not args.no_figure:
            _seed_N = [N for N in N_values if bb84_per_seed["SNSPD"][N]]
            fig_s, ax_s = plt.subplots(figsize=(8, 5))
            _seed_assumptions = {
                "Seed": seed,
                "Relay counts (K)": K_list,
                "User count sweep range": f"{args.n_min}-{args.n_max} (step {args.n_step})",
                "Area": area_label,
                "Relay strategy": "real (fixed)" if args.real else args.strategy,
                "Catchment shape": (f"hard disc, radius {_catchment_radius:.1f} km"
                                     if _catchment_radius is not None
                                     else f"Gaussian, std {_spread:.2f} km"),
                "Tortuosity mean": args.tortuosity,
                "Runtimes per pair": args.runtimes,
            }
            for variant, _ in DETECTOR_VARIANTS:
                seed_bb84 = [bb84_per_seed[variant][N][s_idx] for N in _seed_N]
                ax_s.plot(_seed_N, np.array(seed_bb84) / 1000, '--', color=BB84_COLORS[variant],
                          lw=1.5, label=f"BB84-{variant}")
                _seed_assumptions[f"BB84-{variant} key rate (bps) per N"] = dict(zip(_seed_N, seed_bb84))
            for ki, K in enumerate(K_list):
                seed_mdi = [mdi_per_seed[K][N][s_idx] for N in _seed_N]
                ax_s.plot(_seed_N, np.array(seed_mdi) / 1000, color=MDI_COLORS[ki % len(MDI_COLORS)],
                          marker=MDI_MARKERS[ki % len(MDI_MARKERS)], lw=1.5, label=f"MDI K={K}")
                _seed_assumptions[f"MDI K={K} key rate (bps) per N"] = dict(zip(_seed_N, seed_mdi))
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
                fig_s, os.path.join(args.output_dir, f"user_sweep_K{K_tag}"), f"seed{seed}",
                title=f"Key Rate vs User Count (seed={seed})",
                assumptions=_seed_assumptions,
            )

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    N_arr_final = [N for N in N_values if bb84_per_seed["SNSPD"][N]]

    bb84_stats = {}
    for variant, _ in DETECTOR_VARIANTS:
        bb84_stats[variant] = {
            "mean":  [np.mean(bb84_per_seed[variant][N])       for N in N_arr_final],
            "std":   [np.std(bb84_per_seed[variant][N])        for N in N_arr_final],
            "ok":    [np.mean(bb84_ok_per_seed[variant][N])    for N in N_arr_final],
            "fibre": [np.mean(bb84_fibre_per_seed[variant][N]) for N in N_arr_final],
            "q1":    [np.percentile(bb84_per_seed[variant][N], 25) for N in N_arr_final],
            "q3":    [np.percentile(bb84_per_seed[variant][N], 75) for N in N_arr_final],
        }
    mdi_stats = {}
    for K in K_list:
        mdi_stats[K] = {
            "mean":  [np.mean(mdi_per_seed[K][N])       for N in N_arr_final],
            "std":   [np.std(mdi_per_seed[K][N])        for N in N_arr_final],
            "ok":    [np.mean(mdi_ok_per_seed[K][N])    for N in N_arr_final],
            "fibre": [np.mean(mdi_fibre_per_seed[K][N]) for N in N_arr_final],
            "q1":    [np.percentile(mdi_per_seed[K][N], 25) for N in N_arr_final],
            "q3":    [np.percentile(mdi_per_seed[K][N], 75) for N in N_arr_final],
        }
    _run_tbb84 = "TBB84" in _protocols
    if _run_tbb84:
        tbb84_means = [np.mean(tbb84_per_seed[N])        for N in N_arr_final]
        tbb84_stds  = [np.std(tbb84_per_seed[N])         for N in N_arr_final]
        tbb84_ok    = [np.mean(tbb84_ok_per_seed[N])     for N in N_arr_final]
        tbb84_fibre = [np.mean(tbb84_fibre_per_seed[N])  for N in N_arr_final]

    # --- summary table ---
    _headers = ["N"] + [f"BB84-{v} kbps" for v, _ in DETECTOR_VARIANTS] + [f"MDI K={K} kbps" for K in K_list]
    print("\n" + "  ".join(f"{h:>13}" for h in _headers))
    print("-" * (15 * len(_headers)))
    for i, N in enumerate(N_arr_final):
        row = [f"{N:>13}"]
        for variant, _ in DETECTOR_VARIANTS:
            row.append(f"{bb84_stats[variant]['mean'][i]/1000:>13.2f}")
        for K in K_list:
            row.append(f"{mdi_stats[K]['mean'][i]/1000:>13.2f}")
        print("  ".join(row))

    N_arr = np.array(N_arr_final)

    # --- Figure 1: key rate vs N ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    def _plot_series(x, mean, std, q1, q3, color, marker, linestyle, label):
        mean = np.array(mean) / 1000
        if args.error == "bars":
            std = np.array(std) / 1000
            ax1.errorbar(x, mean, yerr=std, label=label, color=color,
                         marker=marker, linestyle=linestyle, capsize=4, lw=1.5)
        elif args.error == "shade":
            std = np.array(std) / 1000
            ax1.plot(x, mean, linestyle, color=color, marker=marker, lw=1.5, label=label)
            ax1.fill_between(x, mean - std, mean + std, alpha=0.2, color=color)
        else:  # iqr
            q1 = np.array(q1) / 1000
            q3 = np.array(q3) / 1000
            ax1.plot(x, mean, linestyle, color=color, marker=marker, lw=1.5, label=label)
            ax1.fill_between(x, q1, q3, alpha=0.2, color=color)

    for variant, _ in DETECTOR_VARIANTS:
        st = bb84_stats[variant]
        _plot_series(N_arr, st["mean"], st["std"], st["q1"], st["q3"],
                     BB84_COLORS[variant], None, "--", f"BB84-{variant}")
    for ki, K in enumerate(K_list):
        st = mdi_stats[K]
        _plot_series(N_arr, st["mean"], st["std"], st["q1"], st["q3"],
                     MDI_COLORS[ki % len(MDI_COLORS)], MDI_MARKERS[ki % len(MDI_MARKERS)], "-", f"MDI K={K}")
    if _run_tbb84:
        t_mean = np.array(tbb84_means) / 1000
        t_std  = np.array(tbb84_stds)  / 1000
        t_q1   = np.array([np.percentile(tbb84_per_seed[N], 25) for N in N_arr_final]) / 1000
        t_q3   = np.array([np.percentile(tbb84_per_seed[N], 75) for N in N_arr_final]) / 1000
        _plot_series(N_arr, tbb84_means, tbb84_stds, [q*1000 for q in t_q1], [q*1000 for q in t_q3],
                     "#4daf4a", "s", ":", "TBB84")

    bb84_ref = bb84_stats["SNSPD"]["mean"][0] / 1000 if bb84_stats["SNSPD"]["mean"][0] > 0 else 1.0

    ax1.set_yscale("log")
    ax1.set_xlabel("User count N")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(N_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(N_arr, np.array(bb84_stats["SNSPD"]["mean"]) / 1000 / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed}): {seeds}"
    plt.title("Key Rate vs User Count", fontsize=10)
    plt.tight_layout()

    if not args.no_figure:
        if args.output_dir:
            _assumptions = {
                "Relay counts (K)": K_list,
                "User count sweep range": f"{args.n_min}-{args.n_max} (step {args.n_step})",
                "Relay placement": f"computed once at N={args.n_min} via "
                                    f"{'real (fixed)' if args.real else args.strategy}, then frozen (per K)",
                "Growth model": "one user at a time, uniform-random catchment, "
                                "catchment membership fixed once assigned (drawn separately per K)",
                "Catchment shape": (f"hard disc, radius {_catchment_radius:.1f} km"
                                 if _catchment_radius is not None
                                 else f"Gaussian, std {_spread:.2f} km"),
                "Area": area_label,
                "Seed": seed_label,
                "Tortuosity mean": args.tortuosity,
                "Runtimes per pair": args.runtimes,
                "Error display": args.error,
                "Real topology": args.real if args.real else "none (synthetic)",
                "BB84 detector variants": {v: e for v, e in DETECTOR_VARIANTS},
                "BB84 reference topology": f"K={K_ref} draw (BB84 is a mesh, independent of relay count)",
                "Final user positions (N=n_max, km, per seed, K_ref draw)": _user_pos_by_seed,
                "Final relay positions (km, per seed, per K)": _relay_pos_by_seed,
            }
            for variant, _ in DETECTOR_VARIANTS:
                _assumptions[f"BB84-{variant} key rate (bps) per N per seed"] = {
                    N: dict(zip(seeds, bb84_per_seed[variant][N])) for N in N_arr_final
                }
            for K in K_list:
                _assumptions[f"MDI K={K} key rate (bps) per N per seed"] = {
                    N: dict(zip(seeds, mdi_per_seed[K][N])) for N in N_arr_final
                }
            save_bundle(
                fig, args.output_dir, f"user_sweep_K{K_tag}",
                title="Key Rate vs User Count",
                assumptions=_assumptions,
            )
            print(f"Saved to {os.path.join(args.output_dir, f'user_sweep_K{K_tag}')}")
        else:
            plt.show()

    if args.output_dir and not args.no_figure:
        print(f"Per-seed plots + topologies saved under {os.path.join(args.output_dir, f'user_sweep_K{K_tag}')}/seed<seed>/")


if __name__ == "__main__":
    main()
