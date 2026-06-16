from multiprocessing import get_context
import os

import netsquid as ns

from netsquid.nodes import Node
from netsquid.components import QuantumChannel, ClassicalChannel
from netsquid.components.models.qerrormodels import DephaseNoiseModel

import sys
_this_dir  = os.path.dirname(os.path.abspath(__file__))
_repo_root = os.path.dirname(_this_dir)
sys.path.insert(0, _this_dir)   # mdiEndUser, mdiRelayNode
sys.path.insert(0, _repo_root)  # lib.functions
from lib.functions import HybridDelayModel, load_config, config_arg_parser

from mdiEndUser import EndNodeProtocol
from mdiRelayNode import RelayNodeProtocol



def _mdi_chunk(args):
    """Sequential simulation block — runs runtimes iterations and returns partial results."""
    runtimes, fibreLen, qDelay, qSpeed, photonCount, sourceFreq, lenLoss, initLoss, detectorEffZ, detectorEffX, darkCount, nodeLossDb, sourceErrRate, dephasingRate, bsEff, charliePos = args

    KeyListA    = []
    KeyListB    = []
    KeyRateList = []
    QBERList    = []

    for _ in range(runtimes):
        ns.sim_reset()

        # nodes =================================================
        alice   = Node("Alice",   port_names=["A.Q.Out", "A.C.Out", "A.C.In", "A.C.Out.basis"])
        bob     = Node("Bob",     port_names=["B.Q.Out", "B.C.Out", "B.C.In", "B.C.Out.basis"])
        charlie = Node("Charlie", port_names=["C.Q.In.A", "C.Q.In.B", "C.C.In.A", "C.C.In.B",
                                              "C.C.Out.A", "C.C.Out.B", "C.C.In.A.basis", "C.C.In.B.basis"])

        # channels ==============================================
        lenA = fibreLen * charliePos
        lenB = fibreLen * (1 - charliePos)
        QChann1 = QuantumChannel("[A: -Q-> :C]", delay=qDelay, length=lenA,
                                 models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05),
                                         "quantum_noise_model": DephaseNoiseModel(min(1.0, dephasingRate * lenA), time_independent=True)})
        QChann2 = QuantumChannel("[B: -Q-> :C]", delay=qDelay, length=lenB,
                                 models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05),
                                         "quantum_noise_model": DephaseNoiseModel(min(1.0, dephasingRate * lenB), time_independent=True)})

        alice.connect_to(charlie, QChann1,
                         local_port_name=alice.ports["A.Q.Out"].name,
                         remote_port_name=charlie.ports["C.Q.In.A"].name)
        bob.connect_to(charlie, QChann2,
                       local_port_name=bob.ports["B.Q.Out"].name,
                       remote_port_name=charlie.ports["C.Q.In.B"].name)

        CChann1 = ClassicalChannel("[A: -C-> :C]", delay=0, length=lenA,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann2 = ClassicalChannel("[B: -C-> :C]", delay=0, length=lenB,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann3 = ClassicalChannel("[C: -C-> :A]", delay=0, length=lenA,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann4 = ClassicalChannel("[C: -C-> :B]", delay=0, length=lenB,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann5 = ClassicalChannel("[A: -C.basis-> :C]", delay=0, length=lenA,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann6 = ClassicalChannel("[B: -C.basis-> :C]", delay=0, length=lenB,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})

        alice.connect_to(charlie, CChann1,
                         local_port_name=alice.ports["A.C.Out"].name,
                         remote_port_name=charlie.ports["C.C.In.A"].name)
        bob.connect_to(charlie, CChann2,
                       local_port_name=bob.ports["B.C.Out"].name,
                       remote_port_name=charlie.ports["C.C.In.B"].name)
        charlie.connect_to(alice, CChann3,
                           local_port_name=charlie.ports["C.C.Out.A"].name,
                           remote_port_name=alice.ports["A.C.In"].name)
        charlie.connect_to(bob, CChann4,
                           local_port_name=charlie.ports["C.C.Out.B"].name,
                           remote_port_name=bob.ports["B.C.In"].name)
        alice.connect_to(charlie, CChann5,
                         local_port_name=alice.ports["A.C.Out.basis"].name,
                         remote_port_name=charlie.ports["C.C.In.A.basis"].name)
        bob.connect_to(charlie, CChann6,
                       local_port_name=bob.ports["B.C.Out.basis"].name,
                       remote_port_name=charlie.ports["C.C.In.B.basis"].name)

        # protocols =============================================
        aliceProt   = EndNodeProtocol(alice, 'alice', photonCount, sourceFreq,
                                      portNames=["A.Q.Out", "A.C.Out", "A.C.In", "A.C.Out.basis"],
                                      fibreLen=lenA, lenLoss=lenLoss, initLoss=initLoss,
                                      sourceErrRate=sourceErrRate)
        bobProt     = EndNodeProtocol(bob, 'bob', photonCount, sourceFreq,
                                      portNames=["B.Q.Out", "B.C.Out", "B.C.In", "B.C.Out.basis"],
                                      fibreLen=lenB, lenLoss=lenLoss, initLoss=initLoss,
                                      sourceErrRate=sourceErrRate)
        charlieProt = RelayNodeProtocol(charlie, 'charlie', photonCount,
                                        portNames=["C.Q.In.A", "C.Q.In.B", "C.C.In.A", "C.C.In.B",
                                                   "C.C.Out.A", "C.C.Out.B", "C.C.In.A.basis", "C.C.In.B.basis"],
                                        detectorEffZ=detectorEffZ, detectorEffX=detectorEffX,
                                        darkCount=darkCount, sourceFreq=sourceFreq, nodeLossDb=nodeLossDb,
                                        aliceProto=aliceProt, bobProto=bobProt, bsEff=bsEff)

        bobProt.flipper = True

        charlieProt.start()
        aliceProt.start()
        bobProt.start()

        startTime = ns.util.simtools.sim_time(magnitude=ns.NANOSECOND)
        ns.sim_run(end_time=ns.SECOND * 100)

        if aliceProt.end_time is not None and bobProt.end_time is not None:
            endTime = max(aliceProt.end_time, bobProt.end_time)
            keyA, keyB = aliceProt.key, bobProt.key
            length = min(len(keyA), len(keyB))
            qber = sum(a != b for a, b in zip(keyA, keyB)) / length if length > 0 else 0
            QBERList.append(qber)
            if qber > 0.11:
                KeyListA.append("nan"); KeyListB.append("nan"); KeyRateList.append("nan")
            else:
                KeyListA.append(keyA)
                KeyListB.append(keyB)
                KeyRateList.append(len(keyA) * 10**9 / (endTime - startTime))
        else:
            QBERList.append(None)
            KeyListA.append("nan")
            KeyListB.append("nan")
            KeyRateList.append("nan")

    return KeyListA, KeyListB, KeyRateList, QBERList


def run_mdi_sims(runtimes=10,
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
                 bsEff=1.0,
                 charliePos=0.5,
                 workers=None):

    n = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n = min(n, runtimes)

    base, remainder = divmod(runtimes, n)
    sizes = [base + (1 if i < remainder else 0) for i in range(n)]

    job_args = [(s, fibreLen, qDelay, qSpeed, photonCount, sourceFreq,
                 lenLoss, initLoss, detectorEffZ, detectorEffX, darkCount, nodeLossDb, sourceErrRate, dephasingRate, bsEff, charliePos) for s in sizes]

    with get_context('spawn').Pool(n) as pool:
        parts = pool.map(_mdi_chunk, job_args)

    KeyListA, KeyListB, KeyRateList, QBERList = [], [], [], []
    for kA, kB, kR, kQ in parts:
        KeyListA.extend(kA)
        KeyListB.extend(kB)
        KeyRateList.extend(kR)
        QBERList.extend(kQ)

    return KeyListA, KeyListB, KeyRateList, QBERList


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--fibre",          type=float, default=20,   help="Fibre length (km)")
    parser.add_argument("--runtimes",       type=int,   default=10,   help="Number of simulation runs")
    parser.add_argument("--det-eff-x",      type=float, default=None, help="X-basis detector efficiency (default: same as Z)")
    parser.add_argument("--dephasing-rate", type=float, default=None, help="Dephasing rate per km (default: 0)")
    parser.add_argument("--bs-eff",         type=float, default=None, help="Beam splitter efficiency at relay (default: 1)")
    args = parser.parse_args()
    cfg  = load_config(args.config)

    _, _, rates, _ = run_mdi_sims(
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
        bsEff         = args.bs_eff if args.bs_eff is not None else cfg["bs_eff"],
    )
    valid = [r for r in rates if r != "nan"]
    avg   = f"{sum(valid)/len(valid):.2f} bps" if valid else "no completed runs"
    print(f"MDI  | fibre={args.fibre}km | avg key rate: {avg}")
