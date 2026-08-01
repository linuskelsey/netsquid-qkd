# **Probing an electron spin ensemble with squeezed microwave signals** 

P. Oehrl,<sup>1, 2</sup> F. Fesquet,<sup>1, 2</sup> K. E. Honasoge,<sup>1, 2</sup> M. Handschuh,<sup>1, 2</sup> A. Marx,<sup>1</sup> R. Gross,<sup>1, 2, 3</sup> K. G. Fedorov,<sup>1, 2, 3</sup> and H. Huebl<sup>1, 2, 3,</sup><sup>_∗_</sup> 

> 1 _Walther-Meißner-Institut, Bayerische Akademie der Wissenschaften, 85748 Garching, Germany_ 

> 2 _Technical University of Munich, TUM School of Natural Sciences, Physics Department, 85748 Garching, Germany_ 

> 3 _Munich Center for Quantum Science and Technology (MCQST), 80799 Munich, Germany_ 

(Dated: December 22, 2025) 

The efficient transfer of quantum states into a long-lived storage unit such as solid-state spin ensembles is widely recognized as a critical challenge with significant implications for quantum communication, sensing and computing applications. Here, we experimentally investigate the interaction of propagating squeezed microwaves with an electron spin resonance transition in order to evaluate the use of spin ensembles as quantum memories for GHz signals. We generate continuous variable microwave states with a squeezing of up to 5 dB below the vacuum level and let this signal interrogate a spin ensemble, which is inductively coupled to a lumped element superconducting microwave resonator with a cooperativity of _C_ = 0 _._ 3. Analyzing this signal using Wigner tomography, we observe a transfer efficiency of around 61 % between the squeezed microwaves and the spin excitation. We successfully model our experimental results with a dedicated steady-state model based on the quantum input-output formalism and provide guidance for design parameters required to enable spin-based quantum memories. 

**Introduction.** The realization of secure communication in future quantum networks requires a high-fidelity transfer and storage of quantum states [1–4]. In particular, long-range quantum key distribution and quantum repeater schemes are expected to rely on long-lived quantum memories (QMs) to preserve nonclassical or entangled states and offset inevitable temporal delays in practical networks [5–7]. Another promising application of QMs in communication protocols concerns the idea of quantum tokens, where quantum states are associated with unique identities or credentials, which can be securely verified through communication with a trusted node [8–10]. Security of such schemes relies on fundamental information-theoretic assumptions, which provide access to the concept of unconditional security, in contrast to the computational security provided by modern classical encryption schemes. 

Among various QM platforms [11–13], solid state spin ensembles are considered to be very promising candidates due to their long coherence times and ability to be coupled to both optical and microwave signals. In the last decade, a significant progress towards the implementation of long-lived QMs with spin ensembles has been achieved by demonstrating long coherence times up to several hours [14, 15], the potential for scalability and for integration into networks [16, 17], the ability to store and retrieve coherent states in the limit of single photons [18, 19], and the realization of a random-access QM with classical microwave signals [20]. Nonetheless, the realization of efficient quantum state storage and retrieval at microwave frequencies in the single photon regime remains an open challenge [20–22]. The experimental demonstration of such a microwave QM platform would 

enable further integration with superconducting quantum circuits, one of the leading architectures in quantum information processing. 

Here, we present experimental results based on a modular combination of a Josephson parametric amplifier (JPA) for the generation of squeezed microwave signals and a spin ensemble coupled to a microwave cavity for the QM implementation. We demonstrate the successful generation of propagating microwave squeezed states with squeezing levels up to 5 _._ 3 dB below vacuum. We use these nonclassical photonic states to couple them to the excitations of a spin-resonator hybrid and study the resulting response in the steady-state regime. This allows us to estimate a corresponding transfer efficiency of 61% for the transduction of quantum microwave states into spin excitations. 

**Experimental setup.** A conceptual scheme of our experimental setup is presented in Fig. 1. We generate squeezed vacuum states at microwave frequencies using a reflection-type, flux-driven JPA consisting of a coplanar waveguide resonator coupled to a nonlinear Josephson junction circuit [23–25]. This circuit is realized by a dc-SQUID, which acts as a flux-tunable inductor and, thus, changes the JPA resonance frequency _ω_ SQZ as a function of the applied local magnetic flux. The JPA resonator operates in the overcoupled limit and uses an input circulator which separates the input vacuum state from output squeezed states. In addition, the JPA has an independent microwave port, inductively coupled to the dc-SQUID, which is used to apply a strong parametric pump signal at the frequency 2 _ω_ SQZ. More details about the design, fabrication and performance of the JPA can be found in Ref. [26]. 

The propagating nonclassical squeezed signal is directed via a microwave cryogenic circulator to the spinresonator hybrid device which resembles the quantum 

> _∗_ hans.huebl@wmi.badw.de 

2 



<!-- Start of picture text -->
(a) SQZ spin ensemble<br>B<br>0 Wigner tomography<br>(i) (ii) (iii)<br>(b) (c)<br>10 mm 10 mm<br>g eff γ s<br>κ int κ ext<br>b b<br>in out<br><!-- End of picture text -->



<!-- Start of picture text -->
(c)<br>10 mm<br><!-- End of picture text -->



<!-- Start of picture text -->
(b)<br>10 mm<br><!-- End of picture text -->

