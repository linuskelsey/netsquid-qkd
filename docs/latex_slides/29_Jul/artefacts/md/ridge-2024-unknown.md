# SIMULATORS FOR QUANTUM NETWORK MODELLING: A COMPREHENSIVE REVIEW 

**Oceane Bel Mariam Kiran** Physical & Computational Sciences Directorate Computational Sciences and Engineering Division Pacific Northwest National Laboratory Oak Ridge National Laboratory Richland, WA, USA Oak Ridge, TN, USA `obel@pnnl.gov kiranm@ornl.gov` 

August 23, 2024 

## **ABSTRACT** 

Quantum network research, is exploring new networking protocols, physics-based hardware and novel experiments to demonstrate how quantum distribution will work over large distances. Current work explores much of these concepts in simulations, that are developed to understand how quantum networking will be set up and researchers can experiment virtually. Exposing flaws in network designs, like unsustainable topologies, or develop protocols that efficiently utilize network resources, simulators can also help assess whether workloads are balanced across virtual machines in the network. However, much of these simulation models come without reliable verification methods, for testing performance in real deployments. 

In this paper, we present a review of, to the best of our knowledge, currently used toolkits for modeling quantum networks. With these toolkits and standardized validation techniques, we can lay down the foundations for more accurate and reliable quantum network simulators. 

### **Topics: Quantum network, network models, simulators, verification and validation** 

## **1 Introduction** 

Quantum networks are the next generation of communication networks that deliver entanglement and connect distributed quantum physics devices such as quantum computers, sensors and detectors [1, 2, 3, 4]. Instead of classical ‘bits’ (0s,1s), qubits are transmitted that can encode more information, by using the spin of the photons. Argued to be the next internet revolution, distributed quantum networks have shown case studies to process and communicate secure and highly accurate measurements, currently beyond the classical machines [5]. 

Industry quantum efforts are developing new hardware, protocols and tools that can enable quantum information exchange. These technologies can demonstrate reliable quantum communication with high rates of fidelity and automated error correction [6, 7, 8]. Some of these approaches use discrete and continuous variable demonstrations, each bringing their own capabilities in the experiments [9], or transmission over fiber optical cable or free space point to point communication. Network loss plays a huge role in guaranteeing the validity of the quantum states, current demonstrations have only shown upto 300 km [10]. With the help of quantum repeaters, one can extend these to longer distances such that quantum states can be refreshed or preserved [11, 12, 13]. 

Quantum network simulations are also being developed to help define use cases, and collect data to build reliable devices. Several efforts such as Qunet [14], ComNetsEmu [15], or Cisco’s QnetLab are focused on developing kits that can interface with other simulations and provide a GUI, to build topology, collect parameters and investigate new protocols. These can demonstrate large-distance transmission using repeaters and help identify solutions to protocols that can utilize network resources effectively. However, these simulation toolkits, still lack robust testing and verification methods to verify the accuracy of simulated quantum networks and how these would translate in the real world hardware. 



