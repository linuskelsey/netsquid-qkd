# **NetSquid, a NETwork Simulator for QUantum Information using Discrete events** 

Tim Coopmans,<sup>1, 2,</sup><sup>_∗_</sup> Robert Knegjens,<sup>1,</sup><sup>_∗_</sup> Axel Dahlberg,<sup>1, 2</sup> David Maier,<sup>1, 2</sup> Loek Nijsten,<sup>1</sup> Julio de Oliveira Filho,<sup>1</sup> Martijn Papendrecht,<sup>1</sup> Julian Rabbie,<sup>1, 2</sup> Filip Rozpędek,<sup>1, 2, 3</sup> Matthew Skrzypczyk,<sup>1, 2</sup> Leon Wubben,<sup>1</sup> Walter de Jong,<sup>4</sup> Damian Podareanu,<sup>4</sup> Ariana Torres-Knoop,<sup>4</sup> David Elkouss,<sup>1,</sup><sup>_†_</sup> and Stephanie Wehner<sup>1, 2, 5,</sup><sup>_†_</sup> 

> 1 _QuTech, Delft University of Technology and TNO, Lorentzweg 1, 2628 CJ Delft, The Netherlands_ 

> 2 _Kavli Institute of Nanoscience, Delft, The Netherlands_ 

> 3 _Pritzker School of Molecular Engineering, University of Chicago, Chicago, IL 60637, USA_ 

> 4 _SURF, P.O. Box 94613, 1090 GP Amsterdam, The Netherlands_ 

> 5 _Corresponding author: s.d.c.wehner@tudelft.nl_ 

(Dated: July 27, 2021) 

## **ABSTRACT** 

In order to bring quantum networks into the real world, we would like to determine the requirements of quantum network protocols including the underlying quantum hardware. Because detailed architecture proposals are generally too complex for mathematical analysis, it is natural to employ numerical simulation. Here we introduce NetSquid, the NETwork Simulator for QUantum Information using Discrete events, a discrete-event based platform for simulating all aspects of quantum networks and modular quantum computing systems, ranging from the physical layer and its control plane up to the application level. We study several use cases to showcase NetSquid’s power, including detailed physical layer simulations of repeater chains based on nitrogen vacancy centres in diamond as well as atomic ensembles. We also study the control plane of a quantum switch beyond its analytically known regime, and showcase NetSquid’s ability to investigate large networks by simulating entanglement distribution over a chain of up to one thousand nodes. 

## **I. INTRODUCTION** 

Quantum communication can be used to connect distant quantum devices into a quantum network. At short distances, networking quantum devices provides a path towards a scalable distributed quantum computer [1]. At larger distances, interconnected quantum networks allow for communication tasks between distant users on a quantum internet. Both types of quantum networks have the potential for large societal impact. First, analogous to classical computers, it is likely that any approach for scaling up a quantum computer so that it can solve real world problems impractical to treat on a classical computer, will require the interconnection of different modules [2–4]. Furthermore, quantum communication networks enable a host of tasks that are impossible using classical communication [5]. For both types of networks, many challenges must be overcome before they can fulfil their promise. The exact extent of these challenges remains unknown, and precise requirements to guide the construction of large-scale quantum networks are missing. At the physical layer, many proposals exist for quantum repeaters that can carry qubits over long distances (see e.g. [6–8] for an overview). Using analytical methods [9–30] and ad-hoc simulations [31– 38] rough estimates for the requirements of such hardware proposals have been obtained. Yet, while greatly valuable to set minimal requirements, these 

> _∗_ These authors contributed equally. 

> _†_ These authors jointly supervised this work. 

studies still provide limited detail. Even for a smallscale quantum network, the intricate interplay between many communicating devices, and the resulting timing dependencies makes a precise analysis challenging. To go beyond, we would like a tool that can incorporate not only a detailed physical modelling, but also account for the implications of timedependent behaviour. 

Quantum networks cannot be built from quantum hardware alone; in order to scale they need a tightly integrated classical control plane, i.e. protocols responsible for orchestrating quantum network devices to bring entanglement to users. Fundamental differences between quantum and classical information demand an entirely new network stack in order to create entanglement, and run useful applications on future quantum networks [39–44]. The design of such a control stack is furthermore made challenging by numerous technological limitations of quantum devices. A good example is given by the limited lifetimes of quantum memories, due to which delays in the exchange of classical control messages have a direct impact on the performance of the network. To succeed, we hence need to understand how possible classical control strategies do perform on specific quantum hardware. Finally, to guide overall development, we need to understand the requirements of quantum network applications themselves. Apart from quantum key distribution (QKD) [45–49] and a few select applications [50–53], little is known about the requirements of quantum applications [5] on imperfect hardware. 

Analytical tools offer only a limited solution for our needs. Statistical tools (see e.g. [54–57]) have been 

used to make predictions about certain aspects of large regular networks using simplified models, but are of limited use for more detailed studies. Information theory [58] can be used to benchmark implementations against the ideal performance. However, it gives no information about how well a specific proposal will perform. As a consequence, numerical methods are of great use to go beyond what is feasible using an analytical study. Ad-hoc simulations of quantum networks have indeed been used to provide further insights on specific aspects of quantum networks (see e.g. [31–38, 59–61]). However, while greatly informative, setting up ad-hoc simulations for each possible networking scenario to a level of detail that might allow the determination of more precise requirements is cumbersome, and does not straightforwardly lend itself to extensive explorations of new possibilities. 

We would hence like a simulation platform that satisfies at least the following three features: First, accuracy: the tool should allow modelling the relevant physics. This includes the ability to model timedependent noise and network behaviour. Second, modularity: it should allow stacking protocols and models together in order to construct complicated network simulations out of simple components. This includes the ability to investigate not only the physical layer hardware, but the entirety of the quantum network system including how different control protocols behave on a given hardware setup. Third, scalability: it should allow us to investigate large networks. 

Evaluating the performance of large classical network systems, including their time-dependent behaviour is the essence of classical network analysis. Yet, even for classical networks, the predictive power of analytical methods is limited due to complex emergent behaviour arising from the interplay between many network devices. Consequently, a crucial tool in the design of such networks are network simulators, which form a tool to test new ideas, and many such simulators exist for purely classical networks [62–64]. However, such simulators do not allow the simulation of quantum behaviour. 

In the quantum domain, many simulators are known for the simulation of quantum computers (see e.g. [65]). However, the task of simulating a quantum network differs greatly from simulating the execution of one monolithic quantum system. In the network, many devices are communicating with each other both quantumly and classically, leading to complex stochastic behaviour, and asynchronous and time-dependent events. From the perspective of building a simulation engine, there is also an important difference that allows for gains in the efficiency of the simulation. A simulator for a quantum computation is optimised to track large entangled states. In contrast, in a quantum network the state space grows and shrinks dynamically as qubits get measured or entangled, but for many protocols, at any moment in time the state space describing the quantum state of the network is small. We would thus like 

a simulator capable of exploiting this advantage. In this paper we introduce the quantum network simulator NetSquid: the NETwork Simulator for QUantum Information using Discrete events. NetSquid is a software tool (available as a package for Python and previously made freely available online [66]) for accurately simulating quantum networking and modular computing systems that are subject to physical non-idealities. It achieves this by integrating several key technologies: a discrete-event simulation engine, a specialised quantum computing library, a modular framework for modelling quantum hardware devices, and an asynchronous programming framework for describing quantum protocols. We showcase the utility of this tool for a range of applications by studying several use cases: the analysis of a control plane protocol beyond its analytically accessible regime, predicting the performance of protocols on realistic near-term hardware, and benchmarking different quantum devices. These use cases, in combination with a scalability analysis, demonstrate that NetSquid achieves all three features set forth above. Furthermore, they show its potential as a general and versatile design tool for quantum networks, as well as for modular quantum computing architectures. 

## **II. RESULTS AND DISCUSSION** 

## **A. NetSquid in a nutshell** 

Simulating a quantum network with NetSquid is generally performed in three steps. Firstly, the network is modelled using a modular framework of components and physical models. Next, protocols are assigned to network nodes to describe the intended behaviour. Finally, the simulation is executed for a typically large number of independent runs to collect statistics with which to determine the performance of the network. To explain these steps and the features involved further, we consider a simple use case for illustration. For a more detailed presentation of the available functionality and design of the NetSquid framework see section Design and functionality of NetSquid of the Methods. 

The scenario we will consider is the analysis of an entanglement distribution protocol over a quantum repeater chain with three nodes. The goal of the analysis is to estimate the average output fidelity of the distributed entangled pairs. The entanglement distribution protocol is depicted in Figure 1(d-e). It works as follows. First, the intermediate node generates two entangled pairs with each of its adjacent neighbours. Entanglement generation is modelled as a stochastic process that succeeds with a certain probability at every attempt. When two pairs are ready at one of the links, the DEJMPS entanglement distillation scheme [67] is run to improve the quality of the entanglement. If it fails, the two links are discarded and the executing nodes restart entanglement generation. Once both distilled states 

2 



<!-- Start of picture text -->
Fidelity of entanglement (F)<br>a) d) < 50% 100% e)<br>Node A ENTANGLEMENTGENERATED QUBITS DECOHEREWITH TIME 1 1 1<br>b)<br>Connection 1 7 1 1 1 1 7 7<br>Quantum<br>Source equal →<br>StateSampler DISTILLATION unequal→<br>SUCCEEDS<br>Classical 2 2 2<br>Quantum Channel<br>Channel 8 8<br>FibreLossModel<br>FibreDelayModel Node R<br>2 8 2 2 2 ENTANGLEMENT<br>3 9 SWAP<br>3 5 3 9 11 9 Repeat for N runs<br>c) DISTILLATION DISTILLATION f) 1<br>FAILS SUCCEEDS<br>10 -1<br>QuantumProcessor<br>X, Y, ZH PhysicalInstructions 1 F1 = 0.5<br>RXMeasure 0 CNOT F4 = 1<br>2 SWAP Node B 4 10<br>MemoryPosition 3 Time progresses by stepping from event to event 4 6 4 10 12 10 10 10 -6 F9 = 0F7 = 0.9<br>timeline 0 time [ms] 100<br>...<br>cumulative  probability<br><!-- End of picture text -->

Figure 1: **Illustrative example of a NetSquid use case.** Each sub-figure explains part of the modelling and simulation process. For greater clarity the figures are not based on real simulation data. The scenario shown is a quantum repeater utilising entanglement distillation (see main text). **a)** The setup of a quantum network using node and connection components. **b)** A zoom in showing the subcomponents of the entangling connection component. The quantum channels are characterised using fibre delay and loss models. The quantum source samples from an entangled bipartite state sampler when externally triggered by the classical channel. **c)** A zoom in of the quantum memory positions within a quantum processor illustrating their physical gate topology. The physical single-qubit instructions possible on each memory in this example are the Pauli ( _X_ , _Y_ , _Z_ ), Hadamard ( _H_ ), and _X_ -rotation ( _RX_ ) gates, and measurement. The blue-dashed arrows show the positions and control direction (where applicable) for which the two-qubit instructions controlled- _X_ (CNOT) and swap are possible. Noise and error models for the memories and gates are also assigned. **d)** Illustration of a single simulation run. Time progresses by discretely stepping from event to event, with new events generated as the simulation proceeds. Qubits are represented by circles, which are numbered according to the order they were generated. A star shows the moment of generation. The curved lines between qubits denote their entanglement with the colour indicating fidelity. The state of each qubit is updated as it is accessed during the simulation, for instance to apply time-dependent noise from waiting in memory. **e)** A zoom in of the distillation protocol. The shared quantum states of the qubits are combined in an entangling step, which then shrinks as two of the qubits are measured. The output is randomly sampled, causing the simulation to choose one of two paths by announcing success or failure. **f)** A plot illustrating the stochastic paths followed by multiple independent simulation runs over time, labeled by their final end-to-end fidelity _Fi_ . The blue dashed line corresponds to the run shown in panel (d). The runs are typically executed in parallel. Their results are statistically analysed to produce performance metrics such as the average outcome fidelity and run duration. 

are ready, the intermediate node swaps the entanglement to achieve end-to-end entanglement. We remark that already this simple protocol is rather involved to analyse. 

We begin by modelling the network. The basic element of NetSquid’s modular framework is the “component”. It is capable of describing the physical model composition, quantum and classical communication ports, and, recursively, any subcomponents. All hardware elements, including the network itself, are represented by components. For this example we require three remote nodes linked by two quantum and two classical connections, the setup of which is shown in Figure 1(a). In Figure 1(b,c) the nested structure of these components is highlighted. A se- 

lection of physical models is used to describe the loss and delay of the fibre optic channels, the decoherence of the quantum memories, and the errors of quantum gates. 

Quantum information in NetSquid is represented at the level of qubits, which are treated as objects that dynamically share their quantum states. These internally shared states will automatically merge or “split” – a term we use to mean the separation of a tensor product state into two separately shared sub-states – as qubits entangle or are measured, as illustrated by the distillation protocol in Figure 1(e). The states are tracked internally, i.e. hidden from users, for two reasons: to encourage a node-centric approach to programming network protocols, and to 

3 







allow a seamless switching between different quantum state representations. The representations offered by NetSquid are ket vectors, density matrices, stabiliser tableaus and graph states with local Cliffords, each with trade-offs in modelling versatility, computation speed and network (memory) scalability (see the subsection Fast and scalable quantum network simulation below and Supplementary Note 1). 

Discrete-event simulation, an established method for simulating classical network systems [68], is a modelling paradigm that progresses time by stepping through a sequence of events – see Figure 2 for a visual explanation. This allows the simulation engine to efficiently handle the control processes and feedback loops characteristic of quantum networking systems, while tracking quantum state decoherence based on the elapsed time between events. A novel requirement for its application to quantum networks is the need to accurately evolve the state of the quantum information present in a network with time. This can be achieved by retroactively updating quantum states when the associated qubits are accessed during an event. While it is possible to efficiently track a density matrix, quantum operations requiring a singular outcome for classical decision making, for instance a quantum measurement, must be probabilistically sampled. A single simulation run thus consists of a sequence of random choices that forms one of many possible paths. In Figure 1 (d) we show such a run for the repeater protocol example, which demonstrates the power of the discrete-event approach for tracking qubit decoherence and handling feedback loops. 

The performance metrics of a simulation are determined statistically from many runs. Due to the independence of each run, simulations can be massively parallelised and thereby efficiently executed on computing clusters. For the example at hand we choose as metrics the output fidelity and run duration. In Figure 1 (f) the sampled run from (d), which resulted in perfect fidelity, is plotted in terms of its likelihood and duration together with several other samples, some less successful. By statistically averaging all of the sampled runs the output fidelity and duration can be estimated. 

In the following sections, we will outline three use cases of NetSquid: first, a quantum switch, followed by simulations of quantum repeaters based on nitrogen-vacancy technology or atomic-ensemble memories. We will also benchmark NetSquid’s scalability in both quantum state size and number of quantum network nodes. Although the use cases each provide relevant insights into the performance of the studied hardware and protocols, we emphasise that one can use NetSquid to simulate arbitrary network topologies. 



<!-- Start of picture text -->
entanglement Alice<br>Charlie source 0,1<br>qubit quantum<br>arrives Bob memory<br>start . . . . . . . .<br>qubit message<br>arrives arrives<br>handle schedule event<br>event event timeline<br>Generate Measure & send Store & wait Apply corrections<br>entanglement<br>0,1 X<br>BSM<br><!-- End of picture text -->

Figure 2: **Abstract example of simulating a** 

**quantum protocol with discrete events** . When setting up the simulation, protocol actions are defined to occur when a specific event occurs, as in the setup of a real system. Instead of performing a continuous time evolution, the simulation advances to the next event, and then automatically executes the actions that should occur when the event takes place. Any action may again define future events to be triggered after a certain (stochastic) amount of time has elapsed. For concreteness a simplified quantum 

teleportation example is shown where a qubit, shown as an orange circle with arrow, is teleported between the quantum memories of Alice and Bob. Here, entanglement is produced using an abstract source sending two qubits, shown as blue circles with arrows, to Alice and Bob. Once the qubit has traversed the fibre and reaches Alice’s lab, an event is triggered that invokes the simulation of Alice’s Bell state measurement (BSM) apparatus. The simulation engine steps from event to events defined by the next action, which generally occur at irregular intervals. This approach allows time-dependent physical non-idealities, such as quantum decoherence, to be accurately tracked. 

## **B. Simulating a quantum network switch beyond its analytically known regime** 

As a first use case showcasing the power of NetSquid, we study the control plane of a recently introduced quantum switch beyond the regime for which analytical results have been obtained, including its performance under time-dependent memory noise. 

The switch is a node which is directly connected to each of _k_ users by an optical link. The communications task is distributing Bell pairs and _n_ -partite Greenberger-Horne-Zeilinger (GHZ) states [69] between _n ≤ k_ users. The switch achieves this by connecting Bell pairs which are generated at random intervals on each link. See Figure 3. 

Intuitively, the switch can be regarded as a generalisation of a simple repeater performing entanglement swapping with added logic to choose which parties to link. Even with a streamlined physical model, it is already rather challenging to analytically characterise the switch use case [56]. 

4 

In the following, we recover via simulation a selection of the results from Vardoyan et al. [56], who studied the switch as the central node in a star network, and extend them in two directions. First, we increase the range of parameters for which we can estimate entanglement rates using the same model as used in the work of Vardoyan et al. Second, simulation enables us to investigate more sophisticated models than the exponentially distributed erasure process from their work, in particular we analyse the behaviour of a switch in the presence of memory dephasing noise. 

The protocol for generating the target _n_ -partite GHZ states is simple. Entanglement generation is attempted in parallel across all _k_ links. If successful they result in bipartite Bell states that are stored in quantum memories. The switch waits until _n_ Bell pairs have been generated until performing an _n_ - partite GHZ measurement, which converts the pairs into a state locally equivalent to a GHZ state. An additional constraint is that the switch has a finite buffer _B_ of number of memories dedicated for each user (see Figure 3). If the number of pairs stored in a link is _B_ and a new pair is generated, the old one is dropped and the new one is stored. 

The protocol can be translated to a Markov chain. The state space is represented by a _k_ -length vector where each entry is associated with a link and its value denotes the number of stored links. The switch’s mean capacity, i.e. the number of states produced per second, can be derived from the steadystate of the Markov chain [56]. 

Using NetSquid, it is straightforward to fully reproduce the previous model and study the behaviour of the network without constructing the Markov Chain (details can be found in Supplementary Note 3). In Figure 4(a), we use NetSquid to study the capacity of a switch network serving nine users. The figure shows the capacity (number of produced GHZstates per second), which we investigate for three use cases. First we consider a switch network distributing bipartite entanglement. Second, we consider also a switch-network serving bipartite entanglement but with link generation rates that do not satisfy the stability condition for the Markov Chain if the buffer _B_ is infinitely large, i.e. a regime so far intractable. Third, we consider a switch-network distributing four-partite entanglement where the link generation rates _µ_ differ per user, a regime not studied so far, and compute the capacity. 

Beyond rate, it is important to understand the quality of the states produced. Answering this question with Markov chain models seems challenging. In order to analyse entanglement quality, we introduce a more sophisticated decoherence model where the memories suffer from decay over time. In particular, we model decoherence as exponential _T_ 2 noise, which impacts the quality of the state, as expressed in its fidelity with the ideal state. In Figure 4(b), we show the effect of the time-dependent memory noise on the average fidelity. 



<!-- Start of picture text -->
C<br>B = 2 qubits<br>per leaf node<br>B<br>LC<br>D<br>LD LB<br>SWITCH B B<br>NODE<br>C GHZ C<br>Measurement<br>3 H<br>LA 2<br>1<br>A<br>A A<br>qubit<br>entangled pair<br>of qubits<br>3<br>2<br>4<br>1<br><!-- End of picture text -->

Figure 3: **A quantum switch in a star-shaped network topology as studied by Vardoyan et al.[56]** . The switch (central node) is connected to a set of users (leaf nodes) via an optical fibre link that distributes perfect Bell pairs at random times, following an exponential distribution with mean rate _µ ∝ e_<sup>_−βL_</sup> , where _L_ denotes the distance of the link and _β_ the attenuation coefficient. Associated with each link there is a buffer that can store _B_ qubits at each side of the link. As soon as _n_ Bell pairs with different leaves are available, the switch performs a measurement in the _n_ -partite Greenberger-Horne-Zeilinger (GHZ) basis, which results in an _n_ -partite GHZ state shared by the leaves. The GHZ-basis measurement consists of: first, controlled-X gates with the same qubit as control; next, a Hadamard ( _H_ ) gate on the control qubit; finally, measurement of all qubits individually. The figure shows 4 leaf nodes, GHZ size _n_ = 3 and a buffer size _B_ = 2. 

## **C. Sensitivity analysis for the physical modelling of a long range repeater chain** 

The next use case is the distribution of long-distance entanglement via a chain of quantum repeater nodes [6, 9] based on nitrogen-vacancy (NV) centres in diamond [70, 71]. This example consists of a more detailed physical model and more complicated control plane logic than the quantum switch or the distillation example presented at the start of this section. It is also an example of how NetSquid’s modularity supports setting up simulations involving many nodes; in this case the node model and the protocol (which runs locally at a node) only need to be specified once, and can then be assigned to each node in the chain. Furthermore, the use of a discrete-event engine allows the actions of the individual protocols to be simulated asynchronously, in contrast to the typically sequential execution of quantum comput- 

5 



<!-- Start of picture text -->
- 4 o _O<br>+ — 00<br>slr gm<br><!-- End of picture text -->



