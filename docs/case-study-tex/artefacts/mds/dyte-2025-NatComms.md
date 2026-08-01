https://doi.org/10.1038/s41467-025-66948-6 



### Article 

# Storing quantum coherence in a quantum dot nuclear spin ensemble for over 100 milliseconds 

Received: 2 June 2025 Accepted: 19 November 2025 Check for updates 





Harry E. Dyte 1, Santanu Manna 2,4, Saimon F. Covre da Silva 2,5, Armando Rastelli 2 & Evgeny A. Chekhovich 3 

States with long coherence are a crucial requirement for qubits and quantum memories. Nuclear spins in epitaxial GaAs/AlGaAs quantum dots are a great candidate, offering excellent isolation from external environments and ondemand coupling to optical flying qubits. However, coherence times are limited to ≲ 1 ms by the dipole-dipole interactions between the nuclei and by the nuclear quadrupolar coupling to inhomogeneous crystal strain. Here, we combine strain engineering of the nuclear spin ensemble and tailored dynamical decoupling sequences to achieve nuclear spin coherence times exceeding 100 ms. Recently, a reversible transfer of quantum information into nuclear spin ensembles has been demonstrated in quantum dots: our results provide a path to develop this concept into a functioning solid-state quantum memory suitable for quantum repeaters in optical quantum communication networks. 

Quantum memories are indispensable in large scale quantum networks, which are expected to enable long distance communication of quantum information<sup>1–4</sup> . Quantum memories have several key requirements<sup>2</sup> , a primary figure of merit is the storage time, which is directly related to quantum repeater communication distance. Millisecond-range storage time allows for improvements over direct transmission through an optical fibre<sup>5,6</sup> . Another requirement is for the ratio of the storage time and the entanglement generationtime, known as quantum link efficiency<sup>7</sup> , to be as high as possible. Although entanglement generation time is currently the main limitation<sup>8</sup> , its continuous improvement (reduction) highlights the need for even longer storage times, exceeding 100 ms, in order to achieve worldwide optical communication. 

The storage of a quantum state in a memory is limited by the coherence time T2. Several material systems offer long T2, ranging from seconds to hours<sup>9</sup> , including trapped atomic ensembles<sup>10,11</sup> , ions<sup>12–17</sup> , electron spins<sup>18,19</sup> and phosphorus nuclear spins<sup>20–22</sup> in silicon, as well as electron and nuclear spins of impurities in diamond<sup>23,24</sup> . 

However, long T2 are often negated by poor optical properties required for a long-distance quantum network. There are promising hybrid approaches, such as combination of transmon qubits with solid-state quantum memories<sup>25</sup> , but these often suffer from coupling inefficiencies and bandwidth mismatch<sup>9</sup> (see further discussion in Supplementary Note 4). 

Epitaxial quantum dots (QDs) in group III-V semiconductors have high qubit entanglement rates<sup>26</sup> and are excellent on-demand emitters of single<sup>9,27–29</sup> and entangled photons<sup>30,31</sup> . At the same time, QDs host material qubits: Electron spin qubits can be interfaced with optical photon qubits<sup>32–34</sup> , but the coherence of the electron spin is limited to ≈100 μs<sup>35</sup> . The nuclear spins are isolated from external environments, resulting in long lifetimes and coherence times<sup>36–38</sup> . The recent demonstration of a reversible quantum state transfer between an electron spin qubit and a nuclear spin ensemble (with fidelity of ≈0.68)<sup>39,40</sup> offers a route for electron-mediated storage of a photonic quantum state in a nuclear ensemble of a QD. However, since all atoms in group III-V materials have non-zero nuclear spins, the natural 

> 1School of Mathematical and Physical Sciences, University of Sheffield, Sheffield, United Kingdom. 2Institute of Semiconductor and Solid State Physics, Johannes Kepler University Linz, Linz, Austria.<sup>3</sup> Department of Physics and Astronomy, University of Sussex, Brighton, United Kingdom.<sup>4</sup> Present address: Department of Electrical Engineering, Indian Institute of Technology Delhi, New Delhi, India.<sup>5</sup> Present address: Instituto de Física Gleb Wataghin, Universidade Estadual de Campinas (UNICAMP), Campinas, Brazil. e-mail: E.Chekhovich@sussex.ac.uk 

Nature Communications |  (2026) 17:239 

1 

Article 

https://doi.org/10.1038/s41467-025-66948-6 

nuclear spin coherence is limited to a rather modest ≈1 ms range<sup>41</sup> . Extending nuclear spin coherence is thus a key task in achieving quantum memories suitable for quantum repeaters<sup>42,43</sup> . 

Here, we achieve nuclear spin coherence of over T2 ≈ 100 ms, made possible by applying two concepts: Firstly, elastic strain is used to engineer the spin-3/2 nuclei and spectrally isolate the subspace with Iz = ±1/2 spin projections. The small inhomogeneity of this subspace allows application of thousands of coherent control operations, thus enabling efficient dynamical decoupling. Secondly, a dedicated 40pulse decoupling sequence cycle is designed to extend nuclear spin ensemble coherence while overcoming the parasitic spin locking effects encountered in previous decoupling experiments<sup>44,45</sup> . The analysis of the results shows that residual decoherence is dominated by the finite-pulse effects and the effective three-body nuclear spin interactions, which are often overlooked. We predict that even longer T2 values, on the order of ≈1 s, are well within reach through larger strains and further advances in dynamical decoupling. The macroscopically long coherence times achieved here were previously possible only in group IV semiconductor spin qubits<sup>21,46</sup> , where optical efficiency is limited. Our demonstration of engineered long coherence unlocks the unrivalled optical properties of group III-V materials for applications in quantum memory devices. 

## Results 

#### Strain-engineered nuclear spin ensemble 

We study the nuclear spin coherence of GaAs/AlGaAs QDs grown by molecular beam epitaxy. The right inset of Fig. 1a sketches the QD nuclear spin system of N ≈ 5 × 10<sup>4</sup> nuclei. The three isotopes<sup>75</sup> As, 69Ga, and 71Ga all have nuclear spin I = 3/2. The sample is cooled to ≈4.2 K. A superconducting magnet is used to apply a static magnetic field Bz ≈ 5.16 T along the sample growth crystal direction [001], lifting the degeneracy of the four nuclear spin states with spin projections Iz = ±1/2, ±3/2 (left inset in Fig. 1a). Optical pumping with circularly polarized light (Faraday geometry) is used to polarize the 

