week ending 25 NOVEMBER 2011 

P H Y S I C A L R E V I E W L E T T E R S 

PRL 107, 220501 (2011) 

# Hybrid Quantum Circuit with a Superconducting Qubit Coupled to a Spin Ensemble 

Y. Kubo,<sup>1</sup> C. Grezes,<sup>1</sup> A. Dewes,<sup>1</sup> T. Umeda,<sup>2</sup> J. Isoya,<sup>2</sup> H. Sumiya,<sup>3</sup> N. Morishita,<sup>4</sup> H. Abe,<sup>4</sup> S. Onoda,<sup>4</sup> T. Ohshima,<sup>4</sup> V. Jacques,<sup>5</sup> A. Dre´au,<sup>5</sup> J.-F. Roch,<sup>5</sup> I. Diniz,<sup>6</sup> A. Auffeves,<sup>6</sup> D. Vion,<sup>1</sup> D. Esteve,<sup>1</sup> and P. Bertet<sup>1</sup> 

> 1Quantronics group, SPEC (CNRS URA 2464), IRAMIS, DSM, CEA-Saclay, 91191 Gif-sur-Yvette, France 

> 2Research Center for Knowledge Communities, University of Tsukuba, Tsukuba 305-8550, Japan 

> 3Sumitomo Electric Industries Ltd., Itami 664-001, Japan 

> 4Japan Atomic Energy Agency, Takasaki 370-1292, Japan 

> 5LPQM (CNRS UMR 8537), ENS de Cachan, 94235 Cachan, France 

> 6Institut Ne´el, CNRS, BP 166, 38042 Grenoble, France 

(Received 19 October 2011; published 21 November 2011) 

We report the experimental realization of a hybrid quantum circuit combining a superconducting qubit and an ensemble of electronic spins. The qubit, of the transmon type, is coherently coupled to the spin ensemble consisting of nitrogen-vacancy centers in a diamond crystal via a frequency-tunable superconducting resonator acting as a quantum bus. Using this circuit, we prepare a superposition of the qubit states that we store into collective excitations of the spin ensemble and retrieve back into the qubit later on. These results constitute a proof of concept of spin-ensemble based quantum memory for superconducting qubits. 

DOI: 10.1103/PhysRevLett.107.220501 

PACS numbers: 03.67.Lx, 42.50.Ct, 42.50.Pq, 85.25.Cp 

Present-day implementations of quantum information processing rely on two widely different types of quantum bits (qubits). On the one hand, microscopic systems such as atoms or spins are naturally well decoupled from their environment and as such can reach extremely long coherence times [1,2]; on the other hand, more macroscopic objects such as superconducting circuits are strongly coupled to electromagnetic fields, making them easy to entangle [3,4] although with shorter coherence times [5,6]. It thus seems appealing to combine the two types of systems in hybrid structures that could possibly take the best of both worlds. 

But if superconducting qubits have been successfully coupled to electromagnetic [7] as well as mechanical [8] resonators, coupling them to microscopic systems in a controlled way has up to now remained an elusive perspective—even though qubits sometimes turn out to be coupled to unknown and uncontrolled microscopic degrees of freedom with relatively short coherence times [9]. Whereas the coupling constant g of one individual microscopic system to a superconducting circuit is usually too weakN such systems are coupled with a constantfor quantum information applications, ensembles gpfN enhancedof by collective effects. This makes possible to reach a regime i f of strong coupling between one collective variable of the ensemble and the circuit. This collective variable, which behaves in the low excitation limit as a harmonic oscillator, has been proposed [10–13] as a quantum memory for storing the state of superconducting qubits. Experimentally, the strong coupling between an ensemble of electronic spins and a superconducting resonator has been demonstrated spectroscopically [14–16], and the storage of a microwave field into collective excitations of a 

