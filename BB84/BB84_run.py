from multiprocessing import get_context
import os

from difflib import SequenceMatcher
import netsquid as ns

from netsquid.nodes import Node
from netsquid.components import QuantumChannel, ClassicalChannel
from netsquid.components.models.qerrormodels import DephaseNoiseModel

import sys
_this_dir  = os.path.dirname(os.path.abspath(__file__))
_repo_root = os.path.dirname(_this_dir)
sys.path.insert(0, _this_dir)   # BB84_Alice, BB84_Bob
sys.path.insert(0, _repo_root)  # lib.functions
from lib.functions import HybridDelayModel, load_config, config_arg_parser

from BB84_Alice import AliceProtocol
from BB84_Bob import BobProtocol



def _bb84_chunk(args):
    """Sequential simulation block — runs runtimes iterations and returns partial results."""
    runtimes, fibreLen, qDelay, qSpeed, photonCount, sourceFreq, lenLoss, initLoss, detectorEffZ, detectorEffX, darkCount, nodeLossDb, sourceErrRate, dephasingRate = args

    KeyListA    = []
    KeyListB    = []
    KeyRateList = []

    for _ in range(runtimes):
        ns.sim_reset()

        # nodes =================================================
        alice = Node("Alice", port_names=["A.Q.Out", "A.C.Out", "A.C.In", "A.C.Out.tags"])
        bob   = Node("Bob",   port_names=["B.Q.In",  "B.C.In",  "B.C.Out", "B.C.In.tags"])

        # channels ==============================================
        p_dephase = min(1.0, dephasingRate * fibreLen)
        QChann = QuantumChannel("[A: -Q-> :B]",
                                delay=qDelay,
                                length=fibreLen,
                                models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05),
                                        "quantum_noise_model": DephaseNoiseModel(p_dephase, time_independent=True)})

        alice.connect_to(bob, QChann,
                         local_port_name=alice.ports["A.Q.Out"].name,
                         remote_port_name=bob.ports["B.Q.In"].name)

        CChann1 = ClassicalChannel("[A: -C-> :B]", delay=0, length=fibreLen,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann2 = ClassicalChannel("[B: -C-> :A]", delay=0, length=fibreLen,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann3 = ClassicalChannel("[A: -C:tags-> :B]", delay=0, length=fibreLen,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})

        alice.connect_to(bob, CChann1,
                         local_port_name=alice.ports["A.C.Out"].name,
                         remote_port_name=bob.ports["B.C.In"].name)
        bob.connect_to(alice, CChann2,
                       local_port_name=bob.ports["B.C.Out"].name,
                       remote_port_name=alice.ports["A.C.In"].name)
        alice.connect_to(bob, CChann3,
                         local_port_name=alice.ports["A.C.Out.tags"].name,
                         remote_port_name=bob.ports["B.C.In.tags"].name)

        # protocols =============================================
        aliceProt = AliceProtocol(alice, photonCount, sourceFreq,
                                  portNames=list(alice.ports.keys()),
                                  fibreLen=fibreLen, lenLoss=lenLoss, initLoss=initLoss,
                                  sourceErrRate=sourceErrRate)
        bobProt   = BobProtocol(bob, photonCount,
                                portNames=list(bob.ports.keys()),
                                detectorEffZ=detectorEffZ, detectorEffX=detectorEffX, darkCount=darkCount, sourceFreq=sourceFreq,
                                nodeLossDb=nodeLossDb)

        bobProt.start()
        aliceProt.start()

        startTime = ns.util.simtools.sim_time(magnitude=ns.NANOSECOND)
        ns.sim_run(end_time=ns.SECOND * 100)

        if bobProt.end_time is not None:
            keyA, keyB = aliceProt.key, bobProt.key
            length = min(len(keyA), len(keyB))
            qber = sum(a != b for a, b in zip(keyA, keyB)) / length if length > 0 else 0
            if qber > 0.11:
                KeyListA.append("nan"); KeyListB.append("nan"); KeyRateList.append("nan")
            else:
                KeyListA.append(keyA)
                KeyListB.append(keyB)
                KeyRateList.append(len(keyA) * 10**9 / (bobProt.end_time - startTime))
        else:
            KeyListA.append("nan")
            KeyListB.append("nan")
            KeyRateList.append("nan")

    return KeyListA, KeyListB, KeyRateList


def run_BB84_sims(runtimes=10,
                  fibreLen=1,
                  qDelay=0,
                  qSpeed=0.8,
                  photonCount=1024,
                  sourceFreq=1e7,
                  lenLoss=0,
                  initLoss=0,
                  detectorEffZ=1,
                  detectorEffX=None,
                  darkCount=0,
                  nodeLossDb=0.0,
                  sourceErrRate=0.0,
                  dephasingRate=0.0,
                  workers=None):

    n = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n = min(n, runtimes)

    # distribute runtimes as evenly as possible across workers
    base, remainder = divmod(runtimes, n)
    sizes = [base + (1 if i < remainder else 0) for i in range(n)]

    job_args = [(s, fibreLen, qDelay, qSpeed, photonCount, sourceFreq,
                 lenLoss, initLoss, detectorEffZ, detectorEffX, darkCount, nodeLossDb, sourceErrRate, dephasingRate) for s in sizes]

    with get_context('spawn').Pool(n) as pool:
        parts = pool.map(_bb84_chunk, job_args)

    KeyListA, KeyListB, KeyRateList = [], [], []
    for kA, kB, kR in parts:
        KeyListA.extend(kA)
        KeyListB.extend(kB)
        KeyRateList.extend(kR)

    return KeyListA, KeyListB, KeyRateList


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--fibre",          type=float, default=50,   help="Fibre length (km)")
    parser.add_argument("--runtimes",       type=int,   default=10,   help="Number of simulation runs")
    parser.add_argument("--det-eff-x",      type=float, default=None, help="X-basis detector efficiency (default: same as Z)")
    parser.add_argument("--dephasing-rate", type=float, default=None, help="Dephasing rate per km (default: 0)")
    args = parser.parse_args()
    cfg  = load_config(args.config)

    _, _, rates = run_BB84_sims(
        runtimes      = args.runtimes,
        fibreLen      = args.fibre,
        lenLoss       = cfg["fibre_loss_db_per_km"],
        initLoss      = cfg["init_loss"],
        detectorEffZ  = cfg["detector_efficiency"],
        detectorEffX  = args.det_eff_x,
        darkCount     = cfg["dark_count_rate"],
        nodeLossDb    = cfg["node_loss_db"],
        sourceErrRate = cfg["source_error_rate"],
        dephasingRate = args.dephasing_rate if args.dephasing_rate is not None else cfg["dephasing_rate"],
    )
    valid = [r for r in rates if r != "nan"]
    avg   = f"{sum(valid)/len(valid):.2f} bps" if valid else "no completed runs"
    print(f"BB84 | fibre={args.fibre}km | avg key rate: {avg}")
