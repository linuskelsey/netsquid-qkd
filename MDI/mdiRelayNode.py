import netsquid as ns
import numpy as np

from netsquid.components.qsource import SourceStatus
from netsquid.protocols import NodeProtocol



class RelayNodeProtocol(NodeProtocol):
    """
    Protocol to run on End User node in point-to-point BB84.

    Attributes:
        

    Parameters:
        
    """
    def __init__(self, node, name, photonCount, portNames=["Q0.In", "Q1.In", "C0.In", "C1.In", "C0.Out", "C1.Out", "C0.In.basis", "C1.In.basis"], detectorEffZ=1, detectorEffX=None, darkCount=0, sourceFreq=1e7, nodeLossDb=0.0, aliceProto=None, bobProto=None, bsEff=1.0):
        super().__init__()

        # distinguish node on which the protocol runs
        self.node = node
        self.name = name.title()

        # end users each send photonCount//2 photons; relay index space must match
        self.photon_count = photonCount // 2

        # ports, 0/1 denotes side, i/o denotes in/out. basis ports handle matching.
        self.port_q0_i_name = portNames[0]
        self.port_q1_i_name = portNames[1]
        self.port_c0_i_name = portNames[2]
        self.port_c1_i_name = portNames[3]
        self.port_c0_o_name = portNames[4]
        self.port_c1_o_name = portNames[5]
        self.port_c0_i_basis_name = portNames[6]
        self.port_c1_i_basis_name = portNames[7]

        # detector efficiency
        self.detector_eff_z = detectorEffZ
        self.detector_eff_x = detectorEffX if detectorEffX is not None else detectorEffZ
        self.node_loss_prob = 1 - 10 ** (-nodeLossDb / 10)
        # per-slot dark click probability; distance effect emerges naturally as fewer real photons arrive
        self.dark_count   = darkCount
        self.source_freq  = sourceFreq
        self.dark_rate    = self.dark_count / (self.dark_count + self.source_freq)

        # beam splitter efficiency at relay BSM
        self.bs_eff = bsEff

        # end-user protocol refs for basis-dependent detector efficiency (simulation peek)
        self.alice_proto = aliceProto
        self.bob_proto   = bobProto

        # measurement list
        self.meas = []


    def bsm_total(self):
        """
        Perform Bell State Measurements on received qubits.

        Simplified for current modelling with no synchronisation or memory constraints.
        """

        port_q0   = self.node.ports[self.port_q0_i_name]
        port_q1   = self.node.ports[self.port_q1_i_name]
        port_c0   = self.node.ports[self.port_c0_i_name]
        port_c1   = self.node.ports[self.port_c1_i_name]

        received = {}

        # Keep looping until all four messages have arrived
        while len(received) < 4:
            yield (
                self.await_port_input(port_q0) |
                self.await_port_input(port_q1) |
                self.await_port_input(port_c0) |
                self.await_port_input(port_c1)
            )
            # Drain whichever ports fired
            for key, port in [("q0", port_q0), ("q1", port_q1),
                            ("idx0", port_c0), ("idx1", port_c1)]:
                if key not in received:
                    msg = port.rx_input()
                    if msg is not None and msg.items:
                        received[key] = msg.items

        q_list0 = received["q0"]
        q_list1 = received["q1"]
        idx0    = received["idx0"]
        idx1    = received["idx1"]

        # list of common received indices
        q_dict0 = dict(zip(idx0, q_list0))
        q_dict1 = dict(zip(idx1, q_list1))

        common = set(q_dict0.keys()) & set(q_dict1.keys())

        for i in sorted(common):
            coupled0 = np.random.random() >= self.node_loss_prob
            coupled1 = np.random.random() >= self.node_loss_prob
            eff0 = self.detector_eff_x if (self.alice_proto is not None and self.alice_proto.basis_list[i]) else self.detector_eff_z
            eff1 = self.detector_eff_x if (self.bob_proto   is not None and self.bob_proto.basis_list[i])   else self.detector_eff_z
            real0 = coupled0 and np.random.random() < (self.bs_eff * eff0)
            real1 = coupled1 and np.random.random() < (self.bs_eff * eff1)
            dark0 = np.random.random() < self.dark_rate
            dark1 = np.random.random() < self.dark_rate

            det0 = real0 or dark0
            det1 = real1 or dark1

            if not (det0 and det1):
                continue

            if (dark0 and not real0) or (dark1 and not real1):
                self.meas.append((i, np.random.choice([-1, 0, 1])))
            else:
                q0, q1 = q_dict0[i], q_dict1[i]
                ns.qubits.operate([q0, q1], ns.CNOT)
                ns.qubits.operate(q0, ns.H)
                a, _ = ns.qubits.measure(q0)
                b, _ = ns.qubits.measure(q1)

                if a == 1 and b == 1:
                    self.meas.append((i, -1))
                elif a == 0 and b == 1:
                    self.meas.append((i, 1))
                else:
                    self.meas.append((i, 0))

        # dark counts on lost slots — one or both photons were absorbed by fibre
        idx0_set = set(idx0)
        idx1_set = set(idx1)

        # both photons lost
        for i in sorted(set(range(self.photon_count)) - idx0_set - idx1_set):
            if np.random.random() < self.dark_rate and np.random.random() < self.dark_rate:
                self.meas.append((i, np.random.choice([-1, 0, 1])))

        # only Alice's photon arrived
        for i in sorted(idx0_set - idx1_set):
            eff0 = self.detector_eff_x if (self.alice_proto is not None and self.alice_proto.basis_list[i]) else self.detector_eff_z
            det0 = np.random.random() < (self.bs_eff * eff0) or np.random.random() < self.dark_rate
            if det0 and np.random.random() < self.dark_rate:
                self.meas.append((i, np.random.choice([-1, 0, 1])))

        # only Bob's photon arrived
        for i in sorted(idx1_set - idx0_set):
            eff1 = self.detector_eff_x if (self.bob_proto is not None and self.bob_proto.basis_list[i]) else self.detector_eff_z
            det1 = np.random.random() < (self.bs_eff * eff1) or np.random.random() < self.dark_rate
            if np.random.random() < self.dark_rate and det1:
                self.meas.append((i, np.random.choice([-1, 0, 1])))

    def basis_matching(self):
        """
        Receive basis lists from EndNodes and communicate back those bits to discard
        """
        port0 = self.node.ports[self.port_c0_i_basis_name]
        port1 = self.node.ports[self.port_c1_i_basis_name]

        received = {}
        while len(received) < 2:
            yield self.await_port_input(port0) | self.await_port_input(port1)
            for key, port in [("b0", port0), ("b1", port1)]:
                if key not in received:
                    msg = port.rx_input()
                    if msg is not None and msg.items:
                        received[key] = msg.items

        basis_list0 = received["b0"]
        basis_list1 = received["b1"]

        discard = [i for i, b in enumerate(basis_list0) if b != basis_list1[i]]
        out = discard if discard else [-1]
        self.node.ports[self.port_c0_o_name].tx_output(out)
        self.node.ports[self.port_c1_o_name].tx_output(out)


    def run(self):
        """
        Run RelayNodeProtocol.
        """
        # BSMs
        yield from self.bsm_total()

        # send measurement results
        self.node.ports[self.port_c0_o_name].tx_output(self.meas)
        self.node.ports[self.port_c1_o_name].tx_output(self.meas)

        #receive bases and send matching to end nodes
        yield from self.basis_matching()
