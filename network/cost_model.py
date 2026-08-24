"""
CapEx cost model (Section sec:results_cost / sec:cost_model, dissertation.tex).

Implements Equations eq:cost_bb84, eq:cost_mdi, and the closed-form crossover
eq:nstar_closed, under the multi-channel-detector-module simplification used
throughout that derivation ("we additionally assume multi-channel detector
modules suitable for every node's needs... BB84's detector cost becomes N c_d
and MDI's becomes K c_d") — not the raw 2N/4K component counts of
tab:components, which are a separate, un-simplified accounting used only for
the headline CapEx equations before that simplification is introduced.

TBB84 cost is defined identically to MDI's (same formula, same K c_d and
N d_u + K(K-1)/2 d_r fibre accounting) per the appendix bt_case_study spec:
TBB84 and MDI differ only in trust assumptions, not component count, under
this same multi-channel simplification.
"""
import math


def cost_bb84(N, total_fibre_km, c_s, c_d, c_f):
    """C_BB84 = N c_s + N c_d + total_fibre_km * c_f (multi-channel-simplified detector term)."""
    return N * c_s + N * c_d + total_fibre_km * c_f


def cost_relay(N, K, total_fibre_km, c_s, c_d, c_f):
    """C_MDI = C_TBB84 = N c_s + K c_d + total_fibre_km * c_f (multi-channel-simplified detector term)."""
    return N * c_s + K * c_d + total_fibre_km * c_f


def nstar_closed(rho, K):
    """Closed-form crossover user count N*(rho, K), Equation eq:nstar_closed.

    rho = c_d / c_F, the dimensionless detector:fibre price ratio
    (c_F = c_f * mean BB84 pairwise distance).
    """
    a = rho - 0.5 - 0.73 / math.sqrt(K)
    return -a + math.sqrt(a ** 2 + 2 * rho * K + K * (K - 1))