Figure 1. **Experimental setup.** (a) By sending a vacuum state to the phase-sensitively operated JPA, squeezer ˆ(SQZ), _b_ in withwea generatefrequencya _ω_ propagatingSQZ, which squeezedis directedvacuumto thesignal,spinresonator system via superconducting coaxial cables and a cryogenic circulator. The transfer of the squeezed signal to the spin excitation is mediated via a superconducting lumpedelement microwave resonator. The output signal from the spin-cavity system,<sup>ˆ</sup> _b_ out, propagates further through a cascade of cryogenic and room temperature amplifiers, is then down-converted and digitized to perform the Wigner tomography of microwave signals. By tuning the static magnetic field _B_ 0, we can distinguish three coupling cases: (i) the SQZ is off-resonant from the spin-resonator hybrid; (ii) the SQZ is in resonance with the resonator, but off-resonant with the spin ensemble; (iii) the SQZ, resonator and spin ensemble are tuned in resonance. (b) Photo of the spin-resonator system. (c) Photo of the JPA device. 

memory element in our setup. After interacting with the spin-resonator system, the reflected signal is amplified by a broadband low-noise cryogenic HEMT amplifier. The amplified output signal is processed further at room temperature by using a heterodyne detection setup with a high-frequency digitizer [27]. We calibrate gain and noise of the amplification chain, including the JPA properties, by making use of the Planck spectroscopy [28, 29]. This calibration procedure allows us to perform the Wigner tomography of our quantum states at various points of the cryogenic setup based on the reference state reconstruction approach [30]. 

The hybrid spin-resonator system is composed of a reflection type planar niobium microwave resonator and the electron spin ensemble, provided by an isotopically enriched<sup>28</sup> Si crystal with a reduced nuclear spin population that is doped with phosphorus donors at a concentration of [P] = 1x10<sup>17</sup> cm<sup>_−_3</sup> [31]. The 18 µm thick<sup>28</sup> Si phosphorus-doped crystal is mounted in a flip-chip configuration onto the lumped element niobium resonator and held in place using a second silicon chip with a 

natural isotope composition acting as a cover. While phosphorus donors in silicon exhibit two electron spin resonance transitions due to the Fermi contact hyperfine interaction [32, 33], we will selectively exploit only the _|↓⇓⟩→|↑⇓⟩_ transition with frequency _ω_ s. Here, we use the notation _|↓⇓⟩_ to denote the energy levels, where the first (second) arrow corresponds to the electron (nuclear) spin. The energy levels are labeled according to their high-field product-state configuration (see also Appendix A). 

By controlling the static magnetic field _B_ 0, provided by a superconducting solenoid magnet, _ω_ s can be tuned into resonance with the frequency of the resonator _ω_ r. Notably, also the microwave resonator shows a weak frequency dependence with the applied in-plane magnetic field, which we attribute to the field dependent kinetic inductance of niobium. The JPA is spatially separated from the spin-resonator hybrid and placed outside the magnet. The additional superconducting magnetic shield guarantees close to quantum-limited performance. This setting allows to control the resonance frequency of the microwave resonator and the spin ensemble by tuning the external magnetic field _B_ 0 independently of the JPA frequency. 

Ultimately, we can distinguish between three different scenarios: (i) a completely off-resonant regime, where the frequencies of the JPA, microwave resonator, and spin ensemble are all different, _ω_ SQZ = _ω_ r = _ω_ s; (ii) a partially resonant regime, where the squeezed signal from the JPA (SQZ) is resonant with the microwave resonator, but the spin ensemble remains detuned, _ω_ SQZ = _ω_ r = _ω_ s; (iii) a fully resonant regime, where all characteristic carrier frequencies of the aforementioned systems coincide, _ω_ SQZ = _ω_ r = _ω_ s. These three distinct configurations allow us to unambiguously characterize all parts of our cryogenic setup and calibrate all important quantities independently, such as the squeezing level of the incoming microwave signals, the microwave response of the resonator, and the spectral characteristics of the spin-resonator hybrid system. 

**Theoretical model.** Here, we briefly describe our approach to model the spin-resonator hybrid system consisting of a driven microwave resonator coupled resonantly to an electron spin ensemble within a steady-state, quantum-mechanical framework. It enables the analysis of the mean field amplitudes as well as the variances of microwave quantum signals. We define the Hamiltonian of the spin-resonator hybrid as 



where we assume weak excitation signals and also neglect the inhomogeneous spin broadening [22, 34–36]. Here, _a_ ˆ (ˆ _s_ ) and _a_ ˆ<sup>_†_</sup> (ˆ _s_<sup>_†_</sup> ) are the bosonic annihilation and creation operators for excitations inside the resonator (spin 

3 

ensemble). The collective coupling between the spin ensemble and the resonator is defined by _g_ eff = _√Ng_ 0, with the number of spins _N_ and the single spin coupling rate _g_ 0. The eigenfrequency of the resonator (spin ensemble) is _ω_ r ( _ω_ s). The spin dephasing is modeled using a collective coupling with rate _γ_ s to a noise bath _f_<sup>ˆ</sup> s. Similarly, we account for internal resonator losses with an associated loss mode<sup>ˆ</sup> _b_ l and a loss rate _κ_ int. The coupling between the intra-cavity mode of the resonator and the external microwave circuit is described via the coupling of the input mode<sup>ˆ</sup> _b_ in with rate _κ_ ext. We assume all coupling rates as half width at half maximum linewidth. 

Using the Heisenberg equation of motion, we derive the following equations for the Fourier amplitudes of the resonator and spin operators 





with _κ_ = _κ_ int + _κ_ ext. Following Ref. [22], we obtain the relation between the input and output signal variances as 



