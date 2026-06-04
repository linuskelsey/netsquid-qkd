from multiprocessing import Pool
import os

import netsquid as ns

from netsquid.nodes import Node
from netsquid.components import QuantumChannel, ClassicalChannel

import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib"))
from lib.functions import HybridDelayModel, load_config, config_arg_parser

from mdiEndUser import EndNodeProtocol
from mdiRelayNode import RelayNodeProtocol



def _mdi_chunk(args):
    """Sequential simulation block — runs runtimes iterations and returns partial results."""
    runtimes, fibreLen, qDelay, qSpeed, photonCount, sourceFreq, lenLoss, initLoss, detectorEff, darkCount = args

    KeyListA    = []
    KeyListB    = []
    KeyRateList = []

    for _ in range(runtimes):
        ns.sim_reset()

        # nodes =================================================
        alice   = Node("Alice",   port_names=["A.Q.Out", "A.C.Out", "A.C.In", "A.C.Out.basis"])
        bob     = Node("Bob",     port_names=["B.Q.Out", "B.C.Out", "B.C.In", "B.C.Out.basis"])
        charlie = Node("Charlie", port_names=["C.Q.In.A", "C.Q.In.B", "C.C.In.A", "C.C.In.B",
                                              "C.C.Out.A", "C.C.Out.B", "C.C.In.A.basis", "C.C.In.B.basis"])

        # channels ==============================================
        QChann1 = QuantumChannel("[A: -Q-> :C]", delay=qDelay, length=fibreLen/2,
                                 models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        QChann2 = QuantumChannel("[B: -Q-> :C]", delay=qDelay, length=fibreLen/2,
                                 models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})

        alice.connect_to(charlie, QChann1,
                         local_port_name=alice.ports["A.Q.Out"].name,
                         remote_port_name=charlie.ports["C.Q.In.A"].name)
        bob.connect_to(charlie, QChann2,
                       local_port_name=bob.ports["B.Q.Out"].name,
                       remote_port_name=charlie.ports["C.Q.In.B"].name)

        CChann1 = ClassicalChannel("[A: -C-> :C]", delay=0, length=fibreLen/2,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann2 = ClassicalChannel("[B: -C-> :C]", delay=0, length=fibreLen/2,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann3 = ClassicalChannel("[C: -C-> :A]", delay=0, length=fibreLen/2,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann4 = ClassicalChannel("[C: -C-> :B]", delay=0, length=fibreLen/2,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann5 = ClassicalChannel("[A: -C.basis-> :C]", delay=0, length=fibreLen/2,
                                   models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        CChann6 = ClassicalChannel("[B: -C.basis-> :C]", delay=0, length=fibreLen/2,
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
                                      fibreLen=fibreLen/2, lenLoss=lenLoss, initLoss=initLoss)
        bobProt     = EndNodeProtocol(bob, 'bob', photonCount, sourceFreq,
                                      portNames=["B.Q.Out", "B.C.Out", "B.C.In", "B.C.Out.basis"],
                                      fibreLen=fibreLen/2, lenLoss=lenLoss, initLoss=initLoss)
        charlieProt = RelayNodeProtocol(charlie, 'charlie', photonCount,
                                        portNames=["C.Q.In.A", "C.Q.In.B", "C.C.In.A", "C.C.In.B",
                                                   "C.C.Out.A", "C.C.Out.B", "C.C.In.A.basis", "C.C.In.B.basis"],
                                        detectorEff=detectorEff, darkCount=darkCount, sourceFreq=sourceFreq)

        bobProt.flipper = True

        charlieProt.start()
        aliceProt.start()
        bobProt.start()

        startTime = ns.util.simtools.sim_time(magnitude=ns.NANOSECOND)
        ns.sim_run(end_time=ns.SECOND * 100)

        if aliceProt.end_time is not None and bobProt.end_time is not None:
            endTime = max(aliceProt.end_time, bobProt.end_time)
            keyA, keyB = aliceProt.key, bobProt.key
            KeyListA.append(keyA)
            KeyListB.append(keyB)
            KeyRateList.append(len(keyA) * 10**9 / (endTime - startTime))
        else:
            KeyListA.append("nan")
            KeyListB.append("nan")
            KeyRateList.append("nan")

    return KeyListA, KeyListB, KeyRateList


def run_mdi_sims(runtimes=10,
                 fibreLen=1,
                 qDelay=0,
                 qSpeed=0.8,
                 photonCount=1024,
                 sourceFreq=1e7,
                 lenLoss=0,
                 initLoss=0,
                 detectorEff=1,
                 darkCount=0,
                 workers=None):

    n = max(1, int(os.cpu_count() * 0.8)) if workers is None else workers
    n = min(n, runtimes)

    base, remainder = divmod(runtimes, n)
    sizes = [base + (1 if i < remainder else 0) for i in range(n)]

    job_args = [(s, fibreLen, qDelay, qSpeed, photonCount, sourceFreq,
                 lenLoss, initLoss, detectorEff, darkCount) for s in sizes]

    with Pool(n) as pool:
        parts = pool.map(_mdi_chunk, job_args)

    KeyListA, KeyListB, KeyRateList = [], [], []
    for kA, kB, kR in parts:
        KeyListA.extend(kA)
        KeyListB.extend(kB)
        KeyRateList.extend(kR)

    return KeyListA, KeyListB, KeyRateList


if __name__ == "__main__":
    parser = config_arg_parser()
    parser.add_argument("--fibre",    type=float, default=50,  help="Fibre length (km)")
    parser.add_argument("--runtimes", type=int,   default=10,  help="Number of simulation runs")
    args = parser.parse_args()
    cfg  = load_config(args.config)

    _, _, rates = run_mdi_sims(
        runtimes    = args.runtimes,
        fibreLen    = args.fibre,
        lenLoss     = cfg["fibre_loss_db_per_km"],
        initLoss    = cfg["init_loss"],
        detectorEff = cfg["detector_efficiency"],
        darkCount   = cfg["dark_count_rate"],
    )
    valid = [r for r in rates if r != "nan"]
    avg   = f"{sum(valid)/len(valid):.2f} bps" if valid else "no completed runs"
    print(f"MDI  | fibre={args.fibre}km | avg key rate: {avg}")
