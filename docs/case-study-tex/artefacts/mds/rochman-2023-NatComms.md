https://doi.org/10.1038/s41467-023-36799-0 



### Article 

# Microwave-to-optical transduction with erbium ions coupled to planar photonic and superconducting resonators 

Received: 14 July 2022 Accepted: 17 February 2023 Check for updates 





Jake Rochman<sup>1,2,5</sup> , Tian Xie<sup>1,2,5</sup> , John G. Bartholomew 1,2,3,4, K. C. Schwab1,2 & Andrei Faraon 1,2 

Optical quantum networks can connect distant quantum processors to enable secure quantum communication and distributed quantum computing. Superconducting qubits are a leading technology for quantum information processing but cannot couple to long-distance optical networks without an efficient, coherent, and low noise interface between microwave and optical photons. Here, we demonstrate a microwave-to-optical transducer using an ensemble of erbium ions that is simultaneously coupled to a superconducting microwave resonator and a nanophotonic optical resonator. The coherent atomic transitions of the ions mediate the frequency conversion from microwave photons to optical photons and using photon counting we observed device conversion efficiency approaching 10<sup>−7</sup> . With pulsed operation at a low duty cycle, the device maintained a spin temperature below 100 mK and microwave resonator heating of less than 0.15 quanta. 

Quantum transducers that convert photons between different energies are essential components of a hybrid quantum network<sup>1,2</sup> . Transducers that operate between microwave and optical frequencies are of particular interest to interface state-of-the-art cryogenic superconducting quantum circuits<sup>3</sup> , with excitations at microwave frequencies, and room temperature optical quantum networks using telecom photons<sup>4</sup> . Efficient, low-noise, and high bandwidth microwave-to-optical quantum transducers can permit superconducting circuits to function within large-scale and long-distance quantum communication and distributed quantum computing systems<sup>5,6</sup> . High-efficiency transduction requires strong coupling between the transduction medium and both optical and microwave photons. Low noise transduction requires low temperature operation (T < _ω/kB), and minimal decoherence or added parasitic photons from the conversion process. Efforts to develop a microwave-to-optical transducer have focused on schemes using an intermediate mechanical mode<sup>7,8</sup> or electro-optic materials<sup>9,10</sup> , while other approaches, such as atomic ensembles<sup>11–13</sup> or magnonic systems<sup>14</sup> , have also been demonstrated recently. 

Ensembles of rare-earth ions (REIs) in crystals offer a promising platform for microwave-to-optical transduction (Fig. 1a). Efficient transduction can be achieved by simultaneous strong ensemble coupling of REI’s Zeeman or hyperfine transitions to a microwave resonator and their coherent 4f-4f optical transitions to an optical cavity. Also, REIs offer advantages for operating in the low noise regime due to the absence of a mechanical mode that can be susceptible to thermal excitations and they have narrow atomic transition inhomogeneities (i.e. much smaller than the microwave transduction frequency) that intrinsically minimize the Stokes noise process<sup>15</sup> . Further, REIs systems have demonstrated additional quantum network resources such as quantum memories<sup>16</sup> and single-photon sources<sup>17,18</sup> , which can enable additional functionality when combined with a REI-based transducer. 

Previous REI transducers include bulk crystals with macroscopic resonators that require high optical pump power<sup>11</sup> or on-chip optical and microwave waveguides with limited efficiency<sup>12</sup> . These implementations have used a Raman scattering protocol that requires a 

1Kavli Nanoscience Institute and Thomas J. Watson, Sr., Laboratory of Applied Physics, California Institute of Technology, Pasadena, CA 91125, USA. 2Institute for Quantum Information and Matter, California Institute of Technology, Pasadena, CA 91125, USA.<sup>3</sup> The University of Sydney Nano Institute, The University of Sydney, Sydney, NSW 2006, Australia.<sup>4</sup> Present address: Centre for Engineered Quantum Systems, School of Physics, The University of Sydney, Sydney, NSW 2006, Australia.<sup>5</sup> These authors contributed equally: Jake Rochman, Tian Xie. e-mail: faraon@caltech.edu 

Nature Communications |  (2023) 14:1153 

1 



<!-- Start of picture text -->
a d IS,,* [d B] 0<br>Ground Excited 35 |<br>Ii, State State t 2<br>I=) ‘o/s, Hg[a ea\ lo REIEr*:YVOs Transducer" Optical(~196~  THz)Photons £= 807s PERSE i|| -4<br>4), y 9 I=) +) ,,9 = ACE¢ é 3=2 70 //I -6<br>-/ ® eo. ® 5 65 py -8<br>E) A<br>2 60 C— O<br>Microwave(~5 GHz)photonsphot 55 ypy ~~ in<br>4860 4900 4940 4980<br>b c e Frequency [MHz]<br>I II 1<br>S 0.8 Po1Pod1<br>3<br>ee 32 0.6 He !<br>III 204 I= ) = i<br>eeeSALLE — C02 +) 1i<br>me 1 1<br>0 |=) 1 1 1 1<br>300 pm pm 10 pm tv =v 45 410 5 0 5 10 15<br>———— Laser Detuning [GHz]<br><!-- End of picture text -->



<!-- Start of picture text -->
300 pm pm<br><!-- End of picture text -->

-) 