Here, the variance of an operator _O_<sup>ˆ</sup> is defined as _σO_<sup>2</sup> ˆ<sup>=</sup> ˆ _⟨qO_<sup>2</sup> ˆ<sup>_⟩_,with</sup><sup>_q_ˆ</sup> _O_<sup>ˆ=( ˆ</sup><sup>_O_+</sup><sup>_O_ˆ</sup><sup>_†_)</sup><sup>_/_2.Thecomplexcoefficients</sup> _r_ , _l_ , and _t_ describe terms of the Langevin noise operator associated with the reflection from the cavity, the resonator internal losses, and losses of the spin ensemble, respectively. These coefficients are [22] 



with the following definitions 



Here, we define the detuning of the spin and resonator mode as ∆sr = _ω_ s _− ω_ r and the detuning of the resonator mode and the incident microwave signal as ∆r = _ω − ω_ r. The condition _|l_ ( _ω_ ) _|_<sup>2</sup> + _|r_ ( _ω_ ) _|_<sup>2</sup> + _|t_ ( _ω_ ) _|_<sup>2</sup> = 1 ensures that the output mode fulfills the bosonic commutation relation. We note that Eq. 4 with the defined coefficients 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br><!-- End of picture text -->



<!-- Start of picture text -->
+5<br>0<br>-5<br><!-- End of picture text -->



<!-- Start of picture text -->
+5<br>0<br>-5<br><!-- End of picture text -->

Figure 2. **Characterization of the spin-resonator hybrid.** (a) Measured (left) and modeled (right) microwave reflection amplitude _|S_ 11 _|_ as a function of the coherent proberesonator detuning ∆r and spin-resonator detuning ∆sr. The spectrum is modeled based on Eq. 7. (b) Comparison of the measured (dots) and modeled (lines) data for the resonant (∆sr _/_ 2 _π_ = 0) and off-resonant (∆sr _/_ 2 _π_ = 9 _._ 2 MHz) conditions, presented in blue and red, respectively. 

_r, l_ and _t_ is only valid at zero or large spin-resonator detunings [37]. In addition, we compare the expectation value of the input and output fields within the inputoutput formalism and derive the complex scattering parameter [38–40] 



We analyze the output field variance in order to determine the squeezing level _S_ of the corresponding quantum state. To this end, we describe the output microwave signal in terms of its electromagnetic field quadrature ˆ ˆ ˆ ˆ operators, _q_ and _p_ , with<sup>ˆ</sup> _b_ out = _q_ + _ip_ , fulfilling the comˆ mutator relation [ˆ _q, ip_ ] = 1 _/_ 2. As derived in Ref. [30], we can completely define the squeezed and anti-squeezed quadrature variances within this nomenclature. Consequently, the squeezing level can be expressed in decibels as 



where _σ_ sq is the variance of the squeezed quadrature and positive values indicate squeezing below the vacuum level [26]. 

**Characterization of the spin-resonator hybrid.** Next, we perform the continuous wave microwave spectroscopy of the resonator coupled to the electron spin resonance (ESR) transition. In detail, we measure the complex scattering parameter _S_ 11 as a function of frequency using an incident microwave coherent signal with a power of _P_ mw = _−_ 139 dBm, corresponding to an average resonator occupation of 0 _._ 5 photons at _ω_ r [41]. By controlling the applied static magnetic field _B_ 0, we can tune the frequency of the ESR transition to match the resonator resonance frequency, _ω_ s = _ω_ r. For this condition, _S_ 11 also reflects the conversion of coherent microwave photons to spin excitations. 

5 



<!-- Start of picture text -->
=<br>PE \ »<br>a emia ioe WO J IL<br>—-O—- Soff —r es: © F Wy, Wg v2\ ©<br>—-—-Q—- Sresonator: w= Ww #F wy \ “<br>=-0=" Sepins: ®W = Wp = W ©3<br>spins r S<br><!-- End of picture text -->



<!-- Start of picture text -->
\<br><!-- End of picture text -->



<!-- Start of picture text -->
coatou RBS E  BETTIE06  Rg;<br>TO Jresonator \<br>= spins \<br>—-0— Ssaturation ©<br><!-- End of picture text -->

/ 

/ 

5 

the vacuum level. Above a pump power of _−_ 30 dBm, the squeezing level abruptly decreases and, eventually, crosses the threshold value of _S_ = 0 dB. This could originate from the reconstruction model considering moments up to fourth order or from the disappearance of nonclassical correlations in the signal. In the next step, we increase the static magnetic field, such that ∆sr _/_ 2 _π_ = 9 _._ 2 MHz. Then, the frequency of the SQZ and the resonator coincide while the spin mode remains detuned. In this configuration, the pump power dependence of the _S_ is qualitatively similar to the off-resonant reference measurement but shows a reduction in the squeezing level. The measured maximum squeezing level is _S_ r, max = (+1 _._ 47 _±_ 0 _._ 03) dB. This reduction originates from the intrinsic resonator losses, as determined in the cwESR spectroscopy (see Fig. 2(c)). These losses lead to an effective addition of thermal fluctuations from the coupled environmental bath, and consequently lead to an eventual reduction of the squeezing level. Finally, we tune all our subsystems in resonance, _ω_ SQZ = _ω_ r = _ω_ s, and measure the resulting squeezing level. We observe a further reduction of the power-dependent squeezing level as compared to the previous configurations. Here, the measured maximum squeezing level is _S_ spins, max = (+0 _._ 12 _±_ 0 _._ 03) dB. We attribute this additional reduction of the squeezing level to the increased total absorption losses associated with the ESR transition. 

