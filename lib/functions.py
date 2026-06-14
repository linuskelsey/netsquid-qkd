import json
import argparse
import numpy as np

from netsquid.components import QSource
from netsquid.components.qsource import SourceStatus
from netsquid.components.models import DelayModel, FibreLossModel


DEFAULTS = {
    "fibre_loss_db_per_km": 0.2,   # SMF-28 typical; pass --config configs/layer0_ideal.json for idealised baseline
    "init_loss": 0.1,              # linear fraction [0-1], not dB (e.g. 0.1 = 10% loss)
    "detector_efficiency": 0.65,
    "dark_count_rate": 100,
    "node_loss_db": 2.0,           # receiver-side insertion loss in dB (connectors, coupling at Bob/Charlie)
    "source_error_rate": 0.005,
    "basis_bias": 0.5,
    "dephasing_rate": 0.0001,
    "bs_eff": 0.97,
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