spin ensemble has been observed very recently [17,18]. These experiments were however carried out in a classical regime since the resonator and spin ensemble behaved as two coupled harmonic oscillators driven by large microwave fields. In the perspective of building a quantum memory, it is instead necessary to perform experiments at the level of a single quantum of excitation. For that purpose, we integrate on the same chip three different quantum systems: an ensemble of electronic spins, a superconducting qubit, and a resonator acting as a quantum bus between the qubit and the spins. A sketch of the experiment is shown in Fig. 1. 

The spin ensemble N-V consists of �10<sup>11</sup> negatively charged nitrogen vacancy (NV) color centers [19] in a diamond crystal. These centers have an electronic spin S ¼ 1, with electron spin resonance (ESR) transition frequencies !�=2� ’ 2:88 GHz between energy levels mS ¼ 0 and mS ¼ �1 in zero magnetic field [see Fig. 1(c)]. The electronic spin of the NV center is further coupled by hyperfine (HF) interaction to the spin-one<sup>14</sup> N nucleus, which splits !� into three peaks separated by 2.2 MHz [20,21]. In our experiment, the diamond crystal is glued on top of the chip, and the degeneracy between states mS ¼ �1 is lifted with a BNV ¼ 1:4 mT magnetic field applied parallel to the chip and along the [1, 1, 1] crystalline axis. The NV frequencies being sensitive only to the projection of BNV along the NVaxis, two groups of NVs thus experience different Zeeman effects: those along [1,1,1] (denoted I) and those along either of the three other h1; 1; 1i axes (denoted III as they are 3 times more numerous). This results in four different ESR frequencies !�I;�III. 

The qubit Q is a Cooper-pair box of the transmon type [5,22] with transition frequency !Q between its ground 

0031-9007=11=107(22)=220501(5) 

220501-1 

� 2011 American Physical Society 



<!-- Start of picture text -->
—<br>RET<br>Ko<br><!-- End of picture text -->



[)} 

[)} 

(0) 

db 

(6) 

week ending 25 NOVEMBER 2011 

P H Y S I C A L R E V I E W L E T T E R S 

PRL 107, 220501 (2011) 

state �jgi þ �jei into the corresponding photonic state �j0iB þ �j1iB of the bus, leaving the qubit in jgi. This SWAP gate could be performed by tuning !B in resonance with !Q for a duration �=2gQ [26]. Here we prefer instead to adiabatically sweep !B across !Q as this sequence is more immune to flux noise in the SQUID loop of B [21]. This adiabatic SWAP (aSWAP) achieves the same quantum operation as the resonant SWAP except for an irrelevant dynamical phase. The experiments then proceed by combining single-qubit rotations, aSWAP gates, and flux pulses placing B and N-V in and out of resonance for properly chosen interaction times �. 

We apply such a sequence with the qubit initially prepared in jei (see Fig. 2). A first aSWAP converts jei into the bus Fock state j1iB; B is brought in or near resonance with the spin ensemble for a duration �; the resulting B state is then transferred back into the qubit, which is finally readout. Figure 2(b) shows the resulting curves Peð�Þ when the bus is brought in resonance either with !�III or !�I. An oscillation in Pe is observed, revealing a storage in the spin ensemble of the single quantum of excitation initially in the qubit at �s;III ¼ 65 ns or �s;I ¼ 97 ns, and a retrieval back into the qubit at �r;III ¼ 116 ns or �r;I ¼ 146 ns. The fidelity of this storage-retrieval process, defined as 



<!-- Start of picture text -->
b 0.05 P e 0.20 c<br><!-- End of picture text -->



<!-- Start of picture text -->
0.4 ω-III<br>τs,III<br>ω+I<br>0.2 τr,III<br>ω+III<br>0.4 ω-I<br>τs,I ω-III<br>0.2 τr,I<br>ω-I<br>0 200 400 600 200 400<br><!-- End of picture text -->

