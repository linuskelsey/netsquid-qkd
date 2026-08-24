"""
Side-by-side geometric comparison of k-means-centroid vs. Weiszfeld relay
placement on the same synthetic user set — supports Appendix sec:appendix_relay
(worked-example / geometric-comparison figures).

Left panel:  k-means centroid placement (cluster assignment fixed at k-means labels).
Right panel: backbone-coupled Weiszfeld placement, refined from the same k-means
             init/seed (cluster indices — and hence colours — stay aligned across
             panels since Weiszfeld only reassigns by nearest-relay distance).

Both panels report total fibre length (spoke + backbone mesh), matching
Table tab:relay_comparison's metric.

Usage:
    python scripts/network/relay_placement_compare.py --n 20 --k 3 [options]
"""
import argparse
import os
import sys
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

_root    = os.path.join(os.path.dirname(__file__), "../..")
_network = os.path.join(_root, "network")
sys.path.insert(0, _root)
sys.path.insert(0, _network)

from lib.plotting import apply_thesis_style, save_bundle
from topology import place_users, optimise_relays, Topology

apply_thesis_style()

_COLORS = plt.rcParams["axes.prop_cycle"].by_key()["color"]  # tab10, matches rest of thesis figs


def _total_fibre(topo):
    spoke = sum(
        np.linalg.norm(topo.user_pos[i] - topo.relay_pos[int(topo.user_relay[i])])
        for i in range(topo.N)
    )
    backbone = sum(
        np.linalg.norm(topo.relay_pos[k1] - topo.relay_pos[k2])
        for k1 in range(topo.K) for k2 in range(k1 + 1, topo.K)
    )
    return spoke + backbone


def _draw_panel(ax, topo, ghost_relay_pos, title):
    """Draw one placement: users + spokes + backbone mesh, coloured by cluster,
    own relays as filled black stars, the OTHER strategy's relay positions as
    unconnected hollow stars (with a thin dotted connector showing the shift)."""
    K = topo.K
    for k in range(K):
        members = topo.user_pos[topo.user_relay == k]
        ax.scatter(members[:, 0], members[:, 1], color=_COLORS[k % len(_COLORS)],
                   s=32, zorder=3)
        for p in members:
            ax.plot([p[0], topo.relay_pos[k, 0]], [p[1], topo.relay_pos[k, 1]],
                    color=_COLORS[k % len(_COLORS)], lw=0.8, alpha=0.7, zorder=2)

    for k1 in range(K):
        for k2 in range(k1 + 1, K):
            ax.plot([topo.relay_pos[k1, 0], topo.relay_pos[k2, 0]],
                    [topo.relay_pos[k1, 1], topo.relay_pos[k2, 1]],
                    color="grey", lw=1.0, ls="--", alpha=0.7, zorder=1)

    for k in range(K):
        ax.plot([topo.relay_pos[k, 0], ghost_relay_pos[k, 0]],
                [topo.relay_pos[k, 1], ghost_relay_pos[k, 1]],
                color="black", lw=0.8, ls=":", alpha=0.6, zorder=3)

    ax.scatter(topo.relay_pos[:, 0], topo.relay_pos[:, 1], marker="s", s=90,
              color="black", zorder=5)
    ax.scatter(ghost_relay_pos[:, 0], ghost_relay_pos[:, 1], marker="x", s=90,
              color="black", linewidths=1.8, zorder=4)

    ax.set_title(title)
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.set_aspect("equal")


def compare(n, k, area, seed, output_dir, name):
    user_pos = place_users(n, area_km=area, seed=seed)

    km = KMeans(n_clusters=k, n_init=10, random_state=seed)
    labels_km = km.fit_predict(user_pos)
    relay_km  = km.cluster_centers_.copy()
    topo_km   = Topology(user_pos, relay_km, user_relay=labels_km)
    L_km      = _total_fibre(topo_km)

    relay_wz = optimise_relays(user_pos, k, seed=seed)
    topo_wz  = Topology(user_pos, relay_wz)  # nearest-relay labels (final Weiszfeld assignment)
    L_wz     = _total_fibre(topo_wz)

    reduction = 100.0 * (L_km - L_wz) / L_km

    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(12, 5.5))
    _draw_panel(ax_l, topo_km, relay_wz, f"k-means centroid\ntotal fibre length = {L_km:.2f} km")
    _draw_panel(ax_r, topo_wz, relay_km,
               f"Weiszfeld\ntotal fibre length = {L_wz:.2f} km  ({reduction:+.1f}\\%)")
    fig.suptitle(f"Relay placement comparison on a shared user set: N={n} users, K={k} relays",
                fontsize=10, y=0.99)

    handles = [plt.Line2D([], [], marker="s", color="black", linestyle="", markersize=8,
                          label="Relay (this placement)"),
              plt.Line2D([], [], marker="x", color="black", linestyle="", markersize=8,
                          markeredgewidth=1.8, label="Relay (other placement)")]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.02))
    plt.tight_layout(rect=(0, 0.03, 1, 0.96))
    fig.subplots_adjust(wspace=0.084)

    if output_dir:
        save_bundle(
            fig, output_dir, name,
            title=f"k-means vs Weiszfeld relay placement (N={n}, K={k}, seed={seed})",
            assumptions={
                "N (users)":  n,
                "K (relays)": k,
                "Area": f"{area} x {area} km",
                "Seed": seed,
                "k-means total fibre length (km)":  round(L_km, 3),
                "Weiszfeld total fibre length (km)": round(L_wz, 3),
                "Reduction": f"{reduction:.2f}%",
                "User positions (km)": np.round(user_pos, 3).tolist(),
                "k-means cluster labels": labels_km.tolist(),
                "k-means relay positions (km)":  np.round(relay_km, 3).tolist(),
                "Weiszfeld relay positions (km)": np.round(relay_wz, 3).tolist(),
            },
            notes=["Weiszfeld panel is refined from the same k-means init/seed as the left "
                   "panel, so cluster indices (and colours) stay aligned across panels; final "
                   "cluster membership is by nearest-relay distance to the converged Weiszfeld "
                   "relay positions, per optimise_relays()."],
        )
    else:
        plt.show()

    print(f"k-means  L = {L_km:.3f} km")
    print(f"Weiszfeld L = {L_wz:.3f} km  ({reduction:+.2f}%)")


def main():
    parser = argparse.ArgumentParser(description="k-means vs Weiszfeld relay placement, side by side")
    parser.add_argument("--n", type=int, default=20, help="Number of users")
    parser.add_argument("--k", type=int, default=3, help="Number of relays")
    parser.add_argument("--area", type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (random if omitted)")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Save figure bundle to directory instead of displaying")
    parser.add_argument("--name", type=str, default="kmeans_vs_weiszfeld",
                        help="Bundle subdirectory name")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100_000

    compare(args.n, args.k, args.area, args.seed, args.output_dir, args.name)


if __name__ == "__main__":
    main()
