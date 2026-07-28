"""
Analytical bounds for QKD key rates.
"""

import numpy as np


def plob_bound(distances_km, alpha_db_per_km, init_loss=0.0, node_loss_db=0.0, source_freq=1e7):
    """
    PLOB repeaterless bound (Pirandola et al. 2017): R <= -log2(1 - eta).

    Passive optical losses only (fibre + coupling + node connectors).
    Detector efficiency excluded — bound is on the channel, not the detector.

    Parameters
    ----------
    distances_km    : array-like, Alice-Bob separations in km
    alpha_db_per_km : fibre attenuation coefficient in dB/km
    init_loss       : init/coupling loss as linear fraction [0, 1)  e.g. 0.1 = 10%
    node_loss_db    : node/connector loss in dB
    source_freq     : photon source frequency in Hz

    Returns
    -------
    np.ndarray of PLOB bound values in kbps
    """
    d = np.asarray(distances_km, dtype=float)
    eta_fibre = 10 ** (-alpha_db_per_km * d / 10)
    eta_init  = 1.0 - init_loss
    eta_node  = 10 ** (-node_loss_db / 10)
    eta = np.clip(eta_fibre * eta_init * eta_node, 0.0, 1.0 - 1e-15)
    return -np.log2(1.0 - eta) * source_freq / 1000  # kbps
