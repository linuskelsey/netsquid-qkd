PHYSICAL REVIEW APPLIED **23,** 044011 (2025) 

~~Editors’ Suggestion~~ 

# **Quantum key distribution with basis-dependent detection probability** 

Federico Grasselli ,<sup>1,2,*</sup> Giovanni Chesi ,<sup>3</sup> Nathan Walk ,<sup>4</sup> Hermann Kampermann ,<sup>1</sup> Adam Widomski ,<sup>5</sup> Maciej Ogrodnik ,<sup>5</sup> Michał Karpi´nski ,<sup>5</sup> Chiara Macchiavello,<sup>3</sup> 1,† Dagmar Bruß ,<sup>1</sup> and Nikolai Wyderka 

1 _Institut für Theoretische Physik III, Heinrich-Heine-Universität Düsseldorf, Universitätsstraße 1, 40225 Düsseldorf, Germany_ 

2 _Leonardo Innovation Labs—Quantum Technologies, Via Tiburtina km 12,400, 00131 Rome, Italy_ 

3 _Physics Department, QUIT Group, University of Pavia, INFN Sezione di Pavia, Via Bassi 6, 27100 Pavia, Italy_ 

4 _Dahlem Center for Complex Quantum Systems, Freie Universität Berlin, 14195 Berlin, Germany_ 

5 _Faculty of Physics, University of Warsaw, Pasteura 5, 02-093 Warsaw, Poland_ 



(Received 9 December 2024; revised 3 February 2025; accepted 26 February 2025; published 4 April 2025) 

Quantum key distribution (QKD) is a promising technology for secure communication. Nevertheless, QKD is still treated with caution in certain contexts due to potential gaps between theoretical models and actual QKD implementations. A common assumption in security proofs is that the detection probability at the receiver, for a given input state, is independent of the measurement basis, which might not always be verified and could lead to security loopholes. This paper presents a security proof for QKD protocols that does not rely on the aforementioned assumption and is thus applicable in scenarios with detection probability mismatches, even when induced by the adversary. We demonstrate, through simulations, that our proof can extract positive key rates for setups vulnerable to large detection probability mismatches. This is achieved by one monitoring whether an adversary is actively exploiting such vulnerabilities, instead of considering the worst-case scenario as in previous proofs. Our work highlights the importance of accounting for basis-dependent detection probabilities and provides a concrete solution for improving the security of practical QKD systems. 

DOI: 10.1103/PhysRevApplied.23.044011 

## **I. INTRODUCTION** 

Quantum key distribution (QKD) is one of the most studied, developed, and commercialized quantum technologies of the past few decades [1]. With QKD, two users can, in principle, establish an information-theoretically secure key when linked by an insecure quantum channel and an authenticated classical channel [2], thereby providing a solution for long-term secure communication. 

However, QKD is still facing some challenges that hinder its widespread adoption and standardization [3]. From a security point of view, the main challenge is the implementation security of QKD protocols [4,5], which arises due to a disagreement between the theoretical models used by the security proofs and the actual implementation 

- *Contact author: federico.grasselli@hhu.de 

- †Contact author: wyderka@hhu.de 

_Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article’s title, journal citation, and DOI._ 

of QKD protocols. Indeed, discrepancies between theory and experiment have been exploited to conduct successful quantum hacking attacks on QKD setups [6]. 

A crucial quantity in the security of prepare-andmeasure QKD schemes with two measurement bases is the phase error rate [7]. In simple terms, this is the error rate in a basis complementary to the key basis— usually called the “test basis”—that characterizes the pulses detected in key generation rounds. Standard QKD security proofs assume that the detection probability of a given state is independent of the measurement basis [8–10], such that the phase error rate reduces to the (observed) bit error rate of the test measurements. However, this assumption is typically not verified by QKD experimental setups, potentially opening a security loophole that can be exploited by an eavesdropper. 

A basis-dependent detection probability, or efficiency—we will use the two terms interchangeably— could originate from an asymmetry in the nominal efficiency or dark count probability of the detectors used in the two measurement bases [11,12]. The resulting mismatch in the detection probability of the two bases is typically independent of the optical mode incident upon the detector and 

2331-7019/25/23(4)/044011(85) 

Published by the American Physical Society 

044011-1 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

can be easily characterized. On the other hand, a modedependent detection efficiency mismatch could originate from an asymmetric coupling of the two measurement bases to the incoming mode. A notable example is tailored light pulses prepared by the adversary to control which basis clicks in time-frequency QKD setups [13,14]. Regardless of the origin, a basis-dependent detection probability introduces a vulnerability in the QKD protocol that must be treated with hardware countermeasures or security proof fixes. Indeed, popular attacks on QKD systems, such as detector blinding attacks [15], time-shift attacks [16], and spatial-mode attacks on free-space QKD systems [17], can be traced back to basis-dependent detection probabilities. 

In this work, we address the security of prepare-andmeasure QKD protocols with basis-dependent detection probabilities. In particular, we derive an analytical security proof where the assumption about the independence of the detection probability of a state from the measurement basis is dropped. This implies that the phase error rate is no longer identified with the bit error rate in the test basis. Our proof directly applies to all QKD setups where one of the two measurements is a time-of-arrival measurement, e.g., time-bin QKD [18–21] and time-frequency QKD [13,22–27], but could also be extended to other setups. Our proof is obtained in the asymptotic regime and under collective attacks. 

A key role in our solution is played by a high-speed tunable beam splitter (TBS) that is used by the receiver to redirect the signal to the two measurement bases. Our proof processes the rich measurement statistics enabled by the TBS with advanced techniques, including the detector decoy technique [28], to quantify the mismatch in the detection probability of the two bases and reduce the key rate accordingly. 

We apply our proof to an experimental time-encoded QKD setup that is prone to efficiency mismatches [29,30] and show that it generates positive key rates for honest implementations. We then design a sophisticated attack that induces significant asymmetries in the detection efficiency of the two bases by preparing tailored pulses. We show that our proof reduces the key rate proportionately to the extent of the attack, while the standard BB84 key rate would return overly optimistic key rates due to its inability to detect the attack. Moreover, we argue that previous security proofs applicable to such scenarios would return pessimistic rates since they consider the worst-case scenario, i.e., the scenario of the attack, even when the eavesdropper is not present. 

This paper is organized as follows. In Sec. II we discuss security loopholes and countermeasures linked to basisdependent detection probabilities and describe an attack exploiting asymmetric nominal efficiencies. In Sec. III we illustrate a generic prepare-and-measure QKD protocol, which may feature basis-dependent detection probabilities. 

In Sec. IV we highlight the main points of the protocol’s security proof, while we defer the fully detailed proof to Appendix C. In Sec. V we simulate the key rate of a time-encoded QKD scheme with our security proof both in an honest implementation and with attack-induced detection efficiency asymmetries. We provide further simulation details in Appendix E. We discuss the results of the simulations in Sec. VI and provide a summary in Sec. VII. In Appendix A we summarize the notation used in the paper, while in Appendix B we report the formula for the phase error rate resulting from our security proof. In Appendix D we derive some of the bounds required by our proof with the decoy-state method. 

## **II. SECURITY LOOPHOLES AND COUNTERMEASURES** 

Several proposed and implemented QKD schemes can present asymmetries in the detection probability of the two measurement bases, for certain input states. If their security proof fails to account for this fact, an eavesdropper could exploit the security loophole to invalidate the security claim on the established keys. In this paper, we adopt the common nomenclature of QKD for which Alice is the sender of the pulses and Bob the receiver, while Eve is the eavesdropper. 

A mode-independent detection probability mismatch is easier to characterize and treat since the magnitude of the mismatch is independent of the light mode measured by Bob. It can be caused, for example, by detectors with unequal nominal efficiencies and/or unequal dark count probabilities. Nevertheless, here we provide an example where ignoring an asymmetry in the nominal detection efficiency of two detectors opens the door for a successful attack by Eve. To our knowledge, this type of attack was not listed in a recent report by the German cyber security agency (Bundesamt für Sicherheit in der Informationstechnik) about implementation attacks on QKD [31]. 

Consider the BB84 protocol where Bob has an active basis choice and, for simplicity, Alice has a deterministic single-photon source (the attack would also work with decoy BB84). Suppose that Eve performs an intercept-andresend attack where she intercepts the signal and measures it in the _Z_ or _X_ basis, each with probability _p_ , while she lets the signal go undisturbed with probability 1 − 2 _p_ . Since Eve’s attack generates noise in Bob’s measurements, the key rate is reduced accordingly. In particular, the fraction of secret key bits in the sifted rounds is given by the BB84 asymptotic key rate: 



If the _Z_ -basis and _X_ -basis detectors both have unit efficiency and if the quantum channel is ideal, except for 

044011-2 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

Eve’s attack, the quantum bit error rate (QBER) in the two bases reads _QX_ = _QZ_ = _p/_ 2, where the factor 1 _/_ 2 accounts for the fact that when Eve’s and Bob’s bases differ, Bob’s outcome is random. Suppose that the _X_ -basis detector has efficiency _ηX_ , with _ηX <_ 1, while the _Z_ -basis detector is still ideal. In this case, Eve performs the same attack as before, but this time she resends a pulse with _n_ photons (one photon) when she measures in the _X_ basis ( _Z_ basis). This has the effect of spoiling the statistics of Bob’s _X_ -basis outcomes, by flooding them with events where there is no error since Eve’s and Bob’s bases agree, thereby decreasing the QBER in the _X_ basis. Indeed, the error probability in the _X_ basis is unchanged—the errors are still caused by the one photon sent by Eve when she chooses the wrong basis, i.e., the _Z_ basis—but the detection probability increases due to more photons arriving when Eve’s and Bob’s bases coincide. Overall, this decreases the QBER in the _X_ basis, which now reads 



On the other hand, _QZ_ remains unchanged by Eve’s new attack, if we assume that multiclick events in the _Z_ basis are assigned randomly to one of the outcomes. As a consequence, the fraction of secret key bits in the sifted rounds, as per Eq. (1), increases compared with the case with ideal detectors, but Eve’s knowledge of the key remains the same (indeed, note that the rounds discarded due to a noclick event in the _X_ basis are announced publicly, and hence are known to Eve). This implies that the key rate provided in the case of inefficient detectors is an overestimation of the actual secure key rate. The security of the key is thus compromised. 

It is worth mentioning that security fixes in the case of detectors with mismatching nominal efficiencies have already been laid out, for example, in Refs. [11,12], for the BB84 protocol with an active basis choice. 

Mismatching detection probabilities can also be a result of the different ways in which the two measurement bases are constructed. For instance, Ref. [18] features a two-dimensional time-bin encoding where the key basis measurement consists of a simple time-of-arrival measurement with a single-photon detector. Conversely, the test basis measurement is realized by an unbalanced Michelson interferometer with a delay in one of its arms, thereby spreading the whole signal over the range of three time bins, followed by a detector in only one of its output ports. This fact, combined with the fact that the outer time bins overlap with the bins of the neighboring rounds, implies that about 50% of potential detections are unobserved in the test basis compared with the key basis. This violates the basis-independent detection probability assumption of the security proofs [9,10] adopted in Ref. [18]. Similarly, in the BB84 protocols implemented in Refs. [19,32], the 

test basis measurement setup includes, among other optical elements, an interferometer where only one output is detected, such that the overall efficiency is reduced compared with that of the key basis measurements. By generalizing the setup in Ref. [18], Islam _et al._ [20] use a cascade of interferometers to detect the relative phases between pulses of a four-dimensional time-bin QKD protocol. Despite presenting a detector at each output port, they discard the detections in all but the central time bin, thus reducing the detection efficiency of the test basis by 75% under nominal conditions. In such setups [18,20], an attack analogous to the one described above, where Eve adds photons when measuring in the more lossy basis, would successfully spoil the security of the established key. Therefore, measures to avoid such attacks or modified security proofs are required to restore implementation security. 

Mode-dependent detection probability mismatches depend on the coupling between the incoming light mode and each of the two measurement bases; hence, they might not emerge when the QKD experiment is operating nominally. Crucially, however, the assumption of a basisindependent detection probability must be verified not only by the experimental signals but also by any possible signal prepared by an adversary. For instance, prepare-andmeasure protocols exploiting the complementarity of time and frequency (energy) degrees of freedom [13,22–27] are particularly prone to mode-dependent detection efficiency mismatches. In these setups the key basis is typically a time-of-arrival measurement, while the test basis consists of a frequency measurement. This is done either directly with spectrometers or indirectly through group delay dispersion. In the latter case, a dispersive medium spreads out a signal with differing delays depending on its frequency components, such that from the arrival time of a dispersed signal one can infer a frequency value. Regardless of the implemented frequency measurement, the finite detection windows in time and frequency represent a vulnerability that can be exploited by an eavesdropper. Indeed, as pointed out in Refs. [13,14], Eve can intercept the signals and measure either their time or their frequency, after which she prepares a very narrow pulse in time (if she measured the time) or in frequency (if she measured the frequency) and sends it to Bob. The detection probability of such signals at Bob strongly depends on the measurement basis. In the basis opposite to Eve’s, the Fourier transform of a narrow pulse spreads out much more than the finite detection window of Bob’s apparatus, thereby decreasing the detection probability significantly. This ensures that most of the detection events are those where Bob’s choice and Eve’s choice of basis match, hence invalidating security (unless no-detection events are kept). 

Current security proofs that could account for modedependent detection probabilities are limited in scope and, more importantly, would return overly pessimistic 

044011-3 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

key rates [33–36]. In particular, the analytical proofs in Refs. [33,34] restrict Bob’s input to be a single-photon signal, while the numerical security proof in Ref. [36] allows for multiphoton states received by Bob but assumes a deterministic single-photon source used by Alice. The main limitation of such proofs, however, is that they require a prior characterization of the mode-dependent detection efficiency of both measurement bases, for any possible incoming mode. Then, the worst-case efficiency mismatch between the two bases, among all potential input modes, determines the secure key rates given in Refs. [33– 36]. Hence, the resulting key rates are overly pessimistic in all the practical scenarios where there is no eavesdropper tailoring the signals to those modes with the largest efficiency mismatch. 

In contrast, our proof can handle both modeindependent and mode-dependent detection probability mismatches, it does not confine Alice’s output or Bob’s input to the single-photon subspace, and it is applicable to time-encoded QKD protocols such as the ones discussed in this section. Moreover, it can generate significantly higher key rates than previous proofs for honest implementations of protocols that are particularly sensitive to mode-dependent detection efficiency mismatches, e.g., time-frequency QKD (see Sec. VI). 

## **III. QKD PROTOCOL** 

We consider a prepare-and-measure QKD protocol with two measurement bases and _d_ outcomes per measurement. Bob measures the states sent by Alice with a measurement apparatus that is partially characterized. Namely, we assume that the mode-independent detection efficiencies (e.g., nominal detector efficiency, coupling loss) and the dark count probabilities of both measurement bases are known. Nevertheless, an imperfect characterization of such quantities would not affect security: any deviation between the characterized values and the setup’s actual behavior will be treated by our proof as an attack attempt. Importantly, in contrast to previous proofs [33–36], we do not require a careful characterization of (possibly adversarial) mode-dependent efficiency mismatches. 

## **A. Alice’s states** 

Alice prepares states from two sets, named the “ _Z_ -basis states” and the “ _X_ -basis states,” respectively. The _Z_ -basis states are primarily used for key generation, while the _X_ -basis states are used for testing. In both bases, Alice prepares phase-randomized coherent states, as required by the decoy-state method [37–39], with three different intensities: _μ_ 1, _μ_ 2, and _μ_ 3. The three intensities satisfy _μ_ 1 _> μ_ 2 + _μ_ 3 and _μ_ 2 _> μ_ 3 ≥ 0. 

The _Z_ -basis states form the set { _ρZj_ }<sup>_d_</sup> _j_ =<sup>−</sup> 0<sup>1, where</sup> 



is the state corresponding to the _j_ th symbol of the _Z_ basis, with intensity _μi_ ( _i_ = 1, 2, 3). In Eq. (3) we defined the Fock state of _n_ photons in the mode of the _j_ th symbol, 



where _a_<sup>†</sup> _Zj_<sup>isthecreationoperator,aswellasthePoisso-</sup> nian distribution of photons typical of phase-randomized coherent states, 



The _X_ -basis states are given by { _ρXk_ }<sup>_d_</sup> _k_ =<sup>−</sup> 0<sup>1, where</sup> 



is the state corresponding to the _k_ th symbol of the _X_ basis, where | _nXk_ ⟩= _(a_<sup>†</sup> _Xk_<sup>_)n_|vac⟩</sup><sup>_/_</sup> √ _n_ ! is the Fock state of _n_ photons in the mode of the _k_ th symbol and _a_<sup>†</sup> _Xk_<sup>is the creation</sup> operator. The only requirement on the states prepared by Alice is that their single-photon components do not reveal Alice’s choice of basis to a potential eavesdropper. In other words, the average state prepared by Alice in the _Z_ and _X_ bases must coincide when restricted to the single-photon subspace [8,9]: 



This condition, satisfied by many QKD implementations (e.g., polarization, time bin), can be achieved if, for example, the two bases are linked by a discrete Fourier transform: 



## **B. Bob’s measurement** 

Bob’s measurement apparatus is schematized in Fig. 1. For concreteness, here we describe the scenario where Bob’s _Z_ -basis detector measures the time of arrival of Alice’s pulses. Nevertheless, the protocol and its proof are general and can be applied to other scenarios where Alice and Bob use different photonic degrees of freedom. 

The TBS splits the signal received by Bob into a transmitted mode and a reflected mode. The reflected mode is measured by Bob’s _Z_ -basis detector, whose outcomes form Bob’s raw key. The _Z_ -basis detector is characterized by a mode-independent, or nominal, detector efficiency _ηZ_ , which includes the insertion loss of the TBS. We indicate with _Z_ the total time window in which the detector may click in a single measurement round. The time window _Z_ 

044011-4 



<!-- Start of picture text -->
LO)<br><!-- End of picture text -->





<!-- Start of picture text -->
m mi mn<br>1} t<br>Z<br><!-- End of picture text -->

~~-~~ (yf ~~<u>)</u>~~ 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

rounds, then _Z_ would represent the set of modes that are detected by the _Z_ -basis detector. Notably, the framework and the proof we provide are still applicable, as far as the TBS can be dynamically tuned along the new degree of freedom measured in the _Z_ basis. 

In the following, we describe the generic QKD protocol, whose security is proven in Sec. IV. 

## **Protocol 1.** QKD protocol. 

(1) The following describes one measurement round of the protocol, and it must be iterated for a sufficient number of rounds. 

(a) Alice prepares a _Z_ -basis state (event _T_ = _Z_ ) with probability _pZ_ and an _X_ -basis state (event _T_ = _X_ ) with probability 1 − _pZ_ . When preparing a _Z_ -basis ( _X_ - basis) state, Alice draws the symbol _j_ ∈{0, _. . ._ , _d_ − 1} ( _k_ ∈{0, _. . ._ , _d_ − 1}) uniformly at random and records the outcome in the random variable _ZA_ ( _XA_ ). She then chooses an intensity _μi_ ∈ _S_ := { _μ_ 1, _μ_ 2, _μ_ 3} with probabilities _pμ_ 1, _pμ_ 2, and _pμ_ 3 = 1 − _pμ_ 1 − _pμ_ 2 and records it in a random variable _IA_ . On the basis of her choices, Alice prepares the phase-randomized coherent state _ρZj (μi)_ ( _ρXk (μi)_ ) given in Eq. (3) [Eq. (6)] and sends it to Bob via an insecure quantum channel. The states prepared by Alice in the two bases satisfy Eq. (7). 

(b) In each round, Bob chooses one of seven different TBS settings, namely, _(ηi_ , _η_ ↑ _)_ for _i_ = 1, 2, 3, _(ηi_ , _η_ ↓ _)_ for _i_ = 1, 2, 3, and _(η_ 2, _η_ 2 _)_ . The transmittances are chosen as _η_ 1 = _η_ ↑ and _η_ 3 = _η_ ↓, and _η_ 2 satisfies _η_ ↓ _< η_ 2 _< η_ ↑ [a close-to-optimal choice for maximizing the key rate is _η_ 2 = _(_ 1 _/_ 4 _)(_<sup>√</sup> _~~η~~_ ↓ +<sup>√</sup> _~~η~~_ ↑ _~~)~~_<sup>2</sup> ]. In particular, Bob chooses the setting _(η_ ↓, _η_ ↓ _)_ with probability _pZ_ or one of the other six settings with probability _(_ 1 − _pZ)/_ 6 each.If the _Z_ -basis detector ( _X_ -basis detector) clicks and returns outcome _j_ ( _k_ ), Bob sets _ZB_ = _j_ ( _XB_ = _k_ ). Otherwise, if the _Z_ -basis detector ( _X_ -basis detector) does not click, Bob sets _ZB_ = ∅ ( _XB_ = ∅). 

(2) Public announcements: For each round, the parties announce the following information over an authenticated public channel. Alice announces the type of round she performed ( _T_ ) and her intensity choice ( _IA_ ), while Bob announces the TBS setting and whether the _Z_ -basis detector clicked ( _ZB_ = ∅) or did not click ( _ZB_ = ∅). The parties label the rounds where _T_ = _Z_ and _ZB_ = ∅, and Bob selects the TBS setting _(η_ ↓, _η_ ↓ _)_ as “key generation rounds,” while the other rounds are labeled as “test rounds.” For the test rounds, Bob additionally announces _XB_ over the public channel. 

(3) Gain estimation: From the information announced, the parties estimate the _Z_ -basis gains: 

for each _μj_ ∈ _S_ and _ηl_ ∈{ _η_ ↑, _η_ 2, _η_ ↓}. They also estimate the _X_ -basis gains: 



for _μj_ ∈ _S_ and for _ηi_ ∈{ _η_ ↑, _η_ 2, _η_ ↓} and _ηl_ ∈{ _η_ ↑, _η_ ↓}. (4) Error estimation: Bob reveals _ZB_ for a subset of the key generation rounds in order for Alice to compute the QBER of the key generation rounds, for each intensity chosen by Alice: 



Alice also computes the QBERs of the test rounds with a detection in the _X_ -basis detector ( _X_ -basis QBERs): 











for _ηi_ ∈{ _η_ ↑, _η_ 2, _η_ ↓} and _μj_ ∈ _S_ . 

(5) Classical postprocessing: The parties, by performing error correction and privacy amplification, extract a shared secret key from the variables _ZA_ (for Alice) and _ZB_ (for Bob) relative to the key generation rounds where Bob did not reveal _ZB_ . The fraction of shared secret key bits established per protocol round, in the asymptotic limit of infinitely many rounds, is given by 



and is called the “asymptotic key rate” of the protocol. Below we define the quantities appearing in the key rate expression. 

_G_<sup>_Z_</sup> _μj_ , _(ηl_ , _ηl)_<sup>= Pr</sup><sup>_(ZB_= ∅|</sup><sup>_T_=</sup><sup>_Z_,</sup><sup>_IA_=</sup><sup>_μj_,</sup><sup>_(ηl_,</sup><sup>_ηl))_(11)</sup> 

044011-6 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

We define the compatibility coefficient _c_ of Alice’s states in the one-photon subspace [8]: 



where _S_<sup>−1</sup> is the generalized inverse of _S_ (the inverse on its support), with _S_ given in Eq. (7). The key rate is maximal when the compatibility coefficient is minimal (i.e., _c_ = 1 _/d_ ), and this occurs if Alice’s states, in the onephoton subspace, form two mutually unbiased sets (the proof is given in Remark C1 in Appendix C): 



In turn, the condition in Eq. (19) can be obtained, for example, by combining the discrete Fourier transform (8) with the orthogonality of the states in one basis (⟨1 _Zj_ |1 _Zj_ ′ ⟩= _δj_ , _j_ ′). 

The function _u(x)_ appearing in Eq. (17) is defined as 



with _h(x)_ = − _x_ log2 _x_ − _(_ 1 − _x)_ log2 _(_ 1 − _x)_ the binary entropy. 

One of the main results of this paper is the derivation of the upper bound on the phase error rate of the protocol, _e_ ˜ _X_ ,1. Because of its cumbersome expression, we report it in Appendix B as a function of (bounds on) the yields and test-round bit error rates. 

Finally, _Yn_<sup>_Z_</sup> , _(ηl_ , _ηl)_ denotes a statistical lower bound on the _n_ -photon yield in the _Z_ basis, i.e., the probability of a _Z_ - basis detector click given that Alice sent _n_ photons and Bob chose the TBS setting _(ηl_ , _ηl)_ . The explicit expressions for _Y_ 1,<sup>_Z_</sup> _(η_ ↓, _η_ ↓ _)_ , _Y_ 0,<sup>_Z_</sup> _(η_ ↓, _η_ ↓ _)_ , and of all the other bounds 

