import argparse
import os
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


def _plot_wavy(ax, p1, p2, tortuosity, **kw):
    """Draw link p1→p2 as a half-sine curve whose arc length ≈ tortuosity × straight distance.

    Amplitude A = 2L√(τ-1)/π derived from arc-length integral of y=A·sin(πx/L).
    Falls back to a straight line when tortuosity ≤ 1.0 or link is degenerate.
    """
    p1, p2 = np.asarray(p1, float), np.asarray(p2, float)
    d      = float(np.linalg.norm(p2 - p1))
    if d < 1e-9 or tortuosity <= 1.0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], **kw)
        return
    A    = 2.0 * d * np.sqrt(max(tortuosity - 1.0, 0.0)) / np.pi
    t    = np.linspace(0.0, 1.0, 40)
    tang = (p2 - p1) / d
    perp = np.array([-tang[1], tang[0]])
    pts  = (p1[None, :] + t[:, None] * (p2 - p1)[None, :]
            + (A * np.sin(np.pi * t))[:, None] * perp[None, :])
    ax.plot(pts[:, 0], pts[:, 1], **kw)


def draw_mdi(ax, topo, tortuosity_mean=1.0):
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
        _plot_wavy(ax, topo.user_pos[i], topo.relay_pos[r], tortuosity_mean,
                   color=_colour(r), lw=0.8, alpha=0.6)

    for k1 in range(topo.K):
        for k2 in range(k1 + 1, topo.K):
            _plot_wavy(ax, topo.relay_pos[k1], topo.relay_pos[k2], tortuosity_mean,
                       color="k", lw=0.8, alpha=0.4, linestyle="--")

    ax.set_title(f"MDI-QKD  (N={topo.N}, K={topo.K})")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_aspect("equal")


def draw_bb84(ax, topo, tortuosity_mean=1.0):
    ax.scatter(*topo.user_pos.T, color="#377eb8", s=60, zorder=3, label="User")

    for i, j in topo.all_pairs():
        _plot_wavy(ax, topo.user_pos[i], topo.user_pos[j], tortuosity_mean,
                   color="#377eb8", lw=0.4, alpha=0.25)

    ax.set_title(f"BB84  (N={topo.N}, {topo.N*(topo.N-1)//2} direct links)")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_aspect("equal")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n",          type=int,   default=20,   help="Number of users")
    parser.add_argument("--k",          type=int,   default=3,    help="Number of relays (MDI)")
    parser.add_argument("--area",       type=float, default=10.0, help="Area side length (km)")
    parser.add_argument("--seed",       type=int,   default=None, help="Random seed (random if omitted)")
    parser.add_argument("--tortuosity", type=float, default=1.2,  help="Mean fibre tortuosity for wavy links (1.0 = straight)")
    parser.add_argument("--save",       type=str,   default=None, help="Save path (png/pdf)")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int.from_bytes(os.urandom(4), "big") % 100000
        print(f"Seed: {args.seed}")

    topo = build_topology(args.n, args.k, area_km=args.area, seed=args.seed)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    draw_mdi(ax1, topo, tortuosity_mean=args.tortuosity)
    draw_bb84(ax2, topo, tortuosity_mean=args.tortuosity)
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