-) 

Article 

https://doi.org/10.1038/s41467-023-36799-0 







Fig. 2 | CW M2O transduction efficiency with heterodyne detection. a CW heterodyne detection set-up where the upconverted optical tone, generated by mixing an optical pump and the microwave tone in the transducer, was mixed with an optical local oscillator on a photodetector. The microwave beat note signal was then detected on a network analyzer. b The Er<sup>3+</sup> :YVO4 level structure showing all four configurations for generating transduction signals including two using the ground state spin at B~60 mT and two using the excited state spin at B~78 mT. The g-factors of the ground and excited state are shown for the transduction magnetic field angle of 50 degrees from the c-axis. c Normalized heterodyne spectrum where the applied bias magnetic field and the pump laser frequency were swept. The four 

configurations (as labeled in the inset level structure diagrams) for transduction with Er<sup>3+</sup> :YVO4 are identified. The microwave frequency was set to the microwave cavity resonance. In the far-detuned case (i.e. 65-70 mT) the signal was split due to absorption from other optical transitions. d Transduction efficiency spectrum for the ground (purple) and excited (red) state spins as a function of the applied microwave frequency for Po = 550 µW and Pμ = −51 dBm. The level structures used for each trace are shown in the insets and are the same in e. e Transduction efficiency for the ground state (purple) and the excited state (red) at different input optical and microwave power. The circles correspond to the power parameters used in d, where the circle color matches the trace color in d. 

Er<sup>3+</sup> :YVO4 has been shown to be a promising material for microwave-to-optical transduction due to its relatively strong and narrow optical transitions in bulk crystals and telecom optical transition wavelengths<sup>20</sup> . For our integrated transducer, we used an in-plane magnetic field at an angle of 50<sup>o</sup> with respect to the crystal c-axis. In this field orientation, magnetic dipole transitions are allowed for all four optical transitions, which can be frequency resolved because the electron-spin g-factor is different for the optical ground and excited states. 

We first independently characterized the ion-cavity coupling between the erbium ensemble and the microwave and optical resonators. At microwave frequencies, this was conducted by sweeping the magnetic field to bring the erbium spin transitions through the microwave cavity resonance and measuring the cavity transmission spectrum on a network analyzer (Fig. 1d). At a magnetic field of 60 mT, we observed an avoided-crossing due to the large ensemble coupling between the microwave cavity and the erbium ground state spins (gμ,tot=2π = 105 MHz) at the base temperature. Using the measured cavity energy decay rate of κμ=2π = 2 MHz, and spin inhomogeneous linewidth of Δμ=2π = 65 MHz, we obtained a microwave ensemble cooperativity of Cμ = 4g<sup>2</sup> μ,tot<sup>=κ</sup> μ<sup>Δ</sup> μ<sup>= 340.Wealsoobservedcouplingof</sup> the microwave resonator to several spin transitions thatwe attribute to the<sup>167</sup> Er isotope (see Supplementary Note 9 for details) and coupling of the spins directly with the co-planar waveguide. 

The optical ion-cavity coupling was measured by sweeping the frequency of a weak probe laser (Po~1 pW) across the cavity resonance and detecting the light reflected from the cavity on a superconducting nanowire single-photon detector (SNSPD) (Fig. 1e). A magnetic field of 

76 mT was applied such that each transition was resolved, and this is the field used later for excited state transduction. Due to the relatively large cavity linewidth (i.e. κo>ωμ), all the optical transitions coupled to the same optical cavity mode. From fitting the ion-cavity spectrum<sup>21</sup> , we obtained κo=2π = 13.2 GHz and go,tot,k=2π = 2.0 GHz for the optical transition ∣�ig $ ∣�ie and go,tot,?=2π = 0.98 GHz for transition ∣�ig $ ∣ + ie. The inhomogeneous linewidth was measured in photoluminescence (see Supplementary Note 8) to be Δo=2π = 300 MHz resulting in an optical ensemble co-operativity of Co,k = 4.1 and Co,? = 1.1 for the two optical transitions. 