on the yields and bit error rates that appear in _e_ ˜ _X_ ,1 are due to the decoy-state method and are reported in Appendix D. 

For a complete overview of the notation and quantities defined in this paper, we refer the reader to Appendix A. 

## **IV. SECURITY PROOF** 

We analytically prove the asymptotic security of Protocol 1 under collective attacks by the eavesdropper, thereby deriving the key rate expression in Eq. (17). Security against coherent attacks cannot be directly inferred by one invoking de Finetti-type results (e.g., postselection technique [42,43]). Indeed, such results require a reduction to finite dimensions, which contrasts with the generality of our approach (Bob can receive states in an infinite number of different optical modes). 

Unlike standard QKD security proofs [8–10], our proof does not rely on the assumption that the detection probability of the key generation measurement and of test measurement coincide for every input state. We allow Eve to add photons to Alice’s single-photon pulses or prepare states in continuous degrees of freedom (e.g., time, frequency) [44,45], such that the detection probability of Eve’s states depends on the measurement basis. Such attacks might not manifest themselves in asymmetric gains observed in an experiment, as Eve might be able to conceal her attack by acting symmetrically on both bases. Existing proofs [33–36] accounting for detection efficiency mismatches require, at the very least, that mode-dependent mismatches are fully characterized and known _a priori_ . 

The security proof presented here can avoid such a characterization by actively estimating the relevant quantities from the rich statistics generated with the TBS. More specifically, it uses the decoy-state method [37–39] to focus on the rounds where Alice sends exactly one photon. In parallel, it uses the TBS to apply the detector decoy technique [28] and estimate the photon number distribution of Bob’s input states. Finally, it can estimate possible mode-dependent mismatches in the detection efficiency of the two measurement bases, thus not requiring their prior characterization. 

In the following, we provide a simplified version of the security proof highlighting the steps that set it apart from previous proofs. The proof in full detail is reported in Appendix C. 

_Proof._ According to the description of Protocol 1 in Sec. III, the parties extract the shared secret key from the rounds labeled as key generation rounds, where Alice sends a _Z_ -basis state, Bob selects the TBS setting _(η_ ↓, _η_ ↓ _)_ , and the _Z_ -basis detector clicks. We label the intersection of these three events with _�Z_ . ■ 

The asymptotic secret key rate that can be extracted from the events _�Z_ , under collective attacks, is lowerbounded by the Devetak-Winter (DW) rate [46]: 



where _H (ZA_ | _IAE)_ and _H (ZA_ | _IAZB)_ are von Neumann entropies computed on the state shared by Alice, Bob, and Eve in a generic round, conditioned on the event _�Z_ . This state is explicitly derived in Appendix C 1. Note that we can express 



The goal of the proof is to show that the key rate given in Eq. (17) is a lower bound of Eq. (21). 

The second entropy in Eq. (21) quantifies Bob’s uncertainty about Alice’s key bit _ZA_ and represents the information leakage of an optimal error correction scheme. 

044011-7 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

In Appendix C 2 we show how to bound this term with standard arguments in terms of the QBERs of the key generation rounds, Eq. (14), as follows: 



where the function _u(x)_ is defined in Eq. (20) and the gain _G_<sup>_Z_</sup> _μj_ , _(η_ ↓, _η_ ↓ _)_<sup>is obtained as explained in step 3 of Protocol 1.</sup> The remainder of the proof is devoted to deriving a lower bound on the first entropy in Eq. (21) in terms of observed statistics. 

The first step consists in discarding the contributions to _H (ZA_ | _IAE)ρ_ | _�Z_ relative to the rounds where Alice sends more than one photon to Bob. This is because such rounds are vulnerable to photon-number-splitting attacks [47] and hence cannot lead to shared secret bits. We show in Appendix C 3 a that the following inequality holds: 



where _Yn_<sup>_Z_</sup> , _(ηl_ , _ηl)_ is the _n_ -photon _Z_ -basis yield (see Appendix A), i.e., the probability that the _Z_ -basis detector clicks, given that Alice sent _n_ photons encoded in a _Z_ - basis state and Bob selected the TBS setting _(ηl_ , _ηl)_ , while _H (ZA_ | _E)ρ_ |1, _�Z_ is the entropy conditioned on a key generation round where Alice sent exactly one photon. Note that the conditional entropy is maximal when Alice sends the vacuum, _H (ZA_ | _E)ρ_ |0, _�Z_ = log2 _d_ , since Eve cannot be correlated to Alice’s symbol when Alice sends the vacuum. 

The next step, which is detailed in Appendix C 3 b, uses the uncertainty relation for von Neumann entropies [48–51] to derive a lower bound on the entropy _H (ZA_ | _E)ρ_ |1, _�Z_ . In particular, thanks to the condition on Alice’s states in the one-photon subspace (7), we can equivalently describe a key generation round in the entanglement-based picture. That is, there exists an entangled state | _�τ_ ⟩ _AB_ , given by the purification of the state _τB_ = _S/d_ with _S_ in Eq. (7), and two fictitious measurements for Alice, called “Alice’s _Z_ -basis measurement” and “Alice’s _X_ -basis measurement” [8]. Then, Bob’s conditional state, when Alice performs the _Z_ -basis measurement ( _X_ -basis measurement) on system _A_ of | _�τ_ ⟩ _AB_ and obtains outcome _ZA_ = _j_ ( _XA_ = _k_ ), coincides with the state |1 _Zj_ ⟩ (|1 _Xk_ ⟩) sent to Bob in Protocol 1 when Alice draws the symbol _ZA_ = _j_ ( _XA_ = _k_ ) and sends one photon [recall that Alice prepares probabilistic mixtures of Fock states with a Poissonian distribution, Eq. (3)]. 

We recall that the entropy _H (ZA_ | _E)ρ_ |1, _�Z_ is computed on the state of a key generation round, i.e., the state received 

by Bob and postselected on a detection by the _Z_ -basis detector with TBS setting _(η_ ↓, _η_ ↓ _)_ . Hence, we update the state | _�τ_ ⟩ _AB_ to the following entangled state: 



where _UBE_ is a unitary applied by Eve, jointly on Bob’s system and Eve’s system _E_ , describing her collective attack, while _Z_ ✓ is the positive operator–valued measure (POVM) element corresponding to a detection of a key generation round, i.e., a detection by the _Z_ -basis detector with TBS setting _(η_ ↓, _η_ ↓ _)_ . The denominator in the last expression ensures normalization. In this way, by applying the uncertainty relation on | _�_ ⟩ with Alice’s two fictitious measurements, we obtain 



where _c_ is given in Eq. (18) and where the entropy on the left-hand side is computed on the state | _�_ ⟩ after Alice’s _Z_ -basis measurement, which results in the entropy that needs to be bounded in Eq. (24). The entropy on the right-hand side is computed on the state | _�_ ⟩ after Alice’s _X_ -basis measurement, which reads 



where _σk_ is the state received by Bob when Alice sends the one-photon _X_ -basis state relative to symbol _XA_ = _k_ : 



The state in Eq. (27) is properly normalized thanks to Eq. (7). 

We can now focus on deriving an upper bound on the entropy _H (XA_ | _B)σ_ appearing in Eq. (26). Since the entropy _H (XA_ | _B)σ_ is conditioned on a quantum system, system _B_ , we can apply a measurement map on system _B_ such that the resulting conditional Shannon entropy can be estimated with measurement statistics. To this aim, we first define Bob’s test measurement by the POVM: { _X_ 0, _X_ 1, _. . ._ , _Xd_ −1, _X_ ∅}, with _Xk_ the POVM element describing the detection of outcome _XB_ = _k_ by the _X_ -basis detector, with TBS setting _(η_ ↑, _η_ ↑ _)_ . We can also define _X_ ✓ =<sup>�</sup><sup>_d_</sup> _k_ =<sup>−</sup> 0<sup>1</sup><sup>_Xk_tobethePOVMelementcorresponding</sup> to a detection and _X_ ∅ = 1 − _X_ ✓ to be the POVM element corresponding to no detection. Then we consider the 

044011-8 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

measurement map 



where { _X_<sup>˜</sup> _k_ ′}<sup>_d_</sup> _k_<sup>′−</sup> =<sup>1</sup> 0<sup>isaPOVMdefinedfromBob’stestmea-</sup> surement as follows: 



with _(_<sup>~~√~~</sup> _X_ ✓ _)_<sup>−1</sup> the inverse of<sup>~~√~~</sup> _X_ ✓ over its support and 1<sup>⊥</sup> _X_ ✓<sup>the projector on the complement of the support of</sup><sup>_X_✓.</sup> Then, by applying the measurement map (29) on system _B_ of Eq. (27), the following inequality holds [52]: 



where in the second inequality we used Fano’s inequality and defined the phase error rate 



We can now lower-bound the Devetak-Winter rate in Eq. (21) by plugging in Eqs. (23) and (24), where we further bound the latter using Eq. (26) and subsequently Eq. (31). This leads to the following expression: 



where we used Eq. (22) to replace Pr _(�Z)_ and replaced the _Z_ -basis yields with their respective lower bounds, obtained with the decoy-state method [see Eqs. (D23) and (D28)]. 

The remainder of the proof is devoted to deriving a meaningful upper bound on the phase error rate, Eq. (32), in terms of the statistics collected in the test rounds. Indeed, the fact that _u(x)_ given in Eq. (20) is a monotonically nondecreasing function implies that the upper bound can be used to replace _e_ ˜ _X_ ,1 in Eq. (33) and obtain another lower bound on the DW rate. 

In standard QKD security proofs [8,9] it is assumed that the detection probability of Bob’s key generation measurement is equal to the detection probability of Bob’s test measurement, for every input state. Mathematically, 

this amounts to an equality between the POVM elements corresponding to a detection in the two measurements: 



By combining the assumption in Eq. (34) with Eq. (30), we find that the phase error rate reduces to the one-photon bit error rate of Bob’s test measurement, as we derive explicitly in Appendix C 3 c: 



which can be readily estimated with the decoy-state method. The challenge in the more general setting addressed by this paper is to estimate the phase error rate when Eq. (34) is not assumed to hold. 

## **A. Phase error rate estimation** 

Here we briefly sketch the main ideas behind the estimation of the phase error rate. The full argument can be found in Appendix C 4, starting with a detailed overview of the main steps in Appendix C 4 a. 

The first step in estimating the phase error rate in Eq. (32) consists in reducing the calculation to the subspace containing at most one photon in the set of modes _Z_ detected by the _Z_ -basis detector. We call this the “(≤ 1)subspace.” The detailed description of this step is deferred to Appendixes C 4 b–C 4 e and C 4 j. Indeed, we expect most of the state _σ_ ¯ , 



which is the average state received by Bob when Alice sends one photon, to lie in the (≤ 1)-subspace in an honest implementation of the protocol [53]. The reduction to the (≤ 1)-subspace leads us to the following upper bound, reported in Eq. (C103): 



In the last expression,weight of the state _σ_ ¯ outside the _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1denotes an upper bound on the</sup> _(_ ≤ 1)-subspace, 



with _�_<sup>_α_</sup> _Z_<sup>beingtheprojectorontothesubspacecontain-</sup> ing _α_ photons in the set of modes _Z_ . _�_ 2 is a function of 

044011-9 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

both _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1and</sup><sup>_Y_</sup> 1,<sup>_Z_</sup> _(η_ ↓, _η_ ↓ _)_<sup>andisderivedinEq.(C248).The</sup> operator _MZ_<sup>≤1is defined as</sup> 



(see Appendixes C 4 f–C 4 j): 



where the probability _p_ ✓| _α_ is defined in Eq. (C181). Similarly to _�_<sup>_α_</sup> _Z_<sup>forthe</sup><sup>_Z_-basisdetector,weintroducedthe</sup> projector _�_<sup>_β_</sup> _X_<sup>thatprojectsonthesubspacewith</sup><sup>_β_pho-</sup> tons in the set of modes _X_ . Finally, _ηr_ = _ηX /ηZ_ is the ratio between the detector efficiencies of the two bases (by assumption _ηr_ ≤ 1) and _pd_<sup>_X_is the total probability of a dark</sup> count in the _X_ -basis detector. 

The remainder of the proof derives upper bounds on the first two terms on the right-hand side of Eq. (37) by using the detection statistics of the different TBS settings and by solving systems of linear equations. For the first term, the ~~0 0~~ ,1 solution of a linear system yields the variables E _η_ ↑<sup>,</sup> E _η_ ↑<sup>,</sup> ~~1~~ _t_ ~~1~~ _r_ E E _η_ ↑<sup>, and</sup> _η_ ↑<sup>and allows us to derive the following bound</sup> 

The second term in Eq. (37), in turn, is upper-bounded via 



0 1 where the quantities ~~�~~ _w_<sup>0</sup> _X_ ~~�~~ _Z_<sup>and</sup> ~~�~~ _w_<sup>0</sup> _X_ ~~�~~ _Z_<sup>arederived</sup> with the detector decoy technique. The full derivation is reported in Appendixes C 4 k and C 4 l. 

By inserting the bounds (40) and (41) into Eq. (37), we arrive at the final upper bound on the phase error rate, _e_ ˜ _X_ ,1 ≤ _e_ ˜ _X_ ,1, where 



Each quantity in the last expression is either known or directly expressed in terms of observed statistics via the relations given in Appendix B. In Appendix D, the formulas for the bounds on the yields are derived with the use of the decoy-state method. 

By using the bound (42) in the key rate expression (33), we recover the asymptotic key rate of the protocol, Eq. (17), thus demonstrating that it is a lower bound of the DW rate in Eq. (21). This concludes the proof. 

## **V. SIMULATIONS** 

In this section we analyze the performance of our security proof on an experimental four-dimensional time-bin QKD protocol (Protocol 1), both in the case of an honest implementation (Sec. V A) and under an attack where Eve can partially control the detection probabilities of the two bases (Sec. V B). We benchmark the key rate resulting 

from our proof (17) with the asymptotic key rate of the standard decoy-BB84 protocol, with four outcomes per basis, which implicitly assumes basis-independent detection probabilities. 

## **A. High-dimensional time-bin QKD** 

We first consider an honest implementation of the protocol, without any attack in the quantum channel. 

In the experimental setup in Refs. [29,30], Alice prepares _d_ = 4 mutually orthogonal time bins for key generation, while the testing symbols are encoded in the relative phases between such pulses. In particular, if _a_<sup>†</sup> _Zj_<sup>is the cre-</sup> ation operator of one photon in the _j_ th time bin mode, the creation operators of the testing modes are given by the discrete Fourier transform of the time bin modes (8), such that the condition in Eq. (7) is satisfied and the compatibility coefficient of Alice’s states is _c_ = 1 _/_ 4. Alice prepares the 

044011-10 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

pulses in both bases as phase-randomized coherent states, given by Eq. (3) for the _Z_ basis and Eq. (6) for the _X_ basis, with intensities _μ_ 1, _μ_ 2 = 2 _μ_ 3, and _μ_ 3 = 10<sup>−6</sup> (note that weak decoy intensities are optimal). In the asymptotic limit, the optimal number of test rounds is negligible, and hence we set _pZ_ = 1 and _pμ_ 1 = 1. 

Bob’s measurement apparatus is described in Sec. III B, where the _Z_ -basis measurement is realized with a single detector that detects the arrival time of the pulse, while the _X_ -basis measurement is implemented by a dispersive medium followed by a time-of-arrival detection. From the arrival time of the dispersed signal, it is possible to infer the relative phases in the superposition of time bins sent by Alice in the test rounds. More details on Bob’s _X_ - basis measurement can be found in Refs. [29,30]. We set the largest and smallest transmittance allowed by the TBS to _η_ ↑ = 0.9 and _η_ ↓ = 0.1, respectively, such that Eq. (9) is satisfied. We also fix _η_ 2 = _(_ 1 _/_ 4 _)(_<sup>√</sup> _~~η~~_ ↓ +<sup>√</sup> _~~η~~_ ↑ _~~)~~_<sup>2</sup> = 0.4. We fix the insertion loss of the TBS and of the dispersive medium to 1 dB each, while the efficiency of the two detectors is 0.9. Thus, we have _ηZ_ = 0.9 × 10<sup>−1</sup><sup>_/_10</sup> and _ηX_ = _ηZ_ × 10<sup>−1</sup><sup>_/_10</sup> , such that Eq. (10) is satisfied. Finally, the dark count probability of the _Z_ -basis detector ( _X_ -basis detector) in the whole detection window is _pd_<sup>_Z_= 10−4</sup> ( _pd_<sup>_X_= 1.2 × 10−4, due to a longer detection window).</sup> 

We adopt a simple channel model where Alice’s pulses go through a bosonic channel with transmittance _η_ , such that the pulses arriving at Bob are completely contained in the detection window _Z_ used for key generation measurements (see Fig. 2). Moreover, we choose the duration of the detection window of the _X_ -basis detector to be longer than in the _Z_ basis and long enough such that a negligible fraction of the dispersed signal (i.e., the signal exiting the dispersive medium) falls outside the detection window. We avoid modeling noise sources and instead assume that the signals arriving at Bob carry an intrinsic QBER _qZ_ ( _qX_ ) in the _Z_ basis ( _X_ basis). Therefore, the QBERs observed in the protocol, namely, _QZ_ , _μj_ , _QX_ , _μj_ , _(ηi_ , _η_ ↑ _)_ ,✓, and _QX_ , _μj_ , _(ηi_ , _η_ ↑ _)_ ,∅, are the result of the intrinsic QBERs and of the dark counts in the detectors. We report the explicit formulas used for the gains and QBERs in Appendix E 1. 

Using this channel model, in Fig. 3 we investigate the adaptability of our proof to different noise scenarios by computing the maximal tolerable channel loss, such that a positive secret key rate is obtained with Eq. (17) for various intrinsic QBERs _qX_ and _qZ_ . We observe that our proof can tolerate up to 30 dB of loss and is resilient to noise, especially in the test basis. For example, for _qZ_ = 2% and 20 dB loss, we can extract a positive key rate for test-basis QBERs up to _qX_ ≈ 16%. By virtue of the considered honest implementation, different detection probabilities for the two bases are caused only by mode-independent asymmetries in the efficiencies and dark count probabilities of the two detectors ( _ηZ_ = _ηX_ , _pd_<sup>_Z_=</sup><sup>_p_</sup> _d_<sup>_X_).Still,theycouldbe</sup> exploited by an attacker, as discussed in Sec. II. The key 



<!-- Start of picture text -->
0 . 10 30<br>25<br>0 . 08<br>20<br>0 . 06<br>15<br>0 . 04<br>10<br>0 . 02<br>5<br>0 . 00 0<br>0 . 00 0 . 05 0 . 10 0 . 15 0 . 20 0 . 25 0 . 30<br>qX<br>FIG. 3. Maximal tolerable channel loss for a positive key<br>rate of a four-dimensional time-bin QKD protocol with nom-<br>inal detection efficiency mismatch ηX /ηZ = 10 −1 / 10 for vari-<br>ous channel-intrinsic QBERs qZ (key generation basis) and qX<br>(test basis). The key rate is the one obtained from our proof,<br>Eq. (17), and is optimized over the pulse intensity μ 1. Fur-<br>thermore, we fix the decoy intensities μ 2 = 2 μ 3 = 2 × 10 −6 ,<br>the detectors’ mode-independent efficiencies  ηZ = 0.9 × 10 −1 / 10<br>and  ηX =  ηZ × 10 −1 / 10 , the TBS parameters  η ↑ = 1 − η ↓ = 0.9<br>and η 2 = 0.4, and the dark count probabilities pd X = 1.2  p d Z =<br>1.2 × 10 −4 .<br>20<br>dB<br>15<br>dB<br>10<br>dB<br>0<br>dB<br>5<br>dB<br>in (dB)<br>η<br>Z<br>q<br>Maximal channel loss<br><!-- End of picture text -->

rate we provide in Eq. (17) allows for asymmetric detection probabilities and is secure even when the asymmetries are exploited or caused by an adversary. Conversely, the standard decoy-BB84 key rate for _d_ -dimensional encoding [19], 



is derived under the assumption that the detection probability in the two bases coincides for every input state, i.e., that Eq. (34) holds. This effectively results in replacing the phase error rate upper bound in our rate, _e_ ˜ _X_ ,1, with an upper bound on the bit error rate in the test basis, _<u>eX</u>_ ,1. However, the experimental setup considered [30] violates the assumption in Eq. (34) due to mode-independent (and potentially mode-dependent) asymmetries, implying that the decoy-BB84 key rate (43) cannot be applied to distill secure keys. 

Nevertheless, in Fig. 4 we benchmark the performance of the key rate from our proof, Eq. (17), with the key rate in Eq. (43), where _d_ = 4, for the honest implementation described above. Note that the TBS is not required by the security proof underlying Eq. (43). Hence, when computing the key rate via Eq. (43), we use only the TBS settings _(η_ ↑, _η_ ↑ _)_ and _(η_ ↓, _η_ ↓ _)_ to select the _X_ and _Z_ basis, respectively. The explicit expressions for the quantities appearing 

044011-11 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 



<!-- Start of picture text -->
Decoy BB84 ( qX = 0 . 02)<br>10 − 1 This work ( qX = 0 . 02)<br>Decoy BB84 ( qX = 0 . 3)<br>This work ( qX = 0 . 3)<br>10 − 2<br>10 − 3<br>10 − 4<br>10 − 5<br>5 10 15 20 25 30<br>η (dB)<br>(key bits per pulse)<br>∞<br>r<br><!-- End of picture text -->

FIG. 4. Comparison of the secret key rate from our proof [Eq. (17), solid lines] with the decoy-BB84 key rate [Eq. (43), dashed lines] as a function of the channel loss _η_ , for an honest implementation of a four-dimensional time-bin QKD protocol with nominal detection efficiency mismatch _ηX /ηZ_ = 10<sup>−1</sup><sup>_/_10</sup> . We set _qZ_ = 0.02 and fix different values of the intrinsic testbasis QBER, _qX_ . All key rates are optimized over the intensity _μ_ 1. We further fix the decoy intensities _μ_ 2 = 2 _μ_ 3 = 2 × 10<sup>−6</sup> , the detectors’ mode-independent efficiencies _ηZ_ = 0.9 × 10<sup>−1</sup><sup>_/_10</sup> and _ηX_ = _ηZ_ × 10<sup>−1</sup><sup>_/_10</sup> , the TBS parameters _η_ ↑ = 1 − _η_ ↓ = 0.9 and _η_ 2 = 0.4, and the dark count probabilities _pd_<sup>_Z_= 10−4and</sup> _pd_<sup>_X_= 1.2 × 10−4.Inthishonestimplementation,thedetection</sup> mismatch is mode independent and is caused only by different dark count rates and different nominal detection efficiencies for the two measurement bases. Even in this case, the decoyBB84 key rate would not be applicable as it does not contemplate detection efficiency mismatches. 

in Eq. (43) are reported in Appendix E 1. We observe that our key rate presents a gap to the decoy-BB84 key rate and that the gap widens for larger values of the QBER _qX_ . 

## **B. Attack-induced efficiency mismatch** 

We now consider an adversarial implementation of the four-dimensional time-bin QKD protocol (Protocol 1). Eve’s attack could exploit one of the two vulnerabilities of the protocol, namely, the nominal detection efficiency mismatch between the two bases ( _ηZ > ηX_ ) or a detection probability asymmetry induced by tailored light modes. An attack based on the first vulnerability was illustrated in Sec. II, and it involves adding photons to the one-photon signals sent from Alice. This would cause an increase of the gain of the lossier basis and could be noticed by Alice and Bob when compared with the gain in other runs where Eve is not present. Nevertheless, the standard decoy-BB84 key rate does not account for asymmetric nominal efficiencies, and hence the attack would be successful. 

In this section, we consider the second vulnerability and devise an intercept-resend attack where the eavesdropper can actively control which basis clicks with tailored light pulses. In particular, in each round, with probability _wZ_ 