<!-- Start of picture text -->
i<br><!-- End of picture text -->



<!-- Start of picture text -->
u<br><!-- End of picture text -->

The second question that we address is which protocol performs best for a given distance. We consider seven protocols: no repeater, and repeater chains implementing swap-asap or nested-withdistill over 1, 3 or 7 repeaters. The latter is motivated by the fact that the nested-withdistill protocol is defined for 2<sup>_n_</sup> _−_ 1 repeaters ( _n ≥_ 1), and thus 1, 3, and 7 are the first three possible configurations. In Figure 5(b), we sweep over the hardware parameter space for two distances, where we improve all hardware parameters simultaneously and the improvement is quantified by a number we refer to as "improvement factor" (see section How we choose improved hardware parameters of the Methods). For 500 km, we observe that the no-repeater configuration achieves larger or equal fidelity for the entire range studied. However, repeater schemes boost the rate for all parameter values. If we increase the distance to 800 km, then we see that the use of repeaters increases both rate and fidelity for the same range of parameters. If we focus on the repeater scheme, we observe for both distances that for high hardware quality, the nested-with-distill scheme, which includes distillation, is optimal. In contrast, for lower hardware quality, the best-performing scheme that achieves fidelities larger than the classical bound 0 _._ 5 is the swap-asap protocol. 

We note that beyond 700 km the entanglement rate decreases when the hardware is improved. This is due to the presence of dark counts, i.e. false signals that a photon has been detected. At large distances most photons dissipate in the fibre, whereby the majority of detector clicks are dark counts. Because a dark count is mistakenly counted as a successful entanglement generation attempt, improving (i.e. decreasing) the dark count rate in fact results in a lower number of observed detector clicks, from which the (perceived) entanglement rate plotted in Figure 5(a) is calculated. 

Lastly, in Figure 6, we investigate the sensitivity of the entanglement fidelity for the different hardware parameters. We take as the figure of merit the best fidelity achieved with a swap-asap protocol. The uniform improvement factor is set to 3, while the following four hardware parameters are varied: a two-qubit gate noise parameter, photon detection probability (excluding transmission), induced storage qubit noise and visibility. We observe that improving the detection probability yields the largest fidelity increase from 2 _×_ to 50 _×_ improvement, while this increase is smallest for visibility. We also see that improving two-qubit gate noise or induced storage qubit noise on top of an increase in detection probability yields only a small additional fidelity improvement, which however boosts fidelity beyond the classical threshold of 0.5. These observations indicate that detection probability is the most important parameter for realising remote-entanglement generation with the swap-asap scheme, followed by two-qubit gate noise and induced storage qubit noise. 

## **D. Performance comparison between two atomic-ensemble memory types through NetSquid’s modular design** 

Finally, we showcase that NetSquid’s modular design greatly reduces the effort of assessing possible hardware development scenarios. We demonstrate the power of this modularity by simulating point-topoint remote-entanglement generation based on either of two types of atomic-ensemble based quantum memories: atomic frequency combs (AFC) [72] and electronically induced transparency (EIT) [73, 74] memories. Both simulations are identical except for the choice of a different quantum memory component. 

The two types of memories are a promising building block for high-rate remote entanglement generation through quantum repeaters because of their high efficiency (EIT) or their ability for multiplexing (AFC), i.e. to perform many attempts at entanglement generation simultaneously without network components having to wait for the arrival of classical messages that herald successful generation. The first type of memories, AFCs, are based on a photon-echo process, where an absorbed photon is re-emitted after an engineered duration. In contrast, the second type, EITs, emit the photon after an ondemand interval, due to optical control. In principle the AFC protocol can be extended to offer such ondemand retrieval as well. At this point both technologies are promising candidates and it is not yet clear which outperforms the other and under what circumstances. 

Atomic-ensemble based repeaters have been analytically and numerically studied before with streamlined physical models [19, 75]. NetSquid’s discreteevent based paradigm allows us to go beyond that by concurrently introducing several non-ideal characteristics. In particular, we include the emission of more than one photon pair, photon distinguishability and time-dependent memory efficiency. Efficiency in this context is the probability that the absorbed photon will be re-emitted. All these characteristics have a significant impact on the performance of the repeater protocol. 

In order to compare the two memory types, we simulate many rounds of the BB84 quantum key distribution protocol [76] between two remote nodes, using a single repeater positioned precisely in between them. Entanglement generation is attempted in synchronised rounds over both segments in parallel. At the end of each round, the two end nodes measure in the X- or Z-basis, chosen uniformly at random, and the repeater performs a probabilistic linear-optical Bell-state measurement. Upon a successful outcome, we expect correlation between the measurement outcomes if they were performed in the same basis. As a figure of merit we choose the asymptotic BB84 secret-key rate. 

The results of our simulations are shown in Figure 7, where the rate at which secret key between the two nodes can be generated is obtained as a function 

7 



<!-- Start of picture text -->
1 / 3 / 7 repeaters:<br>Hardware quality: no repeater / / SWAP-ASAP<br>near-term no repeater<br>/ / WITH-DISTILL<br>10x 3 repeaters 500 km 800 km<br>1.0 1. 0 0<br>0.75<br>0.5<br>0.50<br>0.25<br>0.0<br>0.00<br>10 1 10 1<br>10 1 10 1<br>1010 35 10 3<br>10 5<br>20 250 500 750 1000 1250 1500<br>Distance between end nodes [km] 10 7 1 5 10 15 20 25 1 5 10 15 20 25 30<br>Uniform hardware improvement<br>(b)<br>(c)<br>(a)<br>Fidelity Fidelity<br>Rate [Hz]<br>Rate [Hz]<br><!-- End of picture text -->

Figure 5: **Performance of repeaters based on nitrogen-vacancy (NV) centres in diamond. (a)** Fidelity and entanglement distribution rate achieved with near-term and 10 _×_ improved hardware (Supplementary Note 4) with the swap-asap protocol. Dashed line represents classical fidelity threshold of 0 _._ 5. We observe that for near-term hardware, the use of 3 repeaters yields worse performance in terms of fidelity than the no-repeater setup. For improved hardware we observe (i) that for approx. 0 - 750 kms, repeaters improve upon rate by orders of magnitude while still producing entanglement (fidelity _>_ 0 _._ 5), while (ii) for approx. 750 - 1500 kms, repeaters outperform in both rate and fidelity. **(b-c)** Fidelity and rate achieved without and with repeaters (1, 3 or 7 repeaters) as function of a hardware improvement factor (Methods, section How we choose improved hardware parameters) for two typical distances from both distance regime (i) and (ii), for two protocols swap-asap and nested-with-distill. For the repeater case, only the best-performing number-of-repeaters & protocol in terms of achieved fidelity is shown in (b), accompanied by its rate in (c). Each data point represents the average over (a) 200 and (b) 100 runs. Standard deviation is smaller than dot size. 

of the distance between the nodes. For the parameters considered (see Supplementary Note 7), we observe that EIT memories outperform AFC memories at short distances. The crossover performance point is reached at _∼_ 50 kilometers, beyond which AFC memories outperform EIT memories. 

In the use case above, we showcased NetSquid’s modularity by only replacing the memory component. We emphasise that this modularity also applies to different parts of the simulation. For example, if the quantum switch should produce a different type of multipartite state than GHZ states, then one only needs to change the circuit at the switch node. A different example is the NV repeater chain, where one could replace the protocol module (currently either swap-asap or nested-with-distill). 

## **E. Fast and scalable quantum network simulation** 

NetSquid has been designed and optimised to meet several key performance criteria: to be capable of accurate physical modelling, to be scalable to large networks, and to be sufficiently fast to support multi-variate design analyses with adequate statistics. While it is not always possible to jointly satisfy all the criteria for all use cases, NetSquid’s design allows the user to prioritise them. We proceed to benchmark NetSquid to demonstrate its capabilities and unique strengths for quantum network simula- 

tion. 

## _1. Benchmarking of quantum computation_ 

To accurately model physical non-idealities, it is necessary to choose a representation for quantum states that allows a characterisation of general processes such as amplitude damping, general measurements, or arbitrary rotations. NetSquid provides two representations, or “formalisms”, that are capable of universal quantum computation: ket state vectors (KET) and density matrices (DM), both stored using dense arrays. The resource requirements for storage in memory and the computation time associated with applying quantum operations both scale exponentially with the number of qubits. While the density matrix scales less favourably, 2<sup>2</sup><sup>_n_</sup> versus 2<sup>_n_</sup> for _n_ qubits, its ability to represent mixed states makes it more versatile for specific applications. Given the exponential scaling, these formalisms are most suitable for simulations in which a typical qubit lifetime involves only a limited number of (entangling) interactions. 

When scaling to large network simulations it can happen that hundreds of qubits share the same entangled quantum state. For such use cases, we need a quantum state representation that scales subexponentially in time and space. NetSquid provides two such representations based on the stabiliser state formalism: “stabiliser tableaus” (STAB) and 

8 



<!-- Start of picture text -->
(A) two-qubit gate noise<br>(A) & (D) (A) & (B)<br>(B) detection<br>(D) probability<br>visibility (excluding<br>transmission)<br>single/two-<br>parameter<br>(C) & (D) (B)  improvement:<br>  & (C) 2x<br>3x<br>(C) induced storage qubit noise 10x<br>50x<br>0.35<br>0.30<br>0.55<br>0.45<br>0.50 fidelity<br><!-- End of picture text -->

Figure 6: **Sensitivity of fidelity in various hardware parameters for nitrogen-vacancy (NV) repeater chains.** The NV hardware model consists of<sup>�</sup> 15 parameters and from those we focus on four parameters in this figure: (A) two-qubit gate fidelity, (B) detection probability, (C) induced storage qubit noise and (D) visibility. We start by improving all<sup>�</sup> 15 parameters, including the four designated ones, using an improvement factor of 3 (Methods, section How we choose improved hardware parameters). Then, for each of the four parameters only, we individually decrease their improvement factor to 2, or increase it to 10 or 50. The figure shows the resulting fidelity (horizontal and vertical grid lines; dashed line indicates maximal fidelity which can be attained classically). Note that at an improvement factor of 3 (orange line), all<sup>�</sup> 15 parameters are improved by 3 times, resulting in a fidelity of 0.39. In addition, we vary the improvement factor for combinations of two of the four parameters (diagonal lines). The 3 _×_ improved parameter values can be found in Supplementary Table II. The other values (at 2 _/_ 10 _/_ 50 _×_ ) are approximately: two-qubit gate fidelity _FEC_ (0 _._ 985 _/_ 0 _._ 997 _/_ 0 _._ 9994), detection probability _p_<sup>nofibre</sup> det (6 _._ 8% _/_ 58% _/_ 90%), induced storage qubit noise _N_ 1 _/e_ (2800 _/_ 14000 _/_ 70000), visibility _V_ (95% _/_ 99% _/_ 99 _._ 8%). The fidelities shown are obtained by simulation of the swap-asap protocol (3 repeaters) with a total spanned distance of 500 km. Each data point represents the average of 1000 runs (standard deviation on fidelity _<_ 0 _._ 002). 

“graph states with local Cliffords” (GSLC) [77, 78] that the user can select. Stabiliser states are a subset of quantum states that are closed under the application of Clifford unitaries and single-qubit measurement in the computational basis. In the context of simulations for quantum networks stabiliser states are particularly interesting because many network protocols consist of only Clifford operations and noise can be well approximated by stochastic application of Pauli gates. For a theoretical compar- 

ison of the STAB and GSLC formalisms see Supplementary Note 1. 

The repetitive nature of simulation runs due to the collection of statistics via random sampling allows NetSquid to take advantage of “memoization” for expensive quantum operations, which is a form of caching that stores the outcome of expensive operations and returns them when the same input combinations reoccur to save computation time. Specifically, the action of a quantum operator onto a quantum state for a specific set of qubit indices and other discrete parameters can be efficiently stored, for instance as a sparse matrix. Future matching operator actions can then be reduced to a fast lookup and application, avoiding several expensive computational steps – see the Methods, section Qubits and quantum computation for more details. 

In the following we benchmark the performance of the available quantum state formalisms. For this, we first consider the generation of an _n_ qubit entangled GHZ state followed by a measurement of each qubit (see section Benchmarking of the Methods). For a baseline comparison with classical quantum computing simulators we also include the ProjectQ [79] package for Python, which uses a quantum state representation equivalent to our ket vector. We show the average computation time for a single run versus the number of qubits for the different quantum computation libraries in Figure 8(a). The exponential scaling of the universal formalisms in contrast to the stabiliser formalisms is clearly visible, with the density matrix formalism performing noticeably worse. For the ket formalism we also show the effect of memoization, which gives a speed-up roughly between two and five. 

Let us next consider a more involved benchmarking use case: the quantum computation involved in simulating a repeater chain i.e. only the manipulation of qubits, postponing all other simulation aspects, such as event processing and component modelling, to the next section. This benchmark involves the following steps: first the _N −_ 1 pairs of qubits along an _N_ node repeater chain are entangled, then each qubit experiences depolarising noise, and finally adjacent qubits on all but the end-nodes do an entanglement swap via a Bell state measurement (BSM). If the measured qubits are split from their shared quantum states after the BSM, then the size of any state is limited to four qubits. 

The average computation time for a single run versus the number of qubits in the chain are shown for the different quantum computation libraries in Figure 8(b), where we have again included ProjectQ. We observe that for the NetSquid formalisms (but not for ProjectQ) keeping qubits “in-place” after each measurement is more performant than “splitting” them below a certain threshold due to the extra overhead of doing the latter. The ket vector formalism is seen to be the most efficient for this benchmarking use case if states are split after measurement. When the measurement operations are performed in-place the GSLC formalism performs 

9 



<!-- Start of picture text -->
10 1 0.20<br>EIT EIT<br>10 2 AFC AFC<br>0.15<br>10 2<br>10 3 EIT X basis<br>EIT Z basis<br>0.10<br>10 4 AFC X basis<br>AFC Z basis<br>10 5 0.05 10 1<br>10 6<br>0 0.00<br>0 20 40 60 80 100 0 20 40 60 80 100 0 20 40 60 80 100<br>Total Distance [km] Total Distance [km] Total Distance [km]<br>(a) (b) (c)<br>ess<br>c<br>QBER<br>f attempts/suc<br>o<br>Secret Key Rate [bits/att.]<br>Number<br><!-- End of picture text -->

Figure 7: **Performance comparison of a single quantum repeater with atomic frequency comb (AFC) or electronically induced transparency (EIT) quantum memories** . Shown are: **(a)** the secret key rate in secret bits per entanglement generation attempt, **(b)** the quantum bit error rate (QBER) in the X and Z bases **(c)** the average number of attempts necessary for one successful end-to-end entanglement generation. Each data point is obtained using 10.000 (EIT) or 30.000 (AFC) successful attempts at generating entanglement between the end nodes. Solid lines are fits. Note that for the secret key plot we use logarithmic scale with added 0 at the origin of the axes. Error bars denote standard deviation and are symmetrical. 





<!-- Start of picture text -->
(a) (b)<br><!-- End of picture text -->

Figure 8: **Runtime comparison of NetSquid’s quantum state formalisms.** Runtime comparisons of the available quantum state formalisms in NetSquid as well as ProjectQ ket vector for two benchmark use cases. The KET, DM, STAB and GSLC formalisms refer to the use of ket vectors, density matrices, stabiliser tableaus and graph states with local Cliffords, respectively. **(a)** Generating a Greenberger-Horne-Zeilinger (GHZ) state. Qubits are _split_ off from the shared quantum state after a measurement. For the KET formalism the effect of turning off memoization (dotted line) is also shown. **(b)** Quantum computation involved in a repeater chain. Each formalism is shown with qubits split (dotted lines) versus being kept _in-place_ (solid lines) after measurement. 

the best beyond 15 qubits. 

## _2. Benchmarking of event-driven simulations_ 

As explained in the results section, a typical NetSquid simulation involves repeatedly sampling many independent runs. As such NetSquid is “embarrassingly parallelisable”: the reduction in runtime scales linearly with the number of processing cores available, assuming there is sufficient memory available. 

Nonetheless, given the computational requirements associated with collecting sufficient statistics and analysing large parameter spaces it remains crucial to optimise the runtime performance per core. 

Depending on the size of the network, the detail of the physical modelling, and the duration of the protocols under consideration, the number of events processed for a single simulation run can range anywhere from a few thousand to millions. To efficiently process the dynamic scheduling and handling of events NetSquid uses the discrete-event simulation 

10 

engine PyDynAA [80] (see section Discrete event simulation of the Methods). NetSquid aims to schedule events as economically as possible, for instance by streamlining the flow of signals and messages between components using inter-connecting ports. To benchmark the performance of an event-driven simulation run in NetSquid we consider a simple network that extends the single repeater (without distillation) shown in Figure 1 into an _N_ node chain – see Supplementary Note 2 for further details on the simulation setup. For the quantum computation we will use the ket vector formalism based on the benchmarking results from the previous section, and split qubits from their quantum states after measurement to avoid an exponential scaling with the number of nodes. In Figure 9 we show the average computation time for deterministically generating end-to-end entanglement versus the number of nodes in the chain. Also shown is a relative breakdown in terms of the time spent in the NetSquid sub-packages involved, as well as the PyDynAA and NumPy packages. We observe that the biggest contribution to the simulation runtime is the components sub-package, which accounts for 30% of the total at 1000 nodes. The relative time spent in each of the NetSquid subpackages, as well as NumPy and PyDynAA, is seen to remain constant with the number of nodes. The total runtime of each of the NetSquid sub-packages is the sum of many small contributions, with the costliest function for the components sub-package for a 1000 node chain, for example, contributing only 7% to the total. 

Extending this benchmark simulation with more detailed physical modelling may shift the relative runtime distribution and impact the overall performance. For example, more time may be spent in calls to the “components” and “components.models” subpackages, additional complexity can increase the volume of events processed by the “pydynaa” engine, and extra quantum characteristics can lead to larger quantum states. In case of the latter, however, the effective splitting of quantum states can still allow such networks to scale if independence among physical elements can be preserved. 

## **F. Comparison with other quantum network simulators** 

Let us compare NetSquid to other existing quantum network simulators. First, SimulaQron [81] and QuNetSim [82] are two simulators that do not aim at realistic physical models of channels and devices, or timing control. Instead, SimulaQron’s main purpose is application development. It is meant to be run in a distributed fashion on physically-distinct classical computers. QuNetSim focuses on simplifying the development and implementation of quantum network protocols. 

In contrast with SimulaQron and QuNetSim, the simulator SQUANCH [83] allows for quantum network simulation with configurable error models at 



<!-- Start of picture text -->
2 . 00 Runtime profile of a repeater chain<br>nodes<br>1 . 75 protocols 0 . 02<br>util<br>1 . 50<br>components.models<br>0 . 00<br>1 . 25 components 3 5 10 15 20<br>qubits<br>1 . 00 numpy<br>pydynaa<br>0 . 75 other<br>0 . 50<br>0 . 25<br>0 . 00<br>3 100 200 300 400 500 600 700 800 900 1000<br>Number of nodes<br>[s]<br>Runtime<br><!-- End of picture text -->

Figure 9: **Runtime profile of a repeater chain simulation using Netsquid.** Runtime profile for a repeater chain simulation with a varying number of nodes in the chain. The maximum quantum state size is four qubits. The total time spent in the functions of each NetSquid subpackage and its main package dependencies (in italics) is shown. The dark hatched bands show the largest contribution from a single function in each NetSquid sub-package, as well as in NumPy and uncategorised ( _other_ ) functions. The sub-packages are stacked in the same order as they are listed in the legend. 

the physical layer. However, SQUANCH, similar to SimulaQron and QuNetSim, does not use a simulation engine that can accurately track time. Accurate tracking is crucial for e.g. studying time-dependent noise such as memory decoherence. 

Other than NetSquid, there now exist three discreteevent quantum simulators: the QuISP [84], qkdX [85] and SeQUeNCe [86] simulators. With these simulators it is possible to accurately characterise complex timing behaviour, however they differ in goals and scope. Similarly to NetSquid, QuISP aims to support the investigation of large networks that consist of too many entangled qubits for full quantum-state tracking. In contrast to NetSquid, which achieves this by managing the size of the state space, and providing the stabiliser representation as one of its quantum state formalisms, QuISP’s approach is to track an error model of the qubits in a network instead of their quantum state. qkdX, on the other hand, captures the physics more closely through models of the quantum devices but is restricted to the simulation of quantum key distribution protocols. Lastly, SeQUeNCe, similar to NetSquid, aims at simulation at the level of hardware, control plane or application. It has a fixed control layer consisting of reprogrammable modules. In contrast, NetSquid’s modularity is not tied to a particular network stack design. Furthermore, it is unclear to us how performant SeQUeNCe’s quantum simulation engine is: currently, at most a 9-node network has been simulated, whereas NetSquid’s flexibility to choose a quantum state representation enables 

11 

scalability to simulation of networks of up to 1000 nodes. 

distributed quantum computers or more generally to simulate different components in modular architectures. 

## **G. Conclusions** 

## **III. METHODS** 

In this work we have presented our design of a modular software framework for simulating scalable quantum networks and accurately modelling the nonidealities of real world physical hardware, providing us with a design tool for future quantum networks. We have showcased its power and also its limitations via example use cases. Let us recap NetSquid’s main features. 

First, NetSquid allows the modelling of any physical device in the network that can be mapped to qubits. To demonstrate this we studied two use cases involving nitrogen-vacancy centres in diamond as well as atomic-ensemble based memories. 