For a quantitative analysis, we compare the presented experimental results with the prediction of the inputoutput model, as given by Eq. 4. Within this model, the variances in the measured output signal are determined by the variances of the reflected incoming squeezed microwave signals and thermal state contributions from the resonator and spin ensemble modes, which are assumed to be weak thermal baths. As an input signal variance _σ_ ˆ _b_ in, we use the value obtained from the reference measurement, where _ω_ SQZ = _ω_ r = _ω_ s. Using the coupling rates obtained from the earlier cwESR measurements, and describing the spin and resonator losses as arising from a thermal bath with the same temperature _T_ = 70 mK, we can use Eq. 4 to estimate the expected squeezing level from the measured output variance. The calculated values are presented as crosses in Fig. 3(a), showing an excellent quantitative agreement with the measured squeezing levels. Furthermore, the parameter _t_ in Eq. 4 can be interpreted as a transfer efficiency between microwave signals and spin excitations, as it describes how strong thermal fluctuations of the spin systems couple to the microwave signal. Based on the fit of our model to the experimental data, we find _|t_ (0) _|_<sup>2</sup> _≃_ 61 %. 

Interestingly, besides detuning the subsystems there is another method to decouple the spin ensemble from the microwave resonator. Conceptually, the application of a strong resonant microwave pulse can saturate the spin transition and decouple the resonator from the spin ensemble. In order to experimentally investigate this regime, we operate in the resonant configuration between all three subsystems and additionally apply a resonant, 

strong, rectangular-shaped, saturation pulse at the carrier frequency of _ω/_ 2 _π_ = 5 _._ 645 GHz for the duration of 20 ms with the power of _−_ 120 dBm before performing the continuous wave measurements with the squeezed states. Within our squeezing measurements, we choose a pulse repetition time of 2 s. The measured squeezing level at the output of the spin-resonator hybrid is shown in Fig. 3(c) with the maximum squeezing level of _S_ spins, sat = (+1 _._ 12 _±_ 0 _._ 03) dB. This value closely reaches the originally measured maximal squeezing level for the case of the SQZ in resonance with the resonator, without the saturation pulse. The clear increase in squeezing level thus confirms that the saturation pulse leads to a decoupling of the spin ensemble and the microwave resonator. Quantitatively, the squeezing levels do not reach the reference values (red line in Fig. 3). We attribute this observation to two aspects: the nonlinear properties of the spin-resonator hybrid and the timescales of the saturation protocol, i.e. the finite _T_ 1 time of the donor spin ensemble which counteracts the spin-resonator decoupling. These nonlinear properties require a more complex description going beyond the simple model provided by Eq. 1. 

**Simulation of the quantum transfer efficiency.** In order to investigate optimal coupling parameters for the spin-resonator hybrid platform, we numerically compute the transfer efficiency using Eq. 4. We study experimentally reachable parameter regimes for realistic internal and external resonator coupling strengths, a spin dephasing rate, and an effective spin-resonator coupling. Figure 4 presents the results of those numerical calculations which provide a foundation for the realization of an optimal quantum state transfer for future experiments. Here, we investigate the resonant case, _ω_ SQZ = _ω_ r = _ω_ s, and thus investigate the transfer efficiency _|t_ (0) _|_<sup>2</sup> as a function of different coupling rates. 

In the first case, we choose the spin dephasing rate to be fixed, _γ_ s = 382 kHz, and vary the external coupling rate of the resonator as well as the effective spinresonator coupling. Panels (a) and (b) in Fig. 4 present the estimated effective transfer strength and cooperativity corresponding to a maximized transfer efficiency, respectively. We observe a parameter regime with an increasing coupling efficiency, approaching unity in the case of _κ_ ext _/_ 2 _π_ = 1 _._ 25 MHz and _g_ eff _/_ 2 _π_ = 976 kHz. For these parameters, the corresponding cooperativity is reaching _C_ max = 0 _._ 982. Next, we fix the spin-resonator coupling, _g_ eff = 460 kHz, and vary the external coupling of the resonator as well as the spin dephasing rate. Panels (c) and (d) in Fig. 4 show the resulting coupling regime and corresponding cooperativity. The coupling efficiency reaches value of 0 _._ 991 for _κ_ ext _/_ 2 _π_ = 1 _._ 25 MHz and _γ_ s _/_ 2 _π_ = 167 kHz, corresponding almost to unit cooperativity. In the third scenario, we keep the spin dephasing rate and effective spin-resonator coupling constant and equal to the determined experimental values, i.e. _γ_ s = 382 kHz and _g_ eff = 460 kHz. Then, we vary the internal and external coupling rates of the resonator, 

# (0)? 



<!-- Start of picture text -->
§ R<br>[9] [9]<br>2 ©<br>3 | J ><br><!-- End of picture text -->



<!-- Start of picture text -->
Le  —<br>~N<br>| ~<br>| =;<br><!-- End of picture text -->



<!-- Start of picture text -->
& kB<br>IN ~N<br>3= - >9<br><!-- End of picture text -->









<!-- Start of picture text -->
\_<br><!-- End of picture text -->



<!-- Start of picture text -->
fe ——<br><!-- End of picture text -->



° 



<!-- Start of picture text -->
[°)<br>)5)<br><<<br><!-- End of picture text -->



T 

8 



<!-- Start of picture text -->
AWG VNA<br>ADC DDC FIR<br>I/Q<br>SGS<br>NI FPGA  Trig IN<br>LO<br>LO **<br>Digi�zer<br>I/Q<br>** SGS SGS<br>* Trig IN Trig IN *<br>ADCMT ADCMT<br>40 K 10 dB 10 dB 10 dB 10 dB<br>4 K 6 dB 20 dB 10 dB HEMT 6 dB<br>700 mK 6 dB 20 dB 20 dB 6 dB<br>100 mK 0 dB 0 dB 0 dB 0 dB<br>70 mK 0 dB 10 dB 20 dB 0 dB<br>30 dB<br>SQZ AMP<br>B<br>0<br><!-- End of picture text -->

