"""
Network hardware and fibre cost model. All monetary values in GBP.

Component model
---------------
BB84 mesh      : N sources, 2N SPDs, N(N-1)/2 fibre links
MDI            : N sources (users only), 2K SPDs + K 50:50 BSs (relays), N + K(K-1)/2 links
Trusted BB84   : N+K sources, 2K SPDs, N + K(K-1)/2 links

MDI relay nodes are passive BSM stations: 2 SPDs + 1 50:50 BS (HOM) + 2 PBS (polarisation
analysis) + 1 optical switch (cross-relay photon routing) per relay. No source at MDI relays.
Trusted BB84 relay nodes are active: source + 2 SPDs per relay. No BSM required.
BB84 nodes use passive basis-choice splitters internal to detectors — negligible cost, not counted.

Classical communication (synchronisation, key forwarding) is assumed free and not included
in the cost model. Only quantum-layer hardware and fibre are costed.

SPD cost is modelled as a linear function of detector efficiency, anchored at:
  InGaAs SPAD : eta = 0.20  ->  GBP 15,000
  SNSPD        : eta = 0.85  ->  GBP 100,000
Valid for eta >= 0.20; raises ValueError below this threshold.
"""

DEFAULT_COSTS = {
    "source_gbp":       150_000,  # quantum dot SPS + cryostat (amortised per channel)
    "bs_gbp":             1_000,  # 50:50 fibre coupler (HOM BS at MDI relay)
    "pbs_gbp":              500,  # polarising beam splitter
    "eom_gbp":            2_000,  # electro-optic modulator (active basis choice, BB84/TBB84 receivers)
    "switch_gbp":         5_000,  # optical switch for cross-relay photon routing (MDI relay)
    "fibre_per_km_gbp":  10_000,
}

# Two supported detector classes. Efficiency drives SPD cost via linear model.
DETECTOR_TECH = {
    "SPAD":  {"efficiency": 0.20, "cost_gbp":  15_000},  # InGaAs SPAD, telecom-band (1550 nm)
    "SNSPD": {"efficiency": 0.85, "cost_gbp": 100_000},  # superconducting nanowire, cryogenic (~2 K)
}

# Linear SPD cost model derived from the two anchor points above
_ETA_LO,  _COST_LO = DETECTOR_TECH["SPAD"]["efficiency"],  DETECTOR_TECH["SPAD"]["cost_gbp"]
_ETA_HI,  _COST_HI = DETECTOR_TECH["SNSPD"]["efficiency"], DETECTOR_TECH["SNSPD"]["cost_gbp"]
_SPD_SLOPE     = (_COST_HI - _COST_LO) / (_ETA_HI - _ETA_LO)
_SPD_INTERCEPT = _COST_LO - _SPD_SLOPE * _ETA_LO


def spd_cost_from_efficiency(eta):
    """
    Return SPD cost per detector (GBP) for detector efficiency eta.

    Linear interpolation anchored at SPAD (eta=0.20, GBP 15k) and
    SNSPD (eta=0.85, GBP 100k). Raises ValueError for eta < 0.20.
    """
    if eta < _ETA_LO:
        raise ValueError(
            f"Detector efficiency {eta:.3f} is below the minimum supported "
            f"value of {_ETA_LO} (InGaAs SPAD baseline)."
        )
    return _SPD_SLOPE * eta + _SPD_INTERCEPT


