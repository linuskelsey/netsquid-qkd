"""
Cost analysis — user count sweep.

Runs the same three-protocol simulation as user_sweep.py, then computes
deployment cost per configuration using the hardware cost model in
network/cost.py. Produces two figures:

  Figure 1: Total deployment cost vs N  (fibre + hardware, all three protocols)
  Figure 2: Avg key rate / cost vs N    (cost-efficiency, kbps per M$)

Component model
---------------
  BB84 mesh     : N sources, 2N SPDs, N(N-1)/2 fibre links  →  O(N²) fibre cost
  MDI           : N sources, 2K SPDs, N + K(K-1)/2 links    →  O(N)  fibre cost
  Trusted BB84  : N+K sources, 2K SPDs, N + K(K-1)/2 links  →  O(N)  fibre cost

Default unit costs from network/cost.py DEFAULT_COSTS; overridden by tech presets,
then further overridden by explicit CLI cost flags.

Usage:
    python scripts/network/cost_sweep.py [options]

Options:
    --k INT                  Number of relays (default: 3)
    --n-min INT              Min user count (default: 4)
    --n-max INT              Max user count (default: 20)
    --n-step INT             Step size (default: 2)
    --area FLOAT             Area side length km (default: 10.0)
    --seed INT               Base random seed (random if omitted)
    --seeds INT              Topologies to average over (default: 1)
    --runtimes INT           MC runs per pair (default: 20)
    --config PATH            JSON config preset
    --detector-tech TECH     Detector preset: SPAD | InGaAs | SNSPD
                               Sets detector_efficiency in sim AND spd_usd in cost model.
                               Explicit --spd-cost overrides the preset cost.
    --source-tech TECH       Source preset: QD | NV | hSPDC | ideal
                               Sets source_usd in cost model.
                               Explicit --source-cost overrides the preset cost.
    --source-cost FLOAT      USD per photon source (overrides --source-tech cost)
    --spd-cost FLOAT         USD per SPD (overrides --detector-tech cost)
    --bs-cost FLOAT          USD per 50:50 beam splitter at MDI relay (default: 1000)
    --fibre-cost FLOAT       USD per km of installed fibre (default: 10000)
    --workers INT            Worker processes (default: 80% of cores)
    --save PATH              Save figure base path (suffix _cost / _efficiency added)
    --no-figure              Suppress all figure output
    --no-p2p-db              Disable P2P DB writing
    --no-net-db              Disable network DB writing
"""
import argparse
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.functions import load_config
from lib.db import DEFAULT_DB_PATH
from lib.progress import Progress
from topology import place_users, optimise_relays, Topology
from bb84_network import run_bb84_network
from mdi_network import run_mdi_network
from trusted_bb84_network import run_trusted_bb84_network
from cost import component_counts, total_cost, DETECTOR_TECH, SOURCE_TECH, DEFAULT_COSTS


def _compute_cost(res, N, K, protocol, cost_kw):
    counts = component_counts(N, K, protocol)
    return total_cost(counts, res["total_fibre_km"], **cost_kw)["total_usd"]