Not all the erbium spins that couple to the microwave resonator can be used for transduction because the mode overlap between the optical and microwave modes is F = 9:5 × 10<sup>�4</sup> and erbium spins are uniformly doped within the substrate. Spins that are only within the microwave cavity act as parasitic spins that can absorb microwave photons but cannot transduce them. The effects from parasitic spins can be suppressed by detuning the spins from the cavity, using the excited state spin for transduction or, for future devices, eliminating their presence by controlling the position of the erbium ions within the device. 

#### Continuous-wave transduction 

As a first step, we measured coherent microwave-to-optical conversion in continuous-wave (CW) mode using a Raman heterodyne technique<sup>11</sup> . The input microwave photons were transduced to optical photons which were mixed with a local oscillator (LO) on a photodetector. The generated microwave beat note was measured with a network analyzer (Fig. 2a). We characterized the large parameter space by performing a 

Nature Communications |  (2023) 14:1153 

3 

Article 

https://doi.org/10.1038/s41467-023-36799-0 

three-dimensional parameter sweep (magnetic field, pump laser frequency and microwave frequency) and observe four atomic configurations that generate a transduction signal. We fixed the optical and microwave power to be Po = 7 µW and Pμ = −51 dBm (referenced to the input of the device) and obtained a high SNR (18 dB) heterodyne spectrum. 

In Fig. 2c, we fixed the microwave frequency on resonance with the microwave cavity (i.e. the microwave frequency with the highest efficiency) and swept the pump laser frequency and the magnetic field strength. There are four configurations for transduction with two conditions that use the ground state spin (Λ systems) at ~60 mT and two conditions that use the excited state spin (V system) at ~78 mT. As the magnetic field changes, the transduction signal follows the laser frequency such that the laser is resonant with the optical transitions. The laser frequency difference between the two Λ (V) systems corresponds to the excited (ground) state spin frequency. The transduction signal decreased when the microwave cavity was resonant with the ground state spin (60 mT) due to extra losses from the parasitic ions but was increased 8 dB by detuning the spins ~100 MHz at 62 mT. 

In Fig. 2d, we show the device transduction efficiency, ηd, for both the ground state and excited state at Po = 550 µW and Pμ = −51 dBm as a function of the input microwave frequency. We define the device transduction efficiency as the ratio of converted optical photons that propagate into the output optical fiber compared to the microwave photons in the input microwave coupling waveguide. We focus on the transduction configurations where the pump laser is coupled to the ∣ + ig $ ∣�ie transition as these configurations have higher efficiency in CW mode. The pump laser frequency was selected to maximize the efficiency and was near the center of the inhomogeneous line. 

The transduction efficiency linewidth followed the microwave cavity linewidth, which is the narrowest bandwidth component of the transducer. The ground state signal had an asymmetric line shape due to the large microwave power that drove the spins during the measurement. The bandwidth of the transduction signal was 1 MHz, which matches the microwave cavity linewidth for each measurement. 

Next, we determined the efficiency dependence on both the optical and microwave power for ground and excited state transduction (Fig. 2e). In our integrated REI transducer, the transduction efficiencyreached a maximum at Po = 550 µW. At higher optical power, the efficiency decreased primarily due to device heating, which limited the spin population difference and caused optical transition saturation. We measured a maximum CW device efficiency of ηd = 2 × 10<sup>�9</sup> in the ground state (Po = 550 µW/ Pμ = −46 dBm) and ηd = 3 × 10<sup>�9</sup> in the excited state (Po = 550 µW/ Pμ = −71 dBm). At this optical power, we expect a spin temperature of ~2 K (see SI Fig. S13), but the temperature can be reduced by operating in a pulsed mode. 

As the microwave power was reduced (i.e. Pμ< � 50 dBm), the ground state efficiency decreased as the input microwave tone was no longer saturating the absorption from the parasitic spins that diminished the transducer efficiency. This makes excited state transduction more promising in the low microwave power and low temperature regime for this device. 

#### Pulsed transduction 

To reduce the device temperature and increase the device efficiency, we characterized the REI transducer operating in pulsed mode. Short transduction pulses and small duty cycles were used to lower the device temperature and minimize optical transition saturation from large driving fields, which limited the device efficiency in CW mode. We also implemented direct photon detection of the transduced optical photons. Here, we attenuated the pump laser photons by ~140 dB with tunable spectral filters and detected the transduced photons using an SNSPD (Fig. 3a). Photon detection is advantageous due to the decreased noise floor, especially for short pulses/ high 

bandwidth measurements, and for measuring transduced single photons<sup>8</sup> . 

For measuring pulsed transduction, we focused on excited state transduction to reduce the effects of the parasitic ions. We applied a magnetic field of 76 mT to avoid the losses associated with the parasitic transitions of the<sup>167</sup> Er isotope. Future devices can use isotopically purified zero-nuclear-spin erbium isotopes to eliminate this complication. In contrast to the previous CW excited state transduction, we set the optical pump frequency to the ∣�ig $ ∣ + ie transition so that the population in the involved ground state increases as the temperature decreases. 

