"""
Experiment 1 — relay count sweep.

Fixed N users, vary relay count K. Plots average key rate vs K for BB84, MDI-QKD,
and trusted-node BB84. Error bars show std across Monte Carlo runs (--seeds 1) or
across random topologies (--seeds N). Topology visualisation only produced when --seeds 1.

BB84 is relay-independent (direct mesh) and is run once per seed.
MDI and trusted-node BB84 both use the relay topology and are re-run per K.

Usage:
    python scripts/network/relay_sweep.py [options]

Options:
    --n INT          Number of users (default: 20)
    --k-min INT      Min relay count (default: 1)
    --k-max INT      Max relay count (default: 8)
    --area FLOAT     Area side length in km (default: 10.0)
    --seed INT       Base random seed; random if omitted
    --seeds INT      Random topologies to average over (default: 1)
    --runtimes INT   Monte Carlo runs per pair (default: 20)
    --config PATH    JSON config preset
    --error          Error style: bars (default), shade (±1σ fill), or iqr (Q1/Q3 fill)
    --workers INT    Worker processes (default: 80% of CPU cores)
    --output-dir DIR Save figures to directory instead of displaying

Examples:
    python scripts/network/relay_sweep.py --n 20 --k-max 6 --runtimes 20
    python scripts/network/relay_sweep.py --seeds 5 --seed 42 --output-dir results/
"""
import argparse
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

import time
from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH, update_network_cost
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from visualise_network import draw_mdi, draw_bb84
from cost import component_counts, total_cost


def _pair_avgs(pair_rates):
    """Mean key rate per pair (valid runs only). Returns list over pairs."""
    avgs = []
    for rates in pair_rates.values():
        valid = [r for r in rates if r != "nan"]
        if valid:
            avgs.append(sum(valid) / len(valid))
    return avgs


