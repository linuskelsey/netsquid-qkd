PHYSICAL REVIEW X 12, 041014 (2022) 

<mark>Featured in Physics</mark> 

# Random-Access Quantum Memory Using Chirped Pulse Phase Encoding 

James O’Sullivan,<sup>1</sup> Oscar W. Kennedy ,<sup>1</sup> Kamanasish Debnath,<sup>2</sup> Joseph Alexander,<sup>1</sup> Christoph W. Zollitsch,<sup>1</sup> Mantas Šimėnas,<sup>1</sup> Akel Hashim,<sup>3,4</sup> Christopher N. Thomas,<sup>5</sup> Stafford Withington,<sup>5</sup> Irfan Siddiqi,<sup>3,4</sup> Klaus Mølmer ,<sup>2</sup> and John J. L. Morton<sup>1,6,*</sup> 

> 1London Centre for Nanotechnology, UCL, 17-19 Gordon Street, London WC1H 0AH, United Kingdom 

> 2Department of Physics and Astronomy, Aarhus University, DK-8000 Aarhus C, Denmark 

> 3Quantum Nanoelectronics Laboratory, Department of Physics, UC Berkeley, Berkeley, California 94720, USA 

> 4Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA 

> 5Cavendish Laboratory, University of Cambridge, JJ Thomson Avenue, Cambridge CB3 0HE, United Kingdom 

> 6Department of Electrical and Electronic Engineering, UCL, Malet Place, London, WC1E 7JE, United Kingdom 



(Received 17 May 2022; revised 16 August 2022; accepted 31 August 2022; published 7 November 2022) 

As in conventional computing, memories for quantum information benefit from high storage density and, crucially, random access, or the ability to read from or write to an arbitrarily chosen register. However, achieving such random access with quantum memories in a dense, hardware-efficient manner remains a challenge. Here we introduce a protocol using chirped pulses to encode qubits within an ensemble of quantum two-level systems, offering both random access and naturally supporting dynamical decoupling to enhance the memory lifetime. We demonstrate the protocol in the microwave regime using donor spins in silicon coupled to a superconducting cavity, storing up to four weak, coherent microwave pulses in distinct memory modes and retrieving them on demand up to 2 ms later. This approach offers the potential for microwave random access quantum memories with lifetimes exceeding seconds, while the chirped pulse phase encoding could also be applied in the optical regime to enhance quantum repeaters and networks. 

DOI: 10.1103/PhysRevX.12.041014 

Subject Areas: Quantum Physics, Quantum Information 

## I. INTRODUCTION 

Quantum memories (QMs) capable of faithfully storing and recalling quantum states on demand are powerful ingredients in building quantum networks [1] and quantum processors [2]. Ensembles of quantum systems are natural platforms for QMs, given their large storage capacity. Multiple qubits can be stored taking advantage of direct spatial addressing to access different regions of the ensemble [2,3]. However, for ensembles in the solid state that offer prospects for high-density QMs and typically have inhomogeneous broadening, spectral addressing can be used to distinguish excitations stored collectively in the ensemble. Solid-state atomic ensembles have long coherence times for both microwave [4–8] and optical [7–9] transitions and can couple to resonant cavities facilitating read, write, and control operations. Coherent control allows 



Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article’s title, journal citation, and DOI. 

coherence times to be extended by dynamical decoupling (DD) [8,10–12] or transferring the qubit state to a more coherent transition [13]. Coupling the ensemble to a cavity – in the strong coupling regime [14 18] or with cooperativity C ¼ 1 facilitates writing and reading information with unit efficiency [19,20]. 

One of the simplest memory protocols in inhomogeneously broadened systems is the Hahn echo [21], in which an excitation stored within an ensemble is inverted by a single π pulse and reemitted later as an “echo.” This has been used widely for retrieval of weak excitations in multimode microwave [5,22–24] and optical [25,26] memories and indeed formed the basis of early (classical) information storage proposals [27]. However, the simple Hahn echo approach is unsuitable for quantum memories, as it leads to amplified (and thus noisy) emission from the quantum systems in their excited state [28]. One solution is using two π pulses to return the ensemble predominantly to the ground state before the memory is accessed [20,29]. This requires suppressing the emission of the echo that would appear after the first π pulse. A second limitation of the Hahn echo sequence is that it acts as a “first-in, last-out” memory, rather than permitting random access to stored qubits. Various approaches have been explored to address 

2160-3308=22=12(4)=041014(16) 

Published by the American Physical Society 

041014-1 



