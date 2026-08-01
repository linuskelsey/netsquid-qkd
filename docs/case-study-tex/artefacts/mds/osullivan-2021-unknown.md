## **Random-access quantum memory using chirped pulse phase encoding** 

James O’Sullivan,<sup>1,</sup><sup>_∗_</sup> Oscar W. Kennedy,<sup>1,</sup><sup>_∗_</sup> Kamanasish Debnath,<sup>2</sup> Joseph Alexander,<sup>1</sup> Christoph W. Zollitsch,<sup>1</sup> Mantas Sim˙enas,<sup>ˇ1</sup> Akel Hashim,<sup>3, 4</sup> Christopher N. Thomas,<sup>5</sup> Stafford Withington,<sup>5</sup> Irfan Siddiqi,<sup>3, 4</sup> Klaus Mølmer,<sup>2</sup> and John J. L. Morton<sup>1, 6,</sup><sup>_†_</sup> 

> 1 _London Centre for Nanotechnology, UCL, 17-19 Gordon Street, London, WC1H 0AH, UK_ 

> 2 _Department of Physics and Astronomy, Aarhus University, DK-8000 Aarhus C, Denmark_ 

> 3 _Quantum Nanoelectronics Laboratory, Department of Physics, UC Berkeley, California 94720, USA_ 

> 4 _Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA_ 

> 5 _Cavendish Laboratory, University of Cambridge, JJ Thomson Ave, Cambridge CB3 0HE, UK_ 

> 6 _Department of Electrical and Electronic Engineering, UCL, Malet Place, London, WC1E 7JE, UK_ 

As in conventional computing, memories for quantum information benefit from high storage density and, crucially, random access, or the ability to read from or write to an arbitrarily chosen register. However, achieving such random access with quantum memories in a dense, hardwareefficient manner remains a challenge. Here we introduce a protocol using chirped pulses to encode qubits within an ensemble of quantum two-level systems, offering both random access and naturally supporting dynamical decoupling to enhance the memory lifetime. We demonstrate the protocol in the microwave regime using donor spins in silicon coupled to a superconducting cavity, storing up to four multi-photon microwave pulses in distinct memory modes and retrieving them on-demand up to 2 ms later. This approach offers the potential for microwave random access quantum memories with lifetimes exceeding seconds, while the chirped pulse phase encoding could also be applied in the optical regime to enhance quantum repeaters and networks. 

Quantum memories (QMs) capable of faithfully storing and recalling quantum states on-demand are powerful ingredients in building quantum networks [1] and quantum processors [2]. Ensembles of quantum systems are natural platforms for QMs, given their large storage capacity. Multiple qubits can be stored taking advantage of direct spatial addressing to access different regions of the ensemble [2, 3]. However, for ensembles in the solid state that offer prospects for high-density QMs and typically have inhomogenous broadening, _spectral_ -addressing can be used to distinguish excitations stored collectively in the ensemble. Solid-state atomic ensembles have long coherence times for both microwave [4–8] and optical [7–9] transitions and can couple to resonant cavities facilitating read, write and control operations. Coherent control allows coherence times to be extended by dynamical decoupling (DD) [8, 10–12] or transferring the qubit state to a more coherent transition [13]. Coupling the ensemble to a cavity in the strong coupling regime [14–18] or with cooperativity _C_ = 1 facilitates writing and reading information with unit efficiency [19, 20]. 

One of the simplest memory protocols in inhomogeneously broadended systems is the Hahn echo [21], in which an excitation stored within an ensemble is inverted by a single _π_ pulse and re-emitted later as an ‘echo’. This has been used widely for retrieval of weak excitations in multimode microwave [5, 22, 23] and optical [24, 25] memories and indeed formed the basis of early (classical) information storage proposals [26]. However, the simple Hahn echo approach is unsuitable for quantum memories, as it leads to amplified (and thus noisy) emission from the quantum systems in their excited state [27]. One solution is using two _π_ pulses to return the ensem- 

ble predominantly to the ground state before the memory is accessed [20, 28]. This requires suppressing the emission of the echo that would appear after the first _π_ pulse. A second limitation of the Hahn echo sequence is that it acts as a ‘first-in last-out’ memory, rather than permitting random access to stored qubits. Various approaches have been explored to address these limitations: frequency-tunable cavities can be shifted off-resonance except when the desired echo is being emitted [29]; external electric or magnetic field gradients can be used to label stored excitations [30]; and AC Stark shifts can shift the emission of excitations into different time bins [31]. None of these ingredients alone realises a random access QM and the requirement of additional control fields poses a significant practical limitation. For example, the magnetic field gradients used in Ref. [32] to retrieve two microwave excitations in arbitrary order have poor compatibility with the superconducting resonators and qubits. In this Article we introduce a simpler and more powerful approach to labelling and recalling stored qubits from an ensemble QM, using chirped control pulses. This protocol suppresses unwanted echoes, allows random access to multiple memory modes (read and write operations performed in arbitrary order), and naturally embeds DD. We demonstrate the performance of the protocol in a prototype memory using weak microwave excitations stored within donor spins in silicon. 

Sweeping the frequency of a control pulse across that of an atomic transition can be used to realise an inversion (or _π_ pulse) by ‘adiabatic fast passage’ (AFP) [33–36]. Such chirped pulses, with forms such as ‘wideband, uniform rate, smooth truncation’ (WURST) [37] (see SI for further details) among others e.g. [38, 39] — offer sev- 