Second, NetSquid is entirely modular, allowing users to set up large scale simulations of complicated networks and to explore variations in the network design; for example, by comparing how different hardware platforms perform in an otherwise identical network layout. Moreover, this modularity makes it possible to explore different control plane protocols for quantum networks in a way that is essentially identical to how such protocols would be executed in the real world. Control programs can be run on any simulated network node, exchanging classical and quantum communication with other nodes as dictated by the protocol. That allows users to investigate the intricate interplay between control plane protocols and the physical devices dictating the performance of the combined quantum network system. As an example, we studied the control plane of a quantum network switch. NetSquid has also already found use in exploring the interplay between the control plane and the physical layer in [39, 87, 88]. Finally, to allow large scale simulations, the quantum computation library used by NetSquid has been designed to manage the dynamic lifetimes of many qubits across a network. It offers a seamless choice of quantum state representations to support different modelling use cases, allowing both a fully detailed simulation in terms of wave functions or density matrices, or simplified ones using certain stabiliser formalisms. As an example use case, we explored the simulation run-time of a repeater chain with up to one thousand nodes. 

In light of the results we have presented, we see a clear application for NetSquid in the broad context of communication networks. It can be used to predict performance with accurate models, to study the stability of large networks, to validate protocol designs, to guide experiment, etc. While we have only touched upon it in our discussion of performance benchmarks, NetSquid would also lend itself well to the study of modular quantum computing architectures, where the timing of control plays a crucial role in studying their scalability. For instance, it might be used to validate the microarchitecture of 

## **A. Design and functionality of NetSquid** 

The NetSquid simulator is available as a software package for the Python 3 programming language. It consists of the sub-packages “qubits”, “components”, “models”, “nodes”, “protocols” and “util”, which are shown stacked in Figure 10. NetSquid depends on the PyDynAA software library to provide its discrete-event simulation engine [80]. Under the hood speed critical routines and classes are written in Cython [89] to give C-like performance, including its interfaces to both PyDynAA and the scientific computation packages NumPy and SciPy. In the following subsections we highlight some of the main design features and functionality of NetSquid; for a more detailed presentation see Supplementary Note 1. 



<!-- Start of picture text -->
netsquid package v0.10<br>protocols util<br>ServiceProtocol NodeProtocol Protocol<br>Data-<br>Collector<br>nodes<br>Node Network Connection<br>simlog<br>components<br>models QuantumMemory<br>Channel simstats<br>ErrorModel DelayModel Port etc.<br>Model Component simtools<br>qubits<br>pydynaa<br>qubitapi Qubit QState<br>Entity Event<br>Operator EventHandler<br>{Ket,DM,Stab,GSLC}State<br>EventExpression<br>(sub)package module Class Inheritance Composition Aggregation<br>Not all classes and modules are shown<br><!-- End of picture text -->

Figure 10: **Overview of NetSquid’s software architecture.** The sub-packages that make up the NetSquid package are shown stacked in relation to each other and the PyDynAA package dependency. The main classes in each (sub-)package are highlighted, and their relationships in terms of inheritance, composition and aggregation are shown. Also shown are the key modules users interact with, which are described in the main text. In this paper NetSquid version 0.10 is described. 

## _1. Discrete event simulation_ 

The PyDynAA package provides a fast, powerful, and lightweight discrete-event simulation engine. It is a C++ port of the core engine layer from the DynAA simulation framework [80], with bindings 

12 

added for the Python and Cython languages. DynAA defines a concise set of classes and concepts for modelling event-driven simulations. The simulation engine manages a timeline of “events”, which can only be manipulated by objects that are subclasses of the “entity” base class. Simulation entities can dynamically schedule events on the timeline and react to events by registering an “event handler” object to wait for event(s) with a specified type, source entity, or identifier to be triggered. 

To deal with the timing complexities encountered in NetSquid simulations, an “event expression” class was introduced to PyDynAA to allow entities to also wait on logical combinations of events to occur. Atomic event expressions, which describe regular wait conditions for standard events, can be combined to form composite expressions using logical “and” and “or” operators to any depth. This feature has been used extensively in NetSquid to model both the internal behaviour of hardware components, as well as for programming network protocols. 

## _2. Qubits and quantum computation_ 

The qubits sub-package of NetSquid defines the “qubit” object that is used to track the flow of quantum information. Qubits internally share quantum state (“QState”) objects, which grow and shrink in size as qubits interact or are measured. The “QState” class is an interface that is implemented by a range of different formalisms, as presented in section Benchmarking of quantum computation of the Results and Discussion. Via the qubit-centric API, which provides functions to directly manipulate qubits without knowledge of their shared quantum states, users can program simulations in a formalism agnostic way. Functionality is also provided to automatically convert between quantum states that use different formalisms, and to sample from a distribution of states, which is useful for instance for pure state formalisms. 

The ket and density matrix formalisms use dense arrays (vectors or matrices, respectively) to represent quantum states. Applying a _k_ qubit operator to an _n_ qubit ket vector state generally involves the computationally expensive task of performing 2<sup>_n−k_</sup> matrix multiplications on 2<sup>_k_</sup> temporary sub-vectors and aggregating the result (only in special cases can this be done in-place) [90, 91]. The analogous application of an operator to a density matrix is more expensive due to the extra dimension involved. However, as discussed in section Fast and scalable quantum network simulation of the Results and Discussion, the repetitive nature of NetSquid simulations allows us to take advantage of operators frequently being applied to the same qubit indices for states of a given size. For these operators, we compute a 2<sup>_n_</sup> _×_ 2<sup>_n_</sup> dimensional sparse matrix representation of the _k_ qubit operator via tensor products with the identity and memoize this result for the specific indices and size. When the memoization is applicable the com- 

putational cost of applying a quantum operator can then be reduced to just sparse matrix multiplication onto a dense vector or matrix. Memoization is similarly applicable to general Clifford operators in the stabiliser tableau formalism. To use memoization on operators that depend on a continuous parameter, such as arbitrary rotations, the parameter can be discretised i.e. rounded to some limited precision. 

## _3. Physical modelling of network components_ 

All physical devices in a quantum network are modelled by a “component” object, and are thereby also all simulation entities, as shown in Figure 10. Components can be composed of subcomponents, which makes setting up networks in NetSquid modular. The network itself, for instance, can be modelled as a composite component containing “node” and “connection” components; these composite components can in turn contain components such as quantum memories, quantum and classical channels, quantum sources, etc., as illustrated in Figure 1. The physical behaviour of a component is described by composing it of “models”, which can specify physical characteristics such as transmission delays or noise such as photon loss or decoherence. Communication between components is facilitated by their “ports”, which can be connected together to automatically pass on messages. 

NetSquid also allows precise modelling of quantum computation capable devices. For this it provides the “quantum processor” component, a subclass of the quantum memory. This component is capable of executing “quantum programs” i.e. sequences of “instructions” that describe operations such as quantum gates and measurements or physical processes such as photon emission. Quantum programs fully support conditional and iterative statements, as well as parallelisation if the modelled device supports it. When a program is executed its instructions are mapped to the physical instructions on the processor, which model the physical duration and errors associated to carrying out the operation. A physical instruction can be assigned to all memory positions or only to a specific position, as well as directionally between specific memory positions in the case of multi-qubit instructions. 



NetSquid provides a “protocol” class to describe the network protocols and classical control plane logic running on a quantum network. Similarly to the component class, a protocol is a simulation entity and can thereby directly interact with the event timeline. Protocols can be nested inside other protocols and may describe both local or remote behaviour across a network. The “node protocol” subclass is specifically restricted to only operating lo- 

13 

cally on a single node. Inter-protocol communication is possible via a signalling mechanism and a request and response interface defined by the “service protocol” class. Protocols can be programmed using both the standard callback functionality of PyDynAA and a tailored asynchronous framework that allows the suspension of a routine conditioned on an “event expression”; for example, to wait for input to arrive on a port, a quantum program to finish, or to pause for a fixed duration. 

The “util” sub-package shown in Figure 10 provides a range of utilities for running, recording and interacting with simulations. Functions to control the simulation are defined in the “simtools” module, including functions for inspecting and diagnosing the timeline. A “data collector” class supports the event-driven collection of data during a simulation, which has priority over other event handlers to react to events. The “simstats” module is responsible for collecting a range of statistics during a simulation run, such as the number of events and callbacks processed, the maximum and average size of manipulated quantum states, and a count of all the quantum operations performed. Finally, the “simlog” module allows fine grained logging of the various modules for debugging purposes. 

## _5. Benchmarking_ 

To perform the benchmarking described in section Fast and scalable quantum network simulation of the Results and Discussion we used computing nodes with two 2.6 GHz Intel Xeon E5-2690 v3 (Haswell) 12 core processors and 64 GB of memory. Because each process only requires a single core, care was taken to ensure sufficient cores and memory were available when running jobs in parallel. The computation time of a process is the arithmetic average of a number of successive iterations; to avoid fluctuations due to interfering CPU processes the reported time is a minimum of five such repeated averages. To perform the simulation profiling the Cython extension modules of both NetSquid and PyDynAA were compiled with profiling on, which adds some runtime overhead. Version 0.10.0 and 0.3.5 of NetSquid and PyDynAA were benchmarked. We benchmarked against ProjectQ version 0.4.2 using its “MainEngine” backend. See Supplementary Note 2 for further details. 

Using the same machine, simulations for Figure 5(bc) were run, which took almost 260 core hours wallclock time in total, while simulations for Figure 7 took roughly 625 core hours. For Figure 4 ( _≈_ 10 hours in total), Figure 5(a) ( _≈_ 90 minutes) and Figure 6 ( _≈_ 30 minutes), a single core Intel Xeon Gold 6230 processor (3.9GHz) with 192 GB RAM was used. 

## **B. Implementing a processing-node repeater chain in NetSquid** 

Here, we explain the details of the most complex of our three use cases, namely the repeater chain of Nitrogen-Vacancy-based processing nodes from section Sensitivity analysis for the physical modelling of a long range repeater chain of the Results and Discussion (see Supplementary Notes 3 and 7 for details on the other two use cases). We first describe how we modelled the NV hardware, followed by the repeater protocols used. With regard to the physical modelling, let us emphasise that this is well established (see e.g. [92]); the main goal here is to explain how we used this model in a NetSquid implementation. 

In our simulations the following NetSquid components model the physical repeater chain: “nodes”, each holding a single “quantum processor” modelling the NV centre, and “classical channels” that connect adjacent nodes and are modelled as fibres with a constant transmission time. We choose equal spacing between the nodes. If we were to simulate individual attempts at entanglement generation, we would also need components for transmitting and detecting qubits such as was used in previous NetSquid simulations of NV centres [39]. However, in order to speed up simulations we insert the entangled state between remote NVs using a model. We designed two types of protocols to run on each node of this network that differ in whether they implement a scheme with or without distillation. 

In the remainder of this section, we describe the components modelling. More detailed descriptions of the hardware parameters and their values used in our simulation can be found in Supplementary Note 4. 

## _1. Modelling a nitrogen-vacancy centre in diamond_ 

In NetSquid, the NV centre is modelled by a quantum processor component, which holds a single communication qubit (electronic spin-1 system) and multiple storage qubits (<sup>13</sup> C nuclear spins). The decay of the state held by a communication qubit or storage qubit is implemented using a noise model, which is based on the relaxation time _T_ 1 and the dephasing time _T_ 2. If a spin is acted upon after having been idle for time ∆ _t_ , then to its state _ρ_ we first apply a quantum channel 



where 



and _p_ = 1 _− e_<sup>_−_∆</sup><sup>_t/T_1</sup> . Subsequently, we apply a dephasing channel 



14 

where _Z_ = _|_ 0 _⟩⟨_ 0 _| −|_ 1 _⟩⟨_ 1 _|_ and the dephasing probability equals 



The electron and nuclear spins have different _T_ 1 and _T_ 2 times. 

We allow the quantum processor to perform the following operations on the electron spin: initialisation (setting the state to _|_ 0 _⟩_ ), readout (measurement in the _{|_ 0 _⟩ , |_ 1 _⟩}_ basis) and arbitrary single-qubit rotation. In particular, the latter includes Pauli rotations 



where _θ_ is the rotation angle, _P ∈ {X, Y, Z}_ and 112 = _|_ 0 _⟩⟨_ 0 _|_ + _|_ 1 _⟩⟨_ 1 _|_ , _X_ = _|_ 0 _⟩⟨_ 1 _|_ + _|_ 1 _⟩⟨_ 0 _|_ , _Y_ = _−i|_ 0 _⟩⟨_ 1 _|_ + _i|_ 1 _⟩⟨_ 0 _|_ and _Z_ = _|_ 0 _⟩⟨_ 0 _| −|_ 1 _⟩⟨_ 1 _|_ are the single-qubit Pauli operators. For the nuclear spin, we have only initialisation and rotations _RZ_ ( _θ_ ) for arbitrary rotation angle _θ_ . In addition, we allow the two-qubit controlled- _RX_ ( _±θ_ ) gate between an electron ( _e_ ) and a nuclear ( _n_ ) spin: 



We model each noisy operation _O_ noisy as the perfect operation _O_ perfect followed by a noise channel _N_ : 



If _O_ is a single-qubit rotation, then _N_ is the depolarising channel: 



with parameter _p_ = 4(1 _− F_ ) _/_ 3 with _F_ the fidelity of the operation. 

If _O_ is single-qubit initialisation, _N_ = _Np_<sup>depol</sup> with parameter _p_ = 2(1 _− F_ ). The noise map of the controlled- _RX_ gate is an identical single-qubit depolarising channel on both involved qubits, i.e. _N_ = _Np_<sup>depol</sup> _⊗Np_<sup>depol</sup> . Finally, we model electron spin readout by a POVM measurement with the Kraus operators 



where 1 _− f_ 0 (1 _− f_ 1) is the probability that a measurement outcome 0 (1) is flipped to 1 (0). 

## _2. Simulation speedup via state insertion_ 

For generating entanglement between the electron spins of two remote NVs, we simulate a scheme based on single-photon detection, following its experimental implementation in [93]. NetSquid was used previously to simulate each generation attempt of this 

scheme, which includes the emission of a single photon by each NV, the transmission of the photons to the midpoint through a noisy and lossy channel, the application of imperfect measurement operators at the midpoint, and the transmission of the measurement outcome back to the two involved nodes [39]. For larger internode distances, simulating each attempt requires unfeasibly long simulation times due to the exponential decrease in attempt success rate. To speed up our simulations in the examples studied here, we generate the produced state between adjacent nodes from a model which has shown good agreement with experimental results [93]. This procedure includes a random duration and noise induced on the storage qubits, as we describe below. Let us define 



where _p_ det is the detection probability, _p_ dc the dark count probability, _V_ denotes photon indistinguishability and _α_ is the bright-state parameter (see Supplementary Note 4 for parameter descriptions). We follow the model of the produced entangled state from the experimental work of [93], whose setup consists of a beam splitter with two detectors located between the two adjacent nodes. In their model, the unnormalised state is given by 



where _±_ denotes which of the two detectors detected a photon (each occurring with probability <u>12</u><sup>).We</sup> also follow the model of [93] for double-excitation noise and optical phase uncertainty, by applying a dephasing channel to both qubits with parameter _p_ = _p_ dexc _/_ 2, followed by a dephasing channel of one of the qubits, respectively. 

The success probability of a single attempt is 



The time elapsed until the fresh state is put on the electron spins is ( _k −_ 1) _·_ ∆ _t_ with ∆ _t_ := ( _t_ emission + _L/c_ ), where _t_ emission is the delay until the NV centre emits a photon, _L_ the internode distance and _c_ the speed of light in fibre. Here, _k_ is the number of attempts up to and including successful entanglement generation and is computed by drawing a random sample from the geometric distribution Pr( _k_ ) = _p_ succ _·_ (1 _− p_ succ)<sup>_k−_1</sup> . After the successful generation, we wait for another time ∆ _t_ to 

15 

mimic the photon travel delay and midpoint heralding message delay. 

Every entanglement generation attempt induces dephasing noise on the storage qubits in the same NV system. We apply the dephasing channel (eq. (1)) at the end of the successful entanglement generation, where the accumulated dephasing probability is 



where _p_ single is the single-attempt dephasing probability (see eq. (46) in Supplementary Note 4). 

## _3. How we choose improved hardware parameters_ 

Here, we explain how we choose ‘improved’ hardware parameters. Let us emphasise that this choice is independent of the setup of our NetSquid simulations and only serves the purpose of showcasing that NetSquid can assess the performance of hardware with a given quality. 

By ‘near-term’ hardware, we mean values for the above defined parameters as expected to be achieved in the near future by NV hardware. If we say that an error probability is improved by an improvement factor _k_ , we mean that its corresponding no-error probability equals<sup>_√_</sup> _k_ _<u>p</u>_ ne, where _p_ ne is the no-error probability of the near-term hardware. For example, visibility _V_ is improved as<sup>_√_</sup> _k V_ while the probability of dephasing _p_ of a gate is improved as 1 _−_<sup>_√_</sup> _k_ 1 _− p_ . A factor _k_ = 1 thus corresponds to ‘near-term’ hardware. By ‘uniform hardware improvement by _k_ ’, we mean that all hardware parameters are improved by a factor _k_ . We do not improve the duration of local operations or the fibre attenuation. The near-term parameter values as well as the individual improvement functions for each parameter can be found in Supplementary Note 4. 

## _4. NV repeater chain protocols_ 

For the NV repeater chain, we simulated two protocols: swap-asap and nested-with-distill. Both protocols are composed of five building blocks: entgen, store, retrieve, distill and swap. By entgen, we denote the simulation of the entanglement generation protocol based on the description in the previous subsection: two nodes wait until a classical message signals that their respective electron spins hold an entangled pair. In reality, such functionality would be achieved by a link layer protocol [39]. store is the mapping of the electron spin state onto a free nuclear spin, and retrieve is the reverse operation. The distill block implements entanglement distillation between two remote NVs for probabilistically improving the quality of entanglement between two nuclear spins (one at each NV), at the cost of reading out entanglement between 

the two electron spins. It consists of local operations followed by classical communication to determine whether distillation succeeded. The entanglement swap (swap) converts two short-distance entangled qubit pairs _A − M_ and _M − B_ into a single long-distance one _A − B_ , where _A, B_ and _M_ are nodes. It consists of local operations at _M_ , including spin readout, and communicating the measurement outcomes to _A_ and _B_ , followed by _A_ and _B_ updating their knowledge of the precise state _A − B_ they hold in the perfect case. We opt for such tracking as opposed to applying a correction operator to bring _A − B_ back to a canonical state since the correction operator generally cannot be applied to the nuclear spins directly. Details of the tracking are given in Supplementary Note 6. The circuit implementations for the building blocks, “quantum programs" in NetSquid, are given in Supplementary Note 5. Let us explain the swap-asap and nested-withdistill protocols in spirit; the exact protocols run asynchronously on each node and can be found in Supplementary Note 5. In the swap-asap protocol, a repeater node performs entgen with both its neighbours, followed by swap as soon as it holds the two entangled pairs. Next, nested-with-distill is a nested protocol on 2<sup>_n_</sup> + 1 nodes (integer _n ≥_ 0) with distillation at each nesting level which is based on the BDCZ protocol [9]. For nesting level _n_ = 0, there are no repeaters and the two nodes only perform entgen once. For nesting level _n >_ 0, the chain is divided into a left part and a right part of 2<sup>_n−_1</sup> + 1 nodes, and the middle node (included in both parts) in the chain generates twice an entangled pair with the left end node following the ( _n −_ 1)-level protocol; store is applied in between to free the electron spin. Subsequently, distill is performed with the two pairs as input (restart if distillation fails), after which the same procedure is performed on the right. Once the right part has finished, the middle node performs swap to connect the end nodes. If needed, store and retrieve are applied prior to distill and swap in order achieve the desired configuration of qubits in the quantum processor, e.g. for distill to ensure that the two involved NVs hold an electron-electron and nuclearnuclear pair of qubits, instead of electron-nuclear for both entangled pairs. 

## **IV. DATA AVAILABILITY** 

The data presented in this paper have been made available at https://doi.org/10.34894/ URV169 [94]. 

## **V. CODE AVAILABILITY** 

The NetSquid-based simulation code that was used for the simulations in this paper has been made available at https://doi.org/10.34894/ DU3FTS [95]. 

16 

## **ACKNOWLEDGEMENTS** 

This work was supported by the Dutch Research Cooperation Funds (SMO), the European Research Council through a Starting Grant (S.W.), the QIA project (funded by European Union’s Horizon 2020, Grant Agreement No. 820445) and the Netherlands Organisation for Scientific Research (NWO/OCW), as part of the Quantum Software Consortium program (project number 024.003.037/3368). The authors would like to thank Francisco Ferreira da Silva, Wojciech Kozlowski and Gayane Vardoyan for critical reading of the manuscript. The authors would like to thank Gustavo Amaral, Guus Avis, Conor Bradley, Chris Elenbaas, Francisco Ferreira da Silva, Sophie Hermans, Roeland ter Hoeven, Hana Jirovská, Wojciech Kozlowski, Matteo Pompili, Arian Stolk and Gayane Vardoyan for useful discussions. 

## **AUTHOR CONTRIBUTIONS** 

T.C. realised the NV repeater chain and the quantum switch simulations. R.K., L.W. realised the benchmarking simulations. D.M., J.R. realised the atomic ensembles simulations. R.K. and J.O. designed NetSquid’s software architecture and R.K. led its software development. T.C, A.D, R.K., D.M., L.N., J.O., M.P., F.R, J.R., M.S., A.T., L.W., and S.W designed use case driven architectures, and contributed to the development of NetSquid and the modelling libraries used in the simulations. W.J., D.P., A.T. contributed to the optimal execution of simulations on computing clusters. T.C., D.E., R.K., D.M. and S.W. wrote the manuscript. All authors revised the manuscript. D.E. and S.W. conceived and supervised the project. 