<!-- Start of picture text -->
Classical layer Node controller Node controller<br>Network Switch Network Switch<br>ITT ETT<br>Control layer<br>= GH) &)<br>2 [ll (Ng—Ng |[]<br>TDC Orchestrator DWDM DWDM Orchestrator Signal generator<br>Communication medium<br>for classical signals<br>Quantum Network<br>Layer<br>1 SNSPD ro @;<br>(I : [<br>11 w <<br>1 ( l<br>1 1 1 1<br>loco 20000 looocooooooocooooocoooocooooooool<br>Hong-Ou-Mandel Interference Quantum frequency transduction<br><!-- End of picture text -->

A PREPRINT - AUGUST 23, 2024 

Section 4 discusses the challenges in these platforms and how these can improved in Section 5. Finally, Section 6 concludes and presents future research directions in this area. 

## **2 Challenges in Designing Quantum Network Simulators** 

The first design consideration is correctly modeling Quantum Nodes and Channels [19]. Factors such as qubit connectivity, gate fidelity, and quantum channel characteristics [20], and scaling with the size of the quantum network while maintaining computational efficiency are all challenges for simulators. 

The second consideration is realism [21] of the behavior of quantum operations on the network. Realistic quantum operations, such as gates, measurements, and entanglement generation, need to pay attention to the impact of noise and errors. This means that simulators need to have capabilities for simulating quantum error correction techniques. Using accurate quantum models to reflect the behavior of physical quantum systems, needs a tool to evaluate the performance of error correction codes and their effectiveness in mitigating the impact of these on quantum communication. 

A third consideration, there is a need to develop a comprehensive benchmarking and validation framework to assess the performance of the simulator. This framework should include metrics for success rates, fidelity, speed, scalability, and resource utilization in entanglement distribution and other quantum communication tasks. It should also have a user-friendly interface, which allows users to setup, configure, and analyse quantum network simulations. It should provide tools for visualizing network states, quantum operations, and simulation results. The interface should be able to measure the accuracy of the simulation compared to what is expected in the real world. Existing work [22] on validation of simulation has used simulator platforms, such as the QISKit platform developed by IBM. The interface needs to validate the simulator against experimental data where possible. Because of a lack of available hardware, gathering heuristics to create a theoretical representation of the network’s expected behavior will help validating results. 

Finally, since work on quantum networks is continuously updating, simulators need to use a modular and extensible architecture. This allows users to easily incorporate new features, quantum algorithms, or simulation models to adapt the simulator to evolving research needs. Additionally, it also allows for validation tools to be incorporated into the simulation. Therefore, any standardized validation framework should also be modular to allow for new validation techniques to be added to the framework as they become available. 

### **2.1 Understanding the output of a simulation** 

Simulations can be compared with known analytical solutions for specific quantum algorithms or network scenarios. For modeling entanglement distribution, validation methods include comparing the success rates, fidelity, and speed of entanglement generation with theoretical expectations and experimental data. 

Another approach to validation is compare the resulting behavior of the simulation to an ideal solution. For this case, idealized simulations, where noise and errors are minimized or absent, can be used to verify the correctness of the implementation. Comparing results from a noise-free simulation with theoretical expectations helps ensure the accuracy of the simulator’s fundamental quantum operations. Simulators like QuNetSim or SeQUeNCE, have assumed minimal to no errors in their models. 

### **2.2 Quantum-Classical Hybrid simulators** 

Researchers have combined classical and quantum hybrid networks to develop full quantum networks [23]. Here a validation framework also validates classical network capabilities and their impact on quantum networks. The interaction between classical and quantum networks includes simulating the interaction between classical and quantum information processing. Many existing quantum workloads and applications use a mix of pure quantum algorithms and classical programs. For example, “proper quantum” algorithms were still hybrid [24] use the Shor algorithm to model quantum parts but used classical processing for the data. 

Quantum machine learning [25, 26] uses classical machine learning enhanced or replaced by quantum algorithms [27, 28]. Hybrid approaches often involve classical pre-processing or post-processing steps alongside quantum algorithms to address machine learning tasks such as classification, clustering, and optimization. The preprocessing and optimization may take advantage of the cloud capabilities as an intermediate to distribute such large models developing Quantum Cloud Computing. 

For Quantum Cloud Computing [29] to have the needed resources, quantum processors can be integrated into cloud computing environments. Researchers have explored how classical and quantum resources can be orchestrated to perform computations efficiently, taking advantage of the strengths of both. Companies such as IBM [30], Microsoft [31], 

3 

A PREPRINT - AUGUST 23, 2024 

|QN Test|beds beingDeveloped|
|---|---|
|Testbed names|Authors|
|EPB Quantum Network (deployed and in<br>operation)|EPB Chattanooga, Tennessee|
|Oak RidgeQuantum Network Testbed|Oak Ridge National Lab,Tennessee|
|Center forQuantum Networks(CQN)|Tuscon,Arizona|
|Boston- Area Quantum Network (BAR-<br>QNET)|MIT, Harvard,_et al._|
|MITquantum Network testbed|Boston|
|ChicagoQuantum Exchange(CQE)|Chicago,Illinois|
|Quantum Application Network testbed for<br>Novel Entanglement Technology (QUANT-<br>NET)|Lawrence Berkeley National Laboratory, Berkeley, Cali-<br>fornia|
|AFRLQuantum Network|Rome,Italy|
|NYSQIT|StonyBrook,BNL,_et al_|
|NICT Quantum Network|National Institute of Information and Communications<br>Technology|
|QuDIT|Lawrence Livermore National Laboratory|
|DC-Qnet|Washington DC|
|Los AlamosQuantum Network|Los Alamos National Laboratory|



Table 1: List of quantum testbeds being developed across the world, to name a few. 

and Google [32] have started offering cloud services that include access to quantum processors. These services allow users to run quantum algorithms and experiments on real quantum hardware through cloud platforms [33]. The concept of hybrid quantum-classical cloud computing involves combining classical computing resources with quantum processing units. This approach is particularly useful for solving complex problems that leverage both classical and quantum algorithms. 

## **3 Overview of Quantum Networking** 

Quantum networking is the infrastructure connecting one or more quantum physics devices such as for distributed quantum computing, sensors or setting up an entangled quantum network. As a means to advance science, quantum networking applications are exploring how to connect multiple observatories for super-resolution images of distant planets [34, 7], or even link high-powered microscopes for unprecedented views of the micro-organisms [35], to help find more key insights in the problems being explored. 

By utilizing quantum entanglement distribution, quantum networks are being used to develop secure communication channels for governments, banks, and more, with applications of Quantum Key Distributions (QKDs) [36, 37, 38]. Qubits have two properties that enable these advances superposition and entanglement, that allows them to encode and carry information among two entangled qubits. However, qubits can be fragile and can loose their quantum states if there is loss or background noise. Various techniques can measure performance and stability of quantum networks such as state tomography [39], used to monitor the state of all qubits in a network, but is resource-intensive and becomes impractical for larger networks, or process tomography [40], which involves quantum operation in its fidelity and errors. Researchers have also developed the Bell state monitoring [41, 42] method, that utilizes entangled Bell states, where changes in correlations between entangled qubits reveal network errors. This is less resource-intensive than full tomography but offers limited information. 

Other developments in quantum repeaters and controllers are being used to amplify weaker signals, increase longer distances or perform qubit operations like rotations, measurements, and entanglement creation. 

Table 1 shows some examples of existing quantum network testbed developments. Testbeds offer a real-world platform for experimenting with actual hardware and protocols. 

### **3.1 Application of Quantum Networks** 

Some quantum applications, as seen in Table 2, include Quantum Key Distribution (QKD), sensing or quantum routing. Examples include QKD implementation in NS3 network simulator [43], clock synchronization accuracy [44] like GPS [45] and financial trading [46], or measuring magnetic fields or temperature over large distances with high 

4 

A PREPRINT - AUGUST 23, 2024 

|QN Ap<br>Application|plications over the last 5years<br>Description|
|---|---|
|Quantum KeyDistribution|Photons used to securelyshare encryption keys|
|Quantum sensing|Measure magnetic felds over large distances with high<br>precision for example[18]|
|Secure Cloud Computing|Secure access toquantum computers in the cloud|
|Distributed Quantum Computation|Distributed quantum processing across geographically dis-<br>tributedquantum computers|



Table 2: High level examples of Quantum Applications. 

||Q|uantum Network sim|ulators comparison||
|---|---|---|---|---|
|Simulators name|year|Small topology|Large topology|Focus|
|Squanch [57]|2018||X|GPU Acceleration + Quan-<br>tum information processing|
|SeQUeNCe [58, 59]|2019|X|X|Open-Source<br>+<br>User-<br>Friendly Interface|
|ComNetsEmu [15]|2020|X||In-network Artifcial Intelli-<br>gence + hybrid quantum net-<br>work|
|QuNetSim [14]|2021|X||Scalability + Performance|
|NetSquid [60]|2021|X|X|High-Performance Comput-<br>ing Integration|
|QDNS [61]|2021|X||<br>Python based + Reusable net-<br>work protocols|
|QuISP [62]|2022|X|X|Error Correction + Fault Tol-<br>erance|
|SimQN [63]|2023||X|User-Defned Noise Models|
|CiscoQnetlab[64]|2024|X|X|Simulations in the cloud|



Table 3: Simulation toolkits for Quantum Networks (More details can be seen in Figure 2). 

precision [47, 48], or quantum-enhanced MRI [49]. Quantum is also being explored for secure Cloud Computing [50, 51] applications to benefit fields like materials science and drug discovery [52, 53]. 

## **4 Overview of Quantum Networks simulators** 

Omnet++ [54], NetSim [55], and NS-3 [56] are well known network discrete-event simulators. These are a series of discrete event modeling toolkits used to simulate traffic flow, customer interactions in a call center, or packet flow in a network. The advantages of these are easier to implement and computationally efficient for large systems. However, these techniques are limited to discrete changes and may not capture continuous behavior accurately. 

On the other hand, mathematics-driven simulators or Equation-Based Modeling (EBM) use mathematical equations to represent system dynamics. The advantages of such a simulation approach is that it allows for accurate representation of continuous processes and is flexible, but can be complex to build. For instance, capturing all the possible states and transitions of qubits in the network can be cumbersome and resource intensive. Hamiltonian-based models are another model that describes the energy structure of the network, good for understanding energy transfer, entanglement generation, and other quantum phenomena in the network. Most quantum simulators have been listed in Table 3. 

### **4.1 QuISP** 

QuISP [62] is a quantum network simulator that uses the OMNET++ [54] framework as the base. OMNET++ is a C++ component-based framework used for building network simulators. In 2023, OMNET++ added several models to help users simulate more types of network and routing protocols such as routing protocol for low power and lossy networks. This uses Monte-Carlo simulation and supports error channels including Pauli channels and excitation/relaxation channels. Here, the evolution of the qubit is modeled as a Markov process, encoding flying qubits onto single photons to handle communication between nodes. 

5 



<!-- Start of picture text -->
Scalable & low runtime<br>Small .--— *~.Large =----...__ overheadTee<br>- — Netsquid,<br>Need fidelity (accuracy) Need full state SimQN, QDNS,<br>simulations representation Squanch<br>Yes IN No PN HPCor ,/ *\ User-defined model or<br>oo \ Yes °° .. No GPU \. application specific<br>QuISP, - - Netsquid,<br>SeQUeNCe QuNetSim,Netsquid SeQUeNCeQuISP, Netsquid,SimQN Squanch<br>Sor Somection ,~ Open-Source & Error Correction” *.. Open-Source &<br>& Fault Tolerance User-Friendly  & Fault Tolerance ~~ *.User-Friendly<br>eQUeNCe eQUeNCe<br><!-- End of picture text -->

A PREPRINT - AUGUST 23, 2024 

### **4.3.1 Use of Quantum Network simulator as part of Hybrid Network simulator (ComNetsEmu)** 

ComNetsEmu [15] is a network simulator that is compatible with the QuNetSim simulator. The ComNetsEmu has been built to support in-network Artificial Intelligence (AI). In recent years, an instance of the quantum network simulator QuNetSim has been merged into the link layer of the classical network emulator ComNetsEmu to create an initial hybrid network simulator [23]. The resulting simulator was used as a way to describe the structure of the full stack of a hybrid quantum-classical network. 

### **4.4 Netsquid** 

Netsquid [60] is a discrete-event-based platform for simulating all aspects of quantum networks. It is widely used across the research community, especially for research in quantum networking and applications. It offers a realistic platform that enables users to collect realistic data on how well their project runs on a quantum network. 

This simulator allows for using large amounts of threads that reduce the runtime linearly with the number of processing cores available. The authors assume that there is sufficient memory available and reiterate that there is a need for a tightly integrated classical control plane with the quantum network. Compared to other simulators, NetSquid also models noise measured during data transfer in the network. 

### **4.5 SimQN** 

SimQN is a discrete-event-based network simulation platform for quantum networks. It is designed to be a functional and easy-to-use tool similar to NS3 for classical networks. It provides researchers with a platform to experiment and simulate quantum networks without needing expensive hardware or waiting for new technology to become available. It aims to address the lack of validation methods for existing quantum network simulations. As explained by Chen _et al._ [63], SimQN provides an average of 8.02 times performance improvement over NetSquid. Another benefit of this simulator is that it provides a modular design that allows for easy customization and extension. This is a benefit since quantum is an evolving field that consistently has new hardware and protocols being developed. As such SimQN enables rapid prototyping and testing of new quantum network protocols and is publicly available [65]. 

### **4.6 QDNS** 

QDNS [61], Quantum Dynamic Network Simulator, is a theoretical framework for simulating the behavior of qubits. Similar to SimQN, QDNS is publically available on [66]. It is a Python-based simulator which makes it user-friendly but reduces the resulting performance of the simulator compared to other simulators. It also provides reusable network protocols and utilities which reduces development time and effort for researchers. 

### **4.7 Cisco’s Qnetlab** 

This is a software development kit created by Cisco Research [64] to simplify the design and execution of simulations for quantum networks. It provides a platform for building and running simulations in the cloud, as well as a protocol builder for designing quantum network protocols. 

### **4.8 Squanch** 

Squanch stands for Simulator for Quantum Networks and CHannels [57]. This is an open-source Python library for simulating quantum networks, focusing on providing tools for developers to design and run simulations, not on building actual quantum networks. 

Squanch is specifically designed for simulating distributed quantum information processing, making it particularly efficient for modeling complex quantum networks that involve multiple nodes and communication channels. By running simulations with different parameters, researchers can fine-tune existing protocols to improve their performance and reliability. Additionally, Squanch can be used to explore the potential of novel network designs and assess their feasibility before committing resources to building them in hardware. Finally, the library leverages the power of multiple processors to run simulations faster, especially for large-scale networks. 

Unlike real-world quantum systems, Squanch simulations are based on models and approximations. These models might not capture all the complexities of real-world systems, leading to potential inaccuracies in the simulation results. This is especially true for simulating large-scale networks or complex noise models. While simulations can provide valuable insights, there’s still a gap between simulated behavior and the actual performance of quantum hardware. Factors like hardware limitations, control errors, and decoherence can significantly affect the practical implementation of protocols 

7 

A PREPRINT - AUGUST 23, 2024 

designed based solely on simulations. Finally, although Squanch utilizes parallelization, simulating extremely large or intricate networks can still become computationally expensive and time-consuming. This can limit its applicability for studying certain types of large-scale quantum systems. 

## **5 Background and Discussions** 

Building and experimenting with quantum networks can be expensive and time-consuming. Simulations allow researchers to test and refine their designs virtually, exploring different architectures, protocols, and parameters to optimize network performance before committing to physical implementations, crucial for developing robust and reliable quantum communication and computing systems. 

### **5.1 Model Quantum Devices** 

Quantum devices are devices that exploit the principles of quantum mechanics to perform computations. Examples include superconducting qubits [67, 68], trapped ion qubits [69], and photonic qubits [70, 71, 72] used in quantum computers. Superconducting qubits are used in superconducting circuits cooled to near absolute zero to encode quantum information. Trapped ion qubits are used individual ions held in place by electromagnetic fields to represent quantum information. Photonic Qubits use photons (particles of light) to encode quantum information. 

### **5.2 Model Quantum Protocols** 

There are various techniques to model quantum protocols including Stochastic Simulation [73, 74, 75] and Tensor Network Methods [76, 77]. Stochastic simulation employs a random sampling approach to simulate the evolution of the quantum state during a protocol. This technique is efficient for analyzing protocols with limited resources. However, it can be statistically noisy such that this approach might not capture the full complexity of the system. Another commonly used approach is the Tensor Network Method, which is a technique that represents the quantum state by decomposing it into a network of tensors. This approach offers an efficient way to model systems with entangled qubits, especially for specific types of entanglement structures. These techniques can become computationally expensive for more general scenarios. 

### **5.3 Model Quantum Repeaters** 

When developing repeaters, it is important to understand that the type of links used would impact the qubit generation technique used by the network. Researchers also need to understand when the resource allocation policy should be triggered and what factors seem to be crucial in the development of a quantum network. 

First, the placement of repeaters has a direct impact on the loss, similar to the placement of the GnB nodes (relay antennas) in a wireless or 5G network. If the relay antennas are too far apart, then the signal may suffer from more interference since it needs to travel farther. In quantum networks, information degrades over distance due to decoherence. This means that the distance between repeaters should be less than the decoherence length of the chosen channel (fiber optic cable, free space, etc). 

Additionally, not all repeaters are built the same way. The quantum memory type and lifetime vary between repeater technologies. This means that some repeaters can transmit signals across a wider distance than others. The entanglement generation and manipulation capabilities and the maintenance also vary between different repeater technologies. A network architect needs to understand the capabilities of each type of repeater used in the network before determining where to place them. This is where simulators can become useful since they give the user the ability to quickly try different repeater technologies. They can then quantify each topology and select the best one for the network’s purpose. 

One approach to model repeaters is using a Heuristic or Analytical model. These algorithms use simplifying assumptions to quickly find possible repeater placements that can satisfy minimum requirements like connectivity and cost. One can expand on this to incorporate detailed channel characteristics, technology specifications, and network topology constraints to optimize placement for factors like fidelity, throughput, and cost. However, while those models can be easy to implement, they struggle when modeling complex systems. To tackle these issues there are simulation tools in which quantum repeater networks can be simulated to evaluate different placement scenarios and their performance under various conditions. 

8 

A PREPRINT - AUGUST 23, 2024 

### **5.4 Complexity of Modeling Quantum Networks** 

Simulating entire quantum networks at the lower levels of individual qubits quickly becomes computationally intractable as the network grows [78]. Abstraction levels allow researchers to focus on the essential features of the network for a specific task [79]. Additionally, abstraction levels provide a framework for designing and developing quantum protocols and algorithms without worrying about the intricate workings of the underlying physical qubits. 

For example, modelling a long-distance quantum network can reveal the error rate (complexity [80, 81]) increases rapidly with distance. Adding a sophisticated error correction protocol or exploring alternative network architectures with built-in redundancy for enhanced resilience can help develop better models. Complexity models can be used to simulate how errors propagate through the network and assess the effectiveness of different error correction protocols. The resulting complexity analysis helps design more robust networks with improved fidelity (accuracy) in transmitting quantum information. 

_Compuational Resources Needed._ Simulating the dynamic behavior of quantum networks, where nodes can be added or removed, and connections can change over time, is also of interest. This includes nodes that become unresponsive because of some fault, allowing quantum network simulators to become more realistic. Understanding how the performance of the network topology changes when a node is unavailable can help researchers understand how their protocol and network topology work in the real world. 

Optimizing the use of quantum resources, such as entanglement generation and distribution, is also a key challenge. At the core of quantum networks, entanglement generation and distribution are used to transmit data from one node to another. Depending on the interaction between qubits and the outside world the resulting qubit value by a node may change and understanding how that change happens would lead simulators to become more realistic tools for researchers. 

_Benchmarking Simulations._ These include entanglement generation success rates [82, 83], fidelity of entanglement [84, 85], entanglement distribution speed [86], or scalability (ex: running millions of agents at the same time with massive data at HPC speed). Other metrics involve the need to integrate with MPI to run on HPC system to increase parallelism and avoid bottlenecks. With these available benchmarks, there is a need to create a tool that can give an overall view of the performance of their network topology and protocols. 

Often, benchmarks have focused on measuring fidelity and the resource usage. Fidelity is a measure of how well the generated entangled states match the ideal entangled states and the benchmarks assess the fidelity of entanglement distribution, and the quality of the generated entangled pairs. Additionally, evaluating the time required to establish entanglement between nodes also helps assess the efficiency of entanglement generation processes. 

## **6 Other Approaches to Qubit Behavior Simulation** 

There are several methods used to simulate qubits such as Stochastic Wavefunction [87], Tensor Network [88], and Monte-Carlo [89]. Stochastic wavefunction methods, like the Quantum Trajectory Approach, involve random sampling of quantum trajectories to approximate the evolution of a quantum system. These methods can be more computationally efficient than exact simulations for certain scenarios. Tensor network methods, including the Matrix Product State [90] (MPS) and the Tensor Network State [91] (TNS) representations, are used for simulating the state of a quantum system. These methods offer a more efficient representation of quantum states, especially for systems with entanglement. And, Monte-Carlo methods are employed in quantum Monte-Carlo simulations to estimate physical quantities related to quantum systems. Variational Monte-Carlo and Diffusion Monte-Carlo are examples of techniques used for qubit simulations. Since currently there is still development happening on different generation methods for qubits, quantum network simulators should at least offer all three approaches so that researchers can explore the effect of all three methods on their new protocol. 

### **6.1 Understanding Qubit behavior** 

In this section, we focus on developing an analytical model that can be used to model the evolution of the density matrix of a quantum system, such as a qubit, going through a quantum communication channel. We start with qubit transmission since it is the base usage of networks and qubits are quantum systems that carry the quantum information from one node to another in a quantum network. A single qubit state can be expressed by using the Dirac notation [92, 93]. An example representation of a qubit is represented in Equation 1. 

_|_ Ψ _⟩_ = _α |_ 0 _⟩_ + _β |_ 1 _⟩_ 

(1) 

9 

A PREPRINT - AUGUST 23, 2024 

Researchers have used the the Bloch equation [94, 95, 96], as described in Equation 2, to model qubit behavior. This equation describes the evolution of the Bloch vector, which is a three-dimensional vector that represents the state of a qubit. It uses differential equations that takes into account the Hamiltonian of the qubit system, which is the operator that describes the energy of the system, which includes 2 or more qubits. It can also be used to describe other aspects linked to qubit behaviors such as precession and relaxation. Precession is the rotation of the qubit state around the Bloch sphere at a frequency that is proportional to the qubit transition frequencies. Relaxation is the decay of the qubit state to its equilibrium value over time due to interactions with the environment. 



_Mx, My,_ and _Mz_ are the components of the Bloch vector on the Bloch sphere. _ω_ x, _ω_ y, and _ω_ z are the frequencies of the qubit transitions in the _x, y,_ and _z_ directions, respectively. M0 is the equilibrium magnetization, which is typically zero for qubits. T1 is the longitudinal relaxation time constant, which is the time it takes for the longitudinal magnetization to relax back to its equilibrium value after it has been perturbed. 

Overall, Bloch equations have been used to model qubit behaviors on quantum communication channels [97, 98, 99]. However, they are not a fully accurate representation of qubit dynamics [100, 101]. This is due to their classical nature, limited scope to two-level systems [102, 103], and lack of consideration for other quantum aspects such as decoherence [104]. For more accurate modeling, more sophisticated techniques such as the master equation are typically used. Therefore, the master equation can be used to determine the evolution of the density matrix of a quantum system. 

The master equation for a qubit in a quantum communication channel is given by Equation 3, where _ρ_ is the density matrix of the qubit, L is the Hamiltonian of the qubit system, Γ is the decoherence rate, and _ρeq_ is the equilibrium density matrix of the qubit. By using this equation, we can directly model the impact of different types of channel parameters on the resulting density matrix of the qubit. Γ and L can be used to experiment with different rates of noise on a quantum system. 



The decoherence rate value Γ depends on the type of noise that the qubit is subject to and the properties of the environment. The decoherence rate can be calculated from the longitudinal relaxation time constant (T1) and the transverse relaxation time constant (T2), as described by Equation 4. By looking at this equation and the Bloch equation we can see that the Bloch equation is missing the decoherence value when calculating the updated state of the qubit. 



The Hamiltonian is written as a formula showing the interaction between the energy of 2 qubits described as _L_ = _L_ 0 + _Lint_ . _L_ 0 is the free Hamiltonian, which describes the energy of the qubits in the absence of any interactions. On the other hand, _Lint_ is the interaction Hamiltonian, which describes the energy of the interactions between the qubits. Both _L_ 0 and _Lint_ are described in Equation 5. 



In the equation, the variables include different components of qubits. ∆ _ω_ is the qubit transition frequency. _σz_ is the Pauli Z operator [105, 106]. J is the coupling constant between the qubits [107, 108]. There exist multiple models that can be used to determine the J coupling value, such as Ising Model or XY Model. It depends on the type of interaction that is being modeled. For example, the XY model seems to depend heavily on the temperature of the system while the Ising model the intrinsic dimension is independent of the real-space topology [109]. Therefore, an interface that uses the equation set needs to have the ability to swap the coupling constant depending on the need of the user and the experiment. Finally, _σi_ and _σj_ are the Pauli operators for the ith and jth qubits, respectively. The Pauli operators are three operators: the X, Y and Z operators. The Pauli operators [110] are denoted using the formulas described in equation 6. Because, even the smallest components of these equations can be written as vector math, using the existing literature, we can build a model that can be used by other researchers to validate new development in quantum network simulators. 

10 

A PREPRINT - AUGUST 23, 2024 



Now that the behavior of a qubit is shown using vector math, it is important to acknowledge that such an approach does not scale well. The number of variables and equations involved in analytical models grows exponentially with the number of qubits or network components. This can quickly render them impractical for simulating realistic quantum networks. This means that validating a simulation of a full network may need other validation techniques such as using Monte-Carlo simulations, which enable us to run the simulation repeatedly under different conditions. Because of the scaling problem, translating analytical models into efficient and accurate simulation code can also be a complex task, which can lead to the potential introduction of errors or numerical instabilities. 

Additionally, assumptions taken by the developers of the analytical models play a crucial part in the outcome of the validation. Verifying these assumptions in real-world quantum networks can be challenging, leading to uncertainties in the model’s accuracy. Additionally, analytical models often make simplifying assumptions, such as perfect qubits, noiseless operations, and ideal channels. These assumptions may not accurately reflect the behavior of real-world quantum networks, which are inherently susceptible to noise, imperfections, and environmental influences. As a result, analytical models may fail to capture the full complexity and nuances of physical quantum systems, potentially leading to inaccurate or misleading simulation results. 

### **6.2 Analytical Benchmarking** 

Dealing with multiple dimensional vector data, a first approach for validation is Euclidean distance [111]. This metric lets users visualize how closely the simulated qubit density matrix matches the expected one. A small distance indicates that the simulated channel behaves as expected in a real quantum network running the same workload. 

However, for a deeper understanding of the discrepancies between the two density matrices, the Earth Mover’s algorithm, can be used for comparing 2D data, needed to transform one distribution into the other. By combining Euclidean distance and the Earth Mover’s value, users can gain a comprehensive picture of how well the simulation replicates reality. A small distance and a low ‘dirt’ value would strongly validate the resulting qubit value. 

Besides Euclidean distance and Earth Mover’s distance, there are several other comparison metrics for 3D vector data. These comparison metrics include distance-based metrics, distribution-based metrics, and directional metrics. We want to use a combination of all three types of metrics to validate the simulated qubit behavior. Similar to Euclidean, the Manhattan distance allows distance metric calculated over the sum of absolute differences instead of squares, emphasizing outliers. Outliers are important to identifying any isolated discrepancies in the simulated results. Using the Root Mean Square Distance between the simulated qubit density metric and the theoretical density metric, it records the impact of larger errors. 

Another benchmark is to understand how the simulation modeled the distribution of the density matrix. The KullbackLeibler divergence [112] (KL divergence) measures how much information is lost when describing one distribution with another. Jensen-Shannon divergence [113], is another distribution-based metric, similar to KL divergence but symmetric based, useful for comparing two distributions simultaneously. This metric allows users to evaluate how well the simulation models the interactions between 2 qubits. Also one can combine the result of Jensen-Shannon divergence with Bhattacharya distance [114, 115] to see how much overlap the simulated matrix has with the resulting theoretical matrix. The Bhattacharya distance measures the overlap between two probability distributions. 

Finally, comparing the direction of both the simulated density matrix and the resulting density matrix one can compare the angle between both vectors. This measures the rotation needed to align one vector with the other. The ‘size’ of the rotation needs to align one set of vectors with the other, we can use the Rotation Matrix Frobenius norm. 

## **7 Conclusion and Future Directions of Research** 

This survey identifies a need for a standardized platform to validate existing quantum simulators. By using existing theoretical work for a validation interface, one can generate values of the density matrix that would be expected 

11 

A PREPRINT - AUGUST 23, 2024 

depending on certain network conditions. Developing a user-friendly interface that can be used by the research community, can help users validate the result of simulators. 

Further, this can also be used to study the interaction between classical and quantum networks. Because qubits carry data in quantum networks it is important to understand how the interactions impact the qubit values. The validation interface should evolve to include the validation techniques for the behavior of hybrid networks expected in the real world. 

We also discussed using analytical models such as modeling a qubit behavior, quantum bnchmarking, or classical shadow optimization to verify quantum network simulators. For quantum benchmarking, we propose to build a library of benchmarking workloads and protocols that can be used to probe the capabilities and limitations of quantum devices and simulators. These benchmarks, like Bell state preparation and tomography, provide a reference point for evaluating the accuracy and fidelity of simulations. For the case of classical shadow optimization, we can use a classical optimization algorithm that mimics the behavior of a quantum algorithm. This algorithm can then provide a classical approximation of the quantum simulation results. Comparing the two sets of results can highlight potential errors or limitations in the simulator. 

Further explorations of formal verification testing and code review can be performed, with sensitivity analysis, to include noise injection and statistical analysis to understand how the simulation is performing. Simulating the effects of different types of noise, such as decoherence and state preparation errors, is crucial for assessing the robustness and accuracy of quantum network simulations. It can help researchers identify sensitive areas and potential sources of error in the simulation. Additionally, performing a parameter sweep by systematically varying key parameters of the quantum network, such as coupling strengths or interaction times, allows researchers to study the behavior of the simulated system across a wider range of conditions. This can reveal unexpected dependencies or edge cases that require further validation. 

Finally, using existing validation techniques such as Monte-Carlo simulations can help reveal inconsistencies in the outcome of the simulation. Running the simulation multiple times with different initial conditions or random noise variations helps to quantify the statistical uncertainty and variability of the results. This provides a more complete picture of the simulated system’s behavior and avoids concluding single realizations. Additionally, statistical tests can be used to formally compare the simulated outcomes with a particular hypothesis or reference data. This allows for a rigorous assessment of the validity and significance of the simulation results. 

## **8 Acknowledgements** 

During the preparation of this work the author(s) used Google Bard in order to improve grammar and flow of the text in the paper, and to supplement background research. After using this tool, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication. This work was supported by the U.S. DOE Office of Science, Office of Advanced Scientific Computing Research, under award 66150: “CENATE - Center for Advanced Architecture Evaluation” project and the DOE ASCR Early Career Grant “Large Scale Deep Learning for Intelligent Networks” award ERKJ435 hosted at Oak Ridge National Laboratory. The Pacific Northwest National Laboratory is operated by Battelle for the U.S. Department of Energy under contract DE-AC05-76RL01830. 

This manuscript has been authored by UT-Battelle, LLC, under contract DE-AC05-00OR22725 with the US Department of Energy (DOE). The US government retains and the publisher, by accepting the article for publication, acknowledges that the US government retains a nonexclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript, or allow others to do so, for US government purposes. DOE will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan (https://www.energy.gov/downloads/doe-public-access-plan). 

## **References** 

- [1] Giulio Chiribella, Giacomo Mauro D’Ariano, and Paolo Perinotti. Theoretical framework for quantum networks. _Physical Review A_ , 80(2):022339, 2009. 

- [2] Shi-Hai Wei, Bo Jing, Xue-Ying Zhang, Jin-Yu Liao, Chen-Zhi Yuan, Bo-Yu Fan, Chen Lyu, Dian-Li Zhou, You Wang, Guang-Wei Deng, et al. Towards real-world quantum networks: a review. _Laser & Photonics Reviews_ , 16(3):2100219, 2022. 

- [3] Wojciech Kozlowski and Stephanie Wehner. Towards large-scale quantum networks. In _Proceedings of the sixth annual ACM international conference on nanoscale computing and communication_ , pages 1–7, 2019. 

12 

A PREPRINT - AUGUST 23, 2024 

- [4] Nicholas A. Peters, Muneer Alshowkan, Joseph C. Chapman, Raphael C. Pooser, Nageswara S. V. Rao, and Raymond T. Newell. Long-term cybersecurity applications enabled by quantum networks, 4 2023. 

- [5] B. J. Lawrie, P. D. Lett, A. M. Marino, and R. C. Pooser. Quantum sensing with squeezed light. _ACS Photonics_ , 6(6):1307–1318, 2019. 

- [6] Samuel L Braunstein. Quantum error correction for communication with linear optics. _Nature_ , 394(6688):47–49, 1998. 

- [7] Jasminder S Sidhu, Siddarth K Joshi, Mustafa Gündo˘gan, Thomas Brougham, David Lowndes, Luca Mazzarella, Markus Krutzik, Sonali Mohapatra, Daniele Dequal, Giuseppe Vallone, et al. Advances in space quantum communications. _IET Quantum Communication_ , 2(4):182–217, 2021. 

- [8] Sreraman Muralidharan, Linshu Li, Jungsang Kim, Norbert Lütkenhaus, Mikhail D Lukin, and Liang Jiang. Optimal architectures for long distance quantum communication. _Scientific reports_ , 6(1):20463, 2016. 

- [9] Muneer Alshowkan, Nageswara S. V. Rao, Joseph C. Chapman, Brian P. Williams, Philip G. Evans, Raphael C. Pooser, Joseph M. Lukens, and Nicholas A. Peters. Lessons Learned on the Interface between Quantum and Conventional Networking, 11 2021. 

- [10] Nageswara S. V. Rao, Muneer Alshowkan, Joseph C. Chapman, Nicholas A. Peters, and Joseph M. Lukens. Throughput Measurements and Capacity Estimates for Quantum Connections, 5 2023. 

- [11] Koji Azuma, Sophia E Economou, David Elkouss, Paul Hilaire, Liang Jiang, Hoi-Kwong Lo, and Ilan Tzitrin. Quantum repeaters: From quantum networks to the quantum internet. _Reviews of Modern Physics_ , 95(4):045006, 2023. 

- [12] Amoldeep Singh, Kapal Dev, Harun Siljak, Hem Dutt Joshi, and Maurizio Magarini. Quantum internet—applications, functionalities, enabling technologies, challenges, and research directions. _IEEE Communications Surveys & Tutorials_ , 23(4):2218–2247, 2021. 

- [13] Benjamin Desef and Martin B Plenio. Protecting quantum states against loss. _Quantum_ , 2021:05–26, 2021. 

- [14] Stephen DiAdamo, Janis Nötzel, Benjamin Zanger, and Mehmet Mert Be¸se. Qunetsim: A software framework for quantum networks. _IEEE Transactions on Quantum Engineering_ , 2:1–12, 2021. 

- [15] Frank HP Fitzek, Fabrizio Granelli, and Patrick Seeling. _Computing in Communication Networks: From Theory to Practice_ . Academic Press, 2020. 

- [16] Michele Amoretti, Mattia Pizzoni, and Stefano Carretta. Enhancing distributed functional monitoring with quantum protocols. _Quantum Information Processing_ , 18(12):371, 2019. 

- [17] Nageswara S Rao and Travis S Humble. Control plane and virtualized development environment for softwarized quantum networks. Technical report, Oak Ridge National Lab.(ORNL), Oak Ridge, TN (United States), 2018. 

- [18] Uman Khalid, Junaid ur Rehman, Saw Nang Paing, Haejoon Jung, Trung Q Duong, and Hyundong Shin. Quantum network engineering in the nisq age: Principles, missions, and challenges. _IEEE Network_ , 2023. 

- [19] Venkat R Dasari, Ronald J Sadlier, Ryan Prout, Brian P Williams, and Travis S Humble. Programmable multinode quantum network design and simulation. In _Quantum Information and Computation IX_ , volume 9873, pages 56–64. SPIE, 2016. 

- [20] Takaaki Matsuo. Simulation of a dynamic, ruleset-based quantum network. _arXiv preprint arXiv:1908.10758_ , 2019. 

- [21] Raphael Fortes and Gustavo Rigolin. Fighting noise with noise in realistic quantum teleportation. _Physical Review A_ , 92(1):012338, 2015. 

- [22] Ieva Cepait<sup>ˇ</sup> e.˙ Simulation of networked quantum computing on encrypted data. _arXiv preprint arXiv:2212.12953_ , 2022. 

- [23] Stephen DiAdamo, Janis Nötzel, Simon Sekavˇcnik, Riccardo Bassoli, Roberto Ferrara, Christian Deppe, Frank HP Fitzek, and Holger Boche. Integrating quantum simulation for quantum-enhanced classical network emulation. _IEEE Communications Letters_ , 25(12):3922–3926, 2021. 

- [24] Benjamin Weder, Johanna Barzen, Frank Leymann, and Michael Zimmermann. Hybrid quantum applications need two orchestrations in superposition: a software architecture perspective. In _2021 IEEE International Conference on Web Services (ICWS)_ , pages 1–13. IEEE, 2021. 

- [25] Jacob Biamonte, Peter Wittek, Nicola Pancotti, Patrick Rebentrost, Nathan Wiebe, and Seth Lloyd. Quantum machine learning. _Nature_ , 549(7671):195–202, 2017. 

- [26] Yao Zhang and Qiang Ni. Recent advances in quantum machine learning. _Quantum Engineering_ , 2(1):e34, 2020. 

13 

A PREPRINT - AUGUST 23, 2024 

- [27] Carlo Ciliberto, Mark Herbster, Alessandro Davide Ialongo, Massimiliano Pontil, Andrea Rocchetto, Simone Severini, and Leonard Wossnig. Quantum machine learning: a classical perspective. _Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences_ , 474(2209):20170551, 2018. 

- [28] Maria Schuld and Nathan Killoran. Quantum machine learning in feature hilbert spaces. _Physical review letters_ , 122(4):040504, 2019. 

- [29] Harpreet Singh and Abha Sachdev. The quantum way of cloud computing. In _2014 International Conference on Reliability Optimization and Information Technology (ICROIT)_ , pages 397–400. Ieee, 2014. 

- [30] Davide Castelvecchi. Ibm’s quantum cloud computer goes commercial. _Nature_ , 543(7644), 2017. 

- [31] Johnny Hooyberghs and Johnny Hooyberghs. Azure quantum. _Introducing Microsoft Quantum Computing for Developers: Using the Quantum Development Kit and Q#_ , pages 307–339, 2022. 

- [32] Mustafa Kaiiali, Sakir Sezer, and Ayesha Khalid. Cloud computing in the quantum era. In _2019 IEEE Conference on Communications and Network Security (CNS)_ , pages 1–4. IEEE, 2019. 

- [33] Hai Luong et al. Towards cloud agnostic quantum-classical hybrid computing, 2023. 

- [34] Emil T Khabiboulline, Johannes Borregaard, Kristiaan De Greve, and Mikhail D Lukin. Optical interferometry with quantum networks. _Physical review letters_ , 123(7):070504, 2019. 

- [35] Ying Yu, Shunfa Liu, Chang-Min Lee, Peter Michler, Stephan Reitzenstein, Kartik Srinivasan, Edo Waks, and Jin Liu. Telecom-band quantum dot technologies for long-distance quantum networks. _Nature Nanotechnology_ , 18(12):1389–1400, 2023. 

- [36] Valerio Scarani, Helle Bechmann-Pasquinucci, Nicolas J Cerf, Miloslav Dušek, Norbert Lütkenhaus, and Momtchil Peev. The security of practical quantum key distribution. _Reviews of modern physics_ , 81(3):1301, 2009. 

- [37] David P Nadlinger, Peter Drmota, Bethan C Nichol, Gabriel Araneda, Dougal Main, Raghavendra Srinivas, David M Lucas, Christopher J Ballance, Kirill Ivanov, EY-Z Tan, et al. Experimental quantum key distribution certified by bell’s theorem. _Nature_ , 607(7920):682–686, 2022. 

- [38] Yichen Zhang, Yiming Bian, Zhengyu Li, Song Yu, and Hong Guo. Continuous-variable quantum key distribution system: Past, present, and future. _Applied Physics Reviews_ , 11(1), 2024. 

- [39] Marcus Cramer, Martin B Plenio, Steven T Flammia, Rolando Somma, David Gross, Stephen D Bartlett, Olivier Landon-Cardinal, David Poulin, and Yi-Kai Liu. Efficient quantum state tomography. _Nature communications_ , 1(1):149, 2010. 

- [40] Masoud Mohseni, Ali T Rezakhani, and Daniel A Lidar. Quantum-process tomography: Resource analysis of different strategies. _Physical Review A_ , 77(3):032322, 2008. 

- [41] Tao Zheng, Shibin Zhang, Xiang Gao, and Yan Chang. Practical quantum private query based on bell state. _Modern Physics Letters A_ , 34(24):1950196, 2019. 

- [42] CF Roos, GPT Lancaster, M Riebe, H Häffner, W Hänsel, S Gulde, C Becher, J Eschner, F Schmidt-Kaler, and R Blatt. Bell states of atoms with ultralong lifetimes and their tomographic state analysis. _Physical review letters_ , 92(22):220402, 2004. 

- [43] David Soler, Iván Cillero, Carlos Dafonte, Manuel Fernández-Veiga, Ana Fernández Vilas, and Francisco J Nóvoa. Qkdnetsim+: Improvement of the quantum network simulator for ns-3. _SoftwareX_ , 26:101685, 2024. 

- [44] Christopher Spiess, Sebastian Töpfer, Sakshi Sharma, Andrej Kržiˇc, Meritxell Cabrejo-Ponce, Uday Chandrashekara, Nico Lennart Döll, Daniel Rieländer, and Fabian Steinlechner. Clock synchronization with correlated photons. _Physical Review Applied_ , 19(5):054082, 2023. 

- [45] Stav Haldar, Ivan Agullo, and James E Troupe. Synchronizing clocks via satellites using entangled photons: Effect of relative velocity on precision. _Physical Review A_ , 108(6):062613, 2023. 

- [46] Swaraj Shekhar Nande, Osel Lhamo, Marius Paul, Riccardo Bassoli, and Frank HP Fitzek. Quantum time synchronization for satellite networks. In _2023 IEEE Aerospace Conference_ , pages 1–9. IEEE, 2023. 

- [47] Kathleen R Mullin, Daniel W Laorenza, Danna E Freedman, and James M Rondinelli. Quantum sensing of magnetic fields with molecular color centers. _Physical Review Research_ , 5(4):L042023, 2023. 

- [48] Bo Bao, Yu Hua, Ridong Wang, and Dachao Li. Quantum-based magnetic field sensors for biosensing. _Advanced Quantum Technologies_ , 6(5):2200146, 2023. 

- [49] Xiai Wang. Quantum-enhanced mri sensitivity: Dissolution-dynamic nuclear and parahydrogen-induced polarization. _Highlights in Science, Engineering and Technology_ , 38:423–430, 2023. 

14 

A PREPRINT - AUGUST 23, 2024 

- [50] Reyazur Rashid Irshad, Shahid Hussain, Ihtisham Hussain, Jamal Abdul Nasir, Asim Zeb, Khaled M Alalayah, Ahmed Abdu Alattab, Adil Yousif, and Ibrahim M Alwayle. Iot-enabled secure and scalable cloud architecture for multi-user systems: A hybrid post-quantum cryptographic and blockchain based approach towards a trustworthy cloud computing. _IEEE Access_ , 2023. 

- [51] K Sundar, S Sasikumar, C Jayakumar, D Nagarajan, and S Karthick. Quantum cryptography based cloud security model (qc-csm) for ensuring cloud data security in storage and accessing. _Multimedia Tools and Applications_ , 82(27):42817–42832, 2023. 

- [52] Gautam Kumar, Sahil Yadav, Aniruddha Mukherjee, Vikas Hassija, and Mohsen Guizani. Recent advances in quantum computing for drug discovery and development. _IEEE Access_ , 2024. 

- [53] Srikanth Pulipeti and Adarsh Kumar. Secure quantum computing for healthcare sector: A short analysis. _Security and Privacy_ , 6(5):e293, 2023. 

- [54] Andras Varga. Omnet++. In _Modeling and tools for network simulation_ , pages 35–59. Springer, 2010. 

- [55] Tamie L Veith, John E Kobza, and C Patrick Koelling. Netsim: Java™-based simulation for the world wide web. _Computers & operations research_ , 26(6):607–621, 1999. 

- [56] Gustavo Carneiro. Ns-3: Network simulator 3. In _UTM lab meeting April_ , volume 20, pages 4–5, 2010. 

- [57] Ben Bartlett. A distributed simulation framework for quantum networks and channels. _arXiv preprint arXiv:1808.07047_ , 2018. 

- [58] Xiaoliang Wu, Alexander Kolar, Joaquin Chung, Dong Jin, Tian Zhong, Rajkumar Kettimuthu, and Martin Suchara. Sequence: a customizable discrete-event simulator of quantum networks. _Quantum Science and Technology_ , 6(4):045027, 2021. 

- [59] R Kettimuthu. Sequence simulator of quantum network communication, 2019. 

- [60] Tim Coopmans, Robert Knegjens, Axel Dahlberg, David Maier, Loek Nijsten, Julio de Oliveira Filho, Martijn Papendrecht, Julian Rabbie, Filip Rozpedek, Matthew Skrzypczyk, et al. Netsquid, a network simulator for quantum information using discrete events. _Communications Physics_ , 4(1):164, 2021. 

- [61] Osman Semi Ceylan and Ihsan Yilmaz. Qdns: Quantum dynamic network simulator based on event driving. In _2021 International Conference on Information Security and Cryptology (ISCTURKEY)_ , pages 45–50. IEEE, 2021. 

- [62] Ryosuke Satoh, Michal Hajdušek, Naphan Benchasattabuse, Shota Nagayama, Kentaro Teramoto, Takaaki Matsuo, Sara Ayman Metwalli, Poramet Pathumsoot, Takahiko Satoh, Shigeya Suzuki, et al. Quisp: a quantum internet simulation package. In _2022 IEEE International Conference on Quantum Computing and Engineering (QCE)_ , pages 353–364. IEEE, 2022. 

- [63] Lutong Chen, Kaiping Xue, Jian Li, Nenghai Yu, Ruidong Li, Qibin Sun, and Jun Lu. Simqn: A network-layer simulator for the quantum network investigation. _IEEE Network_ , 2023. 

- [64] Stephen DiAdamo. The quantum network development kit. `https://www.ciscolive.com/c/dam/r/ ciscolive/emea/docs/2024/pdf/BRKETI-2445.pdf` , 2024. 

- [65] Lutong Chen, Jian Li, Kaiping Xue, Nenghai Yu, Ruidong Li, Qibin Sun, and Jun Lu. Simqn. `https: //github.com/ertuil/SimQN` , 2022. 

- [66] Osman Semi Ceylan and Ihsan Yilmaz. Qdns. `https://github.com/OsmanCeylan/QDNS` , 2021. 

- [67] Michel H Devoret, Andreas Wallraff, and John M Martinis. Superconducting qubits: A short review. _arXiv preprint cond-mat/0411174_ , 2004. 

- [68] Morten Kjaergaard, Mollie E Schwartz, Jochen Braumüller, Philip Krantz, Joel I-J Wang, Simon Gustavsson, and William D Oliver. Superconducting qubits: Current state of play. _Annual Review of Condensed Matter Physics_ , 11:369–395, 2020. 

- [69] Colin D Bruzewicz, John Chiaverini, Robert McConnell, and Jeremy M Sage. Trapped-ion quantum computing: Progress and challenges. _Applied Physics Reviews_ , 6(2), 2019. 

- [70] Jeremy L O’brien, Akira Furusawa, and Jelena Vuˇckovi´c. Photonic quantum technologies. _Nature Photonics_ , 3(12):687–695, 2009. 

- [71] Peter BR Nisbet-Jones, Jerome Dilley, Annemarie Holleczek, Oliver Barter, and Axel Kuhn. Photonic qubits, qutrits and ququads accurately prepared and delivered on demand. _New Journal of Physics_ , 15(5):053007, 2013. 

- [72] Duan-Cheng Liu, Pei-Yun Li, Tian-Xiang Zhu, Liang Zheng, Jian-Yin Huang, Zong-Quan Zhou, Chuan-Feng Li, and Guang-Can Guo. On-demand storage of photonic qubits at telecom wavelengths. _Physical Review Letters_ , 129(21):210501, 2022. 

15 

A PREPRINT - AUGUST 23, 2024 

- [73] Bruno Apolloni, C Carvalho, and Diego De Falco. Quantum stochastic optimization. _Stochastic Processes and their Applications_ , 33(2):233–244, 1989. 

- [74] Chengran Yang, Felix C Binder, Varun Narasimhachar, and Mile Gu. Matrix product states for quantum stochastic modeling. _Physical Review Letters_ , 121(26):260602, 2018. 

- [75] Kang-Da Wu, Chengran Yang, Ren-Dong He, Mile Gu, Guo-Yong Xiang, Chuan-Feng Li, Guang-Can Guo, and Thomas J Elliott. Implementing quantum dimensionality reduction for non-markovian stochastic simulation. _Nature Communications_ , 14(1):2624, 2023. 

- [76] Junxiang Huang, Wenhao He, Yukun Zhang, Yusen Wu, Bujiao Wu, and Xiao Yuan. Tensor-network-assisted variational quantum algorithm. _Physical Review A_ , 108(5):052407, 2023. 

- [77] Mari Carmen Bañuls. Tensor network algorithms: A route map. _Annual Review of Condensed Matter Physics_ , 14:173–191, 2023. 

- [78] Feng Pan and Pan Zhang. Simulation of quantum circuits using the big-batch tensor network method. _Physical Review Letters_ , 128(3):030501, 2022. 

- [79] Stephanie Wehner, David Elkouss, and Ronald Hanson. Quantum internet: A vision for the road ahead. _Science_ , 362(6412):eaam9288, 2018. 

- [80] Michael Siomau. Structural complexity of quantum networks. In _AIP Conference Proceedings_ , volume 1742. AIP Publishing, 2016. 

- [81] Masahito Hayashi, Kazuo Iwama, Harumichi Nishimura, Rudy Raymond, and Shigeru Yamashita. Quantum network coding. In _Annual Symposium on Theoretical Aspects of Computer Science_ , pages 610–621. Springer, 2007. 

- [82] Scott E Vinay and Pieter Kok. Statistical analysis of quantum-entangled-network generation. _Physical Review A_ , 99(4):042313, 2019. 

- [83] Ashlesha Patil, Mihir Pant, Dirk Englund, Don Towsley, and Saikat Guha. Entanglement generation in a quantum network at distance-independent rate. _npj Quantum Information_ , 8(1):51, 2022. 

- [84] Jian Li, Mingjun Wang, Kaiping Xue, Ruidong Li, Nenghai Yu, Qibin Sun, and Jun Lu. Fidelity-guaranteed entanglement routing in quantum networks. _IEEE Transactions on Communications_ , 70(10):6748–6763, 2022. 

- [85] Otfried Gühne, Yuanyuan Mao, and Xiao-Dong Yu. Geometry of faithful entanglement. _Physical Review Letters_ , 126(14):140503, 2021. 

- [86] Takuya Ikuta and Hiroki Takesue. Four-dimensional entanglement distribution over 100 km. _Scientific reports_ , 8(1):817, 2018. 

- [87] Heinz-Peter Breuer, Bernd Kappler, and Francesco Petruccione. Stochastic wave-function method for nonmarkovian quantum master equations. _Physical Review A_ , 59(2):1633, 1999. 

- [88] Simone Montangero, Evenson Montangero, and Evenson. _Introduction to tensor network methods_ . Springer, 2018. 

- [89] John Hammersley. _Monte carlo methods_ . Springer Science & Business Media, 2013. 

- [90] David Perez-Garcia, Frank Verstraete, Michael M Wolf, and J Ignacio Cirac. Matrix product state representations. _arXiv preprint quant-ph/0608197_ , 2006. 

- [91] Glen Evenbly and Guifré Vidal. Tensor network states and geometry. _Journal of Statistical Physics_ , 145:891–918, 2011. 

- [92] Roderich Tumulka. Dirac notation. In _Compendium of Quantum Physics_ , pages 172–174. Springer, 2009. 

- [93] Jack D Hidary and Jack D Hidary. Dirac notation. _Quantum Computing: An Applied Approach_ , pages 377–381, 2021. 

- [94] Matheus Moraes Hammes and Antonio Robles-Kelly. On the behaviour of pulsed qubits and their application to feed forward networks. _arXiv preprint arXiv:2302.10467_ , 2023. 

- [95] Chu-Ryang Wie. Two-qubit bloch sphere. _Physics_ , 2(3):383–396, 2020. 

- [96] Rusko Ruskov and Alexander N Korotkov. Spectrum of qubit oscillations from generalized bloch equations. _Physical Review B_ , 67(7):075303, 2003. 

- [97] Nicolai Lang and Hans Peter Büchler. Topological networks for quantum communication between distant qubits. _npj Quantum Information_ , 3(1):47, 2017. 

16 

A PREPRINT - AUGUST 23, 2024 

- [98] Angela Sara Cacciapuoti, Marcello Caleffi, Rodney Van Meter, and Lajos Hanzo. When entanglement meets classical communications: Quantum teleportation for the quantum internet. _IEEE Transactions on Communications_ , 68(6):3808–3833, 2020. 

- [99] Masashi Ban, Sachiko Kitajima, and Fumiaki Shibata. Decoherence of entanglement in the bloch channel. _Journal of Physics A: Mathematical and General_ , 38(19):4235, 2005. 

- [100] Xin-Qi Li, Wen-Kai Zhang, Ping Cui, Jiushu Shao, Zhongshui Ma, and YiJing Yan. Quantum measurement of a solid-state qubit: A unified quantum master equation approach. _Physical Review B_ , 69(8):085315, 2004. 

- [101] Auro M Perego, Bruno Garbin, François Gustave, Stephane Barland, Franco Prati, and Germán J De Valcárcel. Coherent master equation for laser modelocking. _Nature communications_ , 11(1):311, 2020. 

- [102] Thomas E Skinner, Timo O Reiss, Burkhard Luy, Navin Khaneja, and Steffen J Glaser. Application of optimal control theory to the design of broadband excitation pulses for high-resolution nmr. _Journal of Magnetic Resonance_ , 163(1):8–15, 2003. 

- [103] Jr-Shin Li, Justin Ruths, and Steffen J Glaser. Exact broadband excitation of two-level systems by mapping spins to springs. _Nature communications_ , 8(1):446, 2017. 

- [104] Maximilian Schlosshauer. Quantum decoherence. _Physics Reports_ , 831:1–57, 2019. 

- [105] Kanav Setia, Richard Chen, Julia E Rice, Antonio Mezzacapo, Marco Pistoia, and James D Whitfield. Reducing qubit requirements for quantum simulations using molecular point group symmetries. _Journal of Chemical Theory and Computation_ , 16(10):6091–6097, 2020. 

- [106] Mohsen Heidari and Wojciech Szpankowski. Learning k-qubit quantum operators via pauli decomposition. In _International Conference on Artificial Intelligence and Statistics_ , pages 490–504. PMLR, 2023. 

- [107] Cheng-Zhi Wang, Chun-Xian Li, Liu-Ying Nie, and Jiang-Fan Li. Classical correlation and quantum discord mediated by cavity in two coupled qubits. _Journal of Physics B: Atomic, Molecular and Optical Physics_ , 44(1):015503, 2010. 

- [108] Lucjan Piela. _Ideas of quantum chemistry_ . Elsevier, 2013. 

- [109] Vittorio Vitale, Tiago Mendes-Santos, Alex Rodriguez, and Marcello Dalmonte. Topological kolmogorov complexity and the berezinskii-kosterlitz-thouless mechanism. _arXiv preprint arXiv:2305.05396_ , 2023. 

- [110] Ivan B Djordjevic. _Quantum information processing, quantum computing, and quantum error correction: an engineering approach_ . Academic Press, 2021. 

- [111] Nathan Krislock and Henry Wolkowicz. _Euclidean distance matrices and applications_ . Springer, 2012. 

- [112] Solomon Kullback. Kullback-leibler divergence, 1951. 

- [113] ML Menéndez, JA Pardo, L Pardo, and MC Pardo. The jensen-shannon divergence. _Journal of the Franklin Institute_ , 334(2):307–318, 1997. 

- [114] Thomas Kailath. The divergence and bhattacharyya distance measures in signal selection. _IEEE transactions on communication technology_ , 15(1):52–60, 1967. 

- [115] Euisun Choi and Chulhee Lee. Feature extraction based on the bhattacharyya distance. _Pattern Recognition_ , 36(8):1703–1709, 2003. 

17 