<!-- Start of picture text -->
(b) P A dephasinT g & WURST r ephasingT /dephasinT g &WURST r ephasinT g A\<br>5 inversion (x) | inversion (x)<br>t<br>1 |<br>Z ou a in echo formation  requires Ko 9<br>v z Tn<br>I a inversion (7) y| ¢,, t<br>6 (+3) (+3) (- 2) (- 2)<br>© ’" “AFR.AW e xciteitat. io n =kad 7 A emechoitt\ ed  ST<br>0 e s © O O " Oo<br>read/ | Ol y [9] [| [| | L f<br>write |] CE 0] [| [| 0] :<br>at (© | ] By [] A O] : S| 1 Of 7:<br>by= 0 ju —FY (© (ERS 00 (©) I | I |  EO] | IN| I Lf —>,<br>wo s H OH OH WF B H<br>L] [| L] [| [© [©] [|<br>INV +3 INV +3 INV -2 INV -2<br>WRITE READ<br><!-- End of picture text -->

3 

pulses. In Fig. 2(a,b) we study a pair of identical WURST pulses, plotting spin expectation values _⟨σ_ ˆ _y_<sup>_i⟩_</sup> summed over all spins in an ensemble when the WURST pulse chirps _±_ 0 _._ 25 MHz in 100µs showing that the initial peak value is well recovered. As long as the spin linewidth, _γ_ ≲ ∆ _f_ , the bandwidth of the WURST pulse, the refocusing effect yields approximately unit efficiency. This supports the use of repeated WURST pulses in our protocol and verifies that these will not limit our memory efficiency, at least for a core of sufficiently coupled spins. Next in Fig. 2 (c) we examine the simplest sequence illustrating random access in the memory protocol, where two distinct WURST pulses are used (‘A’) and (‘B’), with chirp rates of _−_ 2 _π ×_ 11 _._ 25 MHz/ms and 2 _π ×_ 7 _._ 50 MHz/ms respectively. The simulation considers two input excitations, _α_ and _β_ , applied in the sequence _α − A − β − B − B − Eβ − A − Eα_ . We see the input _β_ is remitted as echo _Eβ_ following the second _B_ pulse, while _α_ is remitted as _Eα_ only after the second _A_ pulse, confirming the basic principle of the random access protocol. 

To further validate the protocol we perform experiments on a prototype device. The memory consists of an ensemble of bismuth donor spins in natural silicon, coupled to a planar superconducting niobium resonator at 100 mK with resonant frequency 7.093 GHz and quality factor _∼_ 18,000. The bismuth donors are implanted at a target density of 10<sup>17</sup> cm<sup>_−_3</sup> in the top 1 µm of the sample. Further details of the chip and setup are provided in the supplementary information. A schematic of the device, its magnetic field and the implantation profile is shown in in (SI) Fig. S1, a schematic of the full setup is shown in (SI) Fig. S2 and details of resonator performance are provided in (SI) Fig. S3. 

Fitting to S-parameter measurements of the cavity gives a cooperativity _C_ = 0 _._ 07(2) (see SI [43]), leading to a predicted one-way memory efficiency of _η_ em = (1+4 _<u>CC</u>_ )<sup>2</sup> of 0.2 (Ref [19])). Although this is larger than previously reported values for ensemble microwave memories of 0.01–0.04 [5, 22, 23], it poses a bound for the amplitude of the retrieved excitations in our demonstration of the random access QM protocol below. 

Despite the spin-cavity coupling in these experiments being well below unit cooperativity, we can already see the importance of suppressing echo emission from an inverted ensemble. In Fig. 3(a-d) we apply _N_ inv WURST _π_ -pulses (for _N_ inv=0–3) before an echo sequence to selectively prepare the ensemble into a ground ( _N_ inv even) or inverted ( _N_ inv odd) state. Using weak excitations of _⟨n⟩∼_ 200 microwave photons ensures that the ensemble is only weakly perturbed from the ground or excited state when emitting. We see that echoes emitted from an inverted ensemble have larger amplitude than those emitted from a (quasi-)ground state ensemble, indicating that there has been amplification of the input signal from stimulated emission (the echo is always weaker than 



<!-- Start of picture text -->
(a) 400<br>200<br>0<br>-200<br>-400<br>0    100  200   300   400<br>Time (μs)<br>(b) 1<br>0.5<br>0<br>0  0.4  0.8   1.2  1.6  2<br> γ (MHz)<br>(c)<br><!-- End of picture text -->

Figure 2. **Simulation of the memory protocol.** Numerical simulations of 3.23 _×_ 10<sup>5</sup> spins with 100 kHz linewidth showing the effects of a WURST pulse on a large ensemble of emitters. (a) Expectation values _⟨σ_ ˆ _y_<sup>_i⟩_summedover</sup> all spins shows that, following a pair of identical WURST pulses, an initial excitation is faithfully recovered as an echo. (b) The ratio of the excitation to echo amplitude ( _χ_ ) is shown as a function of the spin linewidth _γ_ for a WURST pulse of 0.5 MHz bandwidth. For spin linewidths within the WURST bandwidth the sequence has approximately unit efficiency. (c) Retrieval of two weak excitations within an ‘ABBA’ sequence composed of two different WURST pulses (A and B) with different chirp rates, _RA_ = _−_ 2 _π ×_ 11 _._ 25 MHz/ms and _RB_ = 2 _π ×_ 7 _._ 50 MHz/ms. Two weak pulses, _α_ and _β_ , are stored in the spins and re-emitted at the expected tims as echoes _Eα_ and _Eβ_ . 

the input signal due to other losses). This amplification of states as they are emitted is incompatible with high fidelity state retrieval, and is why robust quantum memory schemes must ensure emission from a (quasi-)ground state ensemble, as supported by our protocol . 

By increasing the delay between WURST pulses, we measure a coherence time of this prototype memory, _T_ 2 _∼_ 0 _._ 6 ms (Fig. S3). This lifetime can be extended using dynamical decoupling (DD) sequences which in- 

4 









<!-- Start of picture text -->
a) Excitation c) d)<br>x Ninv Echo 15<br>10<br>t<br>8<br>10<br>b) Ground 6<br>4 5<br>2 Excited<br>Ground<br>0 0<br>Excited 560 570 0 1 2 3<br>e) t (μs) Inversion Pulses N<br>1.0 n<br>n<br>0.5<br>T 2 = 2.0 ± 0.2 ms<br>0.0<br>0 1 2 3 4 5 6<br>t (ms)<br>Signal (mV)<br>Echo Amplitude (mV)<br>Echo mag.  (fraction of  = 0 echo) t<br><!-- End of picture text -->

Figure 3. **Demonstrating the importance of suppressed echo emission.** (a) The pulse sequence used to study the echo following a pair of WURST pulses as a function of the state of the ensemble. (b) The approximate ensemble ground and excited state in a Bloch sphere representation of the ensemble magnetisation. (c) Two example echoes emitted from the ground state ( _N_ inv = 2) or inverted state ( _N_ inv = 3). Larger amplitude echoes are seen from the inverted ensembles due to amplification of the echo, which adds noise to a quantum memory. (d) Echo amplitude as a function of _N_ inv. The overall reduction of echo amplitude with increasing _N_ inv is likely due to gradual saturation of the spin ensemble. (e) Coherence decay rates from different WURST dynamical decoupling sequences. Given identical pulses (A[AA] _n_ A - purple) echo emission occurs every second pulse leading to an accelerated decay in coherence compared to an A[BB] _n_ A (pink) sequence where only one echo is emitted, at the end. A fit to the A[BB] _n_ A data (dashed line) gives a coherence time of 2 ms, while fitting to the A[AA] _n_ A data accounting for additional loss from repeated echoes (dashed line, see Eq. 5 SI) gives a memory efficiency _η_ em of 0.17. Error bars represent one standard deviation from fitting Gaussians to echoes. 

volve a train of repeated _π_ -pulses [12, 44]. If the DD sequence uses identical WURST pulses (i.e. A[AA] _n_ A), an echo is emitted after every pair of pulses as shown in the upper inset to Fig.3(e). This repeated echo emission can be avoided by introducing a second type of WURST pulse (‘B’) of different chirp rate and/or amplitude to the first (‘A’), creating the sequence A[BB] _n_ A, shown in the 

lower inset to Fig.3(e). Only one echo appears in this sequence, after the second ‘A’ pulse which is applied at the end, and the decay time constant of this echo provides a measure of the memory storage lifetime, _T_ M = 2 _._ 0(2) ms. This lifetime is about three times longer than that measured with a Hahn echo, thanks to the effect of DD. The A[AA] _n_ A WURST DD sequence — in which echoes are emitted periodically throughout — gives a decay time constant _shorter_ than _T_ M. We model this assuming a constant fraction _η_ em of the excitation is lost with each echo, in addition to exponential decay with time constant _T_ M. Fitting this model yields _η_ em = 0 _._ 17(7), and interpreting this value as the one-way efficiency we find good agreement with the value extracted from S-parameter measurements. In a high efficiency quantum memory ( _C ∼ η_ em _∼_ 1), DD sequences of this type will be essential to avoid premature emission of stored excitations. 

Having confirmed control of echo emission using chirped pulses, we present in Figure 4 (a) an experimental demonstration of the random access protocol introduced earlier, showing the storage, protection and retrieval of four weak ( _⟨n⟩∼_ 1200 photon) microwave excitations, using five distinct WURST pulses (see Fig. 4 (b)). The photon number was calibrated from measurements of Rabi frequency and Purcell relaxation (see SI and Fig. S2). Each excitation is encoded into the memory using a pair of identical WURST pulses (colour-coded in teal, coral, lime and mustard), and retrieved later (storage time varying from 0.5 to 2.5 ms) by applying the same pair of pulses. Each echo can be unambiguously matched to one of the input excitations through its phase (see Fig. 4 (c)), which we confirm by repeating permutations of the sequence with only one excitation present (Fig. S10). A fifth variant of WURST pulse (shown in grey) is used to perform DD. The weak amplitude of retrieved signals relative to input states is due primarily to the limited cooperativity in these experiments, rather than the control fidelity in the random-access protocol or decoherence (see SI §D). Rescaling the echo amplitudes by the factors shown in Fig. 4 (c) we observe that the phase of the excitation is generally well preserved. The largest phase error, from the second excitation (coral) is attributed to a phase shift from the Josephson parametric amplifier, as the echo is of larger amplitude due to the short storage time (Fig. S4). 

The memory capacity is determined by the number of independent WURST pulses that can be used in the protocol. This is related to the spectral width (∆ _f_ ) of the storage ensemble, the narrower of the cavity linewidth _κ_ and that of the inhomogeneous ensemble. The WURST pulses can be parameterised using their chirp rate _R_ and amplitude _A_ W, bounds illustrated in Fig. 5. Adiabiticity of refocusing imposes a lower bound of _A_ W [45], with an upper bound set by the maximum pulse amplitude, limited for example by the pulse amplifier or sample heating). We determined the adiabatic bounds on 

5 



<!-- Start of picture text -->
a) 200<br>0<br>I<br>Q<br>-200<br>0 1 2 3 4<br>t (ms)<br>b) Amplitude c) Q (mV)<br>+f<br>100<br>t x3<br>-f 50<br>Pulse Chirp Rate -100 -50 50 100<br>(MHz/ms)<br>x9 x11 I (mV)<br>-11.25<br>+15.00 -50<br>+7.50 x31<br>Input<br>-100<br>-22.50 Output<br>+30.00<br>Chirp<br>Signal (mV)<br><!-- End of picture text -->