## **COMPETING INTERESTS STATEMENT** 

The authors declare no competing interests. 

## **REFERENCES** 

- [1] R. Van Meter and S. J. Devitt, “The path to scalable distributed quantum computing,” Computer, vol. 49, no. 9, pp. 31–42, 2016. 

- [2] B. Lekitsch, S. Weidt, A. G. Fowler, K. Mølmer, S. J. Devitt, C. Wunderlich, and W. K. Hensinger, “Blueprint for a microwave trapped ion quantum computer,” Science Advances, vol. 3, no. 2, p. e1601540, 2017. 

- [3] C. Monroe, R. Raussendorf, A. Ruthven, K. R. Brown, P. Maunz, L.-M. Duan, and J. Kim, “Large-scale modular quantum-computer architecture with atomic memory and photonic interconnects,” Phys. Rev. A, vol. 89, p. 022317, Feb 2014. 

- [4] A. M. Stephens, Z. W. Evans, S. J. Devitt, A. D. Greentree, A. G. Fowler, W. J. Munro, J. L. 

O’Brien, K. Nemoto, and L. C. Hollenberg, “Deterministic optical quantum computer using photonic modules,” Physical Review A, vol. 78, no. 3, p. 032318, 2008. 

- [5] S. Wehner, D. Elkouss, and R. Hanson, “Quantum internet: A vision for the road ahead,” Science, vol. 362, no. 6412, 2018. 

- [6] W. J. Munro, K. Azuma, K. Tamaki, and K. Nemoto, “Inside quantum repeaters,” IEEE Journal of Selected Topics in <u>Quantum</u> Electronics, vol. 21, pp. 78–90, may 2015. 

- [7] S. Muralidharan, L. Li, J. Kim, N. Lütkenhaus, M. D. Lukin, and L. Jiang, “Optimal architectures for long distance quantum communication,” Scientific Reports, vol. 6, pp. 20463 EP –, Feb 2016. Article. 

- [8] N. Gisin and R. Thew, “Quantum communication,” Nature Photonics, vol. 1, pp. 165 EP –, Mar 2007. Review Article. 

- [9] H.-J. Briegel, W. Dür, J. I. Cirac, and P. Zoller, “Quantum repeaters: The role of imperfect local operations in quantum communication,” Phys. Rev. Lett., vol. 81, pp. 5932–5935, Dec 1998. 

- [10] W. Dür, H.-J. Briegel, J. I. Cirac, and P. Zoller, “Quantum repeaters based on entanglement purification,” Phys. Rev. A, vol. 59, pp. 169–181, Jan 1999. 

- [11] L.-M. Duan, M. D. Lukin, J. I. Cirac, and P. Zoller, “Long-distance quantum communication with atomic ensembles and linear optics,” Nature, vol. 414, pp. 413 EP –, Nov 2001. Article. 

- [12] J. Amirloo, M. Razavi, and A. H. Majedi, “Quantum key distribution over probabilistic quantum repeaters,” Phys. Rev. A, vol. 82, p. 032304, Sep 2010. 

- [13] F. Kimiaee Asadi, N. Lauk, S. Wein, N. Sinclair, C. O’Brien, and C. Simon, “Quantum repeaters with individual rare-earth ions at telecommunication wavelengths,” <u>Quantum,</u> vol. 2, p. 93, Sept. 2018. 

- [14] N. K. Bernardes, L. Praxmeyer, and P. van Loock, “Rate analysis for a hybrid quantum repeater,” Phys. Rev. A, vol. 83, p. 012323, Jan 2011. 

- [15] J. Borregaard, P. Kómár, E. M. Kessler, A. S. Sørensen, and M. D. Lukin, “Heralded quantum gates with integrated error detection in optical cavities,” Phys. Rev. Lett., vol. 114, p. 110502, Mar 2015. 

- [16] D. E. Bruschi, T. M. Barlow, M. Razavi, and A. Beige, “Repeat-until-success quantum repeaters,” Phys. Rev. A, vol. 90, p. 032306, Sep 2014. 

- [17] Z.-B. Chen, B. Zhao, Y.-A. Chen, J. Schmiedmayer, and J.-W. Pan, “Fault-tolerant quantum repeater with atomic ensembles and linear optics,” Phys. Rev. A, vol. 76, p. 022329, Aug 2007. 

- [18] O. A. Collins, S. D. Jenkins, A. Kuzmich, and T. A. B. Kennedy, “Multiplexed memoryinsensitive quantum repeaters,” Phys. Rev. Lett., vol. 98, p. 060502, Feb 2007. 

- [19] S. Guha, H. Krovi, C. A. Fuchs, Z. Dutton, J. A. Slater, C. Simon, and W. Tittel, “Rate-loss analysis of an efficient quantum repeater architecture,” Phys. Rev. A, vol. 92, p. 022357, Aug 2015. 

- [20] L. Hartmann, B. Kraus, H.-J. Briegel, and W. Dür, “Role of memory errors in quantum repeaters,” Phys. Rev. A, vol. 75, p. 032310, Mar 2007. 

17 

- [21] L. Jiang, J. M. Taylor, K. Nemoto, W. J. Munro, R. Van Meter, and M. D. Lukin, “Quantum repeater with encoding,” Phys. Rev. A, vol. 79, p. 032325, Mar 2009. 

- [22] K. Nemoto, M. Trupke, S. J. Devitt, B. Scharfenberger, K. Buczak, J. Schmiedmayer, and W. J. Munro, “Photonic quantum networks formed from NV- centers,” Scientific Reports, vol. 6, pp. 26284 EP –, May 2016. Article. 

- [23] M. Razavi, M. Piani, and N. Lütkenhaus, “Quantum repeaters with imperfect memories: Cost and scalability,” Phys. Rev. A, vol. 80, p. 032301, Sep 2009. 

- [24] M. Razavi and J. H. Shapiro, “Long-distance quantum communication with neutral atoms,” Phys. Rev. A, vol. 73, p. 042303, Apr 2006. 

- [25] C. Simon, H. de Riedmatten, M. Afzelius, N. Sangouard, H. Zbinden, and N. Gisin, “Quantum repeaters with photon pair sources and multimode memories,” Phys. Rev. Lett., vol. 98, p. 190503, May 2007. 

- [26] S. E. Vinay and P. Kok, “Practical repeaters for ultralong-distance quantum communication,” Phys. Rev. A, vol. 95, p. 052336, May 2017. 

- [27] Y. Wu, J. Liu, and C. Simon, “Near-term performance of quantum repeaters with imperfect ensemble-based quantum memories,” Phys. Rev. A, vol. 101, p. 042301, Apr 2020. 

- [28] N. Sangouard, C. Simon, J. c. v. Minář, H. Zbinden, H. de Riedmatten, and N. Gisin, “Long-distance entanglement distribution with single-photon sources,” Phys. Rev. A, vol. 76, p. 050301, Nov 2007. 

- [29] N. Sangouard, C. Simon, B. Zhao, Y.-A. Chen, H. de Riedmatten, J.-W. Pan, and N. Gisin, “Robust and efficient quantum repeaters with atomic ensembles and linear optics,” Phys. Rev. A, vol. 77, p. 062301, Jun 2008. 

- [30] N. Sangouard, R. Dubessy, and C. Simon, “Quantum repeaters based on single trapped ions,” Phys. Rev. A, vol. 79, p. 042340, Apr 2009. 

- [31] S. Abruzzo, S. Bratzik, N. K. Bernardes, H. Kampermann, P. van Loock, and D. Bruß, “Quantum repeaters and quantum key distribution: Analysis of secret-key rates,” Phys. Rev. A, vol. 87, p. 052315, May 2013. 

- [32] J. B. Brask and A. S. Sørensen, “Memory imperfections in atomic-ensemble-based quantum repeaters,” Phys. Rev. A, vol. 78, p. 012350, Jul 2008. 

- [33] S. Muralidharan, J. Kim, N. Lütkenhaus, M. D. Lukin, and L. Jiang, “Ultrafast and fault-tolerant quantum communication across long distances,” Phys. Rev. Lett., vol. 112, p. 250501, Jun 2014. 

- [34] M. Pant, H. Krovi, D. Englund, and S. Guha, “Rate-distance tradeoff and resource costs for alloptical quantum repeaters,” Phys. Rev. A, vol. 95, p. 012304, Jan 2017. 

- [35] T. D. Ladd, P. van Loock, K. Nemoto, W. J. Munro, and Y. Yamamoto, “Hybrid quantum repeater based on dispersive CQED interactions between matter qubits and bright coherent light,” New Journal of Physics, vol. 8, pp. 184–184, sep 2006. 

- [36] P. van Loock, T. D. Ladd, K. Sanaka, F. Yamaguchi, K. Nemoto, W. J. Munro, and Y. Yamamoto, “Hybrid quantum repeater using bright coherent light,” Phys. Rev. Lett., vol. 96, 

   - p. 240501, Jun 2006. 

- [37] M. Zwerger, B. Lanyon, T. Northup, C. Muschik, W. Dür, and N. Sangouard, “Quantum repeaters based on trapped ions with decoherencefree subspace encoding,” <u>Quantum</u> Science and Technology, vol. 2, no. 4, p. 044001, 2017. 

- [38] L. Jiang, J. M. Taylor, and M. D. Lukin, “Fast and robust approach to long-distance quantum communication with atomic ensembles,” Phys. Rev. A, vol. 76, p. 012301, Jul 2007. 

- [39] A. Dahlberg, M. Skrzypczyk, T. Coopmans, L. Wubben, F. Rozpędek, M. Pompili, A. Stolk, P. Pawełczak, R. Knegjens, J. de Oliveira Filho, R. Hanson, and S. Wehner, “A link layer protocol for quantum networks,” in Proceedings of the ACM Special Interest Group on Data Communication, SIGCOMM ’19, (New York, NY, USA), pp. 159– 

   - 173, Association for Computing Machinery, 2019. 

- [40] R. V. Meter, “Quantum networking and internetworking,” IEEE Network, vol. 26, no. 4, pp. 59–64, 2012. 

- [41] L. Aparicio, R. Van Meter, and H. Esaki, “Protocol design for quantum repeater networks,” in Proceedings of the 7th Asian Internet Engineering Conference, AINTEC ’11, (New York, NY, USA), pp. 73–80, Association for Computing Machinery, 2011. 

- [42] R. V. Meter and J. Touch, “Designing quantum repeater networks,” IEEE Communications Magazine, vol. 51, pp. 64–71, August 2013. 

- [43] R. V. Meter, T. D. Ladd, W. J. Munro, and K. Nemoto, “System design for a long-line quantum repeater,” IEEE/ACM Transactions on Networking, vol. 17, pp. 1002–1013, June 2009. 

- [44] A. Pirker and W. Dür, “A quantum network stack and protocols for reliable entanglement-based networks,” New Journal of Physics, vol. 21, p. 033003, mar 2019. 

- [45] A. Acín, N. Brunner, N. Gisin, S. Massar, S. Pironio, and V. Scarani, “Device-independent security of quantum cryptography against collective attacks,” Phys. Rev. Lett., vol. 98, p. 230501, Jun 2007. 

- [46] C. Branciard, E. G. Cavalcanti, S. P. Walborn, V. Scarani, and H. M. Wiseman, “One-sided device-independent quantum key distribution: Security, feasibility, and the connection with steering,” Phys. Rev. A, vol. 85, p. 010301, Jan 2012. 

- [47] V. Scarani, H. Bechmann-Pasquinucci, N. J. Cerf, M. Dušek, N. Lütkenhaus, and M. Peev, “The security of practical quantum key distribution,” Rev. Mod. Phys., vol. 81, pp. 1301–1350, Sep 2009. 

- [48] F. Xu, X. Ma, Q. Zhang, H.-K. Lo, and J.-W. Pan, “Secure quantum key distribution with realistic devices,” Rev. Mod. Phys., vol. 92, p. 025002, May 2020. 

- [49] S. Pirandola, U. L. Andersen, L. Banchi, M. Berta, D. Bunandar, R. Colbeck, D. Englund, T. Gehring, C. Lupo, C. Ottaviani, et al., “Advances in quantum cryptography,” Advances in Optics and Photonics, vol. 12, no. 4, pp. 1012–1236, 2020. 

- [50] S. Barz, E. Kashefi, A. Broadbent, J. F. Fitzsimons, A. Zeilinger, and P. Walther, “Demonstration of blind quantum computing,” Science, vol. 335, no. 6066, pp. 303–308, 2012. 

- [51] N. H. Nickerson, J. F. Fitzsimons, and S. C. Benjamin, “Freely scalable quantum technologies using cells of 5-to-50 qubits with very lossy and noisy 

18 

photonic links,” Phys. Rev. X, vol. 4, p. 041041, Dec 2014. 

- [52] V. Lipinska, G. Murta, and S. Wehner, “Anonymous transmission in a noisy quantum network using the _w_ state,” Phys. Rev. A, vol. 98, p. 052320, Nov 2018. 

- [53] E. T. Khabiboulline, J. Borregaard, K. De Greve, and M. D. Lukin, “Optical interferometry with quantum networks,” Phys. Rev. Lett., vol. 123, p. 070504, Aug 2019. 

- [54] E. Shchukin, F. Schmidt, and P. van Loock, “Waiting time in quantum repeaters with probabilistic entanglement swapping,” Phys. Rev. A, vol. 100, p. 032322, Sep 2019. 

- [55] S. E. Vinay and P. Kok, “Statistical analysis of quantum-entangled-network generation,” Phys. Rev. A, vol. 99, p. 042313, Apr 2019. 

- [56] G. Vardoyan, S. Guha, P. Nain, and D. Towsley, “On the stochastic analysis of a quantum entanglement switch,” SIGMETRICS Perform. Eval. Rev., vol. 47, pp. 27–29, Dec. 2019. 

- [57] M. Razavi, K. Thompson, H. Farmanbar, M. Piani, and N. Lütkenhaus, “Physical and architectural considerations in quantum repeaters,” in <u>Quantum</u> Communications Realized II (Y. Arakawa, M. Sasaki, and H. Sotobayashi, eds.), vol. 7236, pp. 18 – 30, International Society for Optics and Photonics, SPIE, 2009. 

- [58] M. M. Wilde, <u>Quantum</u> information theory. Cambridge University Press, 2013. 

- [59] M. Pant, H. Krovi, D. Towsley, L. Tassiulas, L. Jiang, P. Basu, D. Englund, and S. Guha, “Routing entanglement in the quantum internet,” npj <u>Quantum</u> Information, vol. 5, p. 25, Mar 2019. 

- [60] V. Kuzmin, D. Vasilyev, N. Sangouard, W. Dür, and C. Muschik, “Scalable repeater architectures for multi-party states,” npj <u>Quantum</u> Information, vol. 5, no. 1, pp. 1–6, 2019. 

- [61] S. Khatri, C. T. Matyas, A. U. Siddiqui, and J. P. Dowling, “Practical figures of merit and thresholds for entanglement distribution in quantum networks,” Phys. Rev. Research, vol. 1, p. 023032, Sep 2019. 

- [62] A. Varga, “The OMNeT++ discrete event simulation system,” in Proc. of the European Simulation Multiconference <u>(ESM’2001),</u> 2001. 

- [63] G. F. Riley and T. R. Henderson, The ns-3 Network Simulator, pp. 15–34. Berlin, Heidelberg: Springer Berlin Heidelberg, 2010. 

- [64] B. Lantz, B. Heller, and N. McKeown, “A network in a laptop: rapid prototyping for softwaredefined networks,” in Proceedings of the 9th ACM SIGCOMM Workshop on Hot Topics in Networks, pp. 1–6, 2010. 

- [65] M. Fingerhuth, T. Babej, and P. Wittek, “Open source software in quantum computing,” PLOS ONE, vol. 13, p. e0208561, dec 2018. 

- [66] “Netsquid website and online documentation.” https://netsquid.org. Access to documentation requires registration. 

- [67] D. Deutsch, A. Ekert, R. Jozsa, C. Macchiavello, S. Popescu, and A. Sanpera, “Quantum privacy amplification and the security of quantum cryptography over noisy channels,” Physical review letters, vol. 77, no. 13, p. 2818, 1996. 

- [68] K. Wehrle, M. Günes, and J. Gross, Modeling and tools for network simulation. Springer Science & Business Media, 2010. 

- [69] D. M. Greenberger, M. A. Horne, and A. Zeilinger, “Going beyond Bell’s theorem,” in Bell’s theorem, <u>quantum</u> theory and conceptions of the universe, pp. 69–72, Springer, 1989. 

- [70] D. D. Awschalom, R. Hanson, J. Wrachtrup, and B. B. Zhou, “Quantum technologies with optically interfaced solid-state spins,” Nature Photonics, vol. 12, no. 9, pp. 516–527, 2018. 

- [71] M. W. Doherty, N. B. Manson, P. Delaney, F. Jelezko, J. Wrachtrup, and L. C. Hollenberg, “The nitrogen-vacancy colour centre in diamond,” Physics Reports, vol. 528, pp. 1–45, jul 2013. 

- [72] M. Afzelius, C. Simon, H. De Riedmatten, and N. Gisin, “Multimode quantum memory based on atomic frequency combs,” Physical Review A, vol. 79, no. 5, p. 052329, 2009. 

- [73] M. Fleischhauer, A. Imamoglu, and J. P. Marangos, “Electromagnetically induced transparency: Optics in coherent media,” Reviews of modern <u>physics,</u> vol. 77, no. 2, p. 633, 2005. 

- [74] M. Lukin, “Colloquium: Trapping and manipulating photon states in atomic ensembles,” Reviews of Modern Physics, vol. 75, no. 2, p. 457, 2003. 

- [75] H. Krovi, S. Guha, Z. Dutton, J. A. Slater, C. Simon, and W. Tittel, “Practical Quantum Repeaters with Parametric Down-Conversion Sources,” Applied Physics B, vol. 122, p. 52, Mar. 2016. 

- [76] C. H. Bennett and G. Brassard, “Quantum cryptography: Public key distribution and coin tossing,” Theoretical Computer Science, vol. 560, pp. 7–11, Dec. 2014. 

- [77] S. Aaronson and D. Gottesman, “Improved simulation of stabilizer circuits,” Physical Review A, vol. 70, no. 5, p. 052328, 2004. 

- [78] S. Anders and H. J. Briegel, “Fast simulation of stabilizer circuits using a graph-state representation,” Physical Review A, vol. 73, no. 2, p. 022334, 2006. 

- [79] D. S. Steiger, T. Häner, and M. Troyer, “ProjectQ: an open source software framework for quantum computing,” <u>Quantum,</u> vol. 2, p. 49, 2018. 

- [80] J. de Oliveira Filho, Z. Papp, R. Djapic, and J. Oosteveen, “Model-based design of selfadapting networked signal processing systems,” in 2013 IEEE 7th International Conference on Self-Adaptive and Self-Organizing Systems, pp. 41–50, IEEE, 2013. 

- [81] A. Dahlberg and S. Wehner, “SimulaQron – a simulator for developing quantum internet software,” <u>Quantum</u> Science and Technology, vol. 4, no. 1, p. 015001, 2018. 

- [82] S. DiAdamo, J. Nötzel, B. Zanger, and M. M. Beşe, “QuNetSim: A software framework for quantum networks,” arXiv:2003.06397, 2020. 

- [83] B. Bartlett, “A distributed simulation framework for quantum networks and channels,” arXiv:quant-ph/1808.07047, 2018. 

- [84] T. Matsuo, “Simulation of a dynamic, RuleSetbased quantum network,” arXiv:1908.10758, 2020. 

- [85] L. O. Mailloux, J. D. Morris, M. R. Grimaila, D. D. Hodson, D. R. Jacques, J. M. Colombi, C. V. Mclaughlin, and J. A. Holes, “A modeling framework for studying quantum key distribution system implementation nonidealities,” IEEE Access, vol. 3, pp. 110–130, 2015. 

- [86] X. Wu, A. Kolar, J. Chung, D. Jin, T. Zhong, R. Kettimuthu, and M. Suchara, “SeQUeNCe: A 

19 

customizable discrete-event simulator of quantum networks,” arXiv:2009.12000, 2020. 

- [87] Y. Lee, E. Bersin, A. Dahlberg, S. Wehner, and D. Englund, “A quantum router architecture for high-fidelity entanglement flows in multi-user quantum networks,” arXiv:2005.01852, 2020. 

- [88] W. Kozlowski, A. Dahlberg, and S. Wehner, “Designing a quantum network protocol,” in Proceedings of the 16th International Conference on emerging Networking EXperiments and Technologies <u>(CoNEXT</u> ’20), p. 16, ACM, 2020. 

- [89] S. Behnel, R. Bradshaw, C. Citro, L. Dalcin, D. S. Seljebotn, and K. Smith, “Cython: The best of both worlds,” Computing in Science & Engineering, vol. 13, no. 2, pp. 31–39, 2011. 

- [90] K. De Raedt, K. Michielsen, H. De Raedt, B. Trieu, G. Arnold, M. Richter, T. Lippert, H. Watanabe, and N. Ito, “Massively parallel quantum computer simulator,” Computer Physics Communications, vol. 176, no. 2, pp. 121 – 136, 2007. 

- [91] T. Häner and D. S. Steiger, “0.5 petabyte simulation of a 45-qubit quantum circuit,” in Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, SC ’17, (New York, NY, USA), Association for Computing Machinery, 2017. 