( _wX_ ), Eve replaces the quantum channel with an apparatus that intercepts Alice’s pulse and measures it in the _Z_ basis ( _X_ basis), such that the measurement can perfectly distinguish Alice’s states when Alice’s and Eve’s bases coincide. Then, Eve prepares a highly localized one-photon pulse in the time domain (frequency domain), with width parametrized by _s_ ( _σ_ ), which corresponds to the outcome she observed, and sends it through a quantum channel with transmittance _ξZ_ ( _ξX_ ) to Bob. If Bob measures the pulse with the same basis as Eve, his outcome is almost perfectly correlated with Eve’s. Otherwise, when Bob measures in the opposite basis, the outcome is approximately uniformly random and the detection probability is reduced. For example, if Eve intercepts the signal in the _Z_ basis and Bob measures it in the _X_ basis, her time-localized pulse would be stretched by the dispersive medium over a large time interval such that only a fraction of the outgoing pulse is contained in the detection window of the _X_ -basis detector, thereby decreasing the detection probability in the _X_ basis. Moreover, the portion of the stretched signal within the detection window of the _X_ -basis detector is nearly constant in amplitude, such that every outcome is approximately equally likely. When Eve does not perform the attack, we adopt the channel model from Sec. V A, where Alice and Bob are linked by a channel with transmittance _η_ and intrinsic QBERs given by _qZ_ = _qX_ = 0.05 (these values are chosen for comparison purposes and do not reflect currently experimentally achievable values). In Appendix E 2 we detail Eve’s attack and the corresponding statistics observed by Alice and Bob. 

To investigate the performance of our proof under the described attack, we assume that Alice is equipped with a deterministic single-photon source (note that this assumption is also made, for example, in Ref. [36]). Therefore, the decoy-state method becomes superfluous, and the key rate of Protocol 1 in Eq. (17) simplifies to the following expression (for _c_ = 1 _/d_ ): 



where the one-photon yield _Y_ 1,<sup>_Z_</sup> _(η_ ↓, _η_ ↓ _)_<sup>andtheone-photon</sup> error rate in the _Z_ basis _eZ_ ,1, _(η_ ↓, _η_ ↓ _)_ are directly observed quantities, replacing the corresponding gains and QBERs. By our removing the decoy-state method, the upper bound on the phase error rate _e_ ˜ _X_ ,1 reduces to a simpler expression, as discussed in Appendix E 2. Similarly, when we assume there is a deterministic single-photon source, the decoyBB84 protocol reduces to the original BB84 protocol, with key rate given by 



044011-12 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

From Fig. 5, we observe that Eve’s attack cannot be completely concealed from the BB84 protocol, as its key rate decreases for increasing _wZ_ . However, the BB84 key rate surpasses the upper bound on the extractable key rate starting from _wZ_ ≈ 0.27, while our key rate remains well below it. This shows that the BB84 protocol cannot fully grasp the extent of the information gained by Eve, returning an overly optimistic and, crucially, insecure key rate. 



<!-- Start of picture text -->
10 0<br>10 − 1<br>This work<br>BB84<br>Upper bound<br>10 − 2<br>0 . 1 0 . 2 0 . 3 0 . 4 0 . 5 0 . 6<br>wZ<br>(key bits per pulse)<br>∞<br>r<br><!-- End of picture text -->

## **VI. DISCUSSION** 

In Fig. 4, we highlighted a gap between our key rate (17) and the decoy-BB84 key rate (43) for the honest implementation of a four-dimensional time-bin QKD protocol. The gap is related to differing nominal efficiencies for the two measurement bases, i.e., _ηr_ = _ηX /ηZ <_ 1, which could be exploited by an attacker. Intuitively, however, the key rate should not penalized by asymmetric nominal efficiencies, unless an attacker is actively exploiting the asymmetry, as illustrated in Sec. II. The attack would entail adding photons to the signal resent to Bob, which would result in an increase of the weight of the state received by Bob in the subspace with more than one photon in the _Z_ - basis detection interval, _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1.Thisparameterisotherwise</sup> null in an honest implementation without flaws, since it refers to the subset of one-photon signals sent by Alice. 

FIG. 5. Comparison of the secret key rate derived in this work [Eq. (44), solid blue line] with the BB84 key rate [Eq. (45), dashed blue line] and with an upper bound on the achievable key rate [Eq. (E45), solid red line] as a function of the probability that Eve intercepts the signal and measures it in the _Z_ basis (the key basis). All key rates are obtained under the assumption of a deterministic single-photon source (no decoys). With this attack, Eve can partially steer which basis clicks in each round to match the basis she measured in. The result is that the BB84 key rate, which does not account for attack-induced detection efficiency mismatches, overestimates the fraction of secret bits and surpasses the upper bound on the secret key rate, while the key rate from our proof remains below it. The plot parameters are as follows: number of symbols _d_ = 4, intrinsic QBERs in the channel without Eve _qZ_ = _qX_ = 0.05, detectors’ mode-independent efficiencies _ηZ_ = 9 _/_ 10 × 10<sup>−1</sup><sup>_/_10</sup> and _ηX_ = 10<sup>−1</sup><sup>_/_10</sup> _ηZ_ , TBS settings _η_ ↑ = 1 − _η_ ↓ = 0.9 and _η_ 2 = 0.4, dark count probabilities _pd_<sup>_Z_= 10−4 and</sup><sup>_p_</sup> _d_<sup>_X_= 1.2 × 10−4, and channel loss of 1 dB,</sup><sup>_η_=</sup> 10<sup>−1</sup><sup>_/_10</sup> . We partition the detection window of _�t_ = 1.132 ns in the _Z_ basis into four time bins of width _�j_ = 0.283 ns. Likewise, _�f_ = 4 × _�k_ = 4 × 0.340 ns in the _X_ basis. The group delay dispersion coefficient _�_ 2 of the dispersive medium is fixed to 0.01275 ns<sup>2</sup> . See Appendix E 2 b for how these parameters enter the key rates. 

In Appendix E 3, we show that our key rate is indeed insensitive to _ηr_ —and matches the decoy-BB84 key rate—-for honest implementations with asymmetric nominal efficiencies provided that we impose _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1= 0. In other</sup> words, when we impose that _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1matchesitstruevalue</sup> for honest implementations, our key rate confirms the intuition that asymmetric nominal efficiencies do not influence the resulting key rate. We emphasize that this conclusion could not have been drawn from the decoy-BB84 rate since it does not apply to scenarios with _ηr <_ 1. Conversely, when using the estimation for _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1derivedinourproof</sup> [see Eq. (B5)], we observe that our key rate decreases as the asymmetry in the detection efficiency of the two bases increases ( _ηr_ decreases), generating the gap to the decoy-BB84 key rate. Therefore, the gap in Fig. 4 can be attributed to a nontight estimation of the parameter _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1</sup> with the bound (B5) and could be improved by deriving tighter bounds. 

where the phase error rate bound is replaced by the observed one-photon error rate in the _X_ basis _eX_ ,1, _(η_ ↑, _η_ ↑ _)_ . 

In Fig. 5, we plot the key rates in Eqs. (44) and (45) as a function of the probability of attacking the key basis, _wZ_ . For each value of _wZ_ , we optimize the parameters of Eve’s attack ( _wX_ , _s_ , _σ_ , _ξZ_ , _ξX_ ) such that the statistics observed by Alice and Bob in the BB84 protocol remain approximately equal to those in the scenario without attack. The intention is that of concealing Eve’s attack when the parties run the standard BB84 protocol. Additionally, we plot an upper bound on the secret key rate that Alice and Bob can extract (the full derivation is presented in Sec. E 2). This is obtained by subtracting from Alice’s raw key the number of bits known to Eve, which come from the rounds where Eve correctly guesses Alice’s basis and from public error correction information. 

A strong indication of how to improve the bound on the parameter _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1comesfromFig.5,whereweobserve</sup> that our key rate matches the BB84 key rate for _wZ_ = 0, i.e., in an honest implementation where Alice uses a deterministic single-photon source. In such an implementation, the yields and one-photon error rates are directly observed quantities, rather than being estimated with the decoy-state method. One of consequences is that the formula (B5) for _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1returnsthetruevalue,zero(seeAppendixE 2),</sup> allowing our key rate to match the BB84 key rate. This 

044011-13 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

suggests that increasing the number of decoy intensities (we assumed two decoy intensities in Protocol 1) may improve the estimation of _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1andreducethegaptothe</sup> decoy-BB84 key rate for honest implementations. 

We already remarked that the standard BB84 protocol is not applicable to scenarios with asymmetric detection efficiencies, regardless of their being nominal or induced by the adversary. However, for the honest implementation in Fig. 4, the decoy-BB84 key rate represents de facto the largest amount of key that can be securely extracted, by matching our key rate when setting _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1= 0.Thisisnot</sup> the case for the attack corresponding to Fig. 5. The BB84 rate overestimates the fraction of secret key bits that can be extracted, by surpassing the upper bound on the secret key rate. Remarkably, when Eve attacks in the key basis 50% of the time ( _wZ_ = 0.5), the BB84 key rate certifies more than 10% of secret bits per pulse when in reality no secure key can be extracted. This is caused by the nature of the attack we designed, where Eve can increase the fraction of rounds where she learns the key bits (increasing _wZ_ ) without proportionately increasing her footprint: the _X_ -basis error rate remains approximately constant. This is achieved by Eve preparing highly time-localized pulses when attacking in the _Z_ basis ( _s_ ≈ 0.017 _�j_ ), such that their detection probability in the _X_ basis is about 4.6 times less likely than in the same basis as Eve’s. From the optimization, we observe that also attacking in the _X_ basis, i.e., _wX >_ 0, benefits the concealing of Eve’s attack. In this case, Bob’s _Z_ basis clicks with a probability reduced by a factor of about 2.3 compared with the _X_ basis. The result is that the vast majority of Bob’s _X_ -basis detections are events where either Eve attacks in the same basis or does not attack, thereby keeping the _X_ -basis error rate low. 

Crucially, the augmented statistics enabled by the TBS allow our proof to detect Eve’s actions and reduce the key rate accordingly. Indeed, our key rate never surpasses the key rate upper bound in Fig. 5 and, curiously, presents a similar scaling with respect to _wZ_ . In other words, our security solution is capable of reducing the extractable key rate in proportion to the extent of adversarial attacks inducing asymmetric detection efficiencies in a given protocol run. This feature sets our proof apart from previous security proofs dealing with mode-dependent detection efficiencies [33–36]. 

To be more specific, we focus on the proofs that, like ours, do not restrict Eve’s actions and allow her to, for example, add photons to Alice’s pulses and induce detection efficiency asymmetries with tailored light modes [35,36]. Since such proofs are not capable of discerning whether Eve is exploiting or not exploiting the vulnerabilities of the measurement apparatus, they require the prior characterization of the largest detection probability ratio that Eve could induce with specific light modes between two detectors (and potentially two bases); we label this quantity _κ_ . The key rates provided in 

Refs. [35,36] present a penalty depending on the value of _κ_ , regardless of whether Eve is present or not. From the simulations reported in Refs. [35,36], we deduce that for a BB84 protocol with a deterministic single-photon source, 3 dB loss, and QBERs around 5%, no key can be extracted for _κ_ ≥ 2, even if Eve is not present. By using the same parameters ( _η_ = 10<sup>−3</sup><sup>_/_10</sup> , _qZ_ = _qX_ = 0.05, and _d_ = 2) in the adversarial implementation studied in Sec. V B, our proof certifies 0.137 secret key bits per pulse when Eve is not present ( _wZ_ = 0), which is also the rate obtained by naively applying the BB84 protocol. Only when Eve attacks the channel ( _wZ >_ 0) and generates asymmetries in the detection probabilities of the two bases up to _κ_ = 4.6 does our key rate decrease. We conclude that our proof is able to withstand larger mode-dependent asymmetries ( _κ_ ) in the detection probabilities of vulnerable QKD setups compared with previous proposals. And, crucially, it delivers positive key rates when such vulnerabilities are not actively exploited by an eavesdropper. 

## **VII. CONCLUSION** 

We derived an analytical security proof for prepareand-measure QKD protocols affected by basis-dependent detection probabilities. The proof can handle both nominal (mode-independent) and attack-induced (modedependent) detection efficiency mismatches. Compared with previous proposals, our proof requires no prior characterization of the efficiency mismatch generated by different light modes and it makes no assumption on the dimension of the states received by Bob. Moreover, the proof incorporates the decoy-state method and is capable of delivering positive key rates for QKD setups prone to large efficiency mismatches, such as the time-bin QKD protocol simulated in Sec. V. Our proof achieves this by actively monitoring the presence of attack-induced efficiency mismatches through a tunable beam splitter. As a result, it does not penalize the key rate unless an eavesdropper is actually attempting to control which basis clicks, whereas previous proofs always apply a penalty for the mere _possibility_ of controlling the basis that clicks. In the most extreme case, where a QKD setup allows Eve to fully control which basis clicks, previous proofs cannot generate secret keys. Conversely, our proof will return positive key rates unless an adversary is actively exploiting the setup’s flaws, in which case our key rate detects the attack and drops to zero. The merit for this remarkable feature is in part attributed to the tunable beam splitter, which we assume cannot be controlled by the adversary. Relaxing this assumption is an interesting direction for future work. 

Further directions worth pursuing include extending our results to finite-key scenarios to apply our proof to realworld setups. Moreover, proving security against coherent attacks is desirable. Because of apparent difficulties in reducing our general model to finite dimensions, a possible 

044011-14 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

avenue is represented by an adaptation of the approach with entropic uncertainty relations for smooth entropies [8]. Nonetheless, we believe that the techniques introduced in this work can help address other security vulnerabilities of quantum cryptographic protocols. 

_Note added._ While preparing the manuscript, we became aware of a related study [54]. That paper provides a security proof with finite-size effects for the decoy BB84 with mode-dependent detection efficiencies and active basis choice, going beyond the results in Ref. [36]. However, similarly to Ref. [36], the proof in Ref. [54] requires an _a priori_ characterization of the detectors. Indeed, one of the required input parameters is the maximum relative difference in detection efficiencies that the eavesdropper can trigger. Conversely, in our proof no such parameter is required as it is estimated in real time during the execution of the QKD protocol. 

## **ACKNOWLEDGMENTS** 

F.G. contributed to this work exclusively on behalf of Heinrich-Heine-Universität Düsseldorf (previous affiliation). 

F.G. acknowledges funding from the Deutsche Forschungsgemeinschaft through Individual Grant No. BR2159/6-1. H.K., D.B., and N.Wy. acknowledge support by the QuantERA project QuICHE via the German Ministry of Education and Research (BMBF; Grant No. 16KIS1119K). D.B. and H.K. acknowledge support by the BMBF through the projects QuNET+ProQuake (Grant No. 16KISQ137) and QuKuK (Grant No. 16KIS1619). N.Wa. acknowledges funding from the BMBF (QPIC-1, Pho-Quant). M.K. and M.O. acknowledge the project QuICHE, supported by the National Science Centre, Poland (Project No. 2019/32/Z/ST2/00018) under QuantERA, which has received funding from the European Union’s Horizon 2020 research and innovation program under Grant Agreement No. 731473. M.K., M.O., and A.W. acknowledge support by the Excellence Initiative—Research University of the University of Warsaw. G.C. and C.M. acknowledge the European Union’s Horizon 2020 QuantERA ERANET Cofund in Quantum Technologies project QuICHE and support from the PNRR MUR project PE0000023NQSTI. The authors thank Daniel Gauthier, Brian Smith, and Devashish Tupkary for insightful discussions. 

## **APPENDIX A: NOTATION** 

In Table I, we summarize the notation adopted throughout this paper. 

## **APPENDIX B: PHASE ERROR RATE BOUND** 

In this appendix we report, in a concise manner, the formulas that compose the upper bound on the phase error rate _e_ ˜ _X_ ,1, which appears in the key rate of the protocol (17). For the notation and symbols used in the formulas below, see Appendix A. 

The upper bound on the phase error rate is defined as follows: 



˜ The expression for _eX_ ,1 contains several quantities, which we now detail. We start by defining _p_ ✓|0 = _pd_<sup>_Z_and</sup><sup>_p_✓|1=</sup> 1 − _(_ 1 − _pd_<sup>_Z)η_↓,whicharetheprobabilitiesthatthe</sup><sup>_Z_-basisdetectorclicks,withTBSsetting</sup><sup>_(η_↓,</sup><sup>_η_↓</sup><sup>_)_,giventhatthe</sup> state received by Bob contains zero photons or one photon, respectively, localized in _Z_ . We recall that 



are the total probability of a dark count in the _Z_ -basis detector and the total probability of a dark count in the _X_ -basis detector, respectively. We also define _�_ 2 as 



044011-15 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

TABLE I. Notation used in this paper. _W_ is a placeholder for the appropriate yield or error rate. The symbols ✓ and ∅ stand for a detection ( _ZB_ = ∅) and no detection ( _ZB_ = ∅) in Bob’s _Z_ -basis detector, respectively. 

|**Symbol**|**Name**|**Defnition**|
|---|---|---|
|_μ_1,_μ_2,_μ_3|· · ·|The three intensities used by Alice to prepare her states|
|_(ηi_,_ηl)_|TBS setting|The transmittance of the TBS is set to_ηi_ in the interval_Z_ and to_ηl_<br>otherwise|
|_η_↑(_η_↓)|· · ·|Maximal (minimal) transmittance achievable by the TBS|
|_ηX_|· · ·|Detection efciency of the_X_-basis detector, including the TBS insertion<br>loss|
|_ηZ_|· · ·|Detection efciency of the_Z_-basis detector, including the TBS insertion<br>loss<br>|
|_ηr_|· · ·|_ηr_ =_ηX /ηZ_<br>|
|_X_|_X_-basis detection interval|The set of all modes detected by the_X_-basis detector:_X_ = ∪<sup>_d_−1</sup><br>_k_=0<sup>_Xk_</sup><br>|
|_Z_|_Z_-basis detection interval|The set of all modes detected by the_Z_-basis detector:_Z_ = ∪<sup>_d_−1</sup><br>_j_=0<sup>_Zj_</sup>|
|_p_<sup>_X_</sup><br>_d_|· · ·|Probability of a dark count in mode_Xk_ of the_X_-basis detector, for all_k_|
|_p_<sup>_Z_</sup><br>_d_|· · ·|Probability of a dark count in mode_Zj_ of the_Z_-basis detector, for all_j_<br>Total probability of a dark count in the_X_-basis (_Z_-basis) detector if no|
|_p_<sup>_X_</sup><br>_d_ <sup>(</sup><sup>_pZ_</sup><br>_d_ <sup>)</sup>|· · ·|photon is localized in_X_ (_Z_): _p_<sup>_X_</sup><br>_d_ <sup>= 1 −</sup><sup>_(_1 −</sup><sup>_pZ_</sup><br>_d _<sup>_)d_ (</sup><sup>_pZ_</sup><br>_d_ <sup>= 1 −</sup><sup>_(_1 −</sup><sup>_pZ_</sup><br>_d _<sup>_)d_)</sup>|
|_W_ (_W_<br>)<br>· · ·<br>|· · ·<br>(≤1)-subspace|Upper (lower) bound on_W_:<br>_W_≥_W_ (_W_<br>≤_W_)<br>The subspace with at most one photon localized in_Z_|
|[_W_]<sup>≤1</sup><br>_Z_|· · ·|_W_is restricted to the (≤1)-subspace|
|˜_eX_,1|Phase error rate|The crucial parameter to be estimated in the security proof|
|<br>_T_|· · ·|Random variable indicating whether Alice prepares a_Z_-basis state<br>(_X_-basis state):_T_ =_Z_ (_T_ =_X_)|
|_IA_|· · ·|Alice’s intensity choice in one round|
|_NA_|· · ·|Number of photons sent by Alice in one round|
|_ZA_ (_XA_)|· · ·|Random variable storing Alice’s symbol encoded in a_Z_-basis state<br>(_X_-basis state)|
|_ZB_ (_XB_)|· · ·|Random variable storing the outcome of Bob’s_Z_-basis detector (_X_-basis<br>detector):_ZB_,_XB_ ∈{0, 1,_. . ._,_d_−1,∅}|
|_G_<sup>_Z_</sup><br>_μj_,_(ηl_,_ηl)_<br>|_Z_-basis gain|_G_<sup>_Z_</sup><br>_μj_,_(ηl_,_ηl)_ <sup>= Pr</sup><sup>_(ZB_ = ∅|</sup><sup>_T_ =</sup><sup>_Z_,</sup><sup>_IA_ =</sup><sup>_μj_ ,</sup><sup>_(ηl_,</sup><sup>_ηl))_</sup><br>|
|_G_<sup>_X_ ,✓</sup><br>_μj_,_(ηi_,_ηl)_<br>|_X_-basis gain|_G_<sup>_X_ ,✓</sup><br>_μj_,_(ηi_,_ηl)_ <sup>= Pr</sup><sup>_(XB_ = ∅,</sup><sup>_ZB_ = ∅|</sup><sup>_T_ =</sup><sup>_X_ ,</sup><sup>_IA_ =</sup><sup>_μj_ ,</sup><sup>_(ηi_,</sup><sup>_ηl))_</sup><br>|
|_G_<sup>_X_ ,∅</sup><br>_μj_,_(ηi_,_ηl)_|_X_-basis gain|_G_<sup>_X_ ,∅</sup><br>_μj_,_(ηi_,_ηl)_ <sup>= Pr</sup><sup>_(XB_ = ∅,</sup><sup>_ZB_ = ∅|</sup><sup>_T_ =</sup><sup>_X_ ,</sup><sup>_IA_ =</sup><sup>_μj_ ,</sup><sup>_(ηi_,</sup><sup>_ηl))_</sup>|
||QBER of the key||
|_QZ_,_μj_|generation rounds|_QZ_,_μj_ =Pr_(ZA_ =_ZB_|_T_ =_Z_,_IA_ =_μj_,_(η_↓,_η_↓_)_,_ZB_ = ∅_)_|
|_QX_,_μj_,_(ηi_,_η_↑_)_,✓|_X_-basis QBER|_QX_,_μj_,_(ηi_,_η_↑_)_,✓=Pr_(XA_ =_XB_|_T_ =_X_,_IA_ =_μj_,_(ηi_,_η_↑_)_,_XB_ = ∅,_ZB_ = ∅_)_|
|_QX_,_μj_,_(ηi_,_η_↑_)_,∅|_X_-basis QBER<br>_n_-photon_Z_-basis|_QX_,_μj_,_(ηi_,_η_↑_)_,∅=Pr_(XA_ =_XB_|_T_ =_X_,_IA_ =_μj_,_(ηi_,_η_↑_)_,_XB_ = ∅,_ZB_ = ∅_)_|
|_Y_<sup>_Z_</sup><br>_n_,_(ηl_,_ηl)_|yield<br>_n_-photon_X_-basis|_Y_<sup>_Z_</sup><br>_n_,_(ηl_,_ηl)_ <sup>= Pr</sup><sup>_(ZB_ = ∅|</sup><sup>_T_ =</sup><sup>_Z_,</sup><sup>_NA_ =</sup><sup>_n_,</sup><sup>_(ηl_,</sup><sup>_ηl))_</sup>|
||yield<br>(_n_=1:||
|_Y_<sup>_X_ ,✓</sup><br>_n_,_(ηi_,_ηl)_|<br>test-round yield)<br>_n_-photon_X_-basis<br>ild<br> 1|_Y_<sup>_X_ ,✓</sup><br>_n_,_(ηi_,_ηl)_ <sup>= Pr</sup><sup>_(XB_ = ∅,</sup><sup>_ZB_ = ∅|</sup><sup>_T_ =</sup><sup>_X_ ,</sup><sup>_NA_ =</sup><sup>_n_,</sup><sup>_(ηi_,</sup><sup>_ηl))_</sup>|
|_Y_<sup>_X_ ,∅</sup><br>_n_,_(ηi_,_ηl)_|ye<br>(_n_=:<br>test-round yield)<br>_n_-photon_X_-basis bit<br>error rate (_n_=1:|_Y_<sup>_X_ ,∅</sup><br>_n_,_(ηi_,_ηl)_ <sup>= Pr</sup><sup>_(XB_ = ∅,</sup><sup>_ZB_ = ∅|</sup><sup>_T_ =</sup><sup>_X_ ,</sup><sup>_NA_ =</sup><sup>_n_,</sup><sup>_(ηi_,</sup><sup>_ηl))_</sup>|
||test-round bit error||
|_eX_,_n_,_(ηi_,_ηl)_,✓|rate)<br>_n_-photon_X_-basis bit<br>error rate (_n_=1:<br>test-round bit error|_eX_,_n_,_(ηi_,_ηl)_,✓=Pr_(XA_ =_XB_|_T_ =_X_,_NA_ =_n_,_(ηi_,_ηl)_,_XB_ = ∅,_ZB_ = ∅_)_|
|_eX_,_n_,_(ηi_,_ηl)_,∅|rate)|_eX_,_n_,_(ηi_,_ηl)_,∅=Pr_(XA_ =_XB_|_T_ =_X_,_NA_ =_n_,_(ηi_,_ηl)_,_XB_ = ∅,_ZB_ = ∅_)_|
|_�_2|Group delay dispersion coefcient|Group delay dispersion coefcient of the setup simulated in Fig.5|
|_�j_ (_�k_)|<br>Time-bin width|<br>The widths of the time bins in Bob’s time-of-arrival measurement for the<br>_Z_ basis (_X_ basis), used to generate Fig.5|



