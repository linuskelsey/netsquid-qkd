import numpy as np
from sklearn.cluster import KMeans


def place_users(N, area_km=10.0, seed=None):
    rng = np.random.default_rng(seed)
    return rng.uniform(0, area_km, size=(N, 2))


def place_users_clustered(N, relay_pos, area_km=10.0, seed=None, max_radius_km=None):
    """Place N users in Voronoi-aware catchment areas around relays.

    Each user is assigned a relay uniformly at random, then placed uniformly
    within a circle of radius min(0.25*area_km, half_dist_to_nearest_relay).
    If max_radius_km is set, the catchment radius is additionally capped at
    that value (use for real-topology deployments with known service radius).
    """
    rng = np.random.default_rng(seed)
    relay_pos = np.array(relay_pos)
    K = len(relay_pos)

    if max_radius_km is not None:
        # fixed radius for each relay; overlapping catchments allowed — Topology assigns by proximity
        catchment = np.full(K, max_radius_km)
    else:
        # Voronoi-aware: cap at half-distance to nearest relay to avoid cross-catchment placement
        catchment = np.full(K, 0.25 * area_km)
        if K > 1:
            for r in range(K):
                dists = np.linalg.norm(relay_pos[r] - relay_pos, axis=1)
                dists[r] = np.inf
                catchment[r] = min(catchment[r], np.min(dists) / 2.0)

    relay_indices = rng.integers(0, K, size=N)
    positions = np.empty((N, 2))
    for i, r_idx in enumerate(relay_indices):
        cx, cy = relay_pos[r_idx]
        rad = catchment[r_idx]
        angle = rng.uniform(0, 2 * np.pi)
        r_sample = rad * np.sqrt(rng.uniform(0, 1))
        positions[i, 0] = np.clip(cx + r_sample * np.cos(angle), 0, area_km)
        positions[i, 1] = np.clip(cy + r_sample * np.sin(angle), 0, area_km)

    return positions


def optimise_relays(user_pos, K, n_init=10, seed=None):
    km = KMeans(n_clusters=K, n_init=n_init, random_state=seed)
    km.fit(user_pos)
    return km.cluster_centers_


def _dist(a, b):
    return float(np.linalg.norm(a - b))


class Topology:
    def __init__(self, user_pos, relay_pos=None):
        self.user_pos  = np.array(user_pos)
        self.relay_pos = np.array(relay_pos) if relay_pos is not None else None
        self.N = len(self.user_pos)
        self.K = len(self.relay_pos) if self.relay_pos is not None else 0

        if self.K > 0:
            # user_relay[i] = index of nearest relay to user i
            dists = np.linalg.norm(
                self.user_pos[:, None, :] - self.relay_pos[None, :, :], axis=2
            )  # (N, K)
            self.user_relay = np.argmin(dists, axis=1)
        else:
            self.user_relay = None

    def bb84_link(self, i, j):
        """Direct user-user distance in km."""
        return _dist(self.user_pos[i], self.user_pos[j])

    def mdi_link(self, i, j):
        """
        Returns (alice_km, bob_km, charlie_idx, cross_cluster).
        alice = user i sends to relay user_relay[i].
        bob   = user j sends to relay user_relay[j].
        cross_cluster: True if i and j are on different relays;
                       bob_km includes the relay-relay hop.
        Switch insertion loss is NOT included here — apply at call site.
        """
        if self.relay_pos is None:
            raise ValueError("No relays in topology")

        ri = int(self.user_relay[i])
        rj = int(self.user_relay[j])

        alice_km = _dist(self.user_pos[i], self.relay_pos[ri])

        if ri == rj:
            bob_km       = _dist(self.user_pos[j], self.relay_pos[rj])
            charlie_idx  = ri
            cross_cluster = False
        else:
            # Bob's photon travels j → relay_rj → relay_ri; BSM at relay_ri
            bob_km        = (_dist(self.user_pos[j], self.relay_pos[rj])
                             + _dist(self.relay_pos[rj], self.relay_pos[ri]))
            charlie_idx   = ri
            cross_cluster  = True

        return alice_km, bob_km, charlie_idx, cross_cluster

    def all_pairs(self):
        return [(i, j) for i in range(self.N) for j in range(i + 1, self.N)]


def build_topology(N, K, area_km=10.0, seed=None):
    user_pos  = place_users(N, area_km=area_km, seed=seed)
    relay_pos = optimise_relays(user_pos, K, seed=seed) if K > 0 else None
    return Topology(user_pos, relay_pos)