- [92] F. Rozpędek, R. Yehia, K. Goodenough, M. Ruf, P. C. Humphreys, R. Hanson, S. Wehner, and D. Elkouss, “Near-term quantum repeater experiments with NV centers: overcoming the limitations of direct transmission,” Physical Review A, vol. 99, no. 5, p. 052330, 2019. 

- [93] P. C. Humphreys, N. Kalb, J. P. J. Morits, R. N. Schouten, R. F. L. Vermeulen, D. J. Twitchen, M. Markham, and R. Hanson, “Deterministic delivery of remote entanglement on a quantum network,” Nature, vol. 558, no. 7709, pp. 268–273, 2018. 

- [94] T. Coopmans, R. Knegjens, A. Dahlberg, D. Maier, L. Nijsten, J. Oliveira, M. Papendrecht, J. Rabbie, F. Rozpędek, M. Skrzypczyk, L. Wubben, W. de Jong, D. Podareanu, A. Torres Knoop, D. Elkouss, and S. Wehner, “Replication Data for: NetSquid, a discrete-event simulation platform for quantum networks,” 2021. 

- [95] T. Coopmans, R. Knegjens, A. Dahlberg, D. Maier, L. Nijsten, J. Oliveira, M. Papendrecht, J. Rabbie, F. Rozpędek, M. Skrzypczyk, L. Wubben, W. de Jong, D. Podareanu, A. Torres Knoop, D. Elkouss, and S. Wehner, “Simulation Code for: NetSquid, a discrete-event simulation platform for quantum networks,” 2021. 

- [96] D. Gottesman, “The Heisenberg representation of quantum computers,” arXiv:quant-ph/9807006v1, 1998. 

- [97] M. A. Nielsen and I. L. Chuang, “Quantum information and quantum computation,” Cambridge: Cambridge University Press, vol. 2, no. 8, p. 23, 2000. 

- [98] M. Hein, W. Dür, J. Eisert, R. Raussendorf, M. Nest, and H.-J. Briegel, “Entanglement in graph states and its applications,” arXiv:0602096, 2006. 

- [99] S. Hermans. Personal communication, 2020. 

- [100] R. Paschotta, “‘Refractive Index’ in _RP Photonics Encyclopedia_ ,” 2020. 

- [101] D. Riedel, I. Söllner, B. J. Shields, S. Starosielec, P. Appel, E. Neu, P. Maletinsky, and R. J. Warburton, “Deterministic enhancement of coherent photon generation from a nitrogen-vacancy center in ultrapure diamond,” Phys. Rev. X, vol. 7, p. 031040, Sep 2017. 

- [102] B. Hensen, H. Bernien, A. E. Dréau, A. Reiserer, N. Kalb, M. S. Blok, J. Ruitenberg, R. F. L. Vermeulen, R. N. Schouten, C. Abellán, W. Amaya, V. Pruneri, M. W. Mitchell, M. Markham, D. J. Twitchen, D. Elkouss, S. Wehner, T. H. Taminiau, and R. Hanson, “Loophole-free bell inequality violation using electron spins separated by 1.3 kilometres,” Nature, vol. 526, pp. 682 EP –, Oct 2015. 

- [103] S. Zaske, A. Lenhard, C. A. Keßler, J. Kettler, C. Hepp, C. Arend, R. Albrecht, W.-M. Schulz, M. Jetter, P. Michler, and C. Becher, “Visibleto-telecom quantum frequency conversion of light from a single quantum emitter,” Phys. Rev. Lett., vol. 109, p. 147404, Oct 2012. 

- [104] N. Kalb, A. A. Reiserer, P. C. Humphreys, J. J. W. Bakermans, S. J. Kamerling, N. H. Nickerson, S. C. Benjamin, D. J. Twitchen, M. Markham, and R. Hanson, “Entanglement distillation between solid-state quantum network nodes,” Science, vol. 356, pp. 928–932, jun 2017. 

- [105] N. Kalb, P. C. Humphreys, J. J. Slim, and R. Hanson, “Dephasing mechanisms of diamond-based nuclear-spin memories for quantum networks,” Phys. Rev. A, vol. 97, p. 062330, Jun 2018. 

- [106] H. Beukers, “Improving coherence of quantum memory during entanglement creation between nitrogen vacancy centres in diamond (master thesis),” 2019. 

- [107] M. H. Abobeih, J. Cramer, M. A. Bakker, N. Kalb, M. Markham, D. J. Twitchen, and T. H. Taminiau, “One-second coherence for a single electron spin coupled to a multi-qubit nuclear-spin environment,” Nature Communications, vol. 9, p. 2552, Jun 2018. 

- [108] C. E. Bradley, J. Randall, M. H. Abobeih, R. C. Berrevoets, M. J. Degen, M. A. Bakker, M. Markham, D. J. Twitchen, and T. H. Taminiau, “A ten-qubit solid-state spin register with quantum memory up to one minute,” Phys. Rev. X, vol. 9, p. 031045, Sep 2019. 

- [109] A. Reiserer, N. Kalb, M. S. Blok, K. J. M. van Bemmelen, T. H. Taminiau, R. Hanson, D. J. Twitchen, and M. Markham, “Robust quantumnetwork memory using decoherence-protected subspaces of nuclear spins,” Phys. Rev. X, vol. 6, p. 021040, Jun 2016. 

- [110] T. H. Taminiau, J. Cramer, T. van der Sar, V. V. Dobrovitski, and R. Hanson, “Universal control and error correction in multi-qubit spin registers in diamond,” Nature Nanotechnology, vol. 9, pp. 171– 176, feb 2014. 

- [111] C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, “Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels,” Phys. Rev. Lett., vol. 70, pp. 1895–1899, Mar 1993. 

- [112] D.Maier 2020. In preparation. 

- [113] N. Sinclair, E. Saglamyurek, H. Mallahzadeh, J. A. Slater, M. George, R. Ricken, M. P. Hedges, D. Oblak, C. Simon, W. Sohler, and W. Tittel, “Spectral Multiplexing for Scalable Quantum Photonics using an Atomic Frequency Comb Quan- 

20 

   - tum Memory and Feed-Forward Control,” Physical Review Letters, vol. 113, p. 053603, July 2014. 

- [114] N. Sangouard, C. Simon, H. de Riedmatten, and N. Gisin, “Quantum repeaters based on atomic ensembles and linear optics,” Rev. Mod. Phys., vol. 83, pp. 33–80, Mar 2011. 

- [115] J. S. Ivan, K. K. Sabapathy, and R. Simon, “Operator-sum representation for bosonic gaussian channels,” Phys. Rev. A, vol. 84, p. 042311, Oct 2011. 

- [116] I. L. Chuang, D. W. Leung, and Y. Yamamoto, “Bosonic quantum codes for amplitude damping,” Physical Review A, vol. 56, pp. 1114–1125, Aug. 1997. 

- [117] R. H. Dicke, “Coherence in spontaneous radiation processes,” Phys. Rev., vol. 93, pp. 99–110, Jan 1954. 

- [118] M. Sabooni, Q. Li, S. Kröll, and L. Rippe, “Efficient quantum memory using a weakly absorbing sample,” Physical Review Letters, vol. 110, Mar 2013. 

- [119] A. Seri, D. Lago-Rivera, A. Lenhard, G. Corrielli, R. Osellame, M. Mazzera, and H. de Riedmatten, “Quantum storage of frequency-multiplexed heralded single photons,” Phys. Rev. Lett., vol. 123, p. 080502, Aug 2019. 

- [120] P. Jobez, N. Timoney, C. Laplane, J. Etesse, A. Ferrier, P. Goldner, N. Gisin, and M. Afzelius, “Towards highly multimode optical quantum memory for quantum repeaters,” Phys. Rev. A, vol. 93, p. 032327, Mar 2016. 

- [121] A. Holzäpfel, J. Etesse, K. T. Kaczmarek, A. Tiranov, N. Gisin, and M. Afzelius, “Optical storage for 0.53 s in a solid-state atomic frequency comb memory using dynamical decoupling,” New Journal of Physics, vol. 22, p. 063009, Jun 2020. 

- [122] M. Bonarota, J.-L. Le Gouët, and T. Chanelière, “Highly multimode storage in a crystal,” New Journal of Physics, vol. 13, p. 013013, Jan 2011. 

- [123] S. E. Harris, J. E. Field, and A. Imamoğlu, “Nonlinear optical processes using electromagnetically induced transparency,” Phys. Rev. Lett., vol. 64, pp. 1107–1110, Mar 1990. 

- [124] M. Cao, F. Hoffet, S. Qiu, A. S. Sheremet, and J. Laurat, “Efficient reversible entanglement transfer between light and quantum memories,” arXiv:2007.00022, June 2020. 

- [125] P. Vernaz-Gris, K. Huang, M. Cao, A. S. Sheremet, and J. Laurat, “Highly-efficient quantum memory for polarization qubits in a spatially-multiplexed cold atomic ensemble,” Nature Communications, vol. 9, p. 363, Jan. 2018. 

## **Supplementary Note 1: Anatomy of the NetSquid Simulator** 

This section supplements the Methods, section Design and functionality of NetSquid, by going into more depth on specific details of NetSquid’s design. The version of NetSquid that we consider is 0.10. For up-todate documentation of the latest NetSquid version, including a detailed user tutorial, code examples, and its application programming interface, please visit the NetSquid website: https://netsquid.org [66]. 

## **A. Qubits and their quantum state formalisms** 

The _qubits_ sub-package of NetSquid, shown in Figure 10 (main text), provides a specialised quantum computation library for tracking the lifetimes of many qubits across a quantum network. A class diagram of the main classes present in this sub-package is shown in in Supplementary Figure 11. Rather than assigning a single quantum state for a predefined number of qubits, both the number of qubits and the quantum states describing them are managed dynamically during a simulation run. Every _Qubit_ (Qubit) object references a _shared quantum state_ (QState) object, which varies in size according to the number of qubits sharing it. When two or more qubits interact, for instance via a multi-qubit operation, their respective shared quantum states are merged together. On the other hand, when a qubit is projectively measured or discarded it can be split from the quantum state it’s sharing and optionally be assigned a new single-qubit state. 

The QState class is an interface for shared quantum states that NetSquid implements for four different _quantum state formalisms_ – described in more detail below. To allow simulations to seamlessly switch between formalisms NetSquid offers a formalism agnostic API, which is defined in the _qubitapi_ module. The functions in this API take as their primary input parameters the qubits to manipulate and the _operators_ (Operator) describing a quantum operation to perform, if applicable. The merging and splitting of shared quantum states is handled automatically under the hood, as are conversions between states using different formalisms (where this is possible). This allows users to program in a “qubit-centric” way, by for instance applying local operations to qubits at a network node without knowledge of their positions within a quantum state representation or any entanglement they may have across the network. 

We proceed to give a high-level description of the available quantum state formalisms. The first two formalisms are ket state vectors (KET) and density matrices (DM), which both enable universal quantum computation. A ket state vector represents a quantum pure state, while a density matrix can represent statistical ensembles of pure states. The stabiliser formalism (STAB) [77, 96] and graph states with local Cliffords formalisms (GSLC) [78] can only represent stabiliser states. Stabiliser states form a subset of all quantum states that are closed under the application of: 

- _Clifford gates_ . Each Clifford gate can be written as circuit consisting of the following three gates only: 

21 



<!-- Start of picture text -->
DMState<br>Density matrix<br>representation<br>qubitapi Qubit +dm: array<br>Module with functions that A quantum bit ...<br>manipulate qubits +name: str<br>create_qubits()operate() ◄ parameter +qstate: QState+is_number_state: bool+combine(other_qubit: Qubit) Class interface for a quantum stateshared by qubits. QState Ket vector KetState<br>stochastic_operate()multi_operate()measure()gmeasure() +indices: dict+qubits: list of Qubit+num_qubits: int +ket: array... representation<br>discard() Operator ...<br>reduced_dm() A quantum operator +operate_qubits(...)<br>fidelity()exp_value()apply_pauli_noise()depolarize()dephase()amplitude_dampen()apply_dda_noise()delay_depolarize() ◄ parameter +name: str+description: str+num_qubits: int+ctrl: Operator+inv: Operator+conj: Operator... transforms ► +measure_qubit(...)+fidelity(...)+reduce_dm(qubits: list of Qubit)+drop_qubit(qubit: Qubit)+combine_qstate(other_qstate: QState)... +stabiliser: Stabilizer... Stabiliser tableaurepresentation StabState<br>... +projectors(): list of Operator GSLCState<br>... Graph state with local<br>Cliffords representation<br>...<br>...<br><!-- End of picture text -->

Figure 11: **Design overview of NetSquid’s qubits sub-package.** The main classes and module of the _netsquid.qubits_ sub-package. Qubit objects can be manipulated, as described for instance by Operator objects, using the functions of the _qubitapi_ module. Under the hood the qubits share a specific sub-class of the QState interface. Ellipses indicate that not all of a class’s public variables and methods are listed. 

||Density|Ket state|Stabiliser|Graph state with|
|---|---|---|---|---|
||Matrix (DM)|vector (KET)|tableau (STAB)|local Clifords (GSLC)|
|Is universal|Yes|Yes|No<sup>a</sup>|No<sup>a</sup>|
|Supports mixed states|Yes|No|No|No|
|Memory (bits)|128_×_2<sup>2</sup><sup>_n_</sup>|128_×_2<sup>_n_</sup>|2_n_<sup>2 </sup>+_n_|_O_(_nd_+_n_)|
|||||Single qubit gates: _O_(1)|
|Operating complexity|_O_(2<sup>3</sup><sup>_n_</sup>)<sup>b</sup>|_O_(2<sup>2</sup><sup>_n_</sup>)<sup>b</sup>|_O_(_n_)|Two-qubit gates: _O_(_d_<sup>2 </sup>+ 1)|
|Measurement complexity|_O_(2<sup>3</sup><sup>_n_</sup>)<sup>b</sup>|_O_(2<sup>2</sup><sup>_n_</sup>)<sup>b</sup>|_O_(_n_<sup>3</sup>)|_O_(_d_<sup>2 </sup>+ 1)|



> a Can only represent stabiliser states. The only operators that can operate on these states are Clifford operators. 

> b A stricter upper bound exists, depending on the matrix multiplication implementation. 

Supplementary Table I: **The four different quantum state formalisms implemented in NetSquid.** Where _n_ is the amount of qubits in the quantum states and _d_ is the average amount of edges per vertex in the GSLC formalism with 0 _≤ d < n_ . 

the Hadamard gate _H_ (eq. (52)), the phase gate _|_ 0 _⟩⟨_ 0 _|_ + _i |_ 1 _⟩⟨_ 1 _|_ and the CNOT gate _|_ 00 _⟩⟨_ 00 _|_ + _|_ 01 _⟩⟨_ 01 _|_ + _|_ 10 _⟩⟨_ 01 _|_ + _|_ 01 _⟩⟨_ 10 _|_ . Not all unitaries are Clifford gates; 

- single-qubit measurements in the standard ( _|_ 0 _⟩ , |_ 1 _⟩_ ) basis. 

As such, for the STAB and GSLC formalisms quantum operations are limited to these two procedures. The runtime complexity trade-off between GSLC and STAB is nontrivial, since the former is faster on singlequbit unitaries, where the latter outperforms in two-qubit gates. An overview of the four formalisms and their runtime complexities can be found in Supplementary Table I. 

Now, let us describe for each of the formalisms how a quantum state is represented. An example of the different representations of the same quantum state is given in Fig. 12. 

## _Ket vectors (KET)_ 

In the KET formalism, an _n_ -qubit pure state _|ψ⟩_ =<sup>�2</sup> _k_<sup>_n_</sup> =1<sup>_ck |k⟩_is stored as a vector of length 2</sup><sup>_n_containing</sup> the complex amplitudes _ck_ . Here, _|k⟩_ denotes the product state of the binary representation of _k_ , e.g. _|_ 5 _⟩_ = _|_ 1 _⟩⊗|_ 0 _⟩⊗|_ 1 _⟩_ . 

## _Density matrices (DM)_ 

The density matrix of a pure state _|ψ⟩_ is _|ψ⟩⟨ψ|_ = _|ψ⟩·_ ( _|ψ⟩_ )<sup>_†_</sup> , where _·_ denotes matrix multiplication and ( _._ )<sup>_†_</sup> refers to complex transposition. An _n_ -qubit mixed state is a statistical ensemble of _n_ -qubit pure states and 

22 



<!-- Start of picture text -->
21 41 − 1 4 0 0 0 0 − 4 1 i 14 i<br> − 1 2   − 1 4 14 0 0 0 0 14 i − 1 4 i <br> 0   0 0 0 0 0 0 0 0 <br>   <br> 0   0 0 0 0 0 0 0 0 <br>  ρ  =  <br> 0   0 0 0 0 0 0 0 0 <br>   <br> 0   0 0 0 0 0 0 0 0 <br> 1   1 − 1 0 0 0 0 1 − 1 <br>2 i 4 i 4 i 4 4<br> − 1 2 i   − 1 4 i 14 i 0 0 0 0 − 1 4 14 <br>(a) Ket vector (b) Density matrix<br>{Y ⊗ X ⊗ I, Z ⊗ Z ⊗ I, −I ⊗ I ⊗ X}<br>S H | + ⟩ • S<br>1 1 0 1 0 0 0<br>=<br>=  0 0 0 1 1 0 0  | + ⟩ • H<br>0 0 1 0 0 0 1 Z<br> <br>| + ⟩ Z<br>(c) Stabiliser tableau (d) Graph state with local Cliffords<br><!-- End of picture text -->

Figure 12: **Quantum state representations available in NetSquid.** Four different representations of the same quantum state _|ψ⟩_ = _~~√~~_ <u>12</u><sup>(</sup><sup>_|_00</sup><sup>_⟩_+</sup><sup>_i |_11</sup><sup>_⟩_)</sup><sup>_|−⟩_.EachrepresentationtypeissupportedbyNetSquid</sup> and has different trade-offs (see text of section 1 A in Supplementary Note 1). 

can be represented as 



where _|ψ_ 1 _⟩ , . . . , |ψm⟩_ are _n_ -qubit pure states (with 1 _≤ m ≤ n_ ) and the _pk_ are probabilities that sum to 1. In DM, the density matrix of a pure or mixed state is represented as a matrix of dimension 2<sup>_n_</sup> _×_ 2<sup>_n_</sup> with complex entries. 

## _Stabiliser tableaus (STAB)_ 

In the stabiliser formalism [96], one tracks the generators of the stabiliser group of a state. We briefly explain the concept here; for a more accessible introduction to the topic, we refer to [97]. In order to define a stabiliser group, let us give the Pauli group, which consists of strings of Pauli operators with multiplicative phases _±_ 1 _, ±i_ : 



A stabiliser group is a subgroup of the Pauli group which is commutative (i.e. any two elements _A_ and _B_ satisfy _A · B_ = _B · A_ ) and moreover does not contain the element _−_ 112 _⊗_ 112 _⊗· · · ⊗_ 112. In case the stabiliser group contains 2<sup>_n_</sup> elements, there is a unique quantum state _|ψ⟩_ for which each element _A_ from the stabiliser group stabilises _|ψ⟩_ , i.e. _A |ψ⟩_ = _|ψ⟩_ . Not all quantum states have such a corresponding stabiliser group; those that do are called stabiliser states. The intuition behind the stabiliser state formalism is that one tracks how the stabiliser group is altered by Clifford operations and _|_ 0 _⟩ / |_ 1 _⟩_ -basis measurements. Since the stabiliser state belonging to a stabiliser group is unique, one could in principle always convert the group back to any other formalism, such as KET. Concrete examples of stabiliser groups and their corresponding stabiliser states are: 

- the stabiliser group _{_ 112 _, Z}_ , which corresponds to the state _|_ 0 _⟩_ ; 

- the stabiliser group _{_ 112 _⊗_ 112 _,_ 112 _⊗ Z, Z ⊗_ 112 _, Z ⊗ Z}_ , which corresponds to the state _|_ 0 _⟩⊗|_ 0 _⟩_ ; 

- the stabiliser group _{_ 112 _⊗_ 112 _, X ⊗ X, Z ⊗ Z, −Y ⊗ Y }_ , which corresponds to the state ( _|_ 00 _⟩_ + _|_ 11 _⟩_ ) _/√_ 2 _._ 

Rather than tracking the entire 2<sup>_n_</sup> -sized stabiliser group, it suffices to track a generating set, i.e. a set of _n_ Pauli strings whose 2<sup>_n_</sup> product combinations yield precisely the 2<sup>_n_</sup> elements of the stabiliser group. The choice of generators is not unique. For the examples given above, example sets of stabiliser generators are: 

- for _|_ 0 _⟩_ , the stabiliser group is generated by the single element _Z_ , since _Z_<sup>2</sup> = 112 

23 

- for _|_ 00 _⟩_ , the stabiliser group is generated by _{Z ⊗_ 112 _,_ 112 _⊗ Z}_ , since squaring any of these two yields 112 _⊗_ 112, while multiplying them yields _Z ⊗ Z_ ; 

- for the state ( _|_ 00 _⟩_ + _|_ 11 _⟩_ ) _/√_ 2, one possible set of of generators is _{X ⊗ X, Z ⊗ Z}_ . 

In NetSquid we store generators as a stabiliser tableau: 



The _k_ -th generator corresponds to the _k_ -th row of this tableau and is given by 



For updating the stabiliser tableau after the application of a Clifford gate or a _|_ 0 _⟩ / |_ 1 _⟩_ -basis measurement, NetSquid uses the algorithms by [96] and [77]. The runtime performance of stabiliser tableau algorithms is a direct function of the number of qubits: linear for applying single- or two-qubit Clifford unitaries, which any Clifford can be composed into, and cubic for single-qubit measurement [96]. 