044011-16 



<!-- Start of picture text -->
-<br>EE<br>I Ea<br>( )<br>-[]<br>”<br>71<br>( )<br>- [ ]<br>_<br>1 — - —<br>I -<br>EE eeee Ta 1H<br>Ee Uy<br>ee<br>(me<br><!-- End of picture text -->



<!-- Start of picture text -->
a TE J<br>===1]<br>a<br>} [] |]<br>( — C= ) ( 7 T C T )<br>|]<br>( — JC )<br>ob —L 1]<br>|] |]<br>- ( — JC— 7 EC NC )<br>|]<br>( — C7 )<br>ol —1 7]<br>|] to<br>|] t<br>|] EE<br>|] EEN<br><!-- End of picture text -->



<!-- Start of picture text -->
_ oT 1]<br>( = 0 C —  ( EE CN )<br>=== I |<br>_<br>[|<br>— ( — C= 7) )<br>- I a<br>( — 0 7) ) ( = TC 7) )<br>~<br>) ] [ ]<br>( — C= ) ( = T C T )<br>=== 0 J |<br>SE A |<br>|I<br>a<br>]<br>Jl<br>| EE A<br>] Jl<br><!-- End of picture text -->

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

## **APPENDIX C: SECURITY PROOF** 

In this appendix we prove the security of Protocol 1. The DW bound [46] provides a lower bound on the asymptotic secret key rate of a QKD protocol subjected to collective attacks. According to the protocol’s description, the shared secret key is extracted from the key generation rounds, i.e., the rounds where _T_ = _Z_ , the TBS is set to _(η_ ↓, _η_ ↓ _)_ , and _ZB_ = ∅. To keep the notation concise, we define the following intersections of events: 





The DW bound of our protocol then reads [55] 



where _H (ZA_ | _IAE)_ [ _H (ZA_ | _IAZB)_ ] is the von Neumann entropy of Alice’s key outcome _ZA_ conditioned on Eve’s (Bob’s) total side information, while the subscript in the entropies indicates that they are computed on the state _ρ_ shared by Alice, Bob, and Eve, conditioned on the event _�Z_ . Since Alice (Bob) chooses the setting _T_ = _Z_ [ _(η_ ↓, _η_ ↓ _)_ ] with probability _pZ_ , we have 



The remainder of the proof consists in deriving appropriate bounds on the two entropies in Eq. (C3) to show that _r_ ∞, given in Eq. (17), is a lower bound on the DW rate (C3), hence proving the protocol’s security. 

## **1. Computing the postselected state** 

The first step is to obtain a mathematical expression for the quantum state _ρZAIAZBE_ | _�Z_ on which the two entropies in Eq. (C3) are computed. 

To start with, we express the state of Alice’s classical registers ( _ZA_ , _IA_ ) and of Bob’s ( _B_ ) and Eve’s ( _E_ ) quantum systems in a _Z_ -basis round as follows: 



Some comments are due. First, we added a classical register _NA_ , inaccessible to Alice, that contains the exact number of photons sent by Alice. Moreover, we modeled Eve’s collective attack as a unitary acting on systems _BE_ , which is not restrictive since we make no assumption on 

the dimension of Eve’s quantum register _E_ . Finally, the factor 1 _/d_ is due to the uniform probability with which Alice selects the symbol _ZA_ . 

We mathematically describe Bob’s measurement in terms of the following POVM: 



where the POVM element _Mj_<sup>_(η_</sup> , _k_<sup>_i_,</sup><sup>_ηl)_</sup> represents the outcome _ZB_ = _j_ , _XB_ = _k_ when Bob selects _(ηi_ , _ηl)_ as the TBS setting. Similarly, _Mj_<sup>_(η_</sup> ,∅<sup>_i_,</sup><sup>_ηl)_</sup> represents the outcome _ZB_ = _j_ and no click in the _X_ -basis detector ( _XB_ = ∅) with TBS setting _(ηi_ , _ηl)_ . And so on for the others. From Eq. (C6), we can define a POVM that focuses on the outcomes of the _Z_ -basis detector under the TBS setting _(η_ ↓, _η_ ↓ _)_ and can be considered the effective POVM performed by Bob in the key generation rounds: 



with 



For this, we call such a reduced measurement the “key generation measurement” of Bob. From Eq. (C7), in turn, we define the key generation measurement map _EB_<sup>_Z_</sup> → _BZ_<sup>˜</sup> _B_<sup>. This</sup> map acts between the input system _B_ and two classical output systems, _ZB_ and _B_<sup>˜</sup> , where _B_<sup>˜</sup> is a classical register that contains coarse-grained information about the measurement outcome, namely, whether the detector clicked ( _B_<sup>˜</sup> = ✓) or did not click ( _B_<sup>˜</sup> = ∅). We thus have 



We now recast Bob’s key generation measurement map as the concatenation of two quantum maps by following the formalism developed in Refs. [8,14]: _EB_<sup>_Z_</sup> → _BZ_<sup>˜</sup> _B_<sup>=</sup><sup>_E_</sup> _BB_<sup>_Z_</sup> ˜ →˜ _BZB_<sup>◦</sup> 

_E_<sup>_Z_Thefirstmapthatisappliedcanbeviewedasa</sup> _B_ → _BB_<sup>˜.</sup> coarse-grained measurement: 



044011-20 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

where 



The second map replaces the coarse-grained outcomes of the first map with the actual outcomes of Bob’s measurement and traces out the quantum system _B_ . Let 1 _Z_ ✓ be the projector on the support of the operator _Z_ ✓. Then the second map reads 



where 



with _(_<sup><u>√</u></sup> _Z_ ✓ _)_<sup>−1</sup> the inverse of<sup>√</sup> _Z_ ✓ over its support, ~~√~~ _Z_ ✓ _(_<sup>~~√~~</sup> _Z_ ✓ _)_<sup>−1</sup> = _(_<sup>√</sup> _Z_ ✓ _)_<sup>−1√</sup> _Z_ ✓ = 1 _Z_ ✓ , and with 1<sup>⊥</sup> _Z_ ✓<sup>the</sup> projector on the complement of the support of _Z_ ✓. With the definition in Eq. (C14), both maps in Eqs. (C11) and (C13) are completely positive and trace preserving (CPTP) and their concatenation returns the original map (C10). 

In a similar manner, from Eq. (C6) we can define a POVM that focuses on the outcomes of the _X_ -basis detector, which would play the role of Bob’s complementary measurement in a traditional QKD security proof: 

We can thus define Bob’s test measurement map as the quantum map implementing the POVM in Eq. (C15) 



and decompose it as the concatenation of two CPTP maps: 



where the first map reads 



with 



while the second map reads 





where 

with 





For this reason, we call this POVM the “test measurement” of Bob. We emphasize that the information gathered by the parties in the rounds labeled as test rounds exceeds what can be obtained by the above POVM, where the _Z_ -basis detector outcomes are ignored and the TBS setting is fixed. Nevertheless, we are free to choose Bob’s complementary measurement when defining the phase error rate, and our choice will be a POVM connected to Eq. (C15). The goal of the security proof will then be to show how the resulting phase error rate can be estimated from the full statistics observed in the test rounds. 



with _(_<sup>~~√~~</sup> _X_ ✓ _)_<sup>−1</sup> the inverse of<sup>~~√~~</sup> _X_ ✓ over its support and 1<sup>⊥</sup> _X_ ✓<sup>the projector on the complement of the support of</sup><sup>_X_✓.</sup> 

At this point, we can express the state of Alice’s and Bob’s classical registers _ZA_ and _ZB_ and Eve’s quantum system _E_ in a _Z_ -basis round where Bob selected the TBS setting _(η_ ↓, _η_ ↓ _)_ as follows: 



where _ρZAIANABE_ is given in Eq. (C5) and where we used the definition of _�Z_ in Eq. (C1). To obtain the state on which the entropies in Eq. (C3) are computed, we must postselect the state in Eq. (C24) on a detection in the _Z_ - basis detector ( _ZB_ = ∅). For this, we perform the projective measurement {|∅⟩⟨∅| _B_ ˜ , |✓⟩⟨✓| _B_ ˜ } on system _B_<sup>˜</sup> and select 

044011-21 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

_(η_ ↓, _η_ ↓ _)_ . From this quantity we recover the _Z_ -basis gain 

the state conditioned on the outcome _B_<sup>˜</sup> = ✓ through the nonlinear map 



such that the state of a key generation round (i.e., conditioned on the event _�Z_ ) is given by [55] 

and recast the state in Eq. (C28) as 





where we used Bayes’s rule and the definition of _�Z_ in Eq. (C2) to define 

where Pr _(ZB_ = ∅| _�Z)_ = Tr[ _ρZAIANA_ ˜ _BZBE_ | _�Z_ |✓⟩⟨✓| _B_ ˜ ]. The state in Eq. (C26) is the one needed to compute the entropies in Eq. (C3). 



## **2. Computing the leakage** 

Then we observe that the state in Eq. (C31) is a classicalquantum state of the form<sup>�</sup> _x_<sup>_px_|</sup><sup>_x_⟩⟨</sup><sup>_x_| ⊗</sup><sup>_ρx_with</sup><sup>_ρx_nor-</sup> malized states, where the role of _x_ is played by _μi_ . Therefore, we can express its conditional entropy as 

We first focus on the second entropy in Eq. (C3), which quantifies the optimal leakage due to error correction in the asymptotic regime and is computed on a reduced state of Eq. (C26), namely, 





By explicitly calculating the above state through Eq. (C24), we obtain the expression 



where we used Fano’s inequality, with _QZ_ , _μi_ being the QBER of the key generation rounds where Alice used the intensity _μi_ , Eq. (14). In the last inequality we used Eq. (C32) and the definition of _u(x)_ in Eq. (20). 

where _ζB_ | _μi_ , _j_ is the state received by Bob when Alice prepared the weak coherent pulse (WCP) with intensity _μi_ encoding the symbol _ZA_ = _j_ : 





Hence, we recognize that Tr _B_ [ _Zj_ ′ _ζB_ | _μi_ , _j_ ] = Pr _(ZB_ = _j_<sup>′</sup> | _�Z_ , _IA_ = _μi_ , _ZA_ = _j )_ is the probability that Bob obtains outcome _ZB_ = _j_<sup>′</sup> , given that Alice sent the symbol _ZA_ = _j_ encoded in a WCP of intensity _μi_ and Bob chose the setting 

## **3. Lower-bounding Eve’s uncertainty** 

## **_a. Discarding multiphoton contributions_** 

We now turn our attention to the first conditional entropy in Eq. (C3), representing Eve’s uncertainty about Alice’s key bit _ZA_ in a key generation round. The goal is to obtain a lower bound that depends only on the statistics observed in the protocol. By the strong subadditivity, we can lowerbound the conditional entropy as follows: 



where the right-hand side describes Eve’s uncertainty about _ZA_ if Eve knew the exact photon number _NA_ of the 

044011-22 



<!-- Start of picture text -->
Q<br>«| SE]<br>@ El<br>a [ «C 1) ] 5<br>Ir Q<br>~<br>a<br>r<br>-<br>r<br>| | SE :<br>D > > r<br>r<br>« Ye > o<br>-<br>CD DE Q<br><!-- End of picture text -->

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 





where we used Eq. (C41) and 



From Eq. (C44) we observe that the state of _IA_ is a tensor product with the state of _ZAE_ , which implies that 



By combining Eqs. (C43) and (C48), we obtain 



where the entropy on the right-hand side is computed in Eq. (C46). 

By combining Eqs. (C34) and (C49), we can lower bound the first entropy in Eq. (C3) as follows: 



where we used Eq. (C41) and defined the _n_ -photon _Z_ -basis yield as the detection probability of Bob’s key generation measurement when Alice selects the _Z_ basis and sends _n_ photons as 



Note that the yields are not directly observed and are instead estimated with the decoy-state method. Moreover, note that the yield in Eq. (C51) is well defined 

since 1 _/d_ = Pr _(ZA_ = _j )_ = Pr _(ZA_ = _j_ | _NA_ = _n)_ , where the last equality is because the distribution of the symbols and photons prepared by Alice is factorized: Pr _(ZA_ = _j_ , _NA_ = _n)_ = Pr _(ZA_ = _j )_ Pr _(NA_ = _n)_ . 

We can further lower-bound the entropy in Eq. (C50) by using the fact that _H (ZA_ | _E)ρ_ | _n_ , _�Z_ ≥ 0 since _ρZAE_ | _n_ , _�Z_ is classical on _ZA_ . We obtain 



where we discarded all the terms corresponding to events where Alice sends _n_ ≥ 2 photons. This is done because our ability to find a nontrivial lower bound on _H (ZA_ | _E)σ_ | _n_ , _�Z_ for _n_ ≥ 2 is limited by the fact that we cannot apply the uncertainty relation on such entropies. Indeed, the states sent by Alice in key generation rounds and test rounds can be seen as originating from the same entangled state (which is a precondition for using the uncertainty relation) only at the single-photon level. In addition, in the event that _n_ ≥ 2, Eve can perform a photon-number-splitting attack and learn _ZA_ while remaining undetected, which implies that _H (ZA_ | _E)σ_ | _n_ , _�Z_ = 0 for _n_ ≥ 2. 

We observe that the state _ρZAE_ |0, _�Z_ in Eq. (C46) factorizes in the case that Alice sends the vacuum 



because Eve’s state (C38), _φE_ |0, _j_ , _�Z_ , is independent of _j_ . This reflects the fact that Eve is uncorrelated with Alice’s outcome _ZA_ when Alice sends the vacuum. Therefore, we have 



where the entropy in the second line is the Shannon entropy of the enclosed distribution. From Eq. (C39) we observe that Pr _(ZB_ = ∅| _�Z_ , _NA_ = 0, _ZA_ = _j )_ = Pr _(ZB_ = ∅| _�Z_ , _NA_ = 0 _)_ , i.e., the distribution is independent of the symbol _ZA_ when Alice sends the vacuum. Thus, the distribution in the Shannon entropy simplifies to a uniform distribution of _d_ outcomes, and we obtain 



044011-24 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

By using Eq. (C55) in Eq. (C52), we obtain 



## **_b. Using uncertainty relations_** 

We are left to find a lower bound on the entropy _H (ZA_ | _E)ρ_ |1, _�Z_ of Alice’s outcome _ZA_ of a key generation round where she sends exactly one photon, conditioned on Eve’s quantum side information. The entropy is computed on the state in Eq. (C46), which for _n_ = 1 can be recast as 



where we used Eqs. (C51) and (C38). The sought bound is obtained through the uncertainty relation for entropies with quantum side information, whose statement is reported below. 

we define the average state sent by Alice in any round, restricted to the single-photon subspace, 



where the equality between the average state of _Z_ -basis rounds and the average state of _X_ -basis rounds is due to the assumption (7). We then define _τAB_ = | _�τ_ ⟩⟨ _�τ_ | to be the purification of _τ_ and define the POVMs { _Mj_<sup>_Z_}</sup><sup>_j_and {</sup><sup>_M X_</sup> _k_<sup>}</sup><sup>_k_</sup> acting on the purifying system _A_ : 



where the superscript “ _T_ ” represents the transpose with respect to the Schmidt basis of _τAB_ . Then, according to Lemma 14 in Ref. [8], the reduced states on _B_ , after application of the POVMs (C62) and (C63) on system _A_ of _τAB_ , are exactly the states Alice prepares in the one-photon subspace (multiplied by their probability): 



Moreover, Lemma 14 in Ref. [8] shows that 

_Lemma 1 (entropic uncertainty relation [48–51])._ Let _σABE_ be a normalized quantum state and let { _Mj_<sup>_Z_}</sup><sup>_j_and</sup> { _Mk_<sup>_X_}</sup><sup>_k_be two POVMs on</sup><sup>_A_. It holds that</sup> 



where the first entropy and the second entropy are computed on the classical-quantum states: 



respectively. 

We choose an appropriate state _σABE_ and POVMs on _A_ such that the first entropy in Eq. (C58) coincides with the entropy we need to bound in Eq. (C56). To this aim, 



for the above-defined POVMs, where _S_ is given in Eq. (7), ∥ _A_ ∥∞ is the largest singular value of _A_ , and _c_ is given in Eq. (18). 

_Remark 1._ As discussed in Sec. III, the protocol’s key rate (17) is maximized when the compatibility coefficient _c_ is minimal: _c_ = 1 _/d_ . Here we show that a sufficient condition to attain this is that Alice’s one-photon states form two mutually unbiased sets: 



_Proof._ The proof hinges on the fact that when two sets of vectors, {|1 _Zj_ ⟩} _j_ and {|1 _Xk_ ⟩} _k_ , sum to the same operator _S_ by Eq. (7) and are mutually unbiased (C67), then they are orthogonal sets. 

044011-25 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

To see this, consider the scalar ⟨1 _Zj_ | _S_ |1 _Zj_ ⟩. By virtue of _S_ =<sup>�</sup> _k_<sup>|1</sup><sup>_X_</sup> _k_<sup>⟩⟨1</sup><sup>_X_</sup> _k_<sup>| and Eq. (C67), we get ⟨1</sup><sup>_Z_</sup> _j_<sup>|</sup><sup>_S_|1</sup><sup>_Z_</sup> _j_<sup>⟩= 1.</sup> At the same time, by using the other expression for _S_ , we 

2 get ⟨1 _Zj_ | _S_ |1 _Zj_ ⟩= 1 +<sup>�</sup> _j_<sup>′</sup> = _j_ ���⟨1 _Zj_ |1 _Zj_ ′ ⟩��� , which implies 2 that<sup>�</sup> _j_<sup>′</sup> = _j_ ���⟨1 _Zj_ |1 _Zj_ ′ ⟩��� = 0. This implies that the set of vectors {|1 _Zj_ ⟩} _j_ is orthonormal: 



Similarly for the set {|1 _Xk_ ⟩} _k_ , 



Thus, we deduce that _S_ is the identity in the subspace defined by {|1 _Zj_ ⟩} _j_ (or {|1 _Xk_ ⟩} _k_ ), which simplifies Eq. (18) as follows: 



> where in the second equality we used Eq. (C67). ■ 

Therefore, we define the state _σABE_ = | _�σ_ ⟩⟨ _�σ_ |, with 



and apply the uncertainty relation on _σABE_ with the POVMs (C62) and (C63). By computing the states (C59) and (C60) with these choices and by using Eqs. (C64) and (C65), we get 



where we used Eq. (C57) and 



respectively, where we defined _σk_ as 



Note that, because of the assumption (7) and the definition (C51) of yields for rounds with _�Z_ , we have 



which confirms that the state in Eq. (C73) is properly normalized. Thus, the uncertainty relation (C58) yields a lower bound on the entropy of interest: 



where we used Eqs. (C72) and (C66) and where the entropy on the right-hand side is computed on the state (C73). The rest of the proof is devoted to finding an upper bound on _H (XA_ | _B)σ_ in terms of observed statistics. 

Since the entropy _H (XA_ | _B)σ_ is defined on a classicalquantum state (C73), we can apply a measurement map _E_<sup>_X_itsconditioningsystemthatcannotreducethe</sup> _B_ → _X_<sup>˜</sup> _B_<sup>on</sup> entropy [52]: 



where _X_<sup>˜</sup> _B_ is now a classical random variable resulting from a fictitious test measurement. Intuitively, a sensible choice for the fictitious measurement on system _B_ could be Bob’s test measurement (C18), defined earlier as the reduced POVM of Bob that focuses on the outcomes of the _X_ -basis detector, from which Bob can try to guess the symbol _XA_ sent by Alice in an _X_ -basis round. However, the states of system _B_ in Eq. (C73) undergo a postselection corresponding to a detection in Bob’s key generation measurement. This postselection can be described in terms of the first map (C11) composing Bob’s key generation measurement map and of the postselection map (C25), such that the state in Eq. (C73) can be recast as 



Therefore, the application of Bob’s test measurement map (C18), _EB_<sup>_X_</sup> → _BX_<sup>˜</sup> _B_<sup>, on the state in Eq. (C78) would</sup><sup>_not_return a</sup> classical state whose correlations are observed experimentally. In other words, while the state 



044011-26 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

could be characterized experimentally with traditional QKD techniques such as the decoy-state method, the state 



cannot, due to the additional maps Tr _B_ ˜ ◦ _P_ ◦ _EB_<sup>_Z_</sup> → _BB_<sup>˜enact-</sup> ing the postselection of a detection in Bob’s key generation measurement. According to this observation, the measurement map _EB_<sup>_X_</sup> → _X_<sup>˜</sup> _B_<sup>to be applied in Eq. (C77) should not be</sup> chosen to be Bob’s test measurement: _E_<sup>_X_</sup> _B_ → _X_<sup>˜</sup> _B_<sup>=</sup><sup>_E_</sup> _B_<sup>_X_</sup> → _BX_<sup>˜</sup> _B_<sup>.</sup> 

Nevertheless, recall that Bob’s test measurement can be decomposed into two CPTP maps (C19), where the first map (C20), _EB_<sup>_X_</sup> → _BB_<sup>˜, is a coarse-grained map that describes</sup> only whether there is a detection in the _X_ detector. Let us assume for the moment that the detection probability of Bob’s key generation and test measurements coincides for every input state, i.e., the assumption in Eq. (34), which is often implicit in standard QKD security proofs. Under the assumption (34), we observe that the following two maps coincide: 



i.e., postselection on a detection in the key generation measurement and in the test measurement has the same effect. This fact suggests a better choice for the fictitious measurement ( _EB_<sup>_X_</sup> → _X_<sup>˜</sup> _B_<sup>)tobeappliedonEq.(C78):thesecond</sup> CPTP map of the decomposition of Bob’s test measurement, i.e., the map _EBB_<sup>_X_</sup> ˜ →˜ _BXB_<sup>,giveninEq.(C22).More</sup> precisely, since the state in Eq. (C78) is already postselected on a detection of the test measurement—provided that the assumption (34) holds—we choose _EB_<sup>_X_</sup> → _X_<sup>˜</sup> _B_<sup>tobe</sup> 

the restriction of _E_<sup>_X_</sup> ˜<sup>_B_˜= 1:</sup> _BB_ →˜ _BXB_<sup>to the subspace with</sup> 



with _X_<sup>˜</sup> _k_ ˜ defined in Eq. (C23). With the above fictitious measurement map and under the assumption (34), the state _σXAB_ transforms to 



which can be characterized experimentally by traditional QKD methods. In our proof, however, we avoid making the assumption in Eq. (34), and hence the classical state arising from _EB_<sup>_X_</sup> → _X_<sup>˜</sup> _B_<sup>_(σXAB)_, with the fictitious measurement</sup> in Eq. (C82), cannot be directly estimated like in most QKD proofs. Nevertheless, we maintain the choice of a fictitious measurement map as given in Eq. (C82), such that our proof can reduce to standard QKD proofs in the special case where the assumption (34) holds. 

With our choice of fictitious test measurement, the entropy on the right-hand side of Eq. (C77) is computed on the normalized state: 



where we used Eq. (C73). Since Eq. (C84) corresponds to a classical-classical state, we can upper-bound its conditional Shannon entropy by using Fano’s inequality, 



where _u(x)_ is given in Eq. (20) and where we introduced the phase error rate 



By combining Eqs. (C76), (C77), and (C85), we obtain the following lower bound on the remaining entropy in Eq. (C56): 



## **_c. Reduction of phase error rate_** 

The derived bound does not yet conclude the proof, since the phase error rate, as defined in Eq. (C86), cannot be directly estimated with the decoy-state method. The reason is that the probability distribution on which the phase error rate is defined is not directly accessible, in general. Indeed, Bob never actually performs the POVM { _X_<sup>˜</sup> _k_ ˜} _k_ ˜ after postselecting the state on a detection in the key generation measurement. This complication, however, vanishes in the proofs that assume that the detection probability is independent of the measurement basis, as explained in the following remark. 

_Remark 2._ Standard QKD security proofs [8,9] assume equality between the detection probabilities of Bob’s key 

044011-27 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

generation measurement (C7) and Bob’s test measurement (C15) for any input state. That is, they assume the equality 



where _Z_ ✓ ( _X_ ✓) is the POVM element corresponding to a detection of the key generation (test) measurement. Equipped with the condition in Eq. (C88), one can immediately verify that the phase error rate can be directly estimated from the decoy-state method applied on the statistics of Bob’s test measurements, thereby completing the security proof. 

To see this, we consider the one-photon bit error rate of Bob’s test measurement (C15), which can be defined as 



where we introduced the one-photon _X_ -basis yield: 



The one-photon _Z_ -basis yield (C51), with Eq. (C39), can be expressed as 



where in the second equality we used the assumption in Eq. (C88) together with Eq. (7). At the same time, the assumption in Eq. (C88) allows us to simplify the 