FIG. 2 (color online). Storage and retrieval of a single quantum of excitation from the qubit to the spin ensemble. (a), Experimental sequence showing the microwave pulses used for exciting the qubit in jei (� pulse) and for reading it out (R pulse), as well as transition frequencies of the quantum bus (B), qubit (Q), and spins (N-V). (b), Experimental (red dots) and theoretical (black line—see text) probability Peð�Þ for !B tuned to !�III (top) or !�I (bottom), showing the storage and retrieval times �s and �r. (c), Two-dimensional plot of Pe versus interaction time � and flux pulse height �, showing resonance with the four spin groups. Chevron-like patterns are observed, showing a faster oscillation with reduced amplitude when !B is detuned from the spin resonance, as expected. Note that the difference between the !� and !þ patterns in the same NV group is simply caused by the nonlinear dependence of !B on � [25]. 

Peð�rÞ=Peð0Þ, is 0.14 for group III and 0.07 for group I. These relatively low values are not due to a short spin dephasing time, but rather to an interference effect caused by the HF structure of NV centers, as evidenced by the nonexponential damping observed in Peð�Þ. These measurements are accurately reproduced by a full calculation of the spin-resonator dynamics [18,21,27,28] taking into account this HF structure, with the linewidth of each HF peak as the only adjustable parameter. A linewidth of 1.6 MHz is in this way determined for the spins in group I [21], and of 2.4 MHz for group III. This larger value is due to a residual misalignment of BNV from the [1,1,1] crystalline axis causing each of the three h1; 1; 1i NV orientations noncollinear with the field to experience slightly different Zeeman shifts. We finally note that in both curves shown in Fig. 2(b) Peð�Þ tends towards 0.08 at long times, as is also found with the qubit initially in jgi. This proves that the collective spin variable coupled to B is, as requested for experiments in the quantum regime, in its ground state j0i�I;�III with a large probability �0:92 at equilibrium, which corresponds to a temperature of �50 mK. Varying both !B and � with the same pulse sequence, we observe similar storage-retrieval cycles at all four spin frequencies [see Fig. 2(c)]. 

In addition to storing a single excitation from the qubit, one has to test if a coherent superposition of states can be transferred to the spin ensemble and retrieved. For that, we now perform the aSWAP and bring !B in resonance withf !�I after having prepared the qubit in ðjgi þ jeiÞ=p2 instead of jei, and we reconstruct the Bloch vector of the iffi qubit by quantum state tomography at the end of the sequence (see Fig. 3). More precisely, we measure h�Xi, h�Yi and h�Zi by using �=2 rotations around Y, X, or no rotation at all (I) prior to qubit readout. After substracting a trivial rotation around Z occurring at frequency (!�I � !Q), we reconstruct the trajectory of this Bloch vector as a function of the interaction time �. It is plotted in Fig. 3, together with the off-diagonal element �ge of the final qubit density matrix, which quantifies its coherence. We find that no coherence is left in the qubit at the end of the sequence for � ¼ �s;I, as expected for a full storage of the initial state into the ensemble. Then, coherence is retrieved at � ¼ �r;I, although with an amplitude �5 times smaller than its value at � ¼ 0 (i.e., without interaction with the spins). Note the � phase shift occurring after each storage-retrieval cycle, characteristic of 2� rotations in the two-level space fj1B; 0�Ii; j0B; 1�Iig. The combination of the results of Figs. 2 and 3 demonstrates that superpositions of the two qubit states can be stored and retrieved in a spin ensemble—although with limited fidelity—and thus represents a proof-of-concept of a spin-based quantum memory for superconducting qubits. 

To evaluate the time during which quantum coherence can be stored in the ensemble, we perform a Ramsey-like experiment on the spin ensemble at the single-photon level 

220501-3 

week ending 25 NOVEMBER 2011 

P H Y S I C A L R E V I E W L E T T E R S 

PRL 107, 220501 (2011) 