## _Graph states with local Cliffords (GSLC)_ 

The last formalism is GSLC: graph states with local Cliffords [78]. Graph states are a subset of all stabiliser states (see [98] for a review) and an _n_ -qubit graph state _|ψ⟩_ can be written as 



where _Zjk_ indicates a controlled- _Z_ gate _|_ 00 _⟩⟨_ 00 _|_ + _|_ 01 _⟩⟨_ 01 _|_ + _|_ 10 _⟩⟨_ 10 _| −|_ 11 _⟩⟨_ 11 _|_ between qubits _j_ and _k_ , and we have denoted _|_ + _⟩_ = ( _|_ 0 _⟩_ + _|_ 1 _⟩_ ) _/√_ 2. As such, a graph state is completely determined by the set of qubit index pairs ( _j, k_ ) at which a controlled- _Z_ operation is performed. These indices can be captured in a graph with undirected edges; in eq. (11), the edge set is _E_ . Each stabiliser state can be written as a graph state, followed by the application of single-qubit Clifford operations. Thus, a stabiliser state in the GSLC formalism is represented by a set of edges _E_ and a list of _n_ single qubit Cliffords. There exist 24 single-qubit Cliffords, so the Clifford list only requires _O_ ( _n_ ) space. For updating the graph and the list of single-qubit Cliffords after the application of a Clifford gate or a _|_ 0 _⟩ / |_ 1 _⟩_ -basis measurement, NetSquid uses the algorithms by [78]. The runtime scaling of the graph-state-based formalism depends on the edge degree _d_ of the vertices involved in the operation – constant-time for single-qubit Cliffords, quadratic in _d_ for two-qubit Cliffords and measurement – and thus scales favourably if the graph is sparse. 

## **B. The PyDynAA simulation engine** 

The discrete-event modelling framework used by NetSquid is provided by the Python package PyDynAA, which is based on the core engine layer of DynAA, a system analysis and design tool [80]. This foundation provides a simple yet powerful language for describing large and complex system architectures. To realise PyDynAA, the simulation engine core was written in C++ for increased performance, and bindings to Python were added using Cython. NetSquid takes advantage of the Cython headers exposed by PyDynAA to efficiently integrate the engine into its own compiled C extension libraries. 

Several of NetSquid’s sub-packages depend and build on the classes provided by PyDynAA, as illustrated in Figure 10 (main text). In Supplementary Figure 13 we highlight several of these key classes and how they interact with the simulation timeline in more detail, namely: the simulation engine (SimulationEngine), events (Event and EventType), simulation entities (Entity), and event handlers (EventHandler). We proceed to describe the concepts these classes represent in more detail. 

Simulation _entities_ represent anything in the simulation world capable of generating or responding to events. They may be dynamically added or removed during a simulation. The Entity superclass provides methods for scheduling events to the timeline at specific instances and waiting for them to trigger. The intended use is that users subclass the Entity class to implement their own entities. The _simulation engine_ efficiently handles the scheduling of events at arbitrary (future) times by storing them in a self-balancing binary search 

24 



<!-- Start of picture text -->
Entity<br>... wait for event to trigger<br>schedule_at (time, EventType)<br>wait (EventHandler, <event mask>) EventHandler<br>... ...<br>handle (Event)<br>schedule event onto timeline respond to event via a function<br>SimulationEngine run<br>... time<br>run ()<br>stop ()<br>...<br>Event<br>id : int EventType<br>type: EventType name<br>source: Entity description<br><!-- End of picture text -->

Figure 13: **Design overview of the PyDynAA package.** Schematic overview of key classes defined by the PyDynAA package, the discrete-event simulation engine used by NetSquid. Also shown is the relation of each class to the simulation timeline. Events are scheduled onto the simulation timeline by Entity objects. Entities wait for events to trigger by registering EventHandlers, which respond to an event by passing it as input to a specified callback function. The events to wait for can be specified by their type, id, and source entity. Ellipses indicate that not all of a class’s public variables and methods are listed. Omitted from this class diagram is the EventExpression class – see the text for more details. 

tree. Events may only be scheduled by entities, which ensures that events always have a source entity. If an entity is removed during a simulation, then any future events it had scheduled will no longer trigger. An entity responds to events by registering an event handler object with a callback function. Responses can be associated to a specific type, source, and id (including wildcard combinations). The simulation engine runs by stepping sequentially from event to event in a discrete fashion and checking if any event handlers in its registry match. A hash table together with an efficient hashing algorithm ensure efficient lookups of the event handlers in the registry. 

PyDynAA implements an _event expression_ class to allow entities to wait on logical combinations of events. Atomic event expressions, which describe regular wait conditions for standard events, can be combined to form composite expressions using logical _and_ and _or_ operators to any depth. Event expressions enable NetSquid simulations to deal with timing complexities. This feature has been used extensively in NetSquid to model both the internal behaviour of hardware components, as well as for programming network protocols. As example, consider DEJMPS entanglement distillation [67]: two nodes participate in this protocol and a node can only decide whether the distillation succeeded or failed when both its local quantum operations have finished and it has received the measurement outcome from the remote node. Thus, the node waits for the logical _and_ of the receive-event and the event that the local operations have finished. 

## **C. The modular component modelling framework** 

The physical modelling of network devices is provided by several NetSquid sub-packages: _components_ , _models_ and _nodes_ , which are shown stacked with relation the NetSquid package in Figure 10 (main text). The pivotal base class connecting all them is the _component_ (Component), which is used to model all hardware devices. Specifically, it represents all physical entities in the simulation, and as such sub-classes the _entity_ (Entity),which enables it to interact with the event timeline. In Supplementary Figure 14 we show a class diagram of the component class and its relationships to other classes from these sub-packages. 

The modularity of NetSquid’s modelling framework is achieved by the composition of components in terms of _properties_ , _models_ , communication _ports_ and _subcomponents_ . A component’s _properties_ are values that physically characterise it, such as the length of a channel or the frequency of a source. A special _constrained map_ (ConstrainedMap) container is used to store the properties (as well as the other composed objects) to give control of the expected types and immutability of properties during a simulation. _Models_ (Model) are used to describe the physical behaviour of a component, such as the transmission delay of a channel, or the quantum decoherence of a qubit in memory. Model objects are essentially elaborate functions and generally do not store any state; when a model is called it is passed its component’s properties, in addition to any modelling specific input, such as, in the case of a quantum noise model, the qubit to apply noise and the time the qubit has been waiting on a memory. Components can be composed of other _subcomponents_ , which allows networks to be pieced together in a very modular fashion. For instance, a complete network 

25 



<!-- Start of picture text -->
Channel QuantumChannel<br>Entity +properties: +models<br>+uid: int     length: float     quantum_noise_model: QuantumErrorModel<br>#_schedule_{now,after,at}(...)#_wait{_once}(...)#_dismiss(...)... +ports:     send    recv +models     delay_model: DelayModel     quantum_loss_model: QuantumErrorModel +models ClassicalChannel<br>...     classical_noise_model: QuantumErrorModel<br>    classical_loss_model: QuantumErrorModel<br>Port Component<br>+name: str+component: Component +name: str +properties: ConstrainedMap +models:MemoryPosition +properties:QuantumMemory<br>... +ports: ConstrainedMap     noise_model: QuantumErrorModel     num_positions: int<br>+connect(other_port: Port)+forward_input(other_port: Port)+forward_output(other_port: Port) +models: ConstrainedMap+subcomponents: ConstrainedMap ... ... +ports:     qin    qout +models:<br>+tx_input(message: Message) ...     qin_noise_model: QuantumErrorModel<br>+tx_output(message: Message)     qout_noise_model: QuantumErrorModel<br>+rx_input() +subcomponents:<br>+rx_output()...     mem_position{0...N}: MemoryPosition<br>Model ...<br>+properties: dict<br>+required_properties: list<br>+items: list+meta: dict Message +validate(...)+compute_model(...)... QuantumSource, QuantumDetector, Clock, QuantumProcessor, ... All modeled hardware devices are components<br>Node<br>ErrorModel DelayModel Network +subcomponents:     qmemory: QuantumMemory<br>... +nodes: ConstrainedMapView<br>+error_operation() +generate_delay() +connections: ConstrainedMapView connects ▲<br>Connection<br>QuantumErrorModel ClassicalErrorModel ports:     A<br>    B<br><!-- End of picture text -->

Figure 14: **Design overview of components in NetSquid.** Class diagram for the Component class, a simulation entity that is used to model all network hardware devices, including composite components such as nodes, connections and the network itself. A component is shown to be composed of _properties_ , _ports_ , _models_ and _subcomponents_ . Ellipses indicate that not all of a class’s public variables and methods are listed. 

can be represented by a single component, which is composed of node and connection sub-components, which in turn are composed of devices such as channels, sources, memories, etc. To streamline and automate the communication between components, including to and from sub-components, components can be linked using _ports_ (Port) that can send, receive and forward both quantum and classical _messages_ (Message). While the component base class defines a modular interface for modelling all kinds of hardware, it doesn’t internally implement any event-driven behaviour itself. That behaviour is implemented by a library of base classes that sub-class Component. The right half of Supplementary Figure 14 shows the sub-classing hierarchy of the provided components, ranging from quantum and classical channels, quantum memory and processing devices, sources, detectors, clocks, to nodes, connections, and networks. 

The _quantum processor_ (QuantumProcessor) is a component from the base class library used for modelling general quantum processing devices. It sub-classes the _quantum memory_ (QuantumMemory) component, from which it inherits a collection of _quantum memory positions_ (MemoryPosition) for tracking the quantum noise of stored qubits. The processor can assign a set of _physical instructions_ to these positions to describe the operations possible for manipulating their stored qubits, such as quantum gates and measurements, or initialisation, absorption, and emission processes. The physical instructions map to general device-independent instructions, for which they specify physical models such as duration and error models specific to the modelled device. This mapping allows users to write _quantum programs_ in terms of device-independent instructions and re-use them across devices. The quantum programs can include classical conditional logic, make use of parallel execution (if supported by the device), and import other programs. 

## **D. Asynchronous programming networks using protocols** 

While components are entities in the simulation describing physical hardware, _protocols_ – represented by the Protocol base class as shown in Supplementary Figure 15 – are entities that describe the intended virtual behaviour of a simulation. In other words, the protocol base class is used to model the various layers of software running on top of the components at the various nodes and connections of a network. That can include, for instance, any automated control software at the physical or link layers of a quantum network stack, up to higher-level programs written at the application layer. 

Protocols in NetSquid can be likened to background processes: they can be started, stopped, as well as reset to clear any state. They can also be nested i.e. a protocol can manage the execution of _sub-protocols_ under its control. To communicate changes of state, such as a successful or failed run, protocols can use a _signalling_ mechanism (Signal). 

26 

NetSquid defines several sub-classes of the protocol base class that add extra restrictions or functionality. To restrict the influence of a protocol to only a local set of nodes the _local protocol_ (LocalProtocol) can be used. Similarly, to restrict a protocol to executing on only a single node, which is a typical use case, a _node protocol_ (NodeProtocol) is available. The _service protocol_ (ServiceProtocol) describes a protocol interface in terms of the types of requests and responses they support. Lastly, a _data node protocol_ adds functionality to process data arriving from a port linked to a connection, and the _timed node protocol_ supports carrying out actions at regularly timed intervals. 

Programming a protocol involves waiting for and responding to events, which is achieved in the simulation engine by defining event handlers that wrap callback functions. As the complexity of a protocol grows, typically the flow and dependencies of the callback calls do too. To make the asynchronous interaction between protocol and component entities easier and more intuitive to program and read, the main execution function of a protocol (the run() method) can be suspended mid-function to wait for certain combinations of events to trigger. This is implemented in Python using the yield statement, which takes as its argument an event expression. Several helper methods have been defined that generate useful event expressions a protocol can _await_ , for instance: await_port_input() to wait for a message to arrive on a port, or await_timer() to have the protocol sleep for some time. 



<!-- Start of picture text -->
ServiceProtocol<br>Entity Protocol LocalProtocol +request_types: ConstrainedMap<br>+uid: int +name: str +nodes: ConstrainedMap +response_types: ConstrainedMap<br>#_schedule_{now,after,at}(...) +signals: dict +max_nodes: int +response_handlers: ConstrainedMap<br>#_wait{_once}(...)#_dismiss(...) +subprotocols: ConstrainedMap... ... ...<br>... +run()<br>+start()<br>+stop() TimedNodeProtocol<br>FINISHED: EventType«Enum» Signals +reset()+start_subprotocols()+send_signal()+await_timer(...) +node: Node NodeProtocol +time_step: float+start_time: float...<br>SUCCESS: EventType +await_signal(...)<br>FAIL: EventType +await_port_input(port: Port, ...)<br>BUSY: EventType +await_port_output(port: Port, ...) DataNodeProtocol<br>WAITING: EventType +await_program(...)<br>READY: EventType ... +port_name: str<br>+process_data(message: Message)<br>+post_process_data(message: Message)<br><!-- End of picture text -->

Figure 15: **Design overview of protocols in NetSquid.** Class diagram of the Protocol class and its subclasses. Ellipses indicate that not all of a class’s public variables and methods are listed. 

## **Supplementary Note 2: Quantum circuits and network setups for benchmarking** 

In this section we extend the Methods, section Benchmarking, to provide additional details on the benchmarking simulations presented in the Results, section Fast and scalable quantum network simulation. 

## **A. Benchmarking of quantum computation runtime** 

The quantum circuit used to benchmark the runtime for generating an _n_ qubit GHZ state is shown in Supplementary Figure 16a. The _n_ qubits are created in NetSquid with independent quantum states and are combined into the larger state via the CNOT operation. The measurement operations at the end of the circuit are performed sequentially and each split the measured qubit from its shared quantum state. Unless otherwise specified the KET and DM formalisms utilise memoization (see Methods, section Qubits and quantum computation). Memoization is effective because the circuit is successively iterated 30 times. The reported runtime is the mean runtime of the iterations. For the baseline comparison with the ProjectQ simulator we set up the circuit in an analogous way to NetSquid, and its default MainEngine was used with no special settings applied. Qubits are similarly added sequentially to the growing state via the CNOT operation, and also the measurements are performed sequentially with the measured qubit directly deallocated afterwards. The quantum circuit used to benchmark the runtime of only the quantum computation involved for a simple repeater chain involving _n_ qubits is shown in Supplementary Figure 16b. It is implemented for NetSquid and ProjectQ similarly to the GHZ benchmark, with qubits only combining their quantum states when a multi-qubit gate is performed. An option has been added to keep qubits _inplace_ after measurements i.e. they are not split from their shared quantum states – in ProjectQ this is achieved by keeping a reference to prevent deallocation. Noise is applied to each qubit after entanglement by selecting a Pauli gate to mimic depolarising noise, which is done deterministically for convenience. For this process the runtime is also determined as the mean of 30 successive iterations. 

27 



<!-- Start of picture text -->
Entangle Noise Swap<br>q 1<br>| 0 ⟩ H • {X, Y, Z}<br>q 2<br>| 0 ⟩ {X, Y, Z} • H •<br>q 3<br>q 1 | 0 ⟩ H • {X, Y, Z} •<br>| 0 ⟩ H • • · · · •<br>q 4<br>q 2 | 0 ⟩ {X, Y, Z} • H •<br>| 0 ⟩ · · ·<br>q 3 · · · · · · · · · · · ·<br>| 0 ⟩ · · ·<br>qn− 1<br>· · · · · · | 0 ⟩ H • {X, Y, Z} •<br>qn qn<br>| 0 ⟩ · · · | 0 ⟩ {X, Y, Z} X Z<br>(a) GHZ state generation (b) Repeater chain quantum computation<br><!-- End of picture text -->

Figure 16: **Circuits used to benchmark quantum computation in the Results, section Benchmarking of quantum computation, for** _n_ **qubits.** For panel (b) the CNOT control line crossing the ellipses represents multiple lines for _n >_ 6 qubits, following the pattern of _q_ 2 and _q_ 3. Similarly, the classical control lines represent an AND of the measurement results for _q_ 3, _q_ 5, . . . , _qn−_ 1 and _q_ 2, _q_ 4, . . . , _qn−_ 2 to determine the control of the _X_ and _Z_ gates, respectively. The noise gates denoted by {X,Y,Z} cycle through the Pauli gates (see main text). Note that this circuit always requires an even number of qubits. 

To benchmark the runtimes of quantum computation circuits the processes were timed in isolation from any setup code using the Python _timeit_ package. Python garbage collection is disabled during the timing of each process. To avoid fluctuations due to interfering CPU processes the reported time is a minimum of five repetitions. 

## **B. Runtime profiling of a repeater chain simulation** 

The runtime profiling of NetSquid presented in the Results, section Benchmarking of event-driven simulations, is performed for a simple repeater chain. The network setup of this simulation extends the single repeater presented in Supplementary Figure 1 to a chain of nodes by adding the entangling connection shown between each pair of neighbouring nodes. Direct classical connections are connected between each node and one of the end-nodes, rather than between neighbouring nodes, and are used to transmit the swapping corrections. The chosen configuration for this network does not need to be physically realistic; it suffices for it to be representative of the typical computational complexities. The nodes are placed at 20km intervals and the channels transmit messages at the speed of light in fibre. The entanglement sources, assumed to be perfect, are all synchronised and operate at a frequency of 100 kHz. Physical non-idealities are represented by adding time-dependent depolarising noise to both the quantum channels and quantum memories, as well as dephasing noise to quantum gates. The corresponding depolarising and dephasing times are 0 _._ 1 s and 0 _._ 04 s, which correspond to the _T_ 1 and _T_ 2 times presented in section Modelling a nitrogen-vacancy centre in diamond of the Methods. 

In a simulation run entanglement is created once between the end-nodes by performing entanglement swaps along the chain. Protocols are assigned to all but the end-nodes to perform entanglement swaps after each round of entanglement generation, and send their measurement results as corrections to the same end-node. A protocol running on the end-node collects these corrections, and applies them if needed. The runtime of this simulation is profiled to determine the distribution of time spent in the functions of NetSquid’s sub-packages, as well as its dependency packages NumPy and PyDynAA. To perform this profiling the cProfile package is used. The reported runtime for a given number of nodes is the mean of 400 successive simulation runs. 

## **Supplementary Note 3: Quantum switch: physical network and protocol** 

Here, we provide the details of the quantum switch simulations, whose results are presented in section Simulating a quantum network switch beyond its analytically known regime of the Results. 

28 

We implement the model of Vardoyan et al. [56], for which the parameters of the simulation are: 

- the number of leaf nodes _k_ ; 

- the desired size _n_ of the shared entanglement on the leaf nodes; 

- for each leaf node: the rate _µ_ at which bipartite entanglement is generated between leaf node and switch; 

- _B_ : the buffer size, i.e. the number of dedicated qubits per leaf node at the switch. 

In addition, we include _T_ 2, the memory coherence time. 

## **A. Physical network** 

In the scenario we study, the quantum switch is the centre node of a star-topology network, with _k ≥_ 2 leaf nodes. Each leaf node individually is connected to the switch by a _connection_ , which consists of a _source_ producing perfect bipartite entangled states ( _|_ 00 _⟩_ + _|_ 11 _⟩_ ) _/√_ 2 on a randomised _clock_ and two _quantum connections_ , from the source to the leaf and switch node, respectively, for transporting the two produced qubits. The interval ∆ _t_ between clock triggers is randomly sampled from an exponential distribution with probability _µ · e_<sup>_−µ·_∆</sup><sup>_t_</sup> where _µ_ is the rate of the source. We set the delay of the quantum channels to zero. Each node holds a single _quantum processor_ with enough quantum memory positions for the total duration of our runs. Each memory position has a _T_ 2 _noise model_ : if a qubit is acted upon after having resided in memory for time ∆ _t_ , then a dephasing map (eq. (1)) is applied with dephasing probability _p_ = 2<sup><u>1</u></sup> �1 _− e_<sup>_−_∆</sup><sup>_t/T_2�</sup> . Each quantum processor can perform any unitary operation or single-qubit measurement; these operations are noiseless and take no time. 

## **B. Protocol of the switch node** 

The switch node continuously waits for incoming qubits. Upon arrival of a qubit from leaf node _ℓ_ , the switch first checks whether it shares more entangled pairs of qubits with _ℓ_ than the pre-specified buffer size _B_ ; if so, it discards the oldest of those pairs. Then, it checks whether it holds entangled pairs with at least _n_ different leaves. If so, then it performs and _n_ -qubit GHZ-basis measurement (see below) on its qubits of those pairs. If multiple groups of _n_ qubits from _n_ distinct nodes are available, then it chooses the oldest pairs. Directly after completion of the GHZ-basis measurement, we register the measurement outcomes and obtain the resulting _n_ -partite entangled state _|ψ⟩_ on the leaf nodes. From these, the fidelity _|⟨ψ|φ_ ideal _⟩|_<sup>2</sup> with the ideal target GHZ state _|φ_ ideal _⟩_ is computed. The _n_ -qubit GHZ states are 



where _bj ∈{_ 0 _,_ 1 _}_ and we have denoted _b_ = 1 _− b_ . The _n_ -qubit _quantum program_ that the switch node applies for performing a measurement in the _n_ -qubit GHZ basis is as follows: first, a CNOT operation on qubits 1 and _j_ (1 is the control qubit) is applied for all _j_ = 2 _,_ 3 _, . . . , n_ , followed by a Hadamard operation (eq. 52) on qubit 1. Then, all qubits are measured in the _|_ 0 _⟩ / |_ 1 _⟩_ -basis. If we denote the outcome of qubit _j_ as _bj_ , the GHZ-state that is measured is precisely the one in eq. (31). 