def component_counts(N, K, protocol):
    """
    Return hardware component counts for a network of N users and K relays.

    Parameters
    ----------
    N        : number of users
    K        : number of relays (0 for direct BB84 mesh)
    protocol : "BB84" | "MDI" | "trusted_BB84"

    Returns
    -------
    dict with keys: n_sources, n_spd, n_bs, n_links
    """
    if protocol == "BB84":
        return {
            "n_sources":  N,
            "n_spd":      2 * N,  # 2 per user (Bob: 1 PBS → 2 outputs)
            "n_bs":       0,
            "n_pbs":      N,      # 1 per user (Bob: polarisation analysis after EOM)
            "n_eom":      N,      # 1 per user (Bob: active basis choice)
            "n_switches": 0,
            "n_links":    N * (N - 1) // 2,
        }
    elif protocol == "MDI":
        return {
            "n_sources":  N,
            "n_spd":      4 * K,  # 4 per relay (2 PBS × 2 outputs = full BSM)
            "n_bs":       K,      # 1 per relay (HOM 50:50 BS)
            "n_pbs":      2 * K,  # 2 per relay (one per BSM arm)
            "n_eom":      0,
            "n_switches": K,      # 1 per relay (cross-relay photon routing)
            "n_links":    N + K * (K - 1) // 2,
        }
    elif protocol == "trusted_BB84":
        return {
            "n_sources":  N + K,  # N user sources + K relay sources (backbone QKD)
            "n_spd":      2 * K,  # 2 per relay (shared detector array)
            "n_bs":       0,
            "n_pbs":      K,      # 1 per relay (Bob: polarisation analysis after EOM)
            "n_eom":      K,      # 1 per relay (Bob: active basis choice)
            "n_switches": K,      # 1 per relay (routes multiple users to shared SPD array)
            "n_links":    N + K * (K - 1) // 2,
        }
    else:
        raise ValueError(f"Unknown protocol: {protocol!r}")


def total_cost(counts, total_fibre_km, detector_efficiency,
               source_gbp=None, bs_gbp=None, pbs_gbp=None,
               eom_gbp=None, switch_gbp=None, fibre_per_km_gbp=None):
    """
    Compute total deployment cost and a per-category breakdown (GBP).

    SPD cost is derived from detector_efficiency via the linear model in
    spd_cost_from_efficiency(); there is no explicit spd_gbp override.

    Parameters
    ----------
    counts               : dict from component_counts()
    total_fibre_km       : total fibre deployed (km), from network simulator result
    detector_efficiency  : detector efficiency eta; must be >= 0.20
    source_gbp           : cost per photon source (GBP)
    bs_gbp               : cost per 50:50 beam splitter (GBP); MDI only
    pbs_gbp              : cost per polarising beam splitter (GBP)
    eom_gbp              : cost per EOM (GBP); BB84 and trusted BB84 receivers
    switch_gbp           : cost per optical switch (GBP); MDI only
    fibre_per_km_gbp     : cost per km of installed fibre (GBP)

    Returns
    -------
    dict with keys: hardware_gbp, fibre_gbp, total_gbp, breakdown
    """
    C_s   = source_gbp       if source_gbp       is not None else DEFAULT_COSTS["source_gbp"]
    C_d   = spd_cost_from_efficiency(detector_efficiency)
    C_b   = bs_gbp           if bs_gbp           is not None else DEFAULT_COSTS["bs_gbp"]
    C_pb  = pbs_gbp          if pbs_gbp          is not None else DEFAULT_COSTS["pbs_gbp"]
    C_eom = eom_gbp          if eom_gbp          is not None else DEFAULT_COSTS["eom_gbp"]
    C_sw  = switch_gbp       if switch_gbp        is not None else DEFAULT_COSTS["switch_gbp"]
    C_f   = fibre_per_km_gbp if fibre_per_km_gbp is not None else DEFAULT_COSTS["fibre_per_km_gbp"]

    source_cost = counts["n_sources"]  * C_s
    spd_cost    = counts["n_spd"]      * C_d
    bs_cost     = counts["n_bs"]       * C_b
    pbs_cost    = counts["n_pbs"]      * C_pb
    eom_cost    = counts["n_eom"]      * C_eom
    switch_cost = counts["n_switches"] * C_sw
    fibre_cost  = total_fibre_km       * C_f
    hardware    = source_cost + spd_cost + bs_cost + pbs_cost + eom_cost + switch_cost
    total       = hardware + fibre_cost

    return {
        "hardware_gbp": hardware,
        "fibre_gbp":    fibre_cost,
        "total_gbp":    total,
        "breakdown": {
            "sources_gbp": source_cost,
            "spd_gbp":     spd_cost,
            "bs_gbp":      bs_cost,
            "pbs_gbp":     pbs_cost,
            "eom_gbp":     eom_cost,
            "switch_gbp":  switch_cost,
            "fibre_gbp":   fibre_cost,
        },
    }
