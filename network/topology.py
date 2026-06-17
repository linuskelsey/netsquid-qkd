import numpy as np
from sklearn.cluster import KMeans


def place_users(N, area_km=10.0, seed=None):
    rng = np.random.default_rng(seed)
    return rng.uniform(0, area_km, size=(N, 2))


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