following expression: 



where we used Eq. (C23). By using Eqs. (C91) and (C92) in the expression for the phase error rate (C86), we obtain 



i.e., the phase error rate reduces to the bit error rate of Bob’s test measurement, which can be estimated with the decoy-state method. This fact would thus conclude the security proof of the protocol, since the phase error rate would be experimentally estimated. 

The absence of the assumption (C88) makes the estimation of the phase error rate in Eq. (C86) considerably more challenging in our proof, as it cannot be identified anymore with the bit error rate of Bob’s test measurement. In the next subsection we show how we can make use of the full statistics collected in the test rounds to provide an accurate estimation of the phase error rate. 

## **4. Phase error rate estimation** 

In this subsection we develop a method to derive an upper bound on the phase error rate as a function of quantities that can be obtained experimentally with the decoy-state method, without assuming basis-independent detection probabilities, i.e., the assumption in Eq. (C88). For clarity, we report the definition of the phase error rate from Eq. (C86): 



where _Z_ ✓ is given in Eq. (C12), { _σk_ } _k_ is given in Eq. (C74), and _X_<sup>˜</sup> _k_ given in Eq. (C23) and forms a POVM { _X_<sup>˜</sup> _k_ } _k_<sup>_d_</sup> =0<sup>−</sup> 0<sup>1.</sup> 

_k_ =0<sup>.</sup> 

We start with a general overview of the argument, after which we detail all the steps of the derivation. 

## **_a. Overview of the argument_** 

Let us consider the subspace with zero photons or one photon localized in _Z_ , which we recall being the set of modes detected by the _Z_ -basis detector. For brevity, we name this subspace the “(≤ 1)-subspace” and label the average state received by Bob, when Alice sends one 

044011-28 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

photon, as follows: 



where in the last equality we used Eq. (7). 

The first step in estimating the phase error rate consists in reducing the calculation of the phase error rate in Eq. (C86) to the (≤ 1)-subspace. The details of this step are provided in Appendixes C 4 b–C 4 e. Indeed, we expect most of the state _σ_ ¯ to lie in the (≤ 1)-subspace in an honest implementation of the protocol. 

To this aim, we define _�_<sup>_α_</sup> _Z_<sup>to be the projector of</sup><sup>_n_=</sup><sup>_α_</sup> photons in the set _Z_ and the identity elsewhere, such that the (≤ 1)-subspace is the support of _�_<sup>0</sup> _Z_<sup>+</sup><sup>_�_1</sup> _Z_<sup>.Thenwe</sup> can express _Z_ ✓ in terms of _�_<sup>_α_</sup> _Z_<sup>as follows:</sup> 



where _p_ ✓| _α_ is the probability that the _Z_ -basis detector clicks, given that Bob’s input state contains _α_ photons localized in _Z_ . The expression for _p_ ✓| _α_ is determined by the dark count probability _pd_<sup>_Z_andthemode-independent</sup> detection efficiency _ηZ_ of the _Z_ -basis detector, as well as the TBS transmittance _η_ ↓, and is given in Eq. (C181) in Appendix C 4 c (in reality, _p_ ✓| _α_ does not depend on _ηZ_ since the loss of Bob’s _Z_ -basis detector is factored out of Bob’s apparatus and assigned to the quantum channel; see Appendix C 4 b). By using the expansion (C97) of _Z_ ✓ in the phase error rate (C86), we can isolate the contribution to the phase error rate given by the fraction of the states _σk_ existing in the (≤ 1)-subspace. We cannot assume that the states _σk_ are completely confined to that subspace due to potential attacks by Eve, which may, for example, add photons to Alice’s pulses. Therefore, in Appendix C 4 d we show how to use the detection statistics of the _Z_ - basis detector, with the TBS settings _(η_ ↓, _η_ ↓ _)_ , _(η_ ↑, _η_ ↑ _)_ , and _(η_ 2, _η_ 2 _)_ , to derive an upper bound on the weight of _σ_ ¯ outside the (≤ 1)-subspace. Our method draws inspiration from the detector decoy technique [28] and leads to the following bound [see Eq. (C217) in Appendix C 4 d]: 



where _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1</sup> is reported in Eq. (C218) in terms of quantities that can be directly estimated with the decoy-state method (the _Z_ -basis yields). In Appendix C 4 e we obtain the following upper bound on the phase error rate (C86), which uses Eqs. (C97) and (C98) to reduce the evaluation 

of the error rate to the (≤ 1)-subspace [see Eq. (C247) in Appendix C 4 e]: 



where _�_ 2 is a function of _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1</sup> and _Y_ 1,<sup>_Z_</sup> _(η_ ↓, _η_ ↓ _)_<sup>givenin</sup> Eq. (C248), and where the support of the operator 



is the (≤ 1)-subspace. 

In Appendix C 4 j, we simplify the expression in Eq. (C99) by computing explicitly the POVM element _X_<sup>˜</sup> _k_ given in Eq. (30). To this aim, similarly to the introduction of _�_<sup>_α_</sup> _Z_<sup>for the</sup><sup>_Z_-basis detector, we introduce the projector</sup> _�_<sup>_β_</sup> _X_<sup>, which projects on the subspace with</sup><sup>_β_photons in the</sup> set of modes _X_ and acts as the identity elsewhere. Then the POVM element _Xk_ of Bob’s test measurement can be written in terms of (1) projectors similar to _�_<sup>_β_</sup> _X_<sup>,(2)the</sup> total dark count probability ( _pd_<sup>_X_)ofthe</sup><sup>_X_-basisdetector,</sup> (3) the TBS transmittance _η_ ↑, and (4) the ratio between the mode-independent detection efficiency of the _X_ -basis detector and the mode-independent detection efficiency of the _Z_ -basis detector (since we factored out the efficiency of the _Z_ -basis detector): 



Note that, by assumption, _ηr_ ≤ 1. The calculation of _X_<sup>˜</sup> _k_ in Appendix C 4 j leads to the following operator upper bound [see Eq. (C386)]: 



When this is used in Eq. (C99), it yields the following upper bound on the phase error rate: 



044011-29 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

We now focus on estimating the first term on the right-hand side of Eq. (C103). This term is clearly linked to the onephoton bit error rate of Bob’s test measurement, Eq. (35). However, note that we must estimate such an error rate when restricting the input state to the (≤ 1)-subspace, due to the presence of the operator _MZ_<sup>≤1. To this aim, we intro-</sup> duce the one-photon _X_ -basis bit error rates _eX_ ,1, _(ηi_ , _ηl)_ ,✓ and _eX_ ,1, _(ηi_ , _ηl)_ ,∅, which we simply refer to as the “test-round bit error rates” and that correspond to the bit error rate in the _X_ basis when the _Z_ -basis detector has a detection or no detection, respectively. They can be expressed as follows [see Eqs. (C274) and (C275) in Appendix C 4 f]: 





where we call _Y_ 1,<sup>_X_,</sup> _(η_<sup>✓</sup> _i_ , _ηl)_<sup>and</sup><sup>_Y_</sup> 1,<sup>_X_,</sup> _(η_<sup>∅</sup> _i_ , _ηl)_<sup>the “test-round yields”</sup> and where _Xk_<sup>_(η_′</sup> ,✓<sup>_i_,</sup><sup>_ηl)_</sup> ( _Xk_<sup>_(η_′</sup> ,∅<sup>_i_,</sup><sup>_ηl)_</sup> ) is Bob’s POVM element describing a detection of outcome _k_<sup>′</sup> in the _X_ -basis detector and a detection (no detection) in the _Z_ -basis detector, given that the TBS is set to _(ηi_ , _ηl)_ . See Appendix A for a precise definition of the test-round yields and bit error rates. Note that, with this formalism, by definition it holds that 



The two test-round bit error rates contain more information about the protocol’s statistics than the bit error rate of Bob’s test measurement alone, Eq. (C93), and this will be crucial to accurately estimate the phase error rate. 

Similarly to the bound on the phase error rate in Eq. (C99) through the expansion (C97), we can use the relation: 1 = _�_<sup>≤</sup> _Z_<sup>1+</sup><sup>_�>_</sup> _Z_<sup>1, with</sup><sup>_�_≤</sup> _Z_<sup>1=</sup><sup>_�_0</sup> _Z_<sup>+</sup><sup>_�_1</sup> _Z_<sup>, to iso-</sup> late the contribution of the (≤ 1)-subspace to the testround bit error rates (C104) and (C105). We do so in Appendix C 4 g, where we obtain in Eqs. (C286) and (C290) tight upper and lower bounds on the following quantities: 





where the notation [·]<sup>≤</sup> _Z_<sup>1indicatesthattheenclosedquan-</sup> tity is calculated only in the (≤ 1)-subspace. The bounds on the above quantities are reported in Eqs. (B26)–(B29). Importantly, they can be directly estimated from the protocol’s statistics, as they are given in terms of the test-round yields and bit error rates as well as of _<u>w</u>_<sup>_>_</sup> _Z_<sup>1.</sup> 

Unfortunately, the restricted test-round bit error rates in Eqs. (C107) and (C108) cannot be directly used to quantify the first term on the right-hand side of Eq. (C103). This is because the latter is restricted to the (≤ 1)-subspace by the operator in Eq. (C100), while the error rates in Eqs. (C107) and (C108) are restricted to the same subspace via the projector _�_<sup>≤</sup> _Z_<sup>1.</sup> 

This prompts us to expand both the term in Eq. (C103) and the restricted test-round bit error rates with Eq. (C100) and _�_<sup>≤</sup> _Z_<sup>1=</sup><sup>_�_0</sup> _Z_<sup>+</sup><sup>_�_1</sup> _Z_<sup>, respectively, such that each term in</sup> the expansion contains either a projection on _�_<sup>0</sup> _Z_<sup>, or a pro-</sup> jection on _�_<sup>1</sup> _Z_<sup>, or the off-diagonal blocks. For the restricted</sup> test-round bit error rates, we obtain 









for _α_ = 0, 1, and similarly for the terms relative to no click in the _Z_ -basis detector. We note that Eq. (C112) is not null, in general, since the POVM elementsnecessarily block diagonal in the subspaces defined by _Xk_<sup>_(η_′</sup> ,✓<sup>_i_,</sup><sup>_ηl)_</sup> are not _�_<sup>_α_</sup> _Z_<sup>.</sup> 

For the first term on the right-hand side of Eq. (C103), the expansion through Eq. (C100) produces the following expression: 

044011-30 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 



where we used the definitions (C111) and (C112) and the equality (C106). 

By comparing the expansions of the restricted testround bit error rates (C109) and (C110) with the expansion (C113) of the term coming from the right-hand side of Eq. (C103), we conclude that an accurate estimation of the latter requires individually estimating each of the three terms in the expansions (C109) and (C110) of the restricted test-round bit error rates. 

The method that we use to estimate each of the three terms on the right-hand side of Eqs. (C109) and (C110) represents one of the novelties of our security proof. The method is based on the observation that when the state (on which the three terms are computed) is projected on the subspaces with zero photons or one photon in _Z_ , then the unitary action of the TBS on the photons localized in _Z_ can be factored out and reduces to a simple prefactor. 

More specifically, recall that the TBS setting _(ηi_ , _ηl)_ means that the TBS acts as a beam splitter with transmittance _ηi_ ( _ηl_ ) for photons localized in (outside) _Z_ . For illustrative purposes, let us consider the 1 term � _Y_ 1,<sup>_X_,</sup> _(η_<sup>✓</sup> _i_ , _ηl)_<sup>_eX_,1,</sup><sup>_(η_</sup> _i_<sup>,</sup><sup>_η_</sup> _l_<sup>_)_,✓</sup> � _Z_<sup>,whichcanbeinterpretedas</sup> 

the probability of the following intersection of events [averaged over Alice’s random selection of the symbol _XA_ = _k_ ): the input state _σk_ of Bob contains one photon localized in _Z_ , the _Z_ -basis detector clicks, and the _X_ -basis detector clicks with an erroneous outcome _k_<sup>′</sup> = _k_ (all with the TBS setting _(ηi_ , _ηl)_ ]. By following Fig. 1, we see that either the single photon localized in _Z_ is transmitted by the TBS with probability _ηi_ , in which case the _Z_ -basis detector click is caused by a dark count, or the photon is reflected by the TBS with probability 1 − _ηi_ , causing a click in the _Z_ -basis detector (recall that the efficiency _ηZ_ of the _Z_ -basis detector is factored out in the quantum channel). Besides, the erroneous outcome in the _X_ -basis detector could be caused by the transmitted photon localized in _Z_ , but also by a dark count or by any number of photons not localized in _Z_ . Then, the probability term that we 

considered can be expressed as a sum of two terms corresponding to the scenarios with the transmitted or reflected photon: 



(C114) where the action of the TBS on the single photon in _Z_ is made explicit by the prefactors _ηi_ and 1 − _ηi_ . In Eq. (C114), the quantities E<sup>1</sup> _η_<sup>_t_</sup> _l_<sup>andE1</sup> _η_<sup>_r_</sup> _l_<sup>dependonthe</sup> input states _σk_ and their interaction with the _X_ -basis detector, but also nontrivially depend on the TBS transmittance _ηl_ —indeed, _σk_ can contain an arbitrary number of photons outside _Z_ . In Appendix C 4 h we provide a rigorous proof of the result in Eq. (C114) and derive similar decompositions for the other terms in Eqs. (C109) and (C110) [see – Eqs. (C350) (C355)]: 



where again the action of the TBS on the photon localized in _Z_ is singled out by the factors containing _ηi_ . 

The notable fact from Eqs. (C114)–(C119) is that _ηi_ is factored out of the variables E<sup>0</sup> _ηl_<sup>, E</sup> _η_<sup>0,1</sup> _l_<sup>, E</sup> _η_<sup>1</sup><sup>_r_</sup> _l_<sup>, and E</sup> _η_<sup>1</sup><sup>_t_</sup> _l_<sup>. There-</sup> fore, any choice of _ηi_ affects the test-round bit error rates only through the coefficients with which the variables E<sup>0</sup> _ηl_<sup>,</sup> E<sup>0,1E1</sup><sup>_r_andE1</sup><sup>_t_inEqs.(C114)–(C119).Thus,</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>appear</sup> by using Eqs. (C114)–(C119) in the expansions (C109) and (C110), we can derive a linear system of equations [see Eq. (C356)] 



044011-31 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

in the variables E<sup>0and E1</sup><sup>_t_simplychoos-</sup> _ηl_<sup>, E</sup> _η_<sup>0,1</sup> _l_<sup>, E</sup> _η_<sup>1</sup><sup>_r_</sup> _l_<sup>,</sup> _ηl_<sup>by</sup> ing different values of _ηi_ . In particular, each equation in the above system corresponds to three different equations depending on the setting _ηi_ ∈{ _η_ ↑, _η_ ↓, _η_ 2}. Note that the left-hand sides, i.e., the test-round bit error rates restricted to the (≤ 1)-subspace (C107) and (C108), can be considered as known quantities since they have been tightly bounded with upper and lower bounds that are given in terms of observed statistics. 

In Appendix C 4 i, we solve the linear system in Eq. (C120) and provide the solution for E<sup>0</sup> _ηl_<sup>,E0,1</sup> _ηl_<sup>,E1</sup> _η_<sup>_r_</sup> _l_<sup>,</sup> and E<sup>1</sup><sup>_t_</sup> _ηl_<sup>in terms of the test-round bit error rates restricted</sup> to the (≤ 1)-subspace. Subsequently, we replace the latter with their respective upper or lower bound in such a way that the resulting expressions are upper bounds on the quantities E<sup>0</sup> _ηl_<sup>,E0,1</sup> _ηl_<sup>,E1</sup> _η_<sup>_r_</sup> _l_<sup>,andE1</sup> _η_<sup>_t_</sup> _l_<sup>.Weindicatesuch</sup> ~~0 0~~ ,1 ~~1~~ _r_ ~~1~~ _t_ bounds with E E E<sup>and</sup> E<sup>reportthemin</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>and</sup> Eqs. (B22)–(B25). The variables E<sup>0</sup> _ηl_<sup>,E0,1</sup> _ηl_<sup>,E1</sup> _η_<sup>_r_</sup> _l_<sup>,andE1</sup> _η_<sup>_t_</sup> _l_ appear with positive signs in the phase error rate and thus should be replaced by their upper bounds if they cannot be computed explicitly. 

~~0 0~~ ,1 ~~1~~ _r_ ~~1~~ _t_ We can now use the bounds E E E<sup>and</sup> E _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_ to obtain an upper bound on the first term of the phase error rate bound in Eq. (C103). Indeed, by combining – Eqs. (C114) (C119) with Eq. (C113), we obtain the upper bound: 



where each quantity on the right-hand side is either known or directly expressed in terms of observed statistics. Recall that _p_ ✓| _α_ was introduced after Eq. (C97). 

The remaining term to be estimated, in order to complete the estimation of the phase error rate, is the second term in the phase error rate bound (C103), which can be interpreted as the weight of the average state received by Bob in the subspace with zero photons in the modes _X_ , restricted to the (≤ 1)-subspace. By expanding it through Eq. (C100), we obtain three terms 



corresponding to the projections in the subspaces of _�_<sup>0</sup> _Z_<sup>,</sup> and _�_<sup>1</sup> _Z_<sup>,ortheoff-diagonalterm.Wededucethatacor-</sup> rect estimation of the term of interest requires estimating individually the three terms on the right-hand side of 

Eq. (C122). To this aim, we need to combine two methods that have already been used in the proof, namely, the detector decoy technique [used to extract the weight of _σ_ ¯ outside the (≤ 1)-subspace with Eq. (C98)] and the method based on linear equations [used to estimate the single terms in the expansion (C113)]. For this reason, the accurate estimation of the three terms in Eq. (C122) can be seen as the more sophisticated procedure of the whole proof. 

The first step considers the test-round yields _Y_ 1,<sup>_X_,</sup> _(η_<sup>✓</sup> _l_ , _ηl)_<sup>and</sup> _Y_<sup>_X_,∅</sup> 1, _(ηl_ , _ηl)_<sup>, i.e., the probability that the</sup><sup>_X_-basis detector clicks</sup> and the _Z_ -basis detector clicks or does not click, respectively (see Appendix A). Their sum can be expressed in terms of Bob’s POVM elements: 



In Appendix C 4 f we show that the following equality holds: 



which can be seen as the POVM element corresponding to a detection in the _X_ -basis detector when the TBS setting is _(ηl_ , _ηl)_ . From the last expression, we can immediately obtain the POVM element describing no detection in the _X_ -basis detector: 



where we used the fact that<sup>�∞</sup> _β_ =0<sup>_�_</sup> _X_<sup>_β_= 1. Now, we real-</sup> ize that the three terms in Eq. (C122) can be recovered from the right-hand side of Eq. (C125) if we project the operator on the subspaces of _�_<sup>0</sup> _Z_<sup>or</sup><sup>_�_1</sup> _Z_<sup>.Bydoingso</sup> on both sides of the operator equation in Eq. (C125), we obtain 



for _α_ = 0, 1. We can now take the expectation value of the operator in Eq. (C126) on the state _σ_ ¯ and obtain the following equation, which contains two of the three terms in Eq. (C122): 

044011-32 