<!-- Start of picture text -->
Excitation [No echo] Echo<br>20 20<br>100<br>52<br>2E 0 Q 0 0<br>i - 20 - 20<br>Time (us) 0 40 245 285 490 530<br>T WURST / WURST<br>P3 Dephasing & 1 RephasingT DephasingT &> RephasingT A<br>\Inversion (x) | Inversion (x)<br>I |<br>v<br>AN t<br>dy“n y  pd Excitation by in Echo formation requires! and $,,;=0  k(5) = 0<br>ar d t<br>5 (+3) (+3) Invers io(- 2)n (7) y| b,, (- 2)<br>bA = . ..wirite E B 7 emohittchoed 2 7<br>[] Q A [9] [] [] [] []<br>Read el le i<br>write &| | | L |] 0 ] [| Ho 10]<br>[QO] [1 5 [] 2 9: Ef [| [© vi<br>C m N c om =  I =<br>4= 0A ra rm ©) mt a ><br>we s HHH WF HH<br>[| L [| [ @ [9 []<br>INV +3 INV +3 INV -2 INV -2<br>WRITE READ<br><!-- End of picture text -->

PHYS. REV. X 12, 041014 (2022) 

RANDOM-ACCESS QUANTUM MEMORY USING CHIRPED PULSE … 

of an echo. A second identical WURST pulse unwinds the phase pattern ϕW, so that when kδ next returns to 0, the initial excitation is emitted as an echo. We exploit this behavior to achieve a general random-access QM: the phase patterns ϕW;i, defined by different WURST pulses, provide the storage index for the memory, as shown in Fig. 1(c). The application of a WURST pulse before and after an excitation “writes” it into the ensemble without affecting previously stored excitations. The same pair of WURST pulses is used later to read out the excitation, enabling random access of the QM. Applying WURST pulses in identical pairs ensures that stored excitations are unaffected by any read-write operation, beyond introducing periodic inversions that offer built-in dynamical decoupling. 

In summary, the random-access protocol consists of applying repeating blocks of the form ðπj − □ − πjÞ where πj is a unique WURST π pulse addressing a particular storage index j. □ can be (i) a weak input excitation to be stored in location j of the memory, (ii) an echo, constituting an excitation being retrieved from location j in memory, or (iii) null, for a clock cycle in which no information is being read or written, where the block is merely applied for dynamical decoupling with πj addressing an unused memory mode. 

## B. Theoretical description 

The cavity is driven by a chirped field which results in a temporal intensity profile of the field inside the cavity, and the coupled equations for the spins and the cavity field must in general be solved numerically. Here we shall make some observations for a simplified model, that will qualitatively explain most features seen in the experimental demonstration presented further below. The spins have a central frequency ωc and each spin is characterized by its detuning δ ¼ ω − ωc. We characterize a WURST pulse by its chirp rate R and pulse center t0, yielding its frequency ωðtÞ ¼ Rðt − t0Þ and phase ϕðtÞ ¼ <u>12</u><sup>Rðt −t0Þ2inthe framerotat-</sup> ing at ωc. In that frame, the Hamiltonian for each given spin is δσz=2, and the time-dependent complex Rabi frequency is ΩðtÞ ¼ Ω0 exp½−iϕðtÞ�. 

The spin transitions are resonant when Rðt − t0Þ ¼ δ, i.e., at the time tδ ≡ t0 þ δ=R. In the interaction picture with respect to the spin excitation energy δσz=2, the Hamiltonian of a single spin reads 



<u>1</u> where ϕðtÞ − δt ¼ 2<sup>Rðt −tδÞ2 þ δt0 −δ2=2R.</sup> Assuming a near perfect adiabatic chirp, the unitary evolution operator of the full chirp process is given in the σz eigenstate basis: 



where θδ ¼ ϕW − δt0. ϕW contains a term δ<sup>2</sup> =2R and a term that does not depend on δ but will in general depend on the chirp rate R and on the coupling strength Ω0 (see below). 

For initial spin states with a (small) excitation amplitude of ϵ at t ¼ 0, the δ dependence of the mean value of the σ<sup>þ</sup> operator is ∝ ϵe<sup>2iδt0</sup> (disregarding the contribution from ϕW), and in the Schrödinger picture, multiplying by e<sup>−iδt</sup> we obtain σ<sup>þ</sup> ∝ ϵe<sup>iδð2t0−tÞ</sup> . If it were not for the detuning dependence of ϕW, these terms would rephase at the time t ¼ 2t0 as in the conventional Hahn echo. Now, instead, the spins may have very different excitation phases and the integral over δ vanishes and the echo is silenced. 

All WURST pulses are described by the same form given in Eq. (2), and the action of two subsequent pulses (in the interaction picture) at times t0 and t1 is readily found: 



With a ¼ e<sup>−iθδ</sup> , with parameters R0, Ω0, and b ¼ e<sup>−iθδ</sup> , with parameters R1, Ω1, we get ab<sup>�</sup> ¼ e<sup>iðϕW0−ϕW1Þþiδðt1−t0Þ</sup> , and if the pulse parameters are identical, this simplifies to ab<sup>�</sup> ¼ e<sup>iδðt0−t1Þ</sup> . Thus, after two identical WURST pulses, a weak spin excitation returns with a global minus sign and a detuning-dependent phase factor. In the Schrödinger picture, the linear detuning dependence of the phase disappears at t ¼ 2ðt1 − t0Þ and we obtain an echo. 

Assuming perfect inversion, a sequence with an even number of WURST pulses yields a final phase which is the sum of all WURST phases θδ with þ (−) signs if they are raising (lowering) pulses, cf. Eq. (1). Two pulses with different chirp rates or strengths will not cause an echo due to the nontrivial dependence of the phase difference ϕW0 − ϕW1. The quadratic variation δ<sup>2</sup> ð1=2R0 − 1=2R1Þ due to the phase chirp may thus cause destructive interference over the distribution of δ, and the dynamical phase associated with the energies of the adiabatic eigenstates during the chirped adiabatic process may cause destructive interference over a range of values for the coupling strength. 

We next consider the theoretical performance of AFP pulse echo silencing to confirm that it can support highfidelity storage. Parameters and timescales are chosen to be realistic values for an ensemble of spins in the solid state driven by a superconducting resonator, as used in Ref. [45] and in this article. We numerically calculate the spin dynamics by discretizing an inhomogeneously broadened spin ensemble into 10<sup>5</sup> subensembles and solve their individual dynamics subject to chirped pulses. The spin dynamics is governed by the Hamiltonian presented in Eq. (1) summed over the spins in different subensembles. 

041014-3 



<!-- Start of picture text -->
400<br>200<br>3<br>S |<br>WW<br>- 200<br>- 400<br>0 100 200 300 400<br>Time (us)<br>1<br>Bh<br>0<br>0 0.4 08 12 1.6 2<br>y (MHz)<br>500 ;<br>3 0 i | 1<br>-5005 0.2 0.4 06 0.8 1<br>Time (ms)<br><!-- End of picture text -->



<!-- Start of picture text -->
NU. J ! ) |<br>Eos<br>><br>=<br>7<br>z Er,<br>; 1.0 0<br>i X 0 2 4 nT<br><!-- End of picture text -->



<!-- Start of picture text -->
_m 1.0<br>g<br>N<br>5 0.5<br>hat<br>0.0<br><!-- End of picture text -->





+ 

PHYS. REV. X 12, 041014 (2022) 

RANDOM-ACCESS QUANTUM MEMORY USING CHIRPED PULSE … 

results in a large collection efficiency of spin echo signals. A schematic of the full microwave setup is shown in Fig. 8 and details of resonator performance are provided in Fig. 9. 

Fitting to S-parameter measurements of the planar superconducting cavity gives a cooperativity C ¼ 0.07ð2Þ (see Appendix C 1 and Ref [46]), leading to a predicted one-way memory efficiency of ηem ¼ ½4C=ð1 þ CÞ<sup>2</sup> �¼ 0.2 [19]. Although this is larger than previously reported values for ensemble microwave memories of 0.01–0.04 [5,22,23], it poses a bound for the amplitude of the retrieved excitations in our demonstration of the random-access QM protocol below. 



## B. Memory efficiency and coherence 

Despite the spin-cavity coupling in these experiments being well below unit cooperativity, we can already see the importance of suppressing echo emission from an inverted ensemble. In Figs. 4(a)–4(d) we apply Ninv WURST π pulses (for Ninv ¼ 0–3) before an echo sequence to selectively prepare the ensemble into a ground (Ninv even) or inverted (Ninv odd) state. Using weak excitations of hni ∼ 200 microwave photons ensures that the ensemble is only weakly perturbedfrom theground orexcited statewhenemitting. We see that echoes emitted from an inverted ensemble have larger amplitude than those emitted from a (quasi)ground state ensemble, indicating that there has been amplification of the input signal from stimulated emission (the echo is always weaker than the input signal due to other losses). This amplification of states as they are emitted is incompatible with high-fidelity state retrieval, and is why robust quantum memory schemes must ensure emission from a (quasi) ground state ensemble, as supported by our protocol. 

By increasing the delay between WURST pulses, we measure a coherence time of this prototype memory, T2 ∼ 0.7 ms [Fig. 10(b)]. This lifetime can be extended using dynamical decoupling sequences which involve a train of repeated π pulses [12,47]. If the DD sequence uses identical WURST pulses (i.e., A½AA�nA), an echo is emitted after every pair of pulses, as shown in the upper inset of Fig. 4(e). This repeated echo emission can be avoided by introducing a second type of WURST pulse (B) of different chirp rate and/or amplitude to the first (A), creating the sequence A½BB�nA, shown in the lower inset of Fig. 4(e). Only one echo appears in this sequence, after the second A pulse which is applied at the end, and the decay time constant of this echo provides a measure of the memory storage lifetime, TM ¼ 2.0ð2Þ ms. This lifetime is about 3 times longer than that measured with a Hahn echo, thanks to the effect of DD. The A½AA�nA WURST DD sequence—in which echoes are emitted periodically throughout—gives a decay time constant shorter than TM. We can use this difference to extract the cooperativity by modeling the echo intensity as a function of echo number and considering the reduction of energy in the echo field with repeated echo emission. 

FIG. 4. Demonstrating the importance of suppressed echo emission. (a) The pulse sequence used to study the echo following a pair of WURST pulses as a function of the state of the ensemble. (b) The approximate ensemble ground and excited state in a Bloch sphere representation of the ensemble magnetization. (c) Two example echoes emitted from the ground state (Ninv ¼ 2) or inverted state (Ninv ¼ 3). Larger amplitude echoes are seen from the inverted ensembles due to amplification of the echo, which adds noise to a quantum memory. (d) Echo amplitude as a function of Ninv. The overall reduction of echo amplitude with increasing Ninv is likely due to gradual saturation of the spin ensemble. (e) Coherence decay rates from different WURST dynamical decoupling sequences. Given identical pulses (A½AA�nA, purple) echo emission occurs every second pulse leading to an accelerated decay in coherence compared to an A½BB�nA (pink) sequence where only one echo is emitted, at the end. A fit to the A½BB�nA data (dashed line) gives a coherence time of 2 ms, while fitting to the A½AA�nA data accounting for additional loss from repeated echoes [dashed line; see Eq. (4)] gives a memory efficiency ηem of 0.17. Error bars represent one standard deviation from fitting Gaussians to echoes. 

Our model assumes a constant fraction ηem of the excitation is lost with each emitted echo of the A½AA�nA sequence, in addition to the background exponential decay with time constant T2 seen in the A½BB�nA. The echo intensity at time t is therefore 



where A0 is the echo amplitude at time t ¼ 0, T2 is the spin decoherence time, ηem is the efficiency with which energy 

041014-5 

PHYS. REV. X 12, 041014 (2022) 

JAMES O’SULLIVAN et al. 

is emitted from the echo field to the cavity, and N is the number of echoes which have occurred before time t. For the DD measurements using the A½BB�nA sequence, only one echo appears (thus, N ¼ 0), enabling us to extract T2 ¼ 2.0 � 0.2 ms for the refocusing rate used of 7.1 kHz. We can then fit the A½AA�nA data using one free parameter, yielding ηem ¼ 0.17ð7Þ, as shown in Fig. 4. From this we infer an operational memory efficiency η<sup>2</sup> em ¼ 0.03ð2Þ, assuming an equal contribution from read and write processes. 

Using Eq. (17) from Ref. [19] we relate the one-way efficiency to the cooperativity by 



<!-- Start of picture text -->
(a)<br><!-- End of picture text -->



<!-- Start of picture text -->
(b) (c)<br><!-- End of picture text -->



giving C ∼ 0.05 in close agreement to the value of C ∼ 0.07 extracted in the more typical method by measuring the S parameters of the resonator and shown in Fig. 9. In a highefficiency quantum memory (C ∼ ηem ∼ 1), DD sequences of the type A½BB�nA will be essential to avoid premature emission of stored excitations. 

## C. Demonstration of memory protocol 

We use this spin-cavity system to perform the randomaccess protocol, storing four weak (hni ∼ 1200 photon) microwave excitations, using five distinct WURST pulses [see Fig. 5(b)]. The photon number was calibrated from measurements of Rabi frequency and Purcell relaxation (see Appendix C and Fig. 10). Each excitation is encoded into the memory using a pair of identical WURST pulses (color coded in teal, coral, lime, and mustard) and retrieved later (storage time varying from 0.5 to 2.5 ms) by applying the same pair of pulses. Each echo can be unambiguously matched to one of the input excitations through its phase [see Fig. 5(c)], which we confirm by repeating permutations of the sequence with only one excitation present (Fig. 15). A fifth variant of WURST pulse (shown in gray) is used to perform DD. The weak amplitude of retrieved signals relative to input states is due primarily to the limited cooperativity in these experiments, rather than the control fidelity in the random-access protocol or decoherence. Rescaling the echo amplitudes by the factors shown in Fig. 5(c) we observe that the phase of the excitation is generally well preserved. The largest phase error, from the second excitation (coral) is attributed to a phase shift from the Josephson parametric amplifier, as the echo is of larger amplitude due to the short storage time (Fig. 11). 

## D. Memory capacity 

The memory capacity is determined by the number of independent WURST pulses that can be used in the protocol. This is related to the spectral width (Δf) of the storage ensemble, the narrower of the cavity linewidth κ and that of the inhomogeneous ensemble. The WURST pulses can be parametrized using their chirp rate R and 

FIG. 5. Experimental demonstration of the random-access memory protocol. (a) An illustrative segment of the protocol in which WURST pulses, excitations, and echoes are color coded, with WURST parameters as defined in (b). In total four excitations are stored for times up to 2 ms. Excitations and echoes are shown with magnified echoes offset from the main trace. The first and last pulses do not come in pairs as the memory sequence starts and finishes halfway through a clock cycle. (c) Echoes and excitations on an Argand diagram matching their phases. The magnitude of each echo is rescaled to account for losses from the finite spin-resonator cooperativity in this experiment and spin decoherence. 

amplitude AW (which is proportional to the Rabi frequency Ω), bounds illustrated in Fig. 6. Adiabiticity of refocusing imposes a lower bound of AW [48], with an upper bound set by the maximum pulse amplitude, limited, for example, by the pulse amplifier or sample heating. We determined the adiabatic bounds on AW in our experiment through microwave simulations, confirmed through experiments of the type illustrated in Fig. 1(a) (see Fig. 13). The rate R has some upper bound set by the experimental frequency resolution and a lower bound determined by the need to at least chirp across Δf within the effective duration of the WURST pulse (TW;eff), such that R ≫ Δf=TW;eff. As we observe in the experiments, variation of the chirp rate and strength permit addressing of separate storage modes. The field-amplitude-dependent Rabi frequency Ω0 and the chirp rate R both appear in the dressed state energies and hence in the dynamical phases which label memory modes. The two control parameters turn out not to lead to exploration of a two-dimensional space of storage modes, as seen in Fig. 6. An analytical theory for the phase textures indicated in Fig. 1(b) would require solution of the driven two-level dynamics by a chirped frequency field with a time- and 

041014-6 

PHYS. REV. X 12, 041014 (2022) 

RANDOM-ACCESS QUANTUM MEMORY USING CHIRPED PULSE … 



FIG. 6. Counting memory modes. Each memory mode is determined by the phase pattern ϕW imparted by a WURST pulse. The parameter space where WURST pulses efficiently refocus spins is bounded in black and is determined by the cavity line-width, the maximum spectrometer power, and the adiabaticity requirement of the WURST pulse. Bounds are the cavity linewidth, the maximum spectrometer power and requirements the WURST is adiabatic. A frequency resolution limit occurs due to the homodyne scheme and would be removed in a heterodyne scheme. We measure the adiabaticity limit by thresholding echo intensity shown in Appendix D 2 and here by the black dashed line giving good agreement with the theoretical line. We measure distinctiveness of WURST pulses using AB-echo sequences. The results of sweeping the B pulse chirp rate at maximum power are inset to the top of the figure and fit by Gaussian profiles. We show a two-dimensional map sweeping chirp rate and Rabi frequency in the inset. In 2D sweeps there are lines of WURST pulses which impart the same ϕW function to the spin ensemble. Green lines in the main panel show the line of equivalent WURST pulses from other two-dimensional maps. Interpolating data from AB-echo sweeps we determine the width of a line of equivalent WURST pulses at fixed Rabi frequency. We partition the space of available WURSTs into unique WURSTs (i.e., memory modes) by constraining neighboring WURST pulses to be separated by the half-width hundredth max and show an example partitioning where blue and white sections indicate unique WURST pulses. We show the WURST pulses used in Fig. 5 where the up (down) markers refer to positive (negative) chirp direction. 

frequency-dependent Rabi frequency Ω0ðtÞ imposed by the finite bandwidth cavity mode. The separation of distinct pulses in R and AW is governed by the requirement of independence in the storage modes of the memory. We explore this using pulse sequences of the form α − πA − πB − ½echo�, where an excitation α is followed by two WURST pulses whose parameters are varied. For sufficiently distinct πA and πB, no echo should be observed. First, we fix the parameters of πA and vary those of πB, shown in the inset of Fig. 6. Equivalent WURST pulses lie on lines of positive gradient—as R increases, the phase from the WURST pulse decreases, compensated by increasing AW. Additional two-dimensional parameter sweeps are shown as green lines in Fig. 6; we also acquire several 



<!-- Start of picture text -->
(a)<br>(b)<br><!-- End of picture text -->

FIG. 7. First-in, first-out (FIFO) time-bin encoding of multiple echoes. (a) An experimental demonstration of multiple excitations stored using the FIFO protocol with two identical WURST pulses. The pattern of excitation or echo phases allows echoes and excitations to be unambiguously matched. (b) Schematic showing evolution of spin waves and WURST phase resulting in the FIFO encoding with silenced echoes. 

one-dimensional sweeps (a subset is shown in Fig. 6). We identify different addressable regions in WURST parameter space by requiring that each WURST pulse in one region is separated by at least the half-width, hundredth max of the pulses in the neighboring regions (Fig. 14). We find ∼8 distinct WURST pulses at an amplitude of 0.6 V, and the same from chirping in the reverse direction, giving ∼16 distinct memory modes. 

Chirped pulse encoding can be combined with other methods such as time-bin encoding (used to store up to 100 weak microwave excitations [5,34]) to implement a memory offering random access to large registers. For example, in Fig. 7 we demonstrate how a pair of WURST pulses can be used to store a register of five microwave excitations, later retrieved in the same order in which they were written [a first-in, first-out (FIFO) memory]. Therefore, by replacing the single excitations shown in Fig. 5 with such registers, the capacity of the quantum memory is further extended. Additional strategies for increasing the number of storage modes include addressing the instrumentation-limited bounds on R and AW, and by increasing the WURST pulse duration (at the expense of slower read-write speeds and less effective DD). 

## IV. OUTLOOK 

The memory efficiency in the experimental demonstration was primarily limited by the spin-resonator cooperativity (C ∼ 0.06), and there are several practical approaches being pursued to increase this to C ∼ 1 using Bi donors and superconducting microresonator cavities by increasing the spin-cavity coupling g0 and the number of resonant spins 

041014-7 

PHYS. REV. X 12, 041014 (2022) 

JAMES O’SULLIVAN et al. 

(see Ref. [45]). Although the memory lifetime in this demonstration using a natural-silicon host was only 2 ms, rare-earth spins coupled to similar resonators have been shown to have coherence times of tens of milliseconds [49,50] while coherence times over 300 ms havebeen shown for near-surface Bi donors in isotopically enriched<sup>28</sup> Si [5]. 

The chirped pulse protocol introduced here could also be applied to provide random read-write access in optical QMs. Chirped microwave pulses could be applied to directly drive transitions in spin-active optical QMs, such as Nd in YVO4 [33], providing DD and controlling access to a register of stored optical excitations. Furthermore, adiabatic fast passages (achieved using acousto-optic and electrooptic modulators) have been used to optimally invert optical transitions in demonstrations of optical QMs [29]. Similarly chirped optical pulses of varying parameters could allow for a random-access protocol to be directly implemented in the optical domain, taking advantage of the stronger atomcavity coupling and larger cavity bandwidth. 

The datasets generated and analyzed during the current studyareavailableintheUCLResearchDatarepository [51]. 

targeting a density of 10<sup>17</sup> cm<sup>−3</sup> bismuth in the top 1 μm of the sample. The sample and implantation profile are shown schematically in Fig. 3. This is annealed at 900 °C for 5 min to incorporate the bismuth into the silicon matrix forming spin-active donors. A planar niobium microresonator is patterned on the top of the sample by lift-off. The Nb film is 100 nm thick and has a field-dependent frequency (see Ref. [45]) of 7.093 GHz at a magnetic field of 46 mT. The resonator is a lumped element design comprising a pair of parallel capacitive plates and a narrow doubled-back inductor wire, designed to enhance the magnetic field generated by the resonator close to the substrate surface. The sample is placed inside a copper cavity, as shown in Fig. 3(d). 

## APPENDIX B: MEASUREMENT SETUP 

The measurement setup is shown in Fig. 8. The copper sample box is mounted at the baseplate of a dilution refrigerator at 100 mK. The output signal is routed through two circulators to a Josephson parametric amplifier (JPA), a quantum limited amplifier, which amplifies the signal in 

## ACKNOWLEDGMENTS 

We thank Philippe Goldner for insightful discussions relating to the implementation of this protocol in the optical domain. We thank the UK National Ion Beam Centre (UKNIBC) where the silicon samples were ion implanted and Nianhua Peng who performed the ion implantation. This work has received funding from the UK Engineering and Physical Sciences Research Council (EPSRC), through UCLQ postdoctoral fellowships (O. W. K. and M. S.) of the Training & Skills Hub in Quantum Systems Engineering (Grant No. EP/P510270/1), the Hub in Quantum Computing and Simulation (Grant No. EP/T001062/1), and a Doctoral Training Grant (J. O’S.). J. J. L. M. acknowledges funding from the European Research Council under the European Union’s Horizon 2020 research and innovation programme [Grant Agreement No. 771493 (LOQO-MOTIONS)]. 

J. O’S. and O. W. K. performed the experiments with assistance from C. W. Z. J. O’S, O. W. K., and J. J. L. M. analyzed the data with input from J. A. and M. S. J. A. and J,J. L. M designed the random-access protocol with input from O. W. K. and J. O’S. K. D. and K. M. performed numerical analyses and the analytical treatment. C. N. T. and S. W. fabricated the device. A. H. and I. S. assembled, tested, and provided scientific support in the operation of the JPA. J. O’S, O. W. K., and J. J. L. M. wrote the manuscript with input from all authors. J. O’S. and O. W. K. contributed equally to this work. 

## APPENDIX A: DEVICE FABRICATION 

A float-zone silicon wafer of natural isotopic abundance is ion implanted with bismuth at a chain of energies 



<!-- Start of picture text -->
MWG<br>0  0  0  50 K<br>dB dB dB<br>0  4 K<br>Pulse gate  20  10  dB<br>dB dB<br>frequency  IQ mixer  +40 dB<br>doubler<br>I<br>x2 L Q R dB0  dB10  dB0  800 mK<br>LO/2 0  10  0  100 mK<br>dB dB dB<br>I<br>VSG AWG Digitizer<br>Q 10  20  0  100 mK<br>dB dB dB<br>NbTi<br>Stainless Steel<br>Cu Ni<br>Cu<br>JPA<br>Other<br><!-- End of picture text -->

FIG. 8. Schematic of the spectrometer and dilution fridge setup. Microwave pulse signals are generated using a vector signal generator (VSG) and an arbitrary waveform generator (AWG). A microwave generator (MWG) is used to drive the Josephson parametric amplifier (JPA). The return signals are down-converted and detected with a digitizer. A signal at half the up-conversion local oscillator (LO) frequency provided by the VSG is doubled with a frequency doubler and used for down-conversion. Coaxial cable types inside the fridge have been color coded. 

041014-8 



<!-- Start of picture text -->
_ Fait 420 +<br>CE Re oi,<br>= ++ i fo i + + t+<br>=&n 0 phHF+F gtThe wFhid | TN 900 N Hat++ + Liv+ a<br>9 fr o | 380 +, +5<br>o - 10 + Ht Ft<br>= + ry +48 * +H<br>5 H + + Fh AE<br>= 360<br>- 20 + +<br>46 48 46 48<br>Field (mT) Field (mT)<br>- 50<br>~ 60 Q=18400<br>f=7.09395 GHz<br>B=46 mT<br>~~ = 70<br>[)<br>AC)<br>N<br>Vv _ go<br>- I<br>—- 100<br>7.080 7.085 7.090 7.095 7.100 7.105 7.110<br>Frequency (GHz)<br><!-- End of picture text -->

PHYS. REV. X 12, 041014 (2022) 

JAMES O’SULLIVAN et al. 



<!-- Start of picture text -->
(a) (b)<br>(c)<br><!-- End of picture text -->

FIG. 10. (a) T1 by inversion recovery. A WURST pulse is used to invert the ensemble before a wait (indicated on the x axis) and a detection sequence at constant high power and τ. (b) T2 measurement of the sample at the same weak excitation strength as used in Fig. 4. The pulse sequence (inset) is a weak excitation followed by two 100 μs WURST pulses. Increasing τ changes the echo time allowing T2 to be measured. Fitting stretched or single exponentials gives different T2 giving a combined uncertainty of T2 ¼ 0.7ð2Þ ms. (c) Rabi oscillations using a Gaussian θ pulse of duration 8 μs and FWHM 4 μs and a two-WURST silenced echo detection sequence. The oscillations are heavily damped due to a large inhomogeneity in Rabi frequency across the ensemble. 

hni ∼ 1200 photons for the memory protocol. Because of the uncertainty in Rabi measurements these photon numbers should be treated as indicative powers accurate to approximately 50%. 

We note that in Fig. 4(d) repeated WURST pulses before a pulse sequence can cause a reduction in echo amplitude which implies that WURST pulses cause some saturation of the ensemble. However, comparing the T2 decay shown here and the TM [Fig. 4(e)] acquired when using repeated WURST pulses, we see that repeated WURST pulses actually increase the final echo amplitude due to dynamical decoupling. These two observations appear initially at 

odds. However, we understand this discrepancy using a toy model where we divide spins into three zones: (i) weakly coupled spins, far from the resonator and unaffected by WURST pulses, (ii) spins a moderate distance from the resonator, in turn moderately coupled and undergo imperfect inversion under WURST pulses, and (iii) spins close and strongly coupled to the resonator which are inverted by WURST pulses with high fidelity. Repeated WURST pulses will saturate zone (ii) which would contribute some of the echo strength. When operating this memory with a long string of WURST pulses, zone (ii) would always remain saturated, and therefore not contribute to the protocol. This means that in future devices, sufficient cooperativity for high-fidelity memory transfer must be achieved with only spins in zone (iii). 

The use of a JPA in measurements was essential to perform experiments at low photon numbers. Such amplifiers are prone to saturation and nonlinearity with large input signals. We calibrate the JPA to determine the onset and extent of the nonlinear regime, and any additional distortions that may be present. For comparison, the same measurements were repeated with the JPA turned off, using only a HEMT at 4 K for amplification. We confirm that for Fig. 5 the echo signals are well into the linear regime but the input excitations are in the nonlinear regime of the JPA and are prone to distortion. The HEMT remains linear and undistorted at all powers, as expected. JPA calibrations are shown in Fig. 11. The inhomogeneous linewidth of the ensemble is ∼2.5 MHz (see Ref. [45] for further details). 

To further increase signal we chose an operating temperature to maximize the population of the ground state of our chosen bismuth transition (∼10%). Pulsed experiments are run with a long shot-repetition delay of 160 s to minimize the saturation of spins. These considerations are to improve the cooperativity between the spin ensemble and resonator which contributes to the read-write efficiency of the memory and thus improve signal—approximately 17% one-way efficiency as shown in the main text. This means that when measuring ∼200 photon input pulses, the output pulse is actually 0.17<sup>2</sup> × 200 ∼ 6 photon output pulses— without considering any T2 decay. Despite our optimized antenna configuration, we may fail to capture all of this output pulse, and also find that the JPA is working slightly suboptimally (given the elevated temperature). The combination of these effects means that to observe a low-noise echo at low powers we typically required hundreds of averages lasting several (often > 10) hours. Recent work using single microwave photon detectors [54] is a promising route to improve sensitivity. In tandem it is necessary to consider routes to improve memory efficiency in order to achieve useful memories. Promising approaches to this include the use of nuclear-spin 1=2 species (allowing the ensemble to be 100% thermally polarized at mK), optimal resonator design, increasing filling factor while maintaining large single-spin coupling necessary for WURST 

041014-10 



<!-- Start of picture text -->
2 3 50<br>80. 1 5 # ;<br>[0] 0 . 10 # 7) 7<br>o A SS<br>2 ———r" S + HEMT<br>3 iF 9<br>o 0 0 . 05 7#2-a 2 5i<br>=<br>- 50<br>@ # i<br>® 0 . 00 ! LT<br>= 00 0.5 1.0 0.0 0.5 1 . 0<br>Input pulse amplitude (arb . units)<br>= 0 . 05 AH 50 k<br>2 0 . 04 # = 25 Th<br>of rd =<br>g hg Q<br>® F < 0<br>L0 0 2 } o + HEMT<br>o iF + 2 2 5<br>Loot} a a i"<br>3 0.00 THEM HH<br>= 0.00 0.05 0.10 0.00 0.05 0.10<br>Input pulse amplitude (arb. units)<br><!-- End of picture text -->

PHYS. REV. X 12, 041014 (2022) 

JAMES O’SULLIVAN et al. 



<!-- Start of picture text -->
(a)<br>(b)<br>(c)<br><!-- End of picture text -->

FIG. 12. WURST-20 pulses with (a) the pulse amplitude and frequency shift for a WURST pulse with bandwidth 2 MHz and duration 100 μs. (b) The I and Q quadratures of the same WURST pulse. (c) The X and Y field quadratures in the cavity once the WURST pulse is filtered by a κ ¼ 200 kHz cavity. 

of the WURST pulse above the bandwidth of the cavity shortens the effective WURST pulse duration. We show an example WURST pulse in FM and AM [Fig. 12(a)], consequent in-phase and quadratures [Fig. 12(b)], and after modulation by a cavity [Fig. 12(c)]. 

## 2. Limits on WURST pulses 

In Fig. 6, a region of suitable WURST pulses—WURST — pulses which invert a large fraction of the spin ensemble is mapped out based on both theory and experiment described in this appendix. Using pulse sequences such as that in Fig. 1(a) (excitation followed by two identical WURST pulses), we have measured the refocusing efficiency. We measure the amplitude of the first (nominally silenced) and second echo and present them as a function of the WURST pulse bandwidth and amplitude in Fig. 13. A “good” WURST pulse results in no echo after the first WURSTand a loud echo after the second. If the distribution of spatial- and frequency-dependent phase imprinted on the spin ensemble by the WURST pulse is insufficient, a weak echo will still form [57]. 

By thresholding the lines we determine regions where WURST pulses adiabatically refocus a large fraction of spins. The constraint that the second echo must have a suitable magnitude (85 mV) gives the experimental 



FIG. 13. Top (bottom): amplitude of the first (second), nominally silenced (unsilenced), echo as a function of the pulse bandwidth for 200 μs WURST pulses. Inset to the bottom panel is the unsilenced data for low bandwidths, showing that there is a minimum bandwidth, similar to the cavity width, required to maximize the echo amplitude by refocusing all the spins in the cavity. The adiabaticity limit is determined by thresholding the unsilenced echo intensity relative to 85 mV shown as a black dashed line. The variation in echo amplitude was used to derive the uncertainties in the data points shown in Fig. 6. 

boundary to suitable WURST pulses shown in Fig. 6 based on adiabaticity. 

This is supported by a theoretical treatment [48]: 



where Qmin is an adiabaticity factor, R is the chirp rate, and ν is the nutation frequency (how quickly the spin precesses around the effective field). ν is minimal (and equal to the Rabi frequency) when the WURST frequency is the same as the spin frequency. We choose a minimum g0 for spins to be refocused and solve this equation for Qmin ¼ 1 finding a lower limit on pulse strength. 

In the homodyne scheme used in this work there is a limit placed by the finite frequency resolution we can imprint onto WURST pulses. The effective duration of the WURST pulse, TW;eff ¼ κTW=ΓW, is the time the WURST pulse of duration TW and total bandwidth ΓW takes to chirp across the cavity frequency κ. The inverse of this time gives an indication of the minimum frequency that can be resolved by modulating the pulse. This frequency must be less than the cavity bandwidth placing a limit on the maximum ΓW which can be used: 

041014-12 

PHYS. REV. X 12, 041014 (2022) 

RANDOM-ACCESS QUANTUM MEMORY USING CHIRPED PULSE … 



<!-- Start of picture text -->
(a) (b)<br>(c)<br><!-- End of picture text -->

FIG. 14. (a) The line of strong echoes from 2D maps of AB-echo sequences. We fit a line to these data and extract their gradient. (b) The gradient of the lines fit in (a) as a function of their extrapolated bandwidth at amplitude A ¼ 1 (black circles). The same gradient measurement was also performed using finer 1D sweeps of bandwidth and amplitude values and plot on the same axes (gray triangles) showing good agreement. We fit these data with ∂A=∂R ¼ C=R with C a fit parameter and return the red dashed line and C ¼ 0.93. (c) Width w of the line of equivalent WURST pulses as a function of WURST pulse parameters, defined as w ¼ ΔR sin θ where ΔR is the width in MHz/ms of the line of equivalent WURST pulses along the x axis in (a) and θ ¼ arctan ½ð∂A=∂RÞ= ð1V · ms=MHzÞ�. We fit a plane to this data to allow interpolation of the width as a function of bandwidth and amplitude. 



The maximum spectrometer power limits the power of WURSTs we can apply and is shown as the top boundary in Fig. 6. This line cannot be increased to arbitrarily high powers using higher power amplifiers as the superconducting resonators will limit the maximum power. There is also a minimum WURST bandwidth imposed by the cavity bandwidth. 

## 3. WURST pulse distinctiveness 

We partition the space of suitable WURSTs into “distinct” WURST pulses to estimate the memory capacity. We partition this region based upon two-WURST echo sequences where the first and second WURST pulse have different properties. The inset in Fig. 6 is the echo amplitude as the amplitude and chirp rate of the B pulse is varied. This sequence results in strong echoes along a line with positive gradient. In the main text we explain that this line of equivalent pulses is due to the acquisition of a dynamic phase. Together with other two-dimensional and onedimensional maps varying a B-pulse parameter, we interpolate the gradient and width of the line of equivalent pulses across the space of WURST pulses giving good inversion and use this interpolation to count WURST pulses. This interpolation is shown in Fig. 14 with the results in Fig. 6. 

## APPENDIX E: HIGH-POWER MEMORY SEQUENCES 

To further confirm the memory protocol functions as intended, we ran identical memory protocols cycling different excitations on and off so that in each run only one excitation was used. To speed up this measurement we increased the power of the input pulses and the results are shown in Fig. 15 where we also show a replication of the full memory protocol at higher power. In each of the sequences where there is only one excitation stored, we only retrieve one echo, and the echo occurs when we would 

041014-13 

PHYS. REV. X 12, 041014 (2022) 

JAMES O’SULLIVAN et al. 



<!-- Start of picture text -->
(a) (b)<br>(c) (d)<br>(e)<br><!-- End of picture text -->



FIG. 15. The same memory sequence as shown in Fig. 5 was performed here at higher input power (∼15 000 photons per excitation – pulse); the raw transient trace of the sequence is shown in (e). In (a) (d) the same experiment was repeated with only one of each of the four input excitation pulses, A, B, C, and D, turned on. This allows us to unambiguously determine which echo originates from which excitation pulse. We see that a single echo appears in the expected read slot in each case. We also see that no other echoes appear when only one excitation is turned on. In this power regime, as well as amplifying (nonlinearly), the JPA also imparts poorly characterized phase shifts seen particularly when comparing (c)–(e). 

expect the echo to form, further confirming that the memory protocol works. 



- [1] H. J. Kimble, The Quantum Internet, Nature (London) 453, 1023 (2008). 

- [2] M. Mariantoni, H. Wang, T. Yamamoto, M. Neeley, R. C. Bialczak, Y. Chen, M. Lenander, E. Lucero, A. D. O’Connell, D. Sank et al., Implementing the Quantum von 

Neumann Architecture with Superconducting Circuits, Science 334, 61 (2011). 

- [3] N. Jiang, Y.-F. Pu, W. Chang, C. Li, S. Zhang, and L.-M. Duan, Experimental Realization of 105-Qubit Random Access Quantum Memory, npj Quantum Inf. 5, 28 (2019). 

- [4] G. Wolfowicz, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. Thewalt, S. A. Lyon, and J. J. Morton, Atomic Clock Transitions in Silicon-Based Spin Qubits, Nat. Nanotechnol. 8, 561 (2013). 

041014-14 

PHYS. REV. X 12, 041014 (2022) 

RANDOM-ACCESS QUANTUM MEMORY USING CHIRPED PULSE … 

- [5] V. Ranjan, J. O’Sullivan, E. Albertinale, B. Albanese, T. Chaneli`ere, T. Schenkel, D. Vion, D. Esteve, E. Flurin, J. J. L. Morton, and P. Bertet, Multimode Storage of Quantum Microwave Fields in Electron Spins over 100 ms, Phys. Rev. Lett. 125, 210505 (2020). 

- [6] M. Steger, K. Saeedi, M. Thewalt, J. Morton, H. Riemann, N. Abrosimov, P. Becker, and H.-J. Pohl, Quantum Information Storage for over 180 s Using Donor Spins in a 28Si Semiconductor Vacuum, Science 336, 1280 (2012). 

- [7] A. Ortu, A. Tiranov, S. Welinski, F. Fröwis, N. Gisin, A. Ferrier, P. Goldner, and M. Afzelius, Simultaneous Coherence Enhancement of Optical and Microwave Transitions in Solid-State Electronic Spins, Nat. Mater. 17, 671 (2018). 

- [8] N. Bar-Gill, L. M. Pham, A. Jarmola, D. Budker, and R. L. Walsworth, Solid-State Electronic Spin Coherence Time Approaching One Second, Nat. Commun. 4, 1743 (2013). 

- [9] D. D. Sukachev, A. Sipahigil, C. T. Nguyen, M. K. Bhaskar, R. E. Evans, F. Jelezko, and M. D. Lukin, Silicon-Vacancy Spin Qubit in Diamond: A Quantum Memory Exceeding 10 ms with Single-Shot State Readout, Phys. Rev. Lett. 119, 223602 (2017). 

- [10] B. Naydenov, F. Dolde, L. T. Hall, C. Shin, H. Fedder, L. C. L. Hollenberg, F. Jelezko, and J. Wrachtrup, Dynamical Decoupling of a Single-Electron Spin at Room Temperature, Phys. Rev. B 83, 081201(R) (2011). 

- [11] H. Y. Carr and E. M. Purcell, Effects of Diffusion on Free Precession in Nuclear Magnetic Resonance Experiments, Phys. Rev. 94, 630 (1954). 

- [12] S. Meiboom and D. Gill, Modified Spin-Echo Method for Measuring Nuclear Relaxation Times, Rev. Sci. Instrum. 29, 688 (1958). 

- [13] J. J. Morton, A. M. Tyryshkin, R. M. Brown, S. Shankar, B. W. Lovett, A. Ardavan, T. Schenkel, E. E. Haller, J. W. Ager, and S. Lyon, Solid-State Quantum Memory Using the 31P Nuclear Spin, Nature (London) 455, 1085 (2008). 

- [14] Y. Kubo, F. R. Ong, P. Bertet, D. Vion, V. Jacques, D. Zheng, A. Dr´eau, J.-F. Roch, A. Auff`eves, F. Jelezko, J. Wrachtrup, M. R. Barthe, P. Bergonzo, and D. Esteve, Strong Coupling of a Spin Ensemble to a Superconducting Resonator, Phys. Rev. Lett. 105, 140502 (2010). 

- [15] S. Weichselbaumer, M. Zens, C. W. Zollitsch, M. S. Brandt, S. Rotter, R. Gross, and H. Huebl, Echo Trains in Pulsed Electron Spin Resonance of a Strongly Coupled Spin Ensemble, Phys. Rev. Lett. 125, 137701 (2020). 

- [16] S. Probst, H. Rotzinger, S. Wünsch, P. Jung, M. Jerger, M. Siegel, A. V. Ustinov, and P. A. Bushev, Anisotropic RareEarth Spin Ensemble Strongly Coupled to a Superconducting Resonator, Phys. Rev. Lett. 110, 157001 (2013). 

- [17] D. I. Schuster, A. P. Sears, E. Ginossar, L. DiCarlo, L. Frunzio, J. J. L. Morton, H. Wu, G. A. D. Briggs, B. B. Buckley, D. D. Awschalom, and R. J. Schoelkopf, HighCooperativity Coupling of Electron-Spin Ensembles to Superconducting Cavities, Phys. Rev. Lett. 105, 140501 (2010). 

- [18] T. Zhong, J. M. Kindem, J. Rochman, and A. Faraon, Interfacing Broadband Photonic Qubits to On-Chip Cavity-Protected Rare-Earth Ensembles, Nat. Commun. 8, 14107 (2017). 

- [19] M. Afzelius, N. Sangouard, G. Johansson, M. Staudt, and C. Wilson, Proposal for a Coherent Quantum Memory for 

Propagating Microwave Photons, New J. Phys. 15, 065008 (2013). 

- [20] B. Julsgaard, C. Grezes, P. Bertet, and K. Mølmer, Quantum Memory for Microwave Photons in an Inhomogeneously Broadened Spin Ensemble, Phys. Rev. Lett. 110, 250503 (2013). 

- [21] E. L. Hahn, Spin Echoes, Phys. Rev. 80, 580 (1950). 

- [22] S. Probst, H. Rotzinger, A. V. Ustinov, and P. A. Bushev, Microwave Multimode Memory with an Erbium Spin Ensemble, Phys. Rev. B 92, 014421 (2015). 

- [23] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima et al., Multimode Storage and Retrieval of Microwave Fields in a Spin Ensemble, Phys. Rev. X 4, 021049 (2014). 

- [24] Z. Bao, Z. Wang, Y. Wu, Y. Li, C. Ma, Y. Song, H. Zhang, and L. Duan, On-Demand Storage and Retrieval of Microwave Photons Using a Superconducting Multiresonator Quantum Memory, Phys. Rev. Lett. 127, 010503 (2021). 

- [25] M. Lovrić, D. Suter, A. Ferrier, and P. Goldner, Faithful Solid State Optical Memory with Dynamically Decoupled Spin Wave Storage, Phys. Rev. Lett. 111, 020503 (2013). 

- [26] A. I. Lvovsky, B. C. Sanders, and W. Tittel, Optical Quantum Memory, Nat. Photonics 3, 706 (2009). 

- [27] A. Anderson, R. Garwin, E. Hahn, J. Horton, G. Tucker, and R. Walker, Spin Echo Serial Storage Memory, J. Appl. Phys. 26, 1324 (1955). 

- [28] J. Ruggiero, J.-L. Le Gouët, C. Simon, and T. Chaneli`ere, Why the Two-Pulse Photon Echo Is Not a Good Quantum Memory Protocol, Phys. Rev. A 79, 053851 (2009). 

- [29] V. Damon, M. Bonarota, A. Louchet-Chauvet, T. Chaneliere, and J.-L. Le Gouët, Revival of Silenced Echo and Quantum Memory for Light, New J. Phys. 13, 093031 (2011). 

- [30] V. Ranjan, Y. Wen, A. Keyser, S. Kubatkin, A. Danilov, T. Lindström, P. Bertet, and S. de Graaf, Spin Echo Silencing Using a Current-Biased Frequency-Tunable Resonator, arXiv:2206.04488. 

- [31] Y. Kubo, C. Grezes, A. Dewes, T. Umeda, J. Isoya, H. Sumiya, N. Morishita, H. Abe, S. Onoda, T. Ohshima et al., Hybrid Quantum Circuit with a Superconducting Qubit Coupled to a Spin Ensemble, Phys. Rev. Lett. 107, 220501 (2011). 

- [32] B. Kraus, W. Tittel, N. Gisin, M. Nilsson, S. Kröll, and J. I. Cirac, Quantum Memory for Nonstationary Light Fields Based on Controlled Reversible Inhomogeneous Broadening, Phys. Rev. A 73, 020302(R) (2006). 

- [33] T. Zhong, J. M. Kindem, J. G. Bartholomew, J. Rochman, I. Craiciu, E. Miyazono, M. Bettinelli, E. Cavalli, V. Verma, S. W. Nam et al., Nanophotonic Rare-Earth Quantum Memory with Optically Controlled Retrieval, Science 357, 1392 (2017). 

- [34] H. Wu, R. E. George, J. H. Wesenberg, K. Mølmer, D. I. Schuster, R. J. Schoelkopf, K. M. Itoh, A. Ardavan, J. J. L. Morton, and G. A. D. Briggs, Storage of Multiple Coherent Microwave Excitations in an Electron Spin Ensemble, Phys. Rev. Lett. 105, 140503 (2010). 

- [35] J. Baum, R. Tycko, and A. Pines, Broadband and Adiabatic Inversion of a Two-Level System by Phase-Modulated Pulses, Phys. Rev. A 32, 3435 (1985). 

041014-15 

PHYS. REV. X 12, 041014 (2022) 

JAMES O’SULLIVAN et al. 

- [36] E. Kupce and R. Freeman, Adiabatic Pulses for Wideband Inversion and Broadband Decoupling, J. Magn. Reson., Ser. A 115, 273 (1995). 

- [37] Ēriks Kupce and R. Freeman, Stretched Adiabatic Pulses for Broadband Spin Inversion, J. Magn. Reson., Ser. A 117, 246 (1995). 

- [38] M. Garwood and L. DelaBarre, The Return of the Frequency Sweep: Designing Adiabatic Pulses for Contemporary NMR, J. Magn. Reson. 153, 155 (2001). 

- [39] L. A. O’Dell, The WURST Kind of Pulses in Solid-State NMR, Solid State Nucl. Magn. Reson. 55–56, 28 (2013). 

- [40] V. Malinovsky and J. Krause, General Theory of Population Transfer by Adiabatic Rapid Passage with Intense, Chirped Laser Pulses, Eur. Phys. J. D 14, 147 (2001). 

- [41] Y. A. Tesiram, Implementation Equations for HSn RF Pulses, J. Magn. Reson. 204, 333 (2010). 

- [42] A. J. Sigillito, H. Malissa, A. M. Tyryshkin, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. Thewalt, K. M. Itoh, J. J. Morton et al., Fast, Low-Power Manipulation of Spin Ensembles in Superconducting Microresonators, Appl. Phys. Lett. 104, 222407 (2014). 

- [43] K. Gerasimov, M. Minnegaliev, S. Moiseev, R. Urmancheev, T. Chaneli`ere, and A. Louchet-Chauvet, Quantum Memory in an Orthogonal Geometry of Silenced Echo Retrieval, Opt. Spectrosc. 123, 211 (2017). 

- [44] M. Bonarota, J. Dajczgewand, A. Louchet-Chauvet, J.-L. Le Gouët, and T. Chaneli`ere, Photon Echo with a Few Photons in Two-Level Atoms, Laser Phys. 24, 094003 (2014). 

- [45] J. O’Sullivan, O. W. Kennedy, C. W. Zollitsch, M. Šimėnas, C. N. Thomas, L. V. Abdurakhimov, S. Withington, and J. J. L. Morton, Spin-Resonance Linewidths of Bismuth Donors in Silicon Coupled to Planar Microresonators, Phys. Rev. Applied 14, 064050 (2020). 

- [46] E. Abe, H. Wu, A. Ardavan, and J. J. Morton, Electron Spin Ensemble Strongly Coupled to a Three-Dimensional Microwave Cavity, Appl. Phys. Lett. 98, 251108 (2011). 

- [47] L. Viola, E. Knill, and S. Lloyd, Dynamical Decoupling of Open Quantum Systems, Phys. Rev. Lett. 82, 2417 (1999). 

- [48] A. Doll, S. Pribitzer, R. Tschaggelar, and G. Jeschke, Adiabatic and Fast Passage Ultra-Wideband Inversion in Pulsed EPR, J. Magn. Reson. 230, 27 (2013). 

- [49] M. L. Dantec, M. Rančić, S. Lin, E. Billaud, V. Ranjan, D. Flanigan, S. Bertaina, T. Chaneli`ere, P. Goldner, A. Erb, R. B. Liu,D.Est`eve,D.Vion,E.Flurin,and P.Bertet, Twenty-Three Millisecond Electron Spin Coherence of Erbium Ions in a Natural-Abundance Crystal, arXiv:2106.14974. 

- [50] O. W. Kennedy, J. O’Sullivan, C. W. Zollitsch, C. N. Thomas, S. Withington, and J. J. Morton, Strain in Heterogeneous Quantum Devices with Atomic Layer Deposition, Mater. Quantum Technol. 1, 045002 (2021). 

- [51] https://rdr.ucl.ac.uk/articles/dataset/Data-for-Random-accessquantum-memory-using-chirped-pulse-phase-encoding-/ 14541747. 

- [52] E. Abe, H. Wu, A. Ardavan, and J. J. L. Morton, Electron Spin Ensemble Strongly Coupled to a Three-Dimensional Microwave Cavity, Appl. Phys. Lett. 98, 251108 (2011). 

- [53] A. Bienfait, J. Pla, Y. Kubo, X. Zhou, M. Stern, C. Lo, C. Weis, T. Schenkel, D. Vion, D. Esteve et al., Controlling Spin Relaxation with a Cavity, Nature (London) 531, 74 (2016). 

- [54] E. Albertinale, L. Balembois, E. Billaud, V. Ranjan, D. Flanigan, T. Schenkel, D. Est`eve, D. Vion, P. Bertet, and E. Flurin, Detecting Spins by Their Fluorescence with a Microwave Photon Counter, Nature (London) 600, 434 (2021). 

- [55] C. W. Gardiner and M. J. Collett, Input and Output in Damped Quantum Systems: Quantum Stochastic Differential Equations and the Master Equation, Phys. Rev. A 31, 3761 (1985). 

- [56] V. Ranjan, S. Probst, B. Albanese, A. Doll, O. Jacquot, E. Flurin, R. Heeres, D. Vion, D. Esteve, J. Morton et al., Pulsed Electron Spin Resonance Spectroscopy in the Purcell Regime, J. Magn. Reson. 310, 106662 (2020). 

- [57] R. Bhattacharyya and L. Frydman, Quadrupolar Nuclear Magnetic Resonance Spectroscopy in Solids Using Frequency-Swept Echoing Pulses, J. Chem. Phys. 127, 194503 (2007). 

041014-16 