Figure 6. **Experimental setup.** Cryogenic and roomtemperature setup for continuous wave and pulsed measurements with coherent microwave signals as well as the generation and detection of squeezed microwave signals. Further details are given in the text. 

we use a DC voltage source (ADCMT 6241A) to apply a flux bias setting the resonance frequency of the JPA and a microwave signal generator (Rohde & Schwarz SGS100A) for the generation of the pump tone. The detection of the output signal is performed in a heterodyne detection setup, including a variety of bandpass filters, roomtemperature amplifiers and the FPGA module (National Instruments FPGA 7972). 

## **Appendix C: Data processing and calibration techniques** 

**Background correction of the cwESR spectrum.** When measuring cwESR spectra, the measured scattering parameter is subject to the complex microwave background based on imperfections in the experimental setup, such as impedance mismatches and signal delays due to finite cable lengths. To correct for those effects, we apply the circle-fit routine and fit the resonator response detuned from the spin mode, ∆sr _/_ 2 _π_ = 9 _._ 2 MHz, using 

the following equation [42]: 



where the complex amplitude _A_ mw = _a_ mwe<sup>_i_(</sup><sup>_α−ωτ_)</sup> captures environmental influences, including amplitude variations, impedance-induced phase shifts, and microwave signal propagation delays. The loaded quality factor _Q_ l is defined as the sum of reciprocal values of the internal and external quality factors ( _Q_ int and _Q_ ext), _Q_<sup>_−_</sup> l<sup>1</sup> = _Q_<sup>_−_</sup> int<sup>1+ Re(</sup><sup>_Q_</sup> ext<sup>_−_1).Theinternalqualityfactorac-</sup> counts for intrinsic losses such as radiative losses, surface resistance, magnetic field-induced dissipation, and spin ensemble interactions. The complex external quality factor _Q_ ext = _|Q_ ext _|_ e<sup>_−iϕ_</sup> quantifies energy dissipation into the external feedline, while the phase _ϕ_ accounts for impedance mismatches and parasitic effects [42]. Applying the circle-fit routine, we find _a_ mw = 0 _._ 021, _α_ = 1 _._ 585, _τ_ = 97 _._ 35 ns, _ω_ r _/_ 2 _π_ = 5 _._ 645 GHz, _ϕ_ = _−_ 0 _._ 002, _Q_ ext = (1900 _±_ 11), and _Q_ l = (1586 _±_ 15). 

Assuming, that the environmental influences are independent on the applied magnetic field for the investigated field range, we correct our measured data as follows 



Furthermore, we use a normalization of the corrected data in order to compare the measured spectrum to the theoretical model. The resulting scattering parameter is defined as 



**Reference state reconstruction.** As described in the main text, we digitize the microwave output signal at room temperature with a heterodyne detection setup using an FPGA module. With the recorded _I/Q_ sampled data points, we compute the quadrature moments up to the fourth order, _⟨I_<sup>_n_</sup> _Q_<sup>_m_</sup> _⟩_ for _n_ + _m ≤_ 4(( _n, m_ ) _∈_ N<sup>2</sup> ), and consequently we compute the corresponding signal moments with respect to a specific reconstruction point in our setup. Thus, we can reconstruct the squeezing angle and squeezing level for the detected output signal [30, 55]. In order to map the detected voltage amplitude of the microwave output signal to a photon number, we rely on Planck spectroscopy [28, 29]. Here, we use a heatable input attenuator that is placed within our microwave circuit before the SQZ. Then, we measure the output voltage dependent on the temperature of the heatable attenuator. Based on a Planck’s distribution fitting routine, we can determine a photon number conversion factor which relates the voltage measured at room temperature to a photon number at the desired reference point in the cryogenic setup. Within our data analysis, we choose the HEMT input as the reconstruction point. To this end, we carefully estimate the microwave losses between the heatable attenuator and the HEMT input to be _−_ 2 _._ 8 dB. 

9 

## **Appendix D: Characterization of the squeezer JPA** 

**Flux-dependent resonance frequency and nondegenerate gain.** Here, we present characterization measurements of the squeezer JPA (SQZ). First of all, we record the dependence of the resonance frequency on the applied magnetic flux. The result is shown in Fig. 7(a). In our experiment, we measure the complex microwave reflection amplitude _|S_ 11 _|_ as a function of the probe frequency and dc current through the superconducting magnetic field coil. We observe a maximum resonance frequency of _ω/_ 2 _π_ = 5 _._ 73 GHz and a tunability range of about 500 MHz. Importantly, we identify two coil currents at which we can tune the SQZ in resonance with our spin-resonator hybrid, fulfilling _ω_ SQZ = _ω_ r = _ω_ s. Furthermore, we measure the dependence of the nondegenerate gain on the applied pump power for a fixed frequency of _ω_ pump _/_ 2 _π_ = 2 _ω_ SQZ _/_ 2 _π_ = 11 _._ 1 GHz. The result is shown in Fig. 7(b). We record a maximum non-degenerate gain of _G_ nd = 36 dB for a fixed power of the coherent pump tone of _−_ 32 _._ 3 dBm. 

