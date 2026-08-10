import numpy as np
from sklearn.cluster import KMeans


def place_users(N, area_km=10.0, seed=None):
    rng = np.random.default_rng(seed)
    return rng.uniform(0, area_km, size=(N, 2))


def _reflect_into_box(pos, area_km):
    """Fold coordinates outside [0, area_km] back in by reflection (triangle wave),
    instead of clipping, so Gaussian tail mass isn't pinned exactly on the boundary."""
    period = 2 * area_km
    pos = np.mod(pos, period)
    return np.where(pos > area_km, period - pos, pos)


def catchment_anchors(K, area_km):
    """K fixed geometric catchment centres used to seed provider-growth topologies.

    K=2 uses the left/right split established by relay_placement.py's exp2; K!=2
    places anchors evenly around a circle so the layout stays sensible for any K.
    """
    if K == 2:
        return np.array([[area_km / 4, area_km / 2], [3 * area_km / 4, area_km / 2]])
    centre = np.array([area_km / 2, area_km / 2])
    radius = area_km / 3
    angles = np.linspace(0, 2 * np.pi, K, endpoint=False)
    return centre + radius * np.column_stack([np.cos(angles), np.sin(angles)])


def grow_catchments(n_min, n_max, K, area_km, spread_km, seed, anchors=None, catchment_radius_km=None):
    """Provider-perspective incremental user growth.

    Draws n_max users one at a time from a single RNG stream: each user joins a
    uniformly-random catchment (out of K fixed anchors). Catchment membership,
    once assigned, never changes — sweeping N just takes a prefix of this
    sequence, so growing the network means adding users rather than re-rolling
    an unrelated sample.

    Two placement modes around the chosen anchor:
      catchment_radius_km is None (default): isotropic Gaussian, std spread_km,
        unbounded but reflected into the service area (soft catchment).
      catchment_radius_km given: uniform-density disc of that radius (hard
        catchment, e.g. a relay's known real-world service radius).

    Returns (user_pos [n_max,2], labels [n_max] int in [0,K), anchors [K,2]).
    """
    if n_min < K:
        raise ValueError(f"n_min ({n_min}) must be >= K ({K}): every catchment needs "
                          f"at least one user before its relay can be placed")

    rng = np.random.default_rng(seed)
    if anchors is None:
        anchors = catchment_anchors(K, area_km)
    else:
        anchors = np.array(anchors)

    # first K users cover each catchment exactly once, so every catchment is
    # guaranteed non-empty by n_min; the rest join uniformly at random
    labels = np.empty(n_max, dtype=int)
    labels[:K] = rng.permutation(K)
    if n_max > K:
        labels[K:] = rng.integers(0, K, size=n_max - K)
    if catchment_radius_km is not None:
        angles = rng.uniform(0, 2 * np.pi, size=n_max)
        radii  = catchment_radius_km * np.sqrt(rng.uniform(0, 1, size=n_max))
        offset = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
        raw_pos = anchors[labels] + offset
    else:
        raw_pos = rng.normal(anchors[labels], spread_km, size=(n_max, 2))
    user_pos = _reflect_into_box(raw_pos, area_km)
    return user_pos, labels, anchors


def relay_centroid(user_pos, labels, K):
    """Relay k placed at the mean of its (fixed) catchment. No reassignment."""
    return np.array([user_pos[labels == k].mean(axis=0) for k in range(K)])


def relay_boundary(user_pos, labels, K):
    """Each relay displaced 1 std from its catchment centroid toward the
    population-weighted mean of all other catchments' centroids."""
    centroids = relay_centroid(user_pos, labels, K)
    counts    = np.array([np.count_nonzero(labels == k) for k in range(K)])
    relay_pos = np.empty_like(centroids)
    for k in range(K):
        others = [l for l in range(K) if l != k]
        w      = counts[others] / counts[others].sum()
        other_mean = (w[:, None] * centroids[others]).sum(axis=0)
        direction  = other_mean - centroids[k]
        norm       = np.linalg.norm(direction)
        if norm < 1e-12:
            relay_pos[k] = centroids[k]
            continue
        direction /= norm
        s = float(np.std(user_pos[labels == k]))
        relay_pos[k] = centroids[k] + s * direction
    return relay_pos