We first characterized the transducer bandwidth by measuring the transduced pulse as a function of the pulse duration at a fixed duty cycle (duty cycle = τpulse/τoff ) of 0.01% with Pμ = −60 dBm and Po = 550 µW (Fig. 3c). We only considered relatively short pulses (τpulse < 10 µs) to avoid significant heating during the transduction pulse. The efficiency reached −3 dB of the maximum when the pulse length decreases to τpulse = 630 ns, which matches the microwave cavity bandwidth. There is a tradeoff between reducing the average optical power for reduced temperature and the maximum efficiency, so we fixed our transduction pulse length to 1 µs for all subsequent pulsed measurements. 

Next, we measured the transducer efficiency as a function of the off time between adjacent transduction pulses (Fig. 3d). As we increased the off time from 30 µs to 100 ms, we observe an increase in efficiency from ηd = 9 × 10<sup>�9</sup> to ηd = 7 × 10<sup>�8</sup> . We attribute this increase in efficiency to a reduction in the device temperature and operating with input fields below saturation of the atomic transitions. The decreased spin temperature increases the number of ions in the V system and increases the efficiency. The efficiency did not increase beyond τoff = 100 ms as the spin temperature saturated beyond this off time (Fig. 4d). 

The model used for the simulation is described in Supplementary Note 2 and used the parameters in Table S4. The only free parameters of the simulation are the spin and optical dephasing rates. The temperature used in the model is from the experimentally determined data from Fig. 4d. 

We also measured the pulsed transduction efficiency as a function of the input microwave power (Fig. 3e). Ideally, we could characterize the transducer at the single photon level where a quantum transducer would operate, but the modest device and detection efficiency and the finite measurement noise of the setup limited measurements to input microwave pulses with ~10<sup>4</sup> photons. At Pμ = −100 dBm (10<sup>4</sup> microwave photons per pulse), we observed a maximum pulsed excited state transduction efficiency of ηd = 6 × 10<sup>�8</sup> . There is an efficiency roll-off at Pμ ∼ −55 dBm (~10<sup>9</sup> photons per pulse) that we attribute to saturation of the microwave transition. The linear approximation of the transduction model, which predicts that the efficiency is independent of the microwave input power, is a good approximation up to the efficiency roll-off power. 

For the optical power sweep, we observed a continuous increase in the efficiency to ηd = 1 × 10<sup>�7</sup> with optical pump power up to Po = 5 mW, which differs from the CW operation where the efficiency reached a maximum at Po = 550 µW (Fig. 3f). Based on the model described in Supplementary Note 2, the transduction efficiency scales linearly with the pump optical power. The rate of efficiency increase with optical power (i.e. dηd/dPo) decreases at the highest optical power in the pulsed mode, which suggests we are approaching the highest efficiency for this device in the pulsed operation. We attribute the simulation and experimental deviation to small changes in the optimal magnetic field and laser frequency as the optical power is changed. All experimental parameters were optimized at Po = 550 μW (highlighted by a red circle in Fig. 3f) and remained fixed during the power sweep. 

Nature Communications |  (2023) 14:1153 

4 

Article 

https://doi.org/10.1038/s41467-023-36799-0 



Fig. 3 | Pulsed excited state transduction efficiency with photon counting detection. a Schematic of the pulsed transduction setup using photon counting detection by filtering out the pump laser. Before the transducer one filter was used to remove broadband noise from the laser, while after the transducer the two high finesse Fabry-Perot filters and a set of broadband spectral filters were used to remove the main pump laser tone and broadband noise leakage. b Pulse sequence configuration, where we have a square pulse of length, τpulse, and an off time between pulses of length, τoff , for both the optical and microwave pulses simultaneously. The level structure used for the excited state transduction process used in c-f. c) Pulsed transduction efficiency as a function of the pulse length with a fixed duty cycle ~~(~~ ττpoffulse<sup>= 0:01%). Inset shows the time domain signal of the 1 µs</sup> 

transduction pulse, where we obtain SNR of 40 dB. The simulation plotted in the red dashed line models the pulse spectral overlap with the microwave resonator. d–f Transduction efficiency as a function of the off time between transduction pulses, the input microwave power, and the input optical pump power, respectively, for a 1 µs transduction pulse. The red circles represent the common experimental condition in the different parameter sweeps. The simulation plotted in the red dashed line follows the model described in Supplementary Note 2. Errorfi fi fi fi fi fi fiffi bars correspond to pcounts measured on the SNSPD and the error bars are propagated to the efficiency. The simulation error bars correspond to the spin temperature uncertainty. 

