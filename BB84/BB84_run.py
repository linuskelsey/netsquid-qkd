from difflib import SequenceMatcher
import netsquid as ns

from netsquid.nodes import Node
from netsquid.components import QuantumChannel, ClassicalChannel

import sys
scriptpath = "lib/"
sys.path.append(scriptpath)
from lib.functions import HybridDelayModel

from BB84_Alice import AliceProtocol
from BB84_Bob import BobProtocol



def run_BB84_sims(runtimes=10,
                  fibreLen=1,
                  qDelay=0,
                  qSpeed=0.8,
                  photonCount=1024,
                  sourceFreq=1e7,
                  lenLoss=0,
                  initLoss=0,
                  detectorEff=1):
    
    KeyListA    = []
    KeyListB    = []
    KeyRateList = []

    counts = []

    for _ in range(runtimes):

        ns.sim_reset()

        # nodes =================================================
        alice = Node("Alice", port_names=["A.Q.Out", "A.C.Out", "A.C.In", "A.C.Out.tags"])
        bob   = Node("Bob", port_names=["B.Q.In", "B.C.In", "B.C.Out", "B.C.In.tags"])

        # channels ==============================================
        QChann = QuantumChannel("[A: -Q-> :B]",
                                delay=qDelay,
                                length=fibreLen,
                                models={
                                    "delay_model": HybridDelayModel(SoL_fraction=qSpeed,stddev=0.05)
                                })
        
        alice.connect_to(bob,
                         QChann,
                         local_port_name=alice.ports["A.Q.Out"].name,
                         remote_port_name=bob.ports["B.Q.In"].name)
        

        CChann1 = ClassicalChannel("[A: -C-> :B]",
                                delay=0,
                                length=fibreLen,
                                models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed,stddev=0.05)})
        
        CChann2 = ClassicalChannel("[B: -C-> :A]",
                                delay=0,
                                length=fibreLen,
                                models={"delay_model": HybridDelayModel(SoL_fraction=qSpeed,stddev=0.05)})
        
        alice.connect_to(bob,
                         CChann1,
                         local_port_name=alice.ports["A.C.Out"].name,
                         remote_port_name=bob.ports["B.C.In"].name)
        
        bob.connect_to(alice,
                       CChann2,
                       local_port_name=bob.ports["B.C.Out"].name,
                       remote_port_name=alice.ports["A.C.In"].name)

        CChann3 = ClassicalChannel("[A: -C:tags-> :B]",
                                   delay=0,
                                   length=fibreLen,
                                   models={'delay_model': HybridDelayModel(SoL_fraction=qSpeed, stddev=0.05)})
        
        alice.connect_to(bob,
                         CChann3,
                         local_port_name=alice.ports["A.C.Out.tags"].name,
                         remote_port_name=bob.ports["B.C.In.tags"].name)

        # protocols =============================================
        aliceProt = AliceProtocol(alice, photonCount, sourceFreq, portNames=list(alice.ports.keys()), fibreLen=fibreLen, lenLoss=lenLoss, initLoss=initLoss)
        bobProt = BobProtocol(bob, photonCount, portNames=list(bob.ports.keys()), detectorEff=detectorEff)

        bobProt.start()
        aliceProt.start()

        startTime = ns.util.simtools.sim_time(magnitude=ns.NANOSECOND)
        stats = ns.sim_run()

        if bobProt.end_time is not None:
            endTime = bobProt.end_time
            keyA, keyB = aliceProt.key, bobProt.key

            KeyListA.append(keyA)
            KeyListB.append(keyB)

            keyRate = len(keyA) * 10**9 / (endTime - startTime)
            KeyRateList.append(keyRate)
        else:
            KeyListA.append("nan")
            KeyListB.append("nan")
            KeyRateList.append("nan")

    return KeyListA, KeyListB, KeyRateList