Figure 4. **Experimental demonstration of the random access memory protocol.** (a) An illustrative segment of the protocol in which WURST pulses, excitations, and echoes are colour coded, with WURST parameters as defined in (b). In total four excitations are stored for times up to 2 ms. Excitations and echoes are shown with magnified echoes offset from the main trace. The first and last pulses do not come in pairs as the memory sequence starts and finishes half way through a clock cycle. (c) Echoes and excitations on an Argand diagram matching their phases. The magnitude of each echo is rescaled to account for losses from the finite spin-resonator cooperativity in this experiment and spin decoherence. 

_A_ W in our experiment through microwave simulations, confirmed through experiments of the type illustrated in Fig. 1(a) (Fig. S6). The rate _R_ has some upper bound set by the experimental frequency resolution and a lower bound determined by the need to at least chirp across ∆ _f_ within the effective duration of the WURST pulse ( _T_ W _,_ eff ), such that _R ≫_ ∆ _f /T_ W _,_ eff . 

The separation of distinct pulses in _R_ and _A_ W is governed by the requirement of independence in the storage modes of the memory. We explore this using pulse sequences of the form _α − π_ A _− π_ B _−_ [echo], where an excitation _α_ is followed by two WURST pulses whose parameters are varied. For sufficiently distinct _π_ A and _π_ B, no echo should be observed. First, we fix the parameters of _π_ A and vary those of _π_ B, shown in the inset to Fig. 5. Equivalent WURST pulses lie on lines of positive gradient — as _R_ increases, the phase from the WURST pulse decreases, compensated by increasing _A_ W. Additional two-dimensional parameter sweeps are shown as green lines in Fig. 5, we also acquire several one-dimensional sweeps (a subset are shown in Fig. 5). We extract the 