#### Device temperature analysis 

During the transduction process, heating from the optical pump can induce noise photons that can pollute the transducer output field. Ideally, to characterize this noise, we can measure the generated noise photons directly at the transducer output. However, due to our limited device efficiency, some noise sources (i.e. thermal microwave excitations) are heavily suppressed at the transducer output, so we cannot faithfully determine the noise contributions from those sources. Instead, we quantify the temperature or noise of different components of the transducer<sup>22–24</sup> . 

Here, we measured the temperature of the erbium ions and the microwave resonator noise to quantify the optical heating effects during the transduction process, which we suspect to be the dominating noise source for our REI transducer. For the erbium spins there are two ensembles that we can characterize; all the erbium ions that couple to the microwave resonator and the erbium ions that are used for transduction (i.e. ions within both the optical and microwave mode volumes). 

The average temperature of the ensemble of erbium ground state spins that couple to the microwave cavity was determined by measuring the microwave polariton frequency during transduction (Fig. 4a). Optical heating decreases the population difference between the erbium spins, which decreases the microwave cavity mode pulling that determines the microwave frequency that has the largest transduction signal. 

We measured the microwave frequency spectrum of the transduction signal for the ground state spin at a magnetic field of 60 mT, Po= 550 µW, Pμ = −60 dBm, τpulse = 1 µs and swept the off time between the pulses to change the average optical power incident on the device. We observed an increase in the transduction signal splitting, 

corresponding to a decrease in device temperature, as we increase the off time. An average spin temperature of ~100 mK was reached at an off time of 100 ms for the spins coupled to the microwave resonator (Fig. 4d). 

The temperature of the erbium spins within the transducer was estimated by measuring the excited state transduction efficiency for the two configurations that interact with each ground state spin level. In the regime where the ion dynamics evolve linearly, the transduction efficiency scales quadratically as a function of population (ηd / N<sup>2</sup> ). By measuring the efficiency ratio between the two configurations, we can deduce the ground state spin population distribution and thus the erbium ground state spin temperature. 

We measured the transduction efficiency for both V-systems at a magnetic field of 76 mT and keep the input power and pulse sequence the same as in the previous microwave resonator spin temperature measurement (Fig. 4b). As the off time increases, the transducer spin temperature decreases, which results in the V system involving the ∣ + ig state to have decreased efficiency, while the V system involving the ∣�ig state efficiency increases due to increased population and lower device temperature (Fig. 4d). As the off time increased to 300 ms, we measured an efficiency ratio up to 20 dB which corresponds to a transducer spin temperature of 100 mK. The temperature of the spins within the transducer was measured to be slightly higher than the ensemble of spins coupled to the microwave resonator, which we attribute to closer proximity to the optical heating source. 