<!-- Start of picture text -->
a N-V<br>X(π/2) τ I, X,Y R<br>Q<br>aSWAP<br>B<br>0.4 0.4<br>b c<br>0.2 τs,I 0.2<br>τr,I<br>0.0<br>180<br>-0.2 0<br>X<br>-0.4 -180<br>-0.2 0 0.2 0 100 200 300 400<br>-<σy> Interaction time τ (ns)<br>|ge<br>ρ<br>2|<br>><br>x<br>σ<br><<br>)ge<br>ρ<br>arg(<br><!-- End of picture text -->

FIG. 3 (color online). Storage and retrieval of a coherent superposition of states from the qubit to the spin ensemble. (a)�=2Experimental pulse in state ðjpulsegi þ jsequence:eiÞ=pf2, which is transferred tothe qubit is prepared B by anby a aSWAP. Bus B is then immediately tuned to !�I=2� ¼ iffi 2:84 GHz for an interaction time �. The quantum state of B is then transferred back to the qubit by a second aSWAP. Quantum state tomography is finally performed to determine the qubit state by applying either I, X, or Y operation to the qubit. (b), Trajectory of the qubit Bloch vector on the Bloch sphere (bottom inset), and its projection on the equatorial plane. (c), Modulus and phase of the off-diagonal element �ge of the qubit density matrix as a function of interaction time �. 

(see Fig. 4): we initially prepare the qubit in jei, transfer its state to B, then tune !B to !�I for a duration ��=2 ¼ �s;�I=2, after which !B is suddenly detuned by �!=2� ¼ 38 MHz for a time �. At this point, the joint bus-spin ensemble statef is an entangled state ðj1B; 0�Ii þ e<sup>i’</sup> j0B; 1�IiÞ=p2 with a phase ’ ¼ �!�. Bus B is then put back in resonance with the spins for a second interaciffi tion of duration ��=2 that converts the phase ’ into population of j1B; 0�Ii. This population is finally transferred to the qubit, and readout. Oscillations at frequency �! are observed in Peð�Þ as seen in Fig. 4, confirming that the resonator and the spins are entangled after the first halfswap pulse. These oscillations are modulated by a beating pattern, with an overall damping of the oscillations envelope in �200 ns. Quite remarkably, this beating observed in the qubit excited state probability is directly caused by the HF structure of NV centers, as proved by the Fourier transform of Peð�Þ which shows the three HF lines. The full calculation of the system dynamics quantitatively captures both the beatings and the oscillations damping, which is thus completely explained by the 1.6 MHz inhomogeneous linewidth of each HF line taken into account in the theory. 



<!-- Start of picture text -->
a N-V<br>π τπ/2 δω τπ/2 R<br>τ<br>Q<br>aSWAP<br>B<br>b 0.5<br>0.4<br>0.3 30 35 40 45<br>Frequency (MHz)<br>0.2<br>0 200 400 600<br>Delay time, τ (ns)<br>e<br>P<br>FFT amp (a.u.)<br>Excited state probability,<br><!-- End of picture text -->

FIG. 4 (color online). Ramsey-like experiment on the spin ensemble at the single-photon level. (a), Experimental pulse sequence: the qubit is prepared in its excited state jei by a � pulse; the state je; 0Bi is then adiabatically transferred to jg; 1Bi by an aSWAP. A fast flux pulse subsequently brings !B onto !�I, and then lets B and the spins from group �I interact for half a swap time ��=2 ¼ �s;I=2, generating an entangled state of the two systems. B is then detuned from the spins by �!=2� ¼ 38 MHz during a time �, and a second half-swap is performed. The quantum state of B is then transferred back to the qubit, which is finally readout. (b), Measured (red circles) and calculated (black line—see text) probability Peð�Þ, as well as the Fourier transform of the experimental data (inset) revealing the NV centers HF structure. 

The previous results suggest that the storage of quantum information in the NV centers ensemble is at present limited both by its HF structure and by the inhomogeneous broadening of its resonance. This broadening is attributed to dipolar interactions between the NV centers and residual paramagnetic impurities (likely neutral nitrogen atoms) in the diamond crystal. Crystals having a nearly complete conversion of the nitrogen into NV centers should thus greatly improve the present performance of our device. Note that the hyperfine coupling to the nuclear spin of 14N could be turned into a useful resource if quantum information was transferred from the electron spin to the nuclear spin degree of freedom, which has much narrower linewidth. Finally, refocusing techniques borrowed from quantum memories in the optical domain [29] should also lead to increase in the storage time by 2 orders of magnitude. 

In conclusion our experiments bring a proof of concept of a spin-based quantum memory for superconducting qubits. In a longer-term perspective, they open the way to the implementation of genuine quantum lab on chips, where superconducting qubits would coherently interact with electron and nuclear spins as well as optical photons. 

We acknowledge useful discussions with K. Moelmer, F. Jelezko, J. Wrachtrup, D. Twitchen, and within the Quantronics group, and technical support from P. Se´nat, 

220501-4 

week ending 25 NOVEMBER 2011 

P H Y S I C A L R E V I E W L E T T E R S 

PRL 107, 220501 (2011) 

P.-F. Orfila, T. David, J.-C. Tack, P. Pari, P. Forget, and M. de Combarieu. We acknowledge support from European project Solid, ANR projects Masquelspec and QINVC, C’Nano, Capes, and Fondation Nanosciences de Grenoble. 

Note added.—After redaction of this work, a related work reporting the coupling of a flux qubit to an ensemble of NV centers was published [30]. 



- [1] C. F. Roos et al., Phys. Rev. Lett. 92, 220402 (2004). 

- [2] G. Balasubramanian et al., Nature Mater. 8, 383 (2009). 

- [3] L. DiCarlo et al., Nature (London) 467, 574 (2010). 

- [4] M. Neeley et al., Nature (London) 467, 570 (2010). 

- [5] J. A. Schreier et al., Phys. Rev. B 77, 180502 (2008). 

- [6] H. Paik et al., arXiv:1105.4652 [Phys. Rev. Lett. (to be published)]. 

- [7] A. Wallraff et al., Nature (London) 431, 162 (2004). 

- [8] A. D. O’Connell et al., Nature (London) 464, 697 (2010). 

- [9] M. Neeley et al., Nature Phys. 4, 523 (2008). 

- [10] A. Imamoglu, Phys. Rev. Lett. 102, 083602 (2009). 

- [11] J. H. Wesenberg et al., Phys. Rev. Lett. 103, 070502 (2009). 

- [12] D. Marcos et al., Phys. Rev. Lett. 105, 210501 (2010). 

- [13] W. L. Yang, Z. Q. Yin, Y. Hu, M. Feng, and J. F. Du, Phys. Rev. A 84, 010301 (2011). 

- [14] Y. Kubo et al., Phys. Rev. Lett. 105, 140502 (2010). 

- [15] D. I. Schuster et al., Phys. Rev. Lett. 105, 140501 (2010). 

- [16] R. Amsuss et al., Phys. Rev. Lett. 107, 060502 (2011). 

- [17] H. Wu et al., Phys. Rev. Lett. 105, 140503 (2010). 

- [18] Y. Kubo et al., arXiv:1109.3960. 

- [19] F. Jelezko, T. Gaebel, I. Popa, A. Gruber, and J. Wrachtrup, Phys. Rev. Lett. 92, 076401 (2004). 

- [20] S. Felton et al., Phys. Rev. B 79, 075203 (2009). 

- [21] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.107.220501 for details and five supplementary figures. 

- [22] J. Koch et al., Phys. Rev. A 76, 042319 (2007). 

- [23] F. Mallet et al., Nature Phys. 5, 791 (2009). 

- [24] M. Sandberg et al., Appl. Phys. Lett. 92, 203501 (2008). 

- [25] A. Palacios-Laloy et al., J. Low Temp. Phys. 151, 1034 (2008). 

- [26] M. Hofheinz et al., Nature (London) 454, 310 (2008). 

- [27] I. Diniz et al., arXiv:1101.1842. 

- [28] Z. Kurucz, J. H. Wesenberg, and K. Molmer, Phys. Rev. A 83, 053852 (2011). 

- [29] A. I. Lvovsky, B. C. Sanders, and W. Tittel, Nat. Photon. 3, 706 (2009). 

- [30] X. Zhu et al., Nature (London) 478, 221 (2011). 

220501-5 