**Generation of squeezed microwave signals.** Finally, we characterize the generation of squeezed microwave signals by recoding the dependence of the squeezing level on the applied pump power for a fixed frequency of _ω_ SQZ _/_ 2 _π_ = 5 _._ 645 GHz. The results are shown in Fig. 7(c). We observe a maximum squeezing level of (+5 _._ 29 _±_ 0 _._ 09) dB. Correspondingly, we reconstruct the purity as a function of the applied pump power. The results are shown in and Fig. 7(d). With increasing pump power, the purity steadily decreases due to pump-induced noise, higher-order nonlinearities and gain-dependent environmental noise [25, 56]. We use this power-dependent squeezing measurement as a reference for the coupling of squeezed microwave signals to the spin-resonator hybrid system. 

- [1] N. Gisin and R. Thew, Quantum communication, Nature photonics **1** , 165 (2007). 

- [2] H. J. Kimble, The quantum internet, Nature **453** , 1023 (2008). 

- [3] M. K. Bhaskar, R. Riedinger, B. Machielse, D. S. Levonian, C. T. Nguyen, E. N. Knall, H. Park, D. Englund, M. Lonˇcar, D. D. Sukachev, and M. Lukin, Experimental demonstration of memory-enhanced quantum communication, Nature **580** , 60 (2020). 

- [4] M. Teller, S. Plascencia, C. Sastre Jachimska, S. Grandi, and H. de Riedmatten, A solid-state temporally multiplexed quantum memory array at the single-photon level, npj Quantum Information **11** , 92 (2025). 

- [5] W. Zhang, T. van Leent, K. Redeker, R. Garthoff, R. Schwonnek, F. Fertig, S. Eppelt, W. Rosenfeld, V. Scarani, C. C.-W. Lim, and H. Weinfurter, A deviceindependent quantum key distribution system for distant 



<!-- Start of picture text -->
(norm.)<br>0 0.5 1<br><!-- End of picture text -->



<!-- Start of picture text -->
(dB)<br>0 10 20 30<br>5.56<br>5.55<br>5.54<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br>2<br>0<br>-2<br><!-- End of picture text -->



Figure 7. **Experimental characterization of the squeezer JPA.** (a) Measurement of the microwave reflection amplitude _|S_ 11 _|_ as a function of the probe frequency and dc current through the superconducting magnetic field coil. (b) Measurement of the dependence of the non-degenerate gain on the applied pump power for a fixed frequency of _ω_ pump _/_ 2 _π_ = 11 _._ 1 GHz. (c) Measured squeezing level as a function of the applied pump power for a fixed frequency of _ω_ SQZ _/_ 2 _π_ = 5 _._ 645 GHz showing a maximum squeezing level of (+5 _._ 29 _±_ 0 _._ 09) dB. The gray-dashed line depicts the vacuum limit, above which the reconstructed microwave signals are referred to as squeezed. (d) The corresponding reconstructed purity dependent on the applied pump power. The gray-dashed line illustrates the upper limit at which the purity becomes unity. 

users, Nature **607** , 687 (2022). 

- [6] D. P. Nadlinger, P. Drmota, B. C. Nichol, G. Araneda, D. Main, R. Srinivas, D. M. Lucas, C. J. Ballance, K. Ivanov, E.-Z. Tan, R. Sekatski, R. L. Urbanke, R. Renner, N. Sangouard, and J.-D. Bancal, Experimental quantum key distribution certified by bell’s theorem, Nature **607** , 682 (2022). 

- [7] Y.-F. Pu, S. Zhang, Y.-K. Wu, N. Jiang, W. Chang, C. Li, and L.-M. Duan, Experimental demonstration of memory-enhanced scaling for entanglement connection of quantum repeater segments, Nature Photonics **15** , 374 (2021). 

- [8] S. Wiesner, Conjugate coding, ACM Sigact News **15** , 78 (1983). 

- [9] F. Pastawski, N. Y. Yao, L. Jiang, M. D. Lukin, and J. I. Cirac, Unforgeable noise-tolerant quantum tokens, Proceedings of the National Academy of Sciences **109** , 

10 

16079 (2012). 

- [10] K. Jir´akov´a, K. Bartkiewicz, A. Cernoch,<sup>ˇ</sup> and K. Lemr, Experimentally attacking quantum money schemes based on quantum retrieval games, Scientific Reports **9** , 16318 (2019). 

- [11] H. P. Specht, C. N¨olleke, A. Reiserer, M. Uphoff, E. Figueroa, S. Ritter, and G. Rempe, A single-atom quantum memory, Nature **473** , 190 (2011). 

- [12] J.-S. Tang, Z.-Q. Zhou, Y.-T. Wang, Y.-L. Li, X. Liu, Y.-L. Hua, Y. Zou, S. Wang, D.-Y. He, G. Chen, Y.N. Sun, Y. Yu, M.-F. Li, G.-W. Zha, H.-Q. Ni, Z.-C. Niu, C.-F. Li, and G.-C. Guo, Storage of multiple singlephoton pulses emitted from a quantum dot in a solidstate quantum memory, Nature Communications **6** , 8652 (2015), 1510.05358. 

- [13] A. Wallucks, I. Marinkovi´c, B. Hensen, R. Stockill, and S. Gr¨oblacher, A quantum memory at telecom wavelengths, Nature Physics **16** , 772 (2020). 

- [14] N. Bar-Gill, L. M. Pham, A. Jarmola, D. Budker, and R. L. Walsworth, Solid-state electronic spin coherence time approaching one second, Nat. Commun. **4** , 1743 (2013). 

- [15] M. Zhong, M. P. Hedges, R. L. Ahlefeldt, J. G. Bartholomew, S. E. Beavan, S. M. Wittig, J. J. Longdell, and M. J. Sellars, Optically addressable nuclear spins in a solid with a six-hour coherence time, Nature **517** , 177 (2015). 