The thermal noise within the microwave resonator due to optical pulses was determined by measuring the thermal noise that coupled to the co-planar waveguide and propagated through the microwave detection setup<sup>25</sup> . After accounting for the added noise (Nadd ~ 6.8 

Nature Communications |  (2023) 14:1153 

5 



<!-- Start of picture text -->
a b c N,N, [Hz's"]<br>ai ULL TTL SE 10<br>[ Ll LITUE 1 0 0.85<br>_ . 11 . wl,<br>£ | Z — be 0.8<br>10% [Fl = g 0<br>i L_ his) me E 0 0.75<br>+), 10°F 11, 1, 1<br>d ! 1! 1 .<br>10° I, : HE ! ' "J ! -40<br>11+ i | 4) ' 11, ' 60 0.7<br>4800 4850 4900 4950 5000 5050 102 10° 10 10 4932 4934 4936 4938 4940<br>Microwave Frequency [MHz] Off Time [ms] Microwave Frequency [MHz]<br>d Averaged Optical Power [uW] e Averaged Opticali Power [pW]<br>5 5x10! 5x10 5x10 5x1 0 10! 5 5x10! 5x10 5x1073 5x1 0<br>—3—  Resonator Spin Temperature Tose = 20 us -3- N,<br>_ —3&— Transducer Spin Temperature = Tow t -§- N<br>=)p  100 11 Microw a ave CavitysOptica Athl Cavity N! = 10° TT—- S— _e TT o -a [1  ~- 5 _ Ra- h [1 + Noosecov<br>& \ Resonator Spins Transducer Spins Zz / o N , L N<br>5] -1 S uita 1 0" “w w , E ..<br>= Tous ~ LHS 1 ST $ e<br>10 7 1 1! Ninode nooNews -aS<br>10° 10° 10 a 10? === 10° 102 10 S==TTo ooo” 10° 10! 102 10°<br><!-- End of picture text -->

Article 

https://doi.org/10.1038/s41467-023-36799-0 

low temperature regime. A path to near unit efficiency is detailed in Supplementary Note 17. 

This transducer device operates at a magnetic field of 60–80 mT to bring the erbium spin transition into resonance with the 4.94 GHz microwave cavity. Interfacing the transducer with a superconducting qubit, which traditionally do not operate within large magnetic fields, would require separating the superconducting qubit chip and the transducer with sufficient magnetic shielding in between, interfacing with superconducting qubits that can operate within large magnetic fields<sup>26</sup> or using other rare-earth ion transitions that allow for transduction at zero or near zero magnetic field<sup>12</sup> . 

With these improvements, integrated REI transducers with highefficiency and low noise operation could be operated with high repetition rates that will allow us to interface our transducer with nonclassical light and superconducting circuits. 

## Methods 

#### Fabrication 

The transducer was fabricated on a 500 µm thick a-cut Er<sup>3+</sup> :YVO4 substrate (560 ppm natural abundance doping concentration). A 5 nm thick alumina layer was deposited with ALD to protect the YVO4 substrate during subsequent dry etching steps. Next, a 150 nm thick film of niobium was sputtered on the surface. The sputterer has a base pressure of 5 × 10<sup>�10</sup> Torr. The deposition was done at a pressure of 7 mTorr with a DC bias power of 200 W resulting in a deposition rate of ~7 Å/s. The deposition pressure was chosen to minimize the niobium thin film stress. MaN-2403 was patterned on the niobium surface using electron beam lithography to define the niobium resonator, coupling waveguide and ground plane. A 25 nm thick aluminum hard mask was deposited on the surface using electron-beam evaporation and the MaN-2403 pattern was transferred to the aluminum hard mask layer with liftoff in Remover PG. The niobium layer was etched in SF6 + Ar chemistry with an ICP-RIE process using aluminum pattern as the hard mask. 

A 300 nm thick film of amorphous silicon was deposited by PECVD. The amorphous silicon photonic structure was defined with electron beam lithography in HSQ (FOx-16) resist. The pattern was transferred to the amorphous silicon layer using a pseudo-bosch process (SF6 + C4F8 chemistry) in an ICP-RIE system. An HF dip was used to remove the remaining HSQ mask and the aluminum hard mask that protected the niobium layer during the amorphous silicon etching step. 

The fabricated device was mounted in a copper box with optical access through a hole in the lid of the box. The niobium co-planar waveguide and ground plane were wire-bonded to a PCB launch board that connected to coaxial cable with an SMP connector. The box was mounted on a copper post on the mixing chamber stage of the dilution refrigerator. 

#### Measurement setup 

A detailed diagram of the measurement set-up is shown in Fig. S7. We coupled to the device optically using an optical fiber that focused light through a lens pair onto the grating coupler that coupled to the optical resonator. The optical fiber and lens pair setup were mounted on a 3-axis piezo stack to control the position of the light and aligned with a 5<sup>o</sup> angle (relative the axis of the sample surface) to best match the output mode of the grating coupler. 

To generate a bias magnetic field for the transducer, we used a two-axis home-built split-pair superconducting electromagnet mounted on the mixing chamber stage of the dilution refrigerator. One axis was used to generate a large (up to ~100 mT) in-plane magnetic field and the second smaller correction coil was used to minimize the out of plane magnetic field. 

Gas condensation was used to tune the optical cavity into resonance with the Er<sup>3+</sup> :YVO4 optical transitions. Nitrogen gas was 

introduced to the fridge at 4 K (i.e. before cooling to base temperature using the dilution unit) and frozen within a copper tube. A heater, thermally lagged to the copper tube at the 4 K stage, permitted the frozen nitrogen to sublimate and then condense on the optical cavity, which provided the resonance tuning. The heater power and duration were controlled to achieve the target frequency. 

For microwave measurements, a network analyzer or microwave signal generator was used as the input signal. For pulsed measurements, the microwave input passed through a fast microwave switch before the fridge. The input microwave coaxial cable to the device in the fridge passed through a series of attenuators at the different stages of the fridge (40 dB in total) before connecting to the PCB launch board with an SMP connector. The output microwave signal passed through two circulators on the mixing chamber stage, superconducting coax between the mixing chamber stage and the 4 K stage and a HEMT on the 4 K stage before exiting the fridge. A low noise amplifier (LNA) at room temperature was used to further amplify the signal before detection on a network analyzer, spectrum analyzer or digitizer when measuring weak signals. 

For the optical measurements, an external cavity diode laser (ECDL) was locked to a stable reference cavity for measurements where a precise laser frequency was needed. For measurements that swept the laser frequency several GHz, the laser was left unlocked, and an internal piezo actuator was used. 

The input light path was modified for the different experiments. For heterodyne measurements, the input light was split on a 90/10 beam splitter, where the 10% path acted as a LO for heterodyne detection and the 90% path passed through a 100 MHz fiber AOM, a polarization controller and a variable optical attenuator towards the device. The AOM acted as a fast optical switch for pulsed measurements and offset the transduction pump laser frequency (and thus the upconverted transduction signal) for heterodyne detection. For photon detection with an SNSPD, an additional Fabry-Perot cavity (finesse = 1000, FSR = 100 GHz) was used at the input to filter the laser noise and was locked to the laser frequency with piezo feedback. A fiber circulator was used to input light to the fridge and route the output photons from the device to the optical detection path. 

For heterodyne measurements, the output optical signal was combined with the LO and mixed down to microwave frequencies on a photodiode. The photodiode output signal passed through a bias tee and the high frequency component was amplified using two LNAs before detection on a network analyzer. 

For SNSPD detection, the output optical light passed through a filtering setup consisting of two high finesse fiber-coupled Fabry-Perot filter cavities (finesse = 10,000, FSR = 20 GHz), a broadband bandpass filter array and two fiber circulators before each Fabry-Perot cavity and a series of optical MEMS switches which were used to change the light path between the locking path and a detection path. The Fabry-Perot filters were frequency stabilized to the transduction light frequency using Pound-Drever-Hall locking with feedback on the Fabry-Perot piezo in a pulsed mode. Every 5 s, the light path switched from measuring transduced photons with the filter piezo voltage held at a fixed value to a locking path where light at the transduction frequency was generated from the laser with an EOM sideband and detected on a photodiode for feedback. 

Before each high finesse filter, fiber circulators were used to prevent reflections and mode coupling between the filters. A broadband bandpass filter array (1× FWHM = 30 GHz filter, 3× FWHM = 400 GHz filters) was place between the two Fabry-Perot filters to prevent far detuned laser noise that leaked through our initial laser noise filter from reaching the SNSPD. Before entering the fridge, the light passed through a 2 km fiber to delay the transduction signal by 11 µs. We observed crosstalk between the optical pump to our device and the SNSPD in the same fridge, so the time delay allowed us to filter out the crosstalk in the time domain. Better packaging in future experiments 

Nature Communications |  (2023) 14:1153 

7 

Article 

https://doi.org/10.1038/s41467-023-36799-0 

can eliminate the crosstalk. The light went back into the dilution refrigerator and passed through a coiled fiber on the 4 K stage to filter IR photons before detection on the SNSPD (background counts ~5 counts/s). 

The filter setup insertion loss was −15 dB, where most of loss came from the insertion loss of the Fabry-Perot filters (~ −7.75 dB). The − remaining loss came from the optical MEMS switches (< 0.5 dB each), fiber circulators (<−0.5 dB each), the broadband filters (−2.2 dB), fiber mating connections, and SNSPD detection efficiency (−3 dB). The detection noise floor was 10 counts/s, which included 5 counts/s from laser leakage when Po = 550 µW. This corresponds to a filter extinction of ~ 140 dB. Depending on the pulse sequence duty cycle, we also observed PL noise leakage (see Supplementary Note 16). However, for low duty cycle measurements (i.e. off time > 10 ms), this was not a dominant factor. 

For detection of the microwave resonator noise under pulsed optical excitation, the noise was mixed down to ~10–20 MHz and detected on a digitizer after exiting the fridge. For continuous wave optical light excitation, a spectrum analyzer was used for detection. 

## Data availability 

The data that support the findings of this study are available from the corresponding author upon request. 

## References 

1. Lambert, N. J., Rueda, A., Sedlmeir, F. & Schwefel, H. G. Coherent conversion between microwave and optical photons—an overview of physical implementations. Adv. Quantum Technol. 3, 1900077 (2020). 

2. Lauk, N. et al. Perspectives on quantum transduction. Quantum Sci. Technol. 5, 020501 (2020). 

3. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505–510 (2019). 

4. Valivarthi, R. et al. Quantum teleportation across a Metropolitan Fibre Network. Nat. Photonics 10, 676–680 (2016). 

5. Kimble, H. The quantum internet. Nature 453, 1023–1030 (2008). 6. Cacciapuoti, A. S. et al. Quantum Internet: networking challenges in distributed quantum computing. IEEE Netw. 34, 137–143 (2020). 

7. Higginbotham, A. P. et al. Harnessing electro-optic correlations in an efficient mechanical converter. Nat. Phys. 14, 1038–1042 (2018). 

8. Mirhosseini, M., Sipahigil, A., Kalaee, M. & Painter, O. Superconducting qubit to optical photon transduction. Nature 588, 599–603 (2020). 

9. Xu, Y. et al. Bidirectional interconversion of microwave and light with thin-film lithium niobate. Nat. Commun. 12, 4453 (2021). 

10. Sahu, R. et al. Quantum-enabled operation of a microwave-optical interface. Nat. Commun. 13, 1276 (2022). 

11. Fernandez-Gonzalvo, X., Horvath, S. P., Chen, Y.-H. & Longdell, J. J. Cavity-enhanced Raman heterodyne spectroscopy in Er3+:Y2SiO5 for microwave to optical signal conversion. Phys. Rev. A 100, 033807 (2019). 

12. Bartholomew, J. G. et al. On-chip coherent microwave-to-optical transduction mediated by ytterbium in YVO4. Nat. Commun. 11, 3266 (2020). 

13. Tu, H.-T. et al. High-efficiency coherent microwave-to-optics conversion via off-resonant scattering. Nat. Photonics 16, 291–296 (2022). 

14. Zhu, N. et al. Waveguide cavity optomagnonics for microwave-tooptics conversion. Optica 7, 1291 (2020). 

15. Wong, N. C., Kintzer, E. S., Mlynek, J., DeVoe, R. G. & Brewer, R. G. Raman heterodyne detection of nuclear magnetic resonance. Phys. Rev. B 28, 4993–5010 (1983). 

16. Lago-Rivera, D., Grandi, S., Rakonjac, J. V., Seri, A. & de Riedmatten, H. Telecom-heralded entanglement between multimode solidstate quantum memories. Nature 594, 37–40 (2021). 

17. Kindem, J. M. et al. Control and single-shot readout of an ion embedded in a nanophotonic cavity. Nature 580, 201–204 (2020). 

18. Raha, M. et al. Optical quantum nondemolition measurement of a single rare earth ion qubit. Nat. Commun. 11, 1605 (2020). 

19. Williamson, L. A., Chen, Y.-H. & Longdell, J. J. Magneto-optic modulator with unit quantum efficiency. Phys. Rev. Lett. 113, 203601 (2014). 

20. Xie, T. et al. Characterization of Er<sup>3+</sup> :YVO4 for microwave to optical transduction. Phys. Rev. B 104, 054111 (2021). 

21. Diniz, I. et al. Strongly coupling a cavity to inhomogeneous ensembles of emitters: potential for long-lived solid-state quantum memories. Phys. Rev. A 84, 063810 (2011). 

22. Hease, W. et al. Bidirectional electro-optic wavelength conversion in the quantum ground state. PRX Quantum 1, 020315 (2020). 

23. Fu, W. et al. Cavity electro-optic circuit for microwave-to-optical conversion in the Quantum Ground State. Phys. Rev. A 103, 053504 (2021). 

24. Forsch, M. et al. Microwave-to-optics conversion using a mechanical oscillator in its quantum ground state. Nat. Phys. 16, 69–74 (2019). 

25. Xu, M. et al. Radiative cooling of a superconducting resonator. Phys. Rev. Lett. 124, 033602 (2020). 

26. Kringhøj, A. et al. Magnetic-field-compatible superconducting transmon qubit. Phys. Rev. Appl. 15, 054001 (2021). 

## Acknowledgements 

This work was supported by the ARO/LPS Cross Quantum Technology Systems program (grant W911NF-18-1-0011), Office of Naval Research awards no. N00014-19-1-2182 and N00014-22-1-2422, Air Force Office of Scientific Research award no. FA9550-21-1-0055, Northrop Grumman, and Weston Havens Foundation. The device nanofabrication was performed in the Kavli Nanoscience Institute at the California Institute of Technology. J.R. acknowledges support from the Natural Sciences and Engineering Council of Canada (Grant No. PGSD3-502844-2017). J.G.B. acknowledges the support of the American Australian Association′s Northrop Grumman Fellowship. The authors would like to acknowledge Jevon Longdell, Yu-Hui Chen, Matt Shaw and Rick LeDuc for useful discussions and Hugo Wallner for simulation development. 

## Author contributions 

J.R. designed and fabricated the device. J.R., T.X., and J.G.B. built the experimental apparatus. J.R. and T.X. measured the device and analyzed the data. J.R. and A.F. wrote the manuscript with input from all authors. K.S. and A.F. supervised the project. 

## Competing interests 

The authors declare no competing interests. 

## Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-023-36799-0. 

Correspondence and requests for materials should be addressed to Andrei Faraon. 

Peer review information Nature Communications thanks the anonymous reviewer(s) for their contribution to the peer review of this work. 

Reprints and permissions information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Nature Communications |  (2023) 14:1153 

8 

Article 

https://doi.org/10.1038/s41467-023-36799-0 

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/ licenses/by/4.0/. 

© The Author(s) 2023 

Nature Communications |  (2023) 14:1153 

9 