nuclear spins along the static magnetic field<sup>47</sup> . The nuclear spin lifetime is typically T1 > 10 s<sup>48</sup> , significantly longer than the coherence times measured in this work. Nuclear spin polarization is measured via photoluminescence (PL) spectroscopy<sup>49</sup> , see examples in Fig. 2a. A copper coil generates oscillating magnetic field perpendicular to Bz, enabling optically detected nuclear magnetic resonance (ODNMR) measurements. Radio frequency (Rf) bursts with raised cosine envelope are used to transfer coherence in and out of the storage nuclear spin subspace Iz = ±1/2 and to perform its dynamical decoupling. 

The sample is stressed uniaxially along the [110] crystal direction, perpendicular to the static magnetic field. The resulting anharmonicity<sup>37,50</sup> , is characterised by the first-order nuclear quadrupolar splitting νQ<sup>ð1Þ. The measured NMR spectrum, shown in Fig. 1a for</sup> 75As nuclei in a neutral (0e) GaAs/AlGaAs QD, reveals ν<sup>ð</sup> Q<sup>1Þ�255:1kHz.</sup> This splitting significantly exceeds the linewidths of the NMR transitions: the full width at half maximum (FWHM) Δν+1/2↔+3/2 ≈ Δν−3/2↔−1/2 ≈ 13.8 kHz of the satellite transitions (STs) − 3/2 ↔ − 1/2 and + 1/2 ↔ + 3/2 is dominated by the inhomogeneous quadrupolar broadening, while the FWHM Δν−1/2↔+1/2 ≈ 0.8 kHz of the central transition (CT) − 1/2 ↔ + 1/2 is controlled by a combination of the second-order quadrupolar inhomogeneity and the dipole-dipole interactions<sup>45,51</sup> . The small linewidth, combined with strain-induced spectral isolation from STs, makes the CT an ideal spin subspace for coherence storage. Notably, the lattice-matched GaAs/AlGaAs QDs offer a significant advantage over Stranski-Krastanov QDs characterised by the much larger Δν−1/2↔+1/2 ≈ 10 − 40 kHz<sup>45</sup> . 

#### Hamiltonian engineering of a nuclear spin ensemble 

Dynamical control of spin interactions is a powerful technique in magnetic resonance<sup>52,53</sup> . The method is based on applying a sequence of Rf pulses that perform fast coherent rotations of the spins, separated by the free evolution intervals. In the interaction picture (the “toggling” frame of reference) the Rf pulses can be viewed as 



