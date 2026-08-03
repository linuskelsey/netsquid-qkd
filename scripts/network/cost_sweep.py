"""
Cost analysis --- user count sweep. All monetary values in GBP.

Runs the three-protocol simulation (BB84, MDI, Trusted BB84), computes
deployment cost using network/cost.py, and produces figures:

  Figure 1: Total deployment cost vs N
  Figure 2: Key rate / cost vs N  (cost-efficiency, kbps per M-GBP)
  Figure 3: Marginal deployment cost vs N  (requires --seeds > 1 or N range)

SPD cost is derived from detector efficiency via a linear model anchored at
SPAD (eta=0.20, GBP 15k) and SNSPD (eta=0.85, GBP 100k). There is no
explicit --spd-cost flag; pass --detector-tech to set efficiency.

Component model
---------------
  BB84 mesh    : N sources, 2N SPDs, N PBS, N EOMs, N(N-1)/2 links      O(N^2) fibre
  MDI          : N sources, 4K SPDs, K BS, 2K PBS, K switches,           O(N) fibre
                 N + K(K-1)/2 links
  Trusted BB84 : N+K sources, 2K SPDs, K PBS, K EOMs, K switches,       O(N) fibre
                 N + K(K-1)/2 links

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
    --detector-tech TECH     Detector preset: SPAD | SNSPD
                               Sets detector_efficiency and dark_count_rate in sim;
                               SPD cost derived from efficiency via linear model.
                               SPAD: eta=0.20, dark=10000 cps; SNSPD: eta=0.85, dark=100 cps.
    --source-cost FLOAT      GBP per photon source (overrides --source-tech cost)
    --bs-cost FLOAT          GBP per 50:50 beam splitter at MDI relay
    --pbs-cost FLOAT         GBP per polarising beam splitter at MDI relay
    --switch-cost FLOAT      GBP per optical switch at MDI relay
    --fibre-cost FLOAT       GBP per km of installed fibre
    --tortuosity FLOAT       Cable route / straight-line ratio (default: 1.0)
                               Scale fibre distances before cost; physics unchanged.
                               Typical urban value ~1.3–1.5.
    --workers INT            Worker processes (default: 80% of cores)
    --save PATH              Save figure base path (suffixes _cost/_efficiency/_marginal added)
    --no-figure              Suppress all figure output
    --no-p2p-db              Disable P2P DB writing
    --no-net-db              Disable network DB writing
    --cost-only              Skip simulation; compute cost from topology geometry only
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
from cost import component_counts, total_cost, spd_cost_from_efficiency, DETECTOR_TECH, DEFAULT_COSTS
from lib.db import update_network_cost



def _fibre_km_bb84(topo):
    return sum(topo.bb84_link(i, j) for (i, j) in topo.all_pairs())


def _fibre_km_mdi(topo):
    user_relay = sum(
        float(np.linalg.norm(topo.user_pos[i] - topo.relay_pos[topo.user_relay[i]]))
        for i in range(topo.N)
    )
    relay_relay = sum(
        float(np.linalg.norm(topo.relay_pos[k1] - topo.relay_pos[k2]))
        for k1 in range(topo.K) for k2 in range(k1 + 1, topo.K)
    )
    return user_relay + relay_relay


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
    parser.add_argument("--source-cost",   type=float, default=None,
                        help="GBP per photon source (default: QD preset, GBP 150k)")
    parser.add_argument("--bs-cost",       type=float, default=None,
                        help="GBP per 50:50 beam splitter at MDI relay")
    parser.add_argument("--pbs-cost",      type=float, default=None,
                        help="GBP per polarising beam splitter")
    parser.add_argument("--eom-cost",      type=float, default=None,
                        help="GBP per EOM (BB84 and trusted BB84 receivers)")
    parser.add_argument("--switch-cost",   type=float, default=None,
                        help="GBP per optical switch at MDI relay")
    parser.add_argument("--fibre-cost",    type=float, default=None,
                        help="GBP per km of installed fibre")
    parser.add_argument("--tortuosity",    type=float, default=1.2,
                        help="Mean fibre tortuosity (cable/Euclidean ratio). 1.0 = Euclidean; ~1.2 typical urban.")
    parser.add_argument("--workers",       type=int,   default=None)
    parser.add_argument("--save",          type=str,   default=None)
    parser.add_argument("--no-figure",     action="store_true")
    parser.add_argument("--no-p2p-db",     action="store_true")
    parser.add_argument("--no-net-db",     action="store_true")
    parser.add_argument("--cost-only",     action="store_true")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    cfg   = load_config(args.config)
    cfg["tortuosity_mean"] = args.tortuosity
    ref_n = args.n_max
    N_values = list(range(args.n_min, args.n_max + 1, args.n_step))

    # --- resolve cost parameters: DEFAULT_COSTS → tech preset → explicit CLI flag ---
    det_preset = DETECTOR_TECH[args.detector_tech] if args.detector_tech else {}

    source_gbp = args.source_cost if args.source_cost is not None else DEFAULT_COSTS["source_gbp"]
    bs_gbp     = args.bs_cost     if args.bs_cost     is not None else DEFAULT_COSTS["bs_gbp"]
    pbs_gbp    = args.pbs_cost    if args.pbs_cost    is not None else DEFAULT_COSTS["pbs_gbp"]
    fibre_gbp  = args.fibre_cost  if args.fibre_cost  is not None else DEFAULT_COSTS["fibre_per_km_gbp"]

    # apply detector preset values to simulation config
    if args.detector_tech:
        if "efficiency" in det_preset:
            cfg["detector_efficiency"] = det_preset["efficiency"]
        if "dark_count_rate" in det_preset:
            cfg["dark_count_rate"] = det_preset["dark_count_rate"]
    det_eff = cfg["detector_efficiency"]

    eom_gbp    = args.eom_cost    if args.eom_cost    is not None else DEFAULT_COSTS["eom_gbp"]
    switch_gbp = args.switch_cost if args.switch_cost is not None else DEFAULT_COSTS["switch_gbp"]
    cost_kw = dict(source_gbp=source_gbp, bs_gbp=bs_gbp, pbs_gbp=pbs_gbp,
                   eom_gbp=eom_gbp, switch_gbp=switch_gbp, fibre_per_km_gbp=fibre_gbp)

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

            user_pos  = place_users(N, area_km=args.area, seed=seed)
            topo_bb84 = Topology(user_pos)
            topo_mdi  = Topology(user_pos, relay_pos)

            if args.cost_only:
                prog.update(step, f"N={N}/{N_values[-1]}  computing cost from geometry...")
                bb84_fibre = _fibre_km_bb84(topo_bb84)
                mdi_fibre  = _fibre_km_mdi(topo_mdi)
                t = args.tortuosity
                bb84_cost_s[N].append(total_cost(component_counts(N, 0,       "BB84"),          bb84_fibre * t, det_eff, **cost_kw)["total_gbp"])
                mdi_cost_s[N].append( total_cost(component_counts(N, args.k,  "MDI"),           mdi_fibre  * t, det_eff, **cost_kw)["total_gbp"])
                trusted_cost_s[N].append(total_cost(component_counts(N, args.k, "trusted_BB84"), mdi_fibre * t, det_eff, **cost_kw)["total_gbp"])
            else:
                prog.update(step, f"N={N}/{N_values[-1]}  running simulations...")
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
                _db_path = None if args.no_net_db else DEFAULT_DB_PATH
                # total_fibre_km from runners already reflects per-link tortuosity via cfg["tortuosity_mean"]
                _bc = total_cost(component_counts(N, 0,       "BB84"),         bb84_res["total_fibre_km"],    det_eff, **cost_kw)
                _mc = total_cost(component_counts(N, args.k,  "MDI"),          mdi_res["total_fibre_km"],     det_eff, **cost_kw)
                _tc = total_cost(component_counts(N, args.k,  "trusted_BB84"), trusted_res["total_fibre_km"], det_eff, **cost_kw)
                bb84_cost_s[N].append(_bc["total_gbp"])
                mdi_cost_s[N].append(_mc["total_gbp"])
                trusted_cost_s[N].append(_tc["total_gbp"])
                update_network_cost(_db_path, bb84_res.get("net_run_id"),    det_eff, _bc["hardware_gbp"], _bc["fibre_gbp"], _bc["total_gbp"])
                update_network_cost(_db_path, mdi_res.get("net_run_id"),     det_eff, _mc["hardware_gbp"], _mc["fibre_gbp"], _mc["total_gbp"])
                update_network_cost(_db_path, trusted_res.get("net_run_id"), det_eff, _tc["hardware_gbp"], _tc["fibre_gbp"], _tc["total_gbp"])

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

    bb84_cost  = _means(bb84_cost_s)    / 1e6
    mdi_cost   = _means(mdi_cost_s)     / 1e6
    t_cost     = _means(trusted_cost_s) / 1e6

    if not args.cost_only:
        bb84_rate = _means(bb84_rate_s)    / 1000
        mdi_rate  = _means(mdi_rate_s)     / 1000
        t_rate    = _means(trusted_rate_s) / 1000
        bb84_eff  = np.where(bb84_cost > 0, bb84_rate / bb84_cost, 0.0)
        mdi_eff   = np.where(mdi_cost  > 0, mdi_rate  / mdi_cost,  0.0)
        t_eff     = np.where(t_cost    > 0, t_rate    / t_cost,    0.0)

    # --- summary table ---
    if args.cost_only:
        print(f"\n{'N':>3}  {'BB84 cost':>11}  {'MDI cost':>10}  {'TBB84 cost':>12}")
        print("-" * 42)
        for i, N in enumerate(N_arr):
            print(f"{int(N):>3}  £{bb84_cost[i]:>9.2f}M  £{mdi_cost[i]:>8.2f}M  £{t_cost[i]:>10.2f}M")
    else:
        print(f"\n{'N':>3}  {'BB84 cost':>11}  {'MDI cost':>10}  {'TBB84 cost':>12}  "
              f"{'BB84 eff':>10}  {'MDI eff':>9}  {'TBB84 eff':>11}")
        print("-" * 90)
        for i, N in enumerate(N_arr):
            print(f"{int(N):>3}  £{bb84_cost[i]:>9.2f}M  £{mdi_cost[i]:>8.2f}M  £{t_cost[i]:>10.2f}M  "
                  f"{bb84_eff[i]:>9.2f}  {mdi_eff[i]:>8.2f}  {t_eff[i]:>10.2f}  kbps/M£")

    if args.no_figure:
        return

    seed_label = f"seed={args.seed}" if args.seeds == 1 else f"{args.seeds} seeds (base={args.seed})"
    det_label  = args.detector_tech or "custom"
    spd_gbp    = spd_cost_from_efficiency(det_eff)
    tort_str   = f"  tort={args.tortuosity:.2f}" if args.tortuosity != 1.0 else ""
    top_label  = (f"K={args.k}, {args.area}×{args.area} km, {seed_label}  |  "
                  f"det={det_label} (η={det_eff:.2f}, £{spd_gbp/1e3:.0f}k/SPD)  "
                  f"src=QD (£{source_gbp/1e3:.0f}k)  "
                  f"fibre=£{fibre_gbp/1e3:.0f}k/km{tort_str}")

    # --- Figure 1: total cost vs N ---
    fig1, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N_arr, bb84_cost, "--", color="#377eb8", lw=1.5, label="BB84 (direct mesh)")
    ax.plot(N_arr, mdi_cost,  "-",  color="#e41a1c", lw=1.5, marker="o", label="MDI")
    ax.plot(N_arr, t_cost,    "-",  color="#4daf4a", lw=1.5, marker="s", label="Trusted BB84")
    ax.set_xlabel("User count $N$")
    ax.set_ylabel("Total deployment cost (M\pounds)")
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

    # --- Figure 2: cost-efficiency vs N (requires simulation data) ---
    if not args.cost_only:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.plot(N_arr, bb84_eff, "--", color="#377eb8", lw=1.5, label="BB84 (direct mesh)")
        ax2.plot(N_arr, mdi_eff,  "-",  color="#e41a1c", lw=1.5, marker="o", label="MDI")
        ax2.plot(N_arr, t_eff,    "-",  color="#4daf4a", lw=1.5, marker="s", label="Trusted BB84")
        ax2.set_xlabel("User count $N$")
        ax2.set_ylabel("Cost-efficiency (kbps / M\pounds)")
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

    # --- Figure 3: marginal cost vs N ---
    if len(N_arr) > 1:
        step_arr   = np.diff(N_arr)
        N_mid      = N_arr[1:]
        bb84_marg  = np.diff(bb84_cost) / step_arr
        mdi_marg   = np.diff(mdi_cost)  / step_arr
        t_marg     = np.diff(t_cost)    / step_arr

        fig3, ax3 = plt.subplots(figsize=(8, 5))
        ax3.plot(N_mid, bb84_marg, "--", color="#377eb8", lw=1.5, label="BB84 (direct mesh)")
        ax3.plot(N_mid, mdi_marg,  "-",  color="#e41a1c", lw=1.5, marker="o", label="MDI")
        ax3.plot(N_mid, t_marg,    "-",  color="#4daf4a", lw=1.5, marker="s", label="Trusted BB84")
        ax3.set_xlabel("User count $N$")
        ax3.set_ylabel(r"Marginal cost $\Delta C\,/\,\Delta N$ (M\pounds)")
        ax3.set_xticks(N_mid)
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        ax3.set_title(f"Marginal deployment cost vs user count\n{top_label}", fontsize=9)
        fig3.tight_layout()

        if args.save:
            stem, ext = (args.save.rsplit(".", 1) + ["png"])[:2]
            p = f"{stem}_marginal.{ext}"
            fig3.savefig(p, dpi=150)
            print(f"Saved {p}")
        else:
            plt.show()


if __name__ == "__main__":
    main()
