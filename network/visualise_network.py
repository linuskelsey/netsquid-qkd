import argparse
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from topology import build_topology


CLUSTER_COLOURS = [
    "#e41a1c", "#377eb8", "#4daf4a", "#984ea3",
    "#ff7f00", "#a65628", "#f781bf", "#999999",
]


def _colour(k):
    return CLUSTER_COLOURS[k % len(CLUSTER_COLOURS)]


def draw_mdi(ax, topo):
    G = nx.Graph()

    for i in range(topo.N):
        G.add_node(f"u{i}", pos=tuple(topo.user_pos[i]), kind="user",
                   cluster=int(topo.user_relay[i]))
    for k in range(topo.K):
        G.add_node(f"r{k}", pos=tuple(topo.relay_pos[k]), kind="relay")

    for i in range(topo.N):
        G.add_edge(f"u{i}", f"r{int(topo.user_relay[i])}", etype="user-relay")

    for k1 in range(topo.K):
        for k2 in range(k1 + 1, topo.K):
            G.add_edge(f"r{k1}", f"r{k2}", etype="relay-relay")

    pos = nx.get_node_attributes(G, "pos")

    for i in range(topo.N):
        c = _colour(int(topo.user_relay[i]))
        ax.scatter(*topo.user_pos[i], color=c, s=60, zorder=3)
    for k in range(topo.K):
        ax.scatter(*topo.relay_pos[k], marker="s", s=75, color=_colour(k), zorder=4)
    ax.scatter([], [], marker="s", s=75, color="grey", label="Relay")

    for i in range(topo.N):
        r = int(topo.user_relay[i])
        xs = [topo.user_pos[i][0], topo.relay_pos[r][0]]
        ys = [topo.user_pos[i][1], topo.relay_pos[r][1]]
        ax.plot(xs, ys, color=_colour(r), lw=0.8, alpha=0.6)

    for k1 in range(topo.K):
        for k2 in range(k1 + 1, topo.K):
            xs = [topo.relay_pos[k1][0], topo.relay_pos[k2][0]]
            ys = [topo.relay_pos[k1][1], topo.relay_pos[k2][1]]
            ax.plot(xs, ys, "k--", lw=0.8, alpha=0.4)

    ax.set_title(f"MDI-QKD  (N={topo.N}, K={topo.K})")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_aspect("equal")


def draw_bb84(ax, topo):
    ax.scatter(*topo.user_pos.T, color="#377eb8", s=60, zorder=3, label="User")

    for i, j in topo.all_pairs():
        xs = [topo.user_pos[i][0], topo.user_pos[j][0]]
        ys = [topo.user_pos[i][1], topo.user_pos[j][1]]
        ax.plot(xs, ys, color="#377eb8", lw=0.4, alpha=0.25)

    ax.set_title(f"BB84  (N={topo.N}, {topo.N*(topo.N-1)//2} direct links)")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_aspect("equal")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n",    type=int,   default=20,   help="Number of users")
    parser.add_argument("--k",    type=int,   default=3,    help="Number of relays (MDI)")
    parser.add_argument("--area", type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed", type=int,   default=42)
    parser.add_argument("--save", type=str,   default=None, help="Save path (png/pdf)")
    args = parser.parse_args()

    topo = build_topology(args.n, args.k, area_km=args.area, seed=args.seed)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    draw_mdi(ax1, topo)
    draw_bb84(ax2, topo)
    plt.suptitle(f"Network topology  (area={args.area}×{args.area} km, seed={args.seed})",
                 fontsize=11)
    plt.tight_layout()

    if args.save:
        plt.savefig(args.save, dpi=150)
        print(f"Saved to {args.save}")
    else:
        plt.show()


if __name__ == "__main__":
    main()