- [16] A. Ghirri, C. Bonizzoni, F. Troiani, N. Buccheri, L. Beverina, A. Cassinese, and M. Affronte, Coherently coupling distinct spin ensembles through a high-t c superconducting resonator, Physical Review A **93** , 063855 (2016). 

- [17] A. Strini´c, P. Oehrl, A. Marx, P. A. Bushev, H. Huebl, R. Gross, and N. Kukharchyk, Broadband electron paramagnetic resonance spectroscopy of<sup>167</sup> Er:<sup>7</sup> LiYF4 at millikelvin temperatures, Phys. Rev. B **111** , 214430 (2025). 

- [18] N. Timoney, I. Usmani, P. Jobez, M. Afzelius, and N. Gisin, Single-photon-level optical storage in a solidstate spin-wave memory, Physical Review A—Atomic, Molecular, and Optical Physics **88** , 022324 (2013). 

- [19] C. Grezes, B. Julsgaard, Y. Kubo, W. L. Ma, M. Stern, A. Bienfait, K. Nakamura, J. Isoya, S. Onoda, T. Ohshima, V. Jacques, D. Vion, D. Esteve, R. B. Liu, K. Mølmer, and P. Bertet, Storage and retrieval of microwave fields at the single-photon level in a spin ensemble, Phys. Rev. A **92** , 020301 (2015). 

- [20] J. O’Sullivan, O. W. Kennedy, K. Debnath, J. Alexander, C. W. Zollitsch, M. Sim˙enas,<sup>ˇ</sup> A. Hashim, C. N. Thomas, S. Withington, I. Siddiqi, K. Mølmer, and J. J. L. Morton, Random-access quantum memory using chirped pulse phase encoding, Phys. Rev. X **12** , 041014 (2022). 

- [21] C. Eichler, A. Sigillito, S. A. Lyon, and J. R. Petta, Electron spin resonance at the level of 1 0 4 spins using low impedance superconducting resonators, Physical Review Letters **118** , 037701 (2017). 

- [22] A. Bienfait, P. Campagne-Ibarcq, A. H. Kiilerich, X. Zhou, S. Probst, J. J. Pla, T. Schenkel, D. Vion, D. Esteve, J. J. L. Morton, K. Moelmer, and P. Bertet, Magnetic resonance with squeezed microwaves, Phys. Rev. X **7** , 041011 (2017). 

- [23] L. Zhong, E. P. Menzel, R. Di Candia, P. Eder, M. Ihmig, A. Baust, M. Haeberlein, E. Hoffmann, K. Inomata, T. Yamamoto, Y. Nakamura, E. Solano, F. Deppe, A. Marx, and R. Gross, Squeezing with a flux-driven 

   - josephson parametric amplifier, New Journal of Physics **15** , 125013 (2013). 

- [24] S. Pogorzalek, K. G. Fedorov, L. Zhong, J. Goetz, F. Wulschner, M. Fischer, P. Eder, E. Xie, K. Inomata, T. Yamamoto, Y. Nakamura, A. Marx, F. Deppe, and R. Gross, Hysteretic flux response and nondegenerate gain of flux-driven josephson parametric amplifiers, Phys. Rev. Appl. **8** , 024012 (2017). 

- [25] M. Renger, S. Pogorzalek, Q. Chen, Y. Nojiri, K. Inomata, Y. Nakamura, M. Partanen, A. Marx, R. Gross, F. Deppe, and K. G. Fedorov, Beyond the standard quantum limit for parametric amplification of broadband signals. npj quantum inf. 7, npj Quantum Information **7** , 160 (2021). 

- [26] K. Honasoge, M. Handschuh, W. Yam, S. Gandorfer, D. Bazulin, N. Bruckmoser, L. Koch, A. Marx, R. Gross, and K. Fedorov, Fabrication of low-loss josephson parametric devices, Physical Review B **111** , 214508 (2025). 

- [27] E. Menzel, F. Deppe, M. Mariantoni, M. Araque Caballero, A. Baust, T. Niemczyk, E. Hoffmann, A. Marx, E. Solano, and R. Gross, Dual-path state reconstruction scheme for propagating quantum microwaves and detector noise tomography, Physical Review Letters **105** , 100401 (2010). 

- [28] M. Mariantoni, E. P. Menzel, F. Deppe, M. Araque Caballero, A. Baust, T. Niemczyk, E. Hoffmann, E. Solano, A. Marx, and R. Gross, Planck spectroscopy and quantum noise of microwave beam splitters, Physical review letters **105** , 133601 (2010). 

- [29] S. Gandorfer, M. Renger, W. Yam, F. Fesquet, A. Marx, R. Gross, and K. Fedorov, Two-dimensional Planck spectroscopy for microwave photon calibration, Phys. Rev. Appl. **23** , 024064 (2025). 

- [30] K. G. Fedorov, S. Pogorzalek, U. Las Heras, M. Sanz, P. Yard, P. Eder, M. Fischer, J. Goetz, E. Xie, K. Inomata, N. Y, D. C. R, S. E, M. A, D. F, and G. R, Finitetime quantum entanglement in propagating squeezed microwaves, Scientific reports **8** , 6416 (2018). 

- [31] S. Weichselbaumer, M. Zens, C. W. Zollitsch, M. S. Brandt, S. Rotter, R. Gross, and H. Huebl, Echo trains in pulsed electron spin resonance of a strongly coupled spin ensemble, Physical Review Letters **125** , 137701 (2020). 

- [32] J. Gordon and K. Bowers, Microwave spin echoes from donor electrons in silicon, Physical Review Letters **1** , 368 (1958). 