def relay_weiszfeld(user_pos, labels, K, max_iter=500, tol=1e-9):
    """Backbone-coupled Weiszfeld relay position for K fixed catchments (no reassignment)."""
    clusters  = [user_pos[labels == k] for k in range(K)]
    relay_pos = np.array([c.mean(axis=0) for c in clusters])
    eps = 1e-9

    def _total_fibre(rp):
        spoke    = sum(np.linalg.norm(rp[k] - p) for k in range(K) for p in clusters[k])
        backbone = sum(np.linalg.norm(rp[k] - rp[l]) for k in range(K) for l in range(k + 1, K))
        return spoke + backbone

    prev_L = _total_fibre(relay_pos)
    for _ in range(max_iter):
        new_rp = np.empty_like(relay_pos)
        for k in range(K):
            num = np.zeros(2)
            den = 0.0
            for p in clusters[k]:
                d = max(np.linalg.norm(relay_pos[k] - p), eps)
                num += p / d
                den += 1.0 / d
            for l in range(K):
                if l == k:
                    continue
                d = max(np.linalg.norm(relay_pos[k] - relay_pos[l]), eps)
                num += relay_pos[l] / d
                den += 1.0 / d
            new_rp[k] = num / den if den > 0 else relay_pos[k]

        relay_pos = new_rp
        L = _total_fibre(relay_pos)
        if abs(prev_L - L) < tol:
            break
        prev_L = L

    return relay_pos


RELAY_STRATEGIES = {
    "centroid":  relay_centroid,
    "boundary":  relay_boundary,
    "weiszfeld": relay_weiszfeld,
}


def optimise_relays(user_pos, K, n_init=10, seed=None, max_iter=500, tol=1e-9):
    """Relay placement by the generalised (multi-facility) Weiszfeld iteration.

    Minimises total fibre length (spoke + fully-meshed backbone), the network's
    actual linear-cost objective, rather than the sum of squared distances that
    a plain k-means centroid minimises. Cluster assignment is initialised by
    k-means; relay position is then refined by the backbone-coupled Weiszfeld
    fixed-point update, alternating with nearest-relay reassignment, until
    total fibre length changes by less than `tol` km between iterations. For
    K=1 the backbone term is absent and this reduces to the plain single-
    facility Weiszfeld iteration (the geometric median).
    """
    user_pos = np.array(user_pos)
    km = KMeans(n_clusters=K, n_init=n_init, random_state=seed)
    labels    = km.fit_predict(user_pos)
    relay_pos = km.cluster_centers_.copy()

    def _total_fibre(relay_pos, labels):
        spoke    = sum(_dist(relay_pos[labels[i]], user_pos[i]) for i in range(len(user_pos)))
        backbone = sum(_dist(relay_pos[k], relay_pos[l]) for k in range(K) for l in range(k + 1, K))
        return spoke + backbone

    eps    = 1e-9
    prev_L = _total_fibre(relay_pos, labels)

    for _ in range(max_iter):
        new_relay_pos = np.empty_like(relay_pos)
        for k in range(K):
            num = np.zeros(2)
            den = 0.0
            for p in user_pos[labels == k]:
                d = max(_dist(relay_pos[k], p), eps)
                num += p / d
                den += 1.0 / d
            for l in range(K):
                if l == k:
                    continue
                d = max(_dist(relay_pos[k], relay_pos[l]), eps)
                num += relay_pos[l] / d
                den += 1.0 / d
            new_relay_pos[k] = num / den if den > 0 else relay_pos[k]

        relay_pos = new_relay_pos
        labels    = np.argmin(
            np.linalg.norm(user_pos[:, None, :] - relay_pos[None, :, :], axis=2), axis=1
        )

        L = _total_fibre(relay_pos, labels)
        if abs(prev_L - L) < tol:
            break
        prev_L = L

    return relay_pos


def _dist(a, b):
    return float(np.linalg.norm(a - b))


class Topology:
    def __init__(self, user_pos, relay_pos=None, user_relay=None):
        """
        user_relay: optional fixed user->relay assignment (e.g. catchment labels
        from grow_catchments). When given, it is used as-is instead of the
        nearest-relay default — needed whenever relay position was computed for
        a fixed membership that should not be silently reassigned by distance.
        """
        self.user_pos  = np.array(user_pos)
        self.relay_pos = np.array(relay_pos) if relay_pos is not None else None
        self.N = len(self.user_pos)
        self.K = len(self.relay_pos) if self.relay_pos is not None else 0

        if user_relay is not None:
            self.user_relay = np.array(user_relay)
        elif self.K > 0:
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