## **Supplementary Note 4: Hardware parameters for the NV repeater chain** 

Here, we provide the values for the hardware parameters of the nitrogen-vacancy setup used in our simulations. An overview of all parameters is provided in Supplementary Table II, including two example sets of improved parameters following the approach in section How we choose improved hardware parameters of the Methods. 

## **A. Parameters for elementary link generation** 

For generating entanglement between the electron spins of two remote NV centres in diamond, we simulate a scheme based on single-photon detection, following its experimental implementation in [93]. The setup consists of a middle station which is positioned exactly in between two remote NV centres in diamond. 

29 

|oise param.<br>10_×_<br>0_._003<br>**_×_**<br>2_._5_·_10_−_9<br>0.58<br>0.11<br>0.99<br>14006<br>10h<br>14.6s<br>100h<br>10s<br>_F_ = 0_._9997<br>_F >_0_._9999<br>_FEC_ = 0_._997<br>_F_ = 0_._999<br>_F_ = 1<br>0_._995_/_0_._9995<br>**nd duration and fdelities (**_F_**) of**<br>ds, section How we choose improved<br>r to a ‘probability of no-error’ to<br>sion loss parameter _γ_ is not changed|
|---|
|Improved n<br>3_×_<br>0_._01<br>**_×_**<br>8_._3_·_10_−_8<br>0.16<br>0.20<br>0.97<br>4206<br>2.8h<br>4.4s<br>27h<br>3s<br>_F_ = 0_._999<br>_F >_0_._9999<br>_FEC_ = 0_._990<br>_F_ = 0_._997<br>_F_ = 1<br>0_._983_/_0_._9983<br>**nce times a**<br>s (see Metho<br>the paramete<br>The transmis<br> simulations.|
|Probability<br>of no-error<br>_p_dexc<br>**_×_**<br>1_−p_dc<br>_p_nofbre<br>det<br>1_−p_phase<br>(eq. (43))<br>_V_<br>_p_ from eq. (45)<br>_e−_1_/T_1<br>_e−_1_/T ∗_<br>2<br>_e−_1_/T_1<br>_e−_1_/T_2<br>2_F −_1<br>4(_F −_1)_/_3<br>(4_√_<br>_FEC −_1)_/_3<br>2_F −_1<br>(4_F −_1)_/_3<br>_fx_<br>**emory cohere**<br>d parameter set<br>ion to convert <br> improvement. <br>ing any of our|
|Duration/time<br>-<br>-<br>-<br>-<br>-<br>-<br>-<br>1h<br>1.46 s<br>10h<br>1s<br>310 _µ_s<br>20 _µ_s<br>500 _µ_s<br>2 _µ_s<br>5 ns<br>3.7 _µ_s<br>**eneration, m**<br>les of improve<br> with the funct<br>respond to 1_×_ <br>0_._2 dB/km dur|
|Noise parameter<br>(‘near-term’)<br>0.06<br>0.2<br>2_._5_·_10_−_8<br>0.0046<br>0_._35<br>0.9<br>1400<br>-<br>-<br>-<br>_F_=0.997<br>_F_=0.999<br>_FEC_=0.97<br>_F_=0.99<br>_F_=1<br>0_._95_/_0_._995(_f_0_/f_1)<br>**ementary link g**<br>m’ and two examp<br>pectively, together <br>r-term’ values cor<br>e and equals _γ_ =|
|Probability of double excitation _p_dexc (4 A b)<br>Transmission loss _γ_ (dB/km, 4 A a)<br>Dark count probability _p_dc (4 A b)<br>Probability of photon detection (4 A a)<br>for zero-length fbre _p_nofbre<br>det<br>Interferometric phase uncertainty<br>_σphase_ (rad, 4 A b)<br>Photon visibility _V_ (4 A b)<br>_N_1_/e_: indicates nuclear dephasing<br>during electron initialization (4 A c)<br>Electron _T_1 (4 A d)<br>Electron _T ∗_<br>2 (4 A d)<br>Carbon _T_1 (4 A d)<br>Carbon _T_2 (4 A d)<br>Carbon initialization to _|_0_⟩_(4 A d)<br>Carbon _Z_-rotation gate (4 A d)<br>E-C controlled-_RX_-gate<br>(electron=control) (4 A d)<br>Electron initialization to _|_0_⟩_(4 A d)<br>Electron single-qubit gate (4 A d)<br>Electron readout (eq. (4) and sec. 4 A d )<br>Supplementary Table II: **Physical parameters dealing with el**<br>**the gates.** Depicted are both parameters of the dataset ‘near-ter<br>hardware parameters), for 3 times and 10 times improved, res<br>compute the improved parameter value for other factors. The ‘nea<br>by the improvement procedur|



30 

The middle station is connected to the two NVs by glass fibre and contains a 50:50 beam splitter and two non-number resolving photon detectors. In the single-photon scheme, each NV performs the following operations in parallel. First, the electron of each NV system is brought into the state<sup>_√_</sup> _<u>α</u> |_ 0 _⟩_ +<sup>_√_</sup> 1 _− α |_ 1 _⟩_ by optical and microwave pulses, where _α_ is referred to as the bright-state parameter. Then, a laser pulse triggers the emission of a photon, yielding the spin-photon state<sup>_√_</sup> _<u>α</u> |_ 0 _⟩s ⊗|_ 1 _⟩p_ +<sup>_√_</sup> 1 _− α |_ 1 _⟩s ⊗|_ 0 _⟩p_ , where _|_ 0 _⟩_ ( _|_ 1 _⟩_ ) denotes absence (presence) of a photon. We set _α_ = 0 _._ 1 since for that value, fidelity is approximately maximal at lab-scale distances [93]; optimising over _α_ is out of the scope for this work. We assume that the delay until emission of the photon is fixed at 3 _._ 8 _µ_ s [99]. 

From each NV centre, the emitted photons are transmitted to the middle station through glass fibre, where a 50:50 beam splitter effectively erases the which-way information of an incoming photon. An attempt at generating entanglement using this single-click scheme is declared successful if precisely one of the detectors clicks, which happens if either (a) a single photon arrives at the detector and the other does not or (b) both photons arrive (in case (b), only a single detector clicks due to the Hong-Ou-Mandel effect). Case (a) yields the generation of the spin-spin state _|φ±⟩_ = ( _|_ 01 _⟩± |_ 10 _⟩_ ) _/√_ 2, where _±_ indicates which of the two detectors clicked, while case (b) results in _|_ 00 _⟩⟨_ 00 _|_ . Given that a single photon arrives, the probabilities that the other photon has or has not arrived are respectively 1 _− α_ and _α_ (in the absence of loss). Therefore, a successful attempt results in the generation of the spin-spin state (1 _− α_ ) _|φ±⟩⟨φ±|_ + _α |_ 00 _⟩⟨_ 00 _|_ . We refer to [93] for a more in-depth description of the scheme. We assume that the speed of the photons and of all classical communication equals _c/nri_ , where _c_ is the speed of light in vacuum and _nri_ = 1 _._ 44 is the refractive index of glass [100]. 

In reality, however, several sources of noise affect the produced state, which we treat below. 

## _a. Imperfect detection_ 

The total probability _p_ det that a photon, emitted by the NV, will be detected in the midpoint is given by the product of four probabilities [92] 

- the probability _p_ zero_phonon that the photon frequency is in the zero-phonon line [101]; 

- the probability _p_ collection that the photon is collected into the glass fibre; 

- the probability _p_ transmission that the photon does not dissipate in the fibre during transmission; 

- the probability _p_ detection that the photon is detected, conditioned on the fact that it reaches the detector. 

Thus we can write 



where 



The transmission probability is given by 



where _L_ is the internode distance (i.e. _L/_ 2 is the length of the fibre from NV to middle station) and _γ_ is the loss parameter which depends on the photon frequency. In our simulations, we assume that the photon frequency is converted to the telecom frequency, corresponding to _γ_ = 0 _._ 2 dB/km. Also, we assume that the emission in the zero-phonon line is enhanced by an optical cavity from _p_ zero_phonon = 3% (without cavity) to _p_ zero_phonon = 46% (with cavity) [101]. We set the detection efficiency _p_ detection to 0.8 [102]. What remains is the collection efficiency _p_ collection, which we compute from experimental values (no cavity, no conversion to the telecom frequency) using eq. (41) with _L_ = 2m, _p_ det = 0 _._ 001 [99] and _γ_ = 5 dB/km [39] (for the zero-photon line frequency), yielding _p_ collection = 0 _._ 042. Since frequency conversion to the telecom frequency is a probabilistic process and only succeeds with probability 30% [103], we set _p_ collection = 0 _._ 3 _·_ 0 _._ 042. 

_b. Other sources of noise_ 

Other sources of noise on the freshly generated electron-electron entanglement are 

31 

- Dark counts: a photon detector falsely registering. The dark count probability follows a Poisson distribution _p_ dc = 1 _− e_<sup>_−t_w</sup><sup>_·λ_dark</sup> where _t_ w = 25 ns [93] is the duration of the time window at the midpoint. We set _λ_ dark = 1 Hz as the dark count rate. 

- Imperfect photon indistinguishability. The generation of entanglement at the middle station is based upon the erasure of the which-way information with respect to the path of the photons. Only in case the photons are fully indistinguishable, the which-way information is erased perfectly. The overlap of the photon states is given by the visibility _V_ , which we set to 0.9 [93]. 

- Double excitation of the electron spin. When triggered to emit a photon by a resonant laser pulse, an NV centre could be excited twice, which results into the emission of two photons. We set its occurrence probability to _p_ dexc = 0 _._ 06 [99]. 

- Photon phase uncertainty. The photons which interfere at the midpoint acquired a phase during transmission and a difference of these phases influences the precise entangled state that is produced [104]. Given a standard deviation _σ_ phase = 0 _._ 35 rad [99] of the acquired phase, we compute the dephasing probability as [93] 



_c. Nuclear spin dephasing during entanglement generation_ 

The initialisation of the electron spin state induces dephasing of the carbon spin states through their hyperfine coupling. Following [105], we model this uncertainty by a dephasing channel for each attempt with dephasing probability 



The parameter _C_ nucl is the product of the coupling strength between the electron spin and the carbon nuclear spin, and an empirically determined decay constant. Rather than expressing the dephasing probability as function of _C_ nucl, we express the magnitude of nuclear dephasing as _N_ 1 _/e_ , the number of electron spin pumping cycles after which the Bloch vector length of a nuclear spin in the state ( _|_ 0 _⟩_ + _|_ 1 _⟩_ ) _/√_ 2 in the _X − Y_ plane of the Bloch sphere has shrunk to 1 _/e_ , when the electron spin state has bright-state parameter _α_ = 0 _._ 5 (i.e the electron spin is in the state ( _|_ 0 _⟩_ + _|_ 1 _⟩_ ) _/√_ 2). Let us compute how _p_ single depends on _N_ 1 _/e_ instead of on _C_ nucl. First, we find by direct computation that the equatorial Bloch vector length of a state is shrunk by a factor 1 _−_ 2 _p_ after a single application of the single-qubit dephasing channel (eq. (1)) with probability _p_ ( _p ≤_<sup><u>1</u></sup> 2<sup>).</sup> Equating (1 _−_ 2 _p_ )<sup>_N_1</sup><sup>_/e_</sup> = 1 _/e_ yields 



Equating _p_ single from eq. (44) with _α_ = 0 _._ 5 and _p_ from eq. (45), followed by solving for _C_ nucl yields 



Substituting back into eq. (44) yields an expression for general _α_ : 



We set _N_ 1 _/e_ = 1400 [106]. 

## _d. Local processing parameters_ 

For the dynamics of the electron spin, we use _T_ 1 = 1 hour and _T_ 2<sup>_∗_=1</sup><sup>_._46s[107].Forthecarbonnuclear</sup> spin, we take _T_ 1 = 10 hours and _T_ 2 = 1 s (experimentally realised: _T_ 1 = 6m and _T_ 2 _≈_ 0 _._ 26 _−_ 25s [108]). For the noise of the controlled- _RX_ gate (Methods, section Modelling a nitrogen-vacancy centre in diamond), we set the depolarising probability _p_ = 0 _._ 02 (denoted as _pEC_ in Supplementary Table II), since by simulation of the circuit [104, Fig. 2a], we find that this value agrees with the experimentally found effective circuit 

32 

fidelity of 0 _._ 95. The corresponding fidelity of the gate is _FEC_ = (1 _−_ 3 _pEC/_ 4)<sup>2</sup> = 0 _._ 97. The initialisation fidelities of the electron and carbon spins are set at 0 _._ 99 [109] and 0 _._ 997 [108]. We use 0 _._ 999 for the carbon _Z_ -rotation gate fidelity (experimentally achieved: 1 [110]). The durations of local operations are identical to our earlier simulations (see Appendix D, Table 6 in [39] and references therein). We summarise all hardware values in Supplementary Table II. 

## **Supplementary Note 5: Protocols and quantum programs for the NV repeater chain** 

Here, we first elaborate on the sequence of quantum operations and classical communication that the NV protocol building blocks consist of (Methods, section NV repeater chain protocols). Then, we describe in detail the two repeater chain protocols we simulated. 

## **A. Operations for the building blocks: store, retrieve, distill and swap** 

store is the mapping of the electron spin state onto a free nuclear spin. The operation requires the nuclear spin state to be _|_ 0 _⟩_ and the circuit, given in Supplementary Figure 17(a), performs the following mapping: 



where _|φ⟩_ is an arbitrary single-qubit state and 



is the Hadamard gate. By retrieve (Supplementary Figure 17(b)), we denote the reverse operation, 



We simulate the specific entanglement distillation protocol (distill) from Kalb et al. [104], which acts upon an electron-electron state and a nuclear-nuclear state to probabilistically increase the quality of the nuclearnuclear state, at the cost of having to read out the electron-electron state. In the protocol, the two involved nodes each perform a sequence of local operations including a measurement (Supplementary Figure 17(c)), followed by communicating the measurement outcome from the circuit to each other. In this work, we only use distillation in one of the two repeater schemes we consider (nested-with-distill) and in that case, the success condition is as follows: if the nodes are adjacent, then the measurement outcomes should both equal 0 (i.e. the bright state of the electron), while otherwise the measurement outcomes only need to be equal (i.e. both 0 or both 1). In the case of failure, the nuclear-nuclear state is considered lost. The entanglement swap (swap) converts two short-distance entangled qubit pairs _A − M_ and _M − B_ into a single long-distance one _A − B_ , where _A, B_ and _M_ are nodes. It is equivalent to performing quantum teleportation [111] to a qubit which is part of a larger remote-entangled state. Our entanglement swapping protocol at node _M_ starts by assuming that one of _M_ ’s qubits which is involved in the entanglement swap is the electron spin. Then, a series of local operations including measurements (Supplementary Figure 17(d)) is performed; the measurement outcomes are transferred to both _A_ and _B_ . In the original teleportation proposal, _B_ performs a local operation to correct the state _A − B_ to the expected one. However, due to the fact that such correction operation is generally not directly possible to perform on the nuclear spin state (see the allowed operations in section Modelling a nitrogen-vacancy centre in diamond of the Methods), we opt for the approach where the correction operation is tracked in a classical database. Details of this tracking, including how it affects the entanglement distillation and entanglement swap protocols, are given in Supplementary Note 6. 

## **B. Repeater chain protocols swap-asap and nested-with-distill** 

We describe two protocols for the NV repeater chain: swap-asap, a protocol where a node performs an entanglement swap as soon as it holds two entangled pairs, one in each direction of the chain, and nestedwith-distill, a nested protocol with distillation at each nesting level which is based on the BDCZ protocol [9]. Both protocols run asynchronously on each node. 

In both protocols, a node remains idle until it is triggered to check whether it should perform an action. It is triggered at the following three moments: (a) at the start of the simulation, (b) when the node receives a classical message (if a node is busy upon reception, the message is stored and responded to later) , (c) 

33 



<!-- Start of picture text -->
(a) e • RX ( π 2 ) • RY  ( − π 2 )<br>store =<br>n initialise RZ ( − π 2 ) RX ( ± π 2 ) RZ ( π 2 ) RX ( ± π 2 )<br>(b) e initialise RY  ( π 2 ) • RX ( − π 2 ) •<br>retrieve =<br>n RX ( ∓ π 2 ) RZ ( − π 2 ) RX ( ∓ π 2 ) RZ ( π 2 )<br>(c) e RY  ( π 2 ) • RX ( π 2 )<br>n RX ( ∓ π 2 )<br>(d) e • RY  ( π 2 ) H<br>retrieve<br>n RZ ( π 2 ) RX ( ± π 2 ) RZ ( − π 2 )<br><!-- End of picture text -->

Figure 17: **Quantum circuits used in simulations of the NV repeater chain, acting on an electron (** _e_ **) and nuclear (** _n_ **) spin.** Figure depicts the quantum circuit for the NV repeater protocol building blocks: (a) store operation (mapping electron spin state onto the nuclear spin), (b) retrieve (reverse operation to store), (c) entanglement distillation, (d) entanglement swap. 

when its previous action is finished. A simulation run finishes as soon as the two end nodes share a single entangled pair of qubits. 

For the swap-asap protocol, the sequence of operations that a node performs depends on its index in the chain (start counting from left to right, nodes have indices 1 _,_ 2 _,_ 3 _, . . ._ ). If the index of the node is even, the node sends a request for entgen to its left neighbour, and starts the operation as soon as it has received confirmation. After performing store to free the electron spin, it repeats it for its right neighbour. Oddindexed nodes remain idle until reception of an entgen request, after which they perform store if necessary to free the electron, send a confirmation, sleep for the duration of the message transmission, followed by performing entgen. Once a node has entanglement with both directions, it performs a swap and sends the outcome to the end nodes. 

The two end nodes are exceptions to the above. The left end node (i.e. with index 1) behaves like an oddindexed node, but without performing swap. The same holds for the rightmost node (i.e. the node with the largest index), unless its index is even, in which case it initiates and performs entanglement generation with the adjacent node on the left. 

The nested-with-distill protocol is a variant of the BDCZ protocol [9], adapted to the fact that an NV cannot perform multiple entgen , distill or swap operations in parallel due to its restricted topology (Methods, section Modelling a nitrogen-vacancy centre in diamond). In the adapted version, nodes take the role of _initiator_ of one of the three main actions (entgen, distill, swap) if the action occurs at the highest nesting level that this node belongs to. To be precise, we do the following. In a repeater chain with 2<sup>_n_</sup> + 1 nodes, denote by _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2<sup>_n_</sup> _}_ the indices of the nodes from left to right. A node (not an end node) with index _k ∈{_ 1 _,_ 2 _,_ 3 _, . . . ,_ 2<sup>_n_</sup> _−_ 1 _}_ initiates an action only if the entanglement that is involved in the task spans precisely _fn_ ( _k_ ) segments, where 



End nodes are never initiators. 

When a node (index _k_ ) is triggered, it performs the following checks in order and performs the first action for which the check holds true: 

1. If it shares entangled pairs with nodes _k − fn_ ( _k_ ) and _k_ + _fn_ ( _k_ ), and both are the immediate result of successful distillation: perform swap and send the measurement outcomes to the involved nodes 

2. If it holds two entangled pairs with node _k − fn_ ( _k_ ) and neither pair is the result from successful entanglement distillation: send a request to distill to the node, wait for confirmation, followed by performing distill 

34 

3. Same as 2, but now for distill on the right, i.e. remote node has index _k_ + _fn_ ( _k_ ) 

4. If there are any request-messages that have not been responded to yet: pick the oldest one and act as follows. Respond to the message with a confirmation message, followed by sleeping for the time that the confirmation takes to arrive at the remote node. Then perform the requested action (entgen or distill). 

5. If _fn_ ( _k_ ) = 1 and the node does not hold entanglement with its immediate left neighbour that is the result of successful entanglement distillation: send a request for entgen to the node, wait for confirmation, followed by performing entgen. 

6. Same as 5 for right adjacent node. 

If no action follows from the checks above, then the node remains idle until the next time at which it is triggered. In the operations above, if necessary entgen is preceded by store to free the electron by storing its state into a free carbon spin. distill is preceded by a combination of store and retrieve to ensure the correct state lives on the electron spin, and so is swap in case neither of the two to-be-swapped qubits live on the electron. Since end nodes are never initiators, they only check 4. 

## **Supplementary Note 6: Tracking of correction operations in the NV repeater chain** 

Here, we explain how nodes of the NV repeater chain track the precise entangled state they hold. This is done by associating unitary operations to each qubit, which map the state of two remotely entangled qubits back to ( _|_ 01 _⟩_ + _|_ 10 _⟩_ ) _/√_ 2 in the ideal case. Tracking these unitaries (gates) in a classical database, instead of performing them on the (imperfect) quantum hardware, has the advantage of avoiding gate noise. This argument is even stronger for NV centres in case the remote-entangled state is held by a carbon nuclear spin, because direct application of a correction operator to a carbon spin is generally not possible due to the restricted topology of the NV quantum processor (Methods, section Modelling a nitrogen-vacancy centre in diamond). Thus, performing the correction operator to the nuclear spin requires even more gates, namely the ones to map the nuclear spin to the electron spin (the retrieve operation, see section NV repeater chain protocols of the Methods), where the correction operator could be applied. 

In what follows, we first explain how we track the correction operations. Then, we describe how the tracking changes the protocol building blocks from section NV repeater chain protocols of the Methods and subsequently prove the correctness of the tracking in the ideal case. Let us denote the four Bell states as 