- [33] G. Feher, Electron spin resonance experiments on donors in silicon. i. electronic structure of donors by the electron nuclear double resonance technique, Physical Review **114** , 1219 (1959). 

- [34] J. H. Wesenberg, A. Ardavan, G. A. D. Briggs, J. J. Morton, R. J. Schoelkopf, D. I. Schuster, and K. Mølmer, Quantum computing with an electron spin ensemble, Physical Review Letters **103** , 070502 (2009). 

- [35] I. Chiorescu, N. Groll, S. Bertaina, T. Mori, and S. Miyashita, Magnetic strong coupling in a spin-photon system and transition to classical regime, Physical Review B—Condensed Matter and Materials Physics **82** , 024413 (2010). 

- [36] I. Diniz, S. Portolan, R. Ferreira, J. G´erard, P. Bertet, and A. Auffeves, Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for longlived solid-state quantum memories, Physical Review A—Atomic, Molecular, and Optical Physics **84** , 063810 (2011). 

11 

- [37] F. Fesquet, _Demonstration of microwave single-shot quantum key distribution_ , Phd thesis, Technische Universit¨at M¨unchen (2025), available at `https: //www.wmi.badw.de/fileadmin/WMI/Publications/ Fesquet_Florian_Doktorarbeit_2025.pdf` . 

- [38] C. W. Gardiner and M. J. Collett, Phys. Rev. A **31** , 3761 (1985). 

- [39] D. A. Steck, Quantum and atom optics (2007). 

- [40] K. Sandner, H. Ritsch, R. Ams¨uss, C. Koller, T. N¨obauer, S. Putz, J. Schmiedmayer, and J. Majer, Strong magnetic coupling of an inhomogeneous nitrogen-vacancy ensemble to a cavity, Physical Review A—Atomic, Molecular, and Optical Physics **85** , 053806 (2012). 

- [41] M. Aspelmeyer, T. J. Kippenberg, and F. Marquardt, Rev. Mod. Phys. **86** , 1391 (2014). 

- [42] S. Probst, F. Song, P. A. Bushev, A. V. Ustinov, and M. Weides, Rev. Sci. Instrum. **86** , 024706 (2015). 

- [43] S. L. Braunstein and P. van Loock, Quantum information with continuous variables, Rev. Mod. Phys. **77** , 513 (2005). 

- [44] M. M¨uller, T. Luschmann, A. Faltermeier, S. Weichselbaumer, L. Koch, G. B. Huber, H. W. Schumacher, N. Ubbelohde, D. Reifert, T. Scheller, F. Deppe, A. Marx, S. Filipp, M. Althammer, R. Gross, and H. Huebl, Magnetic field robust high quality factor nbtin superconducting microwave resonators, Materials for Quantum Technology **2** , 015002 (2022). 

- [45] M. Afzelius, N. Sangouard, G. Johansson, M. Staudt, and C. Wilson, Proposal for a coherent quantum memory for propagating microwave photons, New Journal of Physics **15** , 065008 (2013). 

- [46] B. Julsgaard, C. Grezes, P. Bertet, and K. Mølmer, Quantum memory for microwave photons in an inhomogeneously broadened spin ensemble, Physical Review Letters **110** , 250503 (2013). 

- [47] L. Greggio, T. Lorriaux, A. Petrescu, M. Mirrahimi, and 

   - A. Bienfait, Optimal absorption and emission of itinerant fields into a spin ensemble memory, arXiv preprint arXiv:2506.06107 (2025). 

- [48] J. Z. Bern´ad, M. Schilling, Y. Wen, M. M. M¨uller, T. Calarco, P. Bertet, and F. Motzoi, Analytical solutions for optimal photon absorption into inhomogeneous spin memories, Journal of Physics B: Atomic, Molecular and Optical Physics **58** , 035501 (2025). 

- [49] F. Fesquet, F. Kronowetter, M. Renger, W. K. Yam, S. Gandorfer, K. Inomata, Y. Nakamura, A. Marx, R. Gross, and K. G. Fedorov, Demonstration of microwave single-shot quantum key distribution, Nat. Commun. **15** , 7544 (2024). 

- [50] A. Schweiger and G. Jeschke, _Principles of pulse electron paramagnetic resonance_ (Oxford university press, 2001). 

- [51] S. Weichselbaumer, P. Natzkin, C. W. Zollitsch, M. Weiler, R. Gross, and H. Huebl, Quantitative modeling of superconducting planar resonators for electron spin resonance, Phys. Rev. Appl. **12** , 024021 (2019). 

- [52] C. W. Zollitsch, K. Mueller, D. P. Franke, S. T. B. Goennenwein, M. S. Brandt, R. Gross, and H. Huebl, High cooperativity coupling between a phosphorus donor spin ensemble and a superconducting microwave resonator, Applied Physics Letters **107** (2015). 

- [53] E. L. Hahn, Spin echoes, Physical Review **80** , 580 (1950). 

- [54] A. M. Tyryshkin, S. A. Lyon, A. Astashkin, and A. Raitsimring, Electron spin relaxation times of phosphorus donors in silicon, Physical Review B **68** , 193207 (2003). 

- [55] C. Eichler, D. Bozyigit, C. Lang, M. Baur, L. Steffen, J. M. Fink, S. Filipp, and A. Wallraff, Observation of two-mode squeezing in the microwave frequency domain, Physical Review Letters **107** , 113601 (2011). 

- [56] S. Boutin, D. M. Toyli, A. V. Venkatramani, A. W. Eddins, I. Siddiqi, and A. Blais, Effect of higher-order nonlinearities on amplification and squeezing in josephson parametric amplifiers, Physical Review Applied **8** , 054030 (2017). 