<!-- Start of picture text -->
20<br>a<br>I z = 3/2 10 5<br>18 L   (1)Q 10 4<br>16 1/2 Coherence  10 3<br>L   (2)Q storage 10 2<br>14 1/2 subspace 10 1<br>12 3/2 L   (1)Q T Rf = 10 s 10 0<br>10 75As, 0 e , T Rf = 20 s 1010 -1-2<br>B Z 10 -3<br>8 1/2  1/2<br>10 -4<br>6 10 -5<br>| Q(1) Q(2) | 10 -6<br>4 | Q(1) Q(2) | 10 -7<br>2 1/2  3/2 3/2  1/2 1010 -8-9<br>0 10 -10<br>-300 -200 -100 0 100 200 300<br>Radio frequency offset (kHz)<br>)V<br>e<br> (<br>hf<br>E<br>,la<br>n<br>gis<br>R<br>M<br>N<br>Rf pulse spectral power density (arb. units)<br><!-- End of picture text -->



<!-- Start of picture text -->
b<br>c<br>d<br><!-- End of picture text -->



Fig. 1 | Optically detected nuclear magnetic resonance (NMR) of a single quantum dot. a Right inset shows schematic diagram of Ga and As nuclear spins in a GaAs/AlGaAs quantum dot (QD). NMR spectrum of the spin-3/2<sup>75</sup> As nuclei (black and blue solid lines, left scale) measured in an uncharged (0e) QD. The frequency offset is shown with respect to the Larmor frequency νL ≈ 37.981 MHz arising from the Zeeman splitting at external field of Bz ≈ 5.16 T (left inset). Out of the three magnetic dipole transitions, the two satellite transitions (STs) undergo a first-order quadrupolar shift ± ν<sup>ð</sup> Q<sup>1Þ(where νð</sup> Q<sup>1Þ�255:1 kHz),while the central</sup> transition (CT) is affected only by the second-order quadrupolar shift ν<sup>ð</sup> Q<sup>2Þ�3:3</sup> kHz. The CT linewidth (Δν−1/2↔+1/2 ≈ 0.8 kHz) is much narrower than the ST linewidths (Δν+1/2↔+3/2 ≈ Δν−3/2↔−1/2 ≈ 13.8 kHz). Dashed lines (right scale) show spectral profiles of the radio frequency (Rf) pulse bursts with duration TRf = 10 or 20 μs, tuned in resonance with the CT. b Schematic diagram of a CHASE-10 

sequence cycle, letters and signs denote Rf pulse phases. The pulses are separated by the free-evolution intervals τ. The total nuclear evolution time is TEvolTot = 10TRf + 12τ, while TFreeEvol = 12τ is the pure free evolution time for one cycle. c The CHASE-40 supercycle constructed of four CHASE-10 steps, with pulse carrier phase incremented by π/2 in each step. d Timing of the ODNMR measurement cycle. Optical pumping creates longitudinal nuclear spin polarization. The initialization π/2 Rf pulse converts this into transverse (coherent) nuclear polarization in the xy plane. Dynamical decoupling is applied, followed by a finalization π/2 pulse to rotate the remaining transverse polarization back along the z-axis. Finally, the nuclear polarization is read out using photoluminescence (PL) spectroscopy under an optical probe pulse. The sample bias is pulsed to maximize optical nuclear spin pumping and PL intensity during optical probing. 

Nature Communications |  (2026) 17:239 

2 

Article 

https://doi.org/10.1038/s41467-025-66948-6 



<!-- Start of picture text -->
50<br>a b<br>Optical pump<br>polarization:� + B 75zAs, 40<br>�<br>30<br>� E PL 20<br>10<br>0<br>1.6026 1.6028 1.6030 0 20 40 60 80 100 120 140 160 180 200<br>PL photon energy (eV) Rf pulse duration,  T Rf (�s)<br>c 20 QD Experiment, 75 As, 1/2 � +1/2, d Numerical model,  N  = 12 spins,<br>B z 1.0 homogeneous<br>T Rf = 20 �s<br>15<br>10<br>0.5<br>FID ( T Rf = 10 �s)<br>5 CHASE-40 decoupling (Hahn Echo ( T Rf = 20 T Rf � = 20s)  �s): CHASE-40 decoupling:Hahn Echo (1 pulse)<br>n Cycles = 1 (40 pulses) n Cycles = 1 (40 pulses)<br>n Cycles = 12 (480 pulses) n Cycles = 12 (480 pulses)<br>n Cycles = 32 (1280 pulses) n Cycles = 32 (1280 pulses)<br>0 n Cycles = 48 (1920 pulses) 0.0 n Cycles = 48 (1920 pulses)<br>0.01 0.1 1 10 100 0.01 0.1 1 10 100 1000<br>Free evolution time,  T FreeEvol (ms) Free evolution time,  T FreeEvol (ms)<br>eV)<br>�<br> (<br>hf<br>E<br> �<br>PL intensity (arb. units)<br>NMR signal,<br>eV)<br>�<br> (<br>hf<br>E<br> �<br>NMR signal,<br>Normalized echo amplitude<br><!-- End of picture text -->

Fig. 2 | Dynamical decoupling of QD nuclear spins. a Two photoluminescence (PL) spectra of a neutral exciton in the same individual QD measured after optical pumping with σ<sup>+</sup> (σ<sup>−</sup> ) polarized light, which results in negative (positive) nuclear spin polarization. The PL spectral splitting ΔEPL is a sum of the constant Zeeman splitting and the nuclear hyperfine shift ΔEhf, which is derived from the variations of ΔEPL. b Rabi oscillations of the nuclear spins in a neutral (0e) QD observed under an increasing duration TRf of an Rf pulse of constant amplitude. c Nuclear spin decoherence measured by optically detected nuclear magnetic resonance 

(ODNMR) under free induction decay (FID, open squares), Hahn echo (solid squares) and an increasing number of CHASE-40 dynamical decoupling cycles nCycles = 1 − 48 (see legend). Rf pulses, with duration TRf = 20 μs, are applied to the central spin transition − 1/2 ↔ + 1/2 in a neutral (0e) QD. Nuclear spin polarization is initialized with an x pulse (ϕ = 0). d Numerical modelling of nuclear spin decoherence on a homogeneous ensemble of N = 12 spins under the same decoupling sequences as in (c). 

transformations of the spin-interaction Hamiltonian. The π-pulse rotations invert the sign of the frequency shifts, allowing refocusing of the dephasing<sup>54</sup> , which in QDs is caused primarily by inhomogeneous quadrupolar broadening. However, sequences of π pulses, such as Carr-Purcell<sup>55</sup> or XY8<sup>56</sup> , do not recouple the nuclear spin-spin dipolar interactions. Instead, these dipolar interactions can be averaged to zero with a sequence of four phase-shifted π/2-pulses<sup>57</sup> . The average Hamiltonian is the leading (0th order) term in the Magnus expansion of the entire Hamiltonian in the toggling frame. By introducing more complex sequences of pulses it is possible to eliminate the unwanted interactions to higher orders, thus engineering the spin Hamiltonian to have the desired form<sup>53</sup> . 

Here, we engineer a “time suspension”<sup>58</sup> type of sequence, where the Hamiltonian terms are eliminated as much as possible to preserve an arbitrary coherent state of the nuclear spin ensemble for the longest possible time. As a starting point we use a CHASE-10 cyclic sequence<sup>45</sup> shown in Fig. 1b. By combining π/2 and π pulses, this sequence eliminates the average (0th order) free-evolution Hamiltonian both for the resonance frequency shifts and the spin-spin interactions. Simultaneous suppression of both types of interactions is crucial for dynamical decoupling in a dense nuclear spin ensemble of GaAs. By symmetrizing the sequence, a CHASE-20 supercycle is formed, which further eliminates all the 1st-order terms in the Hamiltonian. The CHASE-20 sequence has been applied to QDs previously, demonstrating its ability to suppress decoherence even under large inhomogeneous resonance broadenings in Stranski-Krastanov InGaAs/ GaAs QDs<sup>45</sup> . In low-strain GaAs/AlGaAs QDs, nuclear spin coherence 

times up to T2 ≈ 20 ms have been achieved<sup>37</sup> . However, the π pulses cause spin locking<sup>44,45</sup> which selectively accelerate decoherence of the spin states polarized along a certain equatorial axis of the Bloch sphere in the rotating frame, while artificially enhancing ("locking”) the coherence of the states polarized along the orthogonal equatorial axis. This behaviour is unwanted in quantum memory applications as it may lead to distortion of the state during storage. 

Here we use a different approach, where four CHASE-10 cycles are combined into a CHASE-40 supercycle shown in Fig. 1c. The phases of the Rf pulses in eachCHASE-10 subcycle are stepped by π/2. While each subcycle causes spin locking, the preferential direction of the “lock”, when viewed in the rotating frame, makes a full rotation about the direction of the static magnetic field (z) over the CHASE-40 supercycle. This four-step “rotating spin lock” eliminates the net spin locking effect for an arbitrary coherent state, as demonstrated through rigorous calculation (See Supplementary Note 5). Furthermore, the leading order residual Hamiltonian of CHASE-40 is twice smaller than in CHASE-20, resulting in extended coherence. 

#### Extended spin coherence under dynamical decoupling 

We start by examining experimentally the nuclear spin dynamicsunder continuous resonant Rf driving. The results shown in Fig. 2b reveal Rabi oscillations, which confirm the coherent nature of spin driving and allow the π/2 and π Rf pulses to be calibrated for dynamical decoupling (See Supplementary Note 2C). We then apply dynamical decoupling to the isolated Iz = ±1/2 nuclear spin subspace with two varying parameters: the number of sequence cycles nCycles and the 

Nature Communications |  (2026) 17:239 

3 



<!-- Start of picture text -->
-- v<br>-1 -1 ol "<br>2 , -2 a KX<br>el = - Kk<br>-3 [ ; -3 | - - 3<br>. . BZ2 EN<br>-4 -3 -2 -1 -0.10 -4 -3 -2 -1 -0.10 P AR B<br>EN A B<br>So, A 5<br>0, AY ooc od<br>2 NAA N p<br>A<br>3<br>D<br>A}<br>A}<br>4<br>coe eos .<br>’ -3 S N<br>S AN<br>5 -2 IS hN<br>: —_— S Ny<br>- CH RL ooo S AY<br>3 3 : oo v .<br>4 5 2 1 ~0.10 4 -3 2 1 -0.10 3 2<br><!-- End of picture text -->

a 

a 

Tx 

Tx 

a 

Article 

https://doi.org/10.1038/s41467-025-66948-6 



Fig. 4 | Uniform decoupling of an arbitrary coherent nuclear spin state. a Nuclear spin decoherence measured under 4 cycles of CHASE-40 with different phases ϕ of the initialization Rf pulse, which initializes transverse nuclear polarization along different azimuth angles in the xy plane (θ = π/2). The measurement of the longitudinal nuclear spin relaxation under CHASE-40 (without the initialization 

pulse, θ = 0) is shown by the open diamonds. b The nuclear spin decay times T2 and T1 obtained from fitting the data in (a). Error bars are 95% confidence intervals. Schematics show orientation of the nuclei on the Bloch sphere after the initialization pulse, where present. 

significant improvement of the storage time and fidelity in a QD nuclear spin quantum memory. 

#### CHASE decoupling of an inhomogeneous spin ensemble 

In order to demonstrate the importance of isolating the homogeneous Iz = ±1/2 CT storage subspace, we examine the opposite case of a Iz = (−3/2, −1/2) ST subspace. The considerably larger inhomogeneous broadening is characterised by the spectral shape of the ST NMR transitions. For each ST, this is a weighted sum of a peak observed in Fig. 1a with a linewidth of Δν+1/2↔+3/2 ≈ Δν−3/2↔−1/2 ≈ 13.8 kHz (65% weight), and a much broader peak (35% weight), that requires a different NMR technique to be observed. That broad spectral component is not shown in Fig. 1a, but was measured previously<sup>35</sup> to stretch to ≈±100 kHz and is caused by the atomic-scale strain of the randomly positioned Al and Ga atoms. The measured ST decoherence under CHASE decoupling is shown in Fig. 3b, and the resulting spin memory time TM is shown by the double solid line in Fig. 3e. Unlike with Iz = ±1/2, the best possibledynamical decoupling of the Iz = (−3/2, −1/2) subspace is achieved at the shortest possible TCycle. Despite this fastest possible Rf pulsing, the maximum achieved memory time is TM ≈ 31 ms. Although this storage time is a factor of ≈15 improvement over the simple Hahn echo, it is a factor of ≈4.4 worse than TM achieved for the spectrally narrow Iz = ± 1/2 subspace. 

The inferior spin memory time for an inhomogeneously broadened spin ensemble demonstrates how CHASE-40, as any other dynamical decoupling protocol, reaches the limit of its performance when the interaction that is being decoupled is no longer a small perturbation. The inhomogeneous broadening of the Iz = ± 1/2 CT subspace is a small perturbation, characterized by Δν−1/2↔+1/2TRf ≈ 0.015 ≪ 1. By contrast, the relative broadening of the Iz = (−3/2, −1/2) subspace is comparable to unity for the observed part of the ST NMR peak (Δν−3/2↔−1/2TRf ≈ 0.28) and violates the perturbative approximation (Δν−3/2↔−1/2TRf > 1) for the broad component of the ST. The large inhomogeneity of the ST exacerbates decoherence through spin evolution during the finite Rf pulses. Moreover, Δν−3/2↔−1/2TRf ≳ 1 means that Rf control pulses become more “soft” (i.e. not infinitely broad spectrally), resulting in imperfect rotations of the nuclear spins<sup>60,61</sup> . On the other hand, CHASE-40 shows no sign of spin-locking even for the Iz = (−3/2, −1/2) subspace, despite its larger inhomogeneous broadening (See Supplementary Note 3B). 

Uniform decoupling of an arbitrary coherent nuclear spin state An ideal quantum memory must store any given state with equally high fidelity. However, dynamical decoupling can create parasitic spin 

locking regimes, where storage effectiveness depends on the initial state<sup>44,45</sup> . We examine the uniformness of the quantum state storage by measuring dynamical decoupling of the homogeneous Iz = ± 1/2 subspace with different initial states. We use CHASE-40 with nCycles = 4 cycles, which provides a balance between extending the coherence time by an order of magnitude, while keeping to a minimum the finite-pulse decoherence. The phase ϕ of the initialization Rf pulse is varied to prepare transverse nuclear spin polarization along the different axes in the equatorial xy plane of the rotating frame (ϕ = 0 corresponds to a “+x” Rf pulse and prepares polarization along the −y axis, a “+y” pulse with ϕ = π/2 prepares polarization along the x axis). We further perform a measurement, where the initialization pulse is omitted, corresponding to initial nuclear spin polarization along the strong magnetic field (θ = 0). The measured decay curves are shown in Fig. 4a. The coherence times obtained from fitting are shown in Fig. 4b, and are around T2 ≈ 18 ms, nearly independent of the initial state. 

The uniform dynamical decoupling of different initial states confirms experimentally the design principle of the CHASE-40 supercycle. Stepping of the Rf pulse phases between the four constituent CHASE-10 subcycles can be understood intuitively as a “rotary spin lock”: the axis of spin locking is slowly precessing with respect to the rotating frame, with a net effect of removing any preferential spin locking axis over the entire CHASE-40 cycle. Rigorous calculations confirm this result, showing that the symmetry axis of the residual Hamiltonian of CHASE-40 is along the strong static magnetic field (z axis). It is also worth noting that the measurement without any initialization pulse (θ = 0 in Fig. 4b) yields the longitudinal spin relaxation time T1, as opposed to the transverse coherence time T2 measured with an initialization π/2 Rf pulse (θ = π/2). In the absence of dynamical decoupling, the strong static magnetic field imposes a pronounced anisotropy with T1 > 10 s<sup>48</sup> much larger than T2 ≈ 1 ms. Under CHASE-40 decoupling T1 decreases and T2 increases, converging to very similar values. This confirms that CHASE-40 is a well-balanced time-suspension sequence that eliminates not only the spin locking anisotropy in the xy transverse plane but also the anisotropy of the strong quantizing magnetic field along the z axis. 

The rotary spin lock offers a simple and reliable approach for reusing the dynamical decoupling sequences where spin locking is otherwise present<sup>45,62,63</sup> . The robustness of CHASE-40 against spin locking is key to achieving long spin memory times TM ≳ 100 ms through repeated cycling (with up to 2400 pulses). 

Nature Communications |  (2026) 17:239 

5 

Article 

https://doi.org/10.1038/s41467-025-66948-6 

#### Predicting dynamical decoupling performance through analytical and numerical modelling 

For any dynamical decoupling sequence the effective spin Hamiltonian can be calculated as a Magnus expansion series. However, finding the spin dynamics from a known Hamiltonian is still a difficult problem. This problem is simplified by noting that the exact spin dynamics is related to the exact NMR spectral lineshape through Fourier transform. The NMR lineshape can be approximated as a Gaussian, and its linewidth can be approximated in terms of the second moment M2, which in turn can be found from the Hamiltonian through direct calculation.T M � pf2i f=Thei fi fMi fi 2 **f** 53coherent. The residualmemoryHamiltoniantime can thenof CHASE-40be approximatedhas beenas computed analytically up to second order: it is too bulky to reproduce in full, a more detailed discussion can be found in Supplementary Note 5. The Hamiltonian depends on two parameters: the magnitude of the dipole-dipole interaction and the quadrupolar inhomogeneity. These parameters are derived from FID and Hahn Echo experimental data, allowing T M<sup>CHASE�40</sup> to be calculated up to second order in analytical form and without any fitting parameters. The results are shown by the dashed lines in Fig. 3e. For the homogeneous subspace Iz = ±1/2 (single dashed line), the analytical model accurately predicts the peak in the spin memory time TM at TCycle ≈ 2 ms. The actual peak value of TM is underestimated but matches the experiment within a factor of ≈2. By contrast, for the inhomogeneous subspace Iz = (−3/2, −1/2), the model underestimates TM by an order of magnitude. This indicates the limited accuracy of the perturbative Magnus expansion, which breaks down when the inhomogeneous broadening (in frequency units) is no longer small in comparison to the reciprocal cycle time 1/TCycle. In principle, the analytical model could be improved by extending the Magnus expansion. However, the increasing complexity of the highorder terms makes this approach impractical. 

The advantage of the analytical model is that it allows insights into the underlying physics. In particular, we find that direct dipole-dipole interactions of the ith and jth spins of the ensemble, characterised by the coupling constant νij, is eliminated by CHASE-40 up to second order inclusive. However, the dipolar interaction of the spins i, j remains, but with a coupling constant ∝ νikνkj, where k ≠ i, j is any other spin. Such a term can be interpreted as an effective three-particle coupling, where the interaction of any two spins i and j is mediated by any other spin k. Although often ignored, here we find that the residual decoherence of the homogeneous subspace Iz = ±1/2 can be explained only by taking into account this effective three-body interaction. The three-body second-order interaction limits TM under slow dynamical decoupling (long TCycle). In the opposite limit of fast decoupling (short TCycle) the memory time TM is limited by the zero-order dipole-dipole term arising from spin evolution during the finite Rf pulses (TRf > 0). A combination of these two effects results in a non-monotonic dependence TM(TCycle) with a maximum in TM, as shown by the single lines in Fig. 3e. By contrast, the decoherence in the inhomogeneous subspace Iz = (− 3/2, −1/2) is dominated by the quadrupolar offset inhomogeneity under finite (TRf > 0) control pulses. 

We analyse the data from an alternative perspective by conducting numerical modelling of the CHASE dynamical decoupling. The exact Schrödinger equation of a system of N = 12 spins is solved using mixed initial spin states with large transverse polarization, mimicking the NMR experiments (see details in Supplementary Note 6). Selected results are shown in Fig. 2d and reproduce well all the main features of experimental results in Fig. 2c. The detailed results for the case of the inhomogeneous subspace Iz = (−3/2, −1/2), are shown in Fig. 3d. Since the decoherence rate is dominated by the quadrupolar offsets, which is a single-particle effect, a good quantitative agreement with the experiment (Fig. 3b) is obtained by using realistic values of the inhomogeneous quadrupolar shifts in the numerical model. The results for the Iz = ±1/2 subspace, where quadrupolar inhomogeneity is taken to be zero, are shown in Fig. 3c. The numerical model reproduces the 



<!-- Start of picture text -->
1.0<br>Numerical model,<br>N  = 12 spins,<br>homogeneous,<br>T Rf = 20 �s<br>0.5<br>FID (0 pulses):<br>full transverse polarization<br>spin wave superposition<br>CHASE-40  n Cycles = 4 (160 pulses):<br>full transverse polarization<br>spin wave superposition<br>0.0<br>0.1 1 10 100<br>Free evolution time,  T FreeEvol (ms)<br>2|<br>Fin<br>|Init<br>Overlap fidelity |<br><!-- End of picture text -->

Fig. 5 | Decoupling of coherent nuclear spin wave states. Decoherence under dynamical decoupling derived from first-principles numerical modelling of spin dynamics of a homogeneous ensemble of N = 12 nuclei. Overlap probability between the initial and final wavefunctions is shown as a function of the free evolution time TFreeEvol. Results are shown for free induction decay (FID, squares) and nCycles = 4 cycles of CHASE-40 (triangles). The spin ensemble is initialized into a coherent state either with transverse polarization (multiple-quantum coherence, solid symbols) or a spin wave (single-quantum coherence, open symbols). 

main features of the experimental data on the Iz = ±1/2 subspace (Fig. 3a), in particular the nonmonotonic dependence of the spin memory time TM on the decoupling sequence cycle time TCycle. However, the agreement is only within an order of magnitude: the numerically-simulated maximum TM ≈ 2 s occurs at TCycle ≈ 8 ms, compared to the measured maximum TM ≈ 0.136 s at TCycle ≈ 2 ms (Fig. 3e). This discrepancy may seem unexpected, given that the numerically-simulated coherence time under simple Hahn echo T<sup>HE</sup> 2 � 1:4 ms is very close to the measured T<sup>HE</sup> 2 � 1:38 ms. However, the decoherence under Hahn echo is governed by the direct (pairwise) dipole-dipole interaction of the nuclear spins, whereas decoherence under CHASE-40 is dominated by the residual effective three-spin interaction. We therefore ascribe the discrepancy in TM to the limited number of spins in the numerical model: the number of three-spin combinations contributing to decoherence in an ensemble with N = 12 is considerably smaller than in a real crystal lattice of a QD (see Supplementary Note 6). The discrepancy is also likely to include the small but nonzero quadrupolar inhomogeneity of the Iz = ± 1/2 subspace, which reduces CHASE-40 TM in a real QD. 

#### Decoupling of coherent spin wave states 

The dynamical decoupling experiments of this work are conducted on nuclear spin states with macroscopic transverse polarization, which corresponds to multiple-quantum coherence. By contrast, recent proposals for nuclear-spin-based quantum memories<sup>40</sup> rely on singlequantum spin wave (magnon) nuclear spin states. The applicability of CHASE-40 dynamical decoupling to the spin wave coherent states is a non-trivial question, which we now investigate using numerical modelling on an ensemble of N = 12 spins. We compare two types of initial wavefunction states ψInit. One is a state with full transverse polarization (macroscopic magnetization), while the other is a superposition of a ground state with full longitudinal polarization and a spin wave excited state. The spin wave is a single-quantum excitation of the ground state<sup>64</sup> (see details in Supplementary Note 6). The Schrödinger equation is propagated to find the final state ψFin of the spin ensemble, and the overlap probability is calculated as ∣〈ψInit∣ψFin〉∣<sup>2</sup> with results shown in Fig. 5. 

The squares in Fig. 5 show the evolution without dynamical decoupling (free induction decay). The state with full transverse polarization exhibits a Gaussian decay on a timescale of T<sup>HE</sup> 2 � 0:9 ms 

Nature Communications |  (2026) 17:239 

6 

Article 

https://doi.org/10.1038/s41467-025-66948-6 

(full squares), which is a close match to T<sup>HE</sup> 2 � 1:4 ms computed above for an initial mixed state with partial transverse polarization. Interestingly, the decoherence of the spin wave superposition (open squares) is considerably slower even without any active dynamical decoupling. Some periodic oscillations and revivals are observed and can be ascribed to the smallness of the spin ensemble (N = 12) combined with the pure nature of the initial state. Next we model spin ensemble evolution as a function of TFreeEvol under dynamical decoupling with a fixed number nCycles = 4 of CHASE-40 cycles (triangles in Fig. 5). Once again, the decay exhibits periodic partial revivals, both for macroscopically polarized (full triangles) and spin wave (open triangles) coherent states. Most importantly, compared to free induction decay, CHASE-40 decoupling is found to slow down the decoherence both for macroscopically polarized and single-quantum spin wave coherent states. The computed coherence times T<sup>4xCHASE</sup> 2<sup>�40</sup> � 90 ms for pure initial states are found to be very similar to coherence times calculated above for mixed initial states. Notably, the spin wave state is more robust against the finite-pulse decoherence (limit of short TFreeEvol) than the macroscopically polarized state. These results suggest that numerical modelling and NMR experiments on spin states with macroscopic transverse polarization can be used to predict the dynamics of a single-quantum spin wave excitation. This initial finding confirms the prospect of using dynamical decoupling in spin wave quantum memories, which will be explored further in future work. 

## Discussion 

We have demonstrated very long coherence storage times of over 100 ms, achieved despite the dense nature of the nuclear spin ensemble in GaAs, where coherence extension via isotope enrichment<sup>21,46</sup> is not possible. The optically-active GaAs QDs are a promising candidate for quantum memory, which integrates a spin qubit with a single photon sources<sup>9</sup> , thus avoiding the need for complex hybrid schemes<sup>25</sup> . The long-term preservation of nuclear spin coherence demonstrated here is a key step in bringing the concept of QD-based optical quantum memory<sup>40</sup> to practical implementation. The extended coherence is enabled by strain engineering of the nuclear spin ensemble and the tailored 40-pulse time-suspension decoupling sequence. 

We use a three-pronged approach to the design of dynamical decoupling sequences. Numerical modelling can predict the overall performance of a dynamical decoupling protocol, but its accuracy is limited by the small number of spins N, constrained in turn by the exponential scaling of the required classical computing resources with increasing N. As a result, numerical simulations are time-consuming: full datasets of Fig. 3c, d require many days of computations on a workstation PC, which is comparable to experimental time required for Fig. 3a, b. Analytical calculations provide good predictions in case of small inhomogeneity. However, for a sequence with 40 pulses, derivation of the residual Hamiltonian takes several hours of computer-assisted algebraic derivations and further tedious manual work to analyse the bulky analytical results. Thus, the two modelling approaches encounter their different limitations, leaving experiment as the ultimate verification of the excellent coherence protection achieved with CHASE-40. The sequence is robust against spin locking, imperfections in control pulses, and is applicable to spin ensembles with a substantial inhomogeneous broadening. 

Strain engineering is a key enabling technique, as it allows spectral isolation of the homogeneous Iz = ±1/2 nuclear spin subspace. A further increase of elastic strain by a factor of ≈4 is within the yield strain of GaAs and isfeasible using membrane microstructures<sup>59,65,66</sup> . Thiswould allow quadrupolar splitting in excess of ν<sup>ð</sup> Q<sup>1Þ≳1MHz,enablingfurther</sup> improvement in quantum memory storage time and fidelity. More importantly, the MHz-range quadrupolar splitting would be required to exceed the electron-nuclear hyperfine interaction, which is ≲200 kHz in the studied GaAs QDs<sup>50</sup> . While dynamical decoupling of nuclear spins in presence of the central electron spin qubit is possible in 

principle<sup>38</sup> , achieving long nuclear spin coherence would require spectral isolation (through increased strain) of the hyperfinebroadened nuclear spin transitions. 

The maximum storage time TM under CHASE-40 decoupling is limited by the finite duration of the control pulses, which causes a drop in TM in the limit of frequent Rf pulsing (single lines in Fig. 3e, limit of small TCycle). By eliminating the zero-order finite-pulse effects<sup>52,67</sup> it should be possible to achieve TM ≈ 1 s even atthe current level of elastic strain, limited only by the second-order three-particle spin-spin interactions. More broadly, dynamical decoupling can be used to study spin-spin entanglement, thermalization in disordered quantum systems, and many-body localization<sup>68,69</sup> . 

## Data availability 

The data generated in this study are provided in the Source Data file SourceData.zip. Additional information and data related to this study are available from the corresponding author upon request. Source data are provided with this paper. 

## References 

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45–53 (2010). 2. Lvovsky, A. I., Sanders, B. C. & Tittel, W. Optical quantum memory. Nat. Photon. 3, 706–714 (2009). 

3. Pang, X.-L. et al. A hybrid quantum memory-enabled network at room temperature. Sci. Adv. 6, eaax1425 (2020). 

4. Bussières, F. et al. Quantum teleportation from a telecomwavelength photon to a solid-state quantum memory. Nat. Photon. 8, 775–778 (2014). 

5. Tittel, W. et al. Photon-echo quantum memory in solid state systems. Laser Photonics Rev. 4, 244–267 (2010). 

6. Zhao, R. et al. Long-lived quantum memory. Nat. Phys. 5, 100–104 (2009). 

7. Humphreys, P. C. et al. Deterministic delivery of remote entanglement on a quantum network. Nature 558, 268–273 (2018). 

8. Yu, Y. et al. Entanglement of two quantum memories via fibres over dozens of kilometres. Nature 578, 240–245 (2020). 

9. Neuwirth, J. et al. Quantum dot technology for quantum repeaters: from entangled photon generation toward the integration with quantum memories. Mater. Quantum Technol. 1, 043001 (2021). 

10. Treutlein, P., Hommelhoff, P., Steinmetz, T., Hänsch, T. W. & Reichel, J. Coherence in microchip traps. Phys. Rev. Lett. 92, 203005 (2004). 

11. Deutsch, C. et al. Spin self-rephasing and very long coherence times in a trapped atomic ensemble. Phys. Rev. Lett. 105, 020401 (2010). 

12. Langer, C. et al. Long-lived qubit memory using atomic ions. Phys. Rev. Lett. 95, 060502 (2005). 

13. Bollinger, J., Heizen, D., Itano, W., Gilbert, S. & Wineland, D. A 303MHz frequency standard based on trapped Be<sup>+</sup> ions. IEEE Trans. Instrum. Meas. 40, 126–128 (1991). 

14. Wang, Y. et al. Single-qubit quantum memory exceeding tenminute coherence time. Nat. Photon. 11, 646–650 (2017). 

15. Wang, P. et al. Single ion qubit with estimated coherence time exceeding one hour. Nat. Commun. 12, 233 (2021). 

16. Zhong, M. et al. Optically addressable nuclear spins in a solid with a six-hour coherence time. Nature 517, 177–180 (2015). 

17. Bruzewicz, C. D., Chiaverini, J., McConnell, R. & Sage, J. M. Trappedion quantum computing: Progress and challenges. Appl. Phys. Rev. 6, 021314 (2019). 

18. Tyryshkin, A. M., Lyon, S. A., Astashkin, A. V. & Raitsimring, A. M. Electron spin relaxation times of phosphorus donors in silicon. Phys. Rev. B 68, 193207 (2003). 

19. Tyryshkin, A. M. et al. Electron spin coherence exceeding seconds in high-purity silicon. Nat. Mater. 11, 143–147 (2011). 

Nature Communications |  (2026) 17:239 

7 

Article 

https://doi.org/10.1038/s41467-025-66948-6 

20. Morton, J. J. et al. Solid-state quantum memory using the<sup>31</sup> P nuclear spin. Nature 455, 1085–1088 (2008). 

21. Steger, M. et al. Quantum information storage for over 180 s using donor spins in a<sup>28</sup> Si “semiconductor vacuum". Science 336, 1280–1283 (2012). 

22. Freer, S. et al. A single-atom quantum memory in silicon. Quantum Sci. Technol. 2, 015009 (2017). 

23. Atatüre, M., Englund, D., Vamivakas, N., Lee, S.-Y. & Wrachtrup, J. Material platforms for spin-based photonic quantum technologies. Nat. Rev. Mater. 3, 38–51 (2018). 

24. Stas, P.-J. et al. Robust multi-qubit quantum network node with integrated error detection. Science 378, 557–560 (2022). 

25. Kubo, Y. et al. Hybrid quantum circuit with a superconducting qubit coupled to a spin ensemble. Phys. Rev. Lett. 107, 220501 (2011). 

26. Stockill, R. et al. Phase-tuned entangled state generation between distant spin qubits. Phys. Rev. Lett. 119, 010503 (2017). 

27. Huber, D. et al. Highly indistinguishable and strongly entangled photons from symmetric GaAs quantum dots. Nat. Commun. 8, 15506 (2017). 

28. Schweickert, L. et al. On-demand generation of background-free single photons from a solid-state source. Appl. Phys. Lett. 112, 093106 (2018). 

29. Arakawa, Y. & Holmes, M. J. Progress in quantum-dot single photon sources for quantum information technologies: a broad spectrum overview. Appl. Phys. Rev. 7, 021309 (2020). 

30. Liu, J. et al. A solid-state source of strongly entangled photon pairs with high brightness and indistinguishability. Nat. Nanotechnol. 14, 586–593 (2019). 

31. Rota, M. B. et al. A source of entangled photons based on a cavityenhanced and strain-tuned GaAs quantum dot. eLight 4, 13 (2024). 

32. De Greve, K. et al. Quantum-dot spin-photon entanglement via frequency downconversion to telecom wavelength. Nature 491, 421–425 (2012). 

33. Coste, N. et al. High-rate entanglement between a semiconductor spin and indistinguishable photons. Nat. Photon. 17, 582–587 (2023). 

34. Laccotripes, P. et al. Spin-photon entanglement with direct photon emission in the telecom C-band. Nat. Commun. 15, 9740 (2024). 

35. Zaporski, L. et al. Ideal refocusing of an optically active spin qubit under strong hyperfine interactions. Nat. Nanotechnol. 18, 257–263 (2023). 

36. Gillard, G. et al. Fundamental limits of electron and nuclear spin qubit lifetimes in an isolated self-assembled quantum dot. npj Quantum Inf. 7, 43 (2021). 

37. Chekhovich, E. A., da Silva, S. F. C. & Rastelli, A. Nuclear spin quantum register in an optically active semiconductor quantum dot. Nat. Nanotechnol. 15, 999–1004 (2020). 

38. Gillard, G., Clarke, E. & Chekhovich, E. A. Harnessing many-body spin environment for long coherence storage and high-fidelity single-shot qubit readout. Nat. Commun. 13, 4048 (2022). 

39. Gangloff, D. A. et al. Quantum interface of an electron and a nuclear ensemble. Science 364, 62–66 (2019). 

40. Appel, M. H. et al. A many-body quantum register for a spin qubit. Nat. Phys. 21, 368–373 (2025). 

41. Chekhovich, E., Hopkinson, M., Skolnick, M. & Tartakovskii, A. Suppression of nuclear spin bath fluctuations in self-assembled quantum dots induced by inhomogeneous strain. Nat. Commun. 6, 6348 (2015). 

42. Childress, L., Taylor, J. M., Sørensen, A. S. & Lukin, M. D. Faulttolerant quantum communication based on solid-state photon emitters. Phys. Rev. Lett. 96, 070504 (2006). 

43. Sharman, K., Kimiaee Asadi, F., Wein, S. C. & Simon, C. Quantum repeaters based on individual electron spins and nuclear-spinensemble memories in quantum dots. Quantum 5, 570 (2021). 

44. Li, D. et al. Intrinsic origin of spin echoes in dipolar solids generated by strong π pulses. Phys. Rev. B 77, 214306 (2008). 

45. Waeber, A. M. et al. Pulse control protocols for preserving coherence in dipolar-coupled nuclear spin baths. Nat. Commun. 10, 3157 (2019). 

46. Balasubramanian, G. et al. Ultralong spin coherence time in isotopically engineered diamond. Nat. Mater. 8, 383–387 (2009). 

47. Millington-Hotze, P. et al. Approaching a fully-polarized state of nuclear spins in a solid. Nat. Commun. 15, 985 (2024). 

48. Millington-Hotze, P., Manna, S., Covre da Silva, S. F., Rastelli, A. & Chekhovich, E. A. Nuclear spin diffusion in the central spin system of a GaAs/AlGaAs quantum dot. Nat. Commun. 14, 2677 (2023). 

49. Urbaszek, B. et al. Nuclear spin physics in quantum dots: An optical investigation. Rev. Mod. Phys. 85, 79–133 (2013). 

50. Dyte, H. E. et al. Is wave function collapse necessary? explaining quantum nondemolition measurement of a spin qubit within linear evolution. Phys. Rev. Lett. 132, 160804 (2024). 

51. Klauder, J. R. & Anderson, P. W. Spectral diffusion decay in spin resonance experiments. Phys. Rev. 125, 912–932 (1962). 

52. Haeberlen, U. & Waugh, J. S. Coherent averaging effects in magnetic resonance. Phys. Rev. 175, 453–467 (1968). 

53. Mehring, M. Principles of High Resolution NMR in Solids (Springer Berlin Heidelberg, 1983). 

54. Hahn, E. L. Spin echoes. Phys. Rev. 80, 580–594 (1950). 

55. Carr, H. Y. & Purcell, E. M. Effects of diffusion on free precession in nuclear magnetic resonance experiments. Phys. Rev. 94, 630–638 (1954). 

56. Gullion, T., Baker, D. B. & Conradi, M. S. New, compensated CarrPurcell sequences. J. Magn. Reson. 89, 479–484 (1990). 

57. Waugh, J. S., Huber, L. M. & Haeberlen, U. Approach to highresolution NMR in solids. Phys. Rev. Lett. 20, 180–182 (1968). 

58. Cory, D., Miller, J. & Garroway, A. Time-suspension multiple-pulse sequences: applications to solid-state imaging. J. Magn. Reson. 90, 205–213 (1990). 

59. Huo, Y. H. et al. A light-hole exciton in a quantum dot. Nat. Phys. 10, 46–51 (2013). 

60. Khodjasteh, K. & Lidar, D. A. Fault-tolerant quantum dynamical decoupling. Phys. Rev. Lett. 95, 180501 (2005). 

61. Souza, A. M., Álvarez, G. A. & Suter, D. Robust dynamical decoupling. Philos. Trans. R. Soc. A 370, 4748–4769 (2012). 

62. Dementyev, A. E., Li, D., MacLean, K. & Barrett, S. E. Anomalies in the NMR of silicon: Unexpected spin echoes in a dilute dipolar solid. Phys. Rev. B 68, 153302 (2003). 

63. Li, D., Dementyev, A. E., Dong, Y., Ramos, R. G. & Barrett, S. E. Generating unexpected spin echoes in dipolar solids with π pulses. Phys. Rev. Lett. 98, 190401 (2007). 

64. Taylor, J. M., Marcus, C. M. & Lukin, M. D. Long-lived memory for mesoscopic quantum bits. Phys. Rev. Lett. 90, 206803 (2003). 

65. Hjort, K., Soderkvist, J. & Schweitz, J. A. Gallium arsenide as a mechanical material. J. Micromech. Microeng. 4, 1 (1994). 

66. Martín-Sánchez, J. et al. Strain-tuning of the optical properties of semiconductor nanomaterials by integration onto piezoelectric actuators. Semicond. Sci. Technol. 33, 013001 (2017). 

67. Burum, D. P. & Rhim, W. K. Analysis of multiple pulse NMR in solids. III. J. Chem. Phys. 71, 944–956 (1979). 

68. Wei, K. X., Ramanathan, C. & Cappellaro, P. Exploring localization in nuclear spin chains. Phys. Rev. Lett. 120, 070501 (2018). 

69. Lukin, A. et al. Probing entanglement in a many-body-localized system. Science 364, 256–260 (2019). 

## Acknowledgements 

H.E.D. was supported by an EPSRC doctoral training grant. E.A.C. was supported by a Royal Society University Research Fellowship, the Leverhulme Trust grant RPG-2023-141, and the EPSRC awards EP/ V048333/1 and EP/V048333/2. A.R. acknowledges support of the 

Nature Communications |  (2026) 17:239 

8 

Article 

https://doi.org/10.1038/s41467-025-66948-6 

Austrian Science Fund (FWF) via the Research Group FG5, the cluster of excellence Quantum Science Austria (10.55776/COE1), the Linz Institute of Technology (LIT), and the LIT Secure and Correct Systems Lab, supported by the State of Upper Austria, the European Union’s Horizon 2020 research and innovation program under Grant Agreements No. 899814 (Qurope), No. 871130 (Ascent+), the QuantERA II project QD-E-QKD and the FFG (grant No. 891366). A.R. and E.A.C. were supported by the QuantERA award MEEDGARD (EPSRC award EP/Z000556/1 and FFG Grant No. 906046). E.A.C. is grateful to Daniel Treuherz, Dorian Gangloff, and Christian Schimpf for fruitful discussions. 

## Author contributions 

S.M., S.F.C.S. and A.R. developed, grew and processed the quantum dot samples. H.E.D. conducted the experiments. H.E.D. and E.A.C. analysed the data. H.E.D. and E.A.C. drafted the manuscript with input from all authors. E.A.C. performed numerical modelling and coordinated the project. 

## Competing interests 

The authors declare no competing interests. 

## Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-66948-6. 

Peer review information Nature Communications thanks Yuhei Sekiguchi, and the other, anonymous, reviewers for their contribution to the peer review of this work. A peer review file is available. 

Reprints and permissions information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/. 

© The Author(s) 2025 

Correspondence and requests for materials should be addressed to Evgeny A. Chekhovich. 

Nature Communications |  (2026) 17:239 

9 

