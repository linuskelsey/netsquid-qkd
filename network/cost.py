"""
Network hardware and fibre cost model.

Component model
---------------
BB84 mesh      : N sources, 2N SPDs, N(N-1)/2 fibre links
MDI            : N sources (users only), 2K SPDs + K 50:50 BSs (relays), N + K(K-1)/2 links
Trusted BB84   : N+K sources, 2K SPDs, N + K(K-1)/2 links

MDI relay nodes are passive (BSM only: 2 SPDs + 1 50:50 fibre beam splitter per relay, no source).
Trusted BB84 relay nodes are active (source + SPDs, no BSM required).
BB84 and trusted BB84 nodes use passive basis-choice splitters internal to detectors — not
counted separately as the cost is negligible vs SPDs.

Default unit costs (USD, indicative literature values):
  Photon source      : $20,000   (WCP laser + intensity modulator)
  SPD                : $50,000   (SNSPD, per detector)
  50:50 beam splitter: $5,000    (precision fibre coupler, per BSM relay)
  Fibre              : $10,000   per km (installed dark fibre)
"""

# Indicative unit costs in USD — used when no CLI override is given
DEFAULT_COSTS = {
    "source_usd":       20_000,
    "spd_usd":          50_000,
    "bs_usd":            1_000,
    "fibre_per_km_usd": 10_000,
}

# Named detector technology presets: (efficiency, cost_usd per SPD).
# Presets set defaults only — all values remain overridable via CLI flags.
#   SPAD    : Si/InGaAs avalanche diode, room/TE-cooled, low cost, moderate efficiency
#   InGaAs  : InGaAs SPAD, telecom-band (1550 nm), moderate cost and efficiency
#   SNSPD   : superconducting nanowire, cryogenic (~2 K), highest efficiency; cost
#             includes amortised cryostat share (~$80k–$150k system / 4–8 channels)
DETECTOR_TECH = {
    "SPAD":   {"efficiency": 0.30, "cost_usd":  5_000},
    "InGaAs": {"efficiency": 0.25, "cost_usd": 15_000},
    "SNSPD":  {"efficiency": 0.85, "cost_usd": 100_000},
}

# Named source technology presets: cost_usd per source node.
# The simulation assumes ideal single-photon sources throughout (no WCP / decoy state).
# Presets reflect real single-photon source technologies for cost modelling only;
# source_error_rate and other physics parameters must be set separately in the config.
#   QD      : semiconductor quantum dot, typically cryogenic (~4 K), high purity
#   NV      : nitrogen-vacancy centre in diamond, room-temperature capable, lower brightness
#   hSPDC   : heralded SPDC — probabilistic, non-ideal single photon; cheaper but higher error rate
#   ideal   : theoretical baseline (zero cost), matches simulation assumption
SOURCE_TECH = {
    "QD":    {"cost_usd": 150_000},  # QD + cryostat (amortised per channel)
    "NV":    {"cost_usd":  80_000},  # NV centre system
    "hSPDC": {"cost_usd":  25_000},  # heralded SPDC, no cryogenics
    "ideal": {"cost_usd":       0},  # theoretical baseline
}


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
    dict with keys: n_sources, n_spd, n_links
    """
    if protocol == "BB84":
        return {
            "n_sources": N,
            "n_spd":     2 * N,
            "n_bs":      0,
            "n_links":   N * (N - 1) // 2,
        }
    elif protocol == "MDI":
        return {
            "n_sources": N,
            "n_spd":     2 * K,
            "n_bs":      K,
            "n_links":   N + K * (K - 1) // 2,
        }
    elif protocol == "trusted_BB84":
        return {
            "n_sources": N + K,
            "n_spd":     2 * K,
            "n_bs":      0,
            "n_links":   N + K * (K - 1) // 2,
        }
    else:
        raise ValueError(f"Unknown protocol: {protocol!r}")


def total_cost(counts, total_fibre_km, source_usd=None, spd_usd=None, bs_usd=None,
               fibre_per_km_usd=None):
    """
    Compute total deployment cost and a per-category breakdown.

    Parameters
    ----------
    counts          : dict from component_counts()
    total_fibre_km  : total fibre deployed (km), from network simulator result
    source_usd      : cost per photon source (USD)
    spd_usd         : cost per SPD (USD)
    bs_usd          : cost per 50:50 beam splitter (USD); only applies to MDI relays
    fibre_per_km_usd: cost per km of installed fibre (USD)

    Returns
    -------
    dict with keys: hardware_usd, fibre_usd, total_usd, breakdown
    """
    C_s = source_usd       if source_usd       is not None else DEFAULT_COSTS["source_usd"]
    C_d = spd_usd          if spd_usd          is not None else DEFAULT_COSTS["spd_usd"]
    C_b = bs_usd           if bs_usd           is not None else DEFAULT_COSTS["bs_usd"]
    C_f = fibre_per_km_usd if fibre_per_km_usd is not None else DEFAULT_COSTS["fibre_per_km_usd"]

    source_cost = counts["n_sources"] * C_s
    spd_cost    = counts["n_spd"]     * C_d
    bs_cost     = counts["n_bs"]      * C_b
    fibre_cost  = total_fibre_km      * C_f
    hardware    = source_cost + spd_cost + bs_cost
    total       = hardware + fibre_cost

    return {
        "hardware_usd": hardware,
        "fibre_usd":    fibre_cost,
        "total_usd":    total,
        "breakdown": {
            "sources_usd": source_cost,
            "spd_usd":     spd_cost,
            "bs_usd":      bs_cost,
            "fibre_usd":   fibre_cost,
        },
    }