def main():
    parser = argparse.ArgumentParser(description="Relay count sweep (Experiment 1)")
    parser.add_argument("--n",        type=int,   default=20,   help="Number of users (fixed)")
    parser.add_argument("--k-min",    type=int,   default=1,    help="Min relay count")
    parser.add_argument("--k-max",    type=int,   default=8,    help="Max relay count")
    parser.add_argument("--area",     type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed",     type=int,   default=None, help="Base random seed (random if omitted)")
    parser.add_argument("--seeds",    type=int,   default=1,    help="Number of random topologies to average over")
    parser.add_argument("--runtimes", type=int,   default=20,   help="Monte Carlo runs per pair")
    parser.add_argument("--config",     type=str,   default=None, help="Path to JSON config")
    parser.add_argument("--tortuosity", type=float, default=1.2,
                        help="Mean fibre tortuosity (cable/Euclidean ratio). 1.0 = Euclidean; ~1.2 typical urban.")
    parser.add_argument("--error",     type=str,   default="bars", choices=["bars", "shade", "iqr"])
    parser.add_argument("--output-dir", type=str,   default=None, help="Directory to save figures into (skips interactive display)")
    parser.add_argument("--no-figure", action="store_true", help="Skip all figure output (no show, no save)")
    parser.add_argument("--no-p2p-db", action="store_true", help="Disable P2P DB writing")
    parser.add_argument("--no-net-db", action="store_true", help="Disable network DB writing")
    parser.add_argument("--workers",   type=int,   default=None, help="Worker processes (default: 80%% of CPU cores)")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100000

    cfg      = load_config(args.config)
    cfg["tortuosity_mean"] = args.tortuosity
    K_values = list(range(args.k_min, args.k_max + 1))

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    bb84_per_seed        = []
    bb84_ok_per_seed     = []
    bb84_fibre_per_seed  = []
    mdi_per_seed         = {K: [] for K in K_values}
    mdi_ok_per_seed      = {K: [] for K in K_values}
    mdi_fibre_per_seed   = {K: [] for K in K_values}
    trusted_per_seed     = {K: [] for K in K_values}
    trusted_ok_per_seed  = {K: [] for K in K_values}
    trusted_fibre_per_seed = {K: [] for K in K_values}

    seed_total  = 1 + len(K_values)
    total_start = time.time()

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog = Progress(seed_total)
        step = 0
        user_pos = place_users(args.n, area_km=args.area, seed=seed)

        prog.update(step, f"BB84 reference running...")
        topo_bb84  = Topology(user_pos)
        bb84_res   = run_bb84_network(topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers,
                              p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                              net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                              experiment="relay_sweep", seed=seed, area_km=args.area,
                              config_preset=args.config)
        bp         = _pair_avgs(bb84_res["pair_rates"])
        _s_bb84    = np.mean(bp) if bp else 0.0
        _s_bb84_ok = bb84_res["success_rate"] * 100
        bb84_per_seed.append(_s_bb84)
        bb84_ok_per_seed.append(_s_bb84_ok)
        bb84_fibre_per_seed.append(bb84_res["total_fibre_km"])
        _det_eff = cfg["detector_efficiency"]
        _bb84_cost = total_cost(component_counts(args.n, 0, "BB84"),
                                bb84_res["total_fibre_km"], _det_eff)
        update_network_cost(None if args.no_net_db else DEFAULT_DB_PATH,
                            bb84_res.get("net_run_id"), _det_eff,
                            _bb84_cost["hardware_gbp"], _bb84_cost["fibre_gbp"], _bb84_cost["total_gbp"])
        step += 1
        prog.update(step, f"BB84 {_s_bb84/1000:.2f} kbps  ({_s_bb84_ok:.0f}% ok)")

        for K in K_values:
            prog.update(step, f"Relay count: {K}/{K_values[-1]}  MDI running...")
            relay_pos  = optimise_relays(user_pos, K, seed=seed)
            topo       = Topology(user_pos, relay_pos)
            mdi_res    = run_mdi_network(topo, cfg, runtimes=args.runtimes, workers=args.workers,
                             p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                             net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                             experiment="relay_sweep", seed=seed, area_km=args.area,
                             config_preset=args.config)
            mp         = _pair_avgs(mdi_res["pair_rates"])
            _s_mdi     = np.mean(mp) if mp else 0.0
            _s_mdi_ok  = mdi_res["success_rate"] * 100
            mdi_per_seed[K].append(_s_mdi)
            mdi_ok_per_seed[K].append(_s_mdi_ok)
            mdi_fibre_per_seed[K].append(mdi_res["total_fibre_km"])

            trusted_res   = run_trusted_bb84_network(topo, cfg, runtimes=args.runtimes, workers=args.workers,
                                p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                                net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                                experiment="relay_sweep", seed=seed, area_km=args.area,
                                config_preset=args.config)
            tp            = _pair_avgs(trusted_res["pair_rates"])
            _s_trusted    = np.mean(tp) if tp else 0.0
            _s_trusted_ok = trusted_res["success_rate"] * 100
            trusted_per_seed[K].append(_s_trusted)
            trusted_ok_per_seed[K].append(_s_trusted_ok)
            trusted_fibre_per_seed[K].append(trusted_res["total_fibre_km"])
            _mdi_cost = total_cost(component_counts(args.n, K, "MDI"),
                                   mdi_res["total_fibre_km"], _det_eff)
            update_network_cost(None if args.no_net_db else DEFAULT_DB_PATH,
                                mdi_res.get("net_run_id"), _det_eff,
                                _mdi_cost["hardware_gbp"], _mdi_cost["fibre_gbp"], _mdi_cost["total_gbp"])
            _tbb84_cost = total_cost(component_counts(args.n, K, "trusted_BB84"),
                                     trusted_res["total_fibre_km"], _det_eff)
            update_network_cost(None if args.no_net_db else DEFAULT_DB_PATH,
                                trusted_res.get("net_run_id"), _det_eff,
                                _tbb84_cost["hardware_gbp"], _tbb84_cost["fibre_gbp"], _tbb84_cost["total_gbp"])

            step += 1
            prog.update(step, f"Relay count: {K}/{K_values[-1]}  BB84 {_s_bb84/1000:.2f} | MDI {_s_mdi/1000:.2f} | TBB84 {_s_trusted/1000:.2f} kbps")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    print(f"\n{'K':>3}  {'BB84 kbps':>10}  {'MDI kbps':>9}  {'TBB84 kbps':>11}  {'BB84 ok%':>9}  {'MDI ok%':>8}  {'TBB84 ok%':>10}  {'BB84 km':>8}  {'MDI km':>7}  {'TBB84 km':>9}")
    print("-" * 102)
    b_fibre_mean = np.mean(bb84_fibre_per_seed) if bb84_fibre_per_seed else 0.0
    for K in K_values:
        print(
            f"{K:>3}  "
            f"{np.mean(bb84_per_seed)/1000:>10.2f}  "
            f"{np.mean(mdi_per_seed[K])/1000:>9.2f}  "
            f"{np.mean(trusted_per_seed[K])/1000:>11.2f}  "
            f"{np.mean(bb84_ok_per_seed):>8.0f}%  "
            f"{np.mean(mdi_ok_per_seed[K]):>7.0f}%  "
            f"{np.mean(trusted_ok_per_seed[K]):>9.0f}%  "
            f"{b_fibre_mean:>8.1f}  "
            f"{np.mean(mdi_fibre_per_seed[K]):>7.1f}  "
            f"{np.mean(trusted_fibre_per_seed[K]):>9.1f}"
        )

    bb84_means = [np.mean(bb84_per_seed)] * len(K_values)
    bb84_stds  = [np.std(bb84_per_seed)]  * len(K_values)
    bb84_ok    = [np.mean(bb84_ok_per_seed)] * len(K_values)

    mdi_means = [np.mean(mdi_per_seed[K])    for K in K_values]
    mdi_stds  = [np.std(mdi_per_seed[K])     for K in K_values]
    mdi_ok    = [np.mean(mdi_ok_per_seed[K]) for K in K_values]

    t_means = [np.mean(trusted_per_seed[K])    for K in K_values]
    t_stds  = [np.std(trusted_per_seed[K])     for K in K_values]
    t_ok    = [np.mean(trusted_ok_per_seed[K]) for K in K_values]

    K_arr  = np.array(K_values)
    b_mean = np.array(bb84_means) / 1000   # bps → kbps
    b_std  = np.array(bb84_stds)  / 1000
    b_q1   = np.array([np.percentile(bb84_per_seed, 25)] * len(K_values)) / 1000
    b_q3   = np.array([np.percentile(bb84_per_seed, 75)] * len(K_values)) / 1000
    m_mean = np.array(mdi_means)  / 1000
    m_std  = np.array(mdi_stds)   / 1000
    m_q1   = np.array([np.percentile(mdi_per_seed[K], 25) for K in K_values]) / 1000
    m_q3   = np.array([np.percentile(mdi_per_seed[K], 75) for K in K_values]) / 1000
    t_mean = np.array(t_means)    / 1000
    t_std  = np.array(t_stds)     / 1000
    t_q1   = np.array([np.percentile(trusted_per_seed[K], 25) for K in K_values]) / 1000
    t_q3   = np.array([np.percentile(trusted_per_seed[K], 75) for K in K_values]) / 1000

    bb84_ref = b_mean[0] if b_mean[0] > 0 else 1.0  # normalise relative axis to BB84

    # --- Figure 1: results ---
    fig, ax1 = plt.subplots(figsize=(8, 5))

    # BB84 — always dotted, no markers; error band style follows --error
    ax1.plot(K_arr, b_mean, '--', color="#377eb8", lw=1.5, label="BB84")
    if args.error == "iqr":
        ax1.fill_between(K_arr, b_q1, b_q3, alpha=0.2, color="#377eb8")
    else:
        ax1.fill_between(K_arr, b_mean - b_std, b_mean + b_std, alpha=0.2, color="#377eb8")

    # MDI and trusted BB84 — solid with markers, error controlled by --error flag
    if args.error == "bars":
        ax1.errorbar(K_arr, m_mean, yerr=m_std, label="MDI", color="#e41a1c",
                     marker="o", capsize=4, lw=1.5)
        ax1.errorbar(K_arr, t_mean, yerr=t_std, label="Trusted BB84", color="#4daf4a",
                     marker="s", capsize=4, lw=1.5)
    elif args.error == "shade":
        ax1.plot(K_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(K_arr, m_mean - m_std, m_mean + m_std, alpha=0.2, color="#e41a1c")
        ax1.plot(K_arr, t_mean, color="#4daf4a", marker="s", lw=1.5, label="Trusted BB84")
        ax1.fill_between(K_arr, t_mean - t_std, t_mean + t_std, alpha=0.2, color="#4daf4a")
    else:  # iqr
        ax1.plot(K_arr, m_mean, color="#e41a1c", marker="o", lw=1.5, label="MDI")
        ax1.fill_between(K_arr, m_q1, m_q3, alpha=0.2, color="#e41a1c")
        ax1.plot(K_arr, t_mean, color="#4daf4a", marker="s", lw=1.5, label="Trusted BB84")
        ax1.fill_between(K_arr, t_q1, t_q3, alpha=0.2, color="#4daf4a")

    ax1.set_yscale("log")
    ax1.set_xlabel("Relay count K")
    ax1.set_ylabel("Avg key rate (kbps)")
    ax1.set_xticks(K_arr)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(K_arr, b_mean / bb84_ref, alpha=0)
    ax2.plot(K_arr, m_mean / bb84_ref, alpha=0)
    ax2.plot(K_arr, t_mean / bb84_ref, alpha=0)
    ax2.set_ylabel("Relative key rate")
    ax2.set_yscale("log")

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed})"
    plt.title(
        f"Key rate vs relay count  (N={args.n}, area={args.area}×{args.area} km, {seed_label})",
        fontsize=10
    )
    plt.tight_layout()

    if not args.no_figure:
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)
            fn = os.path.splitext(os.path.basename(__file__))[0] + ".png"
            save_path = os.path.join(args.output_dir, fn)
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
            print(f"Saved to {save_path}")
        else:
            plt.show()

    # --- Figure 2: topology at midpoint K (single seed only) ---
    if args.seeds == 1 and not args.no_figure:
        K_mid      = K_values[len(K_values) // 2]
        topo_users = place_users(args.n, area_km=args.area, seed=seeds[0])
        topo_mid   = Topology(topo_users, optimise_relays(topo_users, K_mid, seed=seeds[0]))

        fig2, (axA, axB) = plt.subplots(1, 2, figsize=(12, 5))
        draw_mdi(axA, topo_mid, tortuosity_mean=args.tortuosity)
        draw_bb84(axB, topo_mid, tortuosity_mean=args.tortuosity)
        plt.suptitle(
            f"Network topology at K={K_mid}  (N={args.n}, {seed_label})",
            fontsize=11
        )
        plt.tight_layout()

        if args.output_dir:
            topo_fn = os.path.splitext(os.path.basename(__file__))[0] + "_topology.png"
            topo_save = os.path.join(args.output_dir, topo_fn)
            plt.savefig(topo_save, dpi=150, bbox_inches="tight")
            print(f"Topology saved to {topo_save}")
        else:
            plt.show()


if __name__ == "__main__":
    main()
