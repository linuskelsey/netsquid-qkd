import netsquid as ns
import numpy as np

from netsquid.protocols import NodeProtocol
from netsquid.components import QSource
from netsquid.components.qsource import SourceStatus

import sys
scriptpath = "lib/"
sys.path.append(scriptpath)
from lib.functions import rng_bin_lst



class BobProtocol(NodeProtocol):
    def __init__(self, node, photonCount, portNames=["B.Q.In","B.C.In","B.C.Out","B.C.In.tags"], detectorEff=1):
        super().__init__()
        self.node         = node
        self.photon_count = photonCount
        self.port_qi_name = portNames[0]
        self.port_ci_name = portNames[1]
        self.port_co_name = portNames[2]
        self.port_ci_tags_name = portNames[3]

        self.detector_eff = detectorEff

        self.basis_list   = rng_bin_lst(photonCount)
        self.meas_results = []
        self.mask         = []
        self.key          = []
        self.end_time     = None

        self.bits = []


    def receive_and_measure(self):
        """
        Receive qubit batch on B.Q.In, measure in pre-assigned bases, store outcomes
        """
        # wait for qubit array input to port
        port = self.node.ports[self.port_qi_name]
        yield self.await_port_input(port)
        qubit_batch = port.rx_input().items

        # receive arrival indices from Alice
        port_c = self.node.ports[self.port_ci_tags_name]
        yield self.await_port_input(port_c)
        self.arrived_indices = port_c.rx_input().items
        
        # measure and store
        for i, q in zip(self.arrived_indices, qubit_batch):
            #detector efficiency
            if np.random.random() > self.detector_eff:
                continue
            basis = self.basis_list[i]
            if basis: ns.qubits.operate(q,ns.H)  # if: X basis, then: rotate
            meas = ns.qubits.measure(q)[0]       # Z basis measurement
            self.meas_results.append((i, meas))  # outcome bit with index
            self.bits.append((i, basis, meas))
        
        self.key = [m for _, m in self.meas_results]


    def basis_reconciliation(self):
        """
        Receive basis choices from Alice, send Bob's and sift common bits into self.key
        """
        # send to Alice
        self.node.ports[self.port_co_name].tx_output(self.basis_list)

        # identify classical in port and await Alice's basis list
        port = self.node.ports[self.port_ci_name]
        yield self.await_port_input(port)
        alice_bases = port.rx_input().items

        self.mask = [i for i, b in enumerate(alice_bases) if b == self.basis_list[i]]
        
        # finalise key output by matching bases
        self.key = [meas for i, meas in self.meas_results if self.basis_list[i] == alice_bases[i]]


    def run(self):
        """
        Run Bob's protocol in full
        """
        # Wait for Alice's qubits + auto‑measure
        yield from self.receive_and_measure()
        
        # Basis exchange + sift
        yield from self.basis_reconciliation()

        # set end time of simulation
        self.end_time = ns.sim_time(magnitude=ns.NANOSECOND)