def main():
    parser = argparse.ArgumentParser(description="Cost analysis — user count sweep")
    parser.add_argument("--k",           type=int,   default=3)
    parser.add_argument("--n-min",       type=int,   default=4)
    parser.add_argument("--n-max",       type=int,   default=20)
    parser.add_argument("--n-step",      type=int,   default=2)
    parser.add_argument("--area",        type=float, default=10.0)
    parser.add_argument("--seed",        type=int,   default=None)
    parser.add_argument("--seeds",       type=int,   default=1)
    parser.add_argument("--runtimes",    type=int,   default=20)
    parser.add_argument("--config",        type=str,   default=None)
    parser.add_argument("--detector-tech", type=str,   default=None,
                        choices=list(DETECTOR_TECH))
    parser.add_argument("--source-tech",   type=str,   default=None,
                        choices=list(SOURCE_TECH))
    parser.add_argument("--source-cost",   type=float, default=None,
                        help="USD per source (overrides --source-tech cost)")
    parser.add_argument("--spd-cost",      type=float, default=None,
                        help="USD per SPD (overrides --detector-tech cost)")
    parser.add_argument("--bs-cost",       type=float, default=None)
    parser.add_argument("--fibre-cost",    type=float, default=None)
    parser.add_argument("--workers",       type=int,   default=None)
    parser.add_argument("--save",          type=str,   default=None)
    parser.add_argument("--no-figure",     action="store_true")
    parser.add_argument("--no-p2p-db",     action="store_true")
    parser.add_argument("--no-net-db",     action="store_true")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg   = load_config(args.config)
    ref_n = args.n_max
    N_values = list(range(args.n_min, args.n_max + 1, args.n_step))

    # --- resolve cost parameters: DEFAULT_COSTS → tech preset → explicit CLI flag ---
    det_preset = DETECTOR_TECH[args.detector_tech] if args.detector_tech else {}
    src_preset = SOURCE_TECH[args.source_tech]     if args.source_tech   else {}

    spd_usd    = args.spd_cost    if args.spd_cost    is not None else det_preset.get("cost_usd",    DEFAULT_COSTS["spd_usd"])
    source_usd = args.source_cost if args.source_cost is not None else src_preset.get("cost_usd",    DEFAULT_COSTS["source_usd"])
    bs_usd     = args.bs_cost     if args.bs_cost     is not None else DEFAULT_COSTS["bs_usd"]
    fibre_usd  = args.fibre_cost  if args.fibre_cost  is not None else DEFAULT_COSTS["fibre_per_km_usd"]

    # apply detector efficiency from preset to simulation config (unless config already sets it)
    if args.detector_tech and "efficiency" in det_preset:
        cfg["detector_efficiency"] = det_preset["efficiency"]

    cost_kw = dict(source_usd=source_usd, spd_usd=spd_usd,
                   bs_usd=bs_usd, fibre_per_km_usd=fibre_usd)

    if args.seeds == 1:
        seeds = [args.seed]
    else:
        rng   = np.random.default_rng(args.seed)
        seeds = rng.integers(0, 100_000, size=args.seeds).tolist()

    bb84_rate_s    = {N: [] for N in N_values}
    mdi_rate_s     = {N: [] for N in N_values}
    trusted_rate_s = {N: [] for N in N_values}
    bb84_cost_s    = {N: [] for N in N_values}
    mdi_cost_s     = {N: [] for N in N_values}
    trusted_cost_s = {N: [] for N in N_values}

    total_start = time.time()

    for s_idx, seed in enumerate(seeds):
        print(f"\n--- Seed {s_idx+1}/{args.seeds}  (seed={seed}) ---")
        seed_start = time.time()
        prog = Progress(len(N_values))
        step = 0

        ref_pos   = place_users(ref_n, area_km=args.area, seed=seed)
        relay_pos = optimise_relays(ref_pos, args.k, seed=seed)

        for N in N_values:
            if N < args.k:
                step += 1
                continue

            prog.update(step, f"N={N}/{N_values[-1]}  running simulations...")
            user_pos  = place_users(N, area_km=args.area, seed=seed)
            topo_bb84 = Topology(user_pos)
            topo_mdi  = Topology(user_pos, relay_pos)

            bb84_res = run_bb84_network(
                topo_bb84, cfg, runtimes=args.runtimes, workers=args.workers,
                p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                experiment="cost_sweep", seed=seed, area_km=args.area,
                config_preset=args.config)
            mdi_res = run_mdi_network(
                topo_mdi, cfg, runtimes=args.runtimes, workers=args.workers,
                p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                experiment="cost_sweep", seed=seed, area_km=args.area,
                config_preset=args.config)
            trusted_res = run_trusted_bb84_network(
                topo_mdi, cfg, runtimes=args.runtimes, workers=args.workers,
                p2p_db_path=None if args.no_p2p_db else DEFAULT_DB_PATH,
                net_db_path=None if args.no_net_db else DEFAULT_DB_PATH,
                experiment="cost_sweep", seed=seed, area_km=args.area,
                config_preset=args.config)

            bb84_rate_s[N].append(bb84_res["avg_key_rate"])
            mdi_rate_s[N].append(mdi_res["avg_key_rate"])
            trusted_rate_s[N].append(trusted_res["avg_key_rate"])
            bb84_cost_s[N].append(_compute_cost(bb84_res, N, 0, "BB84", cost_kw))
            mdi_cost_s[N].append(_compute_cost(mdi_res, N, args.k, "MDI", cost_kw))
            trusted_cost_s[N].append(_compute_cost(trusted_res, N, args.k, "trusted_BB84", cost_kw))

            step += 1
            prog.update(step, f"N={N}  costs: BB84 ${bb84_cost_s[N][-1]/1e6:.2f}M  MDI ${mdi_cost_s[N][-1]/1e6:.2f}M  TBB84 ${trusted_cost_s[N][-1]/1e6:.2f}M")

        prog.stop()
        m, s = divmod(int(time.time() - seed_start), 60)
        print(f"✓ Seed {s_idx+1}/{args.seeds} complete  {m}m {s:02d}s")

    m, s = divmod(int(time.time() - total_start), 60)
    print(f"✓ complete  total {m}m {s:02d}s")

    N_arr = np.array([N for N in N_values if bb84_cost_s[N]])

    def _means(d):
        return np.array([np.mean(d[N]) for N in N_arr])

    def _stds(d):
        return np.array([np.std(d[N]) for N in N_arr])

    bb84_cost  = _means(bb84_cost_s)  / 1e6
    mdi_cost   = _means(mdi_cost_s)   / 1e6
    t_cost     = _means(trusted_cost_s) / 1e6
    bb84_rate  = _means(bb84_rate_s)  / 1000
    mdi_rate   = _means(mdi_rate_s)   / 1000
    t_rate     = _means(trusted_rate_s) / 1000

    # cost-efficiency: kbps per M$  (avoid divide-by-zero)
    bb84_eff = np.where(bb84_cost > 0, bb84_rate / bb84_cost, 0.0)
    mdi_eff  = np.where(mdi_cost  > 0, mdi_rate  / mdi_cost,  0.0)
    t_eff    = np.where(t_cost    > 0, t_rate    / t_cost,    0.0)

    # --- summary table ---
    print(f"\n{'N':>3}  {'BB84 cost':>11}  {'MDI cost':>10}  {'TBB84 cost':>12}  "
          f"{'BB84 eff':>10}  {'MDI eff':>9}  {'TBB84 eff':>11}")
    print("-" * 90)
    for i, N in enumerate(N_arr):
        print(f"{int(N):>3}  ${bb84_cost[i]:>9.2f}M  ${mdi_cost[i]:>8.2f}M  ${t_cost[i]:>10.2f}M  "
              f"{bb84_eff[i]:>9.2f}  {mdi_eff[i]:>8.2f}  {t_eff[i]:>10.2f}  kbps/M$")

    if args.no_figure:
        return

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed})"
    det_label = args.detector_tech or "custom"
    src_label = args.source_tech   or "custom"
    top_label  = (f"K={args.k}, {args.area}×{args.area} km, {seed_label}  |  "
                  f"det={det_label} (η={cfg['detector_efficiency']:.2f}, ${spd_usd/1e3:.0f}k)  "
                  f"src={src_label} (${source_usd/1e3:.0f}k)  "
                  f"fibre=${fibre_usd/1e3:.0f}k/km")

    # --- Figure 1: total cost vs N ---
    fig1, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N_arr, bb84_cost, "--", color="#377eb8", lw=1.5, label="BB84 (direct mesh)")
    ax.plot(N_arr, mdi_cost,  "-",  color="#e41a1c", lw=1.5, marker="o", label="MDI")
    ax.plot(N_arr, t_cost,    "-",  color="#4daf4a", lw=1.5, marker="s", label="Trusted BB84")
    ax.set_xlabel("User count $N$")
    ax.set_ylabel("Total deployment cost (M\$)")
    ax.set_xticks(N_arr)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Deployment cost vs user count\n{top_label}", fontsize=9)
    fig1.tight_layout()

    if args.save:
        stem, ext = (args.save.rsplit(".", 1) + ["png"])[:2]
        p = f"{stem}_cost.{ext}"
        fig1.savefig(p, dpi=150)
        print(f"Saved {p}")
    else:
        plt.show()

    # --- Figure 2: cost-efficiency vs N ---
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(N_arr, bb84_eff, "--", color="#377eb8", lw=1.5, label="BB84 (direct mesh)")
    ax2.plot(N_arr, mdi_eff,  "-",  color="#e41a1c", lw=1.5, marker="o", label="MDI")
    ax2.plot(N_arr, t_eff,    "-",  color="#4daf4a", lw=1.5, marker="s", label="Trusted BB84")
    ax2.set_xlabel("User count $N$")
    ax2.set_ylabel("Cost-efficiency (kbps / M\$)")
    ax2.set_xticks(N_arr)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_title(f"Key rate per unit cost vs user count\n{top_label}", fontsize=9)
    fig2.tight_layout()

    if args.save:
        stem, ext = (args.save.rsplit(".", 1) + ["png"])[:2]
        p = f"{stem}_efficiency.{ext}"
        fig2.savefig(p, dpi=150)
        print(f"Saved {p}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
