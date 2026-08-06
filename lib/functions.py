import json
import argparse
import numpy as np

from netsquid.components import QSource
from netsquid.components.qsource import SourceStatus
from netsquid.components.models import DelayModel, FibreLossModel


DEFAULTS = {
    "fibre_loss_db_per_km": 0.18,  # Corning SMF-28 max at 1550 nm; pass --config configs/layer0_ideal.json for idealised baseline
    "init_loss": 0.10,             # linear fraction [0-1]; OZ Optics PM fused coupler, 0.4dB max excess loss (DTS0092), rounded up
    "detector_efficiency": 0.90,   # IDQ ID281 SNSPD default at telecom (range 0.80-0.95)
    "dark_count_rate": 50,         # IDQ ID281 SNSPD at telecom (range 25-100 cps)
    "node_loss_db": 2.0,            # lumped RX insertion loss; matches Duplinskiy et al. 2017 Bob-side receiver (LiNbO3 phase mod + PBS)
    "source_error_rate": 0.015,    # Quandela Prometheus: g²(0)<0.03 → ε_s=g²(0)/2<0.015
    "det_eff_x": 0.715,            # layer-8 X-basis bias: η_X=η_Z×10^-1/10 (1dB extra insertion loss, Grasselli et al. 2025)
    "dephasing_rate": 3.2e-7,       # PMD-derived: β=D²/2T², D=0.04 ps/√km (Corning SMF-28), T=50ps (IDQ ID281 jitter); range 2.6e-7-3.8e-7 /km (±20%)
    "bs_eff": 0.97,
    "tortuosity_mean": 1.0,     # 1.0 = Euclidean (off); set >1.0 to enable per-link stochastic routing factor
}


def load_config(path=None):
    config = DEFAULTS.copy()
    if path is not None:
        with open(path) as f:
            config.update(json.load(f))
    return config


def config_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default=None, help="Path to JSON config file")
    return parser



class HybridDelayModel(DelayModel):
    def __init__(self, SoL_fraction=0.5, stddev=0.05):
        super().__init__()
        # speed of light is ~ 300,000,000 m/s
        self.properties["speed"] = SoL_fraction * 3e8
        self.properties["stddev"] = stddev
        self.required_properties = ["length"] # in m

    def generate_delay(self, **kwargs):
        avg_speed = self.properties["speed"]
        stddev = self.properties["stddev"]
        # The 'rng' property contains a random number generator
        # We can use that to generate a random speed
        speed = self.properties["rng"].normal(avg_speed, avg_speed * stddev)
        delay = 1e9 * kwargs["length"] * 1000 / speed  # in nanoseconds
        return delay


def rng_bin_lst(n):
    return np.random.choice([0,1], size=n).tolist()


class SinglePhotonSource(QSource):
    def __init__(self, name, sourceFreq, efficiency=1, status=SourceStatus.EXTERNAL):
        super().__init__(name, frequency=sourceFreq, status=status)
        self.efficiency = efficiency