en (1 ]) [NE EE ER A > lon mn | ~~}~~ noon 1 [mz nm] [ |] [nx om] [] prs on) oT | | ~~BN~~ <u>:</u> [ oll ] ~~_ i J~~ n n mn on ~~[~~ [ I EE |] ( ) ~~<u>[(</u>~~ lon m1 | 



<!-- Start of picture text -->
oll | |<br>> I E<br>BN nn n<br>oll<br>[c(T IT I |] [eI Omonj<br>J [ellTT IJ<br>[cT1 TT I ] [cl TT I | n<br>nmmn] [ ]<br>orn] (TT) LL<br>en n Co [1<br>[10]<br>[ on] 01 01<br>[oc IT IT ] _<br>[cl TT I | uy<br>[c(T IT I ]<br>| [enIm 1 |<br>Jl A -)l<br>1 (1) 7]<br>— a 7)<br><!-- End of picture text -->

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 



<!-- Start of picture text -->
vac vac<br>vac<br><!-- End of picture text -->

FIG. 6. Bob’s measurement apparatus. In each round, the incoming signal (mode _a_ ) enters a TBS described by the unitary _U(ηi_ , _ηl)_ , where _(ηi_ , _ηl)_ is the TBS setting for that particular round. The transmitted mode (mode _c_ ) is detected by an _X_ -basis detector with efficiency _ηX_ and dark count probability _pd_<sup>_X_for</sup> each outcome. This is modeled by a beam splitter [ _U(ηX )_ ] followed by a perfect detector with dark count probability _pd_<sup>_X_. The</sup> reflected mode (mode _c_<sup>′</sup> ) is detected by a _Z_ -basis detector with efficiency _ηZ_ and dark count probability _pd_<sup>_ZX_</sup> per outcome, which is similarly modeled. Note that the insertion loss of the TBS is 

and where we replaced the one-photon _Z_ -basis yield with the corresponding lower bound from the decoy-state method. We emphasize that all the quantities appearing in Eq. (C151) are either known or obtained with the decoystate method (see Appendix D for the formulas for the decoy-state method). This concludes the derivation of a computable upper bound on the phase error rate. 

## **_b. Bob’s measurement apparatus_** 

We now detail the missing steps of the argument. The method that we introduce to estimate the phase error rate relies on a partial characterization of Bob’s measurement apparatus, as described in Sec. III. In Fig. 6, we provide a model of Bob’s measurement apparatus. Here, the nonunit detection efficiency of the _Z_ -basis detector ( _X_ -basis detector) is modeled by a beam splitter with transmittance _ηZ_ ( _ηX_ ), described by the unitary _U(ηZ)_ [ _U(ηX )_ ]. The TBS is described by a unitary _U(ηi_ , _ηl)_ acting on spatial-temporal modes _a_<sup>†</sup> _t_<sup>and</sup><sup>_b_†</sup> _t_<sup>as follows:</sup> 



> where _Z_ =<sup>�</sup><sup>_d_</sup> _j_ =<sup>−</sup> 0<sup>1</sup><sup>_Zj_istheunionofallthemodesthat</sup> are detected by the _Z_ -basis detector. In the case where the _Z_ -basis detection is a time-of-arrival measurement, _Z_ corresponds to the union of all the time bins. We recall that, in each round, Bob selects one of the following six TBS settings: _(ηi_ , _η_ ↑ _)_ and _(ηi_ , _η_ ↓ _)_ , with _η_ 1 = _η_ ↑, _η_ 3 = _η_ ↓, and _η_ 2 satisfying _η_ ↓ _< η_ 2 _< η_ ↑. Moreover, we recall that the TBS 



<!-- Start of picture text -->
vac vac vac<br><!-- End of picture text -->

FIG. 7. Bob’s simplified measurement apparatus. Here the common loss of the two detectors in Fig. 6—which amounts to 1 − _ηZ_ —has been factored outside Bob’s apparatus, leaving an ideal detector in the _Z_ basis and a lossy detector in the _X_ basis with efficiency _ηr_ = _ηX /ηZ_ . 

settings and the detection efficiencies of the two detectors must satisfy Eqs. (9) and (10). 

In our formalism, the unitary _U(η)_ maps the input modes m<sup>†</sup> 1<sup>=</sup><sup>_a_†,</sup><sup>_c_†,</sup><sup>_c_′†andm†</sup> 2<sup>=</sup><sup>_b_†,</sup><sup>_d_†,</sup><sup>_d_′†totheoutput</sup> modes M<sup>†</sup> 1<sup>=</sup><sup>_c_†,</sup><sup>_e_†,</sup><sup>_e_′† and M†</sup> 2<sup>=</sup><sup>_c_′†,</sup><sup>_f_†,</sup><sup>_f_′†, respectively,</sup> as follows: 





where we have 0 _< ηr <_ 1 since we assumed in Sec. III that the detector used to generate key bits is more efficient. This is a sensible assumption that typically leads to better key rates; however, if not verified, one can always exchange the roles of the two bases. Then, we can reexpress the efficiency of the _X_ -basis detector as _ηX_ = _ηZηr_ , which allows us to factor out the transmittance that is shared by the two detectors, namely, _ηZ_ . In particular, we can equivalently describe Bob’s apparatus as depicted in Fig. 7, where we introduced a beam splitter with transmittance _ηZ_ before Bob’s apparatus, which accounts for the common loss of both detectors, and replaced the _Z_ -basis 

044011-35 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

detector ( _X_ -basis detector) detector with a lossless detector (lossy detector with efficiency _ηr_ ). This equivalence is well known in quantum optics; see, e.g., Ref. [56]. 

Furthermore, we argue that it can be advantageous to Eve only if we give her control over the beam splitter preceding Bob’s apparatus [ _U(ηZ)_ ] by viewing it as part of the insecure channel between Alice and Bob. Therefore, from now on, we ignore the unitary _U(ηZ)_ and describe Bob’s apparatus as depicted in Fig. 7. 

## **_c. Bob’s Z-basis detector_** 

The next step of the proof consists of a reduction of the phase error rate to the subspace with at most one photon in the interval _Z_ , which we call the “(≤ 1)-subspace” for brevity. Intuitively, this is the subspace where most of the states in { _σk_ } _k_ should lie in the absence of an eavesdropper. 

_Remark 3._ We recall that _σk_ is the state received by Bob when Alice encodes the test symbol _XA_ = _k_ on a single photon. However, since we do not restrict Eve’s collective attack, we cannot assume that the states { _σk_ } _k_ are confined to, for example, the subspace with at most one photon. Eve could perform attacks where she adds photons to the states sent by Alice. This could allow her to control the click probability of the two bases if they have asymmetric detection efficiencies. We emphasize that while previous analytical QKD proofs are restricted to the one-photon subspace when dealing with detection efficiency mismatches [11,33,34], our proof can accommodate both mode-dependent and mode-independent mismatches in the detection probability without posing any constraint on the states received by Bob. 

Because, as argued in Remark C3, we do not constrain the states _σk_ , we are forced to estimate their weight in the (≤ 1)-subspace, enabling us to reduce the calculation of the phase error rate to the (≤ 1)-subspace. 

The estimation of the states’ weight in the (≤ 1)subspace is done from the statistics of the _Z_ -basis detector. Thus, as the first step, we derive an explicit expression for some of the elements of the POVM { _(Z_ 0 _)c_ ′, _(Z_ 1 _)c_ ′, _. . ._ , _(Zd_ −1 _)c_ ′, _(Z_ ∅ _)c_ ′} that describes Bob’s _Z_ - basis measurement in the reflected mode of the TBS, where the subscript indicates the spatial mode on which the operator acts (see Fig. 7). 

Let _�_<sup>_α_</sup> _Z_<sup>be the projector of</sup><sup>_n_=</sup><sup>_α_photons in the global</sup> detection interval _Z_ , while acting as the identity outside the interval _Z_ . Then the POVM element corresponding to a detection of one of the _d_ outcomes would be _(Z_ ✓ _)c_ ′ = _d_ −1 � _j_ =0<sup>_(Zj )c_′= �∞</sup> _α_ =1<sup>_(�_</sup> _Z_<sup>_α)c_′in the absence of dark counts,</sup> i.e., the projector in the subspace with at least one photon in _Z_ . Note that this is true since we assumed that multiclick events are always mapped to a single outcome (see Sec. III). However, since the detector has a dark count probability _pd_<sup>_Z_peroutcome,thePOVMelementcorresponding</sup> 

to a detection becomes 



where _pd_<sup>_Z_isdefinedinEq.(B2).Notethatifthe</sup><sup>_Z_-basis</sup> detector implemented a time-of-arrival measurement, the projector _�_<sup>_α_</sup> _Z_<sup>would be given by</sup> 



with exactlywhere _�_<sup>_α_</sup> _Z_ , _n α_<sup>is the projector on the subspace of</sup> photons localized in the time interval<sup>_n_photons,</sup> _Z_ : 



where _Z_ is the complement of _Z_ in the time domain and |1 _t_ ⟩= _a_<sup>†</sup> _t_<sup>|vac⟩represents the unphysical state of one pho-</sup> ton at time _t_ . We have that _a_<sup>†</sup> _t_<sup>creates a photon at time</sup><sup>_t_as</sup> the Fourier transform of a photon with frequency _f_ : 



Moreover, it holds that [ _a_<sup>†</sup> _t_<sup>,</sup><sup>_a_†</sup> _t_<sup>′] = 0and[</sup><sup>_at_,</sup><sup>_a_†</sup> _t_<sup>′] =</sup><sup>_δ(t_−</sup> _t_<sup>′</sup> _)_ 1, which implies 



where _Sn_ is the set of all permutations of indexes in {1, 2, _. . ._ , _n_ }. To familiarize ourselves with this formalism, which allows _n_ photons to be arbitrarily delocalized in time, we can verify that 



holds. The following proof is not essential to the remainder of this appendix and can be skipped. 

044011-36 

PILED 5 yn ~~J~~ m ~~[——~~ | ~~— [|~~ py ~~f—~~ yf ~~————~~ ~~<u>[——</u>~~ ne ~~[——~~ Sr Snow fo ey ’ Yow 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

and (C156) for other degrees of freedom, while the time degree of freedom should be replaced by the measured degree of freedom in Eq. (C157). 

We have thus obtained the expression (C155) for the POVM element representing a detection in the _Z_ -basis detector, acting on the reflected mode _c_<sup>′</sup> . However, the actual measurement statistics are collected from Bob’s global measurement on the received signal (mode _a_ ), which comprises detections in both the _Z_ -basis detector and the _X_ -basis detector and is formally introduced in Eq. (C6). Nevertheless, similarly to Eq. (C7), from the global POVM (C6) we can define a POVM element on mode _a_ that corresponds to a detection in the _Z_ detector and ignores the outcome of the _X_ -basis detector: 



where the superscript indicates the TBS setting. Note that _Z_ ✓ _(η_ ↓, _η_ ↓ _)_ = _Z_ ✓, where _Z_ ✓ is the POVM element for a detection in Bob’s key generation measurement and it appears in the phase error rate. 

To obtain an explicit expression for _Z_ ✓<sup>_(ηl_,</sup><sup>_ηl)_</sup> , we first note that the one-photon _Z_ -basis yield with TBS setting _(ηl_ , _ηl)_ is, similarly to Eq. (C51), given by 



where in the second equality we used a generalization of Eq. (C39) and in the third equality the fact that Eq. (7) holds, together with a shorthand notation for the average state received by Bob: 



with _σk_ given in Eq. (C74). At the same time, by using the scheme in Fig. 7 and the definition of the TBS unitary in 

Eq. (C152), we have 



By comparing Eqs. (C172) and (C174), we deduce an expression for the operator in Eq. (C171): 



where in the second equality we used Eq. (C155). We now define the following operator acting on mode _a_ : 



We can explicitly calculate _Q_ by applying the unitary _U(ηl)_ according to Eq. (C153). To do so, we make _(�_<sup>_α_</sup> _Z_<sup>_)c_′and1</sup><sup>_c_explicitaccordingtoEqs.(C156),(C157),</sup> and (C160). Then, by linearity, we obtain some terms like the following: 



which corresponds to a pure state on mode _a_ . By using Eq. (C177) in Eq. (C176) and by reparametrizing the resulting sums, we obtain 



By using this expression in Eq. (C175), we find the final expression for the POVM element (C171) describing a detection in the _Z_ -basis detector with the TBS setting 

044011-38 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

_(ηl_ , _ηl)_ : 



This operator has a twofold purpose. First, by recalling the definition of Bob’s key generation measurement in Eq. (C7), it provides us with the explicit expression for the operator _Z_ ✓ that appears in the phase error rate formula (C94): 



where we identified _p_ ✓| _α_ as the probability of a detection in the _Z_ -basis detector, given that the state received by Bob contains _α_ photons localized in the detection interval _Z_ , 



We also specify the above expression for the cases _α_ = 0 and _α_ = 1: 





Secondly, the operator in Eq. (C179) allows us to estimate the weight of the states received by Bob in the (≤ 1)-subspace, through the detector decoy technique [28]. 

## **_d. The detector decoy technique applied on the Z-basis detector statistics_** 

The detector decoy technique [28] is a powerful tool that allows one to estimate the weight of measured states in various subspaces with a fixed photon number. In our case, for the purpose of reducing the phase error rate calculation to the (≤ 1)-subspace, we are interested in estimating the weight of the average state received by Bob in the subspaces defined by _�_<sup>0</sup> _Z_<sup>and</sup><sup>_�_1</sup> _Z_<sup>. More precisely, let</sup> 



be the weight of _σ_ ¯ in the subspace with _α_ photons localized in _Z_ . Then the goal is to derive upper and lower bounds on Tr[ _σ�_ ¯<sup>0</sup> _Z_<sup>] and Tr[</sup><sup>_σ�_¯1</sup> _Z_<sup>].</sup> 

To this aim, we will use the statistics of the no-detection events in the _Z_ -basis detector with TBS setting _(ηl_ , _ηl)_ , 

which are generated by the following POVM element: 



where we used Eq. (C179). Therefore, the probability of no detection in the _Z_ -basis detector reads 



The detector decoy technique is based on a set of equations of the following form: 



where _fl_ are known quantities that are experimentally observed, _yα_ ∈ [0, 1] are the variables that are to be bounded, and _ηl_ is a parameter that can be fixed to different values by one varying _l_ . In our case, Eq. (C186) can be put in the form of Eq. (C187) by one identifying 





from which we deduce the normalization property of the variables { _yα_ } _α_ : 



We now apply the idea of the detector decoy technique to Eq. (C187) to derive an upper bound and a lower bound on _y_ 0 and _y_ 1. We recall that among Bob’s possible choices for the TBS setting (see Sec. III), we have _η_ 1 = _η_ ↑ and _η_ 3 = _η_ ↓. 

We start by deriving the upper bound on _y_ 0. Consider the following system of two inequalities, obtained from Eqs. (C187) and (C190): 

044011-39 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 



where in the second step we used the lower bound on _y_ 1 in the second inequality. From the bottom inequality in Eq. (C191), we can derive an upper bound on _y_ 0, provided that its coefficient is positive. We thus require that 



which is indeed satisfied since we assumed that the condition in Eq. (9) holds. Then the upper bound on _y_ 0 can be derived from Eq. (C191) and reads 



Finally, we substitute back the values for _η_ 1, _η_ 3, _fl_ , and _y_ 0 and obtain the desired upper bound on the weight of the state in the subspace with no photon in _Z_ in terms of observed quantities: 



with 



where we used the fact that _�_<sup>0</sup> _Z_<sup>≤1toimposethat</sup> _<u>w</u>_<sup>~~0~~</sup> _Z_<sup>≤1andwherewereplacedthetermscontainingtheyields</sup> _Y_<sup>_Z_</sup> 1, _(ηl_ , _ηl)_<sup>—which are unobserved—with a bespoke upper bound obtained with the decoy-state method (see Appendix D),</sup> such that the resulting expression is still a valid upper bound. 

Now we derive the upper bound on _y_ 1. To this aim, we consider the following system of inequalities: 



044011-40 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

where we used the lower bound on _y_ 0 in the second inequality of the second step. From the bottom inequality in Eq. (C196), we can derive an upper bound on _y_ 1, provided that its coefficient is positive, i.e., provided that 



holds, which is indeed the case since _η_ ↑ _> η_ ↓. Then from Eq. (C196) we obtain the following upper bound on _y_ 1: 



In the original variables this becomes 



with 



We now turn to the derivation of the lower bounds on _y_ 0 and _y_ 1. The lower bound on _y_ 1 can be obtained by one substituting the upper bound on _y_ 0, Eq. (C193), into the lower bound on _y_ 1 in Eq. (C191). By doing so and by simplifying the expression, we obtain 



which in the original variables becomes 



In a similar manner, we can substitute the upper bound on _y_ 1, Eq. (C198), into the lower bound on _y_ 0 from Eq. (C196). After some simplification, we obtain 



which in the original variables becomes 



044011-41 

~~— —~~ x ~~— —]~~ CC ~~— — — —]~~ > ~~— — DE —~~ > ] 

ol ] ol ] (z=) z= ] 

> 

] 

>] 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

and view _g(α)_ as a continuous function of _α_ ≥ 2. First, we observe that _g(α)_ is always non-negative: 



which is verified since 1 ≥ _η_ 1 and _η_ 2 ≥ _η_ 3. Then, we notice that _g(α)_ is a nondecreasing function of _α_ . Indeed, this amounts to showing that 





and a sufficient condition to prove the last inequality is obtained by one replacing _η_ 1<sup>_α_with</sup><sup>_η_</sup> 2<sup>_α_inthesecondterm(since</sup> _η_ 1 _> η_ 2): 



where the last inequality is true since _η_ 2 _> η_ 3. Hence, we showed that _g(α)_ is a nondecreasing function of _α_ and, in particular, it holds that 



We now use the last expression in Eq. (C209) and derive the inequality 



which leads to the following upper bound on the weight of the state _σ_ ¯ outside the (≤ 1)-subspace: 



Then the upper bound in the original variables reads 



with 



where in Appendix D we derive an upper bound tailored to the specific combination of yields in the numerator. 

044011-43 

nm 1 

~~J~~ 

> ~~Tm~~ > ~~Tm -~~ X | ~~Vx~~ , <u>Vv]</u> a a a ~~s~~ ox| Z, a ~~x~~ |x, ] ~~s~~ ox| ox, 

A 

AA 

A 

AA 

A > 

2 

2 > om 

dom 



<!-- Start of picture text -->
AY [on]<br>I Sa<br>0]<br>roy, | |<br>A a<br>NE { r r) a B<br>5<br>x<br>a LC) Te]<br>vi LC Te]<br>O N<br>- 2 - 2<br>aC)<br><!-- End of picture text -->

~~-~~ 



<!-- Start of picture text -->
A--<br>A A<br>A =» (rT r)<br>- y Tr<br>- 2<br>A TT - -<br>A ANT<br>A A<br>~ | — —<br>a x [ox]<br>A<br>A<br><!-- End of picture text -->

A 

2 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 



where we ignore the specific outcome of the _Z_ -basis detector and register onnly whether it clicks or does not click. Note that Bob’s test measurement, as defined in Eq. (C15), is recovered from Eqs. (C250) and (C251) as follows: 



Our goal is to derive explicit expressions for the POVM elements (acting on mode _a_ ) given in Eqs. (C250) and (C251). 

The first step is to describe the ideal _X_ -basis detector acting on mode _e_ in Fig. 7. Let _D_ := {0, 1, _. . ._ , _d_ − 1} be the set of outcomes of the _X_ -basis detector on mode _e_ and let _P(D)_ be the power set of _D_ . Recall that we assumed that Bob maps multiclick events _K_ ∈ _P(D)_ , i.e., events with clicks in the physical modes _Xl_ , for _l_ ∈ _K_ , to a single outcome. This can be formalized by an un-normalized right stochastic matrix _P_ ∈ M _P(D)_ \∅× _d_ , with elements 

_Remark 5._ By using Eqs. (C256) and (C257) in the computation of the POVM element corresponding to a detection in any outcome, _(X_ ✓ _)e_ , one obtains 





where Pr _(k_ | _K)_ represents the probability that the multiclick event _K_ is mapped to the single outcome _k_ . As explained in Sec. III, we assume that the following holds: III, we assume that the following holds:, we assume that the following holds: 

event _K_ is mapped to the single outcome _k_ . As which coincides with the analogous POVM element in the _Z_ basis, Eq. (C155), by using Eq. (B3) and by identiexplained in Sec. III, we assume that the following holds: III, we assume that the following holds:, we assume that the following holds: _d_ −1 fying _�_<sup>≥</sup> ∅<sup>1</sup> = _�_<sup>0</sup> _X_<sup>and�</sup> _X_ ∈ _P(D)_ \∅<sup>_�_</sup> _X_<sup>≥1= �∞</sup> _β_ =1<sup>_�_</sup> _X_<sup>_β_,with</sup> _�_<sup>_β_</sup> _X_<sup>beingtheanalogueforthe</sup><sup>_X_basisof</sup><sup>_�α_</sup> _Z_<sup>forthe</sup><sup>_Z_</sup> � Pr _(k_ | _K)_ = 1 for all _K_ ∈ _P(D)_ \ ∅, (C254) basis, namely, the projector on the subspace with _β_ pho- _k_ =0 tons in the interval _X_ and any number of photons outside i.e., that no event with at least one click is assigned to the _X_ . With these substitutions, we obtain 

i.e., that no event with at least one click is assigned to the no-detection event. In other words, every time there is at least one click (event _K_ = ∅), Bob assigns the event to outcome _k_ according to the distribution Pr _(k_ | _K)_ . Then, the POVM element corresponding to a detection of outcome _k_ , in the absence of dark counts, is given by 



Now we can compute the POVM element corresponding to outcome _k_ in the _X_ -basis detector, acting on the transmitted mode _c_ . According to the model in Fig. 7 and by one following the same approach that led to the derivation of Eq. (C175) this will be given by 



where _�_<sup>≥</sup> _K_<sup>1</sup> is the projector on the subspace with at least one photon in mode _Xl_ for each _l_ ∈ _K_ , and no photons in the other measured modes _Xm_ for _m_ ∈ _/ K_ . Note that the event _K_ = ∅ is excluded from Eq. (C255) since no-detection events are not mapped to measurement outcomes. We now consider that each mode _Xk_ may click with probability _pd_<sup>_X_, given that no photon is in that mode.</sup> Thus, we deduce that even the events where some of the clicks are caused by dark counts are mapped according to Eq. (C253), since Bob has no way to distinguish dark counts from actual detections. Therefore, the POVM element for outcome _k_ in the presence of dark counts becomes 



Alternatively, a faster way to obtain _(Xk)c_ is to observe that when each photon can be lost independently with probability 1 − _ηr_ , the POVM element _XK_ of the multiclick event _K_ receives contributions from any possible configuration of photons arriving at the detector. Thus, the relevant projector to express the operator in Eq. (C261) becomes 





which is defined as the projector on the subspace with _αk_ photons in mode _Xk_ , for _k_ = 0, _. . ._ , _d_ − 1. Moreover, we note that _XK_ will have the same structure as in Eq. (C257) if we interpret _S_ as the set of modes that contain at least one 

where _XK_ is the POVM element corresponding to the multiclick event _K_ . Clearly, _XK_ receives contributions from 

044011-47 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

photon after considering the detector’s nonunit efficiency [i.e., after applying _U(ηr)_ ]: 



where _MS_<sup>≥1</sup> is the POVM element of at least one photon in mode _Xs_ , after loss, for every _s_ ∈ _S_ . Thus, we can easily express _MS_<sup>≥1</sup> in terms of the projectors (C262) as follows: 



where _S_<sup>_c_</sup> = _D_ \ _S_ is the complement of _S_ in _D_ . 

In conclusion, the POVM element for outcome _k_ in the _X_ -basis detector with efficiency _ηr_ and dark count probability _pd_<sup>_X_per mode is given by</sup> 



with _MS_<sup>≥1</sup> given in Eq. (C264). Moreover, it will turn out to be useful to calculate the POVM element corresponding to a detection of any outcome in mode _c_ . This is achieved from Eq. (C261) as follows: 



where we used Eq. (C260) from Remark 5 in the last equality. Now we use the fact that a calculation similar to the one above has already been done for computing Eq. (C176) and resulted in Eq. (C178). Analogously, we obtain 



Now we have all the ingredients to compute the POVM elements defined in Eqs. (C250) and (C251). According to 

the scheme in Fig. 7, we have 



where _(Xk)c_ is given in Eq. (C265), _(Z_ ✓ _)c_ ′ is given in Eq. (C155), and _(Z_ ∅ _)c_ ′ = 1 _c_ ′ − _(Z_ ✓ _)c_ ′. 

Now that we have derived the POVM elements of interest, in the following subsection we link them to the corresponding one-photon yields and bit error rates, which in turn will be used to bound _�_ 1 in Eq. (C247). 

## **_g. One-photon X -basis yields and bit error rates_** 

By applying the decoy-state method on the detection statistics of the test rounds (see Appendix D), Alice and Bob can estimate the following one-photon _X_ -basis yields, which we call the “test-round yields”: 





Similarly, by applying the decoy-state method on the _X_ - basis gains (12) and (13) and on the _X_ -basis QBERs (15) and (16), the parties can estimate the following one-photon _X_ -basis bit error rates, also called the “test-round bit error rates”: 



We observe that the test-round yields, Eqs. (C270) and (C271), and the test-round bit error rates, Eqs. (C274) and (C275), do not depend only on the component of _σk_ in the (≤ 1)-subspace. 

044011-48 



<!-- Start of picture text -->
SI<br>> |[- xX nx, > on]<br>xr [n x, nlx [- mzZ, nm)<br>xr [m z, nm]<br>y| dom<br>x [- mz, nm] -<br>> [- (my, om ) Vt bn I} [en]<br>Jo<br>|<br>] = [- nx, =n]<br>x [m xz, nm]<br>ny, II<br>\<br>> [~ mx, no)<br><!-- End of picture text -->



