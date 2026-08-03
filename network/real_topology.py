"""
Real-topology loader.

Converts geolocation data (lat/lon) to a Topology object compatible with
bb84_network and mdi_network runners.

Input JSON format:
    {
      "nodes": [
        {"name": "UCL",      "lat": 51.524, "lon": -0.134, "type": "user"},
        {"name": "BT Tower", "lat": 51.521, "lon": -0.139, "type": "relay"}
      ]
    }

Projection: equirectangular centred at node centroid. Accurate to <1% for
areas up to ~50 km × 50 km (metropolitan scale).

Usage:
    from real_topology import load_real_topology
    topo, meta = load_real_topology("nodes.json")

    python network/real_topology.py nodes.json [--save topology.png]
"""
import argparse
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from topology import Topology


# km per degree (equirectangular approximation)
_KM_PER_DEG_LAT = 110.574
_KM_PER_DEG_LON = 111.320   # × cos(lat_ref) applied at projection time


def latlon_to_km(lats, lons):
    """
    Project lat/lon arrays to (x_km, y_km).
    Origin is at (min_lat, min_lon) so all coordinates are non-negative.
    Projection reference latitude is the centroid for minimal distortion.
    Returns arrays of same length as inputs.
    """
    lats = np.asarray(lats, dtype=float)
    lons = np.asarray(lons, dtype=float)
    lat_ref = lats.mean()
    cos_lat = math.cos(math.radians(lat_ref))
    x_km = (lons - lons.min()) * cos_lat * _KM_PER_DEG_LON
    y_km = (lats - lats.min()) * _KM_PER_DEG_LAT
    return x_km, y_km


def load_real_topology(path):
    """
    Load a JSON node file and return (Topology, meta).

    meta keys:
        user_names  : list[str]  — names of user nodes in order
        relay_names : list[str]  — names of relay nodes in order
        area_km     : (width_km, height_km) — bounding box of all nodes
        lat_ref     : float — centroid latitude used as projection origin
        lon_ref     : float — centroid longitude used as projection origin
    """
    with open(path) as f:
        data = json.load(f)

    nodes = data["nodes"]
    users  = [n for n in nodes if n["type"] == "user"]
    relays = [n for n in nodes if n["type"] == "relay"]

    all_lats = [n["lat"] for n in nodes]
    all_lons = [n["lon"] for n in nodes]
    lat_ref  = float(np.mean(all_lats))
    lon_ref  = float(np.mean(all_lons))

    if users:
        u_x, u_y = latlon_to_km([n["lat"] for n in users],
                                 [n["lon"] for n in users])
        user_pos = np.column_stack([u_x, u_y])
    else:
        user_pos = np.empty((0, 2))  # relay-only file; users placed by sweep script

    relay_pos = None
    if relays:
        r_x, r_y = latlon_to_km([n["lat"] for n in relays],
                                 [n["lon"] for n in relays])
        relay_pos = np.column_stack([r_x, r_y])

    topo = Topology(user_pos, relay_pos)

    all_x, all_y = latlon_to_km(all_lats, all_lons)
    meta = {
        "user_names":  [n.get("name", f"user_{i}") for i, n in enumerate(users)],
        "relay_names": [n.get("name", f"relay_{i}") for i, n in enumerate(relays)],
        "bbox_km":     (float(all_x.max()), float(all_y.max())),  # bounding box (min is 0,0)
        "lat_ref":     lat_ref,
        "lon_ref":     float(np.mean(all_lons)),
        "protocols":   data.get("protocols", ["BB84", "MDI"]),
    }
    return topo, meta


def _print_summary(topo, meta, path):
    w, h = meta["bbox_km"]
    print(f"Loaded: {path}")
    print(f"  Users  ({topo.N}): {', '.join(meta['user_names'])}")
    if topo.K:
        print(f"  Relays ({topo.K}): {', '.join(meta['relay_names'])}")
        if topo.N and topo.user_relay is not None:
            for i, name in enumerate(meta["user_names"]):
                r = int(topo.user_relay[i])
                print(f"    {name} → {meta['relay_names'][r]}")
    else:
        print("  No relays (BB84 mesh only)")
    print(f"  Bounding box: {w:.2f} × {h:.2f} km")
    print(f"  Projection origin: {meta['lat_ref']:.4f}°N, {meta['lon_ref']:.4f}°E")


def main():
    parser = argparse.ArgumentParser(description="Load and inspect a real-topology JSON file")
    parser.add_argument("path", help="Path to nodes JSON file")
    parser.add_argument("--save", default=None, metavar="FILE",
                        help="Save topology figure to file instead of displaying")
    args = parser.parse_args()

    topo, meta = load_real_topology(args.path)
    _print_summary(topo, meta, args.path)

    try:
        import matplotlib.pyplot as plt
        from visualise_network import draw_mdi, draw_bb84
        ncols = 2 if topo.K else 1
        fig, axes = plt.subplots(1, ncols, figsize=(6 * ncols, 5))
        if ncols == 1:
            axes = [axes]
        if topo.K:
            draw_mdi(axes[0], topo)
            _label_nodes(axes[0], topo, meta)
            draw_bb84(axes[1], topo)
            _label_nodes(axes[1], topo, meta)
        else:
            draw_bb84(axes[0], topo)
            _label_nodes(axes[0], topo, meta)
        w, h = meta["bbox_km"]
        plt.suptitle(f"{args.path}  —  {topo.N} users, {topo.K} relays, {w:.1f}×{h:.1f} km")
        plt.tight_layout()
        if args.save:
            plt.savefig(args.save, dpi=150)
            print(f"Saved to {args.save}")
        else:
            plt.show()
    except ImportError as e:
        print(f"[visualisation skipped: {e}]")


def _label_nodes(ax, topo, meta):
    for i, name in enumerate(meta["user_names"]):
        ax.annotate(name, topo.user_pos[i], fontsize=7, ha="center", va="bottom",
                    xytext=(0, 5), textcoords="offset points")
    for k, name in enumerate(meta["relay_names"]):
        ax.annotate(name, topo.relay_pos[k], fontsize=7, ha="center", va="bottom",
                    xytext=(0, 5), textcoords="offset points")


if __name__ == "__main__":
    main()