To each of the qubits it holds, a node associates a single-qubit Pauli operator 11 _, X, Y_ or _Z_ , which are defined as 



The goal of the tracking is, at any time during the simulation, for any two nodes _A_ and _B_ sharing electronelectron entanglement, that the target electron-electron state equals 



Here, _PA_ and _PB_ denote the Pauli correction operations of node _A_ or _B_ , respectively, and _≡_ denotes equality modulo a complex number of norm 1. In what follows, it will be more convenient to use the following equivalent statement to eq. (61): 



## **A. Tracking correction operators during the NV repeater chain protocol** 

Here, we explain how each of the four protocol building blocks from section NV repeater chain protocols of the Methods are adjusted to ensure that eq. (62) holds after the operations entgen, distill and swap. 

_Entanglement generation._ Suppose that nodes _A_ and _B_ perform the entgen protocol. In the absence of noise, this protocol (approximately) produces the state _|φ_ [ _±_ 1 _, −_ 1] _⟩_ , where _±_ denotes which detector 

35 

clicked (Methods, section Simulation speedup via state insertion). If the +-detector clicked, then the state that A and B hold is the desired state _|φ_ [1 _, −_ 1] _⟩_ , so we set _PA_ = _PB_ = 11. If the other detector clicked, then the produced state is _|φ_ [ _−_ 1 _, −_ 1] _⟩_ . Therefore, one of the nodes (for example, the one with the higher position index in the chain) sets the correction operator to _Z_ , whereas the other sets it to 11, since (11 _⊗ Z_ ) _|φ_ [ _−_ 1 _, −_ 1] _⟩_ = _|φ_ [1 _, −_ 1] _⟩_ . 

_Storing and retrieving qubits._ Locally mapping the state of a qubit onto a different memory position by the store or retrieve circuits does not alter the correction Pauli corresponding to that qubit. 

_Entanglement distillation._ Suppose that nodes _A_ and _B_ wish to perform the distill protocol, which starts by _A_ and _B_ sharing an electron-electron pair (correction Paulis _PA_<sup>_e_and</sup><sup>_P e_</sup> _B_<sup>atnode</sup><sup>_A_and</sup><sup>_B_,respectively)</sup> and a nuclear-nuclear pair ( _PA_<sup>_n_and</sup><sup>_P n_</sup> _B_<sup>). In the protocol, first both nodes apply</sup><sup>_P n ·P e_to their electron spin</sup> qubit. Then, both nodes locally perform the distillation circuit from Supplementary Figure 17(c), followed by sending both the measurement outcome and _P_<sup>_n_</sup> to the other node. The nodes determine whether the distillation succeeded using the condition explained in section 5. In case of failure, the nuclear-nuclear state is discarded. In case of success, one of the nodes in the chain (for example, the one with the lower position index in the chain) sets _P_<sup>_n_</sup> = 11, while the other sets 



Below, in section 6 B of this Supplementary Note, we show that after this procedure, eq. (62) still holds. 

_Entanglement swapping._ Suppose that node _M_ wants to execute the swap protocol on shared pairs _A − M_ and _M − B_ , with nodes _A_ and _B_ respectively. We denote _M_ ’s correction Paulis as _PM_<sup>_A_and</sup><sup>_P B_</sup> _M_<sup>.First,</sup><sup>_M_</sup> performs the Bell-state measurement circuit from Supplementary Figure 17(d). Let us denote the individual measurement outcomes of the circuit as _m_ earlier and _m_ later (both take values from _{_ 1 _, −_ 1 _}_ ), which correspond to the measured Bell state _|φ_ [ _a, b_ ] _⟩_ with _a_ = _−_ 1 _· m_ earlier _· m_ later and _b_ = _m_ later. Then, _M_ sends the Pauli 11 to _A_ , while to _B_ it sends _PM_<sup>_A· P B_</sup> _M_<sup>_· Q_,where</sup><sup>_Q_isgivenby</sup> 



Both nodes _A_ and _B_ multiply their local Pauli with the Pauli they received from _M_ . The proof that after the swap, eq. (62) still holds can be found below in section 6 C of this Supplementary Note. 

## **B. Correctness proof of the correction operator update for distill** 

Here, we prove that eq. (62) holds for the states that are outputted by the protocols for entanglement distillation and swapping explained above. 

Let us start with entanglement distillation. For this, we denote by ‘physical nuclear-nuclear state’ the joint state of the nuclear spins of node _A_ and _B_ . By direct computation, one can show the following. 

**Proposition 1.** _Suppose that nodes A and B share the state |φ_ [ _a, b_ ] _⟩ on the electrons and the physical nuclear-nuclear state |φ_ [ _c, d_ ] _⟩, where a, b, c, d ∈{_ 1 _, −_ 1 _}. When both nodes execute the distillation circuit from Supplementary Figure 17(c), the resulting state on the carbon nuclear spins is_ 



_and the measurement outcome m_ 1 _∈{_ 1 _, −_ 1 _} on one side is uniformly random, while the outcome of the other node equals m_ 2 = _m_ 1 _· b · c._ 

We emphasise that using the correction-operator tracking for the store and retrieve operations as described in section 6 A of this Supplementary Note, the physical nuclear-nuclear state between any two nodes does not satisfy eq. (62). The reason for this is that the store operation maps the electron spin state to the nuclear spin in a rotated basis, where the rotation operator is a Hadamard gate _H_ (eq. 51). However, the correction operators are not updated when the store is applied (see ‘Storing and retrieving qubits’ in section 6 A). Consequently, if nodes _A_ and _B_ share the physical nuclear-nuclear state _|ψ⟩_ , then mapping _|ψ⟩_ 

36 

to the reference Bell state _|φ_ [1 _, −_ 1] _⟩_ requires first the application of _H ⊗ H_ , followed by applying _PA ⊗ PB_ . By ‘virtual nuclear-nuclear state’, we mean the state _|ψ_<sup>_′_</sup> _⟩_ = ( _H ⊗ H_ ) _|ψ⟩_ , i.e. the state that satisfies eq. (62). Let us first convert Prop. 1 to a statement with the virtual-virtual nuclear state. 

**Proposition 2.** _Suppose nodes A and B share the electron-electron state |φ_ [ _a, b_ ] _⟩ and the virtual nuclearnuclear state |φ_ [ _c, d_ ] _⟩. Then after the distillation circuit from Supplementary Figure 17(c), the virtual state on the nuclear spins after performing the distillation equals_ 



_and the measurement outcomes are m_ 1 _∈{_ 1 _, −_ 1 _} (uniformly random) and m_ 2 = _m_ 1 _· b · d._ 

_Proof._ The virtual nuclear-nuclear state and the physical one are related by _H ⊗ H_ . It is not hard to see that _H ⊗ H |φ_ [ _x, y_ ] _⟩_ = _|φ_ [ _y, x_ ] _⟩_ for any _x, y ∈{_ 1 _, −_ 1 _}_ . Applying this to Prop. 1 results in the measurement outcomes _m_ 1 (uniformly random) and _m_ 2 = _m_ 1 _·b·d_ and resulting physical nuclear-nuclear state _|φ_ [ _d, −acd_ <u>]</u> _<u>⟩</u>_ . Obtaining the virtual state is done by applying _H ⊗ H_ again, which yields _|φ_ [ _−acd, d_ ] _⟩_ . 

Using Prop. 2, it is straightforward to check that the output state of the distillation protocol from section 6 A satisfies eq. (62). 

Suppose _A_ and _B_ share the electron-electron state _|φ_ [ _a, b_ ] _⟩_ and the virtual nuclear-nuclear state _|φ_ [ _c, d_ ] _⟩_ for some _a, b, c, d ∈{_ 1 _, −_ 1 _}_ , with correction Paulis _PA_<sup>_e_(</sup><sup>_P_</sup> _B_<sup>_e_)and</sup><sup>_P n_</sup> _A_<sup>(</sup><sup>_P_</sup> _B_<sup>_n_)for</sup><sup>_A_(</sup><sup>_B_).Inthefirststepofthe</sup> protocol, _A_ and _B_ apply _P_<sup>_n_</sup> _· P_<sup>_e_</sup> to the electron-electron state, resulting in the electron-electron state 



where we made use of the fact that each Pauli squares to 11. In case of successful distillation, the virtual nuclear-nuclear state can be found using Prop. 2 and equals _|φ_ [ _−ccd, d_ ] _⟩_ = _|φ_ [ _−d, d_ ] _⟩_ . What remains is to determine the correction operators conditioned on the value of _d_ . If _d_ = 1, then the correction operators are 11 for one node and _Y_ for the other (since 11 _⊗ Y |φ_ [ _−_ 1 _, −_ 1] _⟩_ equals the target Bell state _|φ_ [1 _, −_ 1] _⟩_ ), while for _d_ = _−_ 1 the resulting state is already the target Bell state and both correction operators should be 11. Determining the value of _d_ can be done by using the fact that eq. (62) was satisfied by the pre-distillation virtual nuclear-nuclear state, 



and thus _|φ_ [ _c, d_ ] _⟩_ = _PA_<sup>_n⊗P n_</sup> _B_<sup>_|φ_[1</sup><sup>_, −_1]</sup><sup>_⟩_.Fromcheckingallpossiblecasesof</sup><sup>_P n_</sup> _A_<sup>and</sup><sup>_P n_</sup> _B_<sup>wefindthat</sup><sup>_d_=1</sup> precisely if one of _PA_<sup>_n, P_</sup> _B_<sup>_n_equals</sup><sup>_X_or</sup><sup>_Y_,whiletheotherequals11or</sup><sup>_Z_.</sup> 

## **C. Correctness proof of the correction operator update for swap** 

Here we show that eq. (62) holds for the state between nodes _A_ and _B_ after node _M_ has performed an entanglement swap on Bell states _A − M_ and _M − B_ . Let us denote _A_ ’s ( _B_ ’s) correction operator as _PA_ ( _PB_ ) and _M_ ’s correction operator as _PM_<sup>_A_(</sup><sup>_P B_</sup> _M_<sup>)forthestateitshareswithnode</sup><sup>_A_(</sup><sup>_B_).Thatis,intheideal</sup> case, the nodes hold the state 



We will make use of the fact that 



for single-qubit Paulis _P, Q_ and _a, b ∈{_ 1 _, −_ 1 _}_ , where _≡_ as before indicates that the two states differ only by a complex factor of norm 1 (in fact, for eq.(66) we can restrict this to a multiplicative factor _±_ 1). Using eq. (66), we rewrite eq. (65) to 



Eq. (67) implies that we may assume that _M_ ’s two correction operators are both 11. Thus _M_ only needs to communicate the correction operator that corresponds to having measured one qubit of each pair of the pair _|φ_ [1 _, −_ 1] _⟩⊗|φ_ [1 _, −_ 1] _⟩_ . The resulting correction operator _Q_ can be straightforwardly worked out in a similar way as in [111] and the result is given in 64. The state after the entanglement swap is thus 



37 

which we rewrite using eq. (66) to 



Indeed, _PA_ and _PM_<sup>_AP B_</sup> _M_<sup>_PBQ_are(modulopossiblefactor</sup><sup>_−_1)thecorrectionoperatorsofnode</sup><sup>_A_and</sup><sup>_B_,</sup> respectively, after finishing the entanglement swapping protocol described above in section 6 A of this Supplementary Note. 

What remains is to convert the measurement outcomes from the circuit from Supplementary Figure 17(d) to the measured Bell state. For this, a direct computation shows that applying the circuit to the electronnuclear state (11 _e ⊗ Hn_ ) _|φ_ [ _a, b_ ] _⟩_ (the Hadamard gate _H_ is needed since the nuclear qubit lives in a rotated basis, see section 5) yields the measurement outcomes _m_ earlier = _−ab_ and _m_ later = _b_ . Rewriting gives _a_ = _−m_ earlier _m_ later and _b_ = _m_ later. 

## **Supplementary Note 7: Atomic Ensemble physical modelling** 

Here, we provide the details of the simulation comparing different memory technologies for atomic-ensemble quantum repeaters, whose results are presented in section Performance comparison between two atomicensemble memory types through NetSquid’s modular design of the Result. For a more detailed discussion see [112]. 

## **A. Generating end-to-end entanglement with Atomic Ensembles** 

In our experiment we simulate the protocol proposed by Sinclair et al. [113] and analysed in detail by Guha et al. [19]. However, in our simulation we go further than any previous analysis by not only including dark counts and detector efficiency but also multi-photon emissions, photon distinguishability and time-dependent memory efficiency. For a detailed review of different atomic-ensemble protocols see Sangouard et al. [114]. Let us briefly review the main points necessary to understand our results. 

## _a. The protocol_ 

The simulation setup consists of two elementary links connected by a quantum repeater station. Each elementary link contains two photon-pair sources sending one half of the produced state to a midpoint station through optical fibres. We assume that the speed of all photons and classical communication is _c/nri_ , where _c_ is the speed of light in vacuum and _nri_ = 1 _._ 44 is the refractive index of glass [100]. The midpoint station contains a 50:50 beam splitter and two photon detectors to perform a linear-optical Bell state measurement (BSM) [114]. Detection of a single photon per time-bin heralds successful elementary link entanglement generation. By performing the entanglement attempts on the elementary link simultaneously in multiple modes _M_ (e.g. different temporal, spatial or frequency modes) the probability of successfully generating elementary link entanglement can be greatly increased as _p_ = 1 _−_ (1 _− psingle−mode_ )<sup>_M_</sup> . This is called multiplexing. 

The repeater station also contains two quantum memories, which store the second half of the quantum state emitted by the adjacent sources. 

If both elementary links herald a successful BSM at their respective midpoint station, the successful modes are extracted from the memories. Another BSM is then performed on those modes at the repeater station. The second halves of the quantum state at the end nodes are measured directly in either the X or Z basis without storing them on a memory first. 

The photon-pair source generates a time-bin encoded superposition of photon pairs with a joint quantum state given by [75] 



where 



38 

Here _p_ ( _n_ ) is the probability to generate _n_ pairs and a state _|n − m, m_ ; _n − m, m⟩_ describes _n − m_ photons travelling to the left (/right) side in the early and _m_ in the late time window. Photon loss in the optical fibres is modelled following the beam-splitter-attenuator channel [115], which is also referred to as generalised amplitude damping [116]. Such a channel performs the map _ρ �→_<sup>�</sup><sup>_∞_</sup> _k_ =0<sup>_AkρA†_</sup> _k_ where the Kraus operator _Ak_ corresponds to the case where exactly _k_ photons are lost and is given by 



where _γ_ is the probability of losing a photon. 

For the quantum channel it depends on the fibre attenuation _α_ , the channel length _L_ and the coupling loss _γchan_ (0) as _γchan_ ( _L_ ) = 1 _−_ (1 _− γchan_ (0)) _×_ 10<sup>_−αL/_10</sup> . 

The linear-optical BSM is modelled as a set of POVMs which include non-unit Hong-Ou-Mandel dip visibility (photon distinguishability), detection efficiency and dark counts. We calculate them as a set of perfect POVMs _Mmn_ and then derive the set of effective POVMs _Mkl_<sup>_′_= �</sup> _mn_<sup>_p_(</sup><sup>_mn →kl_)</sup><sup>_Mmn_, where</sup><sup>_p_(</sup><sup>_mn →kl_)</sup> is the probability that an imperfect BSM measures _m_ (/ _n_ ) photons arriving on a detector as _k_ (/ _l_ ) due to dark counts and detection inefficiency. For a complete derivation of the POVM elements see [112]. The quantum memory is also modelled as a quantum channel with generalised amplitude damping using the same operators _Ak_ . However, here the probability of losing the photon _γ_ depends on the time _t_ that the quantum state spent on the memory, the maximum memory efficiency _η_ (at _t_ = 0) and the memory lifetime _τ_ . The memory efficiency then decays either exponentially (AFC) or Gaussian (EIT) with _t/τ_ and _γ_ behaves as 



For a more detailed discussion of the protocol and the reasoning behind our model please see our upcoming work [112]. 

## _b. The figures of merit_ 

In order to compare the two memory technologies, we also need to define figures of merit we want to investigate. To this end we choose the secret key rate (SKR) obtainable for quantum key distribution using the BB84 protocol [76], the quantum bit error rate (QBER) and the average number of attempts per successful end node measurement. 

For the QBER we compare the end node measurement outcomes with the expected correlations in each basis. The fraction of wrong bits among the measurement outcomes in each basis is then called the QBER and is determined by performing end node measurements in either X or Z basis The secret key rate _RSK_ is then computed as 



where _H_ ( _x_ ) = _−x_ log( _x_ ) _−_ (1 _− x_ ) log(1 _− x_ ) is the binary entropy, _Qx, Qz_ are the QBERs in the X and Z bases and _AS_ is the average number of attempts per successful end-to-end entanglement generation. The factor 1 _/_ 2 (in eq. 75 and eq. 76) accounts for the fact that in the BB84 protocol the two end nodes randomly choose between measuring in X or Z basis and therefore only measure in the same basis in 1 _/_ 2 of the successful entanglement generations. 

Errors for the number of attempt are calculated from the standard deviation of the mean. The error on the secret key rate is computed as follow from the error on the number of attempts per success ∆ _AS_ and the errors ∆ _Qx_ and ∆ _Qz_ on the QBER in X and Z basis respectively: 



## **B. Atomic Frequency Comb and Electronically Induced Transparency quantum memories** 

In this work, we study two promising types of atomic-ensemble memories, both based upon photon absorption: electronically induced transparency (EIT) quantum memories as an example of an optical control 

39 

protocol and atomic frequency comb (AFC) memories as an example for an engineered absorption protocol. For a more detailed comparison of these two types of memories see [112]. AFC memories are very promising due to their great potential for multiplexing, while EIT memories promise superior efficiency with limited multiplexing. Here we will give a brief overview of both technologies. 

## _a. AFC_ 

AFC memories require an inhomogeneously broadened material (e.g. rare-earth-doped crystals) with equidistant peaks in occupation density created by spectral hole burning [72]. When a photon is absorbed by the memory, the system will be in a collective delocalised state (Dicke state [117]) which then rapidly dephases with time. After a fixed time the Dicke state rephases and the absorbed photon is re-emitted. The retrieval efficiency decreases exponentially with storage time. Due to the large linewidth of the inhomogeneously broadened state, AFC memories have great potential for massive multiplexing as the number of modes is not limited by the optical depth of the material. Currently, the efficiencies that have been experimentally achieved are up to 58% [118] reported for a cavity-enhanced AFC protocol and around 8.5% [119, 120] for most multiplexed memories. Memory lifetimes of up to 0.53 s [121] have been reported for a dynamically decoupled AFC protocol (however with an efficiency of just 0.5%). In our simulation we set a maximum memory efficiency of 45% (currently optimistic value for multimode memories, but still below the highest demonstrated single-mode storage [118]) with 1000 modes, consisting of 50 spectral and 20 temporal modes (15 x 9 already demonstrated [119], over 1000 total modes also demonstrated [122]), and a lifetime of 1 ms (0.542 ms already achieved for multimode on-demand AFC memory [120]). 

## _b. EIT_ 

EIT [123] is an effect where an opaque sample of atomic-ensembles becomes transparent due to interaction with electromagnetic fields. This creates a steep dispersion which in turn affects the group velocity of incoming light. The effect can be used to slow or completely stop and later re-emit incoming photonic states. Due to the use of a strong resonant control laser to store the incoming light, these kind of memories are subject to background noise in the form of additional photons introduced by the control beam. These additional photons need to be compensated by filtering. Another disadvantage is that multiplexing in EIT is limited to using only the spatial degree of freedom, thus making it more difficult to realise a highly multiplexed protocol. The great advantage of these memories is the high efficiency of 85% [124] at a memory lifetime of 15 _µ_ s. In our simulation we set a maximum efficiency of 90% (within reach of [124]) with 1000 spatial modes (experimentally 2 spatial modes have been demonstrated [125]), and a lifetime of 100 _µ_ s ([124] gives 200 _µ_ s as a theoretical limit) . For a review of EIT see [73]. 

## **C. Parameters** 

For the comparison we used the optimistic elementary link parameters taken from [19](Fig 10 (g)). We then added optimistic values for the the memory parameters (see above) and the additional noise parameters we use, such as the photon visibility. In line with the analysis of [19], we model the source as an almost perfect single-pair source with a small probability _p_ (2) of emitting two pairs. 

We first list the common parameters of both simulations before we compare the parameters for the memory components in Supplementary Table III. It is worth pointing out that using the same number of modes for both technologies slightly biases this comparison as the high multiplexing potential is the main advantage of AFC memories. 

- Source total number of modes (spectral x temporal x spatial) = 1000 

- Source emission probabilities: _p_ (0) = 1 _− p_ (1) _− p_ (2), _p_ (1) = 0 _._ 9, _p_ (2) = 0 _._ 013 (see eq.71) 

- Fibre coupling loss probability _γchan_ (0) = 0 

- Fibre attenuation _α_ = 0 _._ 15dB/km 

- Visibility = 0.9 

- Detector dark count probability = 10<sup>_−_6</sup> 

- Detector detection efficiency = 90% 

- Detectors number-resolving: No 

40 

||**AFC**|**EIT**|
|---|---|---|
|spectral modes|50|1|
|temporal modes|20|1|
|spatial modes|1|1000|
|maximum efciency (_t_= 0)|45%|90%|
|memory lifetime|1 ms|0.1 ms|
|time dependence|exponential|Gaussian|



Supplementary Table III: **Parameters for the two different atomic-ensemble memory technologies.** 

41 