<!-- Start of picture text -->
J<br>| | |<br>[EE I<br>J Vv<br>ny, mn<br>| = [n xz, nn]<br>||<br>|<br>J a.<br>[= [ nn]<br>[= [ nn]<br>[I<br><!-- End of picture text -->

<u>I</u> I A I ~~HE~~ ~~<u>E</u>~~ E ~~<u>RRC</u>~~ IR ~~Be~~ ~~<u>I E</u>~~ E ~~<u>RRC</u>~~ IR 

rrr EN (EE tem) EN (EE 

L ~~T~~ 

<u>J</u> ~~<u>T</u> 01~~ 

] 

J [om | | ) 

) (IT | ) 

n > 0 (I 

oom (I | n > 0 (I ] Y 1 (I ] 

ym 

2x@m @ >(I (I 

(I (I (I ; ’ [« I (T1 (I Tm] (I 

(1 

n 

( ’ 

(1 (I [( (I (T1 (I ] 

| | | ) (IT (Mm I (m (m | | | | ) (TT Mm 1 (I (I | | Ha m nom (mm ] | | | ) (IT (Mm I (m (m | [Hm Mm nom (mm 

[ I EE A 

I 

<u>I</u> ~~Ee~~ 

(EB 

[1 lem om] | ) (IT 

I EC | ) (IT 

Imo (I (Tl | Tm 1 (I (Tl | 

I EE I CER [Ha Mm no (mm | ) (IT m no a ] 2 ~~xf—) J~~ 2 ~~xf—) J]~~ 2 ~~x) J~~ 2 ~~<u>x) J</u> )~~ C7] |] <u>-</u> |] <u>}</u> 

~~xf~~ 



<!-- Start of picture text -->
a<br>[<br>[<br>xf J<br>xf)<br>CIC)<br>[1]<br><!-- End of picture text -->

EE ) |] ( ~~-~~ ) J I J I EE ~~A~~ | = ~~[m~~ nz, 0] | = ~~[~~ nz 0] | = ~~[m~~ nz, 0] J ~~[F~~ (@z, nm) | ~~[F~~ (@z, nm) | | 



<!-- Start of picture text -->
|I<br>|I<br><!-- End of picture text -->

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

By performing calculations analogous to those done for the test-round yields, each term in the expansions (C338) and (C339) can be recast as 



for some real numbers E<sup>0is singled</sup> _ηl_<sup>, E</sup> _η_<sup>0,1</sup> _l_<sup>, E</sup> _η_<sup>1</sup><sup>_t_</sup> _l_<sup>, and E</sup> _η_<sup>1</sup><sup>_r_</sup> _l_<sup>, where again the action of the TBS on the photon localized in</sup><sup>_Z_</sup> out by the factors containing _ηi_ . Therefore, we can use Eqs. (C350)–(C355) in the expansions (C338) and (C339) to derive the following linear system of equations: 



Analogously to the system in Eq. (C337) for the test-round yields, the left-hand sides can be treated as known quantities as they are tightly bounded in Eqs. (C286) and (C290). Hence, we can solve the system for E<sup>0</sup> _ηl_<sup>, E</sup> _η_<sup>0,1</sup> _l_<sup>, E</sup> _η_<sup>1</sup><sup>_t_</sup> _l_<sup>, and E</sup> _η_<sup>1</sup><sup>_r_</sup> _l_<sup>, such</sup> that we learn individually each term in the expansions (C338) and (C339). 

## **_i. Solving the linear systems_** 

In this section, we solve the linear systems in Eqs. (C337) and (C356). Since the two systems are formally identical, we discuss the solution of the one in Eq. (C337) and apply the result to the other system. 

The linear system in Eq. (C337) can be put in the following form, where we selected the second equation three times (for three values of _ηi_ ) and we selected the first equation for _ηi_ = _η_ 3: 



with the coefficient matrix given by 



044011-57 



<!-- Start of picture text -->
Te [A TH |<br>coc ab oo<br>TTT E [A TH |<br>—==9c J b |<br>—==i t | =m==—=cl |<br>—==9c J b |<br>LL<br>IEREEBR<br>(— RA EE CE | CN )<br>= == 0 Il J<br>— | = |<br>TE I A CE [ E e Ta<br>= 0 0 lL J<br>| |<br>( — JC 7 ) EE C E | CN )<br>= == Tl J<br>| | Ly —)<br><!-- End of picture text -->

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

_Remark 7._ With the choices made for _η_ 1, _η_ 2, and _η_ 3 in Eqs. (C359)–(C361), one can verify that the sign of each coefficient, of the restricted test-round yields in Eqs. (C362)–(C365), and of the restricted test-round bit error – rates in Eqs. (C362) (C365), is determined and known. 

We observe that the explicit expressions found for the variables Y<sup>0Y0,1Y1</sup><sup>_t_andY1</sup><sup>_r_E0,1E1</sup><sup>_t_and</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>(E</sup> _η_<sup>0</sup> _l_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> E<sup>1</sup><sup>_r_</sup> _ηl_<sup>) are given in terms of the test-round yields (test-round</sup> bit error rates) restricted to the (≤ 1)-subspace, which are not known exactly but are tightly bounded in Eqs. (C295) and (C296) [Eqs. (C286) and (C290)]. Then, by virtue of Remark 7, we can easily replace the restricted test-round yields (test-round bit error rates) with the respective upper or lower bound, depending on whether the yields (bit error rates) contribute positively or negatively to the phase error rate. 

In the following, we use the expressions derived for Y _η_<sup>0</sup> _l_<sup>,</sup> Y<sup>0,1Y1</sup><sup>_t_andY1</sup><sup>_r_E0,1E1</sup><sup>_t_andE1</sup><sup>_r_toobtain</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>(E</sup> _η_<sup>0</sup> _l_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>,</sup> _ηl_<sup>)</sup> the individual values of the three terms in the yields’ expansions (C302) and (C319) [bit error rates’ expansions (C338) and (C339)]. These are then used to derive an upper bound on _�_ 1, where it will become clear how to replace the restricted yields (bit error rates) with their respective bounds from Eqs. (C295) and (C296) [Eqs. (C286) and (C290)]. 

## **_j. Upper bound on �_ 1** **_: Part 1_** 

Here we derive an upper bound on the remaining contribution that is left to be estimated in the phase error rate upper bound, Eq. (C247), namely, _�_ 1 given in Eq. (C249). Initially, we aim at calculating an upper bound on the operator<sup>�</sup> _k_<sup>′</sup> = _k_<sup>_X_˜</sup><sup>_k_′appearingin</sup><sup>_�_1,where</sup><sup>_X_˜</sup><sup>_k_isthePOVM</sup> element defined in Eq. (C23) and reported here for clarity: 



where both _Xk_ and _X_ ✓ =<sup>�</sup> _k_<sup>_Xk_aretakenfromBob’s</sup> test measurement, Eq. (C252). According to Eqs. (C268) and (C269), we can obtain an expression for the POVM element _Xk_ of Bob’s test measurement, which corresponds to outcome _XB_ = _k_ in the _X_ -basis detector regardless of what happens in the _Z_ -basis detector and for the TBS setting _(η_ ↑, _η_ ↑ _)_ , as follows: 



where _U(η_ ↑ _)_ describes the unitary action of the TBS and where _(Xk)c_ is given in Eq. (C261). By using Eqs. (C261) in Eq. (C371), we notice that _Xk_ on mode _a_ is just the operator _(Xk)e_ , after letting the incoming mode traverse two lossy elements represented by beam splitters with transmittances _ηr_ and _η_ ↑, respectively. Thus, equivalently, we 

can compute _Xk_ as resulting from _(Xk)e_ after one lossy element with a combined transmittance of _ηrη_ ↑, represented by a unitary _U(ηrη_ ↑ _)_ mapping modes _a_ and _b_ to modes _e_ and _f_ . Thus, we obtain 



Then, by analogy with _(Xk)c_ in Eq. (C261), we can use the result in Eq. (C265) to deduce the final form of _Xk_ on mode _a_ : 



where _(MS_<sup>≥1</sup><sup>_)a_is defined as</sup> 



In a similar manner, we can obtain the expression for _X_ ✓, i.e., the POVM element corresponding to a detection in the _X_ -basis detector, regardless of what happens in the _Z_ -basis detector and for a TBS setting _(η_ ↑, _η_ ↑ _)_ . Indeed, from Eq. (C372) we have 





with _(X_ ✓ _)e_ given in Eq. (C260). Then, in analogy with the calculation performed for _(X_ ✓ _)c_ that led to Eq. (C267), from the last expression we obtain the desired expression: 



From Eq. (C376), we can easily obtain the inverse of its square root: 



where we used the fact that the projectors _�_<sup>_β_</sup> _X_<sup>are orthog-</sup> onal. Moreover, since<sup>�∞</sup> _β_ =0<sup>_�_</sup> _X_<sup>_β_= 1, we deduce that</sup><sup>_X_✓</sup> has support on the whole Hilbert space: 

044011-59 



<!-- Start of picture text -->
>. 2.on [TI ] =<br>><br>Sv<br>> ——————— nh [I ] =<br>by<br>>. 2. mn [TI ] =<br>><br>No ol Bh<br>>, —2<br>— x (zZ, ) 2 mn<br>2<br>> Xs ony<br><!-- End of picture text -->



<!-- Start of picture text -->
LE)<br>—X mn — —] ]<br>EL )<br>sa —v [= = ) |<br>— | nn]<br>A ) |<br>(I I 1)<br>—( | ])<br>([ I 1)<br>x [= =, ) |<br>EE ( )<br><!-- End of picture text -->



<!-- Start of picture text -->
> [= = )<br>EE ( ~ ~ )<br>~ — ] — ]<br>( — C= 7) ) ( = TC )<br>— cl I |<br>_<br>I<br>- ( — C= 7) )<br>— I a<br>( — JC ) ( 7 TC )<br>~<br>} ] [ ]<br>( — C= 7) ) ( — TC )<br>=== 50 I |<br>- 1 |<br><!-- End of picture text -->

[on] [cT1 TT I ] ~~—~~ [mom )] [clTT I | 

2 

- 

) 

mI 

|] 2 [om | 

on (10 1) 

on (101) 3 lon m1 | 

2 

jm 

i. 

3 lon m1 | 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 



We emphasize that the left-hand sides of the last two equations can be considered, for the moment, to be known quantities. Indeed, the variables Y _η_<sup>0</sup> _l_<sup>,Y</sup> _η_<sup>1</sup> _l_<sup>_t_,andY</sup> _η_<sup>1</sup> _l_<sup>_r_are</sup> expressed in terms of the test-round yields restricted to the (≤ 1)-subspace via the solutions (C362)–(C365) to the linear system (C337). In turn, the test-round yields restricted to the (≤ 1)-subspace are tightly bounded by observed quantities in Eqs. (C295) and (C296). At the same time, the weights of the average state with zero photons or one photon in _Z_ , namely, Tr[ _σ�_ ¯<sup>0</sup> _Z_<sup>]andTr[</sup><sup>_σ�_¯1</sup> _Z_<sup>],werealready</sup> bounded in Eqs. (C194), (C199), (C202), and (C204) when we applied the detector decoy technique to the statistics of the _Z_ -basis detector. 

We can thus use Eqs. (C403) and (C404) to derive an upper bound on the expectation values Tr � _σ�_ ¯<sup>0</sup> _Z_<sup>_�_0</sup> _X_<sup>_�_0</sup> _Z_ � and Tr � _σ�_ ¯<sup>1</sup> _Z_<sup>_�_0</sup> _X_<sup>_�_1</sup> _Z_ �. To this aim, we observe that Eqs. (C403) and (C404) are of the form 



which allows us to apply the detector decoy technique, 



(see Sec. III). From Eqs. (C405) and (C410) we obtain the following system of inequalities: 



where in the second step we used the lower bound on _x_ 1 in the second inequality. From the bottom inequality in Eq. (C411), we can derive an upper bound on _x_ 0 provided that its coefficient is positive. We thus require that 









which is indeed satisfied since we assumed that the condition in Eq. (10) is satisfied. Then the upper bound on _x_ 0 follows from the bottom inequality in Eq. (C411) and reads 

from which we deduce the following conditions on _xβ_ : 



We now apply the detector decoy technique to derive an upper bound on _x_ 0, and thereby on two of the expectation values in Eq. (C396). We recall that _η_ 1 = _η_ ↑ and _η_ 3 = _η_ ↓ 



By substituting the original variables through Eqs. (C406), (C407), and (C408), we obtain the desired upper bound on the weight of the state in the subspace with no photons in _X_ and in _Z_ : 

044011-64 

[cllIT I ] 



<!-- Start of picture text -->
oll oll |<br>oll oll<br>[1<br>oll - _<br>Re a<br>(— JC 7) Lo<br>(— JC 7 il I |<br>- |= L<br>(— C7 7) I J<br>(— JC 7 Lo<br>EE —<br>[cll TT I ]  rrr]<br>oll oll<br>[1<br><!-- End of picture text -->



<!-- Start of picture text -->
EE GE I CU<br>_<br>i [ |<br>( — D H C— HC ) = H e — J HC)<br>|]<br>( — J H C HC)<br>ob —L 1]<br>[|] |]<br>- ( — HC HC Hy = H e — J HC)<br>|]<br>( — J H C HC)<br>ol —1 7]<br>)<br>[c(1 IT TT ]<br>[cT1TT IT |<br>[ol TT 10 ] | form mom |<br>| vo<br><!-- End of picture text -->



<!-- Start of picture text -->
[c(T IT TT ] J enmnoonom]<br>[c(T TT TT ] (C71)<br>so ———[ 7 —<br>= ( 7 )<br>— tr (7) 07<br>C—O Bl<br>— on<br>—@ 7 )<br>ST<br>SL<br>_<br><!-- End of picture text -->

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

## **5. Secret key rate** 

In this subsection we complete the security proof of Protocol 1. 

We combine the upper bound obtained on the phase error rate (C436) with the entropy bound (C87) to derive the following bound on the entropy of interest: 



where we used the fact that _u(x)_ in Eq. (20) is a monotonically nondecreasing function. We now use Eq. (C438) in Eq. (C56), together with Eqs. (C47) and (5), to derive the following lower bound on the first entropy that appears in the DW rate (C3): 



where we replaced the yields by their lower bounds obtained with the decoy-state method (see Appendix D). Finally, we use the lower bound in Eq. (C439) and the upper bound in Eq. (C33) in the DW rate (C3), together with Eq. (C4), to obtain the following lower bound on the asymptotic key rate of the protocol: 



This coincides with the key rate provided in the protocol’s description, Eq. (17), thereby concluding the security proof. 

## **APPENDIX D: DECOY-STATE METHOD** 

In this appendix, we provide upper and lower bounds on zero-photon and one-photon yields and bit error rates, following the standard procedures of the decoy-state method. Such bounds are required by the phase error rate upper bound, Eq. (B1), as well as in the final expression for the protocol’s key rate (17). Moreover, we provide bounds on specific linear combinations of one-photon yields, which appear in Eqs. (B5)–(B9). 

## **1. Standard equations of the decoy-state method** 

We recall from Sec. III that Alice prepares WCPs with three different intensities: _S_ = { _μ_ 1, _μ_ 2, _μ_ 3}, with _μ_ 1 _> μ_ 2 + _μ_ 3 and _μ_ 2 _> μ_ 3 ≥ 0 . The parties use all three intensities both to generate the key and to derive the decoy bounds. The equalities on which the decoy-state method relies relate the unobserved yields to the observed gains. For instance, by definition (11), the _Z_ -basis gain is the probability that Bob has a detection in the _Z_ -basis detector, given that Alice sent one of the _Z_ -basis states with intensity _μj_ and that Bob chose the TBS setting _(ηl_ , _ηl)_ , and can be expressed as follows: 



where _Z_ ✓<sup>_(ηl_,</sup><sup>_ηl)_</sup> is defined in Eq. (C171) and _ρZi(μj )_ is given in Eq. (3). By using Eqs. (3) and (5), we can recast the gain as follows: 



where in the last equality we defined the _n_ -photon _Z_ -basis yield ( _Yn_<sup>_Z_</sup> , _(ηl_ , _ηl)_<sup>), by generalizing Eq. (C172).</sup> 

044011-68 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

Similarly, the _X_ -basis gain in Eq. (12) is defined as the probability that Bob has a detection in the _X_ -basis detector and in the _Z_ -basis detector, given that Alice sent a state of the _X_ -basis with intensity _μj_ and Bob selected the TBS setting _(ηi_ , _ηl)_ . It can be expressed as 



where _X_ ✓<sup>_(η_</sup> ,✓<sup>_i_,</sup><sup>_ηl)_</sup> is defined in Eq. (C272) and _ρXk (μj )_ is given in Eq. (6). By using Eq. (6), we can express the gain in terms of the _X_ -basis yields: 



where we defined the _n_ -photon _X_ -basis yields ( _Yn_<sup>_X_</sup> ,<sup>,</sup> _(η_<sup>✓</sup> _i_ , _ηl)_<sup>) as a generalization of Eq. (C270). Analogously, we express the</sup> gain in Eq. (13) as follows: 



where _Yn_<sup>_X_</sup> ,<sup>,</sup> _(η_<sup>∅</sup> _i_ , _ηl)_<sup>generalizes Eq. (C271) to</sup><sup>_n_photons.</sup> 

On the same lines, one can relate the _n_ -photon _X_ -basis bit error rates to the corresponding observed QBERs. In particular, the QBER in Eq. (15) is the probability that Bob’s _X_ -basis outcome differs from Alice’s _X_ -basis symbol, given that Bob had a detection in both detectors, Alice chose intensity _μj_ , and Bob chose the TBS setting _(ηi_ , _η_ ↑ _)_ . Then, the product of this QBER and the corresponding _X_ -basis gain reads 



wherethe _X_ -basis yields and bit error rates as follows: _Xk(η_<sup>′</sup> ,✓ _i_ , _η_ ↑ _)_ is defined in Eq. (C250). By using Eq. (6), we can expand the last expression in terms of the products of 



where we defined the _n_ -photon _X_ -basis bit error rate ( _eX_ , _n_ , _(ηi_ , _η_ ↑ _)_ ,✓) as a generalization of Eq. (C274). Analogously, we have 



where _eX_ , _n_ , _(ηi_ , _η_ ↑ _)_ ,∅ generalizes Eq. (C275). 

## **2. Bounds on yields and bit error rates** 

We observe that the equations defining the decoy-state method, namely, Eqs. (D2), (D4), (D5), (D7), and (D8), share the same structure, which can be exemplified as follows: 



where _Gμj_ can be replaced by a gain or a product of QBER and gain, while _Yn_ can be replaced by a yield or a product of yield and bit error rate. Then, starting from Eq. (D9) and following the procedure in the seminal paper on the decoy-state 

044011-69 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

method [39], one obtains the following lower bounds on the vacuum and one-photon yields: 



With similar techniques, one can derive a simple upper bound on the one-photon yield. To derive it, consider the following combination of gains in Eq. (D9): 



Now observe that the sum on the right-hand side is composed only of non-negative terms since _μ_ 2 _> μ_ 3. Therefore, we can obtain the inequality 



which provides us with the upper bound on the one-photon yield: 



An alternative upper bound on _Y_ 1 can be obtained by our using the statistics from all the intensity choices of Alice. In particular, we use the following linear combination of three gains: 



where we introduced 



Now we observe that _f (_ 1 _)_ is negative: 



044011-70 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

which is true since _μ_ 3 _< μ_ 2 _< μ_ 1. At the same time, we can show that _f (n)_ ≥ 0 for _n_ ≥ 3, as follows: 



which is verified since _μ_ 3 _< μ_ 2 _< μ_ 1. Then we can derive an upper bound on _Y_ 1 by replacing _Yn_ with 1 in Eq. (D15), which yields 



where we can simplify the sum running over _n_ as follows: 



By using the last expression in Eq. (D19), we obtain the following upper bound on the one-photon yield: 



By combining Eqs. (D14) and (D21), we come to the final upper bound on the one-photon yield: 



We can now substitute the appropriate yields and bit error rates in the generic bounds in Eqs. (D10), (D11), and (D22) to derive the required bounds appearing in the phase error rate upper bound (C437) and in the key rate expression (C56). For instance, by using the bound (D10) on the relations (D2), (D4), (D5), (D7), and (D8), we obtain, respectively, 



044011-71 



<!-- Start of picture text -->
—<br>EE —<br>0)<br>— ge<br>—<br>EE —<br>—)<br>— ge<br>0)<br>— ge<br>a<br>EE ————<br>So<br>EE ————<br><!-- End of picture text -->

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

Finally, we use the bounds (D11) and (D22) on Eqs. (D7) and (D8) to obtain 



and 



for _ηi_ ∈{ _η_ ↑, _η_ ↓, _η_ 2}. 

## **3. Bounds on linear combinations of yields** 

– Some of the quantities appearing in the phase error rate bound (B1), namely, Eqs. (B5) (B9), depend on linear combinations of one-photon _Z_ -basis yields. In principle, in these expressions we could use the bounds already derived for the single yields. However, to obtain a tighter bound, in the following we derive bounds on the whole linear combination of the yields. 

– To start with, we observe that the linear combinations of yields in Eqs. (B6) (B9) can be generically written in the form 



044011-73 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

where the coefficients _c_ ↑ and _c_ ↓ depend on the particular linear combination that is considered. Then we can obtain a tighter upper bound on Eq. (D38) by considering the following equation: 





We observe that Eq. (D39) has the same form as the standard equation of the decoy-state method, Eq. (D9), with the important difference that the new gains ( _G_<sup>˜</sup><sup>_Z_</sup> _μj_<sup>) and new yields (</sup><sup>_Y_˜</sup> _n_<sup>_Z_) are not necessarily non-negative. In other words, while</sup> 0 ≤ _Yn_ ≤ 1 for every yield, this is not true anymore for _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>. Nevertheless, we can still apply the techniques of the standard</sup> decoy-state method to Eq. (D39), as far as we can obtain an interval of existence for the new yields _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>.</sup> 

To this aim, we recall from Eq. (D2) that the _n_ -photon _Z_ -basis yield can be written as 



with 



By using Eq. (C179) for _Z_ ✓<sup>_(ηl_,</sup><sup>_ηl)_</sup> in Eq. (D42), we can express the new yield (D41) as follows: 



From the last expression, we can immediately derive an interval of existence for _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>:</sup> 





Clearly, the interval of existence of _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>is independent of</sup><sup>_n_(as for the standard yields) but depends on the particular linear</sup> combination of yields, i.e., on _c_ ↑ and _c_ ↓. It is useful to derive a necessary and sufficient condition for the terms in Eqs. (D46) and (D47) to be increasing with _α_ , 



which can then be applied to the specific cases of _c_ ↑ and _c_ ↓. 

044011-74 



<!-- Start of picture text -->
—<br>><br>)<br>J p pa—<br>(1 1 I 1 I<br>C T 1 I<br>T l 1 I 1 ho]<br>(0 ] }<br><!-- End of picture text -->

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

we define _f (α)_ to be the argument of the optimizations in Eqs. (D46) and (D47), 



and find the condition for which its first derivative is non-negative: _f_<sup>′</sup> _(α)_ ≥ 0. We obtain 



which implies _α <_ 1. Thus, we conclude that _f (α)_ is minimal at the two extremes of _α_ ’s range— _f (_ 0 _)_ and _f (_ ∞ _)_ —and since _η_ ↑ _> η_ ↓ _(_ 1 − _η_ ↓ _)_ , we get 





while for _Y_ ˜<sup>_Z_</sup> we used the definition (D41) and the fact that 0 ≤ _Yn_<sup>_Z_≤1.</sup> (3) For _c_ ↑ = − _(_ 1 − _η_ ↓<sup>2</sup><sup>_)_and</sup><sup>_c_↓= −1:InthiscasetheconditioninEq.(D48)becomes</sup><sup>_η_</sup> ↓<sup>_α_≥</sup><sup>_(_1 +</sup><sup>_η_↓</sup><sup>_)(_1 −</sup><sup>_η_↑</sup><sup>_)η_</sup> ↑<sup>_α_,</sup> which is verified for _α_ = 0. Similarly to before, we define _f (α)_ to be the argument of the optimizations in Eqs. (D46) and (D47), 



and find the condition for which its first derivative is non-negative: _f_<sup>′</sup> _(α)_ ≥ 0. We obtain 



which implies that _f (α)_ stops increasing for a value _α >_ 0. Thus, _f (α)_ has its global minimum in either _α_ = 0 or _α_ = ∞. We obtain 





where for _Y_ ˜<sup>_Z_</sup> we again used the definition (D41) and the fact that 0 ≤ _Yn_<sup>_Z_≤1.</sup> (4) For _c_ ↑ = 1 and _c_ ↓ = 1 − _η_ ↑<sup>2:InthiscasetheconditioninEq.(D48)becomes</sup><sup>_(_1 +</sup><sup>_η_↑</sup><sup>_)(_1 −</sup><sup>_η_↓</sup><sup>_)η_</sup> ↓<sup>_α_≤</sup><sup>_η_</sup> ↑<sup>_α_,which</sup> is not verified for _α_ = 0 due to Eq. (9). Therefore, given that _f (α)_ is the argument of the optimizations in Eqs. (D46) and (D47), 



we found that _f (_ 0 _) > f (_ 1 _)_ . Now we find the condition for which its first derivative is negative: _f_<sup>′</sup> _(α) <_ 0. We obtain 



and since we know that _f (_ 0 _) > f (_ 1 _)_ , it must be that _f (α)_ stops decreasing at some point greater than zero. Then we conclude that _f (α)_ is maximal at the extremes and we obtain 





where for _<u>Y</u>_<sup>˜</sup><sup>_Z_</sup> we used the definition (D41) and the fact that 0 ≤ _Yn_<sup>_Z_≤1.</sup> 

044011-76 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

Finally, we derive an upper bound on the linear combination of yields that appears in Eq. (B5), namely, 



This can again be done by our applying the decoy-state method on the formula in Eq. (D39), where this time we define the gain and the yield to be 



Our goal is to derive an upper bound on _Y_<sup>˜</sup><sup>_Z_</sup> 1<sup>. Similarly to Eq. (D44), we can recast the newly defined yield in Eq. (D69) as</sup> follows: 



where we introduced 



˜ To derive an interval of existence for _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>, i.e.,</sup><sup>_<u>Y</u>_˜</sup><sup>_Z_</sup> ≤ _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>≤</sup> _Y_<sup>_Z_</sup> , we notice that _γ_ 0 = _γ_ 1 = 0 and that _γα_ ≥ 0 for every _α_ ≥ 2 [this last result can be directly inferred from the study of _g(α)_ in Eq. (C211)]. Then we have 



For the upper bound, we observe that _γα_ ≤ _γα_ +1 for _α_ ≥ 2. Indeed, 



which is true since _η_ 2 _> η_ ↓ and 1 ≥ _η_ ↑. Then we have 



We can now derive an upper bound on _Y_<sup>˜</sup><sup>_Z_</sup> 1<sup>in the same way used to derive an upper bound on the one-photon yield with two</sup> or three decoy intensities, Eq. (D22). We start by obtaining the bound with two decoy intensities. Consider the decoy-state formula in Eq. (D39) and consider the combination of gains that leads to Eq. (D49). We obtain the following upper bound on _Y_<sup>˜</sup><sup>_Z_</sup> 1<sup>:</sup> 



044011-77 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 



By substituting _<u>Y</u>_<sup>˜</sup><sup>_Z_</sup> = 0 and _G_<sup>˜</sup> _μj_ with Eq. (D68) in the last expression, we obtain 



For the case of three decoy intensities, we consider the same combination of gains as in Eq. (D15). Then, in the resulting expression, we can replace _Y_<sup>˜</sup><sup>_Z_</sup> _n_<sup>with</sup> _Y_ ˜<sup>_Z_</sup> (instead of 1) and follow the same steps leading to Eq. (D21). By doing so, we obtain 



˜ By substituting _Y_<sup>_Z_</sup> = _(_ 1 − _pd_<sup>_Z)(η_↑−</sup><sup>_η_↓</sup><sup>_)_and</sup><sup>_G_˜</sup><sup>_μ_</sup> _j_<sup>with Eq. (D68) in the last expression, we obtain</sup> 





Finally, we combine the two upper bounds derived in Eqs. (D77) and (D79) to obtain the final expression [analogous to Eq. (D22)] for our upper bound on the linear combination of yields in Eq. (D67): 



## **APPENDIX E: SIMULATION FORMULAS** 

In this appendix we report the formulas used to generate the simulations reported in Sec. V. 

absence of eavesdroppers, the _Z_ -basis gain reads 



## **1. High-dimensional time-bin QKD** 

According to the channel model used for simulating the time-bin QKD protocol (Protocol 1) in Figs. 3 and 4, in the 

where _η_ is the transmittance of the quantum channel. For the _X_ -basis gains, we recall that we assumed that the signal arriving at Bob is entirely contained in the detection window _Z_ . Hence, the gains are not affected by the transmittance of the TBS outside the interval _Z_ . Thus, 

044011-78 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

we get 





Instead of modeling noise sources in the quantum channel and in the detectors, we assume that each click caused by a photon detection by the _Z_ -basis detector ( _X_ -basis detector) is affected by a channel-intrinsic QBER of _qZ_ ( _qX_ ), while the clicks caused by dark counts are random and hence contribute with an error rate of 1 − 1 _/d_ . Thus, we obtain the following QBER of the key generation rounds: 







Similarly, the QBERs of the test rounds are given by 







where we observe that in our error model the test round QBERs are independent of whether the _Z_ -basis detector clicks or does not click. 

The quantities appearing in the decoy-BB84 key rate (43) are obtained with a standard application of the decoystate method (see Appendix D). In particular, we have 



for the bit error rate upper bound, while the lower bounds on the one-photon yields _Y_ <u>1</u><sup>_X_</sup> and _Y_ <u>1</u><sup>_Z_</sup> are reported in Eq. (D11). The lower bound _Y_ <u>0</u><sup>_Z_</sup> is given by Eq. (D10). Note that these formulas need to be evaluated with the appropriate _Z_ -basis or _X_ -basis gains. Indeed, in Sec. V we argued that even in the honest implementation of the protocol there is an asymmetry in the gains of the two bases due to asymmetric detectors. We derive the gains appearing in Eq. (43) as follows: 



where the gains on the right-hand side are given in Eqs. (E1)–(E3). This is because the TBS is not needed in the 

decoy-BB84 proof; hence, its only use in that protocol is to select the measurement basis, with setting _(η_ ↓, _η_ ↓ _)_ that selects the _Z_ basis and setting _(η_ ↑, _η_ ↑ _)_ that selects the _X_ basis. For the QBERs appearing in Eq. (43), we have 





## **2. Attack-induced efficiency mismatch** 

To study the attack presented in Sec. V B, we assume that Alice can deterministically send one-photon pulses in each round. This allows us to simplify our proof by removing the decoy-state method, which is no longer needed since in this setting one-photon yields and error rates are directly observable quantities. 

Here we report the new expressions for the one-photon yields and error rates that enter our key rate (44) and the BB84 key rate (45) when Alice sends one-photon pulses. 

## **_a. Protocol statistics without Eve’s attack_** 

First we present the formulas for the case where there is no attack by Eve where and Alice and Bob are linked by a channel with transmittance _η_ and intrinsic QBERs _qZ_ and _qX_ . The one-photon yields are 



The one-photon error rates satisfy the following equalities: 





044011-79 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 





where the yields appearing on the right-hand side are given in Eqs. (E14) and (E15). 

By using Eqs. (E12)–(E19) to replace the corresponding bounds in the phase error rate upper bound (B1), we obtain significant simplifications compared with the expressions in Appendix B, which are obtained when Alice prepares phase-randomized coherent pulses for the decoystate method. In particular, thanks to the knowledge of the true value of the one-photon yields, the estimation of the weight of Bob’s received state in the (≤ 1)-subspace becomes tight. Namely, the upper bound in Eq. (B5) becomes null ( _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1= 0)oncewereplacetheyieldswith</sup> Eq. (E12). This fact greatly improves the tightness of our key rate bound, so much so that it coincides with the asymptotic key rate of the BB84 protocol without decoys, as shown in Fig. 5, for _wZ_ = 0. 

## **_b. Protocol statistics with Eve’s attack_** 

Eve intercepts and measures Alice’s pulses in the _Z_ basis ( _X_ basis) with probability _wZ_ ( _wX_ ). Eve can perfectly distinguish Alice’s symbols when guessing the right basis. She then prepares a tailored time pulse (frequency pulse), corresponding to the _Z_ -basis ( _X_ -basis) outcome she observed, and sends it through a pure-loss channel with transmittance _ξZ_ ( _ξX_ ). Her goal is to make her attack undetectable in the standard BB84 protocol. In other words, she aims to introduce little noise in the events where Alice, Bob, and Eve choose the same basis, while decreasing the detection probability at Bob for the events where she chooses the wrong basis, thereby keeping the QBERs low. 

Before describing Eve’s attack, we review Bob’s measurement apparatus for the case of one-photon signals. Bob’s measurement apparatus comprises the TBS with 

setting _(ηi_ , _ηl)_ , followed by a time-of-arrival measurement in the reflected port with efficiency _ηZ_ . The measurement returns outcome _j_<sup>′</sup> if the photon is detected in the time interval centered at _tj_ ′ with width _�j_ for each bin. The total detection window in the _Z_ basis is _�t_ = _d�j_ . The photon transmitted by the TBS undergoes dispersion in a dispersive medium, modeled by the unitary: 



with _�_ 2 the group delay dispersion coefficient of the dispersive medium, followed by a time-of-arrival measurement with efficiency _ηX_ , where outcome _k_<sup>′</sup> corresponds to a detection in the time bin centered at<sup>˜</sup> _tk_ ′ with width _�k_ for each bin. The total detection window in the _X_ basis is _�f_ = _d�k_ . 

To remain undetected, when intercepting the signal in the _Z_ basis, Eve prepares the following one-photon Gaussian time pulse corresponding to outcome _j_ : 



where _s_ is a free parameter that Eve can freely tune. Similarly, Eve prepares the following one-photon Gaussianmodulated frequency pulse when intercepting the signal in the _X_ basis, corresponding to outcome _k_ : 



where _σ_ is a free parameter. In Eqs. (E21) and (E22), _a_<sup>†</sup> _f_<sup>|vac⟩= |</sup><sup>_f_⟩(</sup><sup>_a_†</sup> _t_<sup>|vac⟩= |</sup><sup>_t_⟩)representsanunphysical</sup> state of a single photon at frequency _f_ (time _t_ ). It holds that | _t_ ⟩= �−∞∞<sup>d</sup><sup>_fe_2</sup><sup>_iπft_|</sup><sup>_f_⟩.</sup> 

We now compute the probabilities of Bob obtaining certain outcomes, given that Eve performed the attack in the _Z_ basis, Eq. (E21), or the _X_ basis, Eq. (E22). 

The probability that Bob obtains outcome _j_<sup>′</sup> in the _Z_ basis, given that Eve sent the pulse corresponding to outcome _j_ in Eq. (E21), is given by 



044011-80 

R 

R 



<!-- Start of picture text -->
-<br>TC “| — 20)<br>ee)<br>[0]<br>A [0]<br>— =) (—)]<br>| o A<br>[. —<br>EEE (Ee<br>(5)<br>A<br>[][]<br>[] [ ]<br>[]<br>[ ]<br>[ ]<br>[ ]<br><!-- End of picture text -->

~~-~~ 2 

~~-~~ 2 

~~-~~ 2 ~~-~~ 2 | ( ~~ol~~ | ( ~~ol~~ | ( ~~ol~~ | ( ~~ol~~ | ( ~~)~~ ( ~~ol~~ | (5 ~~)~~ |<sup>(</sup><sup>~~ol~~</sup> ( ~~ol~~ | ( ~~ol~~ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

where Pr _(Z_ err| _Z)_ is the probability that Bob obtains a click in the _Z_ basis and the outcome is different from Alice’s, given that Eve attacked in the same basis: 



where again we assumed that Eve can perfectly distinguish Alice’s symbols with no errors when she chooses the same basis. When Eve chooses the opposite basis, the probability that Bob gets an error is given by 



where we used the fact that Eve’s outcome is uniformly random when measuring in the basis opposite Alice’s. In the same vein, we have 





## **_c. Upper bound on secret key rate_** 

Here we derive the upper bound on the asymptotic secret key rate achievable by Alice and Bob under Eve’s attack. The upper bound is plotted in Fig. 5 together with the BB84 key rate. The fact that the latter surpasses the former indicates that the BB84 protocol is insecure and returns overly optimistic key rates, as discussed in Sec. VI. 

The upper bound is obtained by considering the raw key bits per pulse shared by Alice and Bob, _r_ raw, and by subtracting the number of raw key bits per pulse known to Eve, _r_ Eve. For _r_ raw, we have 



since the key bits are generated only from the events where both Alice and Bob choose the _Z_ basis and Bob gets a detection. The factor log2 _d_ accounts for the fact that each symbol contains log2 _d_ bits of information. For _r_ Eve, we recall that Eve knows perfectly the shared raw key bits in the rounds where Alice, Bob, and Eve all choose the _Z_ basis and Bob gets a detection in the _Z_ basis. Moreover, Eve learns the bits exchanged by Alice and Bob for error 

correction. This amounts to the following rate of raw key bits known to Eve: 



Hence, the upper bound on the secret key rate is given by 



## **3. Secret key rate versus (mode-independent) detection efficiency mismatch** 

In this section, we study the performance of the key rate from our proof, Eq. (17), for various asymmetries in the mode-independent detection efficiency of the two bases, i.e., as a function of _ηr_ = _ηX /ηZ_ . This study stems from the observation made in Sec. VI that our key rate does not match the decoy-BB84 key rate in the case of an honest implementation of the protocol and that the difference may be due to the asymmetric detection efficiency of the two bases. 

In Fig. 8, we plot the key rate (17) as a function of _ηr_ and compare it with the decoy-BB84 rate (43) and with the same key rate (17) obtained by our artificially setting the weight of the state received by Bob outside the 



<!-- Start of picture text -->
3  ×  10 − 1<br>2  ×  10 − 1<br>Decoy BB84<br>10 − 1 This work ( w > Z 1 = 0)<br>This work<br>0 . 70 0 . 75 0 . 80 0 . 85 0 . 90 0 . 95 1 . 00<br>ηr<br>(key bits per ulse)<br>∞<br>r<br><!-- End of picture text -->

FIG. 8. The secret key rate in Eq. (17) in the case of the honest implementation in Sec. V A as a function of the detection efficiency mismatch _ηr_ . Note that we fix _ηZ_ = 0.9 × 10<sup>−1</sup><sup>_/_10</sup> and vary _ηX_ to achieve different values of _ηr_ . We also fix the intrinsic QBERs to _qZ_ = _qX_ = 0.02. The solid red line represents the secure key rate obtained with the bound on _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1</sup> reported in Eq. (B5). The dashed red line represents the key rate when we impose _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1= 0. The solid blue line represents the decoy-BB84</sup> key rate in Eq. (43). We observe that the dashed red line perfectly overlaps the solid blue line, indicating that our proof will become tight and match the decoy-BB84 rate when a tight estimation of _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1is available.</sup> 

044011-83 

FEDERICO GRASSELLI _et al._ 

PHYS. REV. APPLIED **23,** 044011 (2025) 

_(_ ≤ 1 _)_ -subspace to zero: _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1= 0.Thiswouldcorrespond</sup> to the scenario with perfect knowledge of the parameter _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1,whichisindeednullinthehonestimplementation</sup> considered . The other parameters are set as in Fig. 4 for the honest implementation of the protocol, where _ηZ_ = 0.9 × 10<sup>−1</sup><sup>_/_10</sup> and the channel loss _η_ is fixed to 10<sup>−1</sup><sup>_/_10</sup> . 

From Fig. 8, we observe that in the case of perfect knowledge of the parameter _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1,thedetectionefficiency</sup> mismatch does not influence the key rate (17) and the latter matches the decoy-BB84 key rate perfectly. Conversely, when our bound, Eq. (B5), is used on the parameter _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1,</sup> the key rate of our proof presents a gap to the decoy-BB84 rate that increases as _ηr_ decreases. Therefore, we deduce that the nontight estimation of _<u>w</u>_<sup>_~~>~~_</sup> _Z_<sup>1isthemaincauseof</sup> loss of performance, becoming more problematic as the asymmetry in the detection efficiencies increases. 



- [1] Inside Quantum Technology, Quantum key distribution (QKD) markets: 2019–2028. https://www.insidequantum technology.com/product/quantum-key-distribution-qkdmarkets-2019-2028 [Online]. 

- [2] S. Pirandola, U. L. Andersen, L. Banchi, M. Berta, D. Bunandar, R. Colbeck, D. Englund, T. Gehring, C. Lupo, C. Ottaviani, J. L. Pereira, M. Razavi, J. S. Shaari, M. Tomamichel, V. C. Usenko, G. Vallone, P. Villoresi, and P. Wallden, Advances in quantum cryptography, Adv. Opt. Photon. **12** , 1012 (2020). 

- [3] French Cybersecurity Agency (ANSSI), Federal Office for Information Security (BSI), Netherlands National Communications Security Agency (NLNCSA), and Swedish National Communications Security Authority (Swedish NCSA), Position paper on quantum key distribution (2024). 

- [4] M. Lucamarini, A. Shields, R. Alléaume, C. Chunnilall, I. P. Degiovanni, M. Gramegna, A. Hasekioglu, B. Huttner, R. Kumar, A. Lord, N. Lütkenhaus, V. Makarov, V. Martin, A. Mink, M. Peev, M. Sasaki, A. Sinclair, T. Spiller, M. Ward, C. White, and Z. Yuan, Implementation security of quantum cryptography, _ETSI White Paper No. 27_ , (2018). 

- [5] V. Zapatero, A. Navarrete, and M. Curty, Implementation security in quantum key distribution, Adv. Quantum Technol. **8** , 2300380 (2024). 

- [6] F. Xu, X. Ma, Q. Zhang, H.-K. Lo, and J.-W. Pan, Secure quantum key distribution with realistic devices, Rev. Mod. Phys. **92** , 025002 (2020). 

- [7] P. W. Shor and J. Preskill, Simple proof of security of the BB84 quantum key distribution protocol, Phys. Rev. Lett. **85** , 441 (2000). 

- [8] M. Tomamichel and A. Leverrier, A largely self-contained and complete security proof for quantum key distribution, Quantum **1** , 14 (2017). 

- [9] C. C. W. Lim, M. Curty, N. Walenta, F. Xu, and H. Zbinden, Concise security bounds for practical decoy-state quantum key distribution, Phys. Rev. A **89** , 022307 (2014). 

- [10] K. Tamaki, M. Curty, G. Kato, H.-K. Lo, and K. Azuma, Loss-tolerant quantum cryptography with imperfect sources, Phys. Rev. A **90** , 052314 (2014). 

- [11] M. K. Bochkov and A. S. Trushechkin, Security of quantum key distribution with detection-efficiency mismatch in the single-photon case: Tight bounds, Phys. Rev. A **99** , 032308 (2019). 

- [12] A. Trushechkin, Security of quantum key distribution with detection-efficiency mismatch in the multiphoton case, Quantum **6** , 771 (2022). 

- [13] J. Nunn, L. J. Wright, C. Söller, L. Zhang, I. A. Walmsley, and B. J. Smith, Large-alphabet time-frequency entangled quantum key distribution by means of time-to-frequency conversion, Opt. Express **21** , 15959 (2013). 

- [14] J. E. Bourassa and H.-K. Lo, Entropic uncertainty relations and the measurement range problem, with consequences for high-dimensional quantum key distribution, J. Opt. Soc. Am. B **36** , B65 (2019). 

- [15] L. Lydersen, C. Wiechers, C. Wittmann, D. Elser, J. Skaar, and V. Makarov, Hacking commercial quantum cryptography systems by tailored bright illumination, Nat. Photon. **4** , 686 (2010). 

- [16] Y. Zhao, C.-H. F. Fung, B. Qi, C. Chen, and H.-K. Lo, Quantum hacking: Experimental demonstration of timeshift attack against practical quantum-key-distribution systems, Phys. Rev. A **78** , 042333 (2008). 

- [17] S. Sajeed, P. Chaiwongkhot, J.-P. Bourgoin, T. Jennewein, N. Lütkenhaus, and V. Makarov, Security loophole in free-space quantum key distribution due to spatial-mode detector-efficiency mismatch, Phys. Rev. A **91** , 062301 (2015). 

- [18] A. Boaron, B. Korzh, R. Houlmann, G. Boso, D. Rusca, S. Gray, M.-J. Li, D. Nolan, A. Martin, and H. Zbinden, Simple 2.5 GHz time-bin quantum key distribution, Appl. Phys. Lett. **112** , 171108 (2018). 

- [19] I. Vagniluca, B. Da Lio, D. Rusca, D. Cozzolino, Y. Ding, H. Zbinden, A. Zavatta, L. K. Oxenløwe, and D. Bacco, Efficient time-bin encoding for practical high-dimensional quantum key distribution, Phys. Rev. Appl. **14** , 014051 (2020). 

- [20] N. T. Islam, C. C. W. Lim, C. Cahall, J. Kim, and D. J. Gauthier, Provably secure and high-rate quantum key distribution with time-bin qudits, Sci. Adv. **3** , e1701491 (2017). 

- [21] N. T. Islam, C. C. W. Lim, C. Cahall, B. Qi, J. Kim, and D. J. Gauthier, Scalable high-rate, high-dimensional time-bin encoding quantum key distribution, Quantum Sci. Technol. **4** , 035008 (2019). 

- [22] J. Mower, Z. Zhang, P. Desjardins, C. Lee, J. H. Shapiro, and D. Englund, High-dimensional quantum key distribution using dispersive optics, Phys. Rev. A **87** , 062322 (2013). 

- [23] C. Lee, D. Bunandar, Z. Zhang, G. R. Steinbrecher, P. B. Dixon, F. N. C. Wong, J. H. Shapiro, S. A. Hamilton, and D. Englund, Large-alphabet encoding for higher-rate quantum key distribution, Opt. Express **27** , 17539 (2019). 

- [24] J. Rödiger, N. Perlot, R. Mottola, R. Elschner, C.-M. Weinert, O. Benson, and R. Freund, Numerical assessment and optimization of discrete-variable time-frequency quantum key distribution, Phys. Rev. A **95** , 052312 (2017). 

- [25] Y. Zhang, I. B. Djordjevic, and M. A. Neifeld, Weakcoherent-state-based time-frequency quantum key distribution, J. Mod. Opt. **62** , 1713 (2015). 

044011-84 

PHYS. REV. APPLIED **23,** 044011 (2025) 

QUANTUM KEY DISTRIBUTION. . . 

- [26] M. Leifgen, R. Elschner, N. Perlot, C. Weinert, C. Schubert, and O. Benson, Practical implementation and evaluation of a quantum-key-distribution scheme based on the time-frequency uncertainty, Phys. Rev. A **92** , 042311 (2015). 

- [27] K.-C. Chang, M. C. Sarihan, X. Cheng, Z. Zhang, and C. W. Wong, Large-alphabet time-bin quantum key distribution and Einstein-Podolsky-Rosen steering via dispersive optics, Quantum Sci. Technol. **9** , 015018 (2024). 

- [28] T. Moroder, M. Curty, and N. Lütkenhaus, Detector decoy quantum key distribution, New J. Phys. **11** , 045008 (2009). 

- [29] A. Widomski, M. Ogrodnik, and M. Karpi´nski, Efficient detection of multidimensional single-photon time-bin superpositions, Optica **11** , 926 (2024). 

- [30] M. Ogrodnik, A. Widomski, D. Bruß, G. Chesi, F. Grasselli, H. Kampermann, C. Macchiavello, N. Walk, N. Wyderka, and M. Karpi´nski, High-dimensional quantum key distribution with resource-efficient detection, arXiv:2412. 16782. 

- [31] Federal Office for Information Security (BSI), Implementation attacks against QKD systems (2023). 

- [32] M. Zahidy, D. Ribezzo, C. De Lazzari, I. Vagniluca, N. Biagi, R. Müller, T. Occhipinti, L. K. Oxenløwe, M. Galili, T. Hayashi, D. Cassioli, A. Mecozzi, C. Antonelli, A. Zavatta, and D. Bacco, Practical high-dimensional quantum key distribution protocol over deployed multicore fiber, Nat. Commun. **15** , 1651 (2024). 

- [33] C.-H. F. Fung, K. Tamaki, B. Qi, H.-K. Lo, and X. Ma, Security proof of quantum key distribution with detection efficiency mismatch, Quantum Inf. Comput. **9** , 131 (2009). 

- [34] J. Ma, Y. Zhou, X. Yuan, and X. Ma, Operational interpretation of coherence in quantum key distribution, Phys. Rev. A **99** , 062325 (2019). 

- [35] L. Lydersen and J. Skaar, Security of quantum key distribution with bit and basis dependent detector flaws, Quantum Inf. Comput. **10** , 60 (2010). 

- [36] Y. Zhang, P. J. Coles, A. Winick, J. Lin, and N. Lütkenhaus, Security proof of practical quantum key distribution with detection-efficiency mismatch, Phys. Rev. Res. **3** , 013076 (2021). 

- [37] H.-K. Lo, X. Ma, and K. Chen, Decoy state quantum key distribution, Phys. Rev. Lett. **94** , 230504 (2005). 

- [38] X.-B. Wang, Beating the photon-number-splitting attack in practical quantum cryptography, Phys. Rev. Lett. **94** , 230503 (2005). 

- [39] X. Ma, B. Qi, Y. Zhao, and H.-K. Lo, Practical decoy state for quantum key distribution, Phys. Rev. A **72** , 012326 (2005). 

- [40] X.-S. Ma, S. Zotter, N. Tetik, A. Qarry, T. Jennewein, and A. Zeilinger, A high-speed tunable beam splitter for feedforward photonic quantum information processing, Opt. Express **19** , 22723 (2011). 

- [41] R. R. Carreira, J. J. Barroso, and J. E. B. Oliveira, Generalized analysis of dual-output Mach-Zehnder modulator with 

   - applications to photonic-assisted instantaneous frequency measurement, J. Lightwave Technol. **39** , 7956 (2021). 

- [42] M. Christandl, R. König, and R. Renner, Postselection technique for quantum channels with applications to quantum cryptography, Phys. Rev. Lett. **102** , 020504 (2009). 

- [43] S. Nahar, D. Tupkary, Y. Zhao, N. Lütkenhaus, and E. Y.-Z. Tan, Postselection technique for optical quantum key distribution with improved de Finetti reductions, PRX Quantum **5** , 040315 (2024). 

- [44] M. Y. Niu, F. Xu, J. H. Shapiro, and F. Furrer, Finite-key analysis for time-energy high-dimensional quantum key distribution, Phys. Rev. A **94** , 052323 (2016). 

- [45] N. Walk, J. Barrett, and J. Nunn, Composably secure timefrequency quantum key distribution, arxiv:1609.09436. 

- [46] I. Devetak and A. Winter, Distillation of secret key and entanglement from quantum states, Proc.: Math., Phys. Eng. Sci. **461** , 207 (2005). 

- [47] W.-Y. Hwang, Quantum key distribution with high loss: Toward global secure communication, Phys. Rev. Lett. **91** , 057901 (2003). 

- [48] M. Berta, M. Christandl, R. Colbeck, J. M. Renes, and R. Renner, The uncertainty principle in the presence of quantum memory, Nat. Phys. **6** , 659 (2010). 

- [49] M. Tomamichel and R. Renner, Uncertainty relation for smooth entropies, Phys. Rev. Lett. **106** , 110506 (2011). 

- [50] F. Furrer, T. Franz, M. Berta, A. Leverrier, V. B. Scholz, M. Tomamichel, and R. F. Werner, Continuous variable quantum key distribution: Finite-key analysis of composable security against coherent attacks, Phys. Rev. Lett. **109** , 100502 (2012). 

- [51] F. Furrer, M. Berta, M. Tomamichel, V. B. Scholz, and M. Christandl, Position-momentum uncertainty relations in the presence of quantum memory, J. Math. Phys. **55** , 122205 (2014). 

- [52] M. A. Nielsen and I. L. Chuang, _Quantum Computation and Quantum Information: 10th Anniversary Edition_ (Cambridge University Press, Cambridge, 2011). 

- [53] In an adversarial implementation, we cannot discard the possibility that Eve adds photons to Alice’s pulse before it reaches Bob. 

- [54] D. Tupkary, S. Nahar, P. Sinha, and N. Lütkenhaus, Phase error rate estimation in QKD with imperfect detectors, arXiv:2408.17349. 

- [55] A. Winick, N. Lütkenhaus, and P. J. Coles, Reliable numerical key rates for quantum key distribution, Quantum **2** , 77 (2018). 

- [56] Y. Zhang and N. Lütkenhaus, Entanglement verification with detection-efficiency mismatch, Phys. Rev. A **95** , 042319 (2017). 

- [57] S. Nahar, T. Upadhyaya, and N. Lütkenhaus, Imperfect phase randomization and generalized decoy-state quantum key distribution, Phys. Rev. Appl. **20** , 064031 (2023). 

- [58] R. Bhatia and C. Davis, A Cauchy-Schwarz inequality for operators with applications, Linear Algebra Appl. **223–224** , 119 (1995), Honoring Miroslav Fiedler and Vlastimil Ptak. 

044011-85 