<!-- Start of picture text -->
3500<br>Spectrometer<br>3000 max. power<br>2500 Frequency<br>resolution<br>2000<br>1500<br>20 0<br>1000 0<br>-20 0<br>Non adiabatic<br>500<br>2 0 2<br>d R (MHz/ms)<br>0<br>0 20 40 60 80 100<br>Chirp rate (MHz/ms)<br>)<br>z<br>H<br>k<br>(<br>y<br>c<br>n<br>e<br>u<br>q<br>e<br>r<br>f<br>bi<br>a<br>R<br>d (kHz)<br><!-- End of picture text -->

Figure 5. **Counting memory modes.** Each memory mode is determined by the phase pattern _φ_ W imparted by a WURST pulse. The parameter space where WURST pulses efficiently refocus spins is bounded in black. Bounds are the cavity linewidth, the maximum spectrometer power and requirements the WURST is adiabatic. A frequency resolution limit occurs due to the homodyne scheme and would be removed in a heterodyne scheme. We measure the adiabaticity limit by thresholding echo intensity shown in the SI and here by the black dashed line giving good agreement with the theoretical line. We measure distinctiveness of WURST pulses using AB-echo sequences. The results of sweeping the B pulse chirp rate at maximum power are inset to the top of the figure and fit by Gaussian profiles. We show a two dimensional map sweeping chirp rate and Rabi frequency in the inset. In 2D sweeps there are lines of WURST pulses which impart the same _φ_ W function to the spin ensemble. Green lines in the main panel show the line of equivalent WURST pulses from other two dimensional maps. Interpolating data from AB-echo sweeps we determine the width of a line of equivalent WURST pulses at fixed Rabi frequency. We partition the space of available WURSTs into unique WURSTs (i.e. memory modes) by constraining neighbouring WURST pulses to be separated by the half width hundredth max and show an example partitioning where blue/white sections indicate unique WURST pulses. We show the WURST pulses used in Fig. 4 where the up/down markers refer to positive/negative chirp direction. 

different regions of WURST pulses equivalence requiring that each WURST pulse is separated by at least the half width, _hundredth_ max of the neighbouring regions (Fig. S7). We find _∼_ 8 distinct WURST pulses at an amplitude of 0.6 V, and the same from chirping in the reverse direction, giving _∼_ 16 distinct memory modes. 

Chirped pulse encoding can be combined with other methods such as time-bin encoding (used to store up to 100 weak microwave excitations [5, 32]) to implement a memory offering random access to large registers. For example, in Fig. 6 we demonstrate how a pair of WURST pulses can be used to store a register of five microwave 

6 



<!-- Start of picture text -->
a excitations [no echoes] echoes<br>10 10<br>100 2 4<br>1 3 5<br>0 0 0<br>1 2 3 4<br>100 5<br>10 10<br>time ( μ s) 0 100 350 400 450 700 800<br>excitations echoes<br>,i<br>Signal (mV)<br><!-- End of picture text -->

Figure 6. **First in first out (FIFO) time bin encoding of multiple echoes.** (a) An experimental demonstration of multiple excitations stored using the FIFO protocol with two identical WURST pulses. The pattern of excitation/echo phases allows echoes and excitations to be unambiguously matched. (b) Schematic showing evolution of spin waves and WURST phase resulting in the FIFO encoding with silenced echoes. 

excitations, later retrieved in the same order in which they were written (a first-in first-out, or FIFO memory). Therefore, by replacing the single excitations shown in Fig. 4 with such registers, the capacity of the quantum memory is further extended. Additional strategies for increasing the storage capacity include addressing the instrumentation-limited bounds on _R_ and _A_ W, and by increasing the WURST pulse duration (at the expense of slower read/write speeds and less effective DD). 

The memory efficiency in the experimental demonstration was primarily limited by the spin-resonator cooperativity ( _C ∼_ 0 _._ 06), and there are several practical approaches being pursuedto increase this to _C ∼_ 1 using Bi donors and superconducting microresonator cavities by increasing the spin-cavity coupling _g_ 0 and the number of resonant spins (see Ref [46]). Although the memory lifetime in this demonstration using a natural-silicon host was only 2 ms, rare-earth spins coupled to similar resonators have been shown to have coherence times of tens of milliseconds [47] while coherence times over 300 ms have been shown for near-surface Bi donors in isotopically enriched<sup>28</sup> Si [5]. 

The chirped pulse protocol introduced here could also be applied to provide random read/write access in optical QMs. Chirped microwave pulses could be applied to directly drive transitions in spin-active optical QMs, such as Nd in YVO4 [31], providing DD and controlling access to a register of stored optical excitations. Furthermore, adiabatic fast passages (achieved using acoustooptic and electro-optic modulators) have been used to optimally invert optical transitions in demonstrations of 

optical QMs [28]. Similarly chirped optical pulses of varying parameters could allow for a random access protocol to be directly implemented in the optical domain, talking advantage of the stronger atom-cavity coupling and larger cavity bandwidth. 

#### **ACKNOWLEDGEMENTS** 

We thank Philippe Goldner for insightful discussions relating to the implementation of this protocol in the optical domain. We thank the UK National Ion Beam Centre (UKNIBC) where the silicon samples were ion implanted and Nianhua Peng who performed the ion implantation. This work has received funding from the U.K. Engineering and Physical Sciences Research Council (EPSRC), through UCLQ postdoctoral fellowships (O.W.K, M.S.) Grant No. EP/P510270/1 and a Doctoral Training Grant (J.O’S.). J.J.L.M. acknowledges funding from the European Research Council under the European Union’s Horizon 2020 research and innovation programme (Grant agreement No. 771493 (LOQOMOTIONS). 

#### **AUTHOR CONTRIBUTIONS** 

J.O’S and O.W.K. performed the experiments with assistance from C.W.Z.. J.O’S, O.W.K. and J.J.L.M. analysed the data with input from J.A. and M.S.. J.A. and J.J.L.M designed the random access protocol with input from O.W.K. and J.O’S. K.D. and K.M. performed numerical analyses and the analytical treatment. C.T. and S.W. fabricated the device. A.H. and I.S. assembled, tested, and provided scientific support in the operation of the JPA. J.O’S, O.W.K. and J.J.L.M. wrote the manuscript with input from all authors. 

#### **DATA AVAILABILITY** 

The datasets generated and analysed during the current study are available in the UCL Research Data repository, doi.org/10.5522/04/14541747. 

- _∗_ These authors have contributed equally to this work _†_ jjl.morton@ucl.ac.uk 

- [1] H. J. Kimble, The quantum internet, Nature **453** , 1023 (2008). 

- [2] M. Mariantoni, H. Wang, T. Yamamoto, M. Neeley, R. C. Bialczak, Y. Chen, M. Lenander, E. Lucero, A. D. O’Connell, D. Sank, _et al._ , Implementing the quantum von neumann architecture with superconducting circuits, Science **334** , 61 (2011). 

7 

- [3] N. Jiang, Y.-F. Pu, W. Chang, C. Li, S. Zhang, and L.M. Duan, Experimental realization of 105-qubit random access quantum memory, npj Quantum Information **5** , 1 (2019). 

- [4] G. Wolfowicz, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. Thewalt, S. A. Lyon, and J. J. Morton, Atomic clock transitions in silicon-based spin qubits, Nature Nanotechnology **8** , 561 (2013). 

- [5] V. Ranjan, J. O’Sullivan, E. Albertinale, B. Albanese, T. Chaneli`ere, T. Schenkel, D. Vion, D. Esteve, E. Flurin, J. Morton, and P. Bertet, Multimode storage of quantum microwave fields in electron spins over 100 ms, Physical Review Letters **125** , 210505 (2020). 

- [6] M. Steger, K. Saeedi, M. Thewalt, J. Morton, H. Riemann, N. Abrosimov, P. Becker, and H.-J. Pohl, Quantum information storage for over 180 s using donor spins in a 28Si “semiconductor vacuum”, Science **336** , 1280 (2012). 

- [7] A. Ortu, A. Tiranov, S. Welinski, F. Fr¨owis, N. Gisin, A. Ferrier, P. Goldner, and M. Afzelius, Simultaneous coherence enhancement of optical and microwave transitions in solid-state electronic spins, Nature Materials **17** , 671 (2018). 

- [8] N. Bar-Gill, L. M. Pham, A. Jarmola, D. Budker, and R. L. Walsworth, Solid-state electronic spin coherence time approaching one second, Nature Communications **4** , 1 (2013). 

- [9] D. D. Sukachev, A. Sipahigil, C. T. Nguyen, M. K. Bhaskar, R. E. Evans, F. Jelezko, and M. D. Lukin, Silicon-vacancy spin qubit in diamond: a quantum memory exceeding 10 ms with single-shot state readout, Physical Review Letters **119** , 223602 (2017). 

- [10] B. Naydenov, F. Dolde, L. T. Hall, C. Shin, H. Fedder, L. C. Hollenberg, F. Jelezko, and J. Wrachtrup, Dynamical decoupling of a single-electron spin at room temperature, Physical Review B **83** , 081201 (2011). 

- [11] H. Y. Carr and E. M. Purcell, Effects of diffusion on free precession in nuclear magnetic resonance experiments, Physical Review **94** , 630 (1954). 

- [12] S. Meiboom and D. Gill, Modified spin-echo method for measuring nuclear relaxation times, Review of Scientific Instruments **29** , 688 (1958). 

- [13] J. J. Morton, A. M. Tyryshkin, R. M. Brown, S. Shankar, B. W. Lovett, A. Ardavan, T. Schenkel, E. E. Haller, J. W. Ager, and S. Lyon, Solid-state quantum memory using the 31 P nuclear spin, Nature **455** , 1085 (2008). 

- [14] Y. Kubo, F. Ong, P. Bertet, D. Vion, V. Jacques, D. Zheng, A. Dr´eau, J.-F. Roch, A. Auff`eves, F. Jelezko, _et al._ , Strong coupling of a spin ensemble to a superconducting resonator, Physical Review Letters **105** , 140502 (2010). 

- [15] S. Weichselbaumer, M. Zens, C. W. Zollitsch, M. S. Brandt, S. Rotter, R. Gross, and H. Huebl, Echo trains in pulsed electron spin resonance of a strongly coupled spin ensemble, Physical Review Letters **125** , 137701 (2020). 

- [16] S. Probst, H. Rotzinger, S. W¨unsch, P. Jung, M. Jerger, M. Siegel, A. Ustinov, and P. Bushev, Anisotropic rareearth spin ensemble strongly coupled to a superconducting resonator, Physical Review Letters **110** , 157001 (2013). 

- [17] D. Schuster, A. Sears, E. Ginossar, L. DiCarlo, L. Frunzio, J. Morton, H. Wu, G. Briggs, B. Buckley, D. Awschalom, _et al._ , High-cooperativity coupling 

   - of electron-spin ensembles to superconducting cavities, Physical Review Letters **105** , 140501 (2010). 

- [18] T. Zhong, J. M. Kindem, J. Rochman, and A. Faraon, Interfacing broadband photonic qubits to on-chip cavityprotected rare-earth ensembles, Nature Communications **8** , 1 (2017). 

- [19] M. Afzelius, N. Sangouard, G. Johansson, M. Staudt, and C. Wilson, Proposal for a coherent quantum memory for propagating microwave photons, New Journal of Physics **15** , 065008 (2013). 

- [20] B. Julsgaard, C. Grezes, P. Bertet, and K. Mølmer, Quantum memory for microwave photons in an inhomogeneously broadened spin ensemble, Physical Review Letters **110** , 250503 (2013). 

- [21] E. L. Hahn, Spin echoes, Physical Review **80** , 580 (1950). 

- [22] S. Probst, H. Rotzinger, A. Ustinov, and P. Bushev, Microwave multimode memory with an erbium spin ensemble, Physical Review B **92** , 014421 (2015). 

- [23] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, H. Abe, S. Onoda, T. Ohshima, _et al._ , Multimode storage and retrieval of microwave fields in a spin ensemble, Physical Review X **4** , 021049 (2014). 

- [24] M. Lovri´c, D. Suter, A. Ferrier, and P. Goldner, Faithful solid state optical memory with dynamically decoupled spin wave storage, Physical Review Letters **111** , 020503 (2013). 

- [25] A. I. Lvovsky, B. C. Sanders, and W. Tittel, Optical quantum memory, Nature Photonics **3** , 706 (2009). 

- [26] A. Anderson, R. Garwin, E. Hahn, J. Horton, G. Tucker, and R. Walker, Spin echo serial storage memory, Journal of Applied Physics **26** , 1324 (1955). 

- [27] J. Ruggiero, J.-L. Le Gou¨et, C. Simon, and T. Chaneli`ere, Why the two-pulse photon echo is not a good quantum memory protocol, Physical Review A **79** , 053851 (2009). 

- [28] V. Damon, M. Bonarota, A. Louchet-Chauvet, T. Chaneliere, and J.-L. Le Gou¨et, Revival of silenced echo and quantum memory for light, New Journal of Physics **13** , 093031 (2011). 

- [29] Y. Kubo, C. Grezes, A. Dewes, T. Umeda, J. Isoya, H. Sumiya, N. Morishita, H. Abe, S. Onoda, T. Ohshima, _et al._ , Hybrid quantum circuit with a superconducting qubit coupled to a spin ensemble, Physical Review Letters **107** , 220501 (2011). 

- [30] B. Kraus, W. Tittel, N. Gisin, M. Nilsson, S. Kr¨oll, and J. I. Cirac, Quantum memory for nonstationary light fields based on controlled reversible inhomogeneous broadening, Physical Review A **73** , 020302 (2006). 

- [31] T. Zhong, J. M. Kindem, J. G. Bartholomew, J. Rochman, I. Craiciu, E. Miyazono, M. Bettinelli, E. Cavalli, V. Verma, S. W. Nam, _et al._ , Nanophotonic rare-earth quantum memory with optically controlled retrieval, Science **357** , 1392 (2017). 

- [32] H. Wu, R. E. George, J. H. Wesenberg, K. Mølmer, D. I. Schuster, R. J. Schoelkopf, K. M. Itoh, A. Ardavan, J. J. Morton, and G. A. D. Briggs, Storage of multiple coherent microwave excitations in an electron spin ensemble, Physical Review Letters **105** , 140503 (2010). 

- [33] J. Baum, R. Tycko, and A. Pines, Broadband and adiabatic inversion of a two-level system by phase-modulated pulses, Phys. Rev. A **32** , 3435 (1985). 

- [34] E. Kupce and R. Freeman, Adiabatic Pulses for Wideband Inversion and Broadband Decoupling, Journal of Magnetic Resonance **115** , 273 (1995). 

8 

- [35] Eriks<sup>¯</sup> Kupce and R. Freeman, Stretched adiabatic pulses for broadband spin inversion, Journal of Magnetic Resonance, Series A **117** , 246 (1995). 

- [36] M. Garwood and L. DelaBarre, The return of the frequency sweep: Designing adiabatic pulses for contemporary nmr, Journal of Magnetic Resonance **153** , 155 (2001). 

- [37] L. A. O’Dell, The WURST kind of pulses in solid-state NMR, Solid State Nuclear Magnetic Resonance **55** , 28 (2013). 

- [38] V. Malinovsky and J. Krause, General theory of population transfer by adiabatic rapid passage with intense, chirped laser pulses, The European Physical Journal D- Atomic, Molecular, Optical and Plasma Physics **14** , 147 (2001). 

- [39] Y. A. Tesiram, Implementation equations for hsn rf pulses, Journal of Magnetic Resonance **204** , 333 (2010). 

- [40] A. J. Sigillito, H. Malissa, A. M. Tyryshkin, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. Thewalt, K. M. Itoh, J. J. Morton, _et al._ , Fast, low-power manipulation of spin ensembles in superconducting microresonators, Applied Physics Letters **104** , 222407 (2014). 

- [41] K. Gerasimov, M. Minnegaliev, S. Moiseev, R. Urmancheev, T. Chaneli`ere, and A. Louchet-Chauvet, Quantum memory in an orthogonal geometry of silenced echo retrieval, Optics and Spectroscopy **123** , 211 (2017). 

      - photons in two-level atoms, Laser Physics **24** , 094003 (2014). 

   - [43] E. Abe, H. Wu, A. Ardavan, and J. J. Morton, Electron spin ensemble strongly coupled to a three-dimensional microwave cavity, Applied Physics Letters **98** , 251108 (2011). 

   - [44] L. Viola, E. Knill, and S. Lloyd, Dynamical decoupling of open quantum systems, Physical Review Letters **82** , 2417 (1999). 

   - [45] A. Doll, S. Pribitzer, R. Tschaggelar, and G. Jeschke, Adiabatic and fast passage ultra-wideband inversion in pulsed EPR, Journal of Magnetic Resonance **230** , 27 (2013). 

   - [46] J. O’Sullivan, O. W. Kennedy, C. W. Zollitsch, M. Sim˙enas,<sup>ˇ</sup> C. N. Thomas, L. V. Abdurakhimov, S. Withington, and J. J. Morton, Spin-resonance linewidths of bismuth donors in silicon coupled to planar microresonators, Physical Review Applied **14** , 064050 (2020). 

   - [47] M. L. Dantec, M. Ranˇci´c, S. Lin, E. Billaud, V. Ranjan, D. Flanigan, S. Bertaina, T. Chaneli`ere, P. Goldner, A. Erb, R. B. Liu, D. Est`eve, D. Vion, E. Flurin, and P. Bertet, Twenty-three millisecond electron spin coherence of erbium ions in a natural-abundance crystal, arXiv 10.48550/ARXIV.2106.14974 (2021). 

- [42] M. Bonarota, J. Dajczgewand, A. Louchet-Chauvet, J.L. Le Gou¨et, and T. Chaneli`ere, Photon echo with a few 

# **Supplementary Information for Random-access quantum memory using chirped pulse phase encoding** 

James O’Sullivan,<sup>1,</sup><sup>_∗_</sup> Oscar W. Kennedy,<sup>1,</sup><sup>_∗_</sup> Kamanasish Debnath,<sup>2</sup> Joseph Alexander,<sup>1</sup> Christoph W. Zollitsch,<sup>1</sup> Mantas Sim˙enas,<sup>ˇ1</sup> Akel Hashim,<sup>3</sup> Christopher N. Thomas,<sup>4</sup> 

Stafford Withington,<sup>4</sup> Irfan Siddiqi,<sup>3</sup> Klaus Mølmer,<sup>2</sup> and John J. L. Morton<sup>1, 5</sup> 

> 1 _London Centre for Nanotechnology, UCL,_ 

_17-19 Gordon Street, London, WC1H 0AH, UK_ 

> 2 _Department of Physics and Astronomy,_ 

_Aarhus University, DK-8000 Aarhus C, Denmark_ 

> 3 _Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA_ 

> 4 _Cavendish Laboratory, University of Cambridge,_ 

_JJ Thomson Ave, Cambridge CB3 0HE, UK_ 

> 5 _Department of Electrical and Electronic Engineering,_ 

_UCL, Malet Place, London, WC1E 7JE, UK_ 

> _∗_ These authors have contributed equally to this work 

1 

### **I. METHODS** 

### **A. Device fabrication** 

A float-zone silicon wafer of natural isotopic abundance is ion implanted with bismuth at a chain of energies targeting a density of 10<sup>17</sup> cm<sup>_−_3</sup> bismuth in the top 1 µm of the sample. This is annealed at 900<sup>_◦_</sup> C for 5 minutes to incorporate the bismuth into the silicon matrix forming spin-active donors. A planar niobium microresonator is patterned on the top of the sample by liftoff. The Nb film is 100 nm thick and has a field dependent frequency (see Ref. [ **?** ]) of 7.093 GHz at a magnetic field of 46 mT. The resonator is a lumped element design comprising a pair of parallel capacitive plates and a narrow doubled-back inductor wire, designed to enhance the magnetic field generated by the resonator close to the substrate surface. The sample is placed inside a copper cavity, as shown in Fig. S1(d). Two antennae extend into the box; one short stub antenna (high insertion loss ≳ 30 dB, low coupling) is connected to a 30 dB attenuated microwave in-line and used to apply microwave excitations. Another long antenna (large coupling) is used to collect microwave signals and is connected to the amplification chain. The asymmetry results in a large collection efficiency of spin-echo signals. 

A schematic of the device is shown in Fig. S1(a), the simulated bismuth implantation profile in Fig. S1(b), the simulated microwave magnetic fields caused by the zero point fluctuations in the resonator in Fig. S1(c) and a schematic of the 3D cavity in Fig. S1(d). 

### **B. Microwave measurement** 

The measurement setup is shown in Fig. S2. The copper sample box is mounted at the base plate of a dilution refrigerator at 100 mK. The output signal is routed through two circulators to a Josephson parametric amplifier (JPA), a quantum limited amplifier, which amplifies the signal in reflection. The amplifier is driven via a directional coupler by a dedicated microwave source. Calibration of the JPA is given in the next section. The signal was further amplifed at 4 K by a high electron mobility transistor (HEMT) and again at room temperature before being mixed down in frequency by an IQ mixer and detected using a digitiser. 

Pulsed microwave signals are generated by an arbitrary waveform generator (AWG), 

2 





<!-- Start of picture text -->
Ho ><br><!-- End of picture text -->







<!-- Start of picture text -->
i } t<br>MV Eh<br><!-- End of picture text -->



<!-- Start of picture text -->
MW G<br>0  0  0  50 K<br>dB dB dB<br>0  4 K<br>10 dB Pulse gate 20  10  dB<br>dB dB<br>frequency  IQ mixer  +40 dB<br>doubler<br>I<br>x2 L Q R dB0  dB10  dB0  800mK<br>LO/2 0  10  0  100 mK<br>dB dB dB<br>I<br>V SG AWG Digitize r<br>Q 10  20  0  1 0 0 mK<br>dB dB dB<br>NbTi<br>Stainless Steel<br>Cu  Ni<br>Cu<br>JPA<br>Other<br>Sample  box<br><!-- End of picture text -->

Figure S2. Schematic of the spectrometer and dilution fridge setup. Microwave pulse signals are generated using a vector signal generator (VSG) and an arbitrary waveform generator (AWG). A microwave generator (MWG) is used to drive the Josephson parametric amplifier (JPA). The return signals are down-converted and detected with a digitizer. A signal at half the up-conversion local oscillator (LO) frequency provided by the VSG is doubled with a frequency doubler and used for down-conversion. Coaxial cable types inside the fridge have been colour coded. 

### **C. System Calibration** 

We measure _T_ 1, _T_ 2 and the Rabi frequency of the hybrid system and show these measurements in Fig. I C. _T_ 1 is measured by inversion recovery where the WURST pulse inverts the spin ensemble and we measure the time taken for the inverted ensemble to return to the ground state and find _T_ 1 _∼_ 14 s. _T_ 2 is measured using two WURST pulses to refocus a weak excitation (same strength as in Fig. 2). Varying _τ_ allows us to measure the effect of dephasing on the echo amplitude. We fit a single quadrature of the echo decay returning a coherence time of 0.7(2) ms where most of the uncertainty arises due to different values returned fitting a stretched or single exponential to the data. 

To measure the Rabi frequency, Ω, we appply a _θ_ rotation pulse followed 10 ms later by 

4 



<!-- Start of picture text -->
(a) (b)<br>420<br>10<br>400<br>0<br>380<br>10<br>360<br>20<br>46 48 46 48<br>Field (mT) Field (mT)<br>(c)<br>50<br>60 Q =18400<br>f 0=7.09395 GHz<br>B =46 mT<br>70<br>80<br>90<br>100<br>7.080 7.085 7.090 7.095 7.100 7.105 7.110<br>Frequency (GHz)<br>(kHz)<br>Frequency Shift (kHz)<br>(dB)<br>21<br>S<br><!-- End of picture text -->

Figure S3. Effect of spins on (a) resonator frequency and (b) resonator linewidth _κ_ as a function of magnetic field as the spin line passes through the resonator. Data are fit simultaneously to equations in Ref. [ **?** ] _g_ ens _∼_ 120 kHz and _γ ∼_ 2 _._ 4 MHz. (c) Measurement of transmission magnitude through the copper cavity using a VNA at 46mT (off resonance with spin line). The superconducting resonator gives a characteristic Fano resonance response which we fit to extract a centre frequency for this resonator of 7.09395 GHz and a Q factor of 18400. 

5 



<!-- Start of picture text -->
(a) (b)<br>12 T 2 = 565±62 s<br>100<br>10<br>50<br>8<br>0 6<br>4<br>50<br>2<br>T 2 = 834±56 s<br>100 T 1 = 14.7±0.7 s<br>0<br>10 0 10 2 0 500 1000 1500<br>Wait (s) Echo Time ( s)<br>(c)<br>Echo (mV)<br>Echo Amp (mV)<br><!-- End of picture text -->

Figure S4. (a) _T_ 1 by inversion recovery. A WURST pulse is used to invert the ensemble before a wait (indicated on the x axis) and a detection sequence at constant high power and _τ_ . (b) _T_ 2 measurement of the sample at the same weak excitation strength as used in Fig. 2 main text. The pulse sequence (inset) is a weak excitation followed by two 100 µs WURST pulses. Increasing _τ_ changes the echo time allowing _T_ 2 to be measured. Fitting stretched or single exponentials gives different _T_ 2 giving a combined uncertainty of _T_ 2 = 0 _._ 7(2) ms (c) Rabi oscillations using a Gaussian _θ_ -pulse of duration 8 µs and FWHM 4 µs and a two-WURST silenced echo detection sequence. The oscillations are heavily damped due to a large inhomogeneity in Rabi frequency across the ensemble. 

6 

a detection sequence with VSG output power of -20 dBm sent through the high gain path. The _θ_ -pulse is chosen to match the duration and shape of the excitations used in the memory sequence in Fig. 3. The heavily damped envelope to sinusoidal Rabi oscillations (shown in Fig. S4) is due to a large inhomogeneity in single spin coupling, _g_ 0, across the ensemble and introduces substantial ( _∼_ 50%) uncertainty to this measurement. We fit a decaying cosine function to the echo amplitude, allowing us to extract an approximate _π_ pulse amplitude of 0.435 (where 1 is the maximum pulse amplitude at the chosen VSG output power) giving Ω= 125 kHz. 

Using _T_ 1 and Ωwe calibrate the photon number in the resonator. The Purcell effect limits 1 _/T_ 1 = 4 _g_ 0<sup>2</sup><sup>_/κ_, allowing a measure of average spin-resonator coupling</sup><sup>_g_0.The different</sup> _κ_ dependence from Ref. [ **?** ] is due to the definition of _κ_ being the HWHM in this work and FWHM in Ref. [ **?** ]. At the centre of the line _κ ∼_ 400 kHz, _T_ 1 = 14 _._ 7 s giving _g_ 0 _∼_ 80 Hz ( _g_ 0 varies across the ensemble and this number is indicative). The Rabi frequency can be written as Ω= 2 _g_ 0 _√n_ which allows us to calibrate the photon number _n ∼_ 5 _._ 7 _×_ 10<sup>5</sup> for the _π_ pulse above. We can rescale this to the photon number to the memory sequence in Fig. 3 (main text) based on an amplitude of 0.2 at a power _∼_ 20 dB lower than the Rabi measurement and find _⟨n⟩∼_ 1200 photons for the memory protocol. Due to the uncertainty in Rabi measurements these photon numbers should be treated as indicative powers accurate to approximately 50%. 

We note that in Fig. 2(d) main text, that repeated WURST pulses before a pulse sequence can cause a reduction in echo amplitude which implies that WURST pulses cause some saturation of the ensemble. However, comparing the _T_ 2 decay shown here and the _TM_ (Fig. 2(e) main text) acquired when using repeated WURST pulses, we see that repeated WURST pulses actually increase the final echo amplitude due to dynamical decoupling. These two observations appear initially at odds. However, we understand this discrepancy using a toy model where we divide spins into three zones, (i) weakly coupled spins, far from the resonator and unaffected by WURST pulses, (ii) spins a moderate distance from the resonator, in turn moderately coupled and undergo imperfect inversion under WURST pulses (iii) spins close and strongly coupled to the resonator which are inverted by WURST pulses with high fidelity. Repeated WURST pulses will saturate zone (ii) which would contribute some of the echo strength. When operating this memory with a long string of WURST pulses, zone (ii) would always remain saturated, and therefore not contribute to 

7 

the protocol. This means that in future devices, sufficient cooperativity for high fidelity memory transfer must be achieved with only spins in zone (iii). 

The use of a JPA in measurements was essential to perform experiments at low photon numbers. Such amplifiers are prone to saturation and nonlinearity with large input signals. We calibrate the JPA to determine the onset and extent of the nonlinear regime, and any additional distortions that may be present. For comparison, the same measurements were repeated with the JPA turned off, using only a HEMT at 4 K for amplification. We confirm that for Fig. 3 (main text)the echo signals are well into the linear regime but the input excitations are in the nonlinear regime of the JPA and are prone to distortion. The HEMT remains linear and un-distorted at all powers, as expected. JPA calibrations are shown in Fig. S5. The inhomogeneous linewidth of the ensemble is _∼_ 2.5 MHz (see Ref. [ **?** ] for further details). 

To further increase signal we chose an operating temperature to maximise the population _∼_ of the ground state of our chosen bismuth transition ( 10 %). Pulsed experiments are run at long a shot-repetition rate of 160 s to minimise the saturation of spins. These considerations are to improve the cooperativity between the spin ensemble and resonator which contributes to the read/write efficiency of the memory and thus improve signal - approximately 17 % one way efficiency as shown in the main text. This means that when measuring _∼_ 200 photon input pulses, the output pulse is actually 0 _._ 17<sup>2</sup> _×_ 200 _∼_ 6 photon output pulses - without considering any _T_ 2 decay. Despite our optimized antenna configuration, we may fail to capture all of this output pulse, and also find that the JPA is working slightly sub-optimally (given the elevated temperature). The combination of these effects means that to observe a low-noise echo at low powers we typically required hundreds of averages. Recent work using single microwave photon detectors [ **?** ] is a promising route to improve sensitivity. In tandem it is necessary to consider routes to improve memory efficiency in order to achieve useful memories. Promising approaches to this include the use of nuclear-spin 1/2 species (allowing the ensemble to be 100 % thermally polarised at mK), optimal resonator design, increasing filling factor whilst maintaining large single-spin coupling necessary for WURST inversion pulses and the use of<sup>28</sup> Si substrates which would improve coherence times and also narrow inhomogeneous spin linewidths. 

8 



<!-- Start of picture text -->
(a)<br><!-- End of picture text -->



<!-- Start of picture text -->
(b)<br><!-- End of picture text -->

Figure S5. (a) Measured pulse amplitude as a function of input pulse amplitude, measured using the JPA (blue) and the HEMT without JPA (orange). (b) Low power regime of the same experiment. 

### **D. Cooperativity** 

Cooperativity in a hybrid micro-resonator spin system can be measured by the dispersive shift to the resonator frequency ( _f_ ), and the increased half-width half max of the resonator frequency response ( _κ_ ) [ **?** ]: 



9 



where _κ_ 0 and _f_ 0 are respectively the half width and frequency of the resonator in the absence of spins, and the detuning ∆= ( _B_ 0 _−BR_ ) _×∂f/∂B_ 0, where _BR_ is the magnetic field at which spins and resonator are resonant. Fitting equations 2 and 3 to our data gives _C ∼_ 0 _._ 067 as shown in Fig. S3. 

We also extract the cooperativity from _T_ 2 measurements with CPMG sequences in Fig. 2 (main text) by modelling the echo intensity as a function of echo number and considering the reduction of energy in the echo field with repeated emission. In A[BB] _n_ A sequences the echo is emitted after the final A pulse. As (i) WURST pulses efficiently refocus spins and (ii) only one echo forms, we attribute any change in echo intensity to dephasing of the spins. We fit the echo intensity _A_ sil( _t_ ) to extract the dephasing time _T_ 2 using 



where _A_ 0 is the echo amplitude at time _t_ = 0, _T_ 2 is the dephasing time and _K_ is the background giving a dephasing time of _T_ 2 = 2 _._ 0 _±_ 0 _._ 2 ms for a refocusing rate of 7.1 kHz. We model the echo amplitude in A[AA] _n_ A sequences by assuming that every time an echo forms, a constant fraction of the energy stored in the echo field is lost and that in between echo emission the echo field dephases as in A[BB] _n_ A sequences. We model the echo amplitude by 



where _η_ em is the efficiency with which energy is emitted from the echo field to the cavity, _N_ is the number of echoes which have occurred before time _t_ . This is fit with one free parameter, _η_ em, and is shown shown in Fig. 2. 

Using Equation (17) from Ref. [ **?** ] we relate the one-way efficiency to the cooperativity by 



giving _C_ = 0 _._ 047 in close agreement to the value extracted in the more typical method by measuring effects on the resonator. 

10 

### **E. WURST Pulses** 

WURST pulses are a type of adiabatic fast passage which have been used to control spin ensembles [ **?** ]. They have advantages in the context of semi-classical control as, in the adiabatic limit, they impart faithful _π_ pulses across a wide bandwidth of spins irrespective of the coupling between the spin and the drive field which may be inhomogeneous across the ensemble. By chirping the frequency of the control pulse, the effective magnetic field observed from the rotating frame of the un-driven spin flips from pointing along one pole of the Bloch sphere to pointing along the other pole following a path along the surface of the Bloch sphere. In this reference frame the spin precesses around this effective magnetic field, and if that precession rate is sufficiently high relative to the rate of the field reversal (i.e. the pulse is sufficiently strong relative to the chirp rate) then the spin will adiabatically track this magnetic field and undergo a _π_ inversion pulse. This is described well in section 2.2 of Ref. [ **?** ]. In this work we use WURST pulses of order 20. 

### _1. Input Output Theory_ 

Wideband uniform rate smooth truncation (WURST) pulses can be characterized by frequency and amplitude modulation (FM and AM respectively) 



where ΓW is the bandwidth of the WURST pulse, _T_ W is the WURST pulse duration and _N_ is the WURST pulse index, in this work we use _N_ = 20 pulses. 

The FM results in a time varying phase of the output pulse 



where _φ_ 0 is the phase of the WURST pulse. The I and Q pulse quadratures applied by the AWG are 



11 



<!-- Start of picture text -->
(a) 1<br>0<br>1<br>0 20 40 60 80 100<br>Time (us)<br>(b)<br>I<br>Q<br>0 20 40 60 80 100<br>Time (us)<br>(c)<br>X<br>Y<br>0 20 40 60 80 100<br>Time (us)<br>Amplitude<br>Frequency (MHz)<br>Pulse Out<br>In Resonator<br><!-- End of picture text -->

Figure S6. WURST-20 pulses with (a) the pulse amplitude and frequency shift for a WURST pulse with bandwidth 2 MHz and duration 100 µs. (b) The I and Q quadratures of the same WURST pulse. (c) The X and Y field quadratures in the cavity once the WURST pulse is filtered by a _κ_ =200 kHz cavity. 

The WURST pulse is modulated by the cavity described by input/output theory [ **? ?** ] where 



where _κC_ is the coupling linewidth of the cavity and _κ_ is the loaded linewidth of the cavity. Increasing the bandwidth of the WURST pulse above the bandwidth of the cavity shortens the effective WURST pulse duration. We show an example WURST pulse in FM/AM (Fig. S6a), consequent IQ quadratures (Fig. S6b) and after modulation by a cavity (Fig. S6c) 

12 

### _2. Limits on WURST Pulses_ 

— In Fig. 4, a region of suitable WURST pulses WURST pulses which inverts a large — fraction of the spin ensemble is mapped out based on both theory and experiment described in this section. Using pulse sequences such as that in Fig. 1(a) (excitation followed by two identical WURST pulses) we have measured the refocusing efficiency. We measure the amplitude of the first (nominally silenced) and second echo and present them as a function of the WURST pulse bandwidth and amplitude in Fig. S7. A ‘good’ WURST pulse results in no echo after the first WURST, and a loud echo after the second. 

By thresholding the lines we determine regions where WURST pulses adiabatically refocus a large fraction of spins. The constraint that the second echo must have a suitable magnitude (85 mV) gives the experimental boundary to suitable WURST pulses shown in Fig. 4 (main text) based on adiabaticity. 

This is supported by a theoretical treatment [ **?** ]. 



where _Q_ min is an adiabaticity factor, _R_ is the chirp rate and _ν_ is the nutation frequency (how quickly the spin precesses around the effective field). _ν_ is minimal (and equal to the Rabi frequency) when the WURST frequency is the same as the spin frequency. We choose a minimum _g_ 0 for spins to be refocused and solve this equation for _Q_ min = 1 finding a lower limit on pulse strength. 

In the homodyne scheme used in this work there is a limit placed by the finite frequency resolution we can imprint onto WURST pulses. The effective duration of the WURST pulse, _T_ W _,_ eff = _κT_ W _/_ ΓW, is the time the WURST pulse of duration _T_ W and total bandwidth ΓW takes to chirp across the cavity frequency _κ_ . The inverse of this time gives an indication of the minimum frequency that can be resolved by modulating the pulse. This frequency must be less than the cavity bandwidth placing a limit on the maximum ΓW which can be used, 



The maximum spectrometer power limits the power of WURSTs we can apply and is shown as the top boundary in Fig. 4. This line cannot be increased to arbitrarily high powers using higher power amplifiers as the superconducting resonators will limit the maximum power. There is also a minimum WURST bandwidth imposed by the cavity bandwidth. 

13 



<!-- Start of picture text -->
60<br>amp = 0.1<br>50<br>amp = 0.2<br>40 amp = 0.3<br>30 amp = 0.5<br>amp = 0.7<br>20 amp = 1.0<br>10<br>0<br>0 10 20 30 40 50 60 70<br>Bandwidth (MHz)<br>100<br>80 amp = 0.1<br>60 100 amp = 0.2<br>amp = 0.3<br>40 amp = 0.5<br>0<br>20 0 1 amp = 0.7<br>BW (MHz) amp = 1.0<br>0<br>0 10 20 30 40 50 60 70<br>Bandwidth (MHz)<br>Echo Magnitude (mV)<br>) V<br>m<br>Mag. (<br>Echo Magnitude (mV)<br><!-- End of picture text -->

Figure S7. Top (bottom) panel – amplitude of the first (second), nominally silenced (unsilenced), echo as a function of the pulse bandwidth for 200us WURST pulses. Inset to the bottom panel is the unsilenced data for low bandwidths, showing that there is a minimum bandwidth, similar to the cavity width, required to maximise the echo amplitude by refocusing all the spins in the cavity. The adiabaticity limit is determined by thresholding the unsilenced echo intensity relative to 85 mV shown as a black dashed line. Non-monotocity of echo intensity and uncertainty in echo amplitude give uncertainty in the thresolded value shown in Fig. 4. 

### _3. WURST pulse distinctiveness_ 

We partition the space of suitable WURSTs into ‘distinct’ WURST pulses to estimate the memory capacity. We partition this region based upon two-WURST echo sequences where the first and second WURST pulse have different properties. Inset to Fig. 4 (main text) is the echo amplitude as the amplitude and chirp rate of the B pulse is varied. This sequence results in strong echoes along a line with positive gradient. In the main text we explain that this line of equivalent pulses is due to the acquisition of a dynamic phase. Together with other two dimensional and one dimensional maps varying a B-pulse parameter we interpolate the gradient and width of the line of equivalent pulses across the space of WURST pulses giving good inversion and use this interpolation to count WURST pulses. This interpolation is shown in Fig. S8 with the results in Fig. 4. 

14 



<!-- Start of picture text -->
(a) (b)<br>0.150<br>1.0 2D<br>0.125 1D<br>0.8<br>0.100<br>0.6<br>0.075<br>0.4<br>0.050<br>0.2 0.025<br>0.0 0.000<br>0 50 0 50<br>R (MHz/ms) R for  A =1 (MHz/ms)<br>(c)<br>0.2<br>0.1 0.25<br>0.20<br>0.0 2.5 5.0 7.5 10.0<br>BW (MHz)<br>0.15<br>0.10<br>0.05<br>0.00<br>0.0<br>10 8 BW (MHz)6 4 2 0 1.0 0.8 0.6 0.4 0.2<br>A (V)<br>Width<br>(Vms/MHz)<br>R<br>WURST amp (V) A/<br>w<br><!-- End of picture text -->

Figure S8. (a) The line of strong echoes from 2D maps of AB-echo sequences. We fit a line to these data and extract their gradient. (b) The gradient of the lines fit in (a) as a function of their extrapolated bandwidth at amplitude _A_ =1 (black circles). The gradient determined when B-pulse has been swept in 1D in both amplitude and bandwidth are inferred and plot on the same axes (grey triangles) showing good agreement. We fit these data with _∂A/∂R_ = _C/R_ with _C_ a fit parameter and return the red dashed line and _C_ = 0 _._ 93. (c) Width of the line of equivalent WURST pulses as a function of WURST pulse parameters. We fit a plane to this data to allow interpolation of the width as a function of bandwidth and amplitude. 

15 

### _4. Theoretical description of WURST pulses_ 

The cavity is driven by a chirped field which results in a temporal intensity profile of the field inside the cavity, and the coupled equations for the spins and the cavity field must in general be solved numerically. Here we shall make some observations for a simplified model, that will qualitatively explain most features seen in the experiments. The spins have a central frequency _ωc_ and each spin is characterized by its detuning _δ_ = _ω − ωc_ . We characterize a WURST pulse by its chirp rate _R_ and pulse centre _t_ 0, yielding its frequency _ω_ ( _t_ ) = _R_ ( _t − t_ 0) and phase _φ_ ( _t_ ) =<sup><u>1</u></sup> 2<sup>_R_(</sup><sup>_t −t_0)2in the frame rotating at</sup><sup>_ωc_.In that frame the</sup> Hamiltonian for each given spin is _δσz/_ 2, and the time dependent complex Rabi frequency is Ω( _t_ ) = Ω0 exp( _−iφ_ ( _t_ )). 

The spin transitions are resonant when _R_ ( _t − t_ 0) = _δ_ , i.e., at the time _tδ ≡ t_ 0 + _δ/R_ . In the interaction picture with respect to the spin excitation energy _δσz/_ 2, the Hamiltonian of a single spin reads, 



where _φ_ ( _t_ ) _− δt_ =<sup><u>1</u></sup> 2<sup>_R_(</sup><sup>_t −tδ_)2 +</sup><sup>_δt_0</sup><sup>_−δ_2</sup><sup>_/_2</sup><sup>_R_.</sup> 

Assuming a near perfect adiabatic chirp, the unitary evolution operator of the full chirp process is given in the _σz_ eigenstate basis: 



where _θδ_ = _φW − δt_ 0. _φW_ contains a term _δ_<sup>2</sup> _/_ 2 _R_ and a term that does not depend on _δ_ but will in general depend on the chirp rate _R_ and on the coupling strength Ω0 (see below). 

For initial spin states with a (small) excitation amplitude of _ϵ_ at _t_ = 0 , the _δ_ -dependence of the mean value of the _σ_<sup>+</sup> operator is _∝ ϵe_<sup>2</sup><sup>_iδt_0</sup> (disregarding the contribution from _φW_ ), and in the Schr¨odinger picture, multiplying by _e_<sup>_−iδt_</sup> we obtain _σ_<sup>+</sup> _∝ ϵe_<sup>_iδ_(2</sup><sup>_t_0</sup><sup>_−t_)</sup> . If it was not for the detuning dependence of _φW_ , these terms would rephase at the time _t_ = 2 _t_ 0 as in the conventional _π−_ pulse echo. Now, instead, the spins may have very different excitation phases and the integral over _δ_ vanishes and the echo is silenced. 

All WURST pulses are described by the same form (14), and the action of two subsequent 

16 

pulses (in the interaction picture) at times _t_ 0 and _t_ 1 is readily found, 



With _a_ = _e_<sup>_−iθδ_</sup> , with parameters _R_ 0 _,_ Ω0 and _b_ = _e_<sup>_−iθδ_</sup> , with parameters _R_ 1 _,_ Ω1, we get _ab_<sup>_∗_</sup> = _e_<sup>_i_(</sup><sup>_φW_0</sup><sup>_−φW_1)+</sup><sup>_iδ_(</sup><sup>_t_1</sup><sup>_−t_0)</sup> and if the pulse parameters are identical, this simplifies to _ab_<sup>_∗_</sup> = _e_<sup>_iδ_(</sup><sup>_t_0</sup><sup>_−t_1)</sup> . Thus, after two identical WURST pulses, a weak spin excitation returns with a global minus sign and a detuning dependent phase factor. In the Schr¨odinger picture, the linear detuning dependence of the phase disappears at _t_ = 2( _t_ 1 _− t_ 0) and we obtain an echo. 

Assuming perfect inversion, a sequence with an even number of WURST pulses yields a final phase which is the sum of all WURST phases _θδ_ with +( _−_ ) signs if they are raising (lowering) pulses, cf., (13). Two pulses with different chirp rates or strengths will not cause an echo due to the nontrivial dependence of the phase difference _φW_ 0 _− φW_ 1. The quadratic variation _δ_<sup>2</sup> (1 _/_ 2 _R_ 0 _−_ 1 _/_ 2 _R_ 1) due to the phase chirp may thus cause destructive interference over the distribution of _δ_ and the dynamical phase associated with the energies of the adiabatic eigenstates during the chirped adiabatic process may cause destructive interference over a range of values for the coupling strength. 

As we observe in the experiments, variation of the chirp rate and strength permit addressing of separate storage modes. The field amplitude Ω0, and the chirp rate _R_ both appear in the dressed state energies and hence in the dynamical phases, and the two control parameters turn out not lead to exploration of a two dimensional space of storage modes . An analytical theory for the phase textures indicated in Fig.1(b) would require solution of the driven two-level dynamics by a chirped frequency field with a time and frequency dependent Rabi frequency Ω0( _t_ ) imposed by the finite bandwidth cavity mode. While this is not possible, we can solve the dynamics numerically and do so to elucidate two effects shown in Fig. **??** and Fig. **??** respectively. 

### **F. High power memory sequences** 

To further confirm the memory protocol functions as intended, we ran identical memory protocols cycling different excitations on and off so that in each run only one excitation was 

17 



<!-- Start of picture text -->
(a) (b)<br>(c) (d)<br>(e)<br><!-- End of picture text -->

Figure S9. The memory sequence shown in Fig.3 was performed at higher input power ( _∼_ 15000 photons per excitation pulse); the raw transient trace of the sequence is shown in (e). In Figs.(a-d) the same experiment was repeated with only one of each of the 4 input excitation pulses, A,B,C and D turned on. This allows us to unambiguously determine which echo originates from which excitation pulse. We see that a single echo appears in the expected read slot in each case. We also see that no other echoes appear when only one excitation is turned on. In this power regime, as well as amplifying (non-linearly), the JPA also imparts poorly characterized phase shifts seen particularly when comparing (c,d,e). 

18 

used. To speed up this measurement we increased the power of the input pulses and the results are shown in Fig. I F where we also show a replication of the full memory protocol at higher power. In each of the sequences where there is only one excitation stored, we only retrieve one echo, and the echo occurs when we would expect the echo to form further confirming that the memory protocol works. 

19 

