| 





<!-- Start of picture text -->
|<br><!-- End of picture text -->





<!-- Start of picture text -->
oo5<br><!-- End of picture text -->



<!-- Start of picture text -->
 MMWwWWwW<br><!-- End of picture text -->

> PARIS-SACLAYuniversité <u>ea MMWwWWwW 5oo5</u> 



<!-- Start of picture text -->
universitéPARIS-SACLAYuniversité<br><!-- End of picture text -->

_A papa, c’est une grande joie que d’avoir marché (un petit peu) dans tes pas._ 

ii 

## **Remerciements** 

Beaucoup de personnes ont contribué à rendre ces trois années et demie passées dans le groupe Quantronique formidables et inoubliables, et je voudrais par ces quelques mots les remercier toutes très chaleureusement. 

Il y a en premier ceux que j’ai cotoyés tous les jours et qui m’ont appris énormément. Merci tout d’abord à Patrice, pour ta disponibilité, ton incroyable clarté, ton optimisme et ta très grande gentillesse qui ont fait de ces mois passés au labo et à rédiger ce mémoire des moments chouettes, certes très riches en physique, parfois frustrants, mais aussi remplis d’enthousiasme et captivants! Si Patrice m’a appris la physique, c’est bien Yui que je dois remercier pour m’avoir appris bien des techniques expérimentales et de nano-fabrication (ainsi que de la mécanique!). Je n’aurais pas pu avoir un prof plus sympa, patient et rigoureux tout à la fois ! 

Merci aux permanents de Quantronique (au sens large): Carles, Cristian, Daniel, Denis, Fabien, Hélène, Hugues, Marcelo, Pascal, Philippe, et Pief, d’être aussi passionnés et passionnants, et d’avoir été aussi disponibles pour discuter, filer des coups de main et des encouragements. 

Merci à la jeune génération qui a garanti la bonne ambiance à table, au labo et en-dehors: mes prédécesseurs Cécile, Olivier, et Vivien, les post-docs Xin, Michael, Sebastian, Philippe, Simon, Caglar, Marc et Leandro, mes co-thésards et « compagnons de rédaction » Kristinn (could not have picked a better office and car mate!), Camille, Pierre et Chloé, et enfin les tous derniers arrivants Bartolo et Fernanda. 

Merci à ceux qui ont rendu possible cette thèse. Merci à l’atelier mécanique, Dominique, JeanClaude et Vincent d’avoir réalisé toutes nos pièces même si elles étaient coriaces...Merci à l’atelier de cryogénie, Patrick, Philippe et Matthieu, les héros qui ont sauvé le cryostat (deux fois!) d’une situation plus que précaire; merci au secrétariat et à la direction du SPEC. 

Il y a ensuite tous ceux qui ont contribué directement aux expériences qui sont présentées ici et avec qui j’ai interagi avec beaucoup de plaisir. Merci à toute l’équipe de Londres, Jarryd, Gary, Eva et John Morton, qui nous ont fait découvrir ce sacré champion de bismuth, « the new black stuff », et qui nous ont apporté tant d’idées fructueuses. Merci aussi à Klaus Mølmer, Brian Julsgaard et Alexander Holm-Kiilerich, nos collaborateurs théoriciens d’Aarhus, avec qui ce fut un plaisir de travailler par quelque moyen que ce soit (après avoir essayé Skype, Hangouts, RendezVous et autres, nous concluons d’ailleurs que le téléphone reste sacrément pratique!). 

Finalement, je voudrais remercier ma famille, absents comme présents, et mes amis, pour leur encouragements et pouvoir avoir été là. Merci surtout à Félix, de m’avoir soutenue et supportée dans les moments difficiles, et d’avoir accepté mes horaires parfois incongrus, qui nous ont menés à commander bien trop de pizzas ! 

iii 

# **Contents** 

|**Remerc**|**iements**|**iii**|
|---|---|---|
|**Résum**|**é détaillé**|**1**|
|**1**<br>**Intr**|**oduction**|**11**|
|1.1|Circuit quantum electrodynamics for magnetic resonance . . . . . . . . . . . . . . . .|11|
|1.2|Quantum microwaves and spin dynamics . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|1.3|Electron spin resonance at the quantum-limit of sensitivity . . . . . . . . . . . . . . .|14|
|1.4|The Purcell effect applied to spins<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|17|
|1.5|Squeezing-enhanced magnetic resonance<br>. . . . . . . . . . . . . . . . . . . . . . . . .|18|
|**I**<br>**Bac**|**kground**|**20**|
|**2**<br>**Qua**|**ntum circuits and quantum noise**|**21**|
|2.1|Quantum microwaves and quantum circuits<br>. . . . . . . . . . . . . . . . . . . . . . .|21|
||2.1.1<br>Quantum description of an electromagnetic mode : quantum noise and quan-||
||tum states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
||2.1.2<br>Lumped element LC resonator . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
||2.1.3<br>Lossless transmission line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
||2.1.4<br>Probing and characterizing a resonator<br>. . . . . . . . . . . . . . . . . . . . . .<br>|29|
|2.2|Amplifcation at the quantum-limit . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>|33|
||2.2.1<br>Input-output relations for linear amplifers . . . . . . . . . . . . . . . . . . . .<br>|33|
||2.2.2<br>Quantum limits on the noise added by the amplifer. . . . . . . . . . . . . . .|35|
||<br>2.2.3<br>The fux-pumped Josephson Parametric Amplifer . . . . . . . . . . . . . . . .|36|
|**3**<br>**Spin**|**s in a cavity**<br>|**40**|
|3.1|Spin dynamics in a classical microwave feld . . . . . . . . . . . . . . . . . . . . . . .|40|
||3.1.1<br>Coherent spin evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
||<br>3.1.2<br>Relaxation and decoherence . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|42|
||3.1.3<br>Inductive detection of magnetic resonance<br>. . . . . . . . . . . . . . . . . . . .<br>|43|
|3.2|<br>Spin dynamics in a quantum microwave feld . . . . . . . . . . . . . . . . . . . . . . .|44|
||3.2.1<br>One spin coupled to a harmonic oscillator. . . . . . . . . . . . . . . . . . . . .|45|
||3.2.2<br>Collective effects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|50|
|**4**<br>**Bism**|**uth donors in silicon**|**54**|
|4.1|A substitutional donor in silicon<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|
||4.1.1<br>Electronic states . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|
|4.2|Spin levels and ESR-allowed transitions. . . . . . . . . . . . . . . . . . . . . . . . . . .|58|
|4.3|<br>Donors in strained silicon<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|63|
|4.4|Relaxation times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
||4.4.1<br>_T_1 relaxation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
||4.4.2<br>Coherence times<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|67|
|4.5|Optical transitions via donor-bound exciton states . . . . . . . . . . . . . . . . . . . .|69|
|4.6|<br>Fabrication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|69|



iv 

|**II**<br>**Magnet**|**ic resonance at the quantum limit**<br>**71**|
|---|---|
|**5**<br>**Design and**|**realization of a spectrometer operating at the quantum limit of sensitivity**<br>**72**|
|<br>5.1<br>Nanos|<br>cale ESR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>72|
|5.1.1|State-of-the-art<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>72|
|5.1.2|Pulsed inductive detection at the nanoscale . . . . . . . . . . . . . . . . . . . .<br>73|
|5.2<br>Exper|imental setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>77|
|5.2.1|Low-temperature operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>77|
|5.2.2<br>|Room-temperature setup<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>79<br> <br>|
|5.2.3|JPAcharacterization<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>79|
|5.3<br>Desig|n of a superconducting ESRresonator with high quality factor and small mode|
|volum|e . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>82|
|5.3.1|Design choices<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>82|
|5.3.2|<br>Electromagnetic simulations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>85|
|5.3.3|<br>Coupling to bismuth donor spins. . . . . . . . . . . . . . . . . . . . . . . . . .<br>85|
|5.3.4|Experimental implementation<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>88|
|**6**<br>**ESR spectr**|**oscopy of Bismuth donors in silicon**<br>**92**|
|6.1<br>Hahn-|echo detected ESR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>92|
|6.1.1|Experimental techniques. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>92|
|6.1.2|Hahn-echo sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>93|
|6.1.3|<br>Rabi oscillations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>94|
|6.2<br>Strain|-broadened transitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>97|
|6.2.1|Doublet-shaped transitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>98|
|6.2.2|Rabi frequency dependence on_B_0 . . . . . . . . . . . . . . . . . . . . . . . . .<br>99|
|6.2.3|<br>Induced strain, a likely suspect . . . . . . . . . . . . . . . . . . . . . . . . . . . 101|
|6.3<br>Relaxa|tion times . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103|
|6.3.1|Energy relaxation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103|
|6.3.2|Coherence times<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104|
|**7**<br>**Spectromet**|**er sensitivity**<br>**105**|
|7.1<br>Deter|mining the number of spins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105<br>|
|7.1.1|Direct counting of the donors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105|
|7.1.2|<br>Estimate based on numerical simulations . . . . . . . . . . . . . . . . . . . . . 107|
|7.2<br>Chara|cterization of the sensitivity. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112|
|7.2.1|Single-echo signal-to-noise ratio<br>. . . . . . . . . . . . . . . . . . . . . . . . . . 112|
|7.2.2|Sensitivity enhancement by CPMGechoes . . . . . . . . . . . . . . . . . . . . . 114|
|7.3<br>Concl|usion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115|
|**III**<br>**The Pu**|**rcell effect applied to spins**<br>**116**|
|**8**<br>**Controllin**|**g spin relaxation with a cavity**<br>**117**|
|8.1<br>Cavity|-enhanced spontaneous emission . . . . . . . . . . . . . . . . . . . . . . . . . . 118|
|8.1.1|Spontaneous emission into free space . . . . . . . . . . . . . . . . . . . . . . . 118|
|8.1.2|<br>The Purcell effect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120|
|8.1.3|Experimental realizations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120|
|8.1.4|<br>Spontaneous emission with spins. . . . . . . . . . . . . . . . . . . . . . . . . . 121|
|8.2<br>Exper|imental implementation for electronic spins<br>. . . . . . . . . . . . . . . . . . . . 122|
|8.2.1|Cavity-spin system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122|
|8.2.2|<br>Experimental estimate of_g_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123|
|8.2.3|<br>_T_1 at resonance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124|
|8.3<br>Contr|olling spin relaxation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125|
|8.3.1|Tuning_T_1 via the spin-cavity coupling_g_0 . . . . . . . . . . . . . . . . . . . . . 125|



v 

||8.3.2|Tuning_T_1 via the spin-resonator detuning<br>. . . . . . . . . . . . . . . . .|. . . 127|
|---|---|---|---|
|8.4|Concl|usion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 133|
|**IV**<br>**S**|**queez**|**ing-enhanced magnetic resonance**|**135**|
|**9**<br>**Squ**|**eezing-**|**enhanced magnetic resonance**|**136**|
|9.1|Squee|zing-enhanced measurements<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . 136|
||<br>9.1.1|<br>State-of-the-art<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 136|
||9.1.2|Squeezed states for magnetic resonance . . . . . . . . . . . . . . . . . . .|. . . 138|
|9.2|Detect|ing and characterizing microwave squeezed states . . . . . . . . . . . . .|. . . 141|
||<br>9.2.1|<br>Microwave squeezed-states . . . . . . . . . . . . . . . . . . . . . . . . . .<br>|. . . 141|
||9.2.2|<br>Characterization of the fux-pumped JPAas a squeezing generator<br>. . .|. . . 142|
||9.2.3|<br>Noise reduction below the quantum limit with an ESRresonator . . . . .|. . . 145|
||9.2.4|<br>Detection of displaced squeezed states. . . . . . . . . . . . . . . . . . . .|. . . 146|
|9.3|An ES|Rsignal emitted in squeezed vacuum . . . . . . . . . . . . . . . . . . . . .|. . . 147|
||9.3.1|<br>Squeezing-enhanced ESR: proof-of-principle . . . . . . . . . . . . . . . .|. . . 147|
||9.3.2|Absolute sensitivity<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 148|
||9.3.3|Theoretical limit of a squeezing-enhanced ESRspectrometer . . . . . . .|. . . 150|
|9.4|Concl|<br>usion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 154|
|**10 Con**|**clusion**|**and future directions**|**155**|
|10.1|Magn|etic resonance with quantum microwaves<br>. . . . . . . . . . . . . . . . . .|. . . 155|
|10.2|<br> Future|<br>research directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 155|
|**A The**|**rmal oc**|**cupancy calibration**|**159**|
|**Bibliog**|**raphy**||**164**|



vi 

# **Résumé détaillé** 

### **1 Électrodynamique quantique des circuits appliquée à la résonance magnétique** 

"Photon" et "spin" sont deux notions fondamentales apparues dés le début de la mécanique quantique et essentielles dans de nombreux domaines de recherche. La découverte par Rabi [1], Bloch [2] et Purcell [3] que les spins peuvent absorber ou émettre un rayonnement micro-onde quand ils sont couplés à un résonateur accordé à leur fréquence de précession de Larmor a donné par example naissance à la résonance magnétique, un domaine de recherche qui englobe à la fois la résonance magnétique nucléaire (RMN [4]) et la résonance paramagnétique électronique (RPE [5]). La résonance magnétique permet ainsi l’identification de spins présents dans un échantillon et l’étude de leurs interactions, donnant lieu à une compréhension plus profonde de la matière et de son organisation au niveau atomique. Cette puissante technique de spectroscopie a aujourd’hui un large éventail d’applications en biologie, chimie et science des matériaux, allant de la bio-imagerie non destructive à la découverte de médicaments [6]. Entre autres, elle a rendu possible le développement de l’information quantique, où les spins sont utilisés comme qubits, les porteurs quantiques de l’information [7]. 

Dans les expériences de résonance magnétique réalisées jusqu’à présent, les spins sont toujours traités comme des objets quantiques pour expliquer les interactions entre spins, leur cohérence et leurs mécanismes de relaxation, tandis que les champs micro-ondes utilisés pour les manipuler et les détecter sont seulement considérés comme des objets classiques. Ce traitement semi-classique de l’interaction spin-champ est justifié par deux éléments. Tout d’abord, le couplage des spins au rayonnement est généralement si faible que la nature quantique du champ micro-onde a des effets négligeables sur la dynamique des spins comparé à leur couplage aux vibrations du réseau cristallin ou à d’autres spins voisins. Deuxièmement, à la température où la plupart des expériences de résonance magnétique sont réalisées, les fluctuations micro-ondes du champ du vide sont négligeables par rapport aux fluctuations thermiques du champ – et l’absence d’un détecteur microonde suffisamment sensible empêche de toute façon leur détection. Ces deux derniers arguments sont étroitement liés à la faible sensibilité des spectromètres RPE: le faible couplage des spins au champ micro-onde nécessite l’utilisation d’un nombre conséquent de spins pour que le signal collecté devienne comparable le bruit expérimental, lui-même généralement largement supérieur au bruit quantique. 

En revanche, dans le domaine de l’électrodynamique quantique en cavité (CQED [8]), les systèmes individuels à deux niveaux (TLS) interagissent de manière cohérente avec le champ électromagnétique. Le TLS peut être implémenté par des circuits supraconducteurs non-linéaires, les qubits "Josephson", interagissant avec des résonateurs micro-ondes à haut facteur de qualité dans une architecture appelée circuit-QED (CQED [9, 10]), prometteuse pour le calcul quantique. Au sein de CQED, de nouvelles techniques ont été développées pour la manipulation et la détection de l’état quantique du champ micro-onde. En particulier, des amplificateurs micro-ondes à très faible bruit ont été conçus pour la lecture des qubits Josephson. Ces amplificateurs paramétriques Josephson (JPA) ajoutent le bruit minimum requis par la mécanique quantique, allant jusqu’à pouvoir amplifier sans bruit une quadrature du champ [11, 12, 13]. Cette thèse rapporte **l’application des concepts et techniques de cQED à la détection RPE dans le but d’effectuer des expériences de résonance** 

1 

_Contents_ 

##### **magnétique dans un nouveau régime, où les fluctuations quantiques du champ micro-onde ont un impact majeur sur la sensibilité du spectromètre et sur la dynamique des spins.** 

La première partie du mémoire vise à fournir les outils conceptuels nécessaires à la compréhension des expériences. Nous donnons une brève description des champs micro-ondes quantiques, des résonateurs, et de leur interaction avec un TLS – l’essence même de cQED. Ceci nous permet de présenter un traitement quantique de la détection d’un signal RPE. Nous présentons également les spins utilisés dans nos expériences : des donneurs de bismuth implantés dans le silicium (Si:Bi). 

Dans la deuxième partie de cette thèse, nous présentons la conception et l’implémentation d’un spectromètre RPE à la sensibilité largement améliorée par les outils de CQED. Les éléments-clés de notre dispositif sont l’utilisation de températures cryogéniques, de l’ordre de quelques millikelvins, un résonateur supraconducteur de haut facteur de qualité et de petit volume de mode, fortement couplé à des spins Si:Bi, et un JPA qui amplifie le signal émis par les spins. Le bruit de sortie du spectromètre est entièrement dominé par les fluctuations quantiques du champ micro-onde, lui permettant d’atteindre une sensibilité de détection limitée quantiquement. Nous démontrons une sensibilité sans précédent de 2000 spins par séquence expérimentale [14], ce qui représente une amélioration de quatre ordres de grandeur par rapport à l’état de l’art [15]. 

Les très basses températures utilisées dans nos expériences ont pour avantage supplémentaire de polariser entièrement l’ensemble de spins lors de leur détection RPE. Néanmoins, elles peuvent également augmenter de façon spectaculaire le temps de relaxation spin-phonon [16], conduisant à des taux de répétition beaucoup trop faibles pour mettre en pratique nos expériences. Dans la troisième partie de cette thèse, nous démontrons que le couplage des spins à un résonateur RPE de haut facteur de qualité et de petit volume de mode conduit à exacerber la relaxation des spins par émission spontanée de photons micro-ondes jusqu’à en faire le mécanisme de relaxation dominant, avec un taux nettement supérieur au taux de relaxation par phonons. Ce phénomène, bien connu en CQED et prédit par Edwin Purcell en 1946, est ainsi observé pour des spins électroniques pour la première fois [17]. 

Comme déjà mentionné, les fluctuations du vide du champ micro-onde sont la seule source de bruit de notre spectromètre. Bien que cela semble représenter une limite fondamentale à sa sensibilité, ce seuil peut être surmonté en utilisant des états quantiques dits comprimés, bien connus en optique quantique [18, 19, 20]. Pour de tels états quantiques du champ, le bruit sur une quadrature est réduit au-dessous du niveau de vide alors que le bruit sur l’autre quadrature est augmenté afin de respecter l’inégalité de Heisenberg. Nous rapportons dans la quatrième partie de cette thèse l’utilisation d’états micro-ondes comprimés pour améliorer la sensibilité de notre spectromètre RPE au-delà de la limite quantique. 

### **2 Micro-ondes quantiques et dynamique de spins** 

Il existe plusieurs raisons justifiant un traitement quantique du champ micro-onde lors d’une expérience de résonance magnétique. Un signal micro-onde classique de fréquence _!_ est décrit par son amplitude _A_ et sa phase _φ_ , ou de manière équivalente par ses quadratures _X_ = _A_ cos( _φ_ ) et _Y_ = _A_ sin( _φ_ ). Dans une description quantique, détaillée dans le ch. 2, les variances des quadratures<sup>1</sup> du champ respectent l’inégalité de Heisenberg ~~p~~ _h_ ∆ _X_<sup>2</sup> _ih_ ∆ _Y_<sup>2</sup> _i_ > 1 _/_ 4. Par conséquent, même à des températures suffisamment basses pour que le champ micro-onde soit dans son état fondamental, des fluctuations persistent. En exprimant les fluctuations du champ pour une température _T_ par la quantité adimensionnelle _n_ eq( _T_ ) = _h_ ∆ _X_<sup>2</sup> _i_ , les fluctuations du vide se caractérisent par l’atteinte d’un minimum _n_ eq = 1 _/_ 4 (voir Fig.1a). Ces fluctuations du vide représentent donc une limite fondamentale pour la sensibilité de nombreuses mesures, en particulier pour la spectroscopie RPE. 

> 1réécrites dans des unités sans dimension, telles que ~ _!_ ( _hX_ 2 _i_ + _hY_ 2 _i_ ) est égal à l’énergie du mode du champ 

2 

_Contents_ 



<!-- Start of picture text -->
ω<br>a Y b c<br>ω<br>0<br>sortie<br>∆ Y 2 = 1 JPA<br>2 X sortie<br>ω signal de pompe<br>p<br>d e<br>30 20<br>Y<br>25<br>10<br>X<br>20<br>Y<br>15 0<br>10<br>X<br>-10<br>5<br>ω =2 ω<br>p 0<br>0 -20 -10 0 10 20 -200 π/4 π/2<br>( ω - ω p/2)/2 π  (MHz) φ−φ p (°)<br>entrée<br>entrée<br>Gain (dB) Gain (dB)<br><!-- End of picture text -->

FIGURE 1: **Fluctuations quantiques et limite quantique à l’amplification a** A des températures _kBT ⌧_ ~ _!_ <u>,</u> le champ micro-onde est refroidit dans son état fondamental : ses quadratures ont pour variance p _h_ ∆ _X_<sup>2</sup> _i_ = p _h_ ∆ _Y_<sup>2</sup> _i_ = 1 _/_ 2, correspondant au minimum de fluctuations autorisées pour le champ (disque bleu). **b-c** Un amplificateur paramétrique Josephson, implémenté ici par un résonateur comprenant un réseau de SQUIDs et pompé en flux, peut être utilisé pour détecter des champs microondes quantiques. **d** Utilisé en mode non-dégénéré ( _!p_ = 2 _!_ ), le JPA ajoute un demi-photon de bruit (disque rouge) au demi-photon de bruit (disque bleu) correspondant aux fluctuations du vide à l’entrée du JPA. **e** En mode dégénéré ( _!p_ = 2 _!_ ), le JPA amplifie une quadrature aux dépends de l’autre; dans ce cas l’amplification est sans bruit. Agissant sur le vide, le JPA crée un état comprimé, ayant des fluctuations réduites en-dessous du niveau du vide sur une quadrature mais amplifiées sur l’autre (ellipse bleue). 

Les développements réalisés par cQED fournissent les outils nécessaires pour détecter les fluctuations micro-ondes quantiques. Comme plusieurs ordres de grandeur séparent la faible puissance des signaux micro-ondes quantiques et le niveau de bruit typique des appareils de mesure à température ambiante, il est nécessaire d’amplifier les signaux. Lors de l’amplification, la mécanique quantique impose certaines contraintes sur le bruit _n_ amp ajouté à la quadrature _X_ (également exprimé en unités adimensionnelles). Cette théorie quantique de l’amplification est présentée au ch. 2. Les amplificateurs paramétriques Josephson ont été conçus précisément pour ajouter le moins de bruit possible et opérer près de la limite quantique. Ils sont donc des éléments-clés dans les mesures micro-ondes de haute sensibilité. Dans ce travail, nous utilisons un JPA, représenté schématiquement Fig. 1c, et dont la conception est expliquée au ch. 2. Notre JPA est constitué d’un résonateur comprenant un réseau de SQUIDs et d’une ligne de pompe permettant de moduler le flux magnétique traversant les SQUIDs. Un signal micro-onde de pompe de fréquence _!p ⇡_ 2 _!_ envoyé sur cette ligne crée un gain paramétrique pour un signal de fréquence _!_ . Ce JPA pompé en flux possède deux modes de fonctionnement. Si _!p_ = 2 _!_ (mode "non-dégénéré"), les deux quadratures du signal sont amplifiées et _n_ amp = 1 _/_ 4 de sorte que le bruit total détecté _n_ = _n_ eq + _n_ amp sur une quadrature est _n_ = 1 _/_ 2. Si _!p_ = 2 _!_ (mode "dégénéré"), une seule quadrature est amplifiée, ce qui permet d’échapper à la limite quantique à l’amplification avec _n_ amp = 0 et _n_ = _n_ eq = 1 _/_ 4. Les JPAs ont été utilisés pour détecter l’état de qubits supraconducteurs [21], d’oscillateurs nanomécaniques [22], l’état de charge 

3 

_Contents_ 



<!-- Start of picture text -->
spins<br>g<br>ω<br>�<br>B<br>0<br><!-- End of picture text -->

FIGURE 2: **Description quantique de l’interaction spin-photon.** Un ensemble de spins placé dans une cavité de fréquence _!_ 0 et de facteur de qualité _Q_ = _!_ 0 _/_ interagit avec une force d’interaction _g_ avec le champ micro-onde. 

d’une boîte quantique [23], ainsi que pour améliorer la sensibilité de mesures de magnétométrie [24]. Fonctionnant à des fréquences gigaHerz, ils sont facilement utilisables pour l’amplification des faibles signaux micro-ondes émis par les spins comme cela est montré dans la deuxième partie de cette thèse. Ils peuvent également générer des états comprimés, qui ont moins de fluctuations sur une quadrature que le vide, au prix de fluctuations accrues sur l’autre quadrature de sorte à satisfaire l’inégalité de Heisenberg (voir Fig. 1d). Nous utilisons ces états pour effectuer des mesures au-delà de la limite quantique dans la quatrième partie. 

Les fluctuations quantiques du champ sont également essentielles pour décrire l’interaction entre les spins et le champ micro-onde d’un résonateur de fréquence _!_ 0 et de facteur de qualité _Q_ . Le paramètre-clé décrivant cette interaction est la constante de couplage spin-photon notée _g_ , qui est le produit du moment dipolaire magnétique d’un spin et les fluctuations du vide du champ magnétique à l’emplacement du spin. Au ch. 3, nous utilisons le modèle de Jaynes-Cummings pour décrire les expériences de résonance magnétique, où un ensemble de spins est placé dans un résonateur micro-onde (voir Fig. 2). Contrairement à la plupart des expériences cQED, les expériences de résonance magnétique ont lieu dans le régime de couplage faible où _g ⌧ _ , avec __ = _!_ 0 _/Q_ . Nous montrons que dans cette limite, une description semi-classique de la dynamique des spins est suffisante, pourvu qu’elle soit complétée par un mécanisme de relaxation supplémentaire: l’émission spontanée de photons micro-ondes par le spin dans le résonateur, déclenchée par les fluctuations quantiques de le champ. Le taux de relaxation de cet effet, appelé effet Purcell, est: 



où ∆ est le désaccord fréquentiel entre le spin et le résonateur. Bien que cette relaxation radiative de spin ait toujours été négligée par rapport à d’autres mécanismes de relaxation de spins, nous montrons dans la troisième partie qu’elle peut devenir le mécanisme dominant pour des spins placés dans un résonateur à haut facteur de qualité et petit volume de mode. L’utilisation du modèle de Jaynes-Cummings permet aussi d’exprimer le champ émis par les spins dans le guide d’onde de détection: _hXi_ = 2 _g/_<sup>_p_</sup> _<u>hS−i</u>_ (voir ch. 3). La maximisation du signal de sortie est donc obtenue dans les mêmes conditions que la maximisation de l’émission spontanée par l’effect Purcell, à savoir l’utilisation d’un résonateur de petit mode volume et de haut facteur de qualité. 

Dans cette thèse, nous présentons trois expériences de résonance magnétiques où l’impact des fluctuations micro-ondes quantiques est mis en évidence. Pour réaliser nos expériences, nous utilisons le spin des donneurs de bismuth du silicium. Ces donneurs sont des atomes du réseau cristallin du silicium. A basse température, ils sont à l’état neutre grâce au piégeage d’un électron de la bande de conduction du silicium (voir Fig. 3 a). Les propriétés-clés de ces systèmes sont leur long temps de cohérence (pouvant atteindre des secondes [25]), et l’existence d’une séparation de 7.4 GHz entre les niveaux de spin électronique à champ nul [26]. Il est donc possible de coupler des spins Si:Bi à des résonateurs supraconducteurs en utilisant de faibles champs magnétiques ( _<_ 10 mT), compatibles avec la plupart des matériaux supraconducteurs et en particulier l’aluminium utilisé 

4 



<!-- Start of picture text -->
©<br>oe<br><!-- End of picture text -->



<!-- Start of picture text -->
?<br><!-- End of picture text -->









<!-- Start of picture text -->
I~ Z<br><!-- End of picture text -->



<!-- Start of picture text -->
r<br><!-- End of picture text -->







<!-- Start of picture text -->
= le<br>a ) ae<br><!-- End of picture text -->



<!-- Start of picture text -->
 >> &<br>= X e]<br><!-- End of picture text -->

_Contents_ 

### **3 Détection de RPE avec une sensibilité limitée signaux quantiquement** 

Dans la deuxième partie de la thèse, nous présentons la conception et la réalisation d’un spectromètre RPE dont la sensibilité est largement améliorée par l’utilisation des techniques et des concepts cQED. Comme tous les spectromètres RPE existants, notre dispositif expérimental se compose d’un résonateur de fréquence _!_ 0 et de facteur de qualité _Q_ couplé à un ensemble de spins dont la fréquence de Larmor est accordée au résonateur par l’application d’un champ magnétique externe _B_ 0. L’application d’impulsions micro-ondes à résonance génère une aimantation de spin transverse qui conduit à l’émission de signaux micro-ondes généralement appelés "échos". La séquence de RPE la plus connue, l’écho de Hahn, se compose d’une impulsion _⇡/_ 2 suivie après un délai _⌧_ d’une impulsion _⇡_ qui conduit à un rephasage des spins après un second délai _⌧_ et à l’émission d’un écho de Hahn. La sensibilité d’un spectromètre est caractérisée par le nombre minimum de spins _N_ min détectables par écho de Hahn avec un rapport signal sur bruit (SNR) unité. 

Sur la base des concepts introduits dans la première partie, nous dérivons au ch. 5 une expression quantitative de _N_ min, qui met en évidence les quantités à optimiser pour améliorer la sensibilité d’un spectromètre RPE. Ainsi, la constante de couplage spin-photon _g_ et le facteur de qualité du résonateur _Q_ doivent être maximisés; l’utilisation de températures cryogéniques conduit à une polarisation accrue des spins et à un bruit réduit. Les spectromètres usuels utilisant des résonateurs tridimensionnels à température ambiante ont une sensibilité typique de _N_ min _⇡_ 10<sup>13</sup> spins. Ce nombre a été considérablement réduit en utilisant des résonateurs supraconducteurs de taille micronique refroidit à 4 K et des amplificateurs possédant des températures de bruit de l’ordre de 4 K, donnant lieu à des sensibilités mesurées de _N_ min = 10<sup>7</sup> spins [15]. 

Aux ch. 5-7, nous présentons notre implémentation d’un spectromètre RPE utilisant les outils de cQED, et en particulier l’amplification micro-onde à la limite quantique. Le spectromètre est basé sur un résonateur à éléments discrets supraconducteur de haut facteur de qualité, fabriqué sur un substrat de silicium qui contient l’ensemble des spins Si:Bi. Le résonateur est placé dans un porte-échantillon de cuivre et couplé capacitivement aux antennes d’excitation et de détection (voir Fig. 3b). La géométrie du résonateur est conçue pour que le couplage spin-photon atteigne _g/_ 2 _⇡ ⇡_ 50 Hz et l’échantillon est thermalisé à 20 mK pour obtenir une polarisation de spin totale. Le signal d’écho de spin est amplifié par un JPA, suivi d’une amplification supplémentaire à 4 K et à température ambiante (voir Fig. 3c). Le ch. 5 décrit la conception et la mise en œuvre expérimentale du spectromètre. 

Nous utilisons ce dispositif expérimental pour effectuer une spectroscopie détaillée des spins Si:Bi (voir Fig. 4a&c) ainsi que des mesures du temps de cohérence (voir Fig. 4b). Nous observons une forme de ligne inhabituelle, où chaque résonance apparait sous la forme d’un double pic asymétrique. Au ch. 6, nous soutenons que cette forme de raie est due aux contraintes mécaniques induites dans le substrat par les contractions thermiques du film d’aluminium déposé sur le silicium. 

Au ch. 7, nous caractérisons la sensibilité du spectromètre. Par des mesures précises du rapport signal sur bruit (voir Fig. 4c-d), complétées par des simulations numériques, nous démontrons une sensibilité sans précédent de 2000 spins détectables par écho avec un signal sur bruit unité. Ceci représente une amélioration de quatre ordres de grandeur par rapport à l’état de l’art de la détection RPE {[15], obtenue grâce à l’utilisation combinée de températures cryogéniques permettant la polarisation totale des spins, le grand facteur de qualité et le petit volume de mode du résonateur, et le JPA. 

6 

_Contents_ 



<!-- Start of picture text -->
a 1.0 b 1.0<br>T  = 8.9 ms<br>2<br>0.5 0.5<br>0.0<br>0.0<br>5 6 7 8 0 10 20 30 40<br>Champ magnétique (mT) Délai, 2  �  (ms)<br>c d<br>HEMT JPA<br>0.1<br>(x 38)<br>1 1.0<br>� 0.0<br>0.60 0.64 0.68<br>0.5<br>Temps (ms)<br>�π echo<br>�π /2x y 0.0<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0 20 60 100<br>Temps (ms) Temps (µs)<br>Amplitude (V)<br> (V)<br>I<br>signal d’écho (a.u.)<br>signal d’écho (a.u.)<br><!-- End of picture text -->

FIGURE 4: **RPE limitée quantiquement : principaux résulats. a** Spectroscopie par écho de Hahn de deux transitions consécutives des spins Si:Bi, mettant en évidence deux doublets asymétriques, au lieu des deux raies gaussiennes attendues. **b** Un temps de cohérence _T_ 2 = 8 _._ 9 ms est mesuré à _B_ 0 = 5 _._ 13 mT. **c** Séquence d’écho de Hahn mesurée à _B_ 0 = 5 _._ 13 mT. Les points bleus sont les points expérimentaux, ajustés par un modèle numérique (ligne rouge continue) démontrant que 1 _._ 2 _⇥_ 10<sup>4</sup> spins sont excités par la première impulsion _⇡/_ 2. **d** Le JPA apporte une amélioration d’un facteur dix du signal sur bruit. 

### **4 Effet Purcell appliqué aux spins** 

Un autre élément-clé de la sensibilité est le taux de répétition de la mesure. Aux basses températures où sont réalisées nos expériences, le taux de relaxation des spins peut devenir extrêmement faible, limitant de fait la sensibilité absolue du spectromètre. Au ch. 8, nous proposons l’effet Purcell comme mécanisme de relaxation universel, pouvant s’appliquer à n’importe quel type de spins [27], apportant ainsi une solution au problème de la ré-initialisation des spins. Cet effet est induit par les fluctuations quantiques du champ micro-onde de la cavité, comme évoqué plus tôt. L’émission spontanée, renforcée par la concentration du champ permise par la cavité, offre aux spins un nouveau canal de relaxation pour atteindre l’équilibre thermique lorsqu’ils sont accordés à résonance avec la cavité. L’effet Purcell est employé couramment pour contrôler le temps de vie d’autres TLS, notamment d’atomes [28] et d’hétérostructures semiconductrices [29] insérés dans des cavités microondes et/ou optiques. C’est aussi un des principes-clés pour la réalisation de sources de photons uniques brillantes [30]. Pour des spins néanmoins, leur faible couplage au champ électromagnétique de l’espace libre rend leur temps de relaxation par émission spontanée tout à fait négligeable comparé aux autres mécanimes de relaxation possibles. 

Cependant, nous montrons au ch. 8 que pour notre géométrie un taux Γ _p ⇡_ 3 s<sup>_−_1</sup> est attendu. Une mesure expérimentale du temps _T_ 1 en utilisant notre dispositif donne _T_ 1 = 0 _._ 35 s pour des spins à résonance, comme illustré sur la Fig. 5b. Une conséquence directe est que toutes nos mesures peuvent être répétées à un taux de 1 Hz; le spectromètre décrit au-dessus a donc une sensibilité absolue de 1700 spins/ _p_ Hz. 

Même si le temps _T_ 1 mesuré expérimentalement est similaire à celui attendu par la théorie, nous réalisons deux expériences supplémentaires prouvant définitivement que l’effet Purcell est bien 

7 

_Contents_ 



<!-- Start of picture text -->
a b c<br>���� 0<br>1<br>1.0<br>0<br>T  = 0.35 s<br>1 0.5<br>���� 0,  g=g 0 4 g 2<br>Rayonnement assisté -1 � P = �<br>par cavité 0 1 2 3 0.00 0.5 1<br>Time T (s) g ² /  g 0²<br>d<br>10 3<br>relaxation<br>non-radiative<br>g<br>Relaxation<br>10 2<br>����ω / Q par phonon<br>�<br>rate : 10 -5  s -1<br>�� =  ω �−�ω<br>s 0<br>10<br>Relaxation par<br>effet Purcell<br>g=g 0<br>1<br>-4 -2 0 2 4<br>�/2π (MHz)<br>(s)<br>1<br>T<br>-1)<br> (s1<br>T<br>1/<br>Polarization<br><!-- End of picture text -->

FIGURE 5: **Observation de l’effet Purcell pour des spins a** Un spin placé dans une cavité résonante peut voir sa relaxation par émission spontanée devenir le mécanisme de relaxation dominant, devant d’autres processus intrinsèques comme la relaxation par phonon. **b** Pour des spins Si:Bi accordés à résonance en utilisant le setup de la Fig. 3, l’effet Purcell induit un temps de relaxation de _T_ 1 = 0 _._ 35 s. **c** Temps de relaxation _T_ 1 en fonction de _g_<sup>2</sup> ; la ligne continue est un ajustement linéaire. **d** Une augmentation de _T_ 1 sur trois ordres de grandeur est démontrée en désaccordant les spins de moins de 0 _._ 2 mT, jusqu’à ce qu’un processus non-radiatif devienne plus efficace que l’effet Purcell, et place une borne supérieure au temps _T_ 1 de 1500 s. 

le mécanisme de relaxation dominant dans notre dispositif. Premièrement, nous montrons que le temps _T_ 1 varie linéairement en fonction de _g_<sup>_−_2</sup> (cf Fig. 5c), conformément à l’expression de Γ _p_ à résonance. Deuxièmement, la Fig. 5d démontre une variation lorentzienne de _T_ 1 en fonction du désaccord ∆. En contrôlant ∆, _T_ 1 augmente de trois ordres de grandeur, jusqu’à un maximum de 1500 s. Au-delà, _T_ 1 devient indépendant de ∆, mettant en évidence qu’un autre mécanisme de relaxation, non-radiatif, devient dominant. 

Nous concluons cette troisième partie par une discussion brève des applications possibles de cette émission spontanée assistée par cavité. 

### **5 États comprimés et résonance magnétique** 

Dans un spectromètre RPE à la limite quantique, le bruit provient presque entièrement des fluctuations quantiques du champ micro-onde. Il est possible de réduire ces fluctuations en utilisant des état quantiques comprimés. Cette idée de mesures au-delà de la simple limite quantique a été proposée 

8 



<!-- Start of picture text -->
\ 0 A /<br>I B Il I Jr| l l l hi | Fy<br><!-- End of picture text -->

_Contents_ 

principalement limité par les pertes micro-ondes présentes dans le dispositif. Nous concluons cette partie en analysant les limites de cette mise en œuvre expérimentale d’états comprimés pour la détection RPE, et il apparait qu’en principe une amélioration du signal sur bruit de 10 dB pourrait être envisageable. 

10 

## **Chapter 1** 

# **Introduction** 

### **1.1 Circuit quantum electrodynamics for magnetic resonance** 

Photons and spins are two fundamental concepts born in the early days of quantum mechanics and are key in many active research fields. The discovery that spins can absorb or emit microwave radiation when coupled to a resonator matched to their Larmor precession frequency by Rabi [1], Bloch [2] and Purcell [3] gave birth to the field of magnetic resonance, which encompasses both magnetic resonance of nuclear (NMR [4]) and electronic (ESR[5]) spins. Magnetic resonance made it possible to identify spin species contained in a sample and study their interactions, leading to a deeper understanding of matter and its organisation at the atomic level. These powerful spectroscopy techniques have nowadays a wide range of applications throughout biology, chemistry and materials science, ranging from non-destructive bio-imaging [36] to drug discovery [6]. Another application is Quantum Information Processing (QIP), where the spins are used as "qubits", the carriers of quantum information [7]. 

In all magnetic resonance experiments so far, independently of the application, spins are always treated quantum mechanically for what regards spin-spin interactions, spin coherence and spin relaxation phenomena, while the microwave fields used to manipulate and detect them are described classically. This semi-classical treatment of the spin-field interaction is justified by two facts. First, the spin-photon coupling is generally so weak that the quantum nature of the microwave field has negligible effects on the spins dynamics compared to their coupling to the lattice vibrations or to other neighboring spins. Second, at the temperature where most magnetic resonance experiments are realized, the vacuum fluctuations of the microwave field are negligible compared to thermal fluctuations; moreover, the lack of a microwave detector with high quantum-efficiency prevents their detection. These two arguments are closely related to the poor sensitivity of ESR spectrometers: it is because spins are weakly coupled to the microwave field that a successful detection requires a large number of spins for the collected signal to overcome the experimental noise, which itself is largely above the quantum noise limit. 

In stark contrast, in the field of Cavity Quantum ElectroDynamics (CQED, [8]), individual two-level systems (TLS) interact coherently with the electromagnetic field at the single-photon level. The TLS can be implemented by superconducting non-linear circuits called Josephson qubits, interacting with high-quality factor microwave resonators in an architecture called Circuit-QED (CQED, [9, 10]) which is promising for quantum computing. Within CQED, novel techniques have been developed to engineer and detect the quantum state of the microwave field; in particular, ultra-low-noise microwave amplifiers have been developed for the readout of Josephson qubits. These Josephson Parametric Amplifiers (JPA) add as little noise to the signal as quantum mechanics allows, and they are in fact able to amplify noiselessly one quadrature of the field [11, 12, 13]. This thesis reports **the application of cQED techniques and concepts to ESR in order to perform magnetic resonance experiments in a novel regime where quantum fluctuations of the microwave field have a major influence on the spectrometer sensitivity as well as on the spin dynamics.** 

11 

_Chapter 1. Introduction_ 

The first part of the manuscript aims at providing the conceptual tools needed to understand the experiments. We give a brief account of the quantum description of microwave fields and resonators, and of their interaction with TLS, which is the essence of cQED. This allows us to present a quantum treatment of ESR spectroscopy detection. We also present the spin-system with which all the experimental work was realized: bismuth donors in silicon. 

In the second part of this thesis, we present the design and physical realization of a "circuit-QEDenhanced" ESR spectrometer. It relies on a high-quality factor superconducting resonator of small mode volume, strongly coupled to bismuth donor spins, and on a JPA that amplifies the spin signal. The output noise of this spectrometer is entirely set by quantum fluctuations of the microwave field; in that sense, it reaches the quantum limit of sensitivity. We demonstrate an unprecedented sensitivity of 2000 spins per experimental sequence [14], which represents a four orders of magnitude improvement compared to the state-of-the-art [15]. 

Performing ESR at millikelvin temperatures has the additional benefit that the spin ensemble is fully polarized at thermal equilibrium. However, such low temperatures can also increase dramatically the spin-lattice relaxation time [16] leading to impractically low repetition rates. In the third part of this thesis, we demonstrate that the coupling of the spins to an ESR resonator of high-quality-factor and small-mode-volume leads to a strong enhancement of the rate at which they relax to their ground state by spontaneously emitting a microwave photon, to the point where it becomes a spin relaxation mechanism more efficient than phonon emission. This phenomenon, well-known in CQED and predicted by Purcell in 1946, is observed with spins for the first time [17]. 

As already discussed, the only remaining source of noise in our spectrometer is the vacuum fluctuations of the microwave field. Although this seems to represent a fundamental limit for sensitivity, it is known from quantum optics that this limit can be overcome using so-called quantum squeezed states [18, 19, 20]. In such quantum states of the field, the noise on one quadrature is reduced below the vacuum level whereas the noise on the other quadrature is increased to fulfill Heisenberg uncertainty principle. We report in part four the use of microwave squeezed states to enhance the sensitivity of our ESR spectrometer beyond the quantum-limit. 

### **1.2 Quantum microwaves and spin dynamics** 

There are multiple reasons for a quantum treatment of microwave fields to become relevant in magnetic resonance experiments. A classical microwave signal at frequency _!_ is described by its amplitude _A_ and its phase _φ_ , or equivalently by its in-phase and out-of-phase quadratures _X_ = _A_ cos( _φ_ ) and _Y_ = _A_ sin( _φ_ ). In a quantum-mechanical description outlined in ch. 2, the quadrature<sup>1</sup> variances are constrained by the Heisenberg inequality ~~p~~ _h_ ∆ _X_<sup>2</sup> _ih_ ∆ _Y_<sup>2</sup> _i_ > 1 _/_ 4. As a consequence, even at low temperatures _kBT ⌧_ ~ _!_ where the field is in its quantum-mechanical ground state, fluctuations remain. Expressing the amount of fluctuations per quadrature for a microwave field at temperature T by the dimensionless quantity _n_ eq( _T_ ) = _h_ ∆ _X_<sup>2</sup> _i_ , the vacuum fluctuations are characterized by reaching the minimum value of _n_ eq = 1 _/_ 4 (see Fig.1.1a). These vacuum fluctuations thus represent a fundamental limit to the sensitivity of many measurements, and in particular to ESR spectroscopy. 

A major progress brought by cQED is to provide the tools needed to detect quantum microwave fluctuations. As several orders of magnitudes separate the small power of the quantum microwave signals and the noise figure of typical room-temperature measurement apparatus, it is essential for the signal to be amplified. Upon amplification, quantum mechanics "takes its due a second time", by imposing some constraints on the noise _n_ amp added to the quadrature _X_ (also expressed in dimensionless units). This quantum theory of amplification is presented in ch. 2. The Josephson Parametric Amplifiers have been developed precisely to add as little noise as required by quantum 

> 1re-written in dimensionless units, such that ~ _!_ ( _hX_ 2 _i_ + _hY_ 2 _i_ ) equals the field mode energy 

12 

_Chapter 1. Introduction_ 



<!-- Start of picture text -->
ω<br>a Y b c<br>ω<br>0<br>out<br>∆ Y 2 = 1 JPA<br>2 X out<br>ω flux pump<br>p<br>d e<br>30 20<br>Y<br>25<br>10<br>X<br>20<br>Y<br>15 0<br>10<br>X<br>-10<br>5<br>ω =2 ω<br>p 0<br>0 -20 -10 0 10 20 -200 π/4 π/2<br>( ω - ω p/2)/2 π  (MHz) φ−φ p (°)<br>in<br>in<br>Gain (dB) Gain (dB)<br><!-- End of picture text -->

FIGURE 1.1: **Quantum fluctuations and quantum-limited amplification. a** At temperatures _kBT ⌧_ ~ _!_ , the ground state of the microwave field is reached, with its quadrature variances given by p _h_ ∆ _X_<sup>2</sup> _i_ = p _h_ ∆ _Y_<sup>2</sup> _i_ = 1 _/_ 2 imposing a minimum to the field fluctuations (blue shade). **b-c** A Josephson Parametric Amplifier, here implemented by a flux-pumped SQUID resonator, can be used to detect quantum microwave fields. **d** When employed in non-degenerate mode ( _!p_ = 2 _!_ ), the JPA adds half a noise photon (red shade) to the half-noise photon (blue shade) arising from the input vacuum fluctuations. **e** When operated in its degenerate mode ( _!p_ = 2 _!_ ), it amplifies one quadrature at the expense of the other; in this case the amplification is noiseless. Acting on a vacuum state, it produces a squeezed state, with fluctuations deamplified for one quadrature but amplified on the other one (blue shade). 

mechanics and are thus key novel tools in high-sensitivity microwave measurements. In this work, we use a JPA whose design is explained in ch. 2 and is schematically shown in Fig. 1.1c. The JPA is powered by a pump microwave signal at frequency _!p ⇡_ 2 _!_ which modulates the magnetic flux threading the loops of an array of SQUIDs embedded in a resonator, resulting in parametric gain at _!_ . This flux-pumped JPA has two modes of operation. If _!p_ = 2 _!_ ("non-degenerate mode"), both signal quadratures are amplified equally with _n_ amp = 1 _/_ 4 so that the overall detected noise _n_ = _n_ eq + _n_ amp for one quadrature is _n_ = 1 _/_ 2. If _!p_ = 2 _!_ ("degenerate mode"), only a single quadrature is amplified, allowing to evade the quantum limit for amplification so that _n_ amp = 0 and _n_ = _n_ eq = 1 _/_ 4. JPAs have been used to read-out the state of superconducting qubits [21], the motion of nanomechanical oscillators [22], and the charge state of a quantum dot [23], as well as for high-sensitivity magnetometry [24]. Working at gigaHerz frequencies, they are readily applicable to the amplification of weak microwave signals emitted by spins as will be shown in part two of this thesis. They can also generate squeezed states, which have less fluctuations on one quadrature, but increased fluctuations on the other one to fulfill Heisenberg uncertainty principle (see Fig. 1.1d). We use such states to perform measurements beyond the quantum-limit in part four. 

Quantum microwave fluctuations are also key to describe the interaction between the spins and the microwave field in a resonator of frequency _!_ 0 and quality factor _Q_ . The key parameter describing this interaction is the so-called spin-photon coupling constant noted _g_ , which is the product of the spin magnetic dipole moment and the magnetic field vacuum fluctuations at the 

13 



<!-- Start of picture text -->
Ar<br>{#]<br>vo /<br><!-- End of picture text -->

_Chapter 1. Introduction_ 



<!-- Start of picture text -->
a b<br>209Bi<br>�<br>1 B<br>0<br>�<br>2 C/2 L<br>spins<br>Si<br>10<br>F=5<br>5 0.3<br>0 Al wire<br>-5<br>F=4<br>-0.3<br>-10<br>z (µm)<br>Energy Levels (GHz)<br><!-- End of picture text -->



<!-- Start of picture text -->
1.4 mm<br>L C/2<br><!-- End of picture text -->



<!-- Start of picture text -->
spins<br><!-- End of picture text -->



<!-- Start of picture text -->
Al wire<br>-2 0 2 0 10<br>y (µm) Bi concentration<br>B<br>1<br><!-- End of picture text -->



<!-- Start of picture text -->
π π /2 Si:Bi echo<br>JPA<br>� 1 � 2 ω p<br>ω<br>� Pump<br>20 mK<br>B<br>0<br><!-- End of picture text -->



<!-- Start of picture text -->
ω� LO<br>RF I<br>Q t<br>HEMT<br>4K 300K<br><!-- End of picture text -->

FIGURE 1.3: **Quantum-limited ESR : principle and experimental setup a** A bismuth donor in silicon consists of a substitutional bismuth atom in the silicon lattice. In its neutral charge state, it traps a conduction electron that yields the ESR signal. The 20 energy levels of neutral bismuth donors, shown here as a function of an applied static magnetic field, are the result of the large hyperfine interaction between the _S_ = 1 _/_ 2 electron spin to the _I_ = 9 _/_ 2 nuclear spin of the bismuth atom; in particular there is a 7 _._ 4 GHz separation between level multiplets at zero applied field. **b** The ESR resonator consists of an interdigitated capacitor in parallel with a 5-µm-wide inductor, patterned in a superconducting thin film of aluminum deposited on top of a silicon chip implanted with bismuth spins. The chip contains three nearly identical resonators; it is enclosed in a copper sample holder coupled via microwave antennas to the measurement waveguides. **c** The resonator with the Si:Bi spins is anchored at 20 mK (blue) and is probed by microwave signals triggering the emission of an echo in the detection waveguide. The echo signal is amplified successively by a JPA, a HEMT at 4 K before being amplified and demodulated at room-temperature. 

of a spectrometer is characterized by the minimum number of spins _N_ min detectable in a single Hahn-echo with a signal-to-noise (SNR) unity. 

Based on the concepts introduced in the first part, we derive in ch. 5 a quantitative expression of _N_ min, which clearly shows which quantities need to be optimized to improve the sensitivity of an ESR spectrometer. The spin-photon coupling constant _g_ and the resonator quality factor _Q_ should be maximized; and low-temperatures lead to increased spin polarization and reduced noise. Regular spectrometers using three-dimensional resonators and operating at room-temperature have a typical sensitivity of _N_ min _⇡_ 10<sup>13</sup> spins. This number has been greatly improved by combining micron-scale superconducting resonators operating at 4 K and the use of amplifiers with noise temperatures of 4 K, yielding reported sensitivities of _N_ min = 10<sup>7</sup> spins [37]. 

15 

_Chapter 1. Introduction_ 



<!-- Start of picture text -->
a 1.0 b 1.0<br>T  = 8.9 ms<br>2<br>0.5<br>0.5<br>0.0<br>0.0 0 10 20 30 40<br>5 6 7 8<br>Time, 2  �  (ms)<br>c Magnetic Field (mT) d<br>HEMT JPA<br>0.1 (x 38)<br>1 1.0<br>� 0.0<br>0.60 0.64 0.68<br>0.5<br>Time (ms)<br>�π echo<br>�π /2x y 0.0<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0 20 60 100<br>Time (µs)<br>Time (ms)<br>Amplitude (V)<br> (V)<br>I<br>echo signal (a.u.)<br>echo signal (a.u.)<br><!-- End of picture text -->

FIGURE 1.4: **Quantum-limited ESR : main results. a** Hahn-echo detected Si:Bi spectroscopy of two consecutive transitions, evidencing asymmetric split peaks instead of the expected Gaussian lineshapes. **b** A coherence time _T_ 2 = 8 _._ 9 ms is measured at _B_ 0 = 5 _._ 13 mT. **c** Hahn-echo sequence recording at _B_ 0 = 5 _._ 13 mT. Blue points are raw data, fitted by a numerical model (red line) proving that 1 _._ 2 _⇥_ 10<sup>4</sup> spins are excited by the first _⇡/_ 2 pulse. **d** The JPA brings a ten-fold enhancement to the signal-to-noise ratio. 

In ch. 5-7, we present our implementation of an ESR spectrometer using the tools of cQED, and in particular microwave amplification at the quantum limit. The spectrometer is based on a highquality factor superconducting lumped element resonator, deposited on top of a silicon substrate which contains the ensemble of Si:Bi donor spins, enclosed in a copper sample holder, and coupled to the detection waveguides by excitation and detection antennas (see Fig. 1.3b). The resonator geometry is designed so that the spin-photon coupling reaches _g/_ 2 _⇡ ⇡_ 50 Hz and the sample is anchored at 20 mK to have full spin polarization. The spin-echo signal is amplified by a JPA, followed by further amplification at 4 K and room-temperature (see Fig. 1.3c). Chapter 5 describes the spectrometer design and experimental implementation. 

In ch. 6, using Hahn-echo detected field sweeps (see Fig. 1.4a-c), we use this setup to perform detailed spectroscopy of Si:Bi donors spins as well as coherence time measurements (see Fig. 1.4b). We observe a peculiar line shape, with each Si:Bi resonance appearing as an asymmetric split peak. In ch. 6 we argue that this line shape is caused by mechanical strain due to thermal contractions of the deposited aluminum film onto the silicon substrate. 

In ch. 7, we characterize the spectrometer sensitivity. By careful signal-to-noise ratio measurements (see Fig. 1.4c-d) complemented with numerical simulations, we demonstrate an unprecedented sensitivity of 2000 detectable spins per echo with SNR=1. This represents a four-order-of-magnitude improvement compared to the state-of-the-art of inductive detection, obtained thanks to the combined use of cryogenic temperatures allowing for the full polarization of the spins, the high quality factor of the resonator, and the JPA. 

16 

_Chapter 1. Introduction_ 



<!-- Start of picture text -->
a b c<br>���� 0<br>1<br>1.0<br>0<br>T  = 0.35 s<br>1 0.5<br>Cavity-enhancedradiation -1 ���� 0,  g=g 0 � P =4 � g 2<br>0.0<br>0 1 2 3 0 0.5 1<br>Time T (s) g ² /  g 0²<br>d<br>10 3<br>non-radiative<br>decay<br>g<br>Phonon<br>10 2<br>����ω / Q relaxation<br>�<br>rate : 10 -5  s -1<br>�� =  ω �−�ω<br>s 0<br>10<br>Purcell enhanced<br>relaxation<br>g=g 0<br>1<br>-4 -2 0 2 4<br>�/2π (MHz)<br>(s)<br>1<br>T<br>-1)<br> (s1<br>T<br>1/<br>Polarization<br><!-- End of picture text -->

FIGURE 1.5: **The Purcell effect for spins. a** By placing a spin in a resonant cavity, radiative spin relaxation can be made to dominate over intrinsic processes such as phonon-induced relaxation. **b** For Si:Bi spins tuned at resonance, the Purcell effect gives a relaxation time of _T_ 1 = 0 _._ 35 s using the setup of Fig. 1.3. **c** Measured relaxation time _T_ 1 as a function of _g_<sup>2</sup> ; the solid line is a linear fit. **d** A change in _T_ 1 by 3 orders of magnitude is demonstrated by detuning the spins by less than 0 _._ 2 mT, up until a non-radiative relaxation process dominates the Purcell effect and effectively limits _T_ 1 to 1500 s. 

### **1.4 The Purcell effect applied to spins** 

Another key aspect of the sensitivity is the repetition rate. At the low temperatures of our experiments, the spin relaxation rate may become exceedingly low, limiting effectively the absolute sensitivity of the spectrometer. In ch. 8, we use the Purcell effect to demonstrate a re-initialization mechanism applicable to any spin system [27]. This effect arises from the quantum fluctuations of the cavity field, as mentioned earlier. Cavity-enhanced spontaneous emission provides a new way to reach thermal equilibrium for the spin ensemble. It strengthens the spontaneous emission of microwave photons by the spin when it is tuned at resonance with the cavity and thus ensures its eventual return to thermal equilibrium. The Purcell effect has been used extensively to control the lifetime of other TLS such as atoms [28] and semi-conducting heterostructures [29] placed in microwave and optical cavities. It is also a key concept in the realization of bright single-photon sources [30]. For spins however, due to their very weak coupling to the free space electromagnetic field, the estimated rate is usually so low that it is commonly dismissed as a possible source of relaxation. 

We show in ch. 8 that for our resonator characteristics, we expect Γ _p ⇡_ 3 s<sup>_−_1</sup> . An experimental measurement of _T_ 1 using our setup yields _T_ 1 = 0 _._ 35 s for spins at resonance, as shown in Fig. 1.5b. 

17 



<!-- Start of picture text -->
\ 0 A /<br>I B Il I Jr| l l l hi | Fy<br><!-- End of picture text -->

_Chapter 1. Introduction_ 

For squeezed states, the noise in one field quadrature is reduced below the vacuum level whereas the other quadrature has more noise, to fulfill Heisenberg uncertainty principle (see Fig. 1.6a). Since then, optical squeezed vacuum fields have been observed [19] and used to enhance the sensitivity in a number of experiments, ranging from gravitational waves detectors [31] to atom-based magnetometry [32]. They have also been produced at microwave frequencies [33] and used for fundamental light-matter interaction studies [34] and enhanced sensing of a mechanical resonator [35]. 

In the fourth part of this thesis, we use a squeezed microwave field as depicted in Fig. 1.6b to improve the sensitivity of the spectrometer beyond the quantum limit. Our experiment consists in sending a squeezed vacuum state onto the input of the ESR resonator, while driving the spins with a Hahn echo sequence. The squeezed quadrature is aligned with the quadrature on which the echo is emitted, leading to reduced noise. The squeezed vacuum state is produced by a second JPA - called the squeezer SQZ - placed at the cavity input. 

The main results are shown in Fig. 1.6. First, the average echo amplitude is unchanged when the squeezing is on (see Fig. 1.6c). However the noise histograms reveal that the noise has indeed been reduced in the detection (see Fig. 1.6d). The fact that the signal is unaffected while the noise is decreased demonstrates a net enhancement of the signal-to-noise ratio of the experiment by a factor 1.12. It gives a proof-of-concept that magnetic resonance beyond the standard quantum limit is possible. The modest improvement in SNR is due to the limited degree of squeezing achieved, which is in particular due to losses in the microwave setup. We conclude this part by a thorough analysis of the experiment limitations, and we find that in principle, SNR enhancements as large as 10 dB could be achieved in the future. 

19 

## **Part I** 

# **Background** 

20 

## **Chapter 2** 

# **Quantum circuits and quantum noise** 

For our purpose to perform magnetic resonance with quantum microwave fields, a quantum description of the resonator and of the microwave field is needed. Such description has been used extensively in the field of superconducting circuits and we give here only the results pertaining to the experimental work detailed later on. First, we describe the principal properties of quantum microwave fields as well as the principal quantum states used later on. We then recall the quantization of the mode of a LC resonator as well as of a microwave field propagating along a transmission line. We finally give elements of input-output theory, which describes how the intra-cavity field of a linear or non-linear resonator is related to the propagating modes of the transmission lines to which it is coupled for measurement. In the second part of this chapter, we present the quantum theory of linear amplifiers; in particular we derive the so-called quantum limit of amplification, which gives the minimum amount of noise necessarily added by any amplifier to satisfy the basic principles of quantum mechanics. We also describe the design and working principle of a Josephson Parametric Amplifier, a device which reaches this quantum limit. 

### **2.1 Quantum microwaves and quantum circuits** 

In our experiment, the resonator circuit is coupled to external measurement fields via transmission lines. At temperatures lower than ~ _!/kB_ , the microwave fields residing in the resonator and propagating fields in the transmission lines are cooled down to their ground state and thus require a quantum mechanical description. 

#### **2.1.1 Quantum description of an electromagnetic mode : quantum noise and quantum states** 

A good review of the quantization of electromagnetic modes and quantum states can be found in [38]. We consider a given mode of the electromagnetic field, at frequency _!_ . Classically, this mode is characterized by its complex amplitude _A_ = _|A|e_<sup>_iφ_</sup> . It can be equivalently described by its in-phase and out-of-phase quadratures usually defined as _X_ = Re( _A_ ) and _Y_ = Im( _A_ ). In the frame rotating at frequency _!_ , the field can thus be represented in phase space as a point of polar coordinates ( _|A|, φ_ ) or cartesian coordinates ( _X, Y_ ) (see Fig. 2.1a). The choice of the quadratures is relative to the phase reference. Choosing a phase reference different by an angle _✓_ so that the microwave signal has a phase _φ − ✓_ leads to the definition of new quadratures ( _X✓, Y✓_ ) related to ( _X, Y_ ) by: 



21 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 



<!-- Start of picture text -->
Y<br>Y<br>a b p 2 n th + 1<br>4<br>X<br>1/4<br>ϕ<br>X<br>c Y d<br>Y<br>Im( ↵ )<br>✓<br>X<br>1 1<br>N + M cos( ✓ ) + X<br>4 r 2<br>Re( ↵ )<br>|A|<br><!-- End of picture text -->

FIGURE 2.1: **Microwave field states phase-space representation** using the convention given in the text. **a** Classical picture. **b** Thermal (dashed) and vacuum (solid fill) states. **c** Squeezed state. **d** Coherent state (blue fill), coherent thermal state (dashed blue line), displaced squeezed state (red dashed line). 

In quantum physics, the field quantization is obtained by promoting the quadratures of the field ˆ ˆ as quantum operators obeying the commutation relation _X, Y_ = _i/_ 2. _X_<sup>ˆ</sup> and _Y_<sup>ˆ</sup> are canonically h i conjugate variables, and the commutation relation imposes the following Heisenberg uncertainty relation for any pure state _| i_ or statistical mixture of states described by a density matrix _⇢_ : _h_ ∆ _X_<sup>ˆ2</sup> _ih_ ∆ _Y_<sup>ˆ2</sup> _i ≥|h_ [ _X,_<sup>ˆ</sup> _Y_<sup>ˆ</sup> ] _i|_<sup>2</sup> _/_ 4, i.e. : 



where the notations _ho_ ˆ _i_ and _h_ ∆ˆ _o_<sup>2</sup> _i_ stand respectively for the operator expectation value Tr( _⇢o_ ˆ) and ˆ ˆ for its variance _ho_<sup>2</sup> _i −hoi_<sup>2</sup> . Therefore no field can have a perfectly well-defined value for either of its quadratures and these quantum fluctuations need to be taken into account in experiments that aim at reaching ultimate measurement sensitivity. 

The uncertainty on _X_<sup>ˆ</sup> and _Y_<sup>ˆ</sup> makes it impossible to have a point-like representation. Instead, one needs to use a quasi-probability distribution such as the Wigner function distribution [39]. In the following, we also represent states schematically by shading regions ( _X, Y_ ) such that _|X − X_ max _|_ 6 ~~q~~ _h_ ∆ _X_<sup>ˆ2</sup> _i/_ 2, and equivalently for _Y_ , with ( _X_ max _, Y_ max) being the position of the Wigner function maximum. The field can be equivalently described by the annihilation and creation operators ˆ _a_<sup>_†_</sup> and ˆ _a_ 



22 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

that obey the commutation relation [ˆ _a,_ ˆ _a_<sup>_†_</sup> ] = 1. 

We now briefly describe the field states used in this thesis, their representation and their noise properties. Note that we will restrict ourselves to the so-called Gaussian states, for which the statistical distribution of the quadratures is a Gaussian. As a result they are fully characterized by their mean value and variance, and we will now concentrate on these quantities. 

##### **Vacuum state** 

We first define the Fock states _|ni_ as eigenstates of the number operator ˆ _n_ = ˆ _a_<sup>_†_</sup> _a_ ˆ. The lowest-energystate _n_ = 0 is called the vacuum state. 



and thus reaches the minimal variance authorized by the Heisenberg uncertainty principle for a state verifying _h_ ∆ _X_<sup>ˆ2</sup> _i_ = _h_ ∆ _Y_<sup>ˆ2</sup> _i_ . In phase-space, using the Wigner function, the vacuum state is represented by a disk centered on (0 _,_ 0) of radius 1 _/_ 4 (see Fig. 2.1b). Its incompressible quantum fluctuations set a limit on the signal-to-noise ratio of many experiments and are known as the standard quantum limit. As will be explained in ch. 3, they also set the coupling strength between a TLS 

##### **Thermal state** 

We also need to describe electromagnetic modes that are in thermal equilibrium with a bath at temperature _T_ ; they are said to be "in a thermal state". Such a thermal state is a statistical mixture of Fock states _|ni_ with a Boltzmann distribution, and its mean-value and variance can be shown to be: 



where _n_ th is the mean thermal photon number occupying the field, which obeys: 



In phase-space, a thermal vacuum is represented by a disk centered on (0 _,_ 0) of radius<sup>_p_</sup> 2 _n_ th + 1 _/_ 4, as shown in Fig. 2.1b. In the high temperature limit _kBT ≫_ ~ _!_ , the thermal state fluctuations are simply given by _kBT/_ 2~ _!_ and thus depend linearly on _T_ (see Fig. 2.2). In the low temperature limit _kBT ⌧_ ~ _!_ , the field occupies mostly the _|_ 0 _i_ vacuum state and thus reaches the quantum limit with _h_ ∆ _X_<sup>ˆ2</sup> _i_ = 1 _/_ 4. 

##### **Squeezed states** 

In this thesis we also encounter squeezed states of the field. Compared to the thermal and vacuum states, they are non-isotropic with one quadrature _X✓_ having less fluctuations than the vacuum state, while its other quadrature _Y✓_ has increased fluctuations to fulfill Heisenberg uncertainty principle. 

23 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 



<!-- Start of picture text -->
2 kBT<br>2 !<br>3/2<br>1<br>1/2<br>1 quantum limit<br>4<br>0<br>0 0.2 0.4 0.6 0.8 1.0 1.2 1.4<br>Temperature (K)<br>i<br>2<br>ˆ X<br>∆<br>h<br><!-- End of picture text -->

FIGURE 2.2: **Thermal state fluctuations** as a function of temperature for a mode at frequency _!/_ 2 _⇡_ = 7 GHz. 

The usual definition of these states makes use of a squeezing parameter _⇣_ such that: 



Their phase-space representation is an ellipsoid centered on (0 _,_ 0) (see Fig. 2.1c) with a phasedependent radius _r_ ( _φ_ ) since: 



where _N_ and _M_ are defined as _N_ = cosh( _⇣_ ) _/_ 2 _−_ 1 _/_ 2 and _M_ = sinh( _⇣_ ) _/_ 2. A squeezed state has minimal uncertainty in the sense of Heisenberg inequality (see Eq. 2.3). Even though it is abusively called "squeezed vacuum", it is important to note that this state contains a finite number of photons since it can be shown that _ha_ ˆ<sup>_†_</sup> _a_ ˆ _i_ > _N_ . Moreover, the stronger the squeezing, the larger _N_ , and thus the larger the energy of the state. A state with an infinitely squeezed quadrature _X_<sup>ˆ</sup> would have infinite energy. Since one of its quadratures has less fluctuations than the standard quantum limit, squeezed states are very interesting for ultra-precise measurement and are a key resource in quantum metrology [40]. In ch. 9, we make use of them to perform magnetic resonance spectroscopy beyond the standard quantum limit. 

Squeezed thermal states also exist. Similarly than for a squeezed vacuum state, one of their quadrature has less fluctuations than a thermal state of thermal occupancy _n_ th while the other one has increased fluctuations. Eqs. 2.12-2.13 are modified as follows: 





24 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 



<!-- Start of picture text -->
a b<br>I(t)<br>C<br>V(t)<br>L<br><!-- End of picture text -->



FIGURE 2.3: **_LC_ oscillator. a** Schematic. **b** Example of implementation: a superconducting planar resonator comprising a interdigitated capacitance (orange) in parallel with a wire (inductance, blue). 

while _N_ and _M_ 



##### **Coherent states** 

Throughout this manuscript, the microwave signals that drive the spins are classical and can be described by coherent states. Coherent states _|↵i_ are eigenstates of the operator _a_ ˆ such that the number of photons contained in this state is _h↵ |_ ˆ _a_<sup>_†_</sup> _a_ ˆ _| ↵i_ = _|↵|_<sup>2</sup> . For _↵_ = 0, the coherent state is the vacuum state _|_ 0 _i_ . Coherent states are characterized by their mean value _hX_<sup>ˆ</sup> _i_ = Re( _↵_ ), _hY_<sup>ˆ</sup> _i_ = Im( _↵_ ), and their variances _h_ ∆ _X_<sup>ˆ2</sup> _i_ = 1 _/_ 4 and _h_ ∆ _Y_<sup>ˆ2</sup> _i_ = 1 _/_ 4 which are identical to those of the vacuum state. One can also have coherent thermal states whose fluctuations are then given by Eq. 2.9. 

After having introduced various quantum states, we now discuss physical implementations of the electromagnetic modes relevant for our work. 

#### **2.1.2 Lumped element LC resonator** 

The simplest implementation of an electromagnetic field mode is the lumped-element LC oscillator, which is also highly relevant for the rest of this work as will be clear in the following. A good review of the quantization of a simple _LC_ resonator is given in [41, 42]. Consider an oscillator comprising an inductor L in parallel with a capacitor C as schematized in Fig. 2.3a. We introduce the operator Φ<sup>ˆ</sup> , describing the magnetic flux in the inductor, and _q_ ˆ, describing the charge on the capacitor. Φ<sup>ˆ</sup> and _q_ ˆ obey the conjugation relation [ _φ,_<sup>ˆ</sup> ˆ _q_ ] = _i_ ~. The Hamiltonian of this harmonic oscillator is: 



which may also be written as: 



25 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

where ˆ _a_ and ˆ _a_<sup>_†_</sup> are linked to _φ_<sup>ˆ</sup> and _q_ ˆ by: 



with _!_ 0 = 1 _/pLC_ being the resonator frequency and _Z_ 0 = ~~p~~ _L/C_ the resonator impedance. The voltage _V_<sup>ˆ</sup> across the capacitor and the current _I_<sup>ˆ</sup> flowing through the inductor are thus expressed in terms of the bosonic operators as: 



The eigenstates of _H_<sup>ˆ</sup> are the Fock states _|ni_ and satisfy _H_<sup>ˆ</sup> _|ni_ = ~ _!_ 0 � _n_ +<sup><u>1</u></sup> 2 � _|ni_ . The rms vacuum fluctuations of the voltage and the current when the resonator field is in its quantum ground state are then: 





The rms voltage and rms current generate, respectively, a spatially dependent electric field **E**<sup>ˆ</sup> ( **r** ) = _i_ **_δE_** ( **r** ) (ˆ _a − a_ ˆ<sup>_†_</sup> ) in the space between the capacitor plates, and magnetic field **B**<sup>ˆ</sup> ( **r** ) = **_δB_** ( **r** ) (ˆ _a_ + _a_ ˆ<sup>_†_</sup> ) around the inductor, with **_δE_** ( **r** ) and **_δB_** ( **r** ) their vacuum rms fluctuations at position **_r_** . Throughout this thesis, the rms magnetic field vacuum fluctuations play an important role as they are proportional to the coupling constant between the spins and the resonator. An example of a _LC_ resonator used in later chapters is depicted in Fig. 2.3b. 

#### **2.1.3 Lossless transmission line** 



<!-- Start of picture text -->
dx<br>l dx dx I(t,x)<br>V(t,x) c dx dx<br><!-- End of picture text -->

FIGURE 2.4: **Transmission Line** . Each infinitesimal part of a transmission line can be modeled as a LC. 

A transmission line, for instance any coaxial cable, supports the propagation of electromagnetic modes. A good overview of the quantization procedure for a transmission line is given in [43]. The transmission line can be modeled as an assembly of elementary circuits, as shown in Fig. 2.4, where _l_ and _c_ are the inductance and capacitance per unit-length. To analyze this circuit, a local flux variable _t_ dependent on the position is defined as _φ_ ( _x, t_ ) = R _−1_<sup>_V_(</sup><sup>_x, ⌧_)</sup><sup>_d⌧_where</sup><sup>_V_(</sup><sup>_x, t_) is the local voltage</sup> 

26 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

on the transmission line at position _x_ and time _t_ . In each segment, the charge in the capacitor is given by _q_ ( _x, t_ ) = _cV_ ( _x, t_ ), the voltage drop across the inductance _l dx_ is _−dx @x@tφ_ ( _x, t_ ), yielding the flux through this inductance _−dx @xφ_ ( _x, t_ ) and the corresponding current _I_ ( _x, t_ ) = _−@xφ_ ( _x, t_ ) _/l_ . 

The Lagrangian for an infinite line is given by _L_ = R _dxLx_ , with the Lagrangian density _Lx_ being: 



The corresponding equation of motion for _φ_ is then given by the wave equation _lc @t_<sup>2</sup><sup>_φ −@_</sup> _x_<sup>2</sup><sup>_φ_= 0,</sup> with a propagation speed _vt_ = 1 _/plc_ . By differentiating with respect to the time, one finds a similar expression for _V_ ( _x, t_ ). Without any boundary conditions, the solutions of this equation may be expressed as a composition of right and left propagating waves: 



The solution for the current is related to _V_ by _l@tI_ = _−@xV_ , thus: 

where _Zc_ = ~~p~~ _l/c_ is the characteristic impedance of the line. The left and right propagating waves are independent for an infinite transmission line. If the line is terminated by a load _Zl_ at _x_ = 0, they are linked by the following equation of continuity for classical fields: 



The microwave power transmitted to the right is then given by: 



We now turn to the quantum description of propagating fields. From the Lagrangian density, one can extract the density Hamiltonian by noticing that the charge is the conjugate quantity of the flux: 



and thus _H_ = R _Hxdx_ , with: 



The field quantization is obtained by treating _φ_ and _q_ as quantum operators obeying: 



Using expressions 2.28 and 2.29, one can express _φ_<sup>ˆ</sup> and _q_ ˆ as a function of the voltage amplitude operators _V_<sup>ˆ</sup><sup>_*_</sup> ( _⌧_<sup>_−_</sup> ) and _V_<sup>ˆ</sup><sup>_)_</sup> ( _⌧_<sup>+</sup> ) where we set _⌧_<sup>_±_</sup> = _t ± vxt_<sup>.Usingthefactthatleftandright</sup> fields for an infinite transmission line are independent, one can derive from Eq. 2.34 the following 

27 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

commutation relation for _V_<sup>ˆ⌦</sup> ( _⌧_ ): 



To find the expression of the voltage as a function of annihilation and creation operators _a_ ˆ<sup>⌦</sup> ( _!_ ), Eq. 2.35 is expressed in the frequency domain, by defining: 



and thus: 



One can notice that while _V_<sup>ˆ⌦</sup> ( _⌧_ ) is hermitian, _V_<sup>ˆ⌦</sup> ( _!_ ) is non-hermitian with _V_<sup>ˆ⌦</sup> ( _!_ )<sup>_†_</sup> = _V_<sup>ˆ⌦</sup> ( _−!_ ). To have [ˆ _a_<sup>⌦</sup> ( _!_ ) _,_ ˆ _a_<sup>⌦</sup><sup>_†_</sup> ( _!_<sup>_0_</sup> )] = 2 _⇡δ_ ( _! − !_<sup>_0_</sup> ), we now define ˆ _a_<sup>⌦</sup> ( _!_ ) as: 



and thus one has by reverting to the time domain: 



where _h.c._ stands for hermitian conjugate. 

We are typically interested in a relatively narrow band of frequencies centered on _!a_ . In this case, it is useful to work in the time-domain in a frame rotating at _!a_ . Using Eq 2.40 and assuming that the only relevant frequencies are near _!a_ (performing the so-called rotating wave approximation), one _x_ = 0: 



where we have defined the annihilation and creation operators in the time domain to be: 



Instead of keeping the basis of "infinite-bandwidth" operators _a_ ˆ( _t_ ), the notations can be further simplified by introducing a new operator which defines propagating spatio-temporal modes of finite temporal and spectral extension. We write 



_u_ ( _t_ ) being the propagating signal mode temporal envelope, of bandwidth ∆ _!_ , normalized so that R [ _u_ ( _t_ )]<sup>2</sup> _dt_ = 1. With this definition, we define left and right modes ˆ _a_<sup>⌦</sup> which obey [ˆ _a_<sup>⌦</sup> _,_ ˆ _a_<sup>⌦</sup><sup>_†_</sup> ] = 1 and that are equivalent to the annihilation and creation operators used in 2.1.1. As a result, quantum microwave fields propagating along a transmission line can be described using the results of 2.1.1. 

28 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

#### **2.1.4 Probing and characterizing a resonator** 



<!-- Start of picture text -->
a<br>ain,1 C C ain,2<br>I1(t) C1 A C2 I2(t)<br>Z Z<br>C C<br>a  1  2 a<br>out,1 out,2<br>I<br>E1 V1(t) V2(t)<br>C<br>R int<br>L<br>b c<br>L Rext1 Rext2 ω�<br>C C C<br>c1 c2<br>R<br>�<br>� 2<br>1<br>�<br>int<br><!-- End of picture text -->



<!-- Start of picture text -->
�<br>2<br><!-- End of picture text -->

FIGURE 2.5: **Probing a LC resonator from the outside. a** When a _RLC_ circuit is coupled capacitively to measurement lines of characteristic impedance _Zc_ , the energy stored in the inductive and capacitive elements can leak out with rate __ int into the internal resistance, and with rate __ 1 and __ 2 into the measurement lines. A master equation established for the intra-resonator field ˆ _a_ (t) allows to link the input and output field operators via these dissipation rates in an input-output framework. **b** Norton equivalent circuit. **c** Quantum Optics equivalent representation. 

The _LC_ resonator used in our experiments is coupled to two transmission lines of characteristic impedances _Zc_ via two coupling capacitances _Cc_ 1 and _Cc_ 2, as shown in Fig. 2.5. We also introduce a resistance _R_ in the _LC_ to model the internal losses of the resonator. In this paragraph, we would like to provide a quantum description of the evolution of the intra-resonator field ˆ _a_ in response to external drives and internal losses. We first present a few results obtained by a classical description of the system to define a number of useful quantities. 

##### **Coupling to a measurement transmission line** 

As the _RLC_ circuit is coupled to input and output transmission lines, its frequency _!_ 0 and its characteristic impedance _Z_ 0 are slightly modified. Indeed, the admittance viewed from A (see 

29 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

Fig 2.5a) has two additional terms _Z_ ext _,i_ =1 _,_ 2 = _Zc_ + 1 _/iCCi!_ : 



In the limit _ZcCCi!_ 0 _⌧_ 1 and in the vicinity of _!_ 0, this corresponds to a _R_<sup>_0_</sup> _L_<sup>_0_</sup> _C_<sup>_0_</sup> circuit impedance (see Figure 2.5b), with _L_<sup>_0_</sup> = _L_ and: 



thus renormalizing slightly the resonator frequency in _!_ 0<sup>_0_= 1</sup><sup>_/_</sup> _p_ LC<sup>_<u>0</u>_</sup> and its characteristic impedance in _Z_ 0<sup>_0_=</sup> ~~p~~ _L/C_<sup>_0_</sup> . In the following, we take into account this renormalization but keep the notations _!_ 0 and _Z_ 0. In addition, three dissipation terms corresponding to internal losses or losses via coupling 



The dissipation terms set the damping of the resonator motion via its quality factor _Q_<sup>_−_1</sup> = _R_ ~~p~~ _L/C_ (for a parallel _RLC_ circuit), allowing us to identify three distinct contributions _Q_<sup>_−_1</sup> = _Q_<sup>_−_</sup> ext<sup>1</sup> _,_ 1<sup>+</sup> _Q_<sup>_−_</sup> ext<sup>1</sup> _,_ 2<sup>+</sup><sup>_Q−_</sup> int<sup>1givenrespectivelybytheinternallosses</sup><sup>_Q−_</sup> int<sup>1=</sup><sup>_R_</sup> ~~p~~ _L/C_<sup>_0_</sup> and the coupling to the transmission lines _Q_<sup>_−_</sup> ext<sup>1</sup> _,i_<sup>=</sup><sup>_R_ext</sup><sup>_,i_</sup> ~~p~~ _L/C_ . The energy damping rate into each “port”, either internal or external, is then defined as __ = _!_ 0 _/Q_ . 

This mapping is valid in the high-quality factor limit where _ZcCCi!_ 0 _⌧_ 1. One interpretation is that the coupling capacitances are acting as semi-reflecting mirrors: the strong impedance mismatch between the transmission line and the _LC_ oscillator ensures that the electromagnetic field is confined inside the resonator. 

##### **Input-output theory** 

When probing the resonator with classical microwave fields, the input and output resonator fields can be related using a scattering matrix approach [44]. Consider the two-port device comprising the coupling capacitances and the _RLC_ circuit, denoted by the grey box shown in Fig. 2.5, with each port directly connected to the left and right transmission lines. An ideal voltage source _E_ 1 with a matched output impedance connected to the left transmission line generates a voltage _V_ 1( _t_ ) and a current _I_ 1( _t_ ) on port 1 as well as a voltage _V_ 2( _t_ ) and a current _I_ 2( _t_ ) on port 2. As seen above, _V_ 1( _t_ ) can be separated in two contributions: a right propagating term incident on the device given by _V_ 1<sup>_*_(</sup><sup>_t_)=</sup><sup>_V_1(</sup><sup>_t_) +</sup><sup>_ZcI_1(</sup><sup>_t_) and a left propagating term outcoming of the device given by</sup> _V_ 1<sup>_)_(</sup><sup>_t_)=</sup><sup>_V_1(</sup><sup>_t_)</sup><sup>_−ZcI_1(</sup><sup>_t_), and similarly for</sup><sup>_V_2(</sup><sup>_t_).One can consider equivalently that the incident</sup> term _V_ 1<sup>_*_</sup> gives rise to a transmitted wave _V_ 2<sup>_*_</sup> in the right transmission line and a reflected term _V_ 1<sup>_)_</sup> in the left transmission line. The relation between the input and output power waves defined as _a_ in _,j_ = _Vj_<sup>_*/p_</sup> _Zc_ and _a_ out _,i_ = _Vi_<sup>_*/p_</sup> _Zc_ can be expressed by the scattering matrix coefficient _Sij_ : 



The device behavior is entirely characterized by knowledge of the S-matrix. This scattering matrix approach has been extended to a quantum-mechanical description of the device by Gardiner and 

30 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

Collett [45]. This theory describes the very general case of a system of Hamiltonian _H_<sup>ˆ</sup> coupled to different continuums of modes with coupling strengths _i_ . 

In our particular case, the system is the _LC_ resonator described by the intra-resonator field operator _a_ ˆ( _t_ ) introduced in Eq. 2.22 described in the Heisenberg picture. The two transmission lines provide two baths, described by the propagating operators ˆ _a_ in _,i_ =1 _,_ 2 introduced in Eq. 2.38. The coupling rates _i_ can be identified to the energy damping rates introduced above if one performs a Markovian approximation valid in the limit of coupling to a continuum of modes (see Figure 2.5c). In the treatment introduced by Gardiner and Collett, the evolution of ˆ _a_ ( _t_ ) is given by the following master equation (in the Heisenberg picture): 



ˆ ˆ where [ˆ _a, H_<sup>ˆ</sup> ] _/i_ ~ = _−i!_ 0 _a_ for a LC oscillator. The terms<sup>_p_</sup> _<u>i</u> a_<sup>_*_</sup> _i_<sup>(</sup><sup>_t_) are the source terms and the</sup> terms<sup><u>1</u></sup> 2<sup>(P</sup> _i_<sup>_i_+</sup><sup>__int) ˆ</sup><sup>_a_(</sup><sup>_t_) are the damping terms.The internal losses are associated to an additional</sup> port at thermal equilibrium. The classical continuity equation Eq. 2.30 translates into the important following relation between input and intra-resonator field: 



##### **External drive by coherent states** 

In our experiments, the resonators are driven by classical fields which can be described as coherent states _|↵_ in _,ii_ . The incident power on the resonator is thus given by _P_ = ~ _!|↵_ in _,i|_<sup>2</sup> . Under a classical drive _↵_ in _,i_ on port _i_ , the mean-value of the intra-resonator _ha_ ˆ _i_ ( _t_ ) = _↵_ ( _t_ ) is then given by Eq. 2.49: 



and thus by Fourier transform, one finds the steady state solution of _↵_ : 



At resonance, under a drive of power _Pi_ the intra-cavity photon number ¯ _n_ = _|↵|_<sup>2</sup> is: 



In the following chapters, we are also interested in the current flowing through the inductor and the associated generated magnetic field. Upon an incident resonant signal of power _P_ , they are given by: 



##### **Measurements** 

In ch. 5, the frequency and coupling rates of the resonator are determined experimentally by using a Vector Network Analyser (VNA). This apparatus measures the S-matrix components in transmission ( _S_ 21( _!_ ) and _S_ 12( _!_ )) and in reflexion ( _S_ 11( _!_ ) and _S_ 22( _!_ )). The power waves _a_ in _,i_ and 

31 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 



<!-- Start of picture text -->
a 1 b 1 c 1<br>2 p  1  2<br> 1  −  2  −  int<br> 1 +   2 +   int  1 +   2 +   int  2  −  1  −  int<br> 1 +   2 +   int<br>0 0 0<br>-10 10 -10 10 -10 10<br>(ω-ω0)/κ2 (ω-ω0)/κ2 (ω-ω0)/κ2<br>π π/2 π<br>-π-10 10 -π/2 -10 10 -π-10 10<br>(ω-ω0)/κ2 (ω-ω0)/κ2 (ω-ω0)/κ2<br>|11 |21 |22<br>|S |S |S<br>)11 )21 )22<br>arg(S arg(S arg(S<br><!-- End of picture text -->

FIGURE 2.6: **Transmission and reflexion measurements** evaluated for __ 1 = 0 _._ 2 __ 2 and three values of __ int: __ int + __ 1 = __ 2 (blue), __ int + __ 1 = 0 _._ 25 __ 2 (green), __ int + __ 1 = 10 __ 2 (red). **a, b and c** are respectively the modulus (top) and argument (bottom) of _S_ 11( _!_ ), _S_ 21( _!_ ) and _S_ 22( _!_ ) 

_a_ out _,i_ introduced earlier to define the S-parameters can be replaced by the coherent signals _↵_ in _,i_ and _↵_ out _,i_ . Eq. 2.50 yields the relation _↵_ in _,i_ ( _!_ ) + _↵_ out _,i_ ( _!_ ) =<sup>_p_</sup> _<u>i↵</u>_ ( _!_ ), and thus one can compute the dependencies of _Sij_ ( _!_ ) expected for a LC resonator coupled to two transmission lines: 

in transmission: 



Depending on the relative strength of the internal damping rate __ int compared to the external coupling rate _c_ = __ 1 + __ 2, it is interesting to distinguish three regimes, as illustrated on Fig. 2.6. In our experiment, the coupling to port 1 and 2 are asymmetric with __ 1 _⌧ _ 2. Seen from port 2, we thus have: 

- **The under-coupled regime, where** **__ int** **_≫ _ 2** **_, _ 1:** (green curves) In reflexion on both ports, only a small dip in amplitude is observed with a small phase shift in phase. The transmission peak width is essentially set by __ int. 

- **The critical coupling regime, where** **__ int +** **__ 1 =** **__ 2:** (blue curves). The reflexion on port 2 goes to 0 with a _⇡_ -shift discontinuity. The transmission reaches ~~p~~ __ 1 _/_ 2. The reflexion on port 1 is in the under-coupled regime. 

- **The over-coupled regime, where** **__ int +** **__ 1** **_⌧ _ 2:** (red curves) For both reflexion measurements only a slight dip in amplitude occurs, however the phase when reflecting on port 2 shifts by 2 _⇡_ while the shift on port 1 is less than _⇡_ . The transmission at resonance is close to 2 ~~p~~ __ 1 _/_ 2. 

32 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

In order to determine _!_ 0, __ 1, __ 2 and __ int experimentally on a two-port device with asymmetric couplings, the measurement of at least two elements of the scattering matrix among _S_ 11( _!_ ), _S_ 22( _!_ ) and _S_ 21( _!_ ) is required. However, measuring the transmission _S_ 21( _!_ ) generally only brings knowledge of the total damping rate __ since exploiting the peak height to obtain the quantity<sup>_p_</sup> _<u></u>_ 1 _<u></u>_ 2 requires prior precise calibration of the measurement lines. The best determination of the resonator parameters is thus obtained by measuring and fitting _S_ 11( _!_ ) and _S_ 22( _!_ ) because they are in a sense "self-calibrated" by the fact that _|S_ 11 _|_ = _|S_ 22 _|_ = 1 far from resonance. In the following, we also measure single-port resonators, which are treated with the same formulas as already presented, with __ 1 = 0. It should also be noted that the S-parameters measured by the VNA are defined as the conjugates quantities _Sij_ ( _!_ )<sup>_⇤_</sup> of what is derived here. 

### **2.2** 

Several orders of magnitude separate the small power of the quantum microwave signals that we wish to detect and the noise level of typical room-temperature measurement apparatus. It is thus essential to amplify the signals with as little noise as possible. Quantum mechanics imposes some constraints on the minimum amount of noise that an amplifier has to add to the signal, as shown by Haus and Mullen [46], and Caves [11]. While usual microwave amplifiers add in general much more noise, novel amplifiers developed for cQED research and called Josephson Parametric Amplifiers (JPA) do reach this quantum limit. In this section, we will give an overview of the theoretical aspects of quantum-limited amplification, and we will also expose the working principle of the flux-pumped JPA used in this work. 

#### **2.2.1** 

A signal of frequency _!_ and of bandwidth ∆ _!_ is emitted in a transmission line connected to a linear amplifier with power gain _G_ . The amplified signal then propagates via a second transmission line to either a homodyne detection yielding the _I_ and _Q_ quadratures of the microwave signal, or a frequency spectrum analyser. The signal being narrow-band, we can use the right-propagating spatio-temporal modes defined in 2.1.1 to describe the input and output signals ˆ _a_ in, ˆ _a_<sup>_†_</sup> in<sup>, ˆ</sup><sup>_a_out, ˆ</sup><sup>_a_</sup> out<sup>_†_,</sup> and their associated quadrature operators. 

The outcome of the measurement in the case of homodyne detection is directly linked to the quadrature operators. Indeed, the signal is mixed with a strong microwave tone at frequency _!_ and phase _✓_ . By filtering the two output voltages using a low-pass filter (typically smaller than 2 _⇡/_ ∆ _!_ ), one gets outcomes proportional to _X_<sup>ˆ</sup> out _,✓_ and _Y_<sup>ˆ</sup> out _,✓_ . For one quadrature, the averaged signal is proportional to _hX_<sup>ˆ</sup> out _,✓i_ and the variance to _h_ ∆ _X_<sup>ˆ</sup> out<sup>2</sup> _,✓_<sup>_i_.When measuring the signal with a</sup> spectrum analyser, set with a resolution bandwidth suited to the signal, the noise power detected in the absence of signal is simply _hX_<sup>ˆ</sup> out<sup>2</sup> _,✓_<sup>_i_+</sup><sup>_h_ˆ</sup><sup>_Y_</sup> out<sup>2</sup> _,✓_<sup>_i_.In the remainder of the chapter, we consider only</sup> the quadratures _X_<sup>ˆ</sup> and _Y_<sup>ˆ</sup> related to _X_<sup>ˆ</sup> _✓_ and _Y_<sup>ˆ</sup> _✓_ by Eq. 2.2. We now derive the input-output relations for linear amplifiers as well as their noise properties using these operators. 

It is tempting to relate the output and input quadratures of a linear amplifier by defining _X_<sup>ˆ</sup> out = _pGX X_<sup>ˆ</sup> in and _Y_<sup>ˆ</sup> out =<sup>_p_</sup> _GY Y_<sup>ˆ</sup> in. This definition is however incompatible with the commutation relations for ˆ _a_ out and ˆ _a_ in, except if<sup>_p_</sup> _GX GY_ = 1. Following Caves [11], two types of amplifiers are usually distinguished. 

33 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 



<!-- Start of picture text -->
a<br>ain G, TN aout X, Y<br>signal<br>bin<br>b Phase-preserving amplification c Phase-sensitive amplification<br>Y Y<br>p G Yin pG ∆ Xin 2 + 1 4<br>Yin ∆ Xin 2 2 p 1 G ∆ Yin 2<br>2 p 1 G Yin 2 pG ∆ Xin 2<br>Xin p G Xin X 2 p G Xin X<br><!-- End of picture text -->

FIGURE 2.7: **Linear amplifiers. a** A linear amplifier of gain G and noise temperature _TN_ is used to detect a narrow-band signal. **b-c** Phase-preserving and phase-sensitive amplification in phase-plane representation in the limit of high gain. The disks indicate the contour of the Wigner function. A phase preserving amplifier degrades the SNR, with the added noise represented in red. In phase-sensitive amplification, one quadrature is amplified at the expense of the other, but one can evade the noise added by the Heisenberg uncertainty principle. 

###### 

Phase-preserving amplifiers have identical gain on both quadratures _GX_ = _GY_ = _G_ . According to the above discussion, one needs to introduce a mode<sup>ˆ</sup> _b_ in internal to the amplifier that commutes with ˆ _a_ in to describe the amplification: 







which are the expected relations for the amplified signal. 

###### 

A phase-sensitive device amplifies one quadrature at the expense of the other. We consider here only amplifiers for which _Gs_ = _GX_ = 1 _/GY_ , so that the condition<sup>_p_</sup> _GX GY_ = 1 is satisfied. In that case, the input and output quadratures are linked by: 



34 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

Interestingly, the phase-sensitive amplifier is just a particular case of the phase-preserving amplifier. Writing ˆ _a_ out =<sup>_p_</sup> _GsX_<sup>ˆ</sup> in + _i_ _~~p~~_ <u>1</u> _Gs_<sup>_Y_ˆin yields Eq. 2.58 by choosing ˆ</sup><sup>_b_in= ˆ</sup><sup>_a_in and</sup><sup>_p_</sup> _Gs_ = _pG_ + _pG −_ 1. At large gains, one can identify<sup>_p_</sup> _Gs_ = 2 _pG_ . 

#### **2.2.2** 

###### 

For a phase-preserving amplifier, one can derive from the input-output equations (Eq. 2.58) that the outcoming noise referred to the input in the absence of a signal is: 



where _hX_<sup>ˆ</sup> _b_<sup>2</sup><sup>_i_are the internal mode fluctuations.We thus arrive to the important conclusion that the</sup> output noise is the sum of two contributions : the input noise and the noise added by the amplifier given by the internal mode fluctuations. We note _n_ = _hX_<sup>ˆ</sup> out<sup>2</sup><sup>_i/G_thenoisedetectedonasingle</sup> quadrature and _n_ eq = _h_ ∆ _X_<sup>ˆ</sup> in<sup>2</sup><sup>_i_and</sup><sup>_n_amp=</sup><sup>_h_∆ˆ</sup><sup>_X_</sup> b<sup>2</sup><sup>_i_its two contributions so that</sup><sup>_n_=</sup><sup>_n_eq +</sup><sup>_n_amp.</sup> For an incoming field in a thermal equilibrium state, the input noise _n_ eq is given by Eq. 2.10. The vacuum state with fluctuations equaling the Heisenberg uncertainty relation _n_ eq =<sup><u>1</u></sup> 4<sup>is reached for</sup> temperatures _kBT ⌧_ ~ _!_ . While operating in this limit, the detected noise is purely of quantum origin due to the incompressible fluctuations of the field, in opposition to being set by thermal 

The amplifier added noise is also bound by the Heisenberg uncertainty principle since _hX_<sup>ˆ</sup> _b_<sup>2</sup><sup>_ih_ˆ</sup><sup>_Y_</sup> _b_<sup>2</sup><sup>_i_></sup> 161<sup>.Imposing that the added noise is phase-insensitive for a phase-preserving amplifier</sup><sup>_h_ˆ</sup><sup>_X_</sup> _b_<sup>2</sup><sup>_i_=</sup> _hX_<sup>ˆ</sup> _b_<sup>2</sup><sup>_i_> 1</sup><sup>_/_4 [11], the quantum limit on amplifier-added noise is:</sup> 



showing that a phase-preserving amplifier adds at best the equivalent of half a photon ( _n_ amp > 1 _/_ 4) of noise at the input in the case of large gains, as stated by Haus-Caves theorem. In terms of amplifier noise temperature, this limit can be re-written as: 



###### 

A phase-sensitive amplifier can escape the quantum-limit on amplification since according to Eq. 2.62: 



The price to pay for this noiseless amplification is that we access only one quadrature of the field. This does not necessarily constitute an issue if the output signal phase is constant and known, which 

35 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

is precisely the case for spin-echoes<sup>1</sup> . When one performs a noiseless amplification without thermal population in the incoming waveguide, the measurement reaches the standard quantum limit with _h_ ∆ _X_<sup>ˆ</sup> out<sup>2</sup><sup>_i/Gs_= 1</sup><sup>_/_4.</sup> 

Note that in the absence of a signal, the de-amplified quadrature has less fluctuations than the input state: 



creating a squeezed-state of squeezing parameter _e_<sup>_⇣_</sup> = _Gs_ . In ch. 9, we use a JPA to generate a squeezed state and detect a signal below the standard quantum limit. 

#### **2.2.3** 

In the last decade, various designs for an amplifier operating at the quantum limit have been developed [47, 48, 49, 50, 51, 52, 53, 54]. These designs are based on Josephson junctions embedded in superconducting resonators following pioneering work by Yurke et al. [12]. These elements enable parametric amplification of a signal at frequency _!s ⇡ !_ 0 by transfer of energy from a pump at frequency _!p_ to the signal and to a complementary idler of frequency _!I_ . In the device used in this thesis, the tunability of a variant of the Josephson junction, the SQUID (Superconducting Quantum Interference Device), is used to modulate the resonator frequency at _!p ⇡_ 2 _!_ 0 and create a three-wave mixing process with _!p_ = _!s_ + _!I_ [51, 52, 53, 54]. Due to the use of dissipationless elements these amplifiers can add the minimum amount of noise allowed quantum mechanically when operated in phase-preserving mode ( _!s_ = _!I_ ) and no noise in the amplified quadrature for phase-sensitive amplification ( _!s_ = _!I_ ). In this paragraph, we only intend to give an overview of the device operating principle. We refer the reader to [54, 55, 56] for more details and rigorous demonstrations. 

##### **The SQUID** 



<!-- Start of picture text -->
a b<br>I(t)<br>I(t)<br>�� superconductor<br>2e insulating barrier Ic V(t) �� �2 V(t)<br>�2 superconductor �<br><!-- End of picture text -->

FIGURE 2.8: **Josephson junction and its tunable equivalent: a SQUID. a** A Josephson junction is composed of an insulating barrier between two superconducting electrodes. The Josephson relations describing the current and voltage for this element give rise to a non-linearity. **b** When two Josephson junctions are inserted in a loop, they form a Josephson junction of characteristics tunable by the amount of flux threaded through the loop. 

A Josephson junction is made out of two superconducting electrodes separated by a thin insulating barrier (see Figure 2.8). On each superconducting electrode, the electrons form a Cooper pairs condensate described by a macroscopic quantum mechanical wavefunction of phase _'_ . Due to the small thickness of the barrier, the wavefunctions of each condensate overlap allowing for the 

> 1Indeed, for TLS, the phase of the spin-echo is set by the phases chosen for the drive pulses. For multi-level systems however, the spin-echo phase may vary and this variation can be of interest. Retaining the phase information in such cases prevents the use of phase-sensitive amplifiers. 

36 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

tunneling of Cooper pairs. The Josephson relations describing the current _IJ_ of Cooper pairs across the junction are [57]: 



where _δ_ = _'_ 2 _− '_ 1 is the phase difference across the junction, _Ic_ is the junction critical current, _'_ 0 = ~ _/_ 2 _e_ is called the reduced superconducting flux quantum, and _V_ is the voltage across the junction. From Eqs. 2.68 & 2.69, one gets: 



A Josephson junction thus behaves as a non-linear inductance _LJ_ ( _IJ_ ) with 



When two Josephson junctions are connected in a superconducting loop, as shown in Fig. 2.8b, they form a SQUID[58]. The total current _I_ through the SQUID is the sum of each branch current. In the case of two junctions with identical critical current _Ic_ , the current is expressed as: 



where _δ_ 1 _,_ 2 are the phase differences across each junction. Due to the flux quantization in the superconducting SQUID loop, the phases _δ_ 1 _,_ 2 are linked to the total magnetic flux Φtot threading the SQUID by: 



in which Φ0 = 2 _⇡'_ 0. Φtot is the sum of the applied flux Φ and the flux generated by the circulating current in the SQUID loop. The latter can be neglected for small SQUID loops, which we assume to be the case in the following. The total current can then be expressed as: 



with _δ_ = ( _δ_ 2 + _δ_ 1) _/_ 2. Thus a symmetric SQUID can be seen as a Josephson junction whose supercurrent is flux-tunable, with _Ic_<sup>_S_(Φ) = 2</sup><sup>_Ic_cos</sup> ⇣ _⇡_ Φ<sup><u>Φ</u></sup> 0 ⌘. The SQUID is thus a tunable inductance: 



When the current _I_ approaches the SQUID critical current _Ic_<sup>_S_(Φ) however the non-linearity of the</sup> SQUID Josephson junctions plays a role, as we will see in the following. 

###### 

The tunability of the SQUID inductance is exploited to provide parametric amplification. Consider a resonator with the geometry shown in Fig. 2.9a: a capacitance _Cg_ in parallel with an inductance _Lg_ and an array of _N_ symmetric SQUID loops, probed via a transmission line of characteristic impedance _Zc_ coupled by a capacitance _Cc_ to the resonator. As illustrated in Fig. 2.9a, the resonator 

37 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 



<!-- Start of picture text -->
a b 8<br>� + �<br>L DC AC<br>ain Cc g LJ( � ) flux pump  7<br>Z<br>C C<br>g<br>out aout � 6-0.5 0 0.5<br>�/�<br>d 0<br>10<br>c ω p/2 pump ω p |BY | 5<br>signal ω� idler 0<br>ω s ω i<br>− 5<br>ω − 10<br>filter − 20 − 10 0 10 X/|B| 20<br>in  (GHz)<br>π<br>)/2<br>( �ω 0<br><!-- End of picture text -->

FIGURE 2.9: **Flux-pumped Josephson Parametric Amplifier. a** The JPA comprises a geometrical inductance and capacitance in parallel with an array of SQUIDs, it is probed in reflexion via a transmission line capacitively coupled. **b** Modulation of the frequency of the resonator as a function of the SQUIDs DC flux bias. **c** Phase-preserving amplification operation of the JPA: a pump applied at _!p ⇡_ 2 _!_ 0 amplifies the signal and generates an idler signal. The idler signal can be removed by filtering. **d** Evidence of the phase kick on the intra-cavity field induced by the non-linearity of the SQUID, extracted from [55]. 

is probed in reflexion: a circulator is needed to route the input signal to the resonator, and the output signal towards the output line. 

Using the results we derived in section 2.1.4, the resonator frequency is: 



Denoting _p_ = _NLJ /_ ( _Lg_ + _NLJ_ ) the participation ratio of the Josephson inductance to the total inductance, the Taylor expansion to the second-order in _⇡_ Φ<sup><u>Φ</u></sup> 0<sup>of the resonator frequency yields:</sup> 



The tunability of _!_ 0 with respect to Φ is obtained by placing a flux line nearby the SQUIDs array (see Figure 2.9a). For a resonator of bare frequency _!_ 0(0) _/_ 2 _⇡_ = 8 GHz and characteristic impedance _Z_ 0 = 100 ⌦, the frequency tunability ranges over several hundreds of megaHertz as shown in Fig. 2.9b. 

According to Landau [59], modulating at a frequency close to 2 _!_ 0 the resonator frequency gives rise to the phenomenon of parametric amplification. The amplifier thus consists in a tunable resonator _!_ 0(Φ _DC_ ), a pump signal sent through the flux-line at frequency _!p ⇡_ 2 _!_ 0, and an input port through which a signal at a frequency _! ⇡ !_ 0 is sent, with the reflected signal being amplified. 

The JPA being composed of entirely dissipation-less elements and based on the simple parametric amplification process, it reaches the quantum limit of amplifier-added noise discussed earlier. More precisely, it can be used in either of the two modes of operation: 

- **Non degenerate operation (** **_!p_ = 2** **_!s_ ):** 

In this case, gain at the idler **_!I_ =** **_!p − !s_** and the signal frequencies appear (see Figure 2.9c). The power gain _G_ achieved on the signal by this process increases as a function of the pump 

38 

_Chapter 2._ _<u>Quantum circuits and quantum noise</u>_ 

amplitude until it exceeds the damping occurring via the transmission line and enters an auto-oscillation regime. Below this threshold, this system behaves as a phase-preserving amplifier. As explained earlier, it amplifies each quadrature with half a photon of noise added. In practice, in order to amplify a signal at _!s_ , a narrow-band filter is used to get rid of the idler contribution (see Fig. 2.9). 

- **Degenerate operation (** **_!p_ = 2** **_!s_ ):** 

In this case interferences between the idler mode and the input signal leads to a phase sensitive amplification depending on the relative phase between the signal and the pump ∆ _φ_ : 



As discussed earlier, this degenerate amplifier does not add noise to the incoming signal and amplifies noiselessly one of its quadratures. As a consequence, this device can also be used to generate a squeezed vacuum state, as shown in ch. 9. A strong advantage of this device compared to other designs is that the pump line is physically isolated from the input and output line preventing any leakage of the strong pump tone and thus it can avoid spoiling the produced squeezed vacuum state as well as saturating the next amplification stage. 

##### **Limitations** 

The limitations of this JPA design arise from the non-linearity of the Josephson junction [55, 54]. When the incoming signal amplitude increases, the AC currents flowing through the SQUIDs also increase and eventually approach the SQUID critical current; the resulting Kerr effect leads to a further shift of the resonator frequency which perturbs the parametric amplification process. As a result, the phase response is distorted (see Fig. 2.9d), and the amplifier saturates. In our device, this occurs even for input signal powers as low as -130 dBm. Compared to noisier amplification schemes, all parametric amplifiers also suffer from a limited bandwidth. A strong effort is currently made to circumvent these limitations by exploring different designs and pumping schemes [52, 60]. 

While the device presented here only provides a gain above 25 dB in a bandwidth limited to a few megaHertz with an operating frequency tunable over several hundreds of megaHertz, it is particularly suited for the amplification of weak and narrow-band signals, such as a narrow-line ESR signal. We refer the reader to ch. 5 for a complete characterization of the device used in our experiment. 

39 

## **Chapter 3** 

# **Spins in a cavity** 

In this chapter, we model the behavior and dynamics of an ensemble of spins coupled to one mode of an electromagnetic resonator, such as a _LC_ circuit for instance. We first give a brief account of the spin dynamics in a classical drive field, as can be found for instance in magnetic resonance textbooks. We then attempt to treat the same problem quantum-mechanically: first in the case where only one spin is coupled to a cavity, then for a spin ensemble. The quantum treatment allows us in particular to derive the cavity-induced spin relaxation rate which is the subject of ch. 8. 

We restrict our study in this chapter to electronic spins 1 _/_ 2. Our discussion can be trivially extended to nuclear spins 1/2; for multilevel systems, our treatment applies to a two-level restriction of the full energy spectrum. 

### **3.1** 

#### **3.1.1 Coherent spin evolution** 

Consider an electronic spin 1 _/_ 2, submitted to a classical magnetic field **_B_** ( _t_ ). The two systems ˆ ˆ interact via the Hamiltonian _H_<sup>ˆ</sup> = _−_ **_µ_** _·_ **_B_** ( _t_ ), which involves the spin magnetic dipole **_µ_** = _−γe_ ~ **_S_**<sup>ˆ</sup> . Here _γe_ = 28 GHz/T is the so-called gyromagnetic ratio, and **_S_**<sup>ˆ</sup> = ( _S_<sup>ˆ</sup> _x, S_<sup>ˆ</sup> _y, S_<sup>ˆ</sup> _z_ ) is the dimensionless vectorial spin operator whose components obey the commutation relations [ _S_<sup>ˆ</sup> _i, S_<sup>ˆ</sup> _j_ ] = _i✏ijkS_<sup>ˆ</sup> _k_ . Using the Ehrenfest theorem one readily derives the equation of motion of the expectation value of the ˆ magnetic moment **_µ_** = _h_ **_µ_** _i_ : 



For an ensemble of _N_ spins in a volume _V_ , each magnetic moment **_µ_** _i_ adds up to a macroscopic magnetic moment<sup>P</sup> _i_<sup>**_µ_**</sup><sup>_i_.The detectable quantity is then the macroscopic magnetization per unit</sup> volume defined by the vector: 



that obeys: 



The coherent dynamics of the magnetization vector **_M_** thus exclusively consist of rotations around _B_ ( _t_ ); note in particular that the vector length does not change in this process. As a result, a good representation for the magnetization vector evolution is given by the Bloch sphere: the end point of the magnetization vector stays on a sphere of radius _M_ . 

40 

_Chapter 3. Spins in a cavity_ 



<!-- Start of picture text -->
a b c<br>e e e<br>B z B z B z<br>0 0 0<br>M<br>~e<br>B y<br>1 B ~<br>e e 1 e<br>y e x ω t y y<br>e x e ~ x e~ x<br>π/2<br>M<br><!-- End of picture text -->

FIGURE 3.1: **Spin dynamics. a** Under a static magnetic field **_B_** 0, the magnetization vector **_M_** precesses at frequency _!_ 0 in the laboratory frame. **b** Rotating frame of an oscillating magnetic field **_B_** 1. **c** In this rotating frame, applying a short microwave pulse allows to rotate the magnetization vector. 

˙ When a static field **_B_** 0 = _B_ 0 **_e_** _z_ is applied, the equation reduces to **_M_** = _−!s_ **_M_** _⇥_ **_e_** _z_ with _!s_ = _γeB_ 0. The magnetization vector precesses around **_B_** 0 at frequency _!s_ , the so-called Larmor frequency (see Figure 3.1a). 

Consider next the application of an oscillating microwave field **_B_** 1( _t_ ) = 2 cos( _!t_ ) _B_ 1 **_e_** _x_ orthogonal to **_B_** 0. In the frame rotating at _!_ around **_e_** _z_ , **_B_** 1( _t_ ) is expressed as a time-independent component ˜ **_B_** 1 = _B_ 1 **_e_** _x_ if one neglects the fast-rotating terms in 2 _!_<sup>1</sup> (see Fig. 3.1b). In the rotating frame (˜ **_e_** _x,_ ˜ **_e_** _y,_ **_e_** _z_ ), the equation of motion is: 





where ∆ _s_ = _! − !s_ and _!_ 1 = _γeB_ 1. A convenient representation for the magnetization vector in this frame is given by the Bloch sphere. Under this drive, the magnetization vector **_M_** rotates around the vector _!_ 1 **_e_** ˜ _x_ + ∆ _s_ **_e_** _z_ at an angular speed called the Rabi frequency: 



In the particular case of a resonant microwave excitation ∆ _s_ = 0, the magnetization vector precesses at speed _!_ 1 around **_B_**<sup>˜</sup> 1. Thus, a microwave pulse applied for a duration _⌧p_ rotates the Bloch vector by an angle _!_ 1 _⌧p_ around the axis set by **_B_**<sup>˜</sup> 1 (see Figure 3.1c). In the following, we use mainly _⇡/_ 2 and _⇡_ pulses of fixed lengths and adjust the drive power _!_ 1 to perform the desired rotations. The rotation axis is chosen by setting the phase of the microwave pulse: a microwave field with phase _χ_ , **_B_** 1( _t_ ) = 2 cos( _!t_ + _χ_ ) **_B_** 1 becomes˜ **_B_** ˜<sup>˜</sup> 1 = _B_ 1 cos( _χ_ )˜ **_e_** _x_ + _B_ 1 sin( _χ_ )˜ **_e_** _y_ ( _r_ ) in the rotating frame and thus any rotation axis within the _x − y_ plane can be chosen. Rotation around **_e_** _z_ can be performed ˜ ˜ by decomposing the motion in two rotations in the _x − y_ plane. Such a control allows to bring the magnetization vector to every point of the Bloch sphere. 

> 1This approximation is valid when the AC magnetic field acts just as a perturbation of the static field: _B_ 1 _⌧ B_ 0. This condition is always fulfilled in our experiments and we restrict our study to this regime. For an extended derivation, see [5]. 

41 

_Chapter 3. Spins in a cavity_ 



<!-- Start of picture text -->
e e<br>a B 0 z b B 0 z<br>M<br>~e ~e<br>y y<br>~e e~<br>x x<br>M<br><!-- End of picture text -->

FIGURE 3.2: _T_ 2 **and** _T_ 1 **processes** . **a** A _T_ 2 process describes the decoherence of the spin and leads to a fan-out of the spin transverse magnetization. **b** A _T_ 1 process describes the longitudinal relaxation of the spin ensemble back to its thermal equilibrium. 

#### **3.1.2 Relaxation and decoherence** 

In addition to the coherent dynamics induced by microwave drives, the magnetization relaxes due to its interaction with the environment. We will here only provide a phenomenological description of these incoherent processes. More details will be given in ch. 4 for the specific case of Si:Bi spins. Two different relaxation processes can be distinguished: 

- **Spin relaxation** describes the loss of energy by the spin ensemble and the decay of its longitudinal magnetization _Mz_ back to its equilibrium state _M_ th, which is also the initial condition of the Bloch equations. At finite temperature, the equilibrium is a statistical mixture of excited and ground populations given by Boltzmann statistics. The overall equilibrium magnetization is _M_ th = _pM_ 0, where _p_ is the polarization and _M_ 0 = _N_ **_µ_** is the maximum spin polarization. For an ensemble of spins-1/2 at temperature _T_ , the polarization is given by the Curie law: _p_ = tanh(~ _!s/kBT_ ). Energy relaxation consists in a progressive damping of the longitudinal magnetization _Mz_ towards _M_ th, in a characteristic time _T_ 1 which is called the spin relaxation time. 

- **Spin decoherence:** the relaxation of the transverse magnetization components _Mx_ and _My_ is usually governed by completely different processes, and occurs on a time scale _T_ 2 generally much shorter than its maximum value 2 _T_ 1. 

Longitudinal and transverse relaxation are included in Eq. 3.5 & 3.6 in the following way: 





42 

_Chapter 3. Spins in a cavity_ 



<!-- Start of picture text -->
L I(t)<br>N spins<br>Detection<br>Excitation<br>R C<br>B0 B1<br><!-- End of picture text -->

FIGURE 3.3: **ESR scheme** . A sample containing _N_ spins is embedded inside a resonant structure. A static magnetic field **_B_** 0 is applied to match the spin Larmor frequency to the _RLC_ circuit. The inductive element _L_ is used to apply magnetic microwave pulses **_B_** 1 to excite the spins as well as to detect the transverse magnetization. 

This set of equations is known as the Bloch equations. The steady-state _M_<sup>(s)</sup> reached under a coherent drive in the drive rotating frame is thus: 





For increasing drive powers, the transverse magnetization components _M_<sup>˜</sup> _x_<sup>(</sup><sup>_s_)</sup> and _M_<sup>˜</sup> _y_<sup>(</sup><sup>_s_)</sup> on resonance (∆ _s_ = 0) reach a maximum when _T_ 1 _T_ 2 _!_ 1<sup>2=1beforetheoverallmagnetizationvanishesfor</sup> saturating drive powers _!_ 1 _≫_ 1 _/T_ 1 _T_ 2. When saturation is reached, the two spin-levels are equally populated and essentially no longer interact with microwave fields. 

##### **Inhomogeneous and homogeneous broadening** 

Due to _T_ 2 relaxation processes, the spin resonance acquires a linewidth 1 _/T_ 2. In addition to this "homogeneous" broadening, the linewidth of a large ensemble of spins can also have an "inhomogeneous" distribution that arises from the difference in local environments of each spin, causing their Larmor frequency to have a distribution _⇢_ ( _!s_ ). 

An inhomogeneously broadened ensemble can be seen as a collection of homogeneously-broadenend subsets, each described by the Bloch equations. Summing all inhomogeneously broadened contributions results in a decay of _Mx,y_ at a rate 1 _/T_ 2<sup>_⇤_, with 1</sup><sup>_/T ⇤_</sup> 2<sup>= ∆</sup><sup>_!_being the width of</sup><sup>_⇢_(</sup><sup>_!s_), which can</sup> be much larger than 1 _/T_ 2. 

#### **3.1.3 Inductive detection of magnetic resonance** 

Consider now the setup depicted in Fig. 3.3. The ensemble of spins is now embedded in a _LC_ circuit of frequency _!_ 0 which generates the oscillating field **_B_** 1( _!_ ) at the spins location orthogonally to the static magnetic field **_B_** 0. _B_ 0 is chosen so that the spins Larmor frequency match the LC circuit frequency: _!s ⇡ !_ 0. The transverse components _Mx_ and _My_ expressed in the laboratory frame are related to _M_<sup>˜</sup> _x_ and _M_<sup>˜</sup> _y_ by: 



43 

_Chapter 3. Spins in a cavity_ 

This precessing transverse magnetization gives rise to an induced electromotive force and hence to an AC current flowing in the resonant detection circuit: 



which allows spin detection. This "inductive detection" is the most widely used magnetic resonance measurement method [4]. While the precise link between the measured current and the transverse magnetization depends on the circuit geometry, the current is proportional to the filling factor of the circuit, defined as: 



where _f_ ( **_r_** ) = _B_ 1( **_r_** ) _/_ max[ _B_ 1( **_r_** )]. As the transverse magnetization cannot be larger than _M_ th, the maximum current _Im_ that can be measured is _Im / ⌘pM_ 0. 

The transverse magnetization can result from either a continuous or a pulsed excitation. In the case of a continuous drive, the real and imaginary parts of the transverse magnetization induce a phase shift and/or absorption of the incoming microwave signal, which can be detected by lockin techniques. A transient transverse magnetization can also be induced by more or less complex pulse sequences. We focus on the latter technique, pulsed ESR, in the rest of the thesis. 

##### **Free induction decay** 

Starting from equilibrium, applying a microwave pulse of tipping angle _✓_ = _⇡/_ 2 brings the equilib˜ rium magnetization **_M_** th to the equator of the Bloch sphere, **_M_** = _M_ th **_e_** _y_ . Subsequently to the pulse, the magnetization vector precesses at frequency _!s_ around **_e_** _z_ with its transverse and longitudinal component being damped respectively at rate _T_ 2<sup>_⇤_and</sup><sup>_T_1for an inhomogeneous ensemble (Eqs. 3.9-</sup> 3.10, see Fig. 3.4). This oscillating magnetization induces a decaying rf current in the inductor called the free-induction decay (FID) signal: 



##### **Spin-echo** 

Inhomogeneous broadening can be counteracted by a pulse sequence known as the Hahn echo [61] which will be used extensively throughout this thesis. The principle of a Hahn echo is shown in Fig. 3.4. A first _⇡/_ 2 pulse is applied to the spins along the _x_ axis; the transverse magnetization along _y_ generated by this pulse decays in a characteristic time _T_ 2<sup>_⇤_, due to inhomogeneous broadening.</sup> After a delay _⌧ ≫ T_ 2<sup>_⇤_, a</sup><sup>_⇡_pulse is applied along the</sup><sup>_y_axis.Its action is equivalent to a time reversal</sup> for the spins [61]: as a result, after another waiting time _⌧_ , the transverse magnetization comes back to its initial value. This generates a signal in the detection circuit known as "spin-echo". Like the FID, the echo amplitude is proportional to _⌘pM_ 0. The echo signal itself decays with time constant _T_ 2 as a function of time 2 _⌧_ , due to spin decoherence, as already explained. 

The spin-echo technique, in opposition to the FID detection, has for advantage that the signal is not emitted next to a microwave pulse whose strength may prevent the detection of the echo. 

### **3.2** 

After having introduced basic ESR concepts in the previous section, we now turn to the quantummechanical description of the spin-resonator interaction. Consider the system depicted in Fig. 3.5 

44 

_Chapter 3. Spins in a cavity_ 



<!-- Start of picture text -->
π/2 π<br>x y echo<br>Resonator � �<br>current<br>T *<br>2<br>time<br>ez<br>FID<br>+M<br>th<br>e<br>y<br>ex<br>time<br>-M<br>th<br>ez ez ez ez ez<br>~ ~ ~ ~<br>e e ~ e e<br>y y e y y<br>~ ex ~ ex e ~ x y ~ ex ~ ex<br>z<br>M<br>,<br>~ My<br>,<br>x<br>~ M<br><!-- End of picture text -->

FIGURE 3.4: **Free induction decay and echo** . Starting from equilibrium, a _⇡/_ 2 pulse around **_e_** ˜ _x_ brings the magnetization vector to the equator of the Bloch sphere. Afterwards, in the laboratory frame the transverse magnetization precesses around **_B_** 0 while in the drive rotating frame it vanishes in a time _T_ 2<sup>_⇤_</sup> due to inhomogeneous broadening. A _⇡_ pulse around the _y_ ˜-axis applied after a delay _⌧_ refocusses the magnetization at time 2 _⌧_ , giving rise to an echo. Top-middle graphs: The black lines sketch the control pulses while the colored lines represent the induced current in the resonator as well as the evolution of the magnetization components (extracted from numerical simulations for typical ESR parameters). The Bloch spheres illustrate the sequence at times indicated by dot-dashed grey lines 

withˆ _N_ spinsˆ ˆ embedded into a resonator. As seen in 2.1.2, the _LC_ resonator Hamiltonian is _Hc_ = ~ _!_ 0 � _a_<sup>_†_</sup> _a_ +<sup><u>1</u></sup> 2 �. Its total damping rate __ = __ int + _c_ consists of internal losses and coupling to the measurement line, with _c_ = __ 1 + __ 2 the sum of the coupling rates to input and output ports. The circuit inductance, through which flows a current _I_<sup>ˆ</sup> = _δI_ (ˆ _a_ + ˆ _a_<sup>_†_</sup> ), generates an oscillating magnetic field **_B_**<sup>ˆ</sup> 1( **_r_** ) = **_δB_** ( **_r_** )(ˆ _a_ + ˆ _a_<sup>_†_</sup> ) at the spin location. 

#### **3.2.1 One spin coupled to a harmonic oscillator** 

##### **Interaction Hamiltonian** 

Let us first consider the case of a single spin of Hamiltonian _Hs_ ( **_B_** 0) where **_B_** 0 = _B_ 0 **_e_** _z_ is the applied static magnetic field. We isolate a two-level system _{|_ g _i, |_ e _i}_ among the spin energy-levels, with corresponding transition frequency _!s_ ( _B_ 0) = ( _E|_ e _i − E|_ g _i_ ) _/_ ~. 

We introduce the Pauli matrices (ˆ _σx,_ ˆ _σy,_ ˆ _σz_ ), where : 



45 



<!-- Start of picture text -->
[#]<br>, 7<br><!-- End of picture text -->

~~-~~ <mark>[#]</mark> , 7 

| 

1 

_Chapter 3. Spins in a cavity_ 



<!-- Start of picture text -->
1<br>Pe(t) � =50 g<br>� =g/5<br>0.5<br>0<br>T 1 = 4 g 2 / 100 150 200<br>Time t/4g<br><!-- End of picture text -->

FIGURE 3.6: **Weak and strong regime for a single-spin** . The population of state _|_ e _,_ 0 _i_ , obtained by solving Eqs. 3.30-3.33, presents oscillations when in the strong coupling regime ( _g > _ ) and an exponential decay of characteristic rate 4 _g_<sup>2</sup> _/_ in the weak coupling regime. 

spin, and its emission; those are the basic processes on which the whole field of CQED is built. One prominent phenomenon predicted by the Jaynes-Cummings Hamiltonian is that a spin placed in the excited state can emit and re-absorb reversibly a single photon into an empty cavity at a frequency _g_ ; this phenomenon is known as vacuum Rabi oscillations [39]. 

If the system were perfectly isolated from any environment, these oscillations could last indefinitely. However several mechanisms limit the duration of these coherent exchanges: the resonator has a damping rate __ , giving the characteristic lifetime for an intra-resonator photon of 1 _/_ and the spin looses its coherence at a rate _γ_ = 1 _/T_ 2, as described in 3.1. Thus one distinguishes two regimes: 

- **Strong coupling regime** when _g ≫ , γ_ : the excitations in the system are long-lived compared to the Rabi period and one may observe Rabi oscillations [39], as shown in Fig. 3.6. 

- **Weak coupling regime when** _g ⌧ , γ_ : excitations decay faster than the coherent evolution between spin and the cavity, thus Rabi oscillations are suppressed. 

For an electronic spin-1/2 with _γe/_ 2 _⇡_ = 28 GHz/T located _d_ = 10 µm away from a wire-like inductance embedded in a resonator of frequency _!_ 0 _/_ 2 _⇡_ = 7 GHz and impedance _Z_ 0 = 50 ⌦, _g_ can be estimated to: 



This is much smaller than the damping rates of typical ESR resonant circuits, so that ESR experiments are in the weak coupling regime. In the following, we will see that even in the weak coupling regime, the quantum treatment of the spin-cavity interaction and of field relaxation via a transmission line (see 2.1.3) yields interesting new effects. 

##### **Dynamics of the spin-cavity system coupled to a bath** 

In an ESR experiment, the spin-cavity system is driven and probed via a transmission line coupled with rate __ 1 to the cavity mode. Assuming a coherent state drive sent on port 1, as shown in Fig. 3.5, the drive Hamiltonian is _H_<sup>ˆ</sup> _d/_ ~ = _i_<sup>_p_</sup> _<u></u>_ 1( _βa_ ˆ<sup>_†_</sup> _e_<sup>_−i!dt_</sup> + _β_<sup>_⇤_</sup> _ae_ ˆ<sup>_i!dt_</sup> ), where _β_ is the amplitude of the drive and _!d_ the drive frequency. The Hamiltonian of the system in the frame rotating at _!d_ is: 



47 

_Chapter 3. Spins in a cavity_ 

where ∆0 = _!_ 0 _− !d_ and ∆ _s_ = _!s − !d_ . The state of the system _| i_ at time _t_ is described by a matrix density _⇢_ ( _t_ ). The system evolution can be described by a Lindblad equation written using _⇢_ as: 



where _L↵_ [ _⇢_ ] are called superoperators and are defined as _L↵⇢L_<sup>_†_</sup> _↵_<sup>_−_</sup><sup><u>1</u></sup> 2<sup>_{L_</sup> _↵_<sup>_†L↵, ⇢}_.Each superoperator</sup> is used to describe an interaction with the environment. The cavity leakage due to coupling to ˆ the measurement lines or to internal losses is described by _Lr_ =<sup>_p_</sup> _<u>a</u>_ . Spin energy relaxation is ˆ described by _L_ 1 =<sup>_p_</sup> Γ1 _σ−_ and spin decoherence by _L_ 2 = ~~p~~ _γ/_ 2ˆ _σz_ [64]. 

Eq. 3.29 fully characterizes the evolution of the system. It is valid both in the strong and weak coupling regimes. In the latter however, it can be simplified to retrieve the classical Bloch equations, supplemented by an additional effect of quantum origin : spin relaxation by the Purcell effect. 

##### **Purcell effect** 

To evidence cavity-enhanced spin relaxation by the Purcell effect, we now present a simple argument found in [39]. Consider the undriven spin-cavity system, with the spin prepared at time _t_ = 0 in the excited state _|_ e _i_ and no photon in the cavity, and at zero temperature. The system evolution can be written using only the basis composed of _|_ g _,_ 0 _i_ , _|_ g _,_ 1 _i_ and _|_ e _,_ 0 _i_ states. Using Eq. 3.29 with ∆= ∆0 _−_ ∆ _s_ and ∆ _s_ = 0 (and neglecting non-radiative spin decoherence processes, i.e. taking Γ1 = _γ_ = 0) yields the following equations for the spin-cavity density matrix _⇢_ : 



In the weak-coupling regime _g ⌧ _ , the probability _⇢_ g1 _,_ g1 of finding a photon in the cavity decays much faster than the rate at which the spin can transfer its excitation via Rabi oscillations. As a result the cavity is nearly always empty _⇢_ g1 _,_ g1 _⇡_ 0. In this regime, one can also assume that the coherence terms _⇢_ e0 _,_ g1 and _⇢_ g1 _,_ e0 follow adiabatically the variations of the excited state population [39] such that _⇢_ ˙g1 _,_ e0 _⇡_ 0 and _⇢_ ˙e0 _,_ g1 _⇡_ 0. According to these three assumptions, Eqs. 3.32 & 3.33 yield: 





We now replace _⇢_ e0 _,_ g1 and _⇢g_ 1 _,e_ 0 in Eq. 3.30, leading to: 



We thus obtain that _⇢_ e0 _,_ e0 is exponentially damped, at the so-called Purcell rate given by: 



48 

_Chapter 3. Spins in a cavity_ 

This is illustrated in Fig. 3.6 where we show a numerical integration of Eqs. 3.30-3.33 both in the strong and in the weak coupling regime. We stress that treating the resonator field quantummechanically is essential to derive this Purcell effect, which is a direct manifestation of the action of quantum fluctuations on the spin dynamics. 

##### **Resonator adiabatic elimination** 

A more rigorous treatment of the Purcell effect in a quantum optics theoretical framework, which also takes into account the presence of a drive, relies on adiabatic elimination of the resonator-field variables (see [64, 27, 65, 66] and references within). We summarize here the main results. First, one separates the field operator from its mean value by writing: 



In the absence of the spin, the steady-state value of _↵_ is given by the input-output relations (see Eq. 2.52): _↵_ = 2<sup>_p_</sup> _<u></u>_ 1 _β/_ ( __ + 2 _i_ ∆0). In the limit _g ⌧ _ , the adiabatic elimination of the resonator operators ˆ _c_ and ˆ _c_<sup>_†_</sup> then yields the following master equation in the drive rotating frame [65] for the reduced spin density matrix _⇢_ ˜: 



with the effective Hamiltonian _H_<sup>ˆ</sup> e↵ being [64]: 



where _⇠_ = ∆<sup>2</sup> ∆+ _<u>g</u>_<sup>22</sup> _/_ 4<sup>.The extra</sup><sup>_⇠_term renormalizes slightly the spin frequency.As the correction is</sup> only of order _g_<sup>2</sup> _/_ , we neglect it in the following. 

In addition to modifying _H_<sup>ˆ</sup> e↵ , the adiabatic elimination of the resonator operator is responsible for the appearance of a new spin superoperator _Lp_ = ~~p~~ Γ _p_ (∆)ˆ _σ−_ where Γ _p_ is the decay rate given in Eq. 3.37 [64]. This novel relaxation channel is precisely the cavity-enhanced spontaneous emission, i.e. the Purcell effect. 

Within this approximation, the semi-classical equations of motion for the spin observables and the intra-cavity field in the drive rotating frame can be derived from Eqs. 3.38-3.39. For the sake of simplicity, we consider here that _↵_ is a real number; we write _!_ 1 = _−_ 2 _g↵_ so that: 



with _γ?_ = _γ_ +<sup><u>Γ</u></sup> 2<sup><u>1</u>+Γ</sup> 2<sup>_<u>p</u>_.Eqs. 3.41-3.43 are thus identical to the Bloch equations (see Eqs. 3.9-3.10)</sup> with only in addition a new _T_ 1 relaxation channel given by the Purcell effect. 

Note that in presence of a finite photon thermal <u>population</u> in the resonator _n_ th the Lindblad ˆ operator _Lp_ is changed into the sum of _Lp_ + = ~~p~~ Γ _pn_ th _σ_ + and _Lp−_ = ~~p~~ Γ _p_ ( _n_ th + 1)ˆ _σ−_ , which describes spontaneous and stimulated emission as well as absorption. If no other relaxation process 

49 

_Chapter 3. Spins in a cavity_ 

is present (Γ1 = 0), Eq. 3.43 is modified into [27]: 



This implies that the relaxation is enhanced by a factor (2 _n_ th + 1) while the polarization is decreased by the same factor. 

In addition to showing cavity-enhanced spin-relaxation, Eqs. 3.41-3.43 also provide a way to compute ˆ the signal emitted from the spin. We see that the intra-cavity field is changed by 2 _ig/_ ( __ + 2 _i_ ∆) _hσ−i_ in the presence of the spin; the output signal leaking from the cavity is readily computed thanks to ˆ ˆ input-output theory as _ha_ out _i_ =<sup>_p_</sup> _<u>hai</u>_ (see Eq.2.50). We thus come to the conclusion that the spin ˆ ˆ emits a microwave signal in the detection waveguide that is roughly given by _ha_ out _i_ = 2 _ghσ−i/_<sup>_p_</sup> _<u></u>_ at resonance (∆= 0). This equation is the quantum-optics analog of the classical inductive detection described in 3.1.3. The output signal is proportional to the spin transverse magnetization, to the spin-photon coupling constant, and to 1 _/_<sup>_p_</sup> _<u></u>_ . 

#### **3.2.2 Collective effects** 

We have seen up to now that a spin weakly coupled to a resonator is well described by the classical Bloch equations, with an extra relaxation channel given by the Purcell spontaneous emission rate. In the following we discuss the validity of this description for an ensemble of spins. 

##### **N identical spins model** 

We consider first the ideal case of _N_ identical spins-1/2 with frequency _!s_ coupled with same coupling constant _g_ to the resonator. The system Hamiltonian is the sum of the Jaynes-Cummings Hamiltonians associated with each spin, and is known as the Tavis-Cummings Hamiltonian [67]: 



where ( _j_ ) refers to the operators of spin _j_ . This Hamiltonian acts on _Es ⌦ Ec_ , where _Es_ is the 2<sup>_N_</sup> - dimensional Hilbert state spanned by the states _{|"_ 1 _, . . . , "ni, "i_ = _{_ g _i,_ e _i}}_ and _Ec_ is the resonator Hilbert space. Introducing the collective spin operators _S_<sup>ˆ</sup> _k_ =<sup>P</sup><sup>_N_</sup> _j_ =1<sup>_σ_ˆ</sup> _k_<sup>(</sup><sup>_j_), the Hamiltonian can be</sup> rewritten as: 



> 2 ˆ A remarkable property of this Hamiltonian is that the total spin angular momentum **_S_**<sup>ˆ</sup> = _Sx_ 2<sup>+</sup><sup>_S_ˆ</sup> _y_<sup>2+</sup> _S_ ˆ _z_<sup>2is conserved in time since [</sup><sup>_H_TC</sup><sup>_,_</sup><sup>**_S_**ˆ</sup> 2] = 0. It is therefore interesting to introduce the basis _|S, mi_ of joint eigenstates of **_S_**<sup>ˆ</sup> 2 and _S_ ˆ _z_ , defined as: 



_S_ can take any positive values among _{N/_ 2 _, N/_ 2 _−_ 1 _, ...}_ ; and _m_ can take any values among _{−S, −S_ + 1 _, ..., S −_ 1 _, S}_ . Since _S_ is conserved in time, the system dynamics is restricted to states having the same _S_ as the initial state. Within one _S_ subspace, _m_ + _S_ describes the number of excitations that can be exchanged with the resonator. For instance, emission of a photon takes the system from _|S, mi ⌦|_ 0 _i_ to _|S, m −_ 1 _i ⌦|_ 1 _i_ . Photon absorption or emission is thus impossible for all states for which _S_ = 0, meaning that they are strictly dark states. For other states, the 

50 





<!-- Start of picture text -->
4<br>T ——-—<br>I/<br>|<br>o o<br><!-- End of picture text -->

~~|— —~~ 

/ ~~—~~ / ~~—~~ 

_Chapter 3. Spins in a cavity_ 



<!-- Start of picture text -->
a 6 b 6<br>4<br>4<br>2<br>2<br>0<br>� �<br>−2 0<br>0 1 2 3 4 0 1 2 3 4<br>time (s) time (s)<br>i i<br>z z<br>ˆ S ˆ S<br>h h<br><!-- End of picture text -->

FIGURE 3.8: **Spin relaxation** simulated for 5 spins starting from a disordered state. Black: ideal exponential Purcell relaxation (Γ _p_ = 1 s<sup>_−_1</sup> ), blue _hS_<sup>ˆ</sup> _zi_ . **a** Without inhomogeneous broadening, the relaxation goes to a trap state **b** whereas for sufficiently large inhomogeneous broadening (spins spaced by 1 Hz), a fully exponential decay is observed. Adapted from [27]. 

contain many spins in their excited state. One can say that the system becomes trapped in these highly correlated states, instead of relaxing to its true ground state _|Gi_ . 

Summing up, we see that the radiative relaxation of an ensemble of identical spins seems to be completely different from the single-spin case, where an exponential relaxation of rate Γ _p_ is predicted. Since relaxation now depends on the initial state of the ensemble, and is in general not exponential, a description by the Bloch equations with a single relaxation time _T_ 1 seems clearly impossible. 

##### **Collective or individual relaxation ?** 

The conclusions reached above on the radiative properties of an ensemble of identical spins heavily rely on symmetry properties of the system Hamiltonian. It should thus not come as a surprise that these conclusions are strongly altered when one takes into account two phenomena : spin decoherence, and inhomogeneous broadening of the spin linewidth, both of them characterized by a finite ensemble spin linewidth _γ_ . 

The rigorous treatment of the effects of inhomogeneous broadening and decoherence on the radiative properties of a spin ensemble is a difficult theoretical problem, which has been addressed in a few articles [75, 27, 76]. The outcome of all these works is that in the limit of strong decoherence or inhomogeneous broadening, collective radiative effects are suppressed, and one recovers the situation of a collection of spins radiating independently at a rate Γ _p_ . As a result, the spin ensemble can now truly relax to its ensemble ground state (at rate Γ _p_ ), and trapping in correlated states does not occur any longer. To discriminate between the "independent" or "collective" radiative regime, one has to consider a dimensionless parameter called the ensemble cooperativity defined as: 



Collective effects are found in the so-called strong collective coupling regime _C ≫_ 1; independent radiation from each spin at rate Γ _p_ is obtained in the so-called weak collective coupling regime _C ⌧_ 1. In the remaining of this thesis, we will be in the latter regime. 

52 

_Chapter 3. Spins in a cavity_ 

A clear manifestation of these two situations is seen in Fig. 3.8, which is extracted from [27]. A collection of 5 spins 1 _/_ 2 is considered, starting at _t_ = 0 from a fully unpolarized state. When all spins have the same frequency, the spins relax towards a partially polarized state for which _hS_<sup>ˆ</sup> _zi ⇡_ 2 _._ 8, much less than the true ground state for which _hS_<sup>ˆ</sup> _zi_ = 5. When some frequency inhomogeneity is taken into account, the ensemble relaxes towards the true ground state, at a rate exactly given by the single-spin Purcell rate, Γ _p_ . 

##### **Dynamics of the system** 

In the following, we will often need to simulate the dynamics of an ensemble of _N_ spins when coupled to the cavity. To treat numerically this problem, our collaborator Brian Julsgaard from Aarhus University has written a code [77, 78] that we will use, based on the equations that are presented in the following. Consider a spin ensemble with an inhomogeneous linewidth and non-identical coupling strengths. The spin ensemble is divided into _M_ sub-ensembles regarded each as homogeneous with coupling strength _gm_ , spin resonance frequency _!d_ + ∆ _m_ and containing _Nm_ spins for _m_ = 1 _, . . . , M_ [77]. For each sub-ensemble, collective spin observables _S_<sup>ˆ</sup> _k_<sup>(</sup><sup>_m_)</sup> can be introduced. The Hamiltonian of Eq. 3.46 expressed in the rotating frame in presence of a drive is transformed into: 



Rewriting the master equation of Eq. 3.29 for these collective variables and assuming identical _T_ 1 and _T_ 2 processes for each sub-ensemble allows to derive the following equations for the mean-value of each operator: 



where _X_<sup>ˆ</sup> and _Y_<sup>ˆ</sup> are the intra-resonator quadrature operators. This set of equations can be used to compute numerically the evolution of the mean values for each sub-ensemble. To solve the complete behavior of the system, spin ensemble and resonator, one needs to solve 3 _M_ + 2 differential equations, three for each sub-ensemble and two for the resonator. Provided that _M_ is not too large, this can be done numerically. We use this approach in ch. 7 to simulate a complete spin-echo sequence in our experiment. 

53 

## **Chapter 4** 

# **Bismuth donors in silicon** 

In this third and last background part, we describe the spin system that we use throughout this thesis: bismuth donors in silicon (Si:Bi). Group V donors in silicon were studied as early as 1954, with pioneering works from Honig and Feher [79, 80] focusing extensively on phosphorus and arsenic. The very long values reported for _T_ 1 ( _>_ 1000 s [81]) and _T_ 2 = 0 _._ 2 ms for Si:P lead already in these early days to the idea of using the spin to store classical information [82]. Later on, Kane extended this suggestion to building a quantum computer based on Si:P [83], triggering a renewed intense interest in these systems, seen as "spins living in a semiconducting vacuum”. 

Indeed, in the quest for ideal qubit candidates, the thoroughly-studied silicon appears, along with carbon, as a promising host material since its main isotope<sup>28</sup> Si has zero nuclear spin so that an enriched<sup>28</sup> Si sample would provide a magnetically-silent environment for donor spins. The electronic spin 1 _/_ 2 of a donor in silicon is seen as a particularly promising qubit candidate due to its long-lived coherence and fast manipulation time. Bismuth<sup>209</sup> Bi is the heaviest group V donor in silicon (see Table 4.1); other donors include<sup>31</sup> P,<sup>33</sup> As,<sup>121</sup><sup>_,_123</sup> Sb. In early studies, bismuth gathered less attention than phosphorus due to the latter simplicity and use in modern CMOS devices. However, bismuth received renewed attention recently due to the existence of optimal working points, where the Si:Bi frequency becomes insensitive to magnetic field fluctuations [84] leading to the longest measured coherence times for electronic spins in the solid state [25]. In addition, its large zero-field splitting makes it attractive for coupling to superconducting resonators which could be useful for building a quantum memory for superconducting qubit states [85]. 

|Donor||31P|33As|121Sb|121Sb|209Bi|
|---|---|---|---|---|---|---|
|_ED_|(meV)|45.6|53.8|42.8|42.8|71.0|
|_a_0|(nm)|16.8|15.5|17.3|17.3|11.5|
|∆_E_|(meV)|13.0|22.5|12.3|12.3|41|
|_I_||1/2|3/2|5/2|7/2|9/2|
|_A_|(MHz)|118|198|186|101|1475.4|



TABLE 4.1: **Group V donors characteristics:** ionization energy ( _ED_ ), apparent Bohr radius ( _a_ 0), nuclear spin and hyperfine coupling constant ( _A_ ). Extracted from [16, 86, 87, 88]. 

This chapter will present the essential information to understand the experimental work presented in this thesis. When available we indicate references the reader may consult for more detailed derivations and explanations. In what follows, we briefly present the electronic structure of Si:Bi (see [89]) before describing its spin Hamiltonian, energy levels and ESR transitions (see the work of Mohammady et al. [84]). We list the known relaxation mechanisms (see [81, 90]) as well as the expected sources of decoherence (see [91]). Last we present the characteristics of the sample used in our experiments. 

54 



<!-- Start of picture text -->
“of ap<br><!-- End of picture text -->

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
a b E Conduction Band<br>lattice parameter a c<br>| � (r)| (2) E<br>Bi + ED (6) 1s (3) T2<br>(1) A1<br>V(r) Kohn-Luttinger valley-orbit<br>(EMT) splitting<br><!-- End of picture text -->

FIGURE 4.2: **Bismuth electronic states. a** Illustrative schematic of the donor wave function and of the Coulomb potential compared to the lattice parameter. **b** Six-fold degenerate ground states predicted by effective mass theory and with an additional valley-orbit interaction perturbation. 

in the _µ_ -th valley and are called valley population. In this simplistic picture, EMT produces identical results for all of the donors, with calculations indicating identical Bohr radii and _ED_ = _−_ 31 _._ 3 meV. 

This is in direct contradiction with the experimental results where instead of a single degenerate state three distinct energy-levels are observed [87]. The discrepancy is explained by a break down of the EMT approach in the vicinity of the donor nucleus. To correct this effect and take into account the tetrahedral environment surrounding the donor in the central cell as well as the core and valence electrons screening the Bi nucleus attractive potential, a phenomenological interaction called “valley-orbit” is added as a perturbation of EMT [94]. With this improved model, the degeneracy of the ground state is lifted, yielding three distinct 1s states labeled by their tetrahedral symmetry group designation : a symmetrical ground-state _A_ 1, a three-fold degenerate level _T_ 2 and a two-fold degenerate level _E_ . The corresponding eigenstates may be written in the same manner as in Eq 4.1 with envelope hydrogenic functions (see Fig. 4.1.1a). Written in the valley basis _{±_ **_k_** _x, ±_ **_k_** _y_ , _±_ **_k_** _z_ }, the states are: 





This treatment yields different ionization energies and Bohr radii for the five silicon donors, in agreement with measurements (see Table 4.1). Bismuth is the deepest donor, and its wavefunctions are correspondingly more confined with a smaller Bohr radius. In the remaining part of this chapter, we are mainly interested in the spin properties of the neutral Bismuth donor in its ground state _A_ 1, but the properties of higher-energy states do play a role in the donors physics, as will be clear later. 

#### **Charge state** 

The charge state of the bismuth donors in silicon is found by calculating the position of the Fermilevel as a function of temperature, see Neamen [95]. At zero temperature, for a n-type semiconductor, all donors retain their electrons and thus the Fermi level energy will be situated mid-way through the donor energy level _A_ 1 (see below) and the conduction band : _EF_ =<sup><u>1</u></sup> 2<sup>(</sup><sup>_EC−EA_1).At slightly</sup> higher temperature, the donors electrons start being excited to the conduction band and the fraction of ionized donors is given by: 



56 

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
a b 1<br>T=0 K T<400 K<br>EC conduction band<br>E Fermi level<br>F<br>E<br>A1<br>00 50 100 150 200<br>Temperature (K)<br>Fraction of ionized donors<br><!-- End of picture text -->

FIGURE 4.3: **Charge state of a bismuth donor. a** At non-zero temperature, electrons bound to donors are excited to the conduction band, resulting in a partial ionization of the donors and a lowering of the Fermi energy level. **b** Fraction of ionized donors _ND_<sup>+</sup><sup>_/ND_as a function of temperature in the case of</sup> bismuth, evaluated with _ED_ = 71 meV and _ND_ = 10<sup>16</sup> cm<sup>_−_3</sup> . 

where _ND_ is the total concentration of donors and _ND_<sup>+is the concentration of ionized donors.Since</sup> the silicon gap is much larger than the ionization energy of the shallow donors, for low enough temperatures ( _T <_ 400 K) the valence electrons can not be excited to the conduction band and thus the concentration of free carriers in the conduction band _n_ is only given by the concentration of ionized donors: _n_ = _ND_<sup>+.The concentration of free carriers is also linked in case of non-degenerate</sup> semi-conductors to the temperature by: 



where _Nc_ = 2(2 _⇡m_<sup>_⇤_</sup> _kBT/h_<sup>2</sup> )<sup>3</sup><sup>_/_2</sup> is the effective density of states in the conduction band with _m_<sup>_⇤_</sup> being the effective mass of an electron. Thanks to these two relations, Eq 4.5 may be rewritten to determine _n_ as a function of the temperature _T_ , the donor ionization energy _ED_ and the concentration of donors: 



where _N⇠_ = _Nce_<sup>_−ED/kBT_</sup> . 

As the electrons are moving from the donor level to the conduction band as a function of temperature, the Fermi energy tends to move downwards. Precise determination of the Fermi energy as a function of _n_ is given by Eq 4.6. One can then access the fraction of ionized donors by evaluating Eq 4.5. With an ionization energy _ED_ = 71 meV and for a concentration _ND_ = 10<sup>16</sup> cm<sup>_−_3</sup> , bismuth donors are in their neutral state up to _T_ = 40 K, see Fig. 4.3b. In our experiments which take place at millikelvins temperatures, all donors should be in their neutral state. However, note that other factors may impact the charge states of donors, such as internal electric fields [96, 97] or bending of the energy levels in presence of Schottky barriers; we will come back to this issue later in ch. 7. 

57 

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
20 19 18 17<br>10 16<br>15<br>14<br>13<br>12<br>11<br>5<br>9A/4<br>B0(T)<br>0<br>0.2 0.4 0.6<br>-11A/4<br>-5 10<br>9<br>8<br>7<br>6<br>5<br>-10<br>1 2 3 4<br>-, m=-4<br>=-9/2<br>=1/2, mI<br>mS<br>+, m=5<br>m<br>S=-1/2, mI=-9/2<br>=9/2<br>=1/2, mI<br>mS<br>m<br>S=-1/2, mI=9/2<br>+, m=-5<br>-, m=4<br>Energy (GHz)<br><!-- End of picture text -->

FIGURE 4.4: **Bismuth energy spectrum** . Energy-levels computed from the diagonalisation of the Si:Bi _±_ Hamiltonian as a function of _B_ 0 (Eq 4.8). The coupled energy-levels _Em_<sup>are color-coded from purple to</sup> red, the uncoupled energy-levels are in black. Figure adapted from [99, 84]. 

### **4.2 Spin levels and ESR-allowed transitions.** 

A neutral bismuth donor in silicon has spin properties arising from the coupling of the _S_ = 1 _/_ 2 electronic spin to the<sup>209</sup> Bi _I_ = 9 _/_ 2 nuclear spin. When placed in an external magnetic field **_B_** , its twenty energy levels are described by the following spin Hamiltonian that includes a Zeeman effect for electronic and nuclear spin and an isotropic hyperfine coupling [98]: 



where _γe/_ 2 _⇡_ = 27 _._ 997 GHz _/_ T and _γn/_ 2 _⇡_ = 6 _._ 962 MHz _/_ T are the electronic and nuclear gyromagnetic ratio and _A/_ 2 _⇡_ = 1 _._ 4754 GHz is the hyperfine coupling constant [26]. To understand this system, we will follow the analysis made by Mohammady at al. in [84]. Assuming a static magnetic field directed along z, **_B_** 0 = _B_ 0 **_e_** _z_ , the Hamiltonian may be re-written as: 



where _!_ 0 = _B_ 0 _γe_ and _δ_ = _γn/γe ⇡_ 10<sup>_−_3</sup> . Due to the hyperfine coupling, the Hamiltonian is not diagonal in the Zeeman basis spanned by _{|ms, mii}_ with _ms_ = _±_<sup><u>1</u></sup> 2<sup>and</sup><sup>_mi_=</sup><sup>_−_</sup> 2<sup><u>9</u></sup><sup>_. . ._</sup><sup><u>9</u></sup> 2<sup>andits</sup> energy states are instead hybridized electro-nuclear states. The energy spectrum as a function of magnetic field obtained from the Hamiltonian diagonalization is shown in Fig. 4.4. 

58 

_Chapter 4. Bismuth donors in silicon_ 

#### **Hybridized eigenstates** 

To understand the spectrum in Fig. 4.4 and the spin properties of the eigenstates, one can notice first that the projection _m_ = _mi_ + _ms_ of the total angular momentum operator **_F_**<sup>ˆ</sup> = **_I_**<sup>ˆ</sup> + **_S_**<sup>ˆ</sup> onto **_e_** _z_ is a good quantum number since [ _H,_<sup>ˆ</sup> _S_<sup>ˆ</sup> _z_ + _I_<sup>ˆ</sup> _z_ ] = 0. If we then consider the application of the Hamiltonian on a state of the Zeeman basis: 



it appears that _|_<sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>9</u></sup> 2<sup>_i_and</sup><sup>_|−_</sup><sup><u>1</u></sup> 2<sup>_, −_</sup><sup><u>9</u></sup> 2<sup>_i_are unmixed eigenstates of the Hamiltonian since</sup><sup>_I_ˆ</sup><sup>_±|⌥_</sup><sup><u>1</u></sup> 2<sup>_, ±_</sup><sup><u>9</u></sup> 2<sup>_i_= 0.</sup> Their energies are: 



These states are the only ones in the spectrum (see Fig. 4.4) to have a linear energy dependence on _B_ 0. When _|m| <_ 5, _|±_<sup><u>1</u></sup> 2<sup>_, mii_hybridizes with</sup><sup>_|⌥_</sup><sup><u>1</u></sup> 2<sup>_, mi ±_1</sup><sup>_i_.From these observations, the Hamiltonian</sup> expressed in the Zeeman basis can be decomposed into two one-dimensional Hamiltonians acting on bases 



and nine two-dimensional Hamiltonians acting on subspaces labeled by _m_ : 



As explained in [84], the restriction of _H_<sup>ˆ</sup> 0 to one of these two-dimensional bases is: 



where: 





ˆ ˆ Since cos _✓mσz_ + sin _✓mσx_ = _σ_ 0 _✓m_ , where _σ_ 0 _✓m_ is the Pauli spin matrix in the rotated basis, the eigen-energies are given by: 



This expression is exact for all magnetic fields and for all _m_ and yields the energy spectrum of Fig. 4.4. The corresponding energy eigenstates are: 



where 



From this analysis, it appears that the eigenstates can be labeled in multiple ways: by order of 

59 

_Chapter 4. Bismuth donors in silicon_ 

increasing energy _{|ii, i_ = 1 _, . . . ._ 20 _}_ , by the coupled basis { _|±, mi}_ and in the high-field limit by the Zeeman basis _{|ms, mii, ms_ = _±_<sup><u>1</u></sup> 2<sup>_, mi_=</sup><sup>_−_</sup> 2<sup><u>9</u></sup><sup>_. . ._</sup><sup><u>9</u></sup> 2<sup>_}_, see Fig. 4.4.The correspondence between the</sup> Zeeman basis and the coupled basis is realized by noticing that in the high-field limit, tan _✓m !_ 0 _± ±_ (Eq 4.17). Thus _am_<sup>_!_1 and</sup><sup>_b_</sup> _m_<sup>_!_0, meaning that the electro-nuclear eigenstates</sup><sup>_|±, mi_converge</sup> respectively to the Zeeman eigenstates _|ms_ = _±_<sup><u>1</u></sup> 2<sup>_, mi_=</sup><sup>_m ⌥_</sup><sup><u>1</u></sup> 2<sup>_i_as expected when the hyperfine</sup> term can be neglected with respect to the Zeeman terms. 

###### 

The following simplified expressions are readily obtained in the “low-field limit” _!_ 0 = _B_ 0 _γe ⌧ A_ , which will be the one relevant for our experiments: 



The field _B_ 0 is seen to lift linearly the nine-fold and eleven-fold degeneracy of the ground and excited multiplet (see Fig. 4.4). Transitions from the ground to the excited multiplet have frequencies _± ±_ centered on 5 _A/_ 2 _⇡ ⇡_ 7 _._ 37 GHz. In this low-field limit, the coefficients _am_<sup>and</sup><sup>_b_</sup> _m_<sup>describing the</sup> mixing of the eigenstates are strongly dependent on _m_ . 

#### **ESR-allowed transitions** 

As explained in ch.3 (see Eq. 3.20 and following for instance), spin transitions can be driven if and only if _hi|_ **_S_**<sup>ˆ</sup> _|ji 6_ = 0; in the following, we compute these matrix elements for Si:Bi. 

_Sx transitions allowed at large magnetic field_ . 

In the high-field limit, the Bismuth donor spin eigenstates are well approximated by the Zeeman basis and the allowed transitions are thus given by the usual selection rules _|_ ∆ _ms|_ = 1 and ∆ _mi_ = 0. The 10 transitions _|ms_ =<sup><u>1</u></sup> 2<sup>_, mii$|ms_=</sup><sup>_−_</sup><sup><u>1</u></sup> 2<sup>_, mii_have a matrix element</sup><sup>_h_1</sup><sup>_/_2</sup><sup>_|_ˆ</sup><sup>_Sx|−_1</sup><sup>_/_2</sup><sup>_i_=1</sup><sup>_/_2, as</sup> expected for an electronic spin 1 _/_ 2 (see Figs. 4.5 & 4.6b). 

_Sx transitions allowed at low magnetic field_ . 

At lower magnetic field, states _{|ms_ =<sup><u>1</u></sup> 2<sup>_, mii, |ms_=</sup><sup>_−_</sup><sup><u>1</u></sup> 2<sup>_, mii}_are progressively hybridized into</sup> _{|_ + _, mi, |−, m −_ 1 _i}_ as depicted in Fig. 4.5. Correspondingly, the matrix element of these transitions becomes smaller than 1 _/_ 2 (see Fig. 4.6b). Their matrix elements are: 



and depend strongly on _m_ at low magnetic field. 

In addition to these 10 transitions, transitions between _|−, mi_ and _|_ + _, m−_ 1 _i_ become allowed because of this hybridization due to the hyperfine interaction. The frequency and matrix-element of these extra 9 transitions as a function of magnetic field have been plotted in Fig. 4.6c (blue arrows). Their matrix elements are: 



and go to zero at high field, as expected. 

60 

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
a High-field b Low-field<br>mi+1 mi mi-1 +, m+1 +, m +, m-1<br>ms = 1/2 hyperfinecoupling<br>ms = -1/2 -, m-2<br>mi+1 mi mi-1 -, m -, m-1<br>4.5: Transitions schematic . a At the usual ESR transitions between<br><!-- End of picture text -->

FIGURE 4.5: **Transitions schematic** . **a** At high-field, the usual ESR transitions between levels _|ms_ = <u>12</u><sup>_, mii $ |ms_=</sup><sup>_−_</sup><sup><u>1</u></sup> 2<sup>_, mii_are allowed (brown arrows).At lower fields, the hyperfine coupling renders</sup> the Zeeman basis ( **a** ) invalid to describe the hybridized electro-nuclear states (symbolized by the blue ellipses) however an accurate description is given by the coupled basis _|±, mi_ ( **b** ). **b** At low magnetic field, in the coupled basis _|±, mi_ , the high-field ESR transitions are now labeled _|_ + _, mi $ |−, m −_ 1 _i_ . The mixing induced by the hyperfine term allows in addition the transitions _|−, mi $ |_ + _, m −_ 1 _i_ , as well as _|_ + _, mi $ |_ + _, m −_ 1 _i_ and _|−, mi $ |−, m −_ 1 _i_ . 

It is interesting to note that the transitions _|_ + _, mi $ |−, m−_ 1 _i_ and _|_ + _, m−_ 1 _i $ |−, mi_ (in the _|m_ 6 4 manifold) are quasi-degenerate in frequency and that their matrix elements are complementary: _|a_<sup>+</sup> _m_<sup>_a−_</sup> _m−_ 1<sup>_|_+</sup><sup>_|b_+</sup> _m−_ 1<sup>_b_</sup> _m_<sup>_−|⇡_1</sup><sup>_/_2.Thus,atanygivenmagneticfield,only10transitionshaveamatrix</sup> element greater than 1 _/_ 4, see Fig. 4.6b & c (the associated pairs are denoted by a grey circle). 

##### _Sz transitions_ . 

An unusual feature of Si:Bi (again, due to the hyperfine coupling) is the existence of 9 transitions that can be driven by a microwave field **_B_** 1 parallel to the static field **_B_** 0. These _S_<sup>ˆ</sup> _z_ transitions connect levels _|_ + _, mi_ and _|−, mi_ in the coupled basis and their matrix element is given by: 



Even if these transitions are forbidden in the high-field limit, they have a sizeable matrix element in the range [0 _,_ 0 _._ 4 T] and can thus be observed at low-field. They are shown in pink in Fig. 4.6a, and their frequency and intensity dependence on _B_ 0 is shown in Fig. 4.6d. It is interesting to note that each transition comes in-between two _S_<sup>ˆ</sup> _x_ transitions. 

##### _NMR transitions_ 

In the above description, we have restricted ourselves to transitions whose frequencies lie in the gigaHertz range. In addition, transitions between _|±, mi_ and _|±, m −_ 1 _i_ (with frequencies in the MegaHertz range) are allowed, as shown in grey in Fig. 4.6a. At high fields, these transitions can only be driven via the nuclear spin matrix element _Ix_ ; however at low field they acquire a sizeable _Sx_ matrix element: 



These transitions can thus be driven faster than usual nuclear spin transitions, as demonstrated in [85] 

61 

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
a<br>+, m=5<br>+, 4 +, 3 +, 2<br>20 19 18 +, 1 +, 0 +,-1<br>17 16 15 14 +,-213 +,-312 +,-4 +, m=-5<br>11 10<br>7 8 9 high B0<br>6<br>2 3 4 5 -,-2 -,-3 -, m=-4<br>1 -, 3 -, 2 -, 1 -, 0 -,-1<br>-, m=4<br>Sx transitions allowed at high-B0 Sx Transitions forbidden at high-B0 Sz transitions<br>b c d<br>15<br>10<br>5A<br>5<br>0 Mat. El 0.5<br>0<br>0 0.1 0.2 0.3 0 0.1 0.2 0.3 0 0.1 0.2 0.3<br>Magnetic field B0 (T) Magnetic field B0 (T) Magnetic field B0 (T)<br>+, m -, m-1 +, m -, m+1 +, m -, m<br>Frequency (GHz)<br><!-- End of picture text -->

FIGURE 4.6: **Allowed ESR transitions** . **a** Energy levels diagram with ESR allowed transitions symbolized with arrows: _S_<sup>ˆ</sup> _x_ -transitions allowed at large _B_ 0 _|_ + _, mi $ |−, m −_ 1 _i_ (brown arrows, panel **b** ), _S_<sup>ˆ</sup> _x_ - transitions forbidden at large _B_ 0 _|_ + _, mi $ |−, m_ + 1 _i_ (blue square arrows, panel **c** ) and _S_<sup>ˆ</sup> _z_ -transitions _|_ + _, mi $ |−, mi_ (pink circle arrows, panel **d** ). NMR-like transitions are shown with grey triangle arrows. The additional grey level shows the position of the _|_ + _, −_ 5 _i_ level at large _B_ 0. **b-d** Frequencies of ESR allowed transitions as a function of _B_ 0. The curves coloring indicates the transition matrix element value. The color scale is identical for all panels and given in inset of panel **b** . The grey circles in **a** and on the right-side of panels **b-c** frames indicate degenerate transitions (see main text). 

##### _Clock-transitions_ 

A striking feature of some group V donors in silicon is the existence of multiple _df/dB_ 0 = 0 sweetspots in their spectrum, due to the interplay between the hyperfine and Zeeman terms in their Hamiltonians. Mohamady at al. predicted theoretically the existence of _I −_ 1 _/_ 2 sweet-spots, called clock-transitions [84, 100]. Bismuth has eight minima in the _f − B_ space, occurring for transitions ∆ _m_ = _±_ 1 with _m_ 6 0 as can be seen in Fig. 4.6b-c. These transitions are degenerate two-by-two, giving rise to four clock-transitions (see Table 4.2). They were observed experimentally by Wolfowicz et al. [25]. 

These features are very interesting for quantum information applications since the decoherence arising from classical magnetic field noise is reduced at a clock-transition [101]. Phosphorus does not possess any clock-transition due to its nuclear spin _I_ = 1 _/_ 2. While arsenic (<sup>75</sup> As, _I_ = 3 _/_ 2, _A_ = 0 _._ 198 GHz) and antimony (<sup>121</sup> Sb, _I_ = 5 _/_ 2, _A_ = 0 _._ 186 GHz and<sup>123</sup> As, _I_ = 7 _/_ 2, _A_ = 0 _._ 101GHz) have the necessary nuclear spin to also possess clock-transitions, their weaker hyperfine coupling constant implies that the clock-transitions occur at smaller frequencies ( _<_ 600 MHz)[25]. Thus among the group V donors, Bismuth appears the optimal candidate for quantum information 

62 

_Chapter 4. Bismuth donors in silicon_ 

|Transition label_m_<br>|_m_=_−_4|_m_=_−_3|_m_=_−_2|_m_=_−_1|
|---|---|---|---|---|
|Magnetic feld (mT)|187.8|133.3|79.8|26.6|
|Frequency (GHz)|5.214|6.372|7.032|7.338|



TABLE 4.2: **Magnetic-field clock-transitions in Bismuth donors in silicon** . The clock transitions occur for transitions between pairs _|_ + _, m_ + 1 _i $ |−, mi_ and _|_ + _, mi $ |−, m_ + 1 _i_ , with _m <_ 0 for magnetic fields lower than 0.2 mT and frequencies in the gigaHertz range. Adapted from [25]. 

storage, having four clock-transitions at gigaHertz frequencies. 

### **4.3 Donors in strained silicon** 

We have so far discussed the spin Hamiltonian of bismuth donors in the case of an unperturbed silicon lattice. The effect of strain on donors in Silicon has been first observed in [94] and has triggered important theoretical work [94, 102, 103, 104, 105], with the perspective of providing a precise control over the spin properties of donors in silicon [104, 106]. Here we provide a summary of essential results needed for our experiments. 

To understand the effect of stress, consider first a positive stress applied on the z-axis, which builds a compressive strain in the z-axis and a tensile strain in the x-y axis. The influence of strain on the donor eigenstates can be understood from their valley configurations: the valleys in the direction of compressive strain experience a reduction in energy, leading to a higher valley population whereas valleys in the direction of tensile strain exhibit an increased energy, leading to a lower population. As a consequence, the ground state is no longer purely given by the singlet state _A_ 1 but should be described as a mixture of the singlet with the doublet excited states _E_ xy and _E_ xyz [94]. The _T_ 2 states are not involved since they involve combination of opposite pairs of valleys (see 4.1.1). This change of ground state properties has two distinct effects on the spin Hamiltonian. 

###### 

The hyperfine coupling between the electronic spin and the nuclear spin has two separate contributions: an isotropic component (also called Fermi contact) which is directly proportional to the quantum mechanical probability of finding the electron at the nucleus position _/ |_ ( **_r_** Bi) _|_<sup>2</sup> , and an anisotropic part due to dipolar interactions between both spins. The latter can be shown to be always zero due to the 1s nature of states _A_ 1, _E_ and _T_ 2 [107]. Due to the symmetry of the wavefunctions described in section 4.1.1, only the symmetric _A_ 1 state has a non-zero contact hyperfine coupling. Since strain mixes it with the other states, it leads to a reduced hyperfine interaction A. The exact reduction depends on the amount of stress applied and can be derived in the case of high-strain with density function theory [105] as well as a tight-binding model [105]. In the case of small strain, when the lattice deformation is negligible, the reduction may be approximated via a valley repopulation model based on EMT [94], giving: 



for small values of x, the so-called “valley strain” given by _x_ = ⌅ _us_<sup>_0_</sup> _/_ ∆ _E_ . ∆ _E_ is the splitting between _A_ 1 and _E_ states, ⌅ _u_ is the deformation potential and _s_<sup>_0_</sup> is the shear strain. The reduction of the hyperfine parameter A has the overall effect of lowering the frequencies of the considered ESR transitions. 

Note also that the hyperfine coupling can be modified by Stark shift caused by applied electric fields [108, 97, 109], a promising technique for the local control of donor spins in silicon [83]. 

63 

_Chapter 4. Bismuth donors in silicon_ 

#### **Quadrupolar interaction** 

In addition to modifying the hyperfine term of the spin Hamiltonian, stress also contributes to the appearance of a quadrupolar interaction term [110, 111]. Indeed, with a nuclear spin _I_ = 9 _/_ 2, Bismuth possesses an electric quadrupole moment _Q_ . This quadrupole moment interacts with an electric field gradient (EFG) generated by the electron wavefunction through the operator [112]: 





where _↵_ or _β_ = _x, y, z_ are the crystal axis. In the absence of strain, the fully symmetric ground state _A_ 1 produces no EFG and thus has a vanishing quadrupolar interaction. In the presence of stress, the mixing of _A_ 1 with the non-symmetric _E_ xyz state produces an EFG so that a quadrupolar interaction term appears in the spin Hamiltonian. In the case of a magnetic field _B_ 0 applied on the _z_ direction and a resulting EFG in the z direction, the quadrupolar Hamiltonian is: 



This new term produces an energy shift of transitions between states having a different _mi_ , which is the case for all _S_<sup>ˆ</sup> _x_ -ESR transitions in the above discussion. Note that the sign of the energy shift depends on the sign of the EFG and thus on the sign of the applied strain. 

### **4.4 Relaxation times** 

#### **4.4.1** _T_ 1 **relaxation** 

Spin relaxation of shallow donors in silicon has been studied extensively in the 1950s and 1960s experimentally [79, 113, 114, 80, 81, 114, 94, 115, 116, 117]. The measured relaxation times at 4 K surpassed tens of seconds, sparking strong theoretical efforts to understand and model the underlying mechanisms [118, 119, 120, 121]. A variety of relaxation mechanisms were found to be effective at different temperatures, magnetic field, impurity concentrations, and numbers of free carriers. We only wish here to briefly summarize the known mechanisms and their dependence on these parameters and give reported values in the case of bismuth donors. 

##### **Spin-lattice relaxation** 

The electronic spin of shallow donors can relax via exchange of energy with the lattice by emission of phonons. As schematically shown in Fig. 4.7a, two types of processes are usually distinguished: relaxation with conservation of the nuclear spin (∆ _ms_ = _±_ 1, ∆ _mi_ = 0) with a characteristic time labeled _Ts_ , and diagonal relaxation with an additional nuclear spin flip (∆ _ms_ = _±_ 1, ∆ _mi_ = _⌥_ 1) with a characteristic time labeled _Tx_ (see Fig. 4.7a). The "other” diagonal relaxation _Tx0_ involving a double flip of the electron and of the nuclear spin (∆ _ms_ = _±_ 1, ∆ _mi_ = _±_ 1) is highly forbidden [114]. 

Consider two levels _|_ g _i_ and _|_ e _i_ from the Si:Bi energy spectrum and consider the relaxation between _|_ e _i_ and _|_ g _i_ . The levels are split by ~ _!_ 0 with respective populations _n_ e and _n_ g. If the system is excited, the population difference _n_ = _n_ e _− n_ g will progressively relax towards its thermal equilibrium value _N_ e _− N_ g due to interactions with the lattice, _N_ e and _N_ g being respectively the thermal equilibrium values of _n_ e and _n_ g. Defining _W_ e _!_ g and _W_ g _!_ e as the probabilities per second for a spin to relax 

64 

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
m a s = 1/2mi+1 mi TX’ miT-1s b ħωm ET2 virtual c RamanSpin system<br>Resonant Thermal Narrow<br>TX phonons scatt. phonons scatt. band phonons<br>ms = -1/2mi+1 mi mi-1 ħω0 eg A1DirectphononOrbach Raman bath<br>process process process<br>direct Orbach<br>virtual<br>Phonon continuum<br><!-- End of picture text -->

FIGURE 4.7: **Spin-lattice relaxation processes. a** Subset of Si:Bi level schemes with the various spinlattice relaxation processes. **b** Direct, Orbach and Raman phonon relaxation mechanisms. **c** Relaxation paths available to the spin system. 

from level _|_ e _i_ to level _|_ g _i_ and vice-versa, the change in the excited state population writes: 



(and a similar expression for _ng_ ). The rate equation for the population difference _n_ will then be given by: 



where _N_ = _N_ e + _N_ g = _n_ e + _n_ g is the total spin population. 

The phonon radiation bath of the lattice can be described as an infinite set of harmonic oscillators of characteristic energy ~ _!_ , whose thermal occupancy is given by the Bose-Einstein factor: 



where _T_ ph is the temperature of the crystal lattice. When the lattice is well coupled to the environment bath, the phonon equilibrium temperature is given by the system temperature _T_ . 

##### _Direct-phonon process_ 

If we consider the case of a resonant exchange of energy, where the system relaxes by emitting a phonon of energy ~ _!_ 0 into a lattice mode of the same frequency, see Fig. 4.7b, we can evaluate the transition probabilities as 



where one can identify both spontaneous and stimulated emission, as well as absorption, _K_ being a coefficient independent of temperature. Hence, from Eq 4.30: 



At infinite time, the spin system is thermalized with the phonon bath, yielding the thermal population difference: 



This allows to re-write Eq 4.30 in the well-known form<sup>_<u>dn</u>_</sup> _dt_<sup>=</sup><sup>_−_(</sup><sup>_n −n_0)</sup><sup>_/T_1byidentifyingthe</sup> relaxation time _T_ 1 as _T_ 1<sup>_−_1</sup> = _K_ coth ⇣ 2~ _k!B_ <u>0</u> _T_ ⌘. In the high-temperature limit (~ _!_ 0 _⌧ kBT_ ) _T_ 1<sup>_−_1</sup> _⇠_ 2 _KkBT/_ ~ _!_ 0.. This linear dependence of the relaxation rate with temperature is characteristic of direct phonon processes. At temperatures _kBT <_ ~ _!_ 0 the relaxation rate saturates to _T_ 1<sup>_−_1</sup> = _K_ . 

65 

_Chapter 4. Bismuth donors in silicon_ 

The value of _K_ depends on the spin and material properties. In the case of shallow donors in silicon, both Roth [120] and Hasegawa [121] have estimated theoretically _K_ based on two different models where the spin-lattice relaxation arises from the modulation of the spin-orbit coupling by crystal strain. 

From the formula derived by Hasegawa [121, 122], one can extract the following dependency for _K_ in the case of a _Ts_ -type process: 



where ∆ _E_ is the energy difference between the first excited valley state and the ground state and _c_ is a coefficient factor expected to be similar for all shallow donors in silicon in the derivation of Hasegawa [121]. 

##### _Two-phonon relaxation processes_ 

At higher temperatures, other processes involving two phonons need to be taken into account. These processes are schematically shown in Fig. 4.7b. In the Orbach process, the two-phonon process is mediated by the first excited valley state. The spin relaxes by absorbing a phonon of energy ∆ _E_ and emitting a phonon of energy ∆ _E −_ ~ _!_ 0. In the case of a Raman process, the excited state is replaced by a virtual state. Any phonon may absorbed or emitted, the only maching condition being that _|_ ~ _!_ 1 _−_ ~ _!_ 2 _|_ = ~ _!_ 0. At temperatures _kBT ≫_ ~ _!_ 0, the temperature and frequency dependence of _T_ 1 is: 





where _a_ , _b_ and _b_<sup>_0_</sup> are temperature and frequency independent coefficients determined by the underlying relaxation process [117] and are expected to be different for _Ts_ or _Tx_ processes. The characteristic temperature dependence of the Orbach process on ∆ _E_ has been used to determine experimentally its value in the case of shallow donors in silicon [115]. 

Depending on the coefficients _a_ , _b_ , _b_<sup>_0_</sup> and _c_ , the different processes are active in different temperature ranges. In the case of bismuth, experiments have determined for the _Ts_ relaxation that an Orbach process is dominant down to 25 K [116, 26, 123]. At lower temperatures, a Raman process dominates, with reported _T_<sup>7</sup> [116, 26, 123, 98] and _T_<sup>9</sup> dependences [25, 124]. Wolfowicz et al. [25] reported _T_ 1 = 9 s at _T_ = 4 _._ 2 K. Since all reported measurements were performed at temperatures higher than 4 K, the direct-phonon process has never been observed for bismuth. 

On the other hand, phosphorus donors have been measured down to lower temperatures, where the direct-phonon process is expected to dominate. Feher and Gere measured _T_ 1<sup>_−_1</sup> _⇡_ 2 _⇥_ 10<sup>4</sup> s<sup>_−_1</sup> at _T_ = 1 _._ 2 K. A. Morello et al. reported more recently _T_ 1 values with the expected _!_ 0<sup>5-dependence at</sup> 40 mK: _T_ 1<sup>_−_1</sup> _⇡_ 0 _._ 015( _!_ 0 _/γe_ )<sup>5</sup> s<sup>_−_1</sup> T<sup>_−_5</sup> , where _γe_ is the gyromagnetic ratio for phosphorus [122]. From those measurements, one can estimate the coefficient _c_ to be _c ⇡_ 1 _._ 5 _−_ 3 _._ 2 _⇥_ 10<sup>_−_13</sup> s<sup>_−_1</sup> GHz<sup>_−_5</sup> eV<sup>2</sup> (with ∆ _E_ = 13 meV for phosphorus). This coefficient _c_ is expected to be similar for all shallow donors in silicon, according to Hasegawa theory [121] and could give a first rough estimate for the direct phonon relaxation of bismuth donors, yielding at zero temperature and _!_ 0 _/_ 2 _⇡_ = 7 GHz, _T_ 1 _⇡_ 2 _⇥_ 10<sup>5</sup> s. 

##### _Phonon bottleneck_ 

Up to now, we have assumed that the lattice is well coupled to the environment so that thermal equilibrium is always ensured (see Fig. 4.7c). When this condition is not matched, the phonons created by the spins relaxation will accumulate. This has the effect of slowing down the relaxation since the spins see an effectively hotter lattice. This phenomenon is called a phonon bottleneck and gives rise to a _T_<sup>2</sup> dependence for _T_ 1 [90]. Considering the low concentration of our sample, we do not expect this effect to be relevant in our experiment. 

66 



<!-- Start of picture text -->
10§ :<br>| ® Experiment<br>10° | ~~ RamanOrbach (= T) Pe” i<br>— 10°<br>°<br>=Ls 10<br>10°<br>10°<br>10} 7°<br>LJ<br>74 10 14 20 30 40<br>Temperature (K)<br><!-- End of picture text -->

_Chapter 4. Bismuth donors in silicon_ 



<!-- Start of picture text -->
a π /2 π<br>� �<br>echo<br>R<br>b π /2 �<br>� �<br>echo<br>x N<br>c<br>Repeating unit π<br>π /2<br>� �<br>echo<br><!-- End of picture text -->

FIGURE 4.9: **Measuring the coherence times. a** Hahn-echo sequence. An intermediate _⇡_ rotation ensures the rephasing of the spins and the emission of an echo, it also refocus the dephasing due to slow fluctuations of the environment. **b** A sequence with small refocusing pulses limit the environment fluctuations due to flip-flops of resonant spins. **c** Dynamical decoupling sequence. Successive _⇡_ rotations are performed to refocus the dephasing due to dynamic fluctuations. 

fluctuations of the magnetic environment during the evolving times _⌧_ of the sequence ultimately lead to the disappearance of the echo signal, with a characteristic time called the coherence time _T_ 2. The values obtained for _T_ 2 are governed by the dynamics of nearby magnetic impurities. For bismuth donors in silicon, the relevant species are other bismuth spins and silicon-29, which have a spin 1 _/_ 2, present in 4.7% abundance in natural silicon (whereas<sup>28</sup> Si has zero nuclear spin). At sufficiently low temperatures ( _<_ 5 K), phonon-induced spin relaxation becomes so slow that its effect on the bath dynamics can be neglected. Instead, the bath dynamics are governed by intra-bath flip-flops due to the dipolar interactions between spins. The flip-flops are either between silicon-29 spins, non-resonant Bi spins or resonant Bi spins. 

This last decoherence process deserves a separate discussion. During the Hahn-echo sequence, the _⇡_ pulse flips without distinction all resonant Bi spins. A given Si:Bi spin sees therefore its local environment (consisting in other Si:Bi spins) changed after the _⇡_ pulse, which leads to decoherence. This effect is called "instantaneous diffusion”. The decoherence rate in this process depends linearly on the donor concentration up to an intrinsic contribution _T_ 2<sup>_−_</sup> int<sup>1[5, 124].This intrinsic contribution</sup> is determined experimentally by measuring _T_ 2 for decreasing tipping angles of the refocusing pulse which effectively flip increasingly smaller numbers of resonant spins (see Fig. 4.9b). At small donor concentrations, other flip-flop processes become dominant. More details can be found in particular in [126]. 

In natural silicon, _T_ 2int is eventually limited by flip-flops in the<sup>29</sup> Si bath to 0 _._ 8 ms [124]. The _T_ 2 sensitivity to these flip-flops is proportional to _df/dB_ . At the clock-transitions where the sensitivity is canceled since _df/dB_ = 0, the decoherence time is significantly increased. Wolfowicz et al. [25] measured an enhancement of _T_ 2 from 0.8 ms to 90 ms by working at a clock transition in natural silicon for a donor concentration [Bi] = 1 _⇥_ 10<sup>15</sup> cm<sup>_−_3</sup> ). Instantaneous diffusion is also suppressed at the clock transition. 

In isotopically purified<sup>28</sup> Si samples, the<sup>29</sup> Si bath is eliminated and coherence is limited by resonant Bi spins. Flip-flops between pairs not involving the probed spins may be suppressed once again by working at the clock-transition. Wolfowicz et al. [25] measured an impressive value of _T_ 2CT = 2 _._ 7 s 

68 



<!-- Start of picture text -->
3 il 2 Nn, 3 08<br>= 06 = 06-<br>c T,.=27s [= T,.=93 ms<br>2l=} 04 ] 4 2l=} 04 =<br>< 02 £ 02-<br>i 285i:Bi w<br>50 65<br>0 2 4 6 00 01 02 03<br>Time, 27 (s) Time, 27 (s)<br><!-- End of picture text -->



<!-- Start of picture text -->
¥<br>/N<br>fi<br><!-- End of picture text -->



<!-- Start of picture text -->
¥ No oes<br>/N | ll ill Mil<br>fi A A A )<br>Fy y v v v ) 5 tl INunl Ll {I<br>B=2T<br>~ T=15K<br>/M\ ) 1146.7 1146.9 1147.1 T=15K<br>Photon energy (meV)<br><!-- End of picture text -->



<!-- Start of picture text -->
/M\<br><!-- End of picture text -->



<!-- Start of picture text -->
)—;g 10 annealed} %=5 5H|BEA T T T be=2§ 5T| AT- T)<br>bat | Ik > 3<br>® 8 i! iL hig £4 3 il 1<br>8 6 \ £ 3 Gaber 2436s 243.<br>© | p= 4 Magnetic Field (mT)<br>- * as d Y &<br>2=2implanted "f} Dogl Ty=0.71ms sso —<br>wJ \[ = 0 ~|<br>0 50 100 150 200 250 0 025 05 075 1 125 15<br>Depth (nm) Time (ms)<br><!-- End of picture text -->

## **Part II** 

# **Magnetic resonance at the quantum limit** 

71 

## **Chapter 5** 

# **Design and realization of a spectrometer operating at the quantum limit of sensitivity** 

While inductively-detected ESR spectroscopy has a wide range of applications, this technique has a limited sensitivity since it relies on the detection of radiation emitted by the spins into the detection. As spins interact rather weakly with the electromagnetic field, a successful detection requires a large number of spins for the collected signal to overcome the experimental noise. This prevents the use of conventional ESR to study nanoscale samples containing only a few spins, such as a single protein molecule, or a nanoparticle. While alternative techniques such as STM tips [138], mechanical resonators [139, 140], or more recently NV centers [141] have been developed to overcome this limit, there is still a strong interest to increase the sensitivity of spectrometers based on inductive detection due to their versatility [142, 143, 37, 15]. 

To enhance the signal of inductively detected ESR spectroscopy, resonator geometries maximizing the coupling of the spins to the electromagnetic field are developed and when possible samples are cooled down to increase the equilibrium polarization of the spin ensemble. Working at cryogenic temperatures also allows to reduce considerably the part of the experimental noise arising from the thermal fluctuations in the detection waveguide. To benefit entirely from this reduction, cryogenic microwave amplifiers with improved noise figure can be used, such as the High Electron Mobility Transistor (HEMT) amplifiers. 

In this chapter, we describe the design and experimental realization of an ESR spectrometer based on inductive detection via a high-quality factor superconducting micro-resonator, operating at millikelvin temperatures, with the spin signal amplified by a JPA. In this way, the dominant source of noise is the quantum fluctuations of the microwave field at 20 mK. The sensitivity of this spectrometer will be characterized in ch. 7. 

### **5.1 Nanoscale ESR** 

#### **5.1.1 State-of-the-art** 

A number of techniques are currently investigated to push the sensitivity of ESR to the nanoscale, using methods based on optically (ODMR) or electrically (EDMR) detected magnetic resonance, as well as scanning probe setups. 

ODMR relies on the spin-dependent photoluminescence occurring in certain systems, such as doped pentacene single molecules [145] or individual NV centers in diamond [130]. Single spin sensitivity can be reached, mainly thanks to the use of optical pumping creating a large spin polarization and 

72 











<!-- Start of picture text -->
7<br><!-- End of picture text -->





_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

by Eq. 3.44. If the cavity resonance is matched to the spin frequency _!_ 0 = _!s_ , it follows that the output field of port 2 is given by: 





Eq. 5.7 yields that the signal is emitted on the quadrature _hX_<sup>ˆ</sup> out _i_ at resonance. Assuming that the detection is achieved by a linear amplifier of power _G_ and noise temperature _TN_ followed by homodyne detection yielding the quadratures _I_ ( _t_ ) and _Q_ ( _t_ ), one can set the phase of the local oscillator so that the output field quadrature _X_<sup>ˆ</sup> out corresponds to the _I_ quadrature for instance. As seen in ch. 2, the echo is emitted on a mode characterized by an envelope function _u_ ( _t_ ), normalized such as R _u_ ( _t_ )<sup>2</sup> _dt_ = 1. To maximize the signal we choose _u_ ( _t_ ) _/ hX_<sup>ˆ</sup> out( _t_ ) _i_ and using Eq. 5.7, we obtain: 



As seen in ch. 2, the noise _n_ arises from both the electromagnetic fluctuations at thermal equilibrium given by Boltzmann statistics _n_ eq =<sup><u>1</u></sup> 4<sup>coth(~</sup><sup>_!/_2</sup><sup>_kBT_), and the noise added by the amplifier</sup><sup>_n_amp=</sup> <u>1</u><sup>In addition, the spins may also contribute to</sup><sup>_n_due to their incoherent spontaneous</sup> 2<sup>_kBTN/_~</sup><sup>_!_.</sup> emission [153] into the detection waveguide. Their exact contribution _n_ SE depends on the spins state but an estimate is provided by _n_ SE _⇡_ Γ _pN/_ 4. Overall one can write: 



Finally, the signal-to-noise for the detection of a single-echo is characterized by: 



The sensitivity of the experiment can be defined as the number of spins detectable in a single-echo with a signal-to-noise ratio of 1 and is thus given by: 



where we have simplified the expression by assuming conventional ESR limit with _ ≫ w_ and that the echo duration was set by the inhomogeneity of the line _TE ⇡_ 1 _/w_ as well as set __ 2 _⇡ _ . 

##### **Proposal for nanoscale sensitivity** 

For a conventional room-temperature spectrometer, where the resonators often have a threedimensional geometry, Eq. 5.11 yields _N_ min = 10<sup>13</sup> (see Table 5.1). This number results from the weak spin-photon coupling achieved in the usual three-dimensional ESR resonators as well as the low spin-polarization and large microwave noise inherent to room-temperature operation. 

This figure of merit can be significantly improved by using micro-fabricated resonators [142, 143, 37, 15], as shown in Fig. 5.3, because the two-dimensional confinement of the microwave field at the spin location increases _g_ by several orders of magnitude. Operation at lower temperatures also enhances considerably the sensitivity by increasing the spin polarization and allowing for the use of better amplifiers. Sigillito et al. reported _N_ min = 10<sup>7</sup> with a spectrometer built around a thin-film superconducting resonator at 4 K and a HEMT amplifier ([15], see Table 5.1). The latter is 

75 



<!-- Start of picture text -->
Sample placed on the meme B (@)<br>resonator, —strip line r | 0<br>1<br>upside down N w 1 1|<br>Upper Resonator y a ee B,<br>Auxiliary resonator, for<br>coupling enhancement<br>utile crystal 10 um um 28Si:Pii (®)bb<br>d<br>p —s trip line substrate p —s trip line EE — ——50n mNb<br>ground c c<br><!-- End of picture text -->



<!-- Start of picture text -->
10 um um 28Si:Pii (®)bb<br>d<br>EE — ——50n mNb<br>c c<br>= =a<br>Sapphire =} <<br><!-- End of picture text -->



<!-- Start of picture text -->
V<br>:<br>or /\ of<br>A ~~<br>" il<br>K —— c yU<br>Q 0 =<br><!-- End of picture text -->

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

shown in Fig. 5.4a. The JPA chip is glued and bonded to a printed circuit board (PCB) inserted in an aluminum box to protect the SQUIDs from stray magnetic fields and ensure the stability of the JPA, (see Fig. 5.4a). Additional protection is provided by a two-layer mu-metal shielding (Cryoperm), the first one having the same shape as the aluminum box, and the second one being a 15-cm long cylinder at the bottom of which the JPA is placed. 

The ESR measurements are performed via the microwave setup shown in Fig. 5.4b, with transmission lines linking the room-temperature measurement apparatus to the resonator and the JPA. To prevent heat transfer from higher to lower temperature stages, the transmission lines are made of CuNi (or S-CN) coaxial cables from room-temperature to 4 K and of NbTi superconducting cables from 4 K to 12 mK. An experimental challenge, which is encountered in all cQED experiments, is to prevent thermal or technical noise at microwave frequencies to reach the sample at 20 mK so that the microwave field at 20 mK is truly in its ground state, while still being able to measure the signal transmission. 

For input lines (green and brown lines), the solution is to cool the microwave field along the transmission line by inserting attenuators at low temperatures. Consider a cable with a 50 ⌦ input impedance at room-temperature, yielding a number of propagating noise photons _n_ th( _T_ ) = _kBT/_ ~ _!_ = 900; inserting an attenuator _A_ thermalized at a temperature _T_ 0 brings down the number of propagating noise photons to _n_ th _/A_ while adding _n_ th( _T_ 0) = coth(~ _!/_ 2 _kBT_ ) thermal photons. Thus for the input lines shown in Fig. 5.4 attenuated by 20 dB at 4 K and by 20 dB at 20 mK, the number of propagating noise photons incoming onto the resonator is _n_ th = 0 _._ 2. In addition, the asymmetry of the coupling antennas __ 1 _⌧ _ 2 ensures an additional attenuation ( _⇡_ 6 dB) leading to _n_ th = 0 _._ 05. This figure could be improved by adding an extra 10 dB at 20 mK. 

For the output lines (red lines) however the signal cannot be attenuated without degrading the signal-to-noise ratio of the measurement. To nevertheless protect the sample from thermal photons and noise photons emitted by the amplifiers, microwave circulators are placed at 20 mK. Used as shown in Fig. 5.4, they make it possible to let all the output signal propagate towards the amplifier at 4 K, whereas the noise coming from the opposite direction is channeled to a cold 50 ⌦ load that absorbs the noise. Commercial circulators have only 18 dB isolation, we thus use two circulators in series (green and orange in Fig. 5.4) to isolate the JPA from the HEMT noise. As the noise temperature of our HEMT is _TH_ = 4 _._ 5 K, the number of propagating noise photons incoming onto the JPA is estimated to _n_ th = 0 _._ 01. 

In order to characterize the JPA response without having to pass through the ESR resonator, an additional input microwave line (brown in Fig. 5.4) is coupled via a 20-dB directional coupler to the JPA input. The circulator shown in green in Fig. 5.4 is responsible for routing the signal outcoming from the ESR resonator to the JPA and from the JPA to the output line (red) in addition to providing thermal isolation. A double circulator (purple in Fig. 5.4) is inserted between the JPA and the ESR resonator to protect the ESR resonator from the JPA amplified noise and prevent interferences between the two devices. 

The DC and AC bias lines needed to tune the JPA frequency and deliver the pump tone are shown in purple. The DC bias is provided by a stable voltage source (Yokogawa 7651) and is filtered at room-temperature and 4 K, where in addition a voltage divider ( _÷_ 10) is placed. The AC pump tone at _!p ⇡_ 2 _!p_ ( _⇡_ 14 GHz in our experiment) is sent via a dedicated line attenuated by 20 dB at 4 K and 20 mK, like the input signal line. Pump tone leakage to the ESR resonator is suppressed by a 4-8 GHz bandpass filter. 

Low-noise signal amplification is done in several steps, and relies on the fact that the dominant contribution comes essentially from the first amplifier of the chain, regardless of the noise of followup amplifiers. Indeed two amplifiers of gain _G_ 1 and _G_ 2 with noise temperature _TN,_ 1 and _TN,_ 2 are equivalent to an amplifier of gain _G_ 1 _G_ 2 with noise temperature _T_ 1 + _T_ 2 _/G_ 1. In our case, the JPA provides _⇡_ 25 dB gain; it is followed at 4 K by a HEMT amplifier (LNF amplifier) that provides _GH_ = 42 dB with a noise temperature of _TN,_ H = 4.5 K and finally at room-temperature by two 

78 



<!-- Start of picture text -->
A _ 0 : ©<br>CT Io il<br>i=<br>OE a— ( TH — | ,<br><!-- End of picture text -->

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 



<!-- Start of picture text -->
a b c<br>-40 30<br>8.1 8 1.7 MHz<br>π<br>20<br>8.0 -50<br>7<br>0<br>10<br>7.9 arg(S11) -60<br>6 -π 0<br>-π 0 π 0 2 4 6 -20 0 20 -20 -10 0 10 20<br>arg(S11) VDC (V) �ω−ω��/2π� (MHz) �ω−ω��/2π� (MHz)<br>e f<br>d<br>20<br>8 1dB<br>20<br>6 15<br>0 4<br>10<br>2<br>5<br>-20<br>0<br>0<br>0 π 0 4 8 12 -150 -140 -130 -120<br>Pump Phase (°) Time (h) Pin(JPA) (dBm)<br>Phase (°)<br>|² (dB)<br>21<br>|S<br>Gain (dB)<br>Gain (dB)<br>Gain (dB)<br>Frequency (GHz)<br><!-- End of picture text -->

FIGURE 5.6: **Characterization of the flux-pumped JPA. a** Linear response of the JPA as a function of the flux threaded through the SQUID loop, controlled by _V_ DC. **b** Transmission with (red circles) and without JPA pump (black diamonds). **c** Phase-preserving gain in optimized settings. **d** Phase-sensitive gain. **e** Monitoring the phase-preserving gain set at _φ_ = _⇡/_ 2 overnight evidences a 8<sup>_◦_</sup> phase stability. Fast oscillations are due to the lab air conditioner system. **f** Finite dynamic range of the JPA. 

in the JPA flux line changes Φ and thus _!_ JPA, as seen in Fig. 5.6a, which allows tuning the JPA to the desired frequency _!_ 0. 

We set _!_ 0 _/_ 2 _⇡ ⇡_ 7 _._ 3 GHz. Turning on the JPA pump at _!p ⇡_ 2 _!_ 0 with power _P_ p, the previously flat reflexion coefficient now shows some amplification (see Fig. 5.6b). Taking the ratio of the transmissions with the pump on and off yields a Lorentzian gain curve, with a measured gain of 17 dB for these operating conditions. Fine tuning of the parameters ( _!p, P_ p _,_ Φ) allows to increase the device gain up to 26 dB within a bandwidth of 1.7 MHz (see Fig. 5.6c). 

Phase-sensitive amplification is measured by sending a continuous wave signal at _!_ 0 and setting _!p_ = 2 _!_ 0. Using the spectrum analyser, we record the output signal power with the JPA on and off, with the gain given as _G_ = _P_ out _/P_ out(JPAo↵). Fig. 5.6d shows the dependence of _G_ on the phase difference between the pump and signal tone, behaving as expected from Eq. 2.78 with deamplification for one quadrature and amplification by an extra 6 dB compared to the phasepreserving amplification for the other quadrature. 

The phase-stability of the setup and of the JPA is probed by monitoring overnight the gain in degenerate mode. The pump phase is chosen so that the phase-preserving gain lies around _G ⇡_ 0, so that the gain is maximally sensitive to phase changes (see green arrow in Fig. 5.6d). Fig. 5.6e shows overall phase drifts of 8<sup>_◦_</sup> , clearly due to temperature variations of the room-temperature cables and setup since 15 min oscillations synchronous to the air conditioner system can be seen. In the experiments, the gain is set to its maximal value, so that _G_ is only quadratically sensitive to phase shifts; 8<sup>_◦_</sup> drifts are then acceptable for our measurements. 

80 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 



<!-- Start of picture text -->
a<br>-24<br>signal pump idler<br>-36<br>-2 -1 0 1 2<br>�ω−ω p /2�/2π� (MHz)<br>b -20 c 5<br>JPA<br>4<br>-30 G<br>HEMT 3<br>-40 2<br>1<br>-50 RT amplifiers<br>0<br>10 20<br>-0.7 -0.6 -0.5 -0.4<br>�ω−ω p /2�/2π� (MHz)<br>Output<br>Power (dBm)<br>Output Power (dBm)<br>SNR<br><!-- End of picture text -->

FIGURE 5.7: **SNR enhancement** brought by the JPA as measured by a spectrum analyser. **a** Output power spectrum with acquisition bandwidth 100 kHz for a coherent signal sent at _!_ while the JPA is pumped at _!p ⇡_ 2 _!_ , evidencing signal and idler as well as the noise added by the JPA. **b** Zoom on the signal showing the rise of the noise level compared to amplification with the HEMT and compared to amplification with the room-temperature amplifiers. It evidences a reduction of the noise referred to the input of the amplification chain when turning on the JPA. **b** SNR as a function of the JPA gain. 

##### **Dynamic range** 

To measure the JPA dynamic range, we measure the gain as a function of the power of the incident signal in phase-preserving mode using the homodyne detection setup. Fig. 5.6f shows that the JPA provides a constant gain only for low input powers, with the 1 dB compression point lying at -132 dBm. Note that higher compression points have been obtained with different JPA designs and parameter choices [60, 52, 158] 

##### **Signal-to-noise ratio improvement** 

To characterize the signal-to-noise improvement brought by the JPA over the follow-up amplifiers, we perform measurements of the total output noise power in various configurations using a spectrum analyzer. With both JPA and HEMT switched off, we measure -52 dBm. Switching the HEMT on yields -43 dBm, indicating that the output noise is dominated by the HEMT noise and not by the room-temperature amplifiers. Then, switching the JPA on still yields a 13 dB increase in the noise, which confirms that the total output noise contribution is at 95% from the JPA, in agreement with our expectations based on Eq. 5.12. 

A more precise characterization of the SNR enhancement is done in the following way. A continuous microwave signal at frequency _!_ 0 is sent to the JPA. Fig. 5.7a shows the corresponding output power spectrum (red curve) with both signal and idler mode visible. The JPA gain is given once again as _G_ = _P_ out _/P_ out(JPAo↵) and is measured separately with a measurement bandwidth taken as small as possible to remove any contribution of the noise (in contrast to the data shown in Fig. 5.7a). The same experiment is then repeated without any input signal so as to obtain _P_ n, the noise power in 

81 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

the desired measurement bandwidth, chosen here to be 100 kHz. The amplitude signal-to-noise ratio is then evaluated by SNR = ~~p~~ Pout _/_ Pn and is shown in Fig. 5.7c. 

The SNR can be related to the JPA gain in the following way. Consider the noise referred at the output of the JPA: when the JPA is off, the noise arises from the HEMT, the room-temperature amplifiers (see Eq. 5.12) and from the signal noise. We denote this contribution as _n_ bg. For a gain _G_ , the JPA adds noise ( _G −_ 1) _n_ where _n_ = _n_ eq + _n_ amp. As the signal is amplified by _pG_ , the SNR expressed at the output of the JPA dependent on _G_ according to: 



Fig. 5.7c shows that the measured SNR follow this expected dependence. The fit does not allow us to determine independently _n_ and _n_ bg; however we obtain their ratio, _n_ bg _/n_ = 36, as observed in similar setups [159]. 

Absolute calibration of the mean photon number in the ESR resonator was performed in a later run (see Appendix A) and yields _n_ th = 0 _._ 05 _±_ 0 _._ 05, which confirms that the dominant contribution of noise in the setup is of quantum origin. 

### **5.3 Design of a superconducting ESR resonator with high quality factor and small mode volume** 

In the following, we describe the design of the high quality factor small-mode volume resonator needed to obtain a high sensitivity before describing its experimental implementation and characterization. 

#### **5.3.1 Design choices** 

##### **Small mode volume** 

As explained in ch. 3, the spin-resonator coupling is given by: 



where _|_ e _i_ and _|_ g _i_ are the energy levels spanning the ESR transition to be probed and **_δB_** is generated by the current fluctuations _δI_ in the resonator inductance. We have _δI_ = _!_ 0 ~~p~~ ~ _/_ (2 _Z_ 0), _Z_ 0 being the resonator impedance. Maximizing _g_ thus requires minimizing _Z_ 0 and bringing the spins as close as possible to the inductance. 

We thus choose to implant bismuth atoms very close to the surface (more precisely between 20 and 150 nm). One could also adopt a flip-chip configuration, where the sample containing the spins is stacked on top of the microwave resonator patterned on a different chip, but generally an incompressible gap of several hundreds of nanometers subsists at the interface. 

To minimize the resonator impedance, a **lumped-element geometry** is particularly suited since it can combine small inductors patterned in parallel with large **interdigitated capacitors** (see Fig. 5.8e); simulations indicate that impedances as low as 15 ⌦ can be reached. Even larger capacitances could be obtained by using conventional overlap capacitors, but they are in general more lossy than interdigitated capacitances [160]. 

82 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

##### **High-quality factor** 

In our quest for a high-quality factor resonator, it is indeed important to **minimize the resonator internal losses** , of associated damping rate __ int. The value reached for __ int is also key to determine the choice of the coupling rates __ 2 and __ 1 since it is best to operate in the critical coupling regime. Indeed, using Eq. 5.11, the setup sensitivity _N_ min can be shown to be maximum when __ 2 = __ int (assuming __ 1 _⌧ _ 2). 

Owing to intensive research in the superconducting qubits community, the origin of the internal losses of lumped-element interdigitated resonators are relatively well known. Resonators with internal quality factors in the 10<sup>6</sup> range have been obtained [161]. Four different physical phenomena leading to resonator internal losses have been identified : the motion of magnetic vortices trapped in the superconducting thin films [162], the presence of out-of-equilibrium quasi-particles (i.e., non-superconducting charge carriers) [163], dielectric losses in general [164], originating mostly from dirty interfaces and in particular from the substrate-metal interface which contributes the strongest [165], and finally radiation from the resonator [166]. The latter can be suppressed by enclosing the sample in a leak-tight metallic box, as shown in Fig. 5.8a [167]. The box is designed so that all its modes have frequencies well above the planar _LC_ resonator frequency. The best quality factors are obtained with superconducting boxes since losses through the box walls surface resistivity are then minimized [168]. However in the context of ESR measurements which necessitate to apply magnetic fields, we chose to have the box made of oxygen-free-high-conductivity copper. 

The coupling of the planar resonator to the measurement lines is obtained via **capacitive coupling to antennas** fed through holes drilled in the box (see Fig. 5.8a). The resulting coupling rates __ 1 and __ 2 are the sum of two contributions. The first one is a direct capacitive coupling of the resonator electrical dipole to the antenna while the second one is an evanescent coupling mediated via the first TE101 mode of the copper box (see Fig. 5.8c & d). As a result, the rates __ 1 and __ 2 are set by the position of each antenna relatively to the resonator as well as their coupling to the box mode. 

To control __ 1 and __ 2, the frequency and the quality factor of the copper box TE101 mode thus has to be carefully designed. The box mode quality factor should be kept low so as to be well below its internal quality factor. The internal quality factor of an OFHC copper box was found to be _⇡_ 6000; we thus limit ourselves to _Qbox _ 1000. The larger the detuning between the _LC_ resonator and the box TE101 mode, the weaker the coupling mediated by the box mode is. To obtain quality factors on the order of 10<sup>5</sup> for the _LC_ with _!LC/_ 2 _⇡ ⇠_ 7 _._ 4 GHz, we choose the dimensions of the box so that its lowest-frequency mode mode is at _!_ TE101 _/_ 2 _⇡_ = 8 _._ 9 GHz. 

To be able to adjust the coupling rates __ 1 and __ 2 to __ int at each run, we soldered the antennas on SMA throughs which are then screwed in the cavity wall (see Fig. 5.8a). Depending on the insertion of the SMA through in the wall, the antenna’s depth can be tuned over several millimeters, allowing to tune __ 1 and __ 2 by _⇡⇥_ 50. 

Finally, the resonator is made in a 50-nm-thick aluminum film. We chose this metal because it is wellestablished that aluminum resonators can have quality factors reaching at least 10<sup>6</sup> [161, 169, 170] and contrary to niobium films in particular, aluminum can be processed by lift-off techniques and removed by wet etchants which are harmless for the underlying silicon substrate. This is particularly important in our case given that the dopant atoms are very close to the surface. 

Since Si:Bi spins have a large zero-field splitting, several of the ESR transitions can still be tuned at resonance with a static magnetic field below the 10 mT critical field of bulk aluminum provided that the resonator frequency lies within 200 MHz of _!_ ZFS. In the future, to study the clock-transitions of bismuth located at larger magnetic field (see ch. 4) or other spin systems, materials sustaining higher fields while maintaining high-quality factors could be used. 

83 









<!-- Start of picture text -->
=|<br><!-- End of picture text -->



_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

|||Resona|tor A|Resona|tor B|Resona|tor C|Copp|er box|
|---|---|---|---|---|---|---|---|---|---|
|_lr_||730|µm|720|µm|710|µm|||
|_!_0|_/_2_⇡_|7.1915|GHz|7.2753|GHz|7.3332|GHz|8.52|GHz|
|__1|_/_2_⇡_|0.77|kHz|0.7|kHz|2.6|kHz|0.96|MHz|
|__2|_/_2_⇡_|16|kHz|5.8|kHz|24|kHz|8.1|MHz|



TABLE 5.2: **Simulated resonators characteristics.** 

#### **5.3.2 Electromagnetic simulations** 

The resonator geometry and coupling to the measurement lines are designed using electromagnetic simulations realized with CST 1.4 mm microwave studio. A modeling tool allows to reproduce the geom- <mark>5 µm</mark> etry of the copper sample holder (assuming perfect conductivity for the walls), the antennas, the substrate silicon chip (with relative dielectric constant _"r_ = 11 _._ 5) as well as the superconducting resonator (modeled by a perfect electrical conductor of zero-thickness), as shown in Fig. 5.8b. As the resonator is made of 50-nm-thick <mark>50 µm</mark> aluminum and has lateral dimensions _>_ 1 µm, kinetic inductance contribution is negligible [171] and is not included in the simulation. FIGURE 5.9: **Resonator layout** The sample holder and the resonator eigenmode frequencies can be determined in the software by exciting ports placed on the antennas and analyzing the frequency response, given as a _S_ -parameters matrix. 

The final geometry of the _LC_ resonator is a 5-µm-wide inductive wire of length _lr_ in parallel with an interdigitated capacitance of 12 50-µm-wide fingers spaced by 50 µm (see Fig. 5.9). The width and spacing of the fingers is chosen to minimize the dielectric losses [172]. The whole structure fits in a rectangle of 1 mm by 1.4 mm. The bismuth implanted silicon sample at our disposal is 1-cm-long and 3-mm-wide, we can thus multiplex our measurements by placing 3 resonators of slightly different frequencies, obtained by choosing three different values of _lr_ : 710, 720 and 730 µm. The resonators are separated by 1 mm and visualizing the simulated microwave electrical field (see Fig. 5.8e) shows that there is very little cross-talk between them. 

The simulated _S_ -parameters are shown in Fig. 5.8f. Four resonances are visible, with the highestfrequency one being the box TE101 mode (see Fig. 5.8c & d) and the lowest three the planar resonators (see Fig. 5.8e). Fitting the simulated S-parameters for each resonator to the input-output formulas (see Eq. 2.56), their frequency and coupling rates __ 1and __ 2 are extracted and given in Table 5.2 , with all resonators reaching quality factors above 10<sup>5</sup> . 

#### **5.3.3 Coupling to bismuth donor spins** 

To estimate the coupling constant of the resonator to spins, it is necessary to know the magnitude of the magnetic field vacuum fluctuations. We proceed in three steps, explained below in details. First we determine the resonator current fluctuations _δI_ from CST simulations; then, we compute the geometrical distribution of this current across the resonator inductance; finally, using the COMSOL magnetic field solver, we compute the magnetic field. For this last step a magnetostatic solver is sufficient since the length scales that come into play are very much smaller than the wavelength. 

To estimate _δI_ , we use CST to determine the magnitude of the AC current _I_ sim cos( _!_ 0 _t_ ) that flows through the resonator inductance for the simulated power _P_ in = 0 _._ 5 W. We find that _I_ sim = 60 A. Based on our knowledge of all the resonator _i_ (obtained from CST as explained above), we can 

85 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 



<!-- Start of picture text -->
a<br>ez<br>� B<br>eX<br>[Bi]<br>eY<br>0.1µm<br>8 1016 cm-3<br><!-- End of picture text -->



<!-- Start of picture text -->
 | � B|<br>10 20 30 (nT)<br>100 nm<br><!-- End of picture text -->

FIGURE 5.10: **Coupling between bismuth donor spin and LC resonator** . **a** LC resonator coupled to Bi donor spins with implanted profile of [137]; the directions correspond to the text. The spins are tuned to resonance via an in-plane static magnetic field **_B_** 0 forming an angle _✓_ with **_e_** _x_ and excited via an AC magnetic field **_δB_** orthogonal to the wire. **b** Spatial distribution of the current rms vacuum fluctuations flowing through the resonator, corresponding to an impedance of 44 ⌦. **c** rms vacuum fluctuations of the magnetic field generated by the current density of panel **a** . **d** _y_ (red) and _z_ (blue) components for the vacuum fluctuations of the magnetic field at _z_ = _−_ 100 nm. **e-g** Coupling strength distribution _⇢_ ( _g_ ), plotted as _g_<sup>2</sup> _⇢_ ( _g_ ), extracted from magnetic field simulations and evaluated with _γe_ = 28 GHz _/_ T and _|hi|S_<sup>ˆ</sup> _k|ji|_ = 0 _._ 5 for a _SX_ transition with _✓_ = 0 (panel **g** ) or _⇡/_ 2 (panel **f** ) as well as for a _SZ_ transition with _✓_ = _⇡/_ 2 (panel **e** ). Solid black line is the contribution from all spins whereas red (blue) line is the contribution from spins located under (outside) the wire with _|y| <_ 2 _._ 5 µm ( _|y|_ > 2 _._ 5 µm). 

86 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

derive the mean photon number corresponding to _P_ in using Eq. 2.55. This allows us to extract _δI_ as: 



corresponding to a resonator impedance _Z_ 0 = 44 ⌦. 

The current distribution over the cross-section of a superconducting wire (see Fig. 5.10b) is given by the following formulas [173]: 



In these expressions _y_ is the wire transversal coordinate indicated in Fig. 5.10a, _wr_ = 5 µm is the wire width, _b_ = 50 nm is its thickness and _λ_ = 90 nm is the penetration depth of the aluminum _wr/_ 2 film [174]. The normalization constant _δJ_ (0) is determined by the condition R _−wr/_ 2<sup>_δJ_(</sup><sup>_x_)</sup><sup>_dx_=</sup><sup>_δI_.</sup> 

We finally use _δJ_ ( _y_ ) to compute **_δB_** 0( _r_ ), using the COMSOL magnetostatic solver. The result is shown in Fig. 5.10c. The field **_δB_** ( **_r_** ) is located in the plane perpendicular to the resonator wire axis ( _δBx_ ( **_r_** ) = 0), and importantly Fig. 5.10d shows that it is essentially along **_y_** for spins under the wire, and essentially along **z** for spins outside the wire. 

In our experiment, the static magnetic field **_B_** 0 is applied parallel to the surface (see Fig. 5.10a) along an axis **_e_** _Z_ that can be decomposed along the orientations defined in Fig. 5.10a as: 



The field **_δB_** ( **_r_** ) can be decomposed in either basis: 



For Eq. 5.14 applied to bismuth donors, the coupling constant for a spin located at **_r_** = ( _x, y, z_ ) is thus: 



where _|ii_ and _|ji_ are two of the twenty energy levels of bismuth donors. A bismuth donor in silicon possesses both _S_<sup>ˆ</sup> _x_ transitions probed by an AC magnetic field transverse to **_B_** 0 and _S_<sup>ˆ</sup> _z_ transitions probed by an AC magnetic field parallel to **_B_** 0 (see ch. 4). Eq. 5.19 can be simplified in both cases: 

- For _Sx_ transitions, as _|hi|S_<sup>ˆ</sup> _X |ji|_ = _|hi|S_<sup>ˆ</sup> _Y |ji|_ and _|hi|S_<sup>ˆ</sup> _Z|ji|_ = 0, we have: 



- For _Sz_ transitions, as _|hi|S_<sup>ˆ</sup> _X |ji|_ = _|hi|S_<sup>ˆ</sup> _Y |ji|_ = 0, we have: 



A spin located outside the wire ( _|y|_ > _wr/_ 2) is probed by a microwave field essentially along **_z_** ( _δBy ⇡_ 0) and thus its coupling to the resonator is only possible for a _SX_ transition. In addition, the coupling does not depend on _✓_ since **_B_** 0 is in any case orthogonal to **_δB_** . 

87 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

In contrast, a spin located below the wire ( _|y|_ 6 _wr/_ 2) is probed by a microwave field essentially along **_y_** ( _δBz ⇡_ 0). As a result, the coupling to a _SX_ transition is maximum when _✓_ = 0 and fully suppressed when _✓_ = _⇡/_ 2, whereas the coupling to a _SZ_ transition is suppressed when _✓_ = 0 but maximum for _✓_ = _⇡/_ 2. 

The coupling distribution for both transition types is computed using the bismuth implantation profile and the **_δB_** ( **_r_** ) map and shown in Fig. 5.10e for a matrix element taken arbitrarily at 0.5 for easy comparison. We show in red the contribution from spins located under the wire ( _|y| < wr/_ 2) and in blue the contribution from spins located outside the wire. 

#### **5.3.4 Experimental implementation** 

##### **Fabrication** 

To obtain a high internal quality factor resonator, dielectric losses should be minimized. Lossy dielectrics are found most notably at the metal-substrate interface; our fabrication process thus tries to keep it as clean as possible. In particular it has been demonstrated that oxygen plasma cleaning before metal deposition is essential to reduce the losses [175]: 

- **Substrate cleaning** : 2 hours in a Piranha acid mixture at 80<sup>_◦_</sup> C, followed by 5’ in acetone before rinsing with isopropanol and blowing dry. 

- **Resist coating** : bi-layer MAA(200 nm) - PMMA(100 nm) with a 7-nm-thick aluminum layer deposited by metal evaporation for charge evacuation during the E-beam lithography. 

- **E-beam lithography** : the entire pattern is drawn with a 25keV electron beam in 15’. 

- **Resist development** : 30” in MF-319 to remove the Al layer, before developing the resist with a 40” dip in MIBK (dilution 2:1). Rinse in water and blow dry. 

- **Mask cleaning** : 1’ in an oxygen plasma asher. The plasma parameters were chosen so that it corresponds to the etching of 6-nm of the PMMA layer. 

- **Metal deposition:** 50 nm of Al are deposited via a Plassys evaporator at a rate of 1 nm/s. 

- **Lift-off** : 5’ in acetone before rinsing in isopropanol and blowing dry. 

Other solutions to reduce the contribution of TLS is to deeply etch the substrate using the metallic resonator as a mask [176]. Doing so removes the TLS lying underneath the edges of the metal where the electrical field is the strongest and thus where the TLS contribute the most. However such a solution would damage our substrate permanently. 

##### **Sample mounting and microwave setup** 

After fabrication, the chip is inserted in the copper box by gluing it to a sapphire plate with small amounts of vacuum grease. The sapphire plate is then glued in the copper box sample groove, also using vacuum grease (see Fig. 5.8a). The copper box is closed using an indium seal to ensure good electrical contact between both parts and reduce losses. Finally, the copper box is mounted in a couple of orthogonal Helmholtz coils that provide a 2D static magnetic field **_B_** 0 (see Fig. 5.11) up to 10 mT each. 

The final step to ensure a high-quality factor is to protect the superconducting thin films from losses occurring through out-of equilibrium quasi-particles and vortices. Low-pass filters containing infra-red absorptive material are put on each line to minimize the quasi-particles (see Fig. 5.4b). The Helmholtz coils are inserted in a 1-mm-thick cryoperm magnetic shielding to minimize stray 

88 



<!-- Start of picture text -->
Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity<br>mixing chamber plate<br>magnetic shielding<br>ey<br>Helmholtz B<br>0x<br>B<br>0<br>e<br>z<br>e<br>x<br>copper box<br>Helmholtz B<br>0y<br>FIGURE 5.11: LC within its sample holder mounted inside a couple of Helmholtz coils<br>magnetic field which may introduce vortices in the film during cool down of the film through its<br>critical temperature.(see Fig. 5.11).<br>Microwave characterization<br><!-- End of picture text -->

The characterization of the _LC_ resonators is carried out in two steps. In the first step, we use two extra microwave lines (see Fig. 5.4b) to measure all _S_ -parameters and determine without ambiguity __ 1 and __ 2. The fit of the measured _S_ 21, _S_ 11 and _S_ 22 to the input and output formulas given in Eqs. 2.57 & 2.56 is shown in Fig. 5.12 for resonator _B_ and the extracted values for __ 1 and __ 2 are given in Table 5.3. The values are found to be approximately a factor 2 higher than estimated by the CST simulations (see Table 5.2), meaning that the antennas are inserted a little deeper in the copper box than in the simulation. Similar results are obtained for resonators _A_ and _C_ . 

In what follows, we use the simplified setup shown in black in Fig. 5.4b, without the extra microwave lines used for measuring the complete resonator S-parameters. Using only the transmission from port 1 to port 2, we then can only determine the resonator frequency _!_ 0 and total damping rate __ ; using the previously determined values of __ 1 and __ 2 yields __ int. The measured values for _!_ 0, __ and __ int determined in this setup and used in the following chapters are given in Table 5.3 for the three resonators. All resonators are in the critical coupling regime, with _Q_ int _⇡_ 2 _Q ⇡_ 5 _⇥_ 10<sup>5</sup> . 

Contrary to most usual ESR spectrometers, our ESR resonator has in addition a response in magnetic field. When ramping the parallel static magnetic field applied on the resonator by one of the Helmholtz coils (see Fig. 5.13), the resonator quality factor remains flat whereas the frequency of the resonator decreases quadratically by nearly 1 MHz due to the increase of the thin-film kinetic inductance, with in addition sudden jumps that we attribute to magnetic vortices entering the film. We measured the critical field of the Al resonators to be _⇡_ 14 mT for a parallel magnetic field. The dependence of the resonator in _B_ 0 thus requires us to systematically fit the resonator transmission at each _B_ 0 to determinate its frequency. 

89 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 



<!-- Start of picture text -->
1 1<br>0.5<br>0 0 0<br>π π<br>π/2<br>-π/2<br>-π -π<br>7.2457 7.2458 7.2457 7.2458 7.2457 7.2458<br>Frequency (GHz) Frequency (GHz) Frequency (GHz)<br>|11 |22 |21<br>|S |S |S<br>)11 )22 )21<br>arg(S arg(S arg(S<br><!-- End of picture text -->

FIGURE 5.12: **Characterization of** _!_ 0 **,** __ 1 **and** __ 2 for resonator _B_ .by measuring _S_ 21, _S_ 11 and _S_ 22 with the VNA. 

||Reso|nator A|Resonator B|Resonator C|
|---|---|---|---|---|
|_!_0_/_2_⇡_|7.14|GHz|7.246<br>GHz|7.305<br>GHz|
|__1_/_2_⇡_|2.1|kHz|2.1<br>kHz|5.7<br>kHz|
|__2_/_2_⇡_|31|kHz|9.2<br>kHz|50<br>kHz|
|_Q_|1_._4|_⇥_10<sup>5</sup>|3_._2_⇥_10<sup>5</sup>|1_._1_⇥_10<sup>5</sup>|
|_Q_int|4_._0|_⇥_10<sup>5</sup>|6_._4_⇥_10<sup>5</sup>|6_._8_⇥_10<sup>5</sup>|



TABLE 5.3: **Measured ESR resonator characteristics** with coupling values agreeing within a factor 2 to the simulated values. The copper box mode cannot be measured since at 20 mK its frequency lies outside the circulator range. 

##### **Internal losses** 

We have investigated experimentally the mechanisms at the origin of _Q_ int in our experiment. If the dielectric losses are dominant due to TLS lying at the metal-substrate interface, the internal quality factor is expected to be significantly lower when measured for powers corresponding to intra-resonator photon number ¯ _n ⇠_ 1 than at high-powers when the TLS are saturated. We indeed measure a factor 2 reduction of _Q_ int at low powers (see Fig. 5.14a), indicating that dielectric losses contribute for half of the total internal losses. 

Fig. 5.14b shows that _Q_ int can be improved if a non-zero magnetic field is applied while the Al film is undergoing its metal to superconductor transition. This indicates that there is a small residual magnetic field orthogonal to the field which creates vortices in the film; its compensation thus reduces the number of vortices and improves _Q_ int [162]. 



<!-- Start of picture text -->
1.5<br>1.0<br>-0.2<br>-0.4<br>-0.6<br>-0.8<br>4 6 8 10<br>Magnetic field B0 (mT)<br>)<br>5<br>Q (x 10<br>(0)] (MHz) ω�<br>�ω - �<br><!-- End of picture text -->

FIGURE 5.13: **Resonator** _A_ **response to an applied magnetic field parallel to the resonator wire** 

To conclude, future improvements of _Q_ int will take place by simultaneously reducing dielectric losses, improving the magnetic shielding and removing any 

90 

_Chapter 5. Design and realization of a spectrometer operating at the quantum limit of sensitivity_ 

magnetic material close by the cavity and increasing the infra-red filtering. 



<!-- Start of picture text -->
a 106 b 107<br>105<br>6<br>10<br>10 -1 10 0 10 1 10 2 10 3 10 4 10 5 -1.5 -1 -0.5 0 0.5<br>Mean intra-resonator photon number  n Cooling magnetic field (mT)<br>tot<br>Q<br>,  int<br>int  Q<br>Q<br><!-- End of picture text -->

FIGURE 5.14: **Internal quality factor dependence** on **a** the intra-resonator photon number, indicating that dielectric losses contribute for half of the internal losses; **b** Parallel magnetic field applied during the Al transition to superconductor using one of the Helmholtz coils. A possible misalignement of the mechanical parts probably gives rise to a small orthogonal component of unknown amplitude responsible for the compensation of the stray magnetic field. The blue line is a polynomial fit to _!_ 0 _/Q_ int. 

91 

## **Chapter 6** 

# **ESR spectroscopy of Bismuth donors in silicon** 

In this chapter, we characterize the Si:Bi spins using our setup. The sample we are using was already studied by Weis et al.[137] with a conventional ESR spectrometer at 25 K (see 4.6). We first detail the experimental implementation of Hahn-echo pulse sequences in our setup, before presenting results on Si:Bi. Last, we measure the Si:Bi relaxation times. 

### **6.1 Hahn-echo detected ESR** 

In all that follows, the spin signal is obtained by spin echoes generated via Hahn-echo sequences _⇡/_ 2 _− ⌧ − ⇡ − ⌧_ . We briefly outline here the main experimental specificities of our home-made high quality factor low-temperature spectrometer. 

#### **6.1.1 Experimental techniques** 

##### **Pulse generation** 

The first requirement is to be able to send microwave drive pulses to the spins with a sufficient on/off ratio. The microwave setup of Fig. 5.5 modified to generate microwave pulses is shown in Fig. 6.1. The pulses are shaped by microwave switches with an on/off ratio of 80 dB, in series with the microwave source internal switch, which only allows square-shaped pulses to be sent. The relative phases of the pulses are set by the analog phase modulation of the microwave source. All the control pulses are generated by an arbitrary waveform generator (AWG5014 from Tektronix). 

Two pulses of different powers can be generated using two switches in parallel, each in series with a variable attenuator. By proper calibration of the microwave lines in our setup, we can estimate the power incident on the ESR resonator _P_ in with an accuracy of 1 dB. In this setup we can deliver pulses of power _P_ in up to _−_ 50 dBm. 

##### **Echo acquisition** 

The transmitted pulses and the echo signals are demodulated at _!_ 0 and their _I_ and _Q_ quadratures are detected using the setup shown in Fig. 5.5. To suppress residual DC offsets and drifts on the _I_ and _Q_ channel, every pulse sequence is repeated twice with opposite phases on the excitation pulse _R±✓_ . This phase cycling protocol yields two echo signals with opposite phases taken in the same conditions. The DC offset is then removed by taking the difference between the two time-traces acquired on each sequence. The acquisition by the digitizer is also triggered by the AWG. 

92 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
a b<br>AWG generator ω π/2x πy echo<br>p<br>to JPA pump<br>� �<br>Phase<br>Modulation AWG control signals<br>ω Pulse 2<br>0<br>Pulse 1<br>Trigger acquisition<br>I<br>to LO<br>Q MW JPA pump<br>MW phase modulation<br>echo MW internal switch<br>12 mK<br>JPA ω<br>p<br>µW switch<br>�2<br>dB dB<br>10 dB ��<br>P<br>to ESR resonator in<br>π π/2<br>Gate<br>Gate<br>Pulse 1<br>Pulse 2<br><!-- End of picture text -->

FIGURE 6.1: **Pulsed ESR implementation. a** Two independent microwave pulses can be generated via two microwave switches in parallel, each being in series with a tunable attenuator to control the pulse input power _P_ in referred to port 1 of the resonator. The pulses’ phases are set via phase modulation of the microwave source. All signals are controlled via an AWG generator. **b** Control signals for a Hahn-echo sequence. The JPA is switched on only during the echo emission. 

We also switch the JPA on only during the echo emission by pulsing the pump signal via the microwave source internal switch. This is done to minimize the cryostat heating due to the pump signal. The JPA is set for most of the data shown in the following chapter in phase-preserving mode with a gain _G ⇡_ 20 dB. To ensure that the idler mode is properly filtered out, we take _!p/_ 2 _− !_ 0 = 500 kHz and we set the detection bandwidth to be 100 kHz. 

#### **6.1.2 Hahn-echo sequence** 

Before moving on to the ESR spectroscopy, we first examine a single Hahn-echo sequence acquired with resonator _B_ . The transition _|_ 9 _i $ |_ 10 _i_ is tuned at resonance by applying a magnetic field **_B_** 0 _⇡_ 5 mT. A _⇡/_ 2 pulse of power _P_ in and duration _t⇡/_ 2 = 2 _._ 5 µs followed _⌧_ = 300 µs later by a _⇡_ pulse of same power _P_ in but of duration _t⇡_ = 5 µs leads to the emission of an echo at time 2 _⌧_ . The calibration of the power _P_ in for the _⇡/_ 2 and _⇡_ pulses is realized by performing Rabi oscillations, as will be explained in the following. 

Fig. 6.2 shows the recorded amplitude for such a sequence. The output amplitude shows the two drive pulses, followed after a time 2 _⌧_ by an echo emitted by the spins. The drive pulse shape, far from being square as the input pulse, appears asymmetric with a long-time exponential decay, due to filtering by the resonator. The echo shape, of duration _TE ⇡_ 50 µs, is also not Gaussian, due to the convolution of the spin response with the drive pulses and the resonator filtering. The _I_ and _Q_ quadratures of the echo are shown in the inset of Fig. 6.2, evidencing that the echo lies on a single quadrature. In the following, we quantify the echo signal using either its integrated amplitude _Ae_ 

93 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
t π /2 t π 0.1 T E<br>1<br>�<br>0<br>-0.1<br>620 660<br>0<br>0 100 200 300 400 500 600 700<br> Time (µs)<br> (V)<br>Q A,<br> (V) I,<br> A<br><!-- End of picture text -->

FIGURE 6.2: **Hahn-echo sequence.** Recorded amplitude, showing the _⇡/_ 2 and _⇡_ pulses (green lines indicates the microwave switch control pulses) with their long ESR resonator-induced decay. At time 2 _⌧_ , an echo of duration _TE_ is detected, with its quadratures _I_ and _Q_ and amplitude shown in inset. (The data in the inset is different from the blue points by a factor 3 in the averaging.). Data taken with resonator _B_ at _B_ 0 = 5 _._ 13 mT, with JPA off to avoid its saturation by the control pulses. 

or its integrated quadrature _AQ_ defined as: 



where _I_<sup>˜</sup> ( _t_ ) is either the _I_ (or _Q_ ) quadrature if the demodulation local oscillator phase was set so that the echo is emitted solely on _I_ (or _Q_ ). It may also be the result of a post-acquisition numerical rotation: _I_<sup>˜</sup> ( _t_ ) = _I_ ( _t_ ) cos _'_ + _Q_ ( _t_ ) sin _'_ , where _'_ is chosen so that all signal lies on _I_<sup>˜</sup> ( _t_ ). 

#### **6.1.3 Rabi oscillations** 

To calibrate drive pulses, we measure Hahn-echo detected Rabi oscillations. For that, we apply a Hahn-echo sequence in which the tipping angle _✓p_ of the refocusing pulse is varied, either by sweeping _tp_ or _P_ in (see Fig. 6.3a). This results in the appearance of oscillations in the echo integrated signal, as shown in Fig. 6.3b-d. 

Indeed, consider the same spin ensemble as in 5.1.2, divided in spin subsets whose frequency is distributed according to a distribution _⇢_ (∆). An ideal _⇡/_ 2 applied around the _x_ -axis at time _t_ = _−_ 2 _⌧_ creates a transversal magnetization state aligned on the _y_ -axis (see Eq. 5.3). The evolution of each spin subset ( _j_ ) of detuning ∆ _j_ at times _−_ 2 _⌧_ 6 _t < −⌧_ is: 



94 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 





<!-- Start of picture text -->
0 A (V) 0.12<br><!-- End of picture text -->



FIGURE 6.3: **Rabi oscillations. a** Rabi oscillations can be performed by varying either the amplitude or the duration of the refocusing pulse. **b** They lead to the appearance of oscillations in the integrated echo amplitude _Ae_ (red shade in **a** ) whose well-defined frequency yields _g_ (see text). Data was acquired with _t⇡/_ 2 = 2 _._ 5 µs and _tp_ = 5 µs. **c** Rabi oscillations performed by sweeping _P_ in leading to long-subsisting Rabi oscillations whereas Rabi oscillations performed by sweeping _tp_ ( **d** ) vanishes due to bandwidth mismatches. All data were acquired with resonator _B_ at _B_ 0 = 5 _._ 13 mT and _✓_ = 0. 

Applying a pulse of tipping angle _✓p_ around the _y_ -axis at time _t_ = _−⌧_ leads to the following evolution at times _t_ > _−⌧_ for each spin subset: 



Assuming that the tipping angle is identical for all spin subsets, one can show that the transverse magnetization at time _t_ = 0 is: 



If 2 _⌧ ≫ T_ 2<sup>_⇤_, the sums P</sup> _j_<sup>sin(2∆</sup><sup>_j⌧_) and P</sup> _j_<sup>cos(2∆</sup><sup>_j⌧_) average to zero and as a result the spin echo</sup> signal is proportional only to: 



which describes the oscillations pattern that can be seen directly in the integrated echo signal (see Fig. 6.3a), allowing to determine the set of parameters _P_ in and _tp_ corresponding to a _⇡_ pulse. 

##### **Link between** _✓p_ **and** _g_ 

The precise relation between the tipping angle _✓p_ , the incident power _P_ in and the spin-resonator coupling constant _g_ can be worked out by considering the action of the intra-resonator field on the spins. For a coherent square pulse of duration _tp_ applied at time _t_ = 0 at resonance on port 1 of the ESR resonator, the intra-resonator field evolution is given using Eq. 2.52 by: 





_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 

(see Fig. 6.2 & 6.4), where _n_ ¯ is the steady-state intra-resonator photon number linked to _P_ in by _n_ ¯ = 4 __ 1 _P_ in _/_ (~ _!_ 0 __<sup>2</sup> ) (see Eq. 2.53). The integrated field amplitude is: 



The resulting action of the excitation microwave field **_B_**<sup>ˆ</sup> 1 = **_δB_** (ˆ _a_ + ˆ _a_<sup>_†_</sup> ) on the spins is given using Eqs. 3.41-3.44. In the semi-classical limit, for spins at resonance the rotation induced by a coherent ˆ drive is given by _!_ 1( _t_ ) = 2 _gha_ ( _t_ ) _i_ . As a result, the spins undergo a Rabi oscillation of angle: 



Fig. 6.3a shows very well-defined oscillations taken with resonator _B_ , which show that _✓p_ = _⇡_ is obtained for _tp_ = 5 µs with _P_ in = 1 _._ 9 _±_ 0 _._ 2 pW. Using the relation between _P_ in and _n_ ¯ and the measured damping rates values given in Table 5.3, we can estimate _g/_ 2 _⇡_ = 50 Hz _±_ 7 Hz, a value in good agreement with the estimate given in 5.3.3. The precision on _g_ is set by the 1 dB accuracy on _P_ in. 

In addition, the fact that well-defined oscillations are observed is a first clear indication that the spins are coupled with a narrow _g_ distribution to the resonator. Otherwise, each spin subset of coupling _gj_ would experience a different tipping angle _✓p,j_ . The measured Rabi oscillations would then be a sum of oscillations largely spread in frequency and would thus lead to their averaging for large tipping angles. 



##### **Bandwidth issues** 

So far we have considered only spins at resonance. However, we will see below that in our experiment the ESR linewidth is considerably broader than the resonator linewidth. As a result, the pulse, whose bandwidth is eventually limited by the resonator, excites only a fraction of the spins. Indeed, the power response function _R_ ( _!_ ) of a pulse of length _tp_ incident on a resonator with bandwidth __ at resonance is expressed as: 



For pulses of length _tp ≫_ 2 _/_ , the excitation linewidth is set by the pulse length ∆ _!/_ 2 _⇡ ⇡_ 1 _._ 2 _/tp_ , whereas when _tp ⌧_ 2 _/_ the linewidth is set by __ (see Fig. 6.4a & b). On the latter case, the spins excitation profile would have the same bandwidth were they a linear system. For large tipping angles such an approximation is impossible, since the Rabi frequency varies in ⌦ _R_ = ~~q~~ ( _! − !_ 0)<sup>2</sup> + ⌦<sup>2</sup> _R,_ 0 that makes an angle _✓_ in the _x_ - _z_ plane, with tan _✓_ = ( _! − !_ 0) _/_ ⌦ _R,_ 0 (see ch. 3). Therefore, the larger is ⌦ _R,_ 0, the weaker is the tipping angle inaccuracy for spins whose frequency lies within the resonator bandwidth. The exact excitation profiles can be computed using the Bloch equations and are shown in Fig. 6.4c for a _⇡_ tipping angle and considering different ratios of _tp_ . Their bandwidths appear similar to the corresponding pulse bandwidth and scale with the Rabi frequency ⌦ _R,_ 0, or equivalently with the power _P_ in<sup>1</sup><sup>_/_2.</sup> 

96 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
a b c<br>hai ℛ(𝜔) 1 Spin excitation  1 tp = 25<br>profile<br>t  = 5<br>1 p<br>t  = 1<br>p<br>t  = 0.2<br>p<br>tp t −2 0 2 ω/κ −2 0 2 ω/κ<br><!-- End of picture text -->

FIGURE 6.4: **Pulse bandwidths. a** Normalized temporal and **b** spectral response for a square pulse of duration _tp_ incident on a resonator of bandwidth __ . **c** Spin excitation profile for a _⇡_ pulse applied with different values of the ratio _tp_ . 

In principle, the refocusing pulse bandwidth of the Hahn-echo sequence should exceed the excitation pulse bandwidth for the refocusing to be efficient. Otherwise, the spins whose frequency lies within the excitation pulse bandwidth and therefore contribute to the echo signal are refocused by different tipping angles leading to an averaging in the measured echo signal. This is illustrated in Fig. 6.3b-c, where Rabi oscillations are performed by sweeping either the pulse power _P_ in or the refocusing pulse length _tp_ . The Rabi oscillations performed by sweeping _tp_ appear less robust than those performed by sweeping _P_ in with less oscillations being visible, due to their weaker Rabi frequency. In the following we mainly use short pulses sequences with _tp ⇠_ 1 such as shown in Fig. 6.2. 

### **6.2 Strain-broadened transitions** 

Several ESR transitions can be tuned at resonance with the three resonators patterned on the Si:Bi chip with a magnetic field _B_ 0 below the aluminum bulk critical field. The corresponding _B_ 0 and matrix elements for all three resonators are given in Table. 6.1. We recall that, as explained earlier, an interesting feature of bismuth donor spins is that they possess both _Sx_ transitions that can be probed with a **_B_** 1 field perpendicular to **_B_** 0 and _Sz_ transitions that are probed via a **_B_** 1 field parallel to **_B_** 0. In the following, we present spectroscopic measurements of these transitions. 

|||Reson|ator C|Reson|ator B|Reson|ator A|
|---|---|---|---|---|---|---|---|
|Transitions|Type|_B_0 (mT)|Mat. El.|_B_0 (mT)|Mat. El.|_B_0 (mT)|Mat. El.|
|_|_9_i $ |_10_i_|_Sx_|2.84|0.47|5.18|0.47|9.24|0.47|
|_|_9_i $ |_11_i_|_Sz_|3.20|0.30|5.85|0.30|||
|_|_8_i $ |_11_i_<sup>_⇤_</sup>|_Sx_|3.67|0.42|6.71|0.42|||
|_|_8_i $ |_12_i_|_Sz_|4.30|0.41|7.88|0.41|||
|_|_7_i $ |_12_i_<sup>_⇤_</sup>|_Sx_|5.19|0.37|9.56|0.37|||
|_|_7_i $ |_13_i_|_Sz_|6.56|0.46|||||
|_|_6_i $|_13_i_<sup>_⇤_</sup>|_Sx_|9.00|0.32|||||



TABLE 6.1: **Expected ESR transitions** below Al critical field for resonators A, B, C. Transitions _|ii $ |ji_ noted with (<sup>_⇤_</sup> ) are doubly-degenerate with the corresponding transition _|i_ + 1 _i $ |j_ + 1 _i_ (see ch. 4). In the table and in all the text, we denote them using the transition _|ii $ |ji_ . Since the sum of both matrix elements is 0.5, only the matrix element corresponding to _|ii $ |ji_ is given. 

97 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
2<br>a b<br>ESR<br>resonator<br>1<br>1.0 θ=0 P1<br>P2 10 1.2<br>0.5 0.8<br>8<br>0.4<br>0<br>6 0.0<br>1.0 𝜃= 𝜋/2<br>P2 P 4<br>3<br>0.5<br>2<br>P P P<br>0 1 2 3<br>0<br>2.6 2.8 3.0 3.2 0 40 80 0 40 80 0 40 80<br>Magnetic Field B0 (mT) �  (°) �  (°) �  (°)<br>c d e f<br>z<br>B1 B1 B1<br>Al wire x y y y y<br>B0 B0 B0<br>x � x � x �<br>|9〉↔|10〉<br>B<br>1<br>|9〉↔|11〉<br>0<br>g<br>)/<br>� ( g<br>(V)e<br>(V)<br>e<br>1/2 Echo signal A<br> (pW)<br>1/2<br>Echo signal A in<br>P<br><!-- End of picture text -->

FIGURE 6.5: **First** _Sx_ **and** _Sz_ **ESR transitions** for resonator C. **a** Frequency and power compensated echo-detected field sweep for resonator _C_ with _✓_ = 0 and _✓_ = _⇡/_ 2. The black line on top indicates the resonator linewidth as well as the transition linewidth measured by Weis et al. [137]. **b** Rabi oscillations as a function of _✓_ at magnetic fields _P_ 1, _P_ 2 and _P_ 3 indicated with black points in panel **a** . The color axis is the averaged echo amplitude _Ae_ . Above the color-plots are extracted the ratio _g_ ( _✓_ ) _/g_ 0 (circles, squares and diamond) from the Rabi oscillations, where _g_ 0 is taken to be _g_ ( _✓_ = 0) for _P_ 1 and _P_ 2 but _g_ ( _✓_ = _⇡/_ 2) for _P_ 3. The solid lines give the expected variation (see text). **c** . Schematic of **_B_** 1 for spins located under and outside the Al wire. **d-f** Schematic depicting the relative orientations of **_B_** 1 and **_B_** 0 as a function of _✓_ while probing peak _P_ 1 (panel **d** ), peak _P_ 2 (panel **e** ) and peak _P_ 3 (panel **f** ). 

#### **6.2.1 Doublet-shaped transitions** 

We start with the measurements performed using resonator _C_ , whose frequency is closest to the zero-field splitting. Using a Hahn-echo sequence such as shown in Fig. 6.2, we record the echo signal _Ae_ as a function of _B_ 0. Applying a magnetic field parallel to the superconducting resonator increases the film kinetic inductance which decreases the resonator frequency as seen in ch. 5. As a consequence, at each _B_ 0, the resonator transmission is measured, fitted, and the microwave source adjusted to this frequency, using an automated routine; after that the echo sequence is run as explained earlier. The power of the excitation and refocusing pulses are calibrated via Rabi oscillations to ensure they correspond to _⇡/_ 2 and _⇡_ pulses for each _B_ 0. We also set the repetition rate well below the spin energy relaxation rate. 

Fig. 6.5a shows the data for _✓_ = 0 around the magnetic field _B_ 0 = 2 _._ 84 mT expected for the first _Sx_ encountered _Sx_ transition _|_ 9 _i ! |_ 10 _i_ . The line appears much broader than observed by Weis et al. [137] with its FWHM linewidth being ∆ _B_ 0 = 200 µT _≫_ 12 _._ 2 µT. It is also considerably broader than the ESR resonator linewidth (which corresponds to _⇡_ 3 µT in magnetic field units). In addition, the line appears to be split: two well-defined asymmetric peaks appear on each side of the expected _B_ 0 field. Such a line splitting has never been reported so far in Si:Bi samples, most remarkably 

98 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 

in measurements performed on the exact same sample in a conventional ESR spectrometer. We denote _P_ 1 ( _P_ 2) the low-field (high-field) peak, and we discuss the origin of this doublet shape in the following. 

To complement these data, we perform the exact same measurements but with _✓_ = _⇡/_ 2, (pink curve in Fig. 6.5a). _P_ 1 is seen to be fully suppressed, whereas _P_ 2 remains unchanged. The spins contributing to _P_ 1 are thus not excited anymore when _B_ 0 is orthogonal to the wire, while _P_ 2 spins are probed identically. In addition, a new peak (noted _P_ 3) is visible, at a magnetic field _B_ 0 close to the one expected for the _|_ 9 _i ! |Sz_ 11 _i_ transition, with a linewidth similar to the other peaks but remarkably without visible splitting. 

To account for these experimental facts, our hypothesis is that the peaks _P_ 1 and _P_ 3 arise from spins located under the Al wire, probed by an excitation field **_B_** 1 mainly aligned on _y_ (see Fig. 6.5c). When _✓_ = 0, **_B_** 0 is orthogonal to **_B_** 1 (see Fig. 6.5d) and thus the spins can only contribute to _|_ 9 _i ! |Sx_ 10 _i_ (i.e. _P_ 1); in reverse when _✓_ = _⇡/_ 2, **_B_** 0 is parallel to **_B_** 1 (see Fig. 6.5f) and thus the spins can only contribute to _|_ 9 _i !Sz |_ 11 _i_ (i.e. _P_ 3). In contrast, spins located outside the wire are probed via an excitation field **_B_** 1 mainly aligned on _z_ (see Fig. 6.5c), and thus whatever the orientation of **_B_** 0 they systematically contribute to _|_ 9 _i ! |Sx_ 10 _i_ (i.e. _P_ 2) but never to the _|_ 9 _i ! |Sz_ 11 _i_ transition. 

In order to test this hypothesis, we measure the Rabi oscillation frequency for varying angles _✓_ . As explained in ch. 5, we expect different angular dependence of _g_ (see Eqs. 5.20 & 5.21) on _✓_ : 

- for a _Sx_ transition, for spins located under the wire as _g_ ( _✓_ ) _/_ cos( _✓_ ) 

- for a _Sx_ transition, for spins located outside the wire as _g_ ( _✓_ ) = _g_ (0) 

- for a _Sz_ transition, for spins located under the wire as _g_ ( _✓_ ) _/_ sin( _✓_ ). 

and thus the Rabi-oscillations frequency should follow the expected 1 _/g_ ( _✓_ ) dependence. Fig. 6.5b shows the results. Very different angular dependences are indeed observed for the 3 peaks. On the _P_ 1 peak, a 1 _/_ cos _✓_ dependence is found, while _P_ 3 has a 1 _/_ sin _✓_ dependence and _P_ 2 does not depend on _✓_ ; this confirms our hypothesis for the peaks identification. 

#### **6.2.2 Rabi frequency dependence on** _B_ 0 

According to our previous discussion, there appears to be a correlation between the spins Larmor frequency and their spatial location with respect to the resonator. Further insight in this direction is obtained by doing systematic measurements of the Rabi frequency as a function of _B_ 0 along the spectroscopy peaks. Fig. 6.6 shows the Rabi oscillations performed for transition _|_ 9 _i ! |Sx_ 10 _i_ for resonator _B_ with _✓_ = 0: the recovered echo amplitude _Ae_ is color-coded and plotted as a function of the refocusing power _P_ in and the magnetic field _B_ 0. The overall amplitude of the oscillations (shown in the top panel of Fig. 6.6) resembles the lineshape already observed with resonator _C_ , showing two very asymmetric peaks. The most remarkable feature however is the fact that the frequency of the Rabi oscillations (see Fig. 6.6) shows a pronounced and non-trivial dependence on _B_ 0. 

Our interpretation of the observed dependence of _g_ on _B_ 0 is based on the fact that _g_ is proportional to the amplitude of the **_B_** 1 field generated by the resonator, which itself depends on the spatial position relative to the resonator wire (see for instance Fig. 5.10 in ch. 5). As already discussed for the explanation of the two-peak structure of the line, we are thus led to the conclusion that the spin Larmor frequency is somehow correlated to their location relative to the resonator wire. From our knowledge of **_B_** 1( **_r_** ), we can go further and actually assess that within the _P_ 1 peak, "low-field" spins are located closer to the wire edge where **_B_** 1 is strongest (i.e. _|y|_ just below _wr/_ 2) whereas "high-field" spins are located in the middle of the wire (i.e. _|y| ⌧ wr/_ 2); for the _P_ 2 peak on the 

99 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
P<br>1 P<br>2<br>P in<br>2 τ τ<br>π /2 echo<br>1<br>0<br>eEcho signal A(V)<br><!-- End of picture text -->

FIGURE 6.6: **Rabi oscillations as a function of** **_B_** 0 for transition _|_ 9 _i !Sx |_ 10 _i_ taken with resonator _B_ and _✓_ = 0. The amplitude of the refocusing pulse in the Hahn-echo sequence is varied to reveal oscillations in the integrated echo signal _Ae_ . The frequency of the oscillations allows to extract the spin-resonator coupling _g_ ( _B_ 0). On top is shown the frequency and power compensated ESR spectrum, evidencing the same doublet-shape than resonator _C_ . 

other hand, "low-field" spins are located far from the wire where **_B_** 1 becomes vanishingly small (i.e. _|y| ≫ wr/_ 2) whereas "high-field" spins are closer to the wire edge (i.e. _|y|_ just above _wr/_ 2). 

Thus the physical mechanism that explains the line broadening causes the spins located near the edge of the aluminum wire to be far offset from their expected Larmor frequency, with positive detuning for the spins lying below the edge of the wire ( _|y| < wr/_ 2), and negative detunings for the spins located on the side of the edge of the wire ( _|y| > wr/_ 2). Spins located either far from the wire or underneath its center lie closer in frequency to the expected ESR transition. 

While we have not yet provided an explanation for the underlying physical mechanism causing this effect, we can already note a beneficial consequence for our experiments. Since the resonator line is much narrower than the overall spin distribution, we can effectively choose to drive and measure ensembles of spins with very different couplings to the resonator simply by changing _B_ 0. In particular, we can work with ensembles of spins with a coupling constant to the resonator that is much better defined than in the absence of the line broadening mechanism, where the Rabi oscillation pattern would in fact be an average over all Rabi frequencies observed in Fig. 6.6 and thus lead to much less precise Rabi angles. 

100 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 





<!-- Start of picture text -->
Si:Bi<br><!-- End of picture text -->



FIGURE 6.7: **Induced strain.** Diagonal strain tensor component _"_ yy experienced by the donors as a result of thermal expansion coefficient mismatch between silicon and the aluminum inductive wire, obtained via finite element simulation realized with COMSOL Multiphysics. 

#### **6.2.3 Induced strain, a likely suspect** 

Clearly, the physical mechanism responsible for these phenomena has to be linked to the presence of the aluminum wire on top of the substrate. A thorough and quantitative analysis was performed by J. Pla and will be reported in [177]; as it is not the main topic of this thesis we will only briefly summarize its main conclusions in the following. 

The mechanisms at the origin of the broadening could be either: 

- **Magnetic field inhomogeneities:** _B_ 0 could have a spatial dependence originating from its expulsion from the superconducting thin films forming the resonator, due to the Meissner effect. However such inhomogeneities would be proportional to the applied magnetic field. As a similar or even slightly narrower linewidth is measured for resonator _B_ and _C_ for the _|_ 9 _i ! |Sx_ 10 _i_ transition, this mechanism can be ruled out. 

- **Built-in electric fields:** the aluminum/silicon interface beneath the resonator forms a Schottky barrier which could lead to frequency shifts of the donor spin resonance. However induced electrical fields would only induce a Stark shift of the hyperfine interaction or electron _γe_ -factor, altering only quadratically the spin frequency. As we observe simultaneously positive and negative detunings, we can also rule out this mechanism. 

- **Induced strain** . As aluminum and silicon have different coefficients of thermal expansion, cooling the device from room-temperature to 20 mK induces strain in the silicon. As discussed in ch. 4, strain can induced both hyperfine interaction shift as well as quadrupolar effects. While we can rule out broadening due to the hyperfine interaction, quadrupolar interaction is a likely candidate that can provide both positive and negative detunings [111] as observed in our experiment. 

We thus retain only the latter hypothesis. Through finite elements simulations, the strain in the vicinity of the wire at 20 mK can be computed as shown in Fig. 6.7. The subsequent modification of the donor wave-functions _A_ 1, _E_ and _T_ 2 is computed using an effective mass theory model [109]. As explained in ch. 4, the modification of the fully symmetric _A_ 1 ground state reduces the hyperfine coupling _A_ ( _"_ ) 6 _A_ (0), but from the simulations only a small shift of the order of 0.8 µT is estimated. 

The quadrupolar interaction, while zero in absence of stress, arises via the mixing of _A_ 1 with the nonsymmetric _E_ xyz state that induces a non-zero electrical field gradient (EFG). Linking the quadrupolar factor **_Q_** involved in the quadrupolar Hamiltonian (see Eq. 4.28) to the EFG accurately is non-trivial, due to the very complex structure of the donor and is the object of a detailed discussion in [177]. In 

101 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
a<br>7.36<br>θ=0<br>7.34 𝜃= 𝜋/2<br>7.32<br>C<br>7.30<br>7.28<br>7.26<br>B<br>7.24<br>b 7.36<br>Simulation<br>7.34<br>7.32<br>7.30<br>7.28<br>7.26<br>7.24<br>3 4 5 6 7 8<br>Magnetic Field B0 (mT)<br>|6〉↔|13〉<br>|9〉↔|10〉|9〉↔|11〉 |8〉↔|11〉 |8〉↔|12〉 |7〉↔|12〉 |7〉↔|13〉<br>Frequency (GHz)<br>Frequency (GHz)<br><!-- End of picture text -->

FIGURE 6.8: **Measured and simulated field ESR spectroscopy** for resonator _B_ and _C_ . Top (bottom) panel corresponds to the frequency and power compensated echo-detected field sweep while the bottom panel corresponds to simulations described in the main text (extracted from [177]). Dashed grey lines indicate the resonator frequencies, while the light green (purple) lines indicate the _Sx_ ( _Sz_ ) transitions, with the notations of Table. 6.1 given in grey. Resonator _A_ is not shown, but similar results are obtained _Sx_ for transition _|_ 9 _i ! |_ 10 _i_ . 

particular, a significant part of the imprecision arises from the Sternheimer anti-shielding effect [178]. This phenomenon describes the re-arrangement of the inner electron shells in response to an external EFG, with a resulting enhancement of the total EFG experienced by the nucleus. **_Q_** is thus multiplied by a factor that can be considerable ( _⇡⇥_ 46 for Bi<sup>5+</sup> ions [179]) but that is undetermined up to now for Si:Bi donors. In the following an extra proportional correction on **_Q_** is added as a fitting parameter to include this effect. Once the quadrupolar Hamiltonian is estimated (see Eq. 4.28), the expected transition shift can be computed by adding the quadrupolar term to the Si:Bi Hamiltonian of Eq. 4.8. 

At each point ( _x, y, z_ ) of the sample relative to the wire, one can thus estimate via the strain simulation the expected ESR spectrum. The global expected ESR spectrum can thus be modeled by summing all spins contributions, weighted according to the implantation profile of the bismuth 

102 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
a Inversion Readout<br>π T π /2 π echo<br>t<br>b AQ ( T )<br>π /2<br>Q quadrature (V)<br>c<br>0<br>T=0<br>-0.5<br>1<br>0.5<br>T=T1 ln 2 0 0<br>-0.5<br>1 -1 T 1= 0.35±0.1 s<br>T=<br>0 1 2 3<br>π /2 0 Delay  T  (s)<br>20 40 60<br>Time (µs)<br>)<br>=<br>( TQ<br>A<br>) /<br>( TQ<br>A<br><!-- End of picture text -->

FIGURE 6.9: **Inversion recovery. a** The sequence consists in sending a large bandwidth _⇡_ pulse to invert the spins. After a delay _T_ , the remaining polarization is measured via a Hahn-echo sequence. **b** At very short times ( _T_ = 0), the echo measured on a single quadrature ( _Q_ for instance) has the opposite sign than at times _T ≫ T_ 1. **c** The integrated quadrature signal _AQ_ as a function of the delay _T_ is well-fit by an exponential (red solid line) yielding _T_ 1 = 0 _._ 35 s. 

atoms extracted by SIMS (see Fig. 4.12) and to the coupling constant _g_ extracted from the simulation of the **_δB_** 

The results of the full ESR spectroscopy of resonators _B_ and _C_ as well as the simulated ESR lineshapes is shown in Fig. 6.8. While the model fails to account precisely for the peak broadening and the asymmetry of the _Sz_ transitions, it does capture most of the features of the ESR spectroscopy, such as the _Sx_ peak splitting and the _✓_ -dependence. The best match between experimental data and simulations required a correction factor of 400, it would be very interesting to test this determination using other configurations. Nevertheless, we can conclude that quadrupolar effects due to strain induced in the silicon by the aluminum wire is a very likely mechanism for the overall peak broadenings observed in our experiment. 

### **6.3 Relaxation times** 

We now characterize the relaxation and coherence times of the sample. For this purpose, we concentrate on the transition _|_ 9 _i ! |Sx_ 10 _i_ tuned at resonance with resonator _B_ by applying _B_ 0 = 5 _._ 13 mT and _✓_ = 0. 

#### **6.3.1 Energy relaxation** 

We first measure the energy relaxation time _T_ 1 using inversion-recovery [5] as described in Fig. 6.9. Starting from thermal equilibrium, a 5-µs-long _⇡_ pulse is sent at resonance to invert the spin polarization, after which the magnetization decays by _T_ 1 processes back to thermal equilibrium. To 

103 

_Chapter 6. ESR spectroscopy of Bismuth donors in silicon_ 



<!-- Start of picture text -->
1.0<br>0.4<br>τ τ AQ ( T ) 0.5 01 5 10<br>π /2 �π echo (2n+1) �π y<br>x y<br>T  = 8.9 ms<br>0.0 2<br>0 20 40<br>Time, 2 �  (ms)<br>=0)  (kHz)2<br>�<br>(<br>Q 1/T<br>A<br>) /<br>�<br>(<br>Q<br>A<br><!-- End of picture text -->

FIGURE 6.10: **Decoherence times.** As the total time 2 _⌧_ between the initial _⇡/_ 2 pulse and the echo is increased, the recovered quadrature signal _AQ_ ( _⌧_ ) decays with an exponential behavior (red curve is a fit), yielding a spin coherence time _T_ 2 = 8 _._ 9 ms. When the bandwidth of the refocusing pulse is increased, the decoherence time _T_ 2 decreases (see inset), indicating that the decoherence mechanism is partly due to instantaneous diffusion. 

readout the remaining polarization after a time _T_ , we employ once again a Hahn-echo sequence, with a shorter bandwidth than the excitation pulse ( _t⇡_ = 100 µs). At times _T ≫ T_ 1, the measured spins have relaxed back to equilibrium, and thus a steady-state echo is recorded, yielding _AQ_ ( _T_ = _1_ ). At time _T_ = 0, the polarization is fully inverted, thus the _⇡/_ 2 pulse of the Hahn-echo sequence projects the magnetization vector on the opposite direction compared to the steady-state situation so that the echo signal _AQ_ ( _T_ = 0) has the opposite sign than _AQ_ ( _T_ = _1_ ). The _T_ 1 relaxation is thus observed by measuring the decay from _AQ_ ( _T_ = 0) to _AQ_ ( _T_ = _1_ ). For resonator _B_ at _B_ 0 = 5 _._ 13 mT and _✓_ = 0, the decay is exponential with a characteristic time _T_ 1 = 0 _._ 35 s, as shown in Fig. 6.9c. 

The shortness of this measured time compared to the values obtained in the literature at even higher temperatures (see 4.4.1) is due to the Purcell effect induced by the high quality factor resonator, as will be explained in ch. 8. 

#### **6.3.2 Coherence times** 

As already explained in ch. 4, the decoherence time _T_ 2 is characterized in ESR measurements by sweeping the delay time 2 _⌧_ between the initial _⇡/_ 2 pulse and the echo emission. Fig. 6.10 shows such a measurement for resonator _B_ at _B_ 0 = 5 _._ 13 mT and _✓_ = 0, well fitted by an exponential decay of characteristic time _T_ 2 = 8 _._ 9 ms. Whereas this value is characteristic of the long coherence times readily obtained for donors in isotopically purified silicon samples, it is nevertheless surprisingly long given the sample concentration. Indeed, measurements performed by Weis et al. [137] on the same sample report _T_ 2 = 500 µs, more than an order of magnitude shorter than the data in Fig. 6.10. 

Our interpretation of this discrepancy is as follows. In Weis et al. measurements, _T_ 2 was shown to be limited by instantaneous diffusion, caused by the unwanted spin flips of the neighboring Si:Bi donors upon the application of the refocusing _⇡_ pulse. In our experiment however, due to the strain-induced line broadening discussed earlier and to the narrow resonator bandwidth, the _⇡_ pulses address only a small subset of the entire spin ensemble, which could lead to much less pronounced instantaneous diffusion effects thus explaining the longer _T_ 2 measured. In order to test this idea, we have performed _T_ 2 measurements using higher refocusing pulse powers, leading to higher Rabi frequencies and thus larger number of spins being flipped. As qualitatively expected, we see a reduction in _T_ 2 (see inset of Fig. 6.10), which we have however not attempted to account for quantitatively. To conclude, it seems likely that our measured coherence time is at least partly limited by instantaneous diffusion, as is often the case for measurements on ensembles of donors [126, 124]. 

104 

## **Chapter 7** 

# **Spectrometer sensitivity** 

In this chapter, we estimate the sensitivity _N_ min of our spectrometer defined as the number of spins that can be detected with a single Hahn-echo for a signal-to-noise ratio of 1. We first determine the number of spins contributing to the signal, and we measure the SNR of an echo; this yields a sensitivity of 2000 spins detectable with SNR= 1 in a single echo sequence. We also demonstrate how CPMG sequences can be used to enhance further the sensitivity by a factor _⇡_ 10. 

### **7.1 Determining the number of spins** 

We define the number of spins contributing to the echo signal _N_ spins as the number of spins excited by the _⇡/_ 2 pulse. We estimate _N_ spins using resonator _B_ and concentrating on the low-field peak of transition _|_ 9 _i $ |_ 10 _i_ tuned at resonance with _B_ 0 = 5 _._ 13 mT by two methods detailed in the following. 

#### **7.1.1 Direct counting of the donors** 

A first method to evaluate the number of spins consists in using our knowledge of the bismuth atoms implantation profile to count the number of atoms in the detection volume. Let us call _N_ tot the number of spins contributing to the low-field peak of transitions _|_ 9 _i $ |_ 10 _i_ . As the resonator linewidth is considerably smaller than the ESR linewidth (see Fig. 7.1), only a small fraction of the spins _N_ spins = _⇠N_ tot contributes effectively to the signal. The _⇡/_ 2 pulse of the Hahn-echo sequence shown in Fig. 6.2 being 5 µs long, we make the assumption that it excites spins with a frequency response similar to the resonator response (see 6.1.3) and thus _⇠_ is approximately given by: 



where _⇢_ LC( _!_ ) = 1 _/_ (1 + 4( _! − !_ 0)<sup>2</sup> _/_<sup>2</sup> ) is the ESR resonator spectral response and _⇢_ ESR( _!_ ) is the spins density profile. 

To determine _⇢_ ESR( _!_ ), we use the measured spin-echo line and more precisely we will focus on the low-field peak ( _P_ 1) which has the advantage of corresponding to a well-defined detection volume: the spins located exactly below the resonator wire. The measured spin-echo amplitude _Ae_ ( _B_ 0) does not provide directly the spin density _⇢_ ESR, because, as explained earlier, the spin-resonator coupling is _B_ 0-dependent, which leads to a slight distortion of the curve since the detected signal is itself proportional to _g_ . Thus, _⇢_ ESR is proportional to _Ae_ ( _B_ 0) _/g_ ( _B_ 0). _B_ 0 is converted to _!_ units using the the _|_ 9 _i $ |_ 10 _i_ transition frequency dependence on _B_ 0. The spectrum computed using the ESR data acquired for resonator _B_ and normalized using R _⇢_ ESR( _!_ ) _d!_ = 1 is shown in Fig. 7.1a. At 

105 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
resonator<br>0.4<br>N<br>sim<br>0.2<br>N<br>tot<br>0. 0<br>-10 -5 0<br>( ω-ω 0)/2 π  (MHz)<br>)( ω ESR<br>ρ<br><!-- End of picture text -->

FIGURE 7.1: **Estimation of the number of spins.** The spin density profile _⇢_ ESR( _!_ ) (red circles) is extracted from measuring _Ae_ ( _B_ 0) and _g_ ( _B_ 0) to be compared to the resonator bandwidth (dark blue). The grey shade indicates _N_ tot the total number of spins comprising the low-field peak of transition _|_ 9 _i $ |_ 10 _i_ and the blue shade indicates _N_ num the number of spins comprising the spin ensemble numerical model. 

field _B_ 0 = 5 _._ 13 mT, using the resonator linewidth determined in Table 5.3, we find from Eq. 7.1 _⇠ ⇡_ 1 _._ 6 _⇥_ 10<sup>_−_2</sup> . 

To go further we need to evaluate the total number of spins _N_ tot. We estimate _N_ tot using the implantation profile [Bi](z) measured by SIMS by Weis et al. (see section 4.6 and [137]) by: 



where _wr_ and _lr_ are the wire dimensions. A factor 1 _/_ 9 is added since we are probing via the transition _|_ 9 _i $ |_ 10 _i_ only one of the 9 ground states of Si:Bi that we assume to be equally populated at 20 mK. We find _N_ tot = 4 _._ 7 _⇥_ 10<sup>6</sup> . 

This estimate can be refined by considering that the number of spins may be less than the number of implanted atoms for the following reasons. First, as explained in ch. 4, only 60% of the implanted atoms become converted as donors following the post-implant annealing, as measured by Weis et al. [137]. 

Second, the aluminum thin-film deposited directly on top of the silicon substrate can give rise to a Schottky barrier in which donors may be ionized (see Fig. 7.2). The difference in the work function of aluminum and silicon causes a band-bending responsible for the ionization of the donors over an area called the depletion region. A simple model to estimate the depth of the depletion region is to make the full-depletion assumption[180]. In this model, the donors are assumed to be ionized on a depth _zd_ and neutral for _z_ > _zd_ : 



where _ND_<sup>+(</sup><sup>_z_) is the number of ionized donors.To determine</sup><sup>_zd_, one has then to solve the Poisson</sup> equation: 



106 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
Ef φ Al<br>Aluminium e -e e -- e - 0<br>[Si:Bi]<br>depletion region<br>85 nm<br>Silicon<br>φ Si<br>z<br>E E<br>D C<br>-3<br>16  cm<br>8.10<br>+ +<br>+<br>+<br><!-- End of picture text -->

FIGURE 7.2: **Schottky barrier** at the aluminum-silicon interface. A bending of the valence and conduction band of silicon is observed due to the work function difference _φ_ Al _− φ_ Si between aluminum and silicon. It is responsible for the ionization of the donors in the _depletion region_ of depth 85 nm in our sample. 

with _⇢_ ( _z_ ) = _eND_<sup>+(</sup><sup>_z_),takingasboundaryconditionthattheelectricalfield</sup><sup>_E_=</sup><sup>_−d_</sup> dz<sup>_<u>φ</u>_iszerofor</sup> _z_ > _zd_ . Solving numerically _φ_ ( _zd_ ) _− φ_ (0) = _φ_ Si _− φ_ Al yields _zd ⇡_ 85 nm for _φ_ Si _− φ_ Al = 0 _._ 5 V [181]. Re-evaluating [Bi](z) using this estimate and taking into account the limited yield, we obtain _N_ tot _⇡_ 1 _._ 5 _⇥_ 10<sup>6</sup> and thus: 



#### **7.1.2 Estimate based on numerical simulations** 

To determine more accurately _N_ spins, we simulate numerically a Hahn-echo sequence and extract the number of spins excited by the _⇡/_ 2 pulse, using the model described in ch. 3 and [77, 78, 182]. The spin ensemble is divided into _M_ sub-ensembles where each subset ( _m_ ) contains _Nm_ spins with subset-dependent coupling constant _gm_ and detuning to the resonator ∆ _m_ = _!m − !_ 0. The spinresonator dynamics can then be simulated by integrating numerically the equations of motion (see Eqs. 3.41-3.44) for the resonator field and the spins collective components of all of the sub-ensembles. We use for this purpose a Matlab code developed by our collaborator Brian Julsgaard. 

As input to the simulation, we use the relaxation and decoherence times measured experimentally. An important point for our sensitivity analysis is to determine precisely the size _Nm_ of each subset. For this purpose, we use the numerical simulations to reproduce the time-dependent absorption of a microwave pulse, whose rich features are better suited than a simple echo sequence to assess the model accuracy. 

##### **Modeling** 

While in our experiment strain induces a correlation between a spin frequency and its spatial position and thus its coupling to the resonator (see ch. 5), we make the assumption that the spectral window and thus spatial window probed by the resonator is narrow enough to neglect this correlation. The spin-ensemble is then simply modeled by the joint distribution of a coupling constant distribution _⇢_ ( _gi_ ) and a spin detuning distribution _⇢_ (∆ _j_ ) of total number of bins _Mg ⇥ M_ ∆. The two-dimensional distribution is weighted so that the sum of all the sub-ensembles ( _i, j_ ) contains _g M_ ∆ P<sup>_M_</sup> _i_ =1 P _j_ =1<sup>_Ni,j_=</sup><sup>_N_numspins.</sup> 

107 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
a b<br>0.04<br>0.02 0.002<br>0.02<br>1<br>0<br>48 56 64<br>0.01<br>0<br>0 0<br>60 80 100 120<br>-200 -100 0 100 200<br>g/2 π�� Hz � ( ω j -  ω 0) /2 π  (kHz)<br>�<br>�� g  )  j<br>�<br>(<br>�<br>Resonator Transmission<br><!-- End of picture text -->

FIGURE 7.3: **Spin ensemble modeling a** Coupling constant distribution extracted from **_δB_** ( **_r_** ) simulations for _|y| < wr/_ 2 weighted by the ionized spin concentration _z_ -profile and normalized to unity (red line). The black circles show the discrete distribution used in the simulation, with _Mg_ = 50. In inset is shown the equivalent Gaussian distribution. **b** Tilted square distribution used in the simulation, with _M_ ∆ = 450. The blue line indicates the resonator linewidth. 

**Determining the coupling constant distribution** As the measurements we would like to reproduce were performed with the magnetic field _B_ 0 aligned along the wire, on the low-field peak _P_ 1 of the transition _|_ 9 _i $ |_ 10 _i_ , the _g_ distribution is extracted, similarly to section 6.1.3, from the simulation of **_δB_** ( **_r_** ) for spins under the wire ( _|y| < wr/_ 2) with a _Sx_ transition matrix element _h_ 9 _|S_<sup>ˆ</sup> _x|_ 10 _i_ = 0 _._ 47, taking into account the ionized spin concentration profile. The peak of the distribution now lies at _g/_ 2 _⇡_ = 56 Hz, close to the value determined experimentally by Rabi oscillations (see Fig. 6.3). We choose a discrete distribution with irregularly spaced _Mg_ = 50 bins, as shown in Fig. 7.3a. 

Simulations done in this chapter use this as-extracted distribution. Note that later on, in ch. 9, we simulate the spin-echo at two different magnetic fields within _P_ 1 and thus probe spin subsets with different Larmor frequency that have a different mean coupling constant _g_ 0 (see ch. 6). To capture the difference in _g_ when modeling the two different spin subsets, we simplify the as-extracted distribution in a Gaussian distribution centered on _g_ 0 with a width ∆ _g_ that is phenomenologically adjusted. 

**Determining the spin frequency distribution** Simulating sequences as long as 1 ms requires a small bin size for the spin frequency distribution; we choose 1 bin per 1 kHz, over a 450 kHz range. The resonator linewidth being two orders of magnitude smaller than the spin linewidth, the zero-order approximation would be to assume a square spin frequency distribution. We nevertheless introduce a tilted square distribution to take into account more precisely the shape of the line, as shown in Fig. 7.3b. The relative slope is derived from _⇢_ ESR( _!_ ). 

**Spin-decoherence rate and energy relaxation rate** Spin decoherence is treated by including both a spin dephasing rate _γ?_ = 1 _/T_ 2 and a spin energy decay rate _γk_ = 1 _/T_ 1. We use the experimental measured coherence time _T_ 2 = 9 ms (see Fig. 6.10). The energy relaxation rate, on the other hand, is due to Purcell relaxation (as will be explained ch. 8). As a result, spins detuned from the cavity have a longer relaxation rate. This is captured by defining for each sub-ensemble: 



108 

_Chapter 7. Spectrometer sensitivity_ 

Since _γ? ≫ γk_ , the introduction of _γk_ is only important for describing the initial state of the ensemble. Indeed, every experimental sequence is repeated several times at rate _γ_ rep (with _γ_ rep<sup>_−_1</sup><sup>_⇡_3 to 10 s)</sup> and the results are then averaged. This waiting time _γ_ rep<sup>_−_1islongenoughcomparedto</sup><sup>_T_1tobe</sup> neglected for spins at resonance, however detuned spins have a longer _T_ 1 and thus do not fully relax between two consecutive sequences, contributing less to the signal than spins at resonance. To take into account this effect, we define an effective initial polarization _Sz_<sup>(</sup><sup>_i,j_)</sup> ( _t_ = 0) for a sub-ensemble depending on its relaxation time: 



**Resonator and drive parameters** The ESR resonators parameters __ 1, __ 2, __ int and _!_ 0 are taken equal to the measured values (see Table 5.3). We make the assumption that all drives pulses are sent at resonance. The incident power _P_ in is assumed identical to the value determined experimentally within a 1-dB-error margin. 

##### **Absolute calibration of the spin density** 

The only free parameter in the model is thus the absolute scaling factor _N_ num, whose exact determination is crucial to estimate the number of spins excited during the Hahn-echo sequence. To calibrate _N_ num, we measure the time-dependent absorption by the spins of a 500-µs-long pulse of power _P_ in, as shown in Fig. 7.4a. The data are shown in Fig. 7.4b for unsaturated spins, and in **Fig.8.4c** for saturated spins. When the spins are not saturated, the transmitted pulse shows two prominent features that should be precisely reproduced by the simulations: the Rabi oscillation transients at the beginning, which are characterized by an oscillation frequency ⌦ _R_ , a decay time and an initial amplitude, and the FID of the spins which gives rise to the emission of a microwave signal even after the resonator field has decayed (see Fig. 7.4a). For comparison, and to provide the scaling factor between numerical and experimental data, the transmission of a second pulse _P_ sent right after a strong microwave saturating pulse is also recorded. The sequence is acquired 1000 times with a repetition time _γ_ rep<sup>_−_1= 5 s.</sup> 

We perform a numerical simulation of this experiment using the model described above. We find that for the as-extracted _g_ -distribution, _N_ num = 2 _._ 0 _⇥_ 10<sup>5</sup> gives a good agreement with the FID decay as well as the Rabi oscillations amplitude. To obtain the accurate Rabi oscillation frequency, we had to scale _P_ in by a factor 1 _._ 1. By adjusting only those two independent parameters, the spin absorption data is quantitatively reproduced (solid colored lines in Fig. 7.4b&c), which validates the model to estimate the number of spins contributing to the signal<sup>1</sup> . 

**Comparison with the atom-counting estimate** We can use the absolute scaling determined numerically to evaluate the total number of spins _N_ tot that contribute to the low-field ESR peak _P_ 1. As the absolute scaling _N_ num is evaluated for spins lying in a bandwidth ∆ _!/_ 2 _⇡_ = 450 kHz (see Fig. 7.1), we have: 



where _⇢_ ESR( _!_ ) is the spins spectrum determined from the ESR spectroscopy as explained in section . We find _N_ tot = 1 _._ 2 _⇥_ 10<sup>6</sup> , a value in very good agreement with the estimate _N_ tot = 1 _._ 5 _⇥_ 10<sup>6</sup> given by the "atom-counting" method. 

> 1In the case of a Gaussian _g_ -distribution, the parameters _g/_ 2 _⇡_ = 56 Hz, ∆ _g_ = 1 _._ 5 Hz and _N_ num = 1 _._ 8 _⇥_ 105 with _✏_ = 0 _._ 85 gives a less but still correct agreement to the experimental data, with the Rabi oscillations damping not being entirely captured (dashed line in Fig. 7.4b) 

109 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
a period<br>amplitude decay witness<br>P 1/2<br>in<br>FID 3 T 1<br>time<br>b c<br>0.6 0.6<br>n =4.9x10 4<br>n =1.5x10 4<br>0.4 0.4<br>n =4.9x10 3<br>n =1.5x10 3<br>0.2 0.2<br>n =4.9x10 2<br>0.0 0.0<br>0 500 0 500<br>Time (µs) Time (µs)<br> Transmitted Amplitude (V)  Transmitted Amplitude (V)<br>pulse<br>saturating<br><!-- End of picture text -->

FIGURE 7.4: **Time-dependent absorption. a** Experimental sequence consisting of a first 500-µs-long pulse at power _P_ in, followed by a strong microwave pulse immediately followed by a second 500-µs-long at same power _P_ in to remove the spins contribution. **b-c** Absorbed and saturated pulses taken with average number of photons _n_ ¯ for the intra-resonator field, rescaled to the same amplitude as for the curve corresponding to _n_ ¯ = 4 _._ 9 _⇥_ 10<sup>3</sup> (green) with additional offsets and averaged 1000 times. Open circles: data. Solid-lines: numerical fit with as-extracted _g_ -distribution. Black dashed line: numerical fit with Gaussian _g_ -distribution. 

##### **Reproducing a Hahn-echo sequence** 

We now simulate the full echo-sequence, keeping exactly the same model parameters. The input power of the simulated _⇡/_ 2 and _⇡_ pulses are calibrated by simulating Rabi oscillations. We find that in the simulation the _⇡_ pulse power is only 1 dB away from the experimental one, which further confirms the validity of our model. 

The spin echo sequence was acquired with the JPA off, in order to avoid its saturation by the drive pulses. The output amplitude is scaled by comparing the theoretical and experimental decay of the two excitation pulses. With only this adjustment factor the simulated echo is found to be in quantitative agreement with the experimental data as shown in Fig. 7.5. 

To evaluate the number of spins excited during the spin-echo sequence, we extract from the simulation the time-dependent mean spin polarization _hS_<sup>ˆ</sup> _zi_ , as shown in Fig. 7.5. We consider more particularly that the quantity _hS_<sup>ˆ</sup> _z_ ( _t > ⇡/_ 2) _i −hS_<sup>ˆ</sup> _z_ ( _t_ = 0) _i_ is a direct estimate if the number of spins excited by the Hahn-echo sequence. We find<sup>2</sup> _N_ spins = 1 _._ 2 _⇥_ 10<sup>4</sup> , confirming our previous estimate of _⇠ ⇡_ 1 _._ 6 _⇥_ 10<sup>_−_2</sup> . We thus come to the conclusion that _N_ spins participate to the echo shown in Fig. 7.5. 

> 2Using the Gaussian _g_ -distribution, we find a similar number _N_ spins = 1 _._ 1 _⇥_ 104 

110 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
0.1<br>1<br>0.0<br>0.60 0.64 0.68<br>Time (ms)<br>�π /2 �π echo<br>x y<br>0<br>40<br>20<br>0<br>-60<br>-80<br>-100 + 1.2 10 4<br>-120<br>0.40<br>0.35<br>0.30<br>0.25<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>Time (ms)<br>Amplitude (V)<br>3)<br>(x 10<br>y<br>,<br>x<br>3)(x 10<br>z<br>2<br>ˆ Y<br>,<br>2<br>ˆ X<br><!-- End of picture text -->

FIGURE 7.5: **Hahn-echo sequence simulation** . (Top) The simulated Hahn-echo sequence (red lines) lies on top of the recorded experimental echo sequence (blue points) taken without JPA to avoid any saturation effect and reproduces quantitatively the data. (Middle panels) Collective spin components _hSki_ =<sup>P</sup> _m_<sup>_hS_</sup> _k_<sup>(</sup><sup>_m_)</sup> _i_ extracted from the simulation. The component _hSzi_ is used to determine the number of spins _N_ spins excited during the _⇡/_ 2 pulse. (Bottom) Resonator field quadrature variances evidencing that 30% extra-noise is added during the spin-echo sequence due to spin spontaneous emission. 

111 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
a 5 b 1.5<br>4<br>1.0<br>3<br>0.5<br>2<br>0.0<br>1<br>0 -0.5<br>5 10 15 20 0 20 40 60 80 100<br>Time (µs)<br> (V)<br>I<br>SNR<br><!-- End of picture text -->

FIGURE 7.6: **Single-echo signal-to-noise ratio** . **a** Echo SNR dependence on JPA gain (blue circles), with error bars given in the text. Red-dashed line shows the JPA’s SNR for a coherent signal, rescaled to these data, showing that the spin-echo signal-to-noise increases as expected from the earlier characterization of the JPA, until saturation. **b** Echo signal _I_ ( _t_ ) averaged 10 times without JPA (grey), with JPA in nondegenerate mode (orange), with JPA in degenerate mode (red). The grey ( _⇥_ 38, SNR=2 _±_ 0 _._ 5) and orange curve ( _⇥_ 2 _._ 2, SNR=14 _±_ 1) were rescaled to the red (SNR=22 _±_ 3) for easy comparison. 

### **7.2 Characterization of the sensitivity** 

#### **7.2.1 Single-echo signal-to-noise ratio** 

To obtain the setup sensitivity, we also need to characterize the SNR of a single echo. We study the SNR for various JPA gains, using the homodyne detection setup and the JPA in phase-preserving mode. We evaluate separately the signal and the noise by the following procedure. First, we choose the local oscillator phase so that the echo lies entirely on the _I_ quadrature. We then average 10 spin-echo signals yielding the averaged time-traces _I_ ( _t_ ) from which we compute the signal using only a simple top-hat integration window such that: 



The noise is determined from 500 traces of the same duration acquired without any echo being triggered (microwave drive pulses turned off) as: 



As shown in Fig. 7.6a, the resulting SNR= _S/N_ follows the same dependence on the JPA gain as determined using only the JPA. For the JPA in phase-preserving mode, at the optimal SNR value, the single-echo SNR (orange curve in Fig. 7.6b) is increased by a factor _⇡⇥_ 7 compared to a single-echo acquired with only the HEMT (grey curve in Fig. 7.6b) and reaches SNR= 4. 

We now use the JPA in phase-sensitive (degenerate) mode, with the pump phase chosen so that the _I_ quadrature which is aligned with the echo is amplified. As the gain increases by 6 dB while only increasing the noise power by 3 dB, the SNR is expected to increase by a factor _p_ 2 compared to the non-degenerate mode of the JPA. We find experimentally a factor 1.7, probably due to the fact that when the JPA is operated in phase-preserving gain, the necessity to filter the idler requires working 

112 

_Chapter 7. Spectrometer sensitivity_ 

slightly detuned from the top of the JPA gain curve and thus the gain improves by a little more than 6 dB when shifting to phase-sensitive operation. 

Summing up, the best absolute SNR reached is 7 _±_ 1 (red curve in Fig. 7.6b) a factor _⇡⇥_ 11 better than without JPA. The sensitivity of the spectrometer is thus: 



spins detected in a single-echo with a SNR unity. As _T_ 1 was measured to be 0.3 s (see Fig. 6.9) in these conditions, the SNR determination was done with the repetition rate set at _γ_ rep<sup>_−_1= 3</sup><sup>_T_1= 1 s</sup> and thus the overall absolute sensitivity of the spectrometer is 1 _._ 7 _⇥_ 10<sup>3</sup> spins/ _p_ Hz. 

##### **Spins spontaneous emission noise** 

The interest of determining separately the noise from the signal is to be able to determine more accurately the noise by accumulating more data, since every point can be acquired without having to wait 3 _T_ 1. The statistical uncertainty of the SNR thus comes solely from the signal with _"_ SNR = 1 _/p_ 10 for the above determination. 

However such a determination neglects any noise emitted by the spins such as the spontaneous emission noise _n_ SE . To evaluate nevertheless this contribution, we perform once again numerical simulations but include this time the quantum noise evaluation using the methods of [182]. The numerical results are shown in Fig. 7.5 and predict an excess noise of _⇡_ 30 % during the echo emission, that would scale down the measured SNR to 5 _._ 5 _±_ 1. Taking into account the fact that this noise is proportional to the number of spins _N_ spins(this assumption was checked numerically) being excited, the sensitivity reached with a SNR unity can be estimated to be _N_ min = 1 _._ 8 _⇥_ 10<sup>3</sup> or equivalently 1 _._ 8 _⇥_ 10<sup>3</sup> spins/ _p_ Hz. 

##### **Comparison to theoretical estimate** 

This experimentally determined sensitivity is in semi-quantitative agreement with the theoretical estimate of section 5.1.2, which predicted _N_ min = 400 for our parameters (see Eq. 5.11). The gain of four-orders of magnitude compared to the state-of-the-art is consistent with the improvements made on the spectrometer setup. Working at low-temperatures yields a complete polarization of the spin ensemble, giving a factor 12 enhancement, but also permit to cool-down the microwave field to its ground state. With a detection made by a JPA in phase-sensitive mode, the quantum fluctuations are thus the dominant noise source, giving a factor _⇡_ 10 improvement on _N_ min. Finally the choice of a high-quality factor resonator, together with its small mode volume, gives a factor 20 improvement. 

The remaining discrepancy between the theoretical estimate and our experimental determination can be traced to various origins. First, the derivation of section 5.1.2 assumed that _ ≫ w_ and that the drive pulses were ideal; this is not the case in our experiment as explained earlier. Then, our experiment suffers from microwave losses (resonator internal losses, circulators and filters insertion loss, ...). In addition, our JPA is not perfect; in particular the contribution of the follow-up amplifiers to the total output noise is not negligible. Finally, in the experiment the signal was defined with a square time integration window (see Eq. 7.9), instead of the optimal output mode choice defined as in Eq. 5.8. 

113 

_Chapter 7. Spectrometer sensitivity_ 



<!-- Start of picture text -->
a b<br>0.10<br>π/2� x π y π y π y x m π y<br>�/2 � � � 0.05<br>2.5µs 5µs 0.00<br>0 10 20 30 40<br>Time (µs)<br>c d e<br>40 1.0<br>Amplitude (V) T  = 71.2 ms<br>0.8 CPMG 12<br>30<br>0 0.15<br>0.6<br>8<br>20<br>0.4<br>10 0.2 4<br>0 0.0 0<br>0 40 80 120 0 200 400 600<br>0 200 400 600<br>Delay, m  �   (ms) Number  m  of<br>m CPMG<br>averaged echoes<br>Amplitude (V)<br>1<br> / SNR<br>(a.u.) m<br>e<br>A<br>Time(µs)<br>SNR<br><!-- End of picture text -->

FIGURE 7.7: **CPMG sequence. a** A spin-echo generated by any pulsed ESR experiment can be refocused by a train of _m ⇡_ pulses with axis of rotation oriented along the echo phase direction. **b** Three time-traces (circles) of echoes _mi_ = 1 (light blue), _mi_ = 100 (dark blue) and _mi_ = 600 (dark red). Solid line shows the average over _m_ = 650 echoes. **c** Color-plot giving the damping of echo _mi_ up to _m_ = 650. **d** Decay of the echo integrated amplitude as a function of the time elapsed between the initial _⇡/_ 2 pulse and the echo (circle), well fit to an exponential of characteristic time _T_ CPMG = 71 _._ 2 ms. **e** Experimentally determined SNR enhancement obtained by averaging _m_ echoes as a function of the number _m_ of echoes in the CPMG sequence (blue circles), showing a 12-fold improvement. In the absence of decoherence the SNR should follow a<sup>_p_</sup> _<u>m</u>_ ~~-~~ law (green curve). With damping (red, see text and Eq. 7.13), the SNR levels off for higher _m_ . 

#### **7.2.2 Sensitivity enhancement by CPMG echoes** 

The sensitivity can be further increased by using a Carr-Purcell-Meiboom-Gill (CPMG) sequence [183]. As shown in Fig. 7.7a, adding _m ⇡y_ pulses after the initial echo generated by a _⇡x − ⌧ − ⇡y − ⌧_ Hahn-echo sequence allows to refocus the spins _m_ more times and thus recover _m_ extra-echoes within a single sequence; all the echoes can then be averaged out to improve the SNR. Fig. 7.7b-c shows that for our Si:Bi sample up to 650 echoes can be recovered. The echo signal is seen to decrease exponentially with a characteristic damping time _T_ CPMG = 71 ms, a value ten times bigger than the time _T_ 2 measured in Fig.6.10. 

In terms of sensitivity, the recovered echoes can simply be averaged to enhance the SNR. While averaging _m_ times the same signal yields a<sup>_p_</sup> _<u>m</u>_ -enhancement, the echo damping levels off the enhancement at high _m_ . Indeed, consider the accumulation of _m_ echoes emitted at a a period _T_ damped at rate _T_ CPMG and acquired with the same noise _N_ . The best SNR is obtained by weighting each echo with an exponentially decreasing weight _wi_ = _↵e_<sup>_−iT/T_CPMG</sup> . The overall normalization factor _↵_ for each weight is found by expressing that _N_ ( _m_ ) = ~~qP~~ _i_<sup>_w_</sup> _i_<sup>2</sup><sup>_N_2</sup> (1)<sup>=</sup><sup>_N_(1)and thus</sup> 



114 

_Chapter 7. Spectrometer sensitivity_ 

It then comes that the signal is expressed as _S_ ( _m_ ) =<sup>P</sup> _i_<sup>_S_(1)</sup><sup>_↵e−i_2</sup><sup>_T/T_CPMGso that theSNR enhance-</sup> ment reads: 



Eq. 7.13 yields that for small _m_ , the SNR increases as<sup>_p_</sup> _<u>m</u>_ but is bounded at _T_ CPMG _/_ 2 _T_ for larger values. We applied this averaging method to our experiment, as shown in Fig. 7.7e, demonstrating a 12-fold improvement over the single-echo SNR. This has the direct consequence of improving the sensitivity to _N_ min = 150. Moreover as this technique does not require waiting a time 3 _T_ 1 between each echo, the absolute sensitivity is also improved to 150 spins/ _p_ Hz. 

The sensitivity could be further increased if the CPMG damping was reduced, by for example using more complicated sequences alternating _⇡±y_ and _⇡±x_ such as the CPMG XY-8 sequence[184] up to the point where it becomes limited either by spin decoherence, or by pulse errors. We did not investigate such techniques in our ESR spectrometer. 

### **7.3 Conclusion** 

The analysis above demonstrates that the combined use of low-temperatures, high-quality factors, small-mode volumes and quantum-limited amplifiers can dramatically enhance the sensitivity of an ESR experiment, with a 4-orders of magnitude enhancement compared to the state-of-the-art. This experiment places ESR in a new regime where the noise is no longer limited by thermal or technical noise but by the quantum fluctuations of the electromagnetic field. 

The achieved sensitivity for our resonator detection volume of _⇠_ 0 _._ 02 nl already enables ESR experiments at the nanoscale. More versatility could easily be obtained by patterning the resonator out of superconductors able to sustain higher magnetic fields (such as niobium) which would thus allow to study a wider range of spin species. Applications include studying single cells, small molecular ensembles, nanoparticles and nanodevices. 

Finally, the sensitivity can be improved even beyond the above results. While the spin polarization is now maximum, the other quantities entering into play in the sensitivity can still be improved. Indeed, the quality factor can yet be increased by a factor of 2 or 3 if the losses were reduced to the current state-of-the-art _Q_ int _>_ 10<sup>6</sup> . A straightforward enhancement could also come from the spin-photon coupling. While we reached _g/_ 2 _⇡ ⇠_ 50 Hz with a 5 µm wide wire, nano-fabrication techniques easily allow to scale down the wire transverse dimensions by a factor 100, which would yield an enhancement of the same factor on _g_ and thus allow to improve the sensitivity up to the level of being able to detect only a few spins. Last, even if quantum fluctuations have become the primary noise source in our experiment, decreasing the noise beyond the standard quantum limit is possible with the use of squeezed quantum states as we will see in ch. 9. 

115 

## **Part III** 

# **The Purcell effect applied to spins** 

116 

## **Chapter 8** 

# **Controlling spin relaxation with a cavity** 

Coupling with the radiation is hopelessly inadequate as a relaxation mechanism _A. Abragam_ , on nuclear spins [4]. 

Understanding and controlling spin relaxation is essential in applications such as spintronics, quantum information processing and magnetic resonance imaging. The energy relaxation time _T_ 1 describes the return to equilibrium and has to be sufficiently long to permit coherent spin manipulation since _T_ 2 6 2 _T_ 1. However a too long _T_ 1 can become a major bottleneck, since the return to equilibrium will be prohibitively long and limit the repetition rate of an experiment, directly impacting factors such as the achievable sensitivity. An ideal situation would be to have the ability to re-initialize the spins on-demand while having a long _T_ 1 to preserve the spin coherence. This can be achieved in particular systems by an active reset. For example,NV centers have a state-selective optical transition allowing to establish a spin polarization higher than 90% under laser illumination [185]. Coupling to the environment via other degrees of freedom can also reset the system: a neutral phosphorus donor in silicon can be initialized via its charge state when coupled to a single-electron transistor [122] or by selective Auger photo-ionization when coupled to a donor bound exciton [133]. 

For other spin systems, such active re-initialization schemes may not be available. This is particularly an issue at ultra-low temperature since the spin-lattice relaxation times can become very long due to the vanishing phonon density (see 4.4.1). For instance, _T_ 1 reaches up to thousands of seconds for phosphorus donors at 1.2 K[16]. To shorten the spin relaxation times a number of in-situ methods have been developed such as chemical doping [186] and gamma irradiation [187]. Nevertheless such methods are not tunable and a too fast _T_ 1 relaxation will ultimately affect the coherence time _T_ 2. In short, for systems without an active reset, an efficient, universal and tunable initialization method for spin systems is still lacking. 

In all listed spin relaxation phenomena, spontaneous emission of radiation is usually quickly dismissed as a possible spin relaxation mechanism due to the very weak coupling of spins to their electromagnetic environment. However, Purcell realized in 1946 that the spontaneous emission rate can be dramatically enhanced by placing the quantum system in a resonant cavity [188]. This effect has since then be used to control the lifetime of atoms [28] and semi-conducting heterostructures [29] coupled to microwave or optical cavities and is essential for the realization of high-efficiency singlephoton sources [30]. In this chapter, we apply this idea to spins in solid to provide an on-demand re-initialization scheme. We first review cavity-enhanced spontaneous emission implementations before demonstrating experimentally the Purcell effect for bismuth donors in silicon. The last part will discuss how this effect can be harnessed to control in-situ the spin relaxation. 

117 

_Chapter 8. Controlling spin relaxation with a cavity_ 

### **8.1 Cavity-enhanced spontaneous emission** 

As we have seen in ch. 3, spontaneous emission of radiation is due to the coupling of a twolevel-system (TLS) to the quantum fluctuations of the electromagnetic field. If the TLS is in free space, an infinity of electromagnetic modes are available for the photon emission, resulting in an irreversible incoherent process. E. Purcell predicted in 1946 that by placing the TLS inside a cavity [188], spontaneous emission can be greatly inhibited or enhanced due to the modification of the mode density. This effect is captured by the so-called Purcell rate whose expression was derived in ch. 3 (see Eq. 3.37) and is a founding concept of the field of cavity Quantum Electrodynamics[189]. In his pioneering article of 1946, Purcell considered a nuclear spin embedded in a resonant structure, such as the resonant RLC circuit used in NMR. Because nuclear spin spontaneous emission occurs at a negligible rate due to the very weak coupling of the spin to the vacuum fluctuations, the first experimental observation was done instead with atoms in a microwave cavity [28]. 

Even if we have already derived the Purcell formula using the formalism of CQED in ch. 3, it is interesting to derive it here using other arguments to understand why it has not be observed up to now for spins. We thus first derive the theoretical expressions for spontaneous emission rates both for an electrical and a magnetic dipole before succintly recalling the Purcell effect. We review its experimental realizations in systems with an electrical dipole and then consider its application to spins. 

#### **8.1.1 Spontaneous emission into free space** 

The rate of spontaneous emission into free space Γ0 can be derived using the Weisskopf-Wigner approximation, as explained for instance in [190]. Consider a spin with an energy splitting ~ _!s_ between its ground _|_ g _i_ and excited _|_ e _i_ state. As we have seen in ch. 3, its interacting Hamiltonian ˆ with the electromagnetic radiation is _H_<sup>ˆ</sup> int = _−_ **_µ_** _·_ **_B_**<sup>ˆ</sup> ( _t_ ). In the Heisenberg picture, the free-space quantized magnetic field is the sum of the quantized field of each mode of wavevector **k** and polarization state _λ_ , **_B_**<sup>ˆ</sup> =<sup>P</sup> **_k_** _λ_ **_B_**<sup>ˆ</sup> **_k_** _λ_ with **_B_**<sup>ˆ</sup> **_k_** _,λ_ being [38]: 



where **_ek_** _λ_ are the two unit polarization vectors and _V_ the quantization volume. We assume implicitly in this expression that the electromagnetic field is slowly varying at the spin location so that we can realize the dipole approximation _e_<sup>_i_</sup><sup>**_k_**</sup><sup>_·_</sup><sup>**_r_**</sup> _⇡_ 1. Following the same steps than in 3.2.1 for each mode ( **_k_** _, λ_ ), the interaction Hamiltonian in the interaction picture after the rotating wave approximation is: 



where the coupling strength for each mode is now _g_ **_k_** _λ_ = _h_ e _|_ **_µ_** _·_ **_ek_** _λ |_ g _i_ ~~p~~ _µ_ 0 _!k/_ (2~ _V_ ). We next assume that at time _t_ = 0, the spin is in its excited state while the elecromagnetic field is in its ground state, so that the overall state of the system is written: 



with _c_ e _,_ 0(0) = 1 and _c_ g _,_ **_k_** _λ_ . Using the Schrödinger equation _|_ (<sup>˙</sup> _t_ ) _i_ = _−_<sup>_<u>i</u>_</sup> _<u>H</u>_<sup>ˆ</sup> ~int _|_ ( _t_ ) _i_ , one can show that the evolution of the coefficient _c_ e _,_ 0 is given by the following differential-integral equation: 



118 

_Chapter 8. Controlling spin relaxation with a cavity_ 

||**~~Nuclear spin~~**<br>1_/_2[188]|**Electronic spin**1_/_2[5]|**~~Sodium atom~~**~~[28]~~<br>_|_23_Si $|_22_Pi_|
|---|---|---|---|
|_!_0_/_2_⇡_|10 MHz|7 GHz|340 GHz|
|Interaction|_µ_=_µN_|_µ_=~_γeS_,_γe_ = 28GHz/T|_d_= 570_D_|
|Γ0 (s<sup>_−_1</sup>)|3_⇥_10<sup>_−_28</sup>|1_⇥_10<sup>_−_12</sup>|145|
|Γ1 at_T_ = 4K (s<sup>_−_1</sup>)|5_⇥_10<sup>_−_24</sup>|2_._4_⇥_10<sup>_−_11</sup>|150|
|Γ1 at_T_ = 300K(s<sup>_−_1</sup>)|4_⇥_10<sup>_−_22</sup>|2_⇥_10<sup>_−_9</sup>|6_⇥_10<sup>3</sup>|



TABLE 8.1: Spontaneous emission rate at zero, helium and room temperature for various systems emitting microwave radiation in free space. _µN_ is the nuclear magneton, _γe_ the electron gyromagnetic ratio. 

The sum over the wavevectors may be replaced by an integral over **_k_** -space, spanned by spherical coordinates with the _z_ -axis aligned on **_µ_** so that **_µ_** _._ **_k_** = _dk_ cos _✓_ : 



with the mode density _⇢_ ( _!_ ) being 8 _<u>!⇡</u>_<sup>23</sup> _<u>Vc</u>_<sup>3.Inthiscoordinatesystem,onecanshowthat</sup><sup>_|g!λ|_2</sup> ˜ ˜ simplifies to _µ_<sup>2</sup> sin<sup>2</sup> ( _✓_ ) _µ_ 0 _!k/_ (2~ _V_ ) where _µ_ = _|h_ e _| µ |_ g _i|_ . Next, as _c_ e _,_ 0( _t_ ) is expected to decay at a _1_ rate _⇠_ Γ0 much smaller than the frequency _!_ , R0 _e_<sup>_−i_(</sup><sup>_!−!s_)(</sup><sup>_t−t0_)</sup> _c_ e _,_ 0( _t_<sup>_0_</sup> ) _dt_<sup>_0_</sup> can be approximated as _⇡ ⇡δ_ ( _! − !s_ ) _c_ e _,_ 0( _t_ ), doing the so-called Weisskopf-Wigner approximation [190]. Performing the integration over _✓_ , _φ_ and _!_ , Eq. 8.5 thus yields: 



Identifying the decay rate in Eq. 8.6 to Γ0 _/_ 2, we find the usual expression of Γ0 for a magnetic dipole into free space [4]: 



The derivation for an electrical dipole **_d_** is similar: the interacting Hamiltonian is given by _H_<sup>ˆ</sup> int = _−_ **_d_**<sup>ˆ</sup> _·_ **_E_**<sup>ˆ</sup> ( _t_ ) and the free-space quantized electrical field **_E_**<sup>ˆ</sup> is linked to **_B_**<sup>ˆ</sup> by **_Ek_** _,λ_ = **_Bk_** _,λ ⇥_ **_e_** _k/_<sup>_p_</sup> _<u>µ</u>_ 0 _<u>"</u>_ 0. Following the same steps, we obtain: 



Interestingly, if we consider a Bohr magneton _µB_ and the dipole created by two elementary charges separated by a Bohr radius _d ⇠ ea_ 0 the ratio of their spontaneous emission is Γ<sup>(elec)</sup> 0 _/_ Γ<sup>(magn)</sup> 0 = _<u>cµ</u>_<sup>2</sup> _<u>d</u>_<sup>22</sup> = _↵_ <u>1</u><sup>2where</sup><sup>_↵_is the fine structure constant, confirming that an electrical dipole is naturally</sup> more strongly coupled to the field than a magnetic dipole. 

These rates are derived under the assumption that there are no thermal photons populating the electromagnetic field. If it is at thermal equilibrium at a temperature _T_ , its thermal photon occupancy is _n_ th( _T_ ) (see Eq. 2.10). As we have seen in ch. 3 (see Eq. 3.45), the resulting relaxation rate is modified to Γ1( _T_ ) = (2 _n_ th( _T_ ) + 1)Γ0. Due to the _!s_<sup>3dependenceandtothestrengthdifferencebetween</sup> electric and magnetic dipole transitions, the spontaneous emission rates at 4 K and 300 K for a Rydberg atom, an electronic spin, and a nuclear spin range from easily detectable values to the age of the universe, as shown in Table 8.1. 

119 



<!-- Start of picture text -->
@ [4] w;<br>tuninguni Rg pre—=ag——=——g3] 22p (b)<br>LHe-cooled voltageramp &9 [234em|245cm i ~T ; 238 |:<br>(5.7K) © :<br>Nb microwavecavity | zz) | electric field t1 || ? |3 tramp / ps<br>—ee cavity in<br>Na beam = | pe = resonance<br>(<br>pulsed |<br>laser beams, electron : _<br>perpendicular multiplier // | cavity off<br>| resonance A<br>23s 22p<br><!-- End of picture text -->



<!-- Start of picture text -->
Spectrum<br>FE<br>r4 - Cc. =<br>1 He I; | i<br>| = 1 X|<br>X Lsat L<br>|I RLp=k == g EOI<br>DTN = |<br>sample<br>\ R i =<br>I I<br><!-- End of picture text -->



<!-- Start of picture text -->
-9l<br>_<br>gE |" ~~<br>oS R<br>~gng -92 \AN<br>8 §<br>5-93), A<br>=<br>Oo } 1<br>94<br>+01<br>+ -0.1 STTH HS ST SE ST SR<br>ax 30678 30684 30690<br>Frequency (MHz)<br><!-- End of picture text -->





<!-- Start of picture text -->
[4]a es== ,<br><!-- End of picture text -->





<!-- Start of picture text -->
-<br><!-- End of picture text -->

_Chapter 8. Controlling spin relaxation with a cavity_ 

||_!_0_/_2_⇡_|Q|**_B_**0|_P_in(_⇡_)|__1|¯_n_(_⇡_)|_g/_2_⇡_|_T_1|
|---|---|---|---|---|---|---|---|---|
||GHz||mT|pW|s<sup>_−_1</sup>||Hz|s|
|_B_|7.246|3_._2_⇥_10<sup>5</sup>|5.13|1.9|5_._8_⇥_10<sup>4</sup>|1_._0_⇥_10<sup>6</sup>|50_±_7|0_._26_±_0_._08|
|_C_|7.305|1_._1_⇥_10<sup>5</sup>|2.78|4.6|3_._1_⇥_10<sup>5</sup>|7_._4_⇥_10<sup>5</sup>|58_±_7|0_._75_±_0_._15|



TABLE 8.2: **Experimental values for resonators** _B_ **&** _C_ **.** Resonator X, with frequency _!_ 0 and quality factor _Q_ is resonant with transition _|_ 9 _i $ |_ 10 _i_ at magnetic field **_B_** 0. From Rabi oscillations, the input power of a _⇡_ pulse of duration 5µs can be determined. Knowledge of _Q_ and __ 1 the input coupling rate allow to link _P_ in to _n_ ¯ the intra-cavity mean photon number for a _⇡_ pulse and to the spin-resonator coupling constant _g_ 0. The Purcell formula allows to estimate the expected enhanced spontaneous emission time at resonance. 

shielding (see ch. 5), we expect _n_ th = 0 _._ 05 and additional measurements (described in Appendix A) confirms _n_ th = 0 _._ 05 _±_ 0 _._ 05. We can therefore expect _T_ 1 values given by: 



The experiments are realised on the low-field peak of the transition _|_ 9 _i $ |_ 10 _i_ , with the applied magnetic field **_B_** 0 aligned along the wire ( _✓_ = 0), see Table 8.2. As explained in ch. 6, this peak originates from spins located under the wire. An estimate of the spin-coupling constant over this spin sub-ensemble yields a distribution sharply peaked on _g/_ 2 _⇡_ = 56 _±_ 1 Hz, (see Fig. 8.3b and 5.3.3). 

#### **8.2.2 Experimental estimate of** _g_ 

Rabi oscillations can be performed to obtain an independent estimate of _g_ , see Fig. 8.4c. As explained in 6.1.3, their frequency ⌦ _R_ = 2 _g_<sup>_p_</sup> _n_ ¯ directly yields _g_ upon knowledge of the incident power _P_ in and the measured input and output coupling rates. The precision of this determination is limited by 



<!-- Start of picture text -->
Inversion Readout<br>a b<br>τ P in τ T AQ ( T )<br>ω�� ,  P in π /2 π π echo π π /2 π echo<br>π<br>1<br>1.0<br>π/2<br>echo<br>� � 0<br>� 2<br>0.5<br>T 1= 1.0±0.2 s<br>copper box -1 T 1= 0.35±0.1 s<br>0<br>0 2 4 6 0 1 2 3<br>P in1/2 (pW)1/2 Delay  T  (s)<br>)<br>=<br>( TQ<br>A<br>) /<br>( TQ<br>A<br>Echo amp (a.u.)<br><!-- End of picture text -->

FIGURE 8.4: **Purcell-limited** _T_ 1 **. a-b** Data obtained with the static field **_B_** 0 parallel to the inductor ( _✓_ = 0). The symbols represent data for resonator _B_ (green squares) and resonator _C_ (brown circles) **a** Rabi oscillations are driven by varying the cavity input power of the refocusing _⇡_ pulse (5 µs-long) applied _⌧_ = 300 µs after the first _⇡/_ 2 pulse. Solid lines are exponentially damped sinusoidal fits. **b** The inversion-recovery sequence is used to measure the spin relaxation time _T_ 1 (see 6.3.1). Solid lines are exponential fits to the data with time constant _T_ 1. The uncertainty is given by the standard deviation of the exponential fit parameters. 

123 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
a b<br>1.0 1.0<br>25<br>BW Pulse 5us<br>0.8 BW resonator<br>BW Pulse 100us 20 0.5<br>Pulse   π   5us, T1 = 0.65 s<br>0.6 Inversion Readout<br>15 0.0 T AQ (T)<br>� � /2 �<br>0.4<br>10<br>0.2 5 -0.5 Pulse  Inversion π   100us, TT Readout 1=0.35s AQ (T)<br>� � /2 �<br>-1.0<br>0.0 0<br>-100 -50 0 50 100<br>0 1 2 3 4 5 6<br>Detuning (kHz)<br>Time T (s)<br>)<br>(T=<br>Q<br>(T) /A<br>Q<br>A<br>Normalized response (a.u.) T1 as given by Purcell law (s)<br><!-- End of picture text -->

FIGURE 8.5: _T_ 1(∆= 0) **bandwidth. a** Bandwidths (left axis) of resonator _B_ (green) and applied readout sequences with pulses of 5 µs (green) and 100 µs (blue) resulting in an averaging effect on the measured _T_ 1 (right axis). **b** Comparison of _T_ 1 measured with readout pulses of 5 µs (red squares) and 100 µs (blue circles). The spin energy relaxation time _T_ 1 being of order 1 s, we choose a repetition rate _γ_ rep =0.04 Hz sufficiently low to allow full relaxation of the spins in-between successive inversion recovery sequences. 

the accuracy on _P_ in which we estimate to be of 30%. The values obtained for resonators _B_ and _C_ (see Table 8.2) are in good agreement with the numerical estimate. 

From the experimental determination of _g_ , the measured resonator quality factors and _n_ th, the expected spontaneous emission rate at resonance can be estimated to be _T_ 1 = 0 _._ 26 _±_ 0 _._ 08 s for resonator _B_ and _T_ 1 = 0 _._ 74 _±_ 0 _._ 15 s for resonator _C_ , see Table 8.2. We can also evaluate the spinensemble cooperativity (see Eq. 3.51) to evaluate the relevance of collective radiation effects. Using the numerical simulations of ch. 7 we find _CB_ = 0 _._ 26 and _CC_ = 0 _._ 09. Since both are below 1, we thus expect that spins will relax independently from each other, with an exponential decay at rate Γ _P_ . 

#### **8.2.3** _T_ 1 **at resonance** 

As explained in section 6.3.1, _T_ 1 is measured by the inversion-recovery sequence shown in Fig. 8.4c, consisting in a _⇡_ pulse followed after a varying delay _T_ by a spin-echo readout sequence. The resulting echo signal _AQ_ ( _T_ ) comes from all spins whose frequency lies in the readout sequence pulse bandwidth. To avoid an averaging effect on the measured _T_ 1 arising from its dependence on ∆, the detection bandwidth has to be small (see 6.1.3). For the narrowest bandwidth _/_ 2 _⇡_ = 23 kHz of resonator _B_ , Fig. 8.5a shows that pulses of 5 µs are heavily filtered by the resonator and have a bandwidth of 40 kHz whereas 100 µs-long pulses have a reduced bandwidth of _⇡_ 10 kHz. In the case of 100 µs-long pulses, only spins with _|_ ∆ _|/_ 2 _⇡ _ 5 kHz contribute to the signal, corresponding to a negligible dispersion of 5% for the Purcell relaxation times. Indeed, as illustrated in Fig. 8.5b, no averaging effect is observed for a _T_ 1 measured with 100 µs-long pulses whereas a _T_ 1 acquired with 5-µs–long pulses is 50% longer. Therefore we chose to use 100 µs-long readout pulses although the inversion pulse bandwidth is chosen to be large ( _t⇡_ = 5 µs) in order to maximize the inversion efficiency. 

The relaxation curves measured for resonators _B_ and _C_ are shown in Fig. 8.4c and are well fitted by exponential decays. The extracted characteristic times yield _T_ 1 = 0 _._ 35 _±_ 0 _._ 1 s for resonator _B_ and _T_ 1 = 1 _._ 0 _±_ 0 _._ 2 s for resonator _C_ . This is in close agreement with the predicted values (see Table 8.2). Resonators _B_ and _C_ have a factor 3 difference in their quality factor, a factor that we retrieve in their 

124 

_Chapter 8. Controlling spin relaxation with a cavity_ 

relaxation times. From these results we can infer that cavity-enhanced emission is the dominant spin relaxation mechanism in our experiment. 

### **8.3 Controlling spin relaxation** 

We now show how the Purcell effect can provide a method to tune _T_ 1 in-situ and on-demand. Indeed, the Purcell rate depends on three quantities that can be tuned experimentally: 

- **the cavity quality factor** _Q_ . At resonance, the Purcell rate is proportional to _Q._ This is evidenced in our experiment by the dependence of the relaxation times measured at resonance for resonators _B_ and _C_ on their quality factors. A dynamic control of the quality factor could be achieved by using Josephson junction devices [205, 206]. We have not explored this option. 

- **the spin-cavity coupling constant** _g_ **.** At resonance, the Purcell rate is proportional to _g_<sup>2</sup> _._ In our experiment, due to the strain applied by the aluminum wire on the silicon substrate, we can access different subsets of spins coupled at different strengths to the resonator to probe this dependence (see 6.2.2). In our setup, the coupling constant can also be altered in-situ by changing the angle between the static field **_B_** 0 and the microwave field _δ_ **_B_** , as will be shown below. 

- **the spin-cavity detuning** ∆. The Purcell rate is strongly dependent on the spin-cavity detuning which can be controlled by changing **_B_** 0. 

#### **8.3.1 Tuning** _T_ 1 **via the spin-cavity coupling** _g_ 0 

##### **Purcell-limited** _T_ 1 **dependence on** _B_ 0 

In our experiment, the spin frequency spread ∆ _!_ is much larger than the resonator bandwidth __ . By applying various magnetic fields **_B_** 0, different spin subsets are brought to resonance. Since the line inhomogeneity is due to the strain applied by the aluminum (see ch. 6), the spin frequency is correlated to their spatial position with respect to the wire, which is also correlated to the spatial dependence of _δ_ **_B_** ( **_r_** ) and thus to _g_ . We evidenced this effect in 6.2.2 via the magnetic field **_B_** 0 dependence of the Rabi oscillations frequency (see Fig. 8.6a). From this measurement, we estimate _g_ with values ranging from 20 to 90 Hz for _B_ 0 ranging from 4.9 to 5.4 mT for resonator _B_ . 

We measure _T_ 1 relaxation times with an inversion recovery sequence at various magnetic fields **_B_** 0 on a range covering the entire spin frequency distribution (see Fig. 8.6b). As anticipated, we find a strong dependence of _T_ 1 on **_B_** 0, with values ranging from 1 to 8 s. To verify that _T_ 1 scales as _g_<sup>_−_2</sup> , we plot ( _T_ 1 _,i/T_ 1 _,_ 0) as a function of ( _gi/g_ 0)<sup>_−_2</sup> with _T_ 1 _,_ 0 = _T_ 1(5 _._ 13 mT) and _g_ 0 = _g_ (5 _._ 13 mT) and _T_ 1 _,i_ and _gi_ the values at different magnetic fields. The corresponding experimental data shown in Fig. 8.6c demonstrate quantitatively that within the experimental errors bars _T_ 1 depends linearly on _g_<sup>_−_2</sup> as expected from the Purcell law. 

If we focus on a single magnetic field _B_ 0 = 5 _._ 13 mT, we note that _T_ 1 _,_ 0 = 1 _._ 4 _±_ 0 _._ 2 s which is a factor 2 longer than expected for an estimated _g_ 0 _/_ 2 _⇡_ = 56 Hz and a thermal photon occupancy _n_ th = 0 _._ 05. Two factors can explain this error. First, the measured quality factor was by mistake not determined at the single-photon limit and thus could be wrong by a factor 2 (see 5.3.4). Secondly, _g_ is determined with two uncertainties: the input power _P_ in is known only at 1 dB precision and in 

125 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
a 0.5 P in b<br>τ τ 1<br>0.4 π /2 echo<br>0.3<br>0.2 0<br>0.1 Inversion T Readout AQ ( T )<br>1 π π /2 π echo<br>-1<br>0.1 1 10<br>Delay  T  (s)<br>c 10<br>0<br>100<br>80<br>60<br>40 1<br>20<br>0<br>5.0 5.1 5.2 5.3<br>1 10<br>Magnetic Field  B0  (mT) ( g / g 0)-²<br> (Hz)<br>π<br>g/2<br>1,0<br>/ T 1<br>T<br>)<br>1/2 =<br>T<br>(<br>Q<br> (nW) A<br>1/2 ) /<br>in T<br>P (<br>Q<br>A<br>Echo amp (a.u.)<br><!-- End of picture text -->

FIGURE 8.6: **Dependence of Purcell relaxation on spin-cavity coupling** _g_ 0( _B_ 0) _._ **a** (top) Rabi oscillations as a function of the magnetic field. (middle) Hahn-echo magnetic field sweep (botttom) Coupling constant distribution extracted from Rabi oscillations, with uncertainty solely estimated from the fit (neglecting the 30% uncertainty from the knowledge of the attenuation of the line). **b** _T_ 1-relaxation measured by inversion-recovery as a function of **_B_** 0 _._ For clarity, only three values of **_B_** 0 are shown: 5.06 mT (red circles), 5.29 mT (purple diamonds) and 5.22 mT (blue squares). **c** Measured _T_ 1 _/T_ 1 _,_ 0 as a function of measured coupling constant ( _g/g_ 0)<sup>_−_2</sup> , as evaluated from the Rabi oscillations (filled circles, color corresponds to **_B_** 0, with arrows on **a** ). The index 0 denotes data taken for _B_ 0 = 5 _._ 13 mT (grey dashed line on **a** ). The uncertainties are determined from the _σ_ -values extracted from the _T_ 1 and Rabi oscillations fits. The solid red line is the demarcation y=x. All data was collected with resonator _B_ , with _Q_ = 1 _._ 05 _⇥_ 10<sup>5</sup> and _✓_ = 0. 

this particular run the couplings __ 1 and __ 2 for each resonator were not determined, leading us to rely on assumptions<sup>2</sup> to estimate the intra-cavity photon number ¯ _n_ . 

In spite of this remaining uncertainty, we can still harness the linear dependence of _T_ 1 on _g_<sup>2</sup> to control _T_ 1: here we show that we can access values of _T_ 1 ranging over one order of magnitude. We note that the spatial dependence of _T_ 1 could be evidenced more straightforwardly if the spin ensemble was attached to the tip of a scanning probe, and could be displaced with respect to the resonator. 

> 2Compared to the couplings presented in Table 8.2, the chip was oriented differently and resonators _B_ & _A_ have reversed positions with respect to the input and output antennas whereas resonator _C_ had the same spatial position. Assuming a posteriori that the losses were identical for each resonator, we can estimate __ int = 3 _._ 1 _⇥_ 10<sup>5</sup> _s_<sup>_−_1</sup> by supposing the couplings for resonator _C_ are identical to Table 8.2. Then by assuming resonator _B_ has the same asymmetry in coupling as resonator¯ _A_ had, we can evaluate __ 1 = 9 _._ 4 _⇥_ 10<sup>3</sup> _s_<sup>_−_1</sup> and are able to determine the intra-cavity photon number _n_ and thus determine _g_ 0 _/_ 2 _⇡_ = 56 Hz. 

126 

_Chapter 8. Controlling spin relaxation with a cavity_ 

##### **Purcell-limited** _T_ 1 **dependence on** _✓_ 

Our 2D coil magnet offers another method to control _g_ in-situ. The experimental 2D-coils setup allows to tilt **_B_** 0 within the resonator plane with an angle _✓_ with respect to the resonator wire. As a consequence of the spin system isotropy, the spin quantization axis is always aligned along **_B_** 0. The particular sub-ensemble of spins lying under the wire is excited by a field **_B_** 1 mainly parallel to the surface, with only a small out-of-plane component. By tuning _✓,_ the quantization axis can be tuned from being perpendicular to **_B_** 1, a geometry that maximizes the coupling to the resonator, to being parallel to **_B_** 1 which leads to a vanishing coupling to the field. This _✓_ -dependence of _g_ 0 is captured in the following relation (see Eq. 5.20): 



where _gz / δBz_ and _gy / δBy_ , see Fig. 8.7a. To experimentally test this expected _✓_ -dependence, we perform Rabi-oscillations at varying angles _✓_ , as shown in Fig. 8.7b. We performed this experiment on resonator _C_ using the _|_ 9 _i $ |_ 10 _i_ transition. The frequency of the Rabi oscillations is decreasing as a function of _✓_ , which indicates decreasing values of _g_ ( _✓_ ), as seen in Fig. 8.7c. For large angles _✓_ , the coupling becomes too small to detect a signal, explaining the disappearance of the Rabi oscillations. A fit of _g_ ( _✓_ ) with Eq. 8.12 yields _gy/_ 2 _⇡_ = 55 Hz and _gz/_ 2 _⇡_ =17 Hz. 

_T_ 1 relaxation curves as a function of _✓_ are then measured with an inversion recovery sequence (see Fig. 8.7d). Smaller values of _T_ 1 are measured for larger _✓_ as expected from the reduced coupling of the spin to the microwave field. Plotting 1 _/T_ 1( _✓_ ) versus cos<sup>2</sup> ( _✓_ ) shows a linear dependence (see Fig. 8.7e). It follows the theory line given by the Purcell relation evaluated with the _g_ ( _✓_ )-fit from Fig. 8.7c (red solid line) and the measured quality factor for resonator _C_ (given in Table 8.2). 

Here, we have been able to control the relaxation time _T_ 1 by a factor 3 by tuning the spin-cavity coupling constant. Larger tuning factors could be obtained with a better **_B_** 1 homogeneity over the probed spin ensemble, which would allow to better align **_B_** 1 on **_B_** 0 and thus to suppress completely the spin-microwave coupling. 

#### **8.3.2 Tuning** _T_ 1 **via the spin-resonator detuning** 

##### **Experimental protocol** 

According to Eq 8.9, _T_ 1 should strongly depend on the spin-cavity detuning if it is indeed limited by the Purcell effect. To test this effect we introduce in the _T_ 1 measurement sequence a magnetic field pulse of amplitude **_B_** ∆ and of duration _T_ between the spin excitation and the readout spin-echo sequence (see Fig. 8.9a), which results in a temporary detuning ∆ of the spins given by ∆=<sup>_<u>d!</u>_</sup> dB<sup>_<u>s</u>_</sup><sup>**_B_**∆.</sup> As the spins are detuned from the resonator during this waiting period they have a smaller Purcell decay rate leading to a reduced polarization decay during the time _T_ . The decay of the echo signal amplitude _A_ Q as a function of _T_ yields the detuned spins energy relaxation time. 

The magnetic field pulse **_B_** ∆ is implemented by applying a current pulse on one of the Helmholtz coils used to apply the static field **_B_ 0** , see Fig. 8.8a. The pulse is output by a pulse generator with 50 ⌦ output impedance placed in parallel to the DC supply of one of the Helmholtz coils. To calibrate the additional magnetic field pulse, the generator is used in continuous mode to realize a field sweep echo spectroscopy yielding directly the voltage to _B_ 0 conversion factor, as seen in Fig. 8.8b. Note that pulsing only one of the two coils also slightly modifies _✓_ by less than 4<sup>o</sup> , which we neglect in the following. The response time is determined to be on the order of 1 s by measuring the response to a step pulse via the spin echo signal, see Fig. 8.8c. 

To generate the magnetic field pulse, we use a square voltage biasing pulse, which generates a magnetic field **_B_** ∆ with transient exponential rising and falling periods _t_ up and _td_ (Fig. 8.9, red). 

127 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
a z b c 60<br>0 1<br>Al wire y 10 Echo amp (a.u.)<br>8<br>40<br>Probed<br>6<br>Bismuth donors<br>B1 y B1 y 4 20<br>2<br>B<br>0 B<br>0 0<br>x x � 0 40 80 0 0.5 1<br>�  (°) cos( � )<br>d 1 e<br>1.0<br>0 0°<br>30° 0.5<br>40°<br>50°<br>60°<br>-1 0.0<br>2 4 6 8 10 0 0.5 1<br>Delay  T  (s) cos 2 ( � )<br>B<br>1<br> (Hz)<br>π<br>g/2<br>1/2<br> (pW)<br>1/2<br>in<br>P<br>)<br>)<br>=  -1<br>( T  (s<br>Q<br>) /( AT Q 1/ T 1<br>A<br><!-- End of picture text -->

FIGURE 8.7: **Dependence of Purcell relaxation on spin-cavity coupling** _g_ ( _✓_ ). **a** Schematic: the probed spins (red shade) are aligned with respect to **_B_ 0** and probed by the microwave field generated by the wire, whose direction for the concerned spins is along **y** . **b** Rabi oscillations measured as a function of **_B_** 0 field orientation _✓_ ; the colour scale indicates the echo amplitude in arbitrary units. **c** The Rabi oscillations in **a** are used to extract the spin-cavity coupling strength _g_ (blue symbols, error bars are determined by the 30% uncertainty on _P_ in). These data are fit to Eq 8.12 (red line); the non-zero value of _g_ ( _⇡/_ 2) is due to the finite out-of-plane component of the microwave magnetic field. **d** Inversion recovery measurements (error bars indicate the standard deviation of a measured echo) for different values of _✓_ confirm that the relaxation time _T_ 1 shown in panel **e** (error bars are estimates of the standard deviation of the fit) varies as _g_<sup>2</sup> ( _✓_ ). The red solid line in **e** is the Purcell rate predicted using the _g_ ( _✓_ ) dependence fitted from panel **c** . All data were collected using resonator _C_ at **_B_** 0 = 2 _._ 8 mT, with characteristics given in Table 8.2. 

To take into account the slow coil response, buffer delays of 1 s are added after ramping the coil voltages up and down. The relaxation rate given by the Purcell effect will take values ranging from _T_ 1 (0)<sup>_−_1</sup> to Γ _p_ = _T_ 1 (0)<sup>_−_1</sup> _⇥_ 1+4(∆1 _/_ )<sup>2with soft transitions (Fig. 8.9, green).Those soft transitions</sup> will cause additional unwanted decays of the spin polarization (Fig. 8.9, purple). The overall decay for the polarisation during the pulse may then be written as: 



The polarisation measured with the spin-echo sequence can be expressed without knowledge of _t_ up and _t_ down by writing _pm_ ( _T_ ) = _pm_ ( _1_ ) _−_ [ _pm_ ( _1_ ) _− pm_ (0)] _e_<sup>_−_Γ</sup><sup>_p_(∆)</sup><sup>_T_</sup> since _pm_ ( _T_ = _1_ ) = 1. The readout echo signal _A_ Q( _T_ ) being directly proportional to the polarization, it will decay as _AQ_ ( _T_ ) = _AQ_ ( _1_ ) _−_ [ _AQ_ ( _1_ ) _− AQ_ (0)] _e_<sup>_−_Γ</sup><sup>_p_(∆)</sup><sup>_T_</sup> and gives the expected exponential decay to be measured. The quantity _e_<sup>_−_Γ</sup><sup>_p_(∆)</sup><sup>_T_</sup> is accessed by computing [ _A_ Q( _T_ ) _− A_ Q( _1_ )] _/_ [ _A_ Q(0) _− AQ_ ( _1_ )]. 

128 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
a DC 1 25 � c<br>V � B � B<br>Pulse generator coil response<br>DC 2 25 � B0 B2 command<br>B1<br>b DC biais V �� (V) T time<br>1.5 -0.5 0.0 0.5 spin echo readout<br>1.0<br>1.0<br>0.5<br>0.5<br>0.0 2.7 2.8 2.9 3 010-3 0.1 10 2.6 2.7 2.8<br>Magnetic Field B0 (mT) Delay  T (s) Magnetic Field (mT)<br>Echo signal (a.u.) Echo Sigal (a.u.)<br><!-- End of picture text -->

FIGURE 8.8: **Coil calibration** . **a** A comparison between the lineshape obtained by sweeping the output of the pulse generator used in DC mode (blue points) with _B_ 0 = 2 _._ 82 mT to the lineshape obtained by sweeping the DC coil bias (red points) yield the calibration of the magnetic field pulse. **b** (top panel) The time response of the coil is probed by reading out the spin echo signal for various delay times _T_ (left panel) after a step command pulse rising the magnetic field from _B_ 1 to _B_ 2. At very short times _T ⌧_ 0 _._ 01 s, an echo signal corresponding to the steady state _A_ ( _B_ 1) (right panel) is measured whereas for longer times _T >_ 1 s the echo signal corresponds to the steady-state _A_ ( _B_ 2) signal. In-between, due to the transient of the pulse, the readout does not occur at the same magnetic field as the excitation and thus we measure an echo signal less than the steady-state situation. From this a transient time of 1 s is inferred for the coils. 

For the experiment to be successful, the loss of polarization during the buffer times should be limited: _A_ Q( _T_ = 0) should be significantly smaller than _A_ Q( _T_ = _1_ ). This signal loss is minimized by purposely increasing the _T_ 1 at resonance, thanks to its angular dependence demonstrated earlier. We set _✓_ = _⇡/_ 4 and work on transition _|_ 9 _i $ |_ 10 _i_ with resonator _C_ so that _T_ 1(∆= 0) = 1 _._ 68 s. For values of ∆ ranging from 0.3 MHz to 4 MHz, _A_ Q(0) _/AQ_ ( _1_ ) varies from 0.2 to 0.5 since the coil response time is now on the order of _T_ 1 (0)<sup>_−_1</sup> , which leaves enough signal for the _T_ 1 measurements. 

##### **Spectral spin diffusion** 

Inversion recovery is not an ideal method to observe the long relaxation times we expect. Indeed, when the spin linewidth is broader ( _⇠⇥_ 20) than the excitation bandwidth and the thermalization time is very long, one can observe polarization mixing mechanisms [207, 4], spectral and spatial spin diffusion being the most relevant to our case as the system is only constituted from one species. For ∆ _/_ 2 _⇡_ = ( _!s − !_ 0) _/_ 2 _⇡_ = 3 _._ 8MHz _>_ ∆ _!_ , an inversion recovery sequence including a detuning pulse (see Fig. 8.10a) yields a double exponential relaxation (Fig. 8.10d, green), which we attribute to the existence of a spectral spin diffusion mechanism. 

One way to prevent spectral spin diffusion is to suppress any polarization gradient along the spin line by saturating the spins first to reach an incoherent mixed state with the population evenly shared between excited and ground states [5]. This is difficult to achieve in our experiment since the spin linewidth ∆ _!_ is 20 times larger than the resonator bandwidth. The simplest saturation recovery scheme (Fig. 8.10b) consists of sending a strong microwave tone at resonance, but a _T_ 1-relaxation measured with this scheme still yields a double-exponential decay (Fig. 8.10d, orange), with time 

129 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
a<br>Saturation Magnetic field pulse  B � Readout<br>AQ ( T )<br>T π /2 π echo<br>b saturation buffer time relaxation buffer time<br>1s 1s<br>T<br>4� tup td Spin echo<br>coil response readout<br>�<br>command<br>t<br>1/T1(0)<br>�<br>p<br>� t<br>1<br>p<br>0 t<br><!-- End of picture text -->

FIGURE 8.9: **_T_** 1 **(∆) measurement sequence** . **a** Saturation recovery sequence. The spins are saturated before being detuned by an amount ∆ for a time _T_ . A Hahn echo sequence reads out the subsequent spin polarization. **b** Illustration of the evolution of the polarization during the sequence. 

constants similar to the inversion recovery case. This implies that the saturation of the line is still partial. To improve the saturation, one can sweep the magnetic field during the saturation pulse so as to bring different subsets of the spin line to resonance and realize a full saturation. The adopted sweep scheme is shown on Fig. 8.10c. The corresponding relaxation curve now fits well to a simple exponential decay (Fig. 8.10d, blue), indicating the suppression of the spin diffusion effect. 

One can further check the quality of the saturation by measuring the polarization across the full spin linewidth immediately after saturation. To realize such scans (Fig. 8.10e), we apply the relevant saturation pulse at _!_ 0, then apply a magnetic field pulse _B_ ∆ = ( _!s − !_ 0) _/γe_ to measure the echo signal _AQ_ ( _!s_ ) at a different frequency _!s_ . When no saturation pulse is applied, the measured echo signal _AQ_ 0( _!s_ ) gives the full polarization _−hSz_ ( _!s_ ) _i_ = +1 (black curve) and shows the natural spin linewidth. With an excitation pulse, the polarization is _−hSz_ ( _!s_ ) _i_ = _AQ_ ( _!s_ ) _/AQ_ 0( _!s_ ), where _AQ_ ( _!s_ ) is the measured echo signal. Thus _−hSz_ ( _!s_ ) _i_ = _−_ 1 indicates a full inversion, _hSz_ ( _!s_ ) _i_ = 0 saturation and _−hSz_ ( _!s_ ) _i_ = +1 return to thermal equilibrium. The green, orange and blue curves are taken after respectively a _⇡_ pulse **(a)** and a saturation without field sweep **(b)** and with field sweep **(c)** . At resonance, one expects a change of _Sz_ from -1 to +1 for a _⇡_ pulse and from -1 to 0 for a saturation pulse. Due to the coil transient time, all three curves show partial relaxation. If the saturation was optimal and no partial relaxation was occurring, one should observe _Sz_ = 0 for all detunings ∆. Among the three sequences studied here, scheme **(c)** is the closest to saturating the line. For scheme **(b)** the spin saturation bandwidth is of _⇡_ 250 kHz and for the inversion scheme **(a)** the bandwidth _⇡_ 82 kHz is set by the resonator. This confirms that only in scheme **c** can spin diffusion be fully suppressed as confirmed by the observed simple exponential decay and we therefore use it to measure the ∆-dependent relaxation rates. 

##### **Experimental** ∆ **-dependent relaxation** 

The magnetic field pulse is followed by a spin-echo sequence to readout the polarization of the ensemble; the echo signal amplitude _A_ Q as a function of _T_ yields the spins energy relaxation time while they are detuned by ∆. 

130 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
π�� 5µs Magnetic field pulse  B � Readout Saturation Magnetic field pulse  B � Readout<br>a c<br>AQ ( T ) AQ ( T )<br>1s T 1s π /2 π echo 1s T 1s π /2 π echo<br>2<br>1<br>b Magnetic field pulse  B � Readout<br>0<br>AQ ( T ) -1<br>1s T 1s π /2 π echo -2<br>0 2 4 6<br>Saturation  1s<br>Pin= - 35.8 dBm Time (s)<br>e<br>d 1.0<br>1<br>0.8<br>8<br>0.6<br>0.4<br>T  = 1300s<br>1<br>8 0.1 TT11 ��  = 1100s, T= 800s, T1 � 1 = 110s � = 190s 0.2<br>0 0.5 1 1.5 2<br>-1.0 -0.5 0.0 0.5 1.0<br>Time (10 3 s)<br>( ω s- ω 0)/2 π�� (MHz)<br>(MHz)<br>π��<br>)/2<br>0<br>ω<br>-<br>s<br>ω<br>(<br>(0)]<br>Q<br>A - )0<br>) ω<br>if (<br>(  Q0<br>Q A<br>/<br>) ω s<br>(<br>Q<br>(T)] / [A A<br>Q<br>A<br>-<br>)<br>if<br>(<br>Q<br>[A<br><!-- End of picture text -->

FIGURE 8.10: **Spectral spin diffusion** . **a-c** _T_ 1 measurement sequence when spins are detuned from the cavity by applying a magnetic field _B_ ∆, providing a detuning ∆= _!s − !_ 0 = 2 _⇡γ_ e↵ _B_ ∆, with _γ_ e↵ = _df/dB_ ( _B_ 0). **a** uses a _⇡_ = 5 µs pulse to realize a so-called inversion recovery sequence, **b** and **c** are saturation recovery sequences: **b** uses a 1-s-long strong microwave pulse sent at cavity resonance whereas **c** has in addition a magnetic field scan shown on the bottom part. Depicted in orange is the expected magnetic field profile due to the the coil filtering, assuming the coil to be an order-1 low-pass filter of bandwidth 1-Hz. **d** _T_ 1 measurements for sequence **a** (green), **b** (orange), **c** (blue) for ∆ _/_ 2 _⇡_ = 3 _._ 8 MHz. Fits (black lines): **a** & **b** have a double exponential decay whereas **c** is a simple exponential. We attribute this double-exponential decay to spin diffusion. **e** Spectral profiles of excitation pulses **a** (green), **b** (orange) & **c** (blue). The sequence is as follows: send the excitation pulse, detune the spins and measure _AQ_ ( _!s_ ). Black line is the reference profile without any excitation pulse, yielding reference _hSz_ ( _!s_ ) _i_ = _−AQ_ 0( _!s_ ) _/AQ_ 0( _!s_ ). When an excitation pulse is sent, one can access _hSz_ ( _!s_ ) _i_ = _−AQ_ ( _!s_ ) _/AQ_ 0( _!s_ ). Note that neither the _⇡_ profile or the saturation profile reach either the full inversion +1 or full saturation 0 at resonance. This is an artefact due to the coil transient time. 

As evident in Fig. 8.11b, we find that the decay of the echo signal is well fit by a single exponential with a decay time increasing with _|_ ∆ _|_ . The extracted _T_ 1(∆) curve (see Fig. 8.11c) shows a remarkable increase of _T_ 1 by up to 3 orders of magnitude when the spins are detuned away from resonance, until it becomes limited by a non-radiative energy decay mechanism. The error bars come from the accuracy of the relaxation rates fits. 

The global fit shown on Fig. 8.11c is obtained by using equation _T_ 1(∆)<sup>_−_1</sup> = Γ _p_ + ΓNR which may be expressed as: 

131 

_Chapter 8. Controlling spin relaxation with a cavity_ 



<!-- Start of picture text -->
a Saturation Magnetic field pulse  B � Readout c<br>AQ ( T ) 10 3<br>π /2 π B =0.15 mT<br>b T echo �<br>1<br>10 2<br>�/2π� = 3.8 MHz<br>8<br>10 -1 10<br>1 MHz<br>0 MHz 0.38 MHz<br>8<br>10 -2 1<br>0 0.5 1 1.5 2 -4 -2 0 2 4<br>Delay  T  (10 3  s) �/2π (MHz)<br>(s)<br>1<br>T<br>(0)]<br>Q<br>A<br>)-<br>if<br>(<br>Q<br>A<br>)] / [<br>T<br>(<br>Q<br>A<br>)-<br>if<br>(<br>Q<br>A [<br><!-- End of picture text -->

FIGURE 8.11: **Controlling Purcell relaxation by spin-cavity detuning** . **a** In-between their saturation (see Figure 8.10c) and subsequent readout, the spins are detuned from the cavity by ∆=<sup>_d!_</sup> _dB_<sup><u>s</u></sup><sup>_B_∆by</sup> applying a magnetic field pulse of amplitude _B_ ∆, with 21 _⇡ d!dB_ <u>s</u><sup>_'_25GHz/Tforthistransitionand</sup> magnetic field. **b** Measured spin polarisation decays (dots) for four different detunings, well fit (lines) to exponential decays, with relaxation time constants _T_ 1 increasing with the detuning (Error bars: singleshot standard deviation (s.d.), n=2001). **c** Measured _T_ 1 as a function of detuning ∆, error bars are fit s.d. estimates, using resonator _C_ and with _✓_ = _⇡/_ 4. Blue points correspond to data acquired on the left peak of transition _|_ 9 _i $ |_ 10 _i_ (spins under the wire), the green point, to data acquired on the right peak of transition _|_ 9 _i $ |_ 10 _i_ (spins outside the wire) and the purple point, to data acquired on the left peak of transition _|_ 8 _i $ |_ 11 _i_ (spins under the wire). The solid red line is a fit to the blue data points with (Γ _p_ (∆) + ΓNR)<sup>_−_1</sup> , yielding Γ<sup>_−_</sup> NR<sup>1=1500</sup><sup>_±_100 s, grey area.These measurements are taken using</sup> resonator _C_ and with _✓_ = _⇡/_ 4, which results in _T_ 1 = 1 _._ 68 s at ∆= 0. In this experiment done in a separate run, the quality factor of resonator _C_ dropped from _Q_ = 1 _._ 07 _⇥_ 10<sup>5</sup> to _Q_ = 8 _._ 9 _⇥_ 10<sup>4</sup> due to slightly higher losses, yielding the resonator bandwidth _/_ 2 _⇡_ = 82 kHz. 



so that it involves only experimentally determined quantities. Indeed, __ is precisely determined by measuring the quality factor of the resonator<sup>3</sup> at low power; _T_ 1(0) is determined accurately by an inversion recovery sequence, and ∆ has been determined by the precise calibration of the coil pulse. The only remaining free parameter in the fit is thus ΓNR, yielding Γ<sup>_−_</sup> NR<sup>1= 1500</sup><sup>_±_100 s.</sup> 

##### **Non-radiative decay** 

We now discuss the possible non-radiative decay mechanisms in light of what is known about the relaxation of bismuth donors in silicon, as explained in ch. 4 (see 4.4.1). At the low temperatures of our experiment, direct phonon relaxation should be the dominant process. As explained earlier, Si:Bi energy levels are in general highly hybridized electro-nuclear spin states; as a result, their phonon relaxation rates in general involve complex combinations of _TS_ (electronic spin flip: ∆ _ms_ = _±_ 1, ∆ _mi_ = 0) and _TX_ (∆ _ms_ = _±_ 1, ∆ _mi_ = _⌥_ 1) processes. However, the _|_ 9 _i $ |_ 10 _i_ transition is somewhat special from that respect, as the _TX_ process is impossible and only the _TS_ process can contribute, which simplifies the discussion. In 4.4.1, we have derived by comparison to data on 

> 3In this experiment done in a separate run, the quality factor of resonator _C_ dropped from _Q_ = 1 _._ 07 _⇥_ 105 (given in Table 8.2) to _Q_ = 8 _._ 9 _⇥_ 10<sup>4</sup> due to slightly higher losses, yielding the resonator bandwidth _/_ 2 _⇡_ = 82 kHz. 

132 

_Chapter 8. Controlling spin relaxation with a cavity_ 

Si:P donors that a _Ts_ relaxation time on the order of 10<sup>5</sup> s is expected at zero-temperature, which turns out to be much larger than the 1500 s measured in our experiment. This seems to indicate that phonon relaxation is not likely to explain ΓNR. In addition, for transition _|_ 8 _i $ |_ 11 _i_ , as level _|_ 11 _i_ can relax to two ground states _|_ 7 _i_ and _|_ 9 _i_ with a different admixture of _Tx_ and _Ts_ processes, a different relaxation rate would likely be expected, instead of what we have measured the same non-radiative decay time (purple point shown in Fig. 8.11c). Note that another signature would also be a minor dependence on strain, on the order of a factor unity. We can test this by measuring the non-radiative decay for spins located outside the wire where the strain is different than under the wire. The measured decay Γ<sup>_−_</sup> NR<sup>1= 1800</sup><sup>_±_200 s (green point) is only slightly different than the value</sup> Γ<sup>_−_</sup> NR<sup>1= 1500</sup><sup>_±_100 s measured for spins under the wire (blue point), with a too large uncertainty for</sup> the test to be conclusive. 

We next discuss whether charge hopping (see 4.4.1) could explain our measured ΓNR. Indeed, interestingly, for similar concentrations of Si:P as our sample concentration in Si:Bi, Feher et al. showed that _T_ 1 at 1.25 K is decreased by several orders of magnitude compared to its low-concentration value [16]. They have attributed the effect to the activation of a spin exchange mechanism by the formation of clusters of Si:P donors at higher concentrations. It is difficult to estimate if this effect is relevant in our experiment since on one hand Si:Bi is a deeper and more confined donor than Si:P and thus the threshold concentration should be higher than for Si:P. On the other hand, charge hopping is enhanced in presence of ionized donors [16], as is the case in the experiment since the donors are partially ionized nearby the wire due to the Schottky barrier created in contact with the aluminum (see Fig. 7.2). Charge hopping thus appears as one of the possible candidates to explain our data. 

Last, as we have seen above with the imperfections of the inversion recovery sequence, spin diffusion mechanisms can occur. In the case of ΓNR, the mechanism would not be spectral spin diffusion but spatial spin diffusion. The spins outside the detection volume of the resonator remain polarized even after the microwave saturation and thus a polarization transfer to the saturated probed ensemble of spins located near the wire could take place, appearing in the measurement as a spin relaxation process. One very naive way of estimating this process is by using the measurements we have realized for spectral spin diffusion, as the underlying mechanism is identical. In our experiment, due to strain applied by the aluminum, the spatial and spectral distribution are linked: the ∆ _!/_ 2 _⇡_ = 2 MHz broad linewidth of the left side peak of transition _|_ 9 _i $ |_ 10 _i_ corresponds approximately to spins under the wire which occupy a volume of width 5 µm. With a _⇡_ -pulse of bandwidth 100 kHz, the spectral spin diffusion process takes place approximately in 100 s. Thus, if we were to saturate a spectral range of ∆ _!/_ 2 _⇡_ = 2 MHz one would roughly expect spin diffusion to occur on a timescale of 2000 s, which is indeed of the same order of magnitude as Γ<sup>_−_</sup> NR<sup>1.</sup> 

To conclude, the lack of measured values for bismuth in conditions similar to our experiment, the in-built strain and consequent broad spin linewidth as well as the ionized donors present in our experiment make the identification of the non-radiative decay mechanism quite difficult. Given the above discussion, we tentatively attribute this non-radiative decay to charge hopping spin relaxation, and(or) to spin diffusion. 

### **8.4 Conclusion** 

We have brought three independent experimental demonstrations that _T_ 1 in our experiment is limited by spontaneous emission. _T_ 1 at resonance was found to quantitatively match the Purcell formula; _T_ 1 was found to linearly depend on _g_<sup>_−_2</sup> ; and _T_ 1 was changed by 3 orders of magnitude by changing the spin-resonator detuning by only 2 MHz, again in quantitative agreement with Purcell formula. This Purcell relaxation could be used as an efficient method to re-initialize any spin in its ground state on-demand, which could be particularly useful in particular in Quantum Information Processing. The Purcell effect could also be used for dynamic nuclear polarization 

133 

_Chapter 8. Controlling spin relaxation with a cavity_ 

in magnetic resonance[208, 209]. In such schemes, the polarization of a nuclear state is built by cross relaxation on a electron-nuclear flip-flop transition. Cavity-induced relaxation would be an alternative to existing relaxation mechanisms or enhance the relaxation rate of this transition to improve the efficiency of the nuclear polarization. 

Even if our experiment takes place at low magnetic fields and low temperatures, such limits are not intrinsic to this scheme and the Purcell effect could be observed with a variety of other spin systems. Larger magnetic fields are possible if one uses superconductors with higher critical fields than aluminum. Resonators of high intrinsic quality factors have been demonstrated in a variety of materials (Nb, NbN[155, 156], NbTiN[157]) up to 1 T. On the other hand, temperature is important beyond the need for high quality factors. Spontaneous emission ensures relaxation to thermal equilibrium; low temperatures are required at the frequencies (7 GHz) used in this work for thermal equilibrium to correspond to a spin polarization higher than 99%. This limit could be lifted either by working at higher frequencies or at the price of reduced spin polarization. Note that operation at higher temperatures could make other relaxation mechanisms more efficient, reducing effectively the interest of cavity-enhanced spontaneous emission. 

On a more fundamental level, it is interesting to note that we reach here for the first time a regime where the vacuum fluctuations of the microwave field can have a marked effect on spin dynamics. In many systems (Rydberg atoms, quantum dots, ...), the observation of the Purcell-enhanced relaxation of individual emitters was the first step towards the application of the full range of concepts and ideas of cavity QED (strong coupling, ...), and it is tempting to assume that it will be the case as well for spins in solids [189]. To pursue this aim, a higher Purcell rate could be achieved by increasing the coupling of the spins to the microwave cavity. The wire dimensions could be reduced by a factor 50, yielding an increase of _g_ by the same factor and accessible _T_ 1 below the millisecond range. In addition to permitting faster repetition rates and a higher sensitivity, this would considerably enhance the cooperativity and allow to reach the regime of high cooperativity needed to observe coherent interactions between cavity and spin [70]. 

134 

## **Part IV** 

# **Squeezing-enhanced magnetic resonance** 

135 

## **Chapter 9** 

# **Squeezing-enhanced magnetic resonance** 

Quantum mechanics, through the Heisenberg uncertainty principle, imposes a minimum amount of noise in a measurement. When this limit is set by the vacuum fluctuations of the electromagnetic field, the measurement is said to be performed at the standard quantum limit. Such performance is routinely reached for optical measurements, and more recently for microwave measurements thanks to the use of JPAs, as shown for example in ch. 7 for ESR measurements. 

The standard quantum limit however is not as fundamental as the Heisenberg limits and can be overcome through the use of squeezed states for example. For these field states, whose properties were discovered in the 1970s by Stoler [210] and Yuen [211], the noise on one quadrature is reduced below the vacuum level, whereas the other one is correspondingly more noisy as required by Heisenberg uncertainty principle. In the optical frequency domain, where squeezing factors on the order of 12 dB are now produced [212], squeezed states were first proposed by Caves [18] and recently implemented [213, 31] to enhance the sensitivity of gravitational waves interferometric detectors. They have also been used for increasing the sensitivity of a number of other experiments, such as atomic absorption spectroscopy [214], atom-based magnetometry [32] and particle tracking of living systems [215]. In the microwave domain, while squeezed states were generated as early as 1989[12], it is only through more recent developments in CQED than a sufficient amount of squeezing was observed [216] to realize fundamental studies of light-matter interaction [217, 34] and enhanced sensing of a mechanical resonators [35]. 

In this chapter, squeezed microwave states are used for enhancing the sensitivity of ESR measurements. We review briefly the applications of squeezed states before explaining how they can be harnessed to enhance the sensitivity of an ESR experiment. We finally demonstrate the generation of squeezed states via the flux-pumped JPA presented in ch. 5 and their use in our ESR spectroscopy setup. 

### **9.1 Squeezing-enhanced measurements** 

#### **9.1.1 State-of-the-art** 

##### **Squeezing for enhanced measurement sensitivity** 

The noise reduction provided by a squeezed state can be harnessed to increase the sensitivity of a measurement [40]. Depending on the purpose, several schemes have been put forward [218]. A pioneering proposal due to Caves [18] suggests to use squeezed vacuum at one of the ports of an optical interferometer, in order to enhance the sensitivity of phase detection. A prominent motivation is the application of this idea to gravitational wave detectors. In this scheme, a Michelson 

136 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
10  -17<br>10  -20<br>m<br>10  -18<br>10  -21<br>10  -19<br>10  -22<br>100 1k 5k<br>Frequency (Hz)<br>Laser<br>m<br>Y<br>Squeezed state<br>X<br>–1/2)<br>GW-strain (Hz<br>Observatory noise, calibrated to  test mass displacement (m Hz)–1/2 Observatory noise, calibrated to<br><!-- End of picture text -->



FIGURE 9.1: **Squeezing-enhanced interferometric gravitational detector.** Schematic of Caves proposal (adapted from [18]) where a squeezed state sent on the dark port of the beam-splitter (in blue) can enhance the detection of the floating mirrors displacement (green, see picture on the left for LIGO implementation). (right) Demonstration of squeezing enhanced detector sensitivity on the GEO600 instrument. [213] 

interferometer is used to detect the relative displacement of two heavy masses _m_ as depicted in Fig. 9.1. A laser beam, split in two via a beam splitter, bounces a number of times in each arm between two reflecting mirrors, one being fixed while the other is attached to a mass _m_ . Detecting the light outcoming of each arm via photo-detectors thus yields information on the relative mass displacement. To understand where the usefulness of squeezed states arises, it is important to realize that the beam-splitter used to separate the laser in two coherent lights beams is actually a four-port device, connecting two input modes to two output modes. The first input port is used for the incoming light, while the second input port sees the vacuum state. Caves showed that the sensitivity of the measurement is heavily linked to the vacuum fluctuations arising at this second port [18]. Replacing the vacuum state by a squeezed vacuum state could thus improve the sensitivity of the measurement, as was shown recently by the LIGO collaboration with _⇡_ 2 _._ 5 dB enhancement over a large frequency range (see Fig. 9.1). 

The use of squeezed-states for interferometric measurements generally relies on decreasing the vacuum fluctuations at the dark port of a beam-splitter [19]. The general strategy in all measurement is to adopt a scheme that combines the measured signal to the squeezed-state reduced vacuum fluctuations without signal degradation. An interesting device in this context is the asymmetric beam-splitter (known as directional coupler in microwave engineering), which allows to produce arbitrarily displaced squeezed states with preserved noise reduction. In atomic-absorption microscopy [214], atom-based magnetometry [32] and particle tracking of living systems [215], a displaced squeezed state is created via such an asymmetric beam-splitter to probe the system of interest and improve the measurement sensitivity. Similarly, for enhanced mechanical resonator sensing [35], a displaced microwave squeezed state is produced via a 20-dB coupler to probe the opto-mechanical system. More complex schemes also exist, such as the two-modes squeezing proposed for enhanced superconducting qubits readout [219, 220]. 

137 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
a X2 b X2 X1δt X2 X2 c X2 X2 X2<br>φ X1 X1 δt X 1 X1 X1<br>2.0<br>X1 1.5 TT xy T2zT 1 1.5<br>Pump  1.0 T x<br>3D transmon 1.0 T<br>y<br>T z<br>Squeezed vacuum 0.5 0.5<br>0.0 0.0<br>–0.4 0.0 0.4 0.0 5.0 0.1 5.1 0.2 5.2<br>δ/2π (MHz) N<br>Parametric<br>amplifier<br>s) s)<br>μ μ<br>Decay time ( Decay time (<br><!-- End of picture text -->

FIGURE 9.2: **Radiative decays in squeezed vacuum.** Adapted from [217]. A squeezed-vacuum generated by a JPA is shined on a transmon (panel **a** ) whose longitudinal and transversal radiative lifetime are modified according to Gardiner’s theory (panels **b** & **c** ). 

##### **Squeezing effects in light-matter interaction** 

When a squeezed state field is incident on a two-level-system, Gardiner showed that the damping rates of the TLS are largely modified in presence of squeezing [221]. Consider a TLS described by the Pauli operators _σ_ ˆ _i_ irradiated with a broad-band incident squeezed-state of parameters _N_ and _M_ given in ch. 2. If the TLS decay is radiatively limited with a decay time _γ_ in absence of squeezing, Gardiner showed that the equations of motion for _hσ_ ˆ _xi_ , _hσ_ ˆ _yi_ and _hσ_ ˆ _zi_ become in presence of squeezing [221]: 



The consequences are dramatic for the transverse decay rates _γx_ and _γy_ since they are respectively enhanced and inhibited by the same ratios than the amplified and squeezed quadratures. In the same time, the longitudinal decay rate _γz_ is increased by a factor 2 _N_ +1, with a reduced steady-state polarization 1 _/_ (2 _N_ + 1), as would be the case if a thermal state with the same mean photon number _N_ was impinging on the TLS. These variations on the TLS fluorescence were recently observed experimentally employing superconducting qubits [217, 34], as shown in Fig. 9.2. 

#### **9.1.2 Squeezed states for magnetic resonance** 

To understand how squeezed states can be harnessed to improve the sensitivity of an ESR measurement beyond the vacuum fluctuations limit, consider the scheme depicted in Fig 9.3a. It is very similar to the setup described in earlier chapters: a sample containing an ensemble of spins is embedded inside a microwave resonator of frequency _!_ 0 and cooled to millikelvin temperatures so that the electromagnetic field reaches its ground state. By applying a static magnetic field **_B_** 0, the spins can be tuned to resonance with the ESR resonator. The latter is coupled with rate _c_ to a single measurement line supporting incoming ( _a_ ˆin) and outgoing ( _a_ ˆout) field modes. After application of a _⇡/_ 2 _− ⌧ − ⇡_ sequence to the spins, an echo is emitted at time 2 _⌧_ in the output measurement line. The echo is then amplified and detected at frequency _!_ 0 by homodyne detection with a local oscillator phase chosen so that the echo lies only on one of the two field quadratures _I_ and _Q_ , for instance _I_ . 

As explained in ch. 5, the use of a JPA operated in phase-sensitive mode in the detection chain ensures that a major part of the noise detected on the _I_ quadrature arises from the fluctuations of 

138 



<!-- Start of picture text -->
a<br><!-- End of picture text -->





_Chapter 9. Squeezing-enhanced magnetic resonance_ 

_'j_ = ∆ _j_ ( _t_ + 2 _⌧_ ), refocused by the _⇡_ pulse applied at time _t_ = _−⌧_ which then leads to the echo signal at time _t_ = 0. 

We shall now describe the spin lowering and raising operators as oscillator annihilation _s_ ˆ<sup>_†_</sup> _j_<sup>and</sup> creation ˆ _sj_ operators obeying [ˆ _sj,_ ˆ _s_<sup>_†_</sup> _k_<sup>] =</sup><sup>_δk,j_following the so-called Holstein-Primakov approxima-</sup> tion [71, 222, 223, 224], valid when each spin of the ensemble is only weakly excited. Eq. 9.4 now yields: 



Following a similar treatment that the derivations of Eqs. 3.41-3.44, the spin equations of motion are: 



where the term _↵e_<sup>_−i_∆</sup><sup>_j⌧_</sup> _δ_ ( _t_ + _⌧_ ) describes the spins initial coherent excitation giving rise to the echo and _Fj_ ( _t_ ) is the quantum Langevin noise term associated to spin relaxation at the rate _γ_ , with a zero mean-value. Fourier transforming both equations<sup>1</sup> yields: 





These equations can be solved, which yields: 



To simplify this equation, we consider a Lorentzian distribution of width _w_ : _⇢_ (∆) = ∆<sup>2</sup> _w_ + _<u>/w</u>_ 2 _⇡_<sup>2</sup> _/_ 4<sup>.</sup> Replacing the sum by an integral, the denominator of Eq. 9.9 simplifies in: __<sup>_wN_spins</sup> (9.10) 2<sup>_−i!_+</sup><sup>_g_2</sup> _!_<sup>2</sup> + _w_<sup>2</sup><sup>_/_4</sup> 

In the case of a spin ensemble such that is cooperativity _C_ =<sup>2</sup> _w_<sup>_<u>g</u>_</sup> <u>ens</u><sup>2</sup><sup>_⌧_1, the term</sup><sup>_g_2</sup> _!_<sup>_wN_2</sup> +<sup>s</sup> _w_<sup><u>pins2</u></sup><sup>_/_4can be</sup> ˆ neglected. Using the input-output equation ˆ _a_ in + ˆ _a_ out =<sup>_p_</sup> _<u>a</u>_ (neglecting any internal losses), we can now express the output field as: 



where we have defined the total spin noise Langevin term as _F_<sup>˜</sup> tot( _!_ ) = R∆<sup>_⇢_(∆)</sup> _<u>p</u>_ 2 _γγ_ + _F_<sup>˜</sup> _i_ <u>(∆</u> _!−,_ ∆ _i!_ <u>)</u> _d_ ∆ . The first term, being the only one with a non-zero expectation value, describes the emission of the echo signal into the measurement line. In the weak coupling limit, the spin noise term is also smaller than the third term which describes the input field quantum fluctuations. 

Eq. 9.11 confirms our earlier qualitative argument: the expectation value of the output field is the echo signal unaffected by the quantum statistics of the input field _a_ in; but its fluctuations are governed by the input field, be it in the vacuum or in a squeezed state. We stress that throughout the derivation we have used the weak coupling condition _C ⌧_ 1. Properly expressing the enhancement of the SNR gained by having an incoming squeezed-state during the echo emission requires reverting to the time-domain and choosing a mode filter function, as explained in ch. 5. Nonetheless, Eq 9.11 

> 1The chosen convention in this manuscript is : _f_ ˜( _!_ ) = R _dte_<sup>_i!t_</sup> _f_ ( _t_ ) and _f_ ( _t_ ) = 21 _⇡_ R dte<sup>_−_i</sup><sup>_!_t˜</sup> f( _!_ ). 

140 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
a b<br>Y<br>p 2 n th + 1<br>pG<br>p 2 n th + 1 4<br>4<br>φ<br>1 p 2 n th + 1 X<br>p G 4<br>1<br>N +  M  cos( φ ) + 1<br>2 p 2 2<br>ˆ<br>b<br>ˆ<br>b<br>ˆ<br>b<br>1<br>⌘<br>Y<br>X<br>Y<br>Y<br>X<br>X<br>2<br>out<br>1<br><!-- End of picture text -->

FIGURE 9.4: **Squeezed vacuum. a** Squeezed state produced by a phase-sensitive amplifier of power gain _G_ whose input is a thermal state of occupancy _n_ th, fully characterized either by _G_ and _nth_ or by the numbers _N_ and _M_ defined in Eqs. 2.17 & 2.18. **b** Attenuation of a squeezed state. 

is sufficient to evidence that an input field with a quadrature squeezed by a factor _⌘S_ is expected to enhance of the SNR by a factor<sup>_p_</sup> _<u>⌘S</u>_ . 

### **9.2 Detecting and characterizing microwave squeezed states** 

#### **9.2.1 Microwave squeezed-states** 

At microwave frequencies, a squeezed vacuum state can be generated by a parametric amplifier used in phase-sensitive mode, as explained in ch. 2. If the parametric amplifier input field is a thermal vacuum state of occupancy _n_ th, we recall that for a gain _G_ the squeezed state variances are (see Fig. 9.4a): 



where _X_<sup>ˆ</sup> _φ_ and _Y_<sup>ˆ</sup> _φ_ are respectively the deamplified and amplified quadratures, relative to the choice of the phase _φ_ of the JPA pump tone compared to the detection quadratures _X_<sup>ˆ</sup> and _Y_<sup>ˆ</sup> . 

Microwave squeezed states are well-known to be fragile, and in particular are susceptible to losses encountered during their propagation. Attenuation by a factor _⌘_ is generally modeled as the action of a beam-splitter of finite transmission _⌘_ , with the vacuum at the other port (see Fig. 9.4b). The relations linking the input and output fields of a beam-splitter is: 



If on the port<sup>ˆ</sup> _b_ 2 is impinging a thermal state of occupancy _n_ th identical to the squeezed state _h_ ∆ _X_<sup>ˆ</sup> 2<sup>2</sup><sup>_i_= (2</sup><sup>_n_th+ 1)</sup><sup>_//_4, then the outcoming squeezed state has a reduced degree of squeezing:</sup> 



141 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
a 20 mK 4 K 300 K<br>I, Q<br>SQZ AMP HEMT 300K<br>signal<br>ω��φ in<br>50  � 50  �<br>c<br>b<br>LO ω��φ LO<br>Q<br>RF<br>SQZ AMP<br>I<br>2ω��φ S SQZ flux pump  AMP flux pump  2ω��φ A<br>Fast DAC<br>Acquiris<br><!-- End of picture text -->

FIGURE 9.5: **Experimental setup for SQZ characterization. a** Two JPAs are mounted in series: the first generates a squeezed vacuum state while the second ensures its noiseless detection **b** Circuit view of (panel **a** ). **c** The detection is performed via homodyne detection. The bandwidth of the filters preceding the acquisition card was chosen significantly smaller than the JPAs bandwidths ( _⇥_ 10). 

#### **9.2.2 JPA as a squeezing generator** 

To generate a microwave squeezed-state, we use the flux-pumped JPA presented in ch. 2 and characterized in ch. 5. We first characterize the squeezed vacuum generated by the JPA with a simplified setup that does not include the ESR resonator nor the spins (see Fig. 9.5a), very similar to the one used in [216]. A second JPA device, noted SQZ, is operated in phase-sensitive mode to generate a squeezed vacuum state (blue device), whose squeezed quadrature is set by its pump tone phase _φs_ . To characterize the emitted radiation noise properties of this state, we use the same amplification chain described and characterized in ch. 5, comprising the same JPA device, noted AMP (purple device) in the following, followed by amplification at 4 K and 300 K. 

Using the AMP in phase-sensitive mode ensures noiseless amplification on one quadrature set by its pump phase _φA_ (see ch. 2) . Using homodyne detection, with a local oscillator phase _φ_ LO chosen so that the amplified quadrature corresponds to the _I_ quadrature, one can relate the quantum fluctuations of the input AMP field quadrature _X_<sup>ˆ</sup> _φA,_ in to the _I_ quadrature noise _h_ ∆ _I_<sup>2</sup> _i_ , see ch. 2. 

When the SQZ pump is turned on with no incident signal, a squeezed vacuum state is generated at the AMP input, replacing the vacuum state. If the relative pump phase _φS − φA_ = _⇡/_ 2, the squeezed quadrature is aligned on the amplification quadrature and thus _I_ quadrature noise can be expected to be below the quantum limit. For all phase settings, the noise is related to the variance of the squeezed state by Eq. 2.14. 

##### **SQZ characterization** 

We first characterize the SQZ as explained earlier for the JPA, with the flux-tunability of its resonance frequency and its average phase-dependent gain. Applying the same voltage to both flux-lines at the same time, the reflexion coefficient shows the SQZ and AMP 2 _⇡_ phase shifts associated to their respective resonance frequencies (see Fig. 9.6a). In the remainder of this chapter, we choose their DC bias so that _!_ 0 _/_ 2 _⇡ ⇡_ 7 _._ 3 GHz (grey dashed line in Fig. 9.6a). 

142 



<!-- Start of picture text -->
“4, rd % 3 %<br>rn ry % l J [o} &o ® © So)<br>xeAVE4 o]  SS BE20 &» og® i ilso<br>bf £ i¢ <5 o oe 8% 4 eles<br>lod®7 0 °g°, o aT<br>| £ °%s 8 2d<br>H o © S<br>SRLS 1<br>O (0 |<br>—~ f o V C<br>“© — O. |! O<br>oOo<br>a. ©<br>( acs ) i<br><!-- End of picture text -->

_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
a 1 b<br>Y Y<br>0.05<br>SQZ<br>X X<br>0<br> Pump OFF<br>-0.05 Gs= 5.8 dB Gs= 14.7 dB<br>� = -1.3 dB Gs= 9.2 dB Gs= 20 dB<br>0<br>0 1/G 2 S 1 -0.3 -0.2 -0.1 Xout 0.0(V) 0.1 0.2 0.3<br>S<br>�<br>(V)<br>out<br>Y<br>Squeezing factor<br><!-- End of picture text -->

FIGURE 9.7: **Squeezed vacuum distortion** . **a** Squeezing factor _⌘S_ as a function of _G_<sup>_−_</sup> _S_<sup>1,allowingto</sup> extract the setup microwave losses _⌘_ by a linear fit. **b** Squeezed vacuum distortion at high gains. The data is acquired by varying the phase of a small input coherent signal and measuring the averaged output field quadratures. The corresponding measured squeezing factors are indicated by the arrows in panel **a** . 

The background noise is measured by switching both SQZ and JPA off and is mainly set by the noise of the HEMT amplifier, as shown in ch. 5. For the data shown in Fig. 9.6d, _⌘S_ = _−_ 4 _._ 1 dB. 

##### **Limitations to squeezing** 

The data shown in Fig. 9.6d correspond to the maximum amount of squeezing obtained, far from the 20 dB squeezing that one could naively expect from Eq.2.14, and we will now explain why. Repeating the experiment for several SQZ gains settings, we notice that the degree of squeezing is systematically smaller than the deamplification factor _⌘S_ 6 _G_<sup>_−_</sup> _S_<sup>1, as shown in Fig. 9.7a.At low gains,</sup> _⌘S_ depends linearly on _G_<sup>_−_</sup> _S_<sup>1, as expected from Eq. 9.15 for degradation due to attenuation.Fitting</sup> the linear dependence according to Eq. 9.15 yields a total microwave attenuation of _⌘_ = _−_ 1 _._ 3 dB. This value is compatible with the setup of Fig. 9.5b, where losses are mainly set by the circulator insertion losses (2 _⇥_ 0 _._ 4 dB), the 1-m-long copper coaxial cables linking SQZ and AMP ( _⇡_ 0 _._ 3 dB) and the on-chip losses ( _⇡_ 0 _._ 1 dB). 

At high gains, a departure from linearity is observed, with an increase of _⌘S_ that we attribute to nonlinearity induced in the SQZ resonator by the Josephson junctions used to modulate the resonator frequency (see ch. 2 and [55]). To confirm this hypothesis, we measure the output quadratures _hX_<sup>ˆ</sup> out _i_ and _hY_<sup>ˆ</sup> out _i_ of a small input signal amplified by the SQZ in phase-sensitive mode as a function of its input phase (see Fig 9.7b). When the phase runs from 0 to 2 _⇡_ , plotting _hY_<sup>ˆ</sup> out _i_ versus _hX_<sup>ˆ</sup> out _i_ emulates the shape of the produced squeezed vacuum. When the SQZ is off, a perfect circle is observed. As long as the squeezing factor varies linearly as a function of _G_<sup>_−_</sup> _S_<sup>1, the squeezed vacuum</sup> is ellipsoidal as expected (red curve). For higher gains, a progressive distortion of the ellipse (green, blue and purple curves) is observed which eventually leads to the increase of _⌘S_ . In the following, we thus choose moderate values of _Gs_ which lead to the maximum _⌘S_ . 

##### **Noise reduction optimization** 

The total noise reduction factor _⌘_ tot is smaller than _⌘S_ because the total output noise is not only due to the amplified quantum noise, but also contains a small "background" contribution from the HEMT. This contribution can be minimized by working at high AMP gains. However, as shown in ch. 5, the AMP eventually saturates at high intra-resonator photon number, once again due to the non-linearity induced by the Josephson junctions. We have experimentally observed that even a weakly distorted squeezed state impinging on the AMP can lead to its saturation for high _GA_ . The best achievable _⌘_ tot thus results from an exhaustive simultaneous optimization of _GA_ and _GS_ . 

144 



<!-- Start of picture text -->
wr S OH O a<br>HT — - =<br>- L_| = =<br>- K |<br>( = Bs<br><!-- End of picture text -->









<!-- Start of picture text -->
00000006, oI% F | 2_ RK) %y + °wg?<br>ei 09° %, i S<br><!-- End of picture text -->

_Chapter 9. Squeezing-enhanced magnetic resonance_ 

To ensure that the squeezed quadrature variance _hX_<sup>ˆ2</sup> _iφS_ =0 is reduced below the vacuum fluctuations level _hX_<sup>ˆ</sup> 0<sup>2</sup><sup>_i_=</sup><sup><u>1</u></sup> 4<sup>,anabsolutecalibrationoftheunsqueezedfieldisneeded.Thiscalibrationwas</sup> carried out by Philippe Campagne-Ibarcq using a transmon qubit, and is described in Appendix A. It yields _n_ th = 0 _._ 05 _±_ 0 _._ 05. As seen in ch. 2, the thermal vacuum fluctuations level is given by _hX_<sup>ˆ</sup> th<sup>2</sup><sup>_i_=</sup> <u>2</u> _<u>n</u>_ <u>th4 +1</u> and thus the squeezed quadrature variance is reduced below the vacuum fluctuations level by a factor: 



Given that _⌘S_ = 0 _._ 66, we conclude that the field fluctuations are 0 _._ 73 _±_ 0 _._ 06 times the vacuum fluctuations, thus reaching the regime of true quantum squeezing. It is comparable to other values reached in the literature: for example Mallet et al. achieved a squeezing of 0 _._ 68 _±_ 0 _._ 09 times the vacuum fluctuations [216]. 

#### **9.2.4 Detection of displaced squeezed states** 

Finally, to validate our experimental setup and parameters, we simulate the echo emission by sending a small coherent pulse through port 1 of the ESR resonator, as depicted in Fig. 9.9a. The phase of the input pulse is set so that the detected signal lies entirely on the _I_ quadrature, corresponding also to the squeezed quadrature. The detected field amplitude with SQZ on and off for different input powers is shown in Fig. 9.9a. For moderate signal amplitude, the noise histogram shows the same noise reduction _⌘_ tot = 0 _._ 77 as without a coherent signal (Fig. 9.9b), as expected. 

However for larger input signals, the SQZ on amplitude is a few percents lower than the SQZ off one. We explain this signal degradation once again by the saturation of the JPA devices caused by its Josephson junctions, as already shown in Fig. 9.7. Here, the non-linearity manifests itself in a slightly different way: the output signal phase becomes dependent on the input field amplitude. 



<!-- Start of picture text -->
a  SQZ pump ON Y c Y Y<br> SQZ  p ump OFF AMP �� v<br>X AMP X X<br>0.10 0.8<br>b 5 0.6<br>4 0.4<br>0.2<br>0.05 3<br>0<br>20<br>2<br>10<br>1<br>0<br>0<br>0<br>0 500 -0.5 0 0.5 0 0.05 0.10 0.15<br>Time (µs) I quadrature (V) Ain (V)<br>Ain<br>=12 dB<br>GA<br>Aout<br>3)0<br>1<br>( stn<br>u<br>o<br>C<br>I quadrature (V)<br> (°)<br>��<br>(V)<br>out<br>A<br><!-- End of picture text -->

FIGURE 9.9: **Displaced squeezed vacuum state. a** Coherent pulses of varying powers sent through port 1 are measured with (red) and without squeezing (blue). For low powers, the expected noise reduction is observed (panel **b** ) but at large powers, the output amplitude is reduced when the SQZ is switched on. **c** The effect is explained by the saturation of the AMP, with an important phase deviation due to the Josephson junctions non-linearities. 

146 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 

The amplitude fluctuations of the displaced squeezed state being larger than the ones of a coherent state of same average amplitude causes the observed difference. To avoid this detrimental effect in our experiment we thus intentionally choose to limit the spin-echo amplitude, as explained below. 

### **9.3 An ESR signal emitted in squeezed vacuum** 

#### **9.3.1 Squeezing-enhanced ESR: proof-of-principle** 

We now proceed to the demonstration of squeezingenhanced ESR detection. For this experiment, we use the lowest-frequency spin transition _|_ 9 _i $ |_ 10 _i_ and first characterize the spin-echo with SQZ off. A Hahn-echo field sweep is shown in Fig. 9.10. 

The spin-resonance is found at the expected field _B_ 0 _⇡_ 2 _._ 8 mT; however its shape is significantly different from the one reported in previous chapters. In particular, the double-peak structure is barely visible. This is due to a combination of several factors. The Purcell relaxation time _T_ 1<sup>_−_1</sup> = (2 _n_ th + 1)(4 _g_<sup>2</sup> _/_ ) is now one order of magnitude longer due to the lower resonator quality factor used. As explained in ch. 8, _T_ 1 is longest on the upper field peak, where it now reaches _⇡_ 70 s, thus necessitating a repetition time of _⇡_ 300 s to measure the whole spin resonance without distortion. For practical reasons, we decided to perform this measurement with a shorter repetition time 15 s, which leaves the low-field peak undistorted but strongly reduces the upper-field peak. To minimize the amplitude of the emitted echo signal for the reasons explained earlier, we set _B_ 0 = 2 _._ 6 mT, on the "tails" of the low-field peak. 



<!-- Start of picture text -->
� �<br>π /2 π echo<br>0.6<br>0<br>2.6 2.8 3.0 3.2<br>Magnetic field B0 (mT)<br>echo signal (V)<br><!-- End of picture text -->

FIGURE 9.10: **Hahn-echo field sweep** with calibrated _⇡/_ 2 and _⇡_ pulses. 

The experiment consists in repeating a spin-echo sequence ( _R✓ − ⌧ − ⇡ − ⌧ −_ echo) with the SQZ on and off. To limit the spin-echo amplitude even further, we choose a Rabi angle _R✓ ⇡ ⇡/_ 3 for the excitation pulse instead of a _⇡/_ 2 pulse. The SQZ pump is switched on during a time window of 200 µs around the expected echo emission at _t_ = 2 _⌧_ (see Fig. 9.11a-b). The phase of the excitation pulse is set such that the echo signal lies entirely on the _I_ quadrature, on which is also aligned the squeezed quadrature. 

To minimize setup drifts during the six-hour-long acquisition, we alternate echos acquired with SQZ on and off and we use phase-cycling as shown in Fig. 9.11b. We acquire _N_ avg = 2500 echos with SQZ on and 2500 SQZ off. The quadrature voltage _I_ ( _t_ ) is digitized at a sampling rate of 1 pt/µs with an acquisition bandwidth of 300 kHz. The data is recorded on a time window _T_ = 200 µs centered on the echo. The waiting time between each echo sequence is taken to be _T_ rep _⇡_ 5 _T_ 1 = 5 s. Time traces of the digitized _I_ ( _t_ ) quadrature are shown in Fig. 9.11c with the echo barely visible in single-shots traces. The averaged signals are computed as: 



where subscripts ( _j_ ) are indicated in Fig. 9.11b. As can be seen in Fig. 9.11c, the averaged echoes for SQZ on and off are identical, showing that JPA saturation effects have been indeed avoided. 

147 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
a b (1) R � (2) R −� (3) R � (4) R −�<br>echo SQZ on SQZ on SQZ off SQZ off<br>R � Y π t X 2 � 5 T1 5 T1 5 T1 5 T1<br>X Y<br>Y<br>pump<br>X SQZ<br>π /3 π echo<br>c d 10<br>0.1<br>0.0<br>5<br>-0.1<br>FWHM<br>0.24<br>0<br>0.12<br>380 400 420 -0.3 0.0 0.3<br>Time t (µs) I quadrature (V)<br>0<br>1<br>( st<br>n<br>u<br>o<br>C<br>3)<br>I quadrature (V)<br>FWHM (V)<br><!-- End of picture text -->

FIGURE 9.11: **Squeezing enhanced echo emission. a-b** Acquisition sequence representing the detected field quadratures. The excitation pulse _R✓_ followed by a _⇡_ pulse _⌧_ = 200 µs later triggers the emission of an echo at time 2 _⌧_ . The SQZ is turned on just during the echo emission. The sequence is acquired four times to use phase-cycling and compared echo with SQZ on and off. **c** (top) Echo signal with SQZ on (red) and off (blue). Dash-dotted lines show the single-shot signal. (bottom) Full-width half maximum for identical time stamps. **d** Noise histograms of the _I_ quadrature measured during the echo emission, with SQZ on (red curve) and on (blue curve), fitted with Gaussian distribution (grey dashed lines). 

Noise histograms in Fig. _I_ ¯ON( _t_ ) _, 8i, 8t}_ when the SQZ is on and 9.11d are computed from the bins _{I_ (3) _,i_ ( _t_ ) _− I_ ¯OFF( _t_ ) _, 8 {i, 8I_ (1) _t} [ {,i_ ( _t_ ) _−I_ (4) _I_<sup>¯</sup> _,i_ ON( _t_ ) +( _t_ ) _, 8I_ ¯OFF _i, 8t_ ( _} [ {t_ ) _, 8i,I 8_ (2) _t,i}_ and( _t_ ) + are very close to the ones displayed obtained in Fig. 9.9b for a displaced vacuum squeezed state. In particular the same noise reduction factor of _⌘_ tot = 0 _._ 77 is observed. To ensure the echo emission is not affecting the noise properties, we have also computed the noise histograms and variances keeping only identical stamping times _t_ and found no variations (see Fig. 9.11c). 

To compute the SNR for both echoes, we use the same procedure explained in ch. 5 where the mode filter function _u_ is chosen to be the echo signal _u_ ( _t_ ) _/_ [ _I_ ON( _t_ ) + _I_ OFF( _t_ )] _/_ 2. For each echo ( _j_ ) of each sequence _i_ , we can thus evaluate the signal and noise quantities as _hI_ ( _j_ ) _,ii_ and _h_ ∆ _I_ (<sup>2</sup> _j_ ) _,i_<sup>_i_.Averaging</sup> over all recorded echoes yields the noise and echo signal shown in Table 9.1, demonstrating a rms noise reduction by 11%. Repeating the same procedure for the tophat _u_ function of width 20 µs centered on the echo used in ch. 7 yields similar results. 

#### **9.3.2 Absolute sensitivity** 

Similarly to the analysis done in ch. 7, the number of spins contributing to the signal _N_ spins can de determined by numerical simulations. In ch. 7, the spin distribution at the peak of the spin 

148 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 

|_u_(_t_)||Echo s|hape|To|phat func|tion|
|---|---|---|---|---|---|---|
|SQZ|_hIi_|~~p~~<br>_h_∆_I_<sup>2</sup>_i_|SNR|_hIi_|~~p~~<br>_h_∆_I_<sup>2</sup>_i_|SNR|
|OFF|0.179|0.202|0.886|0.161|0.202|0.797|
|ON|0.177|0.181|0.973|0.160|0.181|0.884|
|ON/OFF ratio|0.988|0.897|1.10|0.992|0.894|1.11|



TABLE 9.1: **Squeezing-enhanced SNR for the echo signal** 



<!-- Start of picture text -->
a Inversion Readout b<br>echo<br>T AQ ( T )<br>π /2 π<br>π π /2 π echo<br>1 0.6<br>0.4<br>0<br>T = 2.5±0.1 s 0.2<br>1<br>T = 0.90±0.07 s<br>1<br>-1 0.0<br>0 4 8 12 190 200 210 220<br>Time (s) Time (us)<br>Amplitude (V)<br>)<br>=<br>T<br>(<br>Q<br>A<br>) /<br>T<br>(<br>Q<br>A<br><!-- End of picture text -->

FIGURE 9.12: **Number of spins characterization** . **a** Spin relaxation times measured using inversion recovery at _B_ 0 = 2 _._ 6 mT (red circles) and _B_ 0 = 2 _._ 8 mT (blue squares), well fit by exponential decays (solid lines) allowing to extract _g_ to perform numerical simulations. **b** Echo time traces for _B_ 0 = 2 _._ 6 mT (red circles) and _B_ 0 = 2 _._ 8 mT (blue squares), reproduced via numerical simulations (solid lines). 

line ( _B_ 0 = 2 _._ 8 mT) was found to be adequately modeled with a Gaussian distribution of _g_ with mean value _g_ 0 _/_ 2 _⇡_ = 56 Hz and FWHM ∆ _g/_ 2 _⇡_ = 1 _._ 5 Hz, as well as a square distribution of the spin detuning of width largely exceeding the resonator bandwidth. Repeating the numerical simulations for resonator _B_ parameters, we find the number of excited spins at _B_ 0 = 2 _._ 8 mT to be _N_ spins(2 _._ 8mT) = 1 _._ 2 _⇥_ 10<sup>5</sup> . 

As discussed in ch. 6, _g_ depends on the magnetic field _B_ 0 due to the strain exerted by the aluminum wire on the silicon introducing a correlation between the spin spectral distribution and the spin spatial distribution (see Fig. 6.6 for example). We estimate the difference in _g_ between 2.6 and 2.8 mT by comparing _T_ 1 at these two fields. As shown in Fig. 9.12a, we find _T_ 1(2 _._ 6 mT) = 0 _._ 9 s and _T_ 1(2 _._ 8 mT) = 2 _._ 5 s, implying that _g_ 0(2 _._ 6 mT) _/_ g0(2 _._ 8 mT) =1.7. Calibrating _g_ by comparing the Rabi oscillation frequency for same input power yields the same factor (not shown). Running once again the numerical simulations with _g_ 0(2 _._ 6 mT) _/_ 2 _⇡_ = 93 Hz to simulate the echo emission at _B_ 0 = 2 _._ 6 mT, we find that _N_ spins(2 _._ 6 mT) = 4 _._ 7 _⇥_ 10<sup>3</sup> reproduces the experimental echo amplitude (see Fig. 9.12b). Associated to the SNR estimation above, this analysis yields a minimal number of detectable spins in one echo sequence _N_ min = 1 _._ 3 _⇥_ 10<sup>4</sup> with SQZ off, improved to 1 _._ 1 _⇥_ 10<sup>4</sup> with the SQZ turned on. It corresponds equivalently to a reduction of the acquisition time by 24%. 

Note that determining _g_ using the Purcell relation with the experimentally determined _n_ th and __ yields the value _g_ (2 _._ 8 mT) _/_ 2 _⇡_ = 65 Hz, 10% larger than estimated in ch. 6. We attribute this difference to the better determination of __ due to the fact that we are now operating in the overcoupled regime where __ int has a minor contribution. In the previous measurements, __ int may have been under-estimated by a measurement at too high power that saturates the TLS lying at 

149 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 

the metal-substrate interface and thus neglects their contribution to the resonator internal losses; a measurement of __ int at input powers corresponding to intra-cavity fields close to 1 photon would have been preferable (see Fig. 5.14). With this newly determined value of _g_ , the sensitivity reported in ch. 7 becomes 1500 spins _/p_ Hz instead of 1700. 

#### **9.3.3 Theoretical limit of a squeezing-enhanced ESR spectrometer** 

In our experiment, the achieved gain in sensitivity is limited by the finite degree of squeezing, due to the technical issues detailed in section 9.2.2 (JPA non-linearity and microwave losses along the squeezed-state propagation path). It is however interesting to discuss which would be the achievable enhancement if ideal squeezing could be achieved, and propagation losses suppressed. In other words, what is the theoretical achievable sensitivity of this scheme in the absence of technical imperfections ? 

##### **Squeezing backaction on spin dynamics** 

A first unavoidable and so far overlooked limitation is the impact that quantum squeezing can have on spin dynamics. As already explained in 9.1.1, it was predicted by Gardiner [221] and recently observed [217, 34] that the radiative damping rates of a TLS are modified in the presence of squeezing. As described by Eq. 9.3, shining a quantum squeezed state characterized by _N_ and _M_ (see Eq. 9.3) modifies the spin dynamics in the following ways: 

- the radiative relaxation rate is increased by (2 _N_ + 1) with the steady-state polarization being reduced by the same factor. 

- the radiative decoherence time is also impacted. 

To measure these effects in our experiment, we compare the spin coherence and relaxation times with and without squeezing. _T_ 2 is found to be unchanged by the squeezing, as shown in Fig. 9.13a, which is understandable by the fact that it is limited by non-radiative processes (see ch. 6). In contrast, we measure _T_ 1 = 0 _._ 45 s with SQZ on whereas _T_ 1 = 0 _._ 9 s with SQZ off as already mentioned. This factor 2 reduction is explained by the fact that contrary to _T_ 2, _T_ 1 is limited by a radiative process (spontaneous emission via the resonator) and is thus affected by squeezing according to Gardiner’s theory. In addition, both measurements evidence a steady-state polarization reduction by the same factor 2, again consistent with Gardiner’s theory. Interestingly, these observations provide us with an independent characterization of the degree of squeezing of the field inside the ESR resonator, in contrast with previous measurements which offer information of the squeezed state at the input of the AMP. We find 2 _N_ + 1 = 2 _._ 0, yielding a larger degree of squeezing for the intra-cavity field than for the field at the AMP input, qualitatively consistent with the additional losses occasioned by the field propagation from the cavity to the AMP. Using Eq 9.13 with _n_ th = 0 _._ 1, we find _⌘S_ = _−_ 4 _._ 8 dB for the intra-cavity field, compatible with previous measurements. We can thus estimate the losses between the resonator and the SQZ to be _⌘_ 1 = _−_ 0 _._ 5 dB and the losses between the resonator and the AMP _⌘_ 2 = _−_ 2 _._ 9 dB. These asymmetric loss factors are somewhat surprising considering our microwave setup; however we note that the relation between _N_ and _⌘S_ is valid only for a perfectly ellipsoidal squeezed state, which is probably not the case in our experiment. 

Squeezing-induced spin de-polarization is a major concern for the experiment, as it reduces the spin-echo signal by a factor 2, which would cause the signal-to-noise ratio to be in fact lower with SQZ on than with SQZ off ! In our experiment, this effect was avoided by switching the squeezing on only during the echo emission. This was possible because of the very large difference between the duration of the echo ( _⇡_ 20µs) and the timescale on which the spin become de-polarized, which is given by _T_ 1 _/_ (1+2 _N_ ) = 0 _._ 45 s. However this strategy would not hold for larger degree of squeezing, if the depolarization time becomes comparable to the echo emission time. 

150 



<!-- Start of picture text -->
+<br>L! S Pa<br>Q)0,<br>®<br>1l<br>\ Qo<br>AN) 0<br>AL YO<br>Xo<br>L8G] [m] [m]<br>any 50 0) a<br>6 OFSo —e=meOREO ©<br>0<br><!-- End of picture text -->





<!-- Start of picture text -->
+<br>* |<br>o0-6© OO 0 OD<br>oD O<br>OK ©<br>7") 071” 8 3 Q y<br>ARSRFOD ode<br>ir)45op<br>los)<br>):(10<br>RD<br>®<br><!-- End of picture text -->



_Chapter 9. Squeezing-enhanced magnetic resonance_ 



<!-- Start of picture text -->
2<br>1<br>10 -5<br>10 -4<br>10 -3<br>10 -2<br>10 -1<br>+<br>1<br><!-- End of picture text -->



<!-- Start of picture text -->
10 5<br>10 4<br>10 3<br>E<br>10 2<br>10<br>1<br>1 10 20<br>E<br><!-- End of picture text -->

FIGURE 9.14: **Gain in ESR sensitivity with squeezing.** Color plot represents the theoretical gain in sensitivity brought by shining a squeezed state of parameter _⌘S_ on the resonator during the echo emission, for spins coupled with a single-spin cooperativity _c_ = 4 _g_<sup>2</sup> _TE/_ . The top and right plots are line-cuts at the white dashed lines. Orange cross is the experiment operating point. The red long dashed line give the best _E_ as a function of _c_ , _E_ max _⌘S_ ( _c_ ). The free parameters _TE_ , _⌧_ , _N_ spins values needed to perform the analysis are taken similar to the experiment. 

section 9.1.2). We neglect for the moment the ESR resonator losses, assuming __ int = __ 1 = 0. We also assume _n_ th = 0 for simplicity. 

From Eq. 5.7, assuming _w ⌧ _ , in absence of squeezing, the amplitude of an echo emitted at _t_ = 0 is given by: 



We assume the dominant effect of squeezing on the echo signal to be the squeezing-induced depolarization. To take into account this effect, we introduce a time dependent function _p_ ( _t_ ) describing the fraction of spins contribution to the echo. From its initial value _p_ (0) = _p_ 0, _p_ decays exponentially under the energy relaxation process after the refocusing _⇡_ pulse at a rate Γ1 = Γ _P_ without squeezing and at rate Γ1 = Γ _P_ (2 _N_ + 1) when squeezing is turned on during the echo emission window ∆ _T_ . We then compute the quantity _ha_ ˆout( _t_ ) _i_ using Eq. 2.43 with _u_ being defined as a tophat function of width ∆ _T_ around the echo emission time. To take into account the spin spontaneous emission noise, we assume _hX_<sup>ˆ</sup> out<sup>2</sup><sup>_i_to be given by:</sup> 



with _n_ SE evaluated as R _t_<sup>_u_(</sup><sup>_t_)Γ1(</sup><sup>_t_)</sup><sup>_p_(</sup><sup>_t_)</sup><sup>_N_s</sup> 2<sup><u>pins</u></sup> . For this analysis, the interesting parameters are _⌘S_ 

152 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 

the degree of squeezing, 2 _⌧_ the sequence duration, _TE_ the echo width, _c_ = 4 _g_<sup>2</sup> _/_ the singlespin cooperativity and _N_ spins. We then evaluate numerically _E_ as a function of _c_ and _⌘S_ from the expressions derived for _hX_<sup>ˆ</sup> out<sup>2</sup><sup>_i_and</sup><sup>_h_ˆ</sup><sup>_X_out</sup><sup>_i_(see Fig. 9.14).</sup><sup>_⌧_and</sup><sup>_TE_are chosen similar to the</sup> experiment, and _N_ spins sufficiently small to ensure _C_ = _cN_ spins _⌧_ 1. 

For small _c_ , as the spontaneous emission and the squeezing back-action are negligible, _E_ =<sup>_p_</sup> _<u>⌘s</u>_ as expected. For larger values of _c_ , their contribution becomes non-negligible, and the achievable gain in sensitivity can be shown to be limited by: 



given at an optimal squeezing degree. At a given _⌘S_ , as _n_ SE _/ c_ , _E_ decreases from<sup>_p_</sup> _<u>⌘S</u>_ to 1 for increasing _c_ values. 

##### **Squeezing and resonator losses** 

We now come back to the impact of losses in the ESR resonator. In practice, there is an upper bound to the internal quality factor achievable for the resonator _Q_ int = _!_ 0 _/_ int and thus to maximize the enhancement brought by the squeezing, one should minimize the losses in reflection and thus pick 

2 a large coupling rate __ 2 = _↵_ int so as to maximize _⌘_ = ⇣ <u>11+</u> _−↵↵_ ⌘ . However in case of a radiatively limited energy relaxation time, one would also like to minimize the repetition time and thus have a small coupling rate __ = (1 + _↵_ ) __ int. 

This is a non-trivial optimization problem with optimization conditions that depends on the context of the experiment: 

- If the bandwidth __ has to be kept large, for instance to excite the whole spin linewidth ( _ ≫ w_ ) or to implement fast-manipulating pulses, then its optimization compared to __ int is unnecessary. The best enhancement brought by squeezing is then described by the previous analysis, keeping in mind that _⌘S_ will be eventually limited by the resonator losses. 

- If on the contrary no physical constraint exists on the choice of the resonator linewidth, then __ should be optimized in such a way as to maximize the experimental sensitivity. We address this optimization problem in the following. 

We assume that the squeezing is always broadband compared to the ESR resonator. As the signal-tonoise ratio scales like the square root of the number of repeated experimental sequences, to take into account the impact of __ on the emission efficiency, the noise reduction efficiency and the repetition rate, the quantity that should be optimized is the absolute sensitivity _H_ = _N_ min<sup>(</sup><sup>_on_)</sup><sup>_/p_</sup> Γ1 with SQZ on. In the case where _w ⌧ _ , we can distinguish several different limits: 

_•_ **Without squeezing and Γ1** **_≫_ Γ** **_P_** , then using Eq. 5.11 we get _H_ 1 = 2 _gppnw_<sup>_~~p~~_</sup> Γ1 _~~p~~_ _<u></u>_ 2<sup>_/_</sup><sup><u>(</u></sup> _↵_<sup>1+1</sup><sup>_/↵_2).</sup> 

- The minimum of _H_ is thus reached for _↵_ = 1, i.e. a critically-coupled resonator. 



The optimum is reached for _↵_ = 1 _/_ 2, once again close to critical-coupling. 

_•_ **With squeezing and Γ1** **_≫_ Γ** **_P_** : There is no back-action from the squeezing on the spins. Thus in _H_ 1 only _n_ = 1 _/_ 4 should be replaced by _n_ =<sup><u>1</u></sup> 4<sup>(</sup><sup>_⌘/⌘S_+1</sup><sup>_−⌘_)+</sup><sup>_n_SE.The quantity to optimize</sup> is then: _H_ 3 _/_ h⇣4 _n_ SE + 1 _−_<sup><u>(</u></sup> (<sup>_↵_</sup> _↵_<sup>_−_</sup> +1)<sup>1)22</sup> ⌘ <u>(1+</u> _↵↵_ <u>)</u><sup>2</sup> i1 _/_ 2 and thus the best choice is again _↵ ⇠_ 1. 

153 

_Chapter 9. Squeezing-enhanced magnetic resonance_ 

- **With squeezing and Γ1 = Γ** **_P_** . In this case, one should take into account the squeezing back-action for the spins and use the above model. The sensitivity _N_ min( _⌘S, c_ ) is rescaled by ~~p~~ 1 + 1 _/↵N_ min( _⌘s, c_ ) in presence of losses. Knowing the intrinsic _c_ int = 4 _g_<sup>2</sup> _TE/_ int, one can optimize the choice of __ 2. For a given _↵_ , the cooperativity is expressed as _c_ = _c_ int _/_ (1 + _↵_ ) and the best achievable squeezing is 1 _− ⌘_ ( _↵_ ). The optimal choice of _↵_ given _c_ int is thus to minimize _H_ ( _↵, c_ int) =<sup>_p_</sup> 1 + _↵N_ min<sup>(on)(</sup><sup>_c_int</sup><sup>_/_(1 +</sup><sup>_↵_)</sup><sup>_,_1</sup><sup>_−⌘_(</sup><sup>_↵_)).</sup> 

   - For our experimental parameters, this optimization yields __ 2 = 0 _._ 25 __ int. 

From this analysis, it appears that in most operating limits, the best choice is a critically coupled ESR resonator. In that case, the resonator internal losses will unavoidably limit the noise reduction obtained by squeezing to at most 3 dB, implying that squeezing factors above 10 dB would be irrelevant for this application. As already stated, this conclusion is only valid if the resonator linewidth can be chosen without any physical constraint (such as a finite spin linewidth, or pulse bandwidth), in which case larger enhancement factors can be theoretically reached as discussed in the previous paragraph. 

### **9.4 Conclusion** 

We realized in this chapter a proof-of-concept demonstration that squeezed states can be used to enhance the sensitivity of a magnetic resonance experiment and reduce the acquisition time. The rms noise reduction achieved in our experiment is limited to 12%, due to a number of technical issues. We note that intensive research in cQED aims at improving JPA devices [60] and developing lossless circulators [225, 226], which will be directly applicable to our scheme, with the perspective of gaining one order of magnitude on the acquisition time. 

Without improving the efficiency of the restitution of the energy stored by the spins by the first excitation pulse, by using CPMG sequences for example, further spectrometer sensitivity improvements will then come from increases in the resonator-spin coupling constant, or smaller resonator internal losses. We also note that other types of non-classical states could be useful for enhanced magnetic resonance: Fock states, Schrödinger-cat states [227], which are readily generated using circuit QED tools, are also known for their potential applications in quantum metrology. Further work should aim at assessing their usefulness for magnetic resonance. Moreover, more elaborate analysis than just measuring the variance could be useful, as was recently demonstrated in atomic spin squeezing [228]. In a broad perspective, our results indicate that the whole arsenal of quantum metrology deserves to be examined in view of its potential application in magnetic resonance. 

154 

## **Chapter 10** 

# **Conclusion and future directions** 

### **10.1 Magnetic resonance with quantum microwaves** 

In this thesis, we have reported three experiments in which we perform magnetic resonance spectroscopy in a novel regime where the microwave field, just like the spins, requires a quantummechanical description. 

So far, the microwave signals detected during ESR experiments had always been treated classically, since the detected noise largely exceeded the field quantum fluctuations. In ch. 7, we demonstrated that thanks to the use of low-temperatures and of a quantum-limited amplifier, the spectrometer output noise could arise mainly from these quantum fluctuations. Combining this quantumlimited sensitivity with high-quality-factor and small-mode-volume resonators, we demonstrated an unprecedented sensitivity for our home-built ESR spectrometer of 1700 spins/ _p_ Hz using Si:Bi spins. Using a CPMG sequence, we decreased this number to 150 spins/ _p_ Hz. 

Entering the regime of quantum-limited noise opens the door to the use of quantum optics techniques to increase the measurement sensitivity beyond the quantum-limit. In ch. 9, we realized a proof-of-concept experiment where we used squeezed vacuum states to reduce the total spectrometer output noise power by 25%. This translates into a 12% enhancement on the sensitivity or equivalently a 25% reduction in the acquisition time. 

Besides being relevant for the spectrometer output noise, quantum microwave fluctuations can also have a strong impact on the spin dynamics. In usual ESR experiments, the coupling constant between each spin and the microwave field is too small for the effect to be relevant. However, we showed in ch. 8 that for a spin placed at resonance in a high-quality-factor small-mode-volume resonator, the spin energy relaxation could be made faster via spontaneous emission of microwave photons. While the non-radiative relaxation time of Si:Bi spins was measured to be on the order of 20 minutes, the Purcell effect decreased _T_ 1 to a few seconds. More generally, cavity-enhanced spin relaxation can be used as a fast spin initialization method in several ESR experiments. For future applications in quantum information, _T_ 1 can be controlled on-demand by changing the spin-resonator coupling or detuning. This provides a new way to combine long intrinsic _T_ 1 times with fast repetition rates. 

### **10.2 Future research directions** 

The experimental results reported in this thesis open new possibilities both for magnetic resonance and for quantum information. 

155 

_Chapter 10. Conclusion and future directions_ 

##### **Beyond proof-of-concept quantum ESR** 

Our experimental setup reached record spin sensitivity, but with a very specific setup, since we measured implanted donors in silicon, and we use superconducting resonators, amplifiers, at ultralow-temperatures, and with applied magnetic fields below 10 mT. An interesting research direction is to use our setup to measure "real-world" samples with comparable sensitivites. 

A first point to note is that in order to detect a wider range of spin species, higher magnetic fields are required. A first objective would be to extend the setup to apply 0.2-0.3 T, which would enable to perform X-band ESR measurements. Such magnetic fields could be applied to the resonator without degrading its quality factor if the superconducting film had a higher critical field. Recently, resonators made out of superconductors such as nobium, nobium nitride [155, 156] and nobium titanium nitride [157] have demonstrated high quality factors up to 1 T. Further improvements can be expected since it is a subject of intense research in the cQED community, with the perspective of realizing hybrid devices combining superconducting qubits and for instance semiconducting nanowires [229], electrostatically quantum dots [230, 231] or Si:P spins [232]. 

Although we have used implanted donors in silicon, which are a well-known model spin system, other non-implanted spins could also be studied. The difficulty lies in having the spins a few tens of nanometers away from the resonator wire without using implantation. Some spins, such as the well-known organic compound 2,2-diphenyl-1-picrylhydrazyl (DPPH), widely used as a field and signal calibration marker in ESR spectrometers [233] or the stable free radical 1,3-bisdiphenylene-2phenylallyl (BDPA), can be mixed with glassing mixtures and could be drop-cast on the chip [234] or vapor-deposited [235]. Measuring low-concentrated samples of these radicals would already be a proof-of-concept that our technique can be generalized. 

Another topic where our experimental setup could be improved is the JPA. While the devices used in this work suffered from limited bandwidth and dynamic range, recently developed devices have reached much higher dynamic ranges ( _−_ 100 dBm) and considerably larger bandwidths (1 GHz) [60]. Cascaded with HEMT amplifiers which have now demonstrated noise temperature of 1 K [154], they could provide quantum-limited amplification without restricting the bandwidth or output power level of the ESR spectrometer. 

Low-temperatures are required both for having high spin polarization at gigaHertz frequencies and ensuring that the microwave field is in its ground state. Commercial spectrometers already operate at 4 K, where the use of frequencies _>_ 100 GHz could allow for quantum-limited ESR. Keeping an operating temperatures of 20 mK would permit working at similar frequencies than used in this thesis and use lower magnetic fields than required for operation at 100 GHz. 

##### **Cavity-assisted dynamic nuclear polarization** 

Another promising research direction is to explore the applications of Purcell-enhanced spin relaxation to magnetic resonance. In particular, it seems interesting to envision how it could be applied to Dynamical Nuclear Polarization (DNP) schemes [208, 209]. In such schemes, the polarization of a nuclear state is built by cross-relaxation on a electron-nuclear flip-flop transition. Cavity-enhanced relaxation could be an alternative to existing relaxation mechanisms or enhance the relaxation rate of this transition to improve the efficiency of the nuclear polarization. 

To give an example of implementation of cavity-assisted DNP, we briefly discuss preliminary results obtained using our setup. As shown in Fig. 10.1, our goal was to transfer population from Si:Bi state _|_ 8 _i_ into _|_ 9 _i_ , using cavity-enhanced relaxation. The scheme consists in exciting the _|_ 8 _i $ |_ 11 _i_ transition with the _|_ 9 _i $ |_ 11 _i_ transition tuned at the resonator frequency so that spins undergo Purcell-enhanced relaxation. The population in _|_ 9 _i_ is finally probed by measuring spin-echoes on the _|_ 9 _i $ |_ 10 _i_ transition. Fig. 10.1b shows the echo signal as a function of the resonator detuning to 

156 

_Chapter 10. Conclusion and future directions_ 



<!-- Start of picture text -->
2<br>a 11 b<br>i<br>10<br>i<br>Saturation<br>Γ p ( � )<br>1<br>2 1<br>3<br>Hahn-echo<br>detection<br>8i 9i 0 -0.4 -0.2 0.0 0.2 0.4<br>� / 2 ⇡ (MHz)<br>)<br>(off e<br>/A<br>)<br>�<br>(<br>e<br>A<br><!-- End of picture text -->

FIGURE 10.1: **Cavity-assisted DNP** using Si:Bi spins. **a** Working at _✓_ = 45<sup>_◦_</sup> , transitions _|_ 8 _i $ |_ 11 _i_ , _|_ 9 _i $ |_ 11 _i_ and _|_ 9 _i $ |_ 10 _i_ are allowed. To transfer population from _|_ 8 _i_ to _|_ 9 _i_ , a saturation pulse is first applied on _|_ 8 _i $ |_ 11 _i_ . The population stored in _|_ 11 _i_ then relaxes via the Purcell effect down to _|_ 9 _i_ . **b** Measuring the echo signal on transition _|_ 9 _i $ |_ 10 _i_ shows that when the Purcell relaxation is tuned at resonance, the echo signal is increased by 50%. 

_|_ 9 _i $ |_ 11 _i_ . When it is at resonance, the Purcell rate is maximized and activates the transfer to _|_ 9 _i_ . Our results demonstrate a cavity-assisted hyperpolarization of _⇡_ 50% in _|_ 9 _i_ . 

Higher degrees of polarization are difficult to obtain in our setup. First, our device geometry with its high quality factor does not allow to apply strong off-resonant pulses. This problem is avoided in the above scheme by pulsing the magnetic field in order to bring the various transitions successively in resonance with the resonator. However the slow response of the Helmholtz coils causes a partial decay via the Purcell effect of any population stored in an excited state and thus limits the pumping scheme efficiency. These issues could be solved with for example either a fast-tunable coil or a frequency-tunable resonator, or an ENDOR-type cavity enabling the application of rf pulses to control the nuclear states in addition to microwave pulses. 

Beyond these technical considerations, the experiment described here is only one example for using cavity-enhanced relaxation in DNP schemes. Depending on the spin systems, many others schemes could be realized, provided that the relaxation transition can be sufficiently coupled to the cavity microwave field to obtain Purcell-enhanced spontaneous emission. 

##### **Single-spin inductive detection** 

A third promising perspective is to enhance the sensitivity of our setup even further. Indeed, when the spin relaxation is set by cavity-enhanced relaxation, the absolute sensitivity is given by _N_ min ~~p~~ Γ _p_ and thus scales as _g_<sup>2</sup> instead of _g_ . As explained in this thesis, _g_ is proportional to the magnetic field quantum fluctuations; reducing the lateral dimensions of our inductance wire by two orders of magnitude (down to 50 nm, see Fig. 10.2) would thus increase _g_ by the same amount. Reaching such a coupling strength would put the detection of a single spin within reach. 



<!-- Start of picture text -->
200 nm<br>δB<br>i<br><!-- End of picture text -->

FIGURE 10.2: **Al nanowire constriction for single-spin sensitivity** 

This goal is actively pursued in the group. Once achieved, such exquisite sensitivity will enable for example the detection of single magnetic entities, for instance individual molecular magnets. 

157 

_Chapter 10. Conclusion and future directions_ 

For quantum information purposes, achieving a ratio _g/_ . 0 _._ 1 would allow the electronic spin to interact strongly with incoming microwave photons. Applied to spin systems having both electronic and nuclear spins coupled by hyperfine interaction, such as Si:Bi spins or NV centers in diamond, the efficient detection of the electron spin opens the way to detection of the nuclear spin state. Indeed, the coupling between electronic and nuclear spin yields ESR transitions whose frequencies are nuclear spin state dependent, as seen in ch. 4 for Si:Bi spins. If only one of these transitions is coupled to the resonator, its efficient readout would then permit to non-destructively measure the nuclear spin state. 

This enables in turn measurement-based entanglement schemes. Consider two spins coupled to two resonators. If each nuclear spin state readout yields the same result when the spins are prepared in the same state, then the simultaneous readout of both nuclear spins will not distinguish one spin from the other, resulting into the creation of an entangled state. Such a scheme would be the microwave transposition of the heralded entanglement scheme demonstrated on NV centers using optical readout [236]. 

##### **Si:Bi spins for quantum memories** 

Finally, we note that Si:Bi spins have specific properties which make them particularly well suited for quantum memory implementation [71]. In this thesis we have already showed that they can be readily coupled to superconducting resonators and that they have long coherence times. Additional interesting features include the electrical control of the donor spin frequency, which has been demonstrated only for Si:P so far [237]. 

In quantum memory proposals [78], the state of a superconducting qubit is stored in a spin ensemble, mediated by an intermediate superconducting resonator. This requires that the spin ensemble is strongly coupled to the resonator so that it can absorb efficiently the microwave field. Strong collective coupling requires largely concentrated samples, which in general translates into lower spin coherence times due to dipolar interactions, thus shortening possible storage times. The key asset of Si:Bi is that seconds-long coherence times are possible even in highly concentrated samples at the clock transitions. Memory reset could be achieved using the Purcell effect, as demonstrated in this thesis. 

158 

## **Appendix A** 

# **Thermal occupancy calibration** 

Due to imperfect filtering of the microwave probe lines and to the refrigerator finite base temperature, one can never reach perfect electromagnetic vacuum. In this appendix, we describe the calibration procedure used to place an upper bound on the average excitation number of the input modes<sup>ˆ</sup> _b_ in( _!_ ) around the ESR resonator resonance frequency (typically _|! − !_ 0 _|_ 6 _c_ ). 

The method consists in replacing, in a separate cool-down of the refrigerator, the ESR resonator with a transmon superconducting qubit [238] coupled to a microwave readout resonator with resonance frequency _!_ 1. The resonator-qubit system is in the so-called _strong dispersive regime_ of circuit QED in which photons in the resonator mode lead to dephasing of the qubit [239, 240]. Thus, by measuring the dephasing rate of the qubit beyond the effect of population relaxation _γφ_ = _γ_ 2 _− γ_ 1 _/_ 2, where _γ_ 2 = 1 _/T_ 2 and _γ_ 1 = 1 _/T_ 1, one can place an upper bound on the thermal photon number _n_ th in the readout resonator, and then on the occupation of the traveling modes<sup>ˆ</sup> _b_ in. 

#### **Microwave setup and device** 

We calibrate the number of thermal photons using the squeezing experiment setup (see ch. 9) shown in Fig. A.1a. The ESR resonator is replaced by the following device, studied in [241]. On a sapphire chip, 4 lumped element microwave readout resonators, each one capacitively coupled to a transmon qubit (see Fig. A.1), are coupled to a single transmission feedline. In the following, we consider only the qubit-resonator system labeled _cell 2_ (the other ones are well out of resonance). The feedline is connected to the setup depicted in Fig. A.1a at points A and B. 

The readout resonator consists in an interdigitated capacitor made out of superconducting aluminum in parallel of an array of Josephson junctions (Fig. A.1). This array behaves as a non-linear inductor and was originally designed to allow for a single-shot readout of the attached qubit. This non-linearity is not relevant here and can anyway be neglected as the average photon number in the resonator is well below one. Note that the readout resonator has a slightly different frequency _!_ 1 _/_ 2 _⇡_ = 7 _._ 62 GHz than the ESR resonators, but we assume that the thermal equilibrium is similar so that _h_<sup>ˆ</sup> _b_<sup>_†_</sup> in<sup>(</sup><sup>_!_)ˆ</sup><sup>_b_in(</sup><sup>_!_)</sup><sup>_i_=</sup><sup>_h_ˆ</sup><sup>_b†_</sup> in<sup>(</sup><sup>_!_1)</sup><sup>_b_in(</sup><sup>_!_1)</sup><sup>_i_for all relevant values of</sup><sup>_!_.This assumption is reasonable</sup> given that _|! − !_ 1 _| ⌧ kBT_ , and the transmission of the microwave input lines is flat ( _±_ 0 _._ 5 dB variation) on this frequency range. 

Note that in this geometry, the readout resonator thermal occupation is set by the average occupation of right propagating modes<sup>ˆ</sup> _b_ in through A and left propagating modes ˆ _c_ in through B (see Fig. A.1d). Internal losses of the readout resonator, that could act as a connexion to a fictitious cold reservoir, are shown to be negligible on Fig. A.3d. The blue input line connected at B in Fig. A.1a, which was originally designed to probe the ESR resonator in reflection on port 1, is less attenuated by 10 dB than the green line connected to A so that left propagating modes tend to increase the thermal 

159 



<!-- Start of picture text -->
a b rir<br>: eee nag?<br>wr s 0 i<br>Jz ? panne "en er PA PA<br>c Se ’<br>=<br>pf G0<br>ol © 1 5 |<br>es<br>Cm) d bin A<br>ia<br><!-- End of picture text -->



<!-- Start of picture text -->
: eee nag?<br>er PA PA<br><!-- End of picture text -->

_Appendix A. Thermal occupancy calibration_ 



<!-- Start of picture text -->
3.4 B=0.472G<br>B<br>0.42 G<br>0.43 G<br>0.44 G<br>0.45 G 2.4<br>0.46 G<br>4 0.47 G sweet  6.2276 6.2280 6.2284 6.2288<br>0.48 G spot<br>3.5 0.49 G0.50 G<br>0.51 G<br>3<br>2.5<br>6.215 6.220 6.225 6.230<br><!-- End of picture text -->

FIGURE A.2: **Two-tone spectroscopy** of the qubit. Starting from thermal equilibrium, the qubit is shined with a 5 µs-long saturating pulse (power -20 dBm referenced at refrigerator input) of frequency _f_ exc and then readout with an optimized pulse around _!_ 1 _/_ 2 _⇡_ (see text and Fig. A.3). The integrated signal _S_ reveals the qubit excited state occupation. One can vary the qubit resonance frequency by varying the amplitude of the applied B-field (encoded in color). **Inset:** desaturated qubit resonance (power -30 dBm at fridge input) at the sweet spot, showing that _!q/_ 2 _⇡_ = 6 _._ 228 GHz. 

resonator frequency, which provides us with a robust readout method of the transmon [242, 243]. Indeed, by probing the resonator with a microwave nearby its resonance frequency and integrating a quadrature of the transmitted field, one gets a signal _S_ depending linearly on _hσ_ ˆ _zi_ . In practice, the power, length and frequency of the readout pulse was empirically adjusted to optimize signal-to-noise ratio. It corresponds to few photons in the resonator (power 10 dB larger than for 1 photon characterization of the resonator on Fig A.3 d). Note that the JPA was turned off during all measurements. 

#### **Thermal photon characterization** 

Rigetti _et al._ computed the dephasing rate of a qubit induced by thermally excited photons in the readout resonator mode [244]. It reads 



where __ is the photon exit rate from the readout resonator, and _n_ th = _ha_<sup>_†_</sup> _ai_ is the mean number of photons hosted by the resonator. Considering that _γ_ phot _ γφ_ = _γ_ 2 _− γ_ 1 _/_ 2, we now measure the qubit population and coherence relaxation rates _γ_ 1 and _γ_ 2 as well as all parameters entering the expression (A.2) in order to place an upper bound on _n_ th. 

By applying _⇡_ and _⇡/_ 2 excitation pulses (calibrated by recording Rabi oscillations of the qubit), we first measure the qubit population relaxation rate _γ_ 1 = 0 _._ 41 µs<sup>_−_1</sup> (see Fig. A.3 a) and coherence relaxation rate _γ_ 2<sup>_⇤_= 1</sup><sup>_._1 µs</sup><sup>_−_1(see Fig. A.3 b).This last rate corresponds to a free-induction decay</sup> measurement, and includes the effect of low-frequency noise, such as second order perturbation of the fluctuations in the flux threading the qubit loop, along with high-frequency noise as induced by thermally induced photons in the readout resonator. A Hahn-echo measurement would rephase any low-frequency noise. As we measure _γ_ 2 _,_ echo _' γ_ 2<sup>_⇤_(see Fig. A.3 c), we can state that</sup> the dominant contribution is thermal dephasing ad thus the qubit pure dephasing rate is simply _γφ_ = _γ_ 2 _− γ_ 1 _/_ 2 = 0 _._ 9 µs<sup>_−_1</sup> . 

161 

_Appendix A. Thermal occupancy calibration_ 



<!-- Start of picture text -->
a b 7.5<br>6<br>7<br>5<br>6.5<br>4 6<br>5.5<br>3<br>5<br>0 2 4 6 8 10 12 0 1 2 3 4<br>c<br>d 0<br>6<br>-5<br>5.5<br>-10<br>5<br>4.5 -15<br>0 1 2 3 4 5 7.620 7.624 7.628 7.632<br><!-- End of picture text -->

FIGURE A.3: **Qubit-resonator parameters characterization** . For each measurement, the pulse sequence is schematically represented at _!q_ (in purple, all rotations around ˆ _σy_ of the qubit) and at _!_ readout _' !_ 1 (in brown). **a** Population relaxation measurement yielding _T_ 1 = 2 _._ 4 µs, **b** Free induction decay measurement yielding _T_ 2<sup>_⇤_= 0</sup><sup>_._9 µs (excitation pulses at</sup><sup>_!_</sup> _q_<sup>_/_2</sup><sup>_⇡_+ 2 MHz).</sup><sup>**c**Hahn-echo measurement yielding</sup><sup>_T_</sup> 2 _,_ echo<sup>=</sup> 0 _._ 9 µs. **d** Measured transmission coefficient _SAB_ when the qubit is at thermal equilibrium (red dots), right after an inverting _⇡_ -pulse (yellow dots) and a qubit half-life later (green dots). Black lines: global fit with parameters _p⇡_ = 0 _._ 66, _χ/_ 2 _⇡_ = 1 _._ 48 MHz and __ int _/_ c = 0 _._ 14. For **a** , **b** and **c** the readout pulse power is empirically adjusted to optimize signal to noise ratio and the transmitted field is integrated over 5 µs. Only the quadrature _S_ containing information on the qubit state is plotted. For **d** the readout pulse power is low enough that readout resonator non-linearity is neglected and the transmitted field is integrated over 0 _._ 2 µs in the stationary regime. 

The last quantity needed to evaluate _n_ th is the anharmonicity _χ_ . To have a precise estimate of its value, we detect the transmitted signal through the feedline for a probe pulse of low amplitude (linear regime of the readout resonator) and integrate the signal over 0 _._ 2 µs _⌧ T_ 1 in the stationary regime of the resonator (signal during ring-up is discarded in order to avoid distortion of the signal). The transmission coefficient from A to B then reads [245] 



where __ c (resp. __ int) is the resonator photon exit rate into the feedline (resp. due to internal losses) ˆ and _p_ = _h_ 1 _− σzi_ /2 is the occupation of the ground state of the qubit. Note that the total photon exit rate from the resonator __ = __ int + __ c = 2 _⇡ ⇥_ 3 _._ 25 MHz is determined independently by measuring the ringdown time of the resonator. 

We record this transmission coefficient at thermal equilibrium ( _p '_ 1, red dots on Fig. A.3d), after applying a _⇡_ -pulse ( _p_ = _p⇡_ , yellow dots) and, for better precision, a duration _t_ 1 _/_ 2 = ln 2 _T_ 1 after the same pulse ( _p_ = _p⇡/_ 2, green dots). If _p⇡_ can be roughly estimated given the drive pulse duration and delay before signal integration, it is difficult to predict accurately its value due to the reduction of _T_ 1 in presence of a field in the readout resonator [246]. We rather estimate it along with the other parameters entering Eq. (A.3) by fitting these three curves altogether (black curves), which yields _p⇡_ = 0 _._ 66, _χ/_ 2 _⇡_ = 1 _._ 48 MHz and __ int _/_ c = 0 _._ 14. In this fit, we allow for a global scaling factor accounting for the attenuation in the lines, and a small offset in the transmitted field complex amplitude, attributed to impedance mismatch. From this calibration and using Eq. (A.2), we find for the readout resonator 

162 

_Appendix A. Thermal occupancy calibration_ 

_n_ th = 0 _._ 5 _±_ 0 _._ 5 _._ (A.4) 

We thus conclude that the thermal occupancy of the transmission lines is also less than 0.1 and use this number throughout the experimental results presented in ch. 5-9, since all are acquired with only small changes in the microwave setup of Fig. A.1, with all probe lines having the same filtering. Improving this figure would certainly require increasing the attenuation of the input lines as well as adding extra-circulators on the output lines. 

163 

# **Bibliography** 

- [1] I. I. Rabi, J. R. Zacharias, S. Millman, and P. Kusch. A new method of measuring nuclear magnetic moment. _Phys. Rev._ , 53:318–318, Feb 1938. 

- [2] F. Bloch, W. W. Hansen, and M. Packard. Nuclear induction. _Phys. Rev._ , 69:127–127, Feb 1946. 

- [3] E. M. Purcell, H. C. Torrey, and R. V. Pound. Resonance absorption by nuclear magnetic moments in a solid. _Phys. Rev._ , 69:37–38, Jan 1946. 

- [4] A. Abragam. _Principles of Nuclear Magnetism_ . Oxford Science Publications, Clarendon Press, 1986. 

- [5] A. Schweiger and G. Jeschke. _Principles of Pulse Electron Paramagnetic Resonance_ . Oxford University Press, 2001. 

- [6] M. Pellecchia, I. Bertini, D. Cowburn, C. Dalvit, E. Giralt, W. Jahnke, T. L. James, S. W. Homans, H. Kessler, C. Luchinat, B. Meyer, H. Oschkinat, J. Peng, H. Schwalbe, and Gregg Siegal. Perspectives on NMR in drug discovery: a technique comes of age. _Nat. Rev. Drug. Discov._ , 7(9):738–745, September 2008. 

- [7] R. M. Serra and I. S. Oliveira. Nuclear magnetic resonance quantum information processing. _Philos. T. Roy. Soc. A_ , 370(1976):4615, 2012. 

- [8] H. Walther, B. T. H. Varcoe, B.-G. Englert, and T. Becker. Cavity quantum electrodynamics. _Reports on Progress in Physics_ , 69(5):1325, 2006. 

- [9] A. Blais, R.-S. Huang, A. Wallraff, S. M. Girvin, and R. J. Schoelkopf. Cavity quantum electrodynamics for superconducting electrical circuits: An architecture for quantum computation. _Phys. Rev. A_ , 69:062320, 2004. 

- [10] A. Wallraff, D. I. Schuster, A. Blais, L. Frunzio, R.-S. Huang, J. Majer, S. Kumar, S. M. Girvin, and R. J. Schoelkopf. Strong coupling of a single photon to a superconducting qubit using circuit quantum electrodynamics. _Nature_ , 431:162, 2004. 

- [11] C. M. Caves. Quantum limits on noise in linear amplifiers. _Phys. Rev. D_ , 26(8):1817–1839, October 1982. 

- [12] B. Yurke, L. R. Corruccini, P. G. Kaminsky, L. W. Rupp, A. D. Smith, A. H. Silver, R. W. Simon, and E. A. Whittaker. Observation of parametric amplification and deamplification in a Josephson parametric amplifier. _Phys. Rev. A_ , 39(5):2519–2533, March 1989. 

- [13] N. Bergeal, F. Schackert, M. Metcalfe, R. Vijay, V. E. Manucharyan, L. Frunzio, D. E. Prober, R. J. Schoelkopf, S. M. Girvin, and M. H. Devoret. Phase-preserving amplification near the quantum limit with a Josephson ring modulator. _Nature_ , 465(7294):64–68, May 2010. 

- [14] A. Bienfait, J. J. Pla, Y. Kubo, M. Stern, X. Zhou, C. C. Lo, C. D. Weis, T. Schenkel, M. L. W. Thewalt, D. Vion, D. Esteve, B. Julsgaard, K. Mølmer, J. J. L. Morton, and P. Bertet. Reaching the quantum limit of sensitivity in electron spin resonance. _Nat. Nanotechnol._ , 11(3):253–257, December 2015. 

- [15] A. J. Sigillito, H. Malissa, A. M. Tyryshkin, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, K. M. Itoh, J. J. L. Morton, A. A. Houck, D. I. Schuster, and S. A. Lyon. Fast, 

164 

_BIBLIOGRAPHY_ 

low-power manipulation of spin ensembles in superconducting microresonators. _Appl. Phys. Lett._ , 104(22):222407, June 2014. 

- [16] G. Feher. Electron Spin Resonance Experiments on Donors in Silicon. I. Electronic Structure of Donors by the Electron Nuclear Double Resonance Technique. _Phys. Rev._ , 114(5):1219–1244, June 1959. 

- [17] A. Bienfait, J. J. Pla, Y. Kubo, X. Zhou, M. Stern, C. C. Lo, C. D. Weis, T. Schenkel, D. Vion, D. Esteve, J. J. L. Morton, and P. Bertet. Controlling spin relaxation with a cavity. _Nature_ , 531(7592):74–77, 2016. 

- [18] C. M. Caves. Quantum-mechanical noise in an interferometer. _Phys. Rev. D_ , 23(8):1693–1708, April 1981. 

- [19] P. Grangier, R. E. Slusher, B. Yurke, and A. LaPorta. Squeezed-light enhanced polarization interferometer. _Phys. Rev. Lett._ , 59(19):2153–2156, November 1987. 

- [20] Min Xiao, Ling-An Wu, and H. J. Kimble. Precision measurement beyond the shot-noise limit. _Phys. Rev. Lett._ , 59(3):278–281, July 1987. 

- [21] R. Vijay, D. H. Slichter, and I. Siddiqi. Observation of quantum jumps in a <superconducting artificial atom. _Phys. Rev. Lett._ , 106(11):110502, mar 2011. 

- [22] J.D. Teufel, T. Donner, M.A. Castellanos-Beltran, J.W. Harlow, and K.W. Lehnert. Nanomechanical motion measured with an imprecision below that at the standard quantum limit. _Nat. Nanotechnol._ , 4(12):820–823, 2009. 

- [23] J. Stehlik, Y.-Y. Liu, C. M. Quintana, C. Eichler, T. R. Hartke, and J. R. Petta. Fast Charge Sensing of a Cavity-Coupled Double Quantum Dot Using a Josephson Parametric Amplifier. _Appl. Phys. Lett._ , 4(1):014018, 2015. 

- [24] M. Hatridge, R. Vijay, D. H. Slichter, J. Clarke, and I. Siddiqi. Dispersive magnetometry with a quantum limited SQUID parametric amplifier. _Phys. Rev. B_ , 83(13):134501, April 2011. 

- [25] G. Wolfowicz, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, M. L. W. Thewalt, S. A. Lyon, and J. J. L. Morton. Atomic clock transitions in silicon-based spin qubits. _Nat. Nanotechnol._ , 8(8):561–564, 2013. 

- [26] G. W. Morley, M. Warner, A. M. Stoneham, P. T. Greenland, J. van Tol, C. W. M. Kay, and G. Aeppli. The initialization and manipulation of quantum information stored in silicon by bismuth dopants. _Nat. Mater._ , 9(9):725–729, 2010. 

- [27] M. C. Butler and D. P. Weitekamp. Polarization of nuclear spins by a cold nanoscale resonator. _Phys. Rev. A_ , 84(6):063407, December 2011. 

- [28] P. Goy, J. M. Raimond, M. Gross, and S. Haroche. Observation of Cavity-Enhanced SingleAtom Spontaneous Emission. _Phys. Rev. Lett._ , 50(24):1903–1906, June 1983. 

- [29] H. Yokoyama, K. Nishi, T. Anan, H. Yamada, S. D. Brorson, and E. P. Ippen. Enhanced spontaneous emission from GaAs quantum wells in monolithic microcavities. _Appl. Phys. Lett._ , 57(26):2814–2816, December 1990. 

- [30] J. M. Gérard, B. Sermage, B. Gayral, B. Legrand, E. Costard, and V. Thierry-Mieg. Enhanced spontaneous emission by quantum boxes in a monolithic optical microcavity. _Phys. Rev. Lett._ , 81(5):1110, 1998. 

- [31] Ligo Scientic Collaboration. Enhanced sensitivity of the LIGO gravitational wave detector by using squeezed states of light. _Nat Photon_ , 7(8):613–619, August 2013. 

- [32] V. G. Lucivero, R. Jiménez-Martínez, J. Kong, and M. W. Mitchell. Squeezed-light spin noise spectroscopy. _Phys. Rev. A_ , 93(5):053802, May 2016. 

165 

_BIBLIOGRAPHY_ 

- [33] B. Yurke. Squeezed-state generation using a Josephson parametric amplifier. _JOSA B_ , 4(10):1551–1557, 1987. 

- [34] M. Toyli, D. W. Eddins, A. S. Boutin, S. Puri, D. Hover, V. Bolkhovsky, D. Oliver, W. A. Blais, and I. Siddiqi. Resonance Fluorescence from an Artificial Atom in Squeezed Vacuum. _Phys. Rev. X_ , 6(3), July 2016. 

- [35] J. B. Clark, F. Lecocq, R. W. Simmonds, J. Aumentado, and J. D. Teufel. Observation of strong radiation pressure forces from squeezed light on a mechanical oscillator. _Nat. Phys._ , 3701, March 2016. 

- [36] T. Yoshimura, H. Yokoyama, S. Fujii, F. Takayama, K. Oikawa, and H. Kamada. In vivo EPR detection and imaging of endogenous nitric oxide in lipopolysaccharide-treated mice. _Nat. Biotechnol._ , 14(8):992–994, August 1996. 

- [37] H. Malissa, D. I. Schuster, A. M. Tyryshkin, A. A. Houck, and S. A. Lyon. Superconducting coplanar waveguide resonators for low temperature pulsed electron spin resonance spectroscopy. _Rev. Sci. Instrum._ , 84(2):025116, February 2013. 

- [38] C. Gerry and P. Knight. _Introductory Quantum Optics_ . Cambridge University Press, Cambridge, UK; New York, 1st edition, November 2004. 

- [39] S. Haroche and J.-M. Raimond. _Exploring the Quantum_ . Oxford University Press, 2006. 

- [40] V. Giovannetti, S. Lloyd, and L. Maccone. Quantum-Enhanced Measurements: Beating the Standard Quantum Limit. _Science_ , 306(5700):1330–1336, November 2004. 

- [41] M. H. Devoret. Quantum Fluctuations in Electrical Circuits. _Elsevier_ , page 351, 1997. 

- [42] B. Yurke and J. S. Denker. Quantum network theory. _Phys. Rev. A_ , 29:1419–1437, 1984. 

- [43] A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt, and R. J. Schoelkopf. Introduction to quantum noise, measurement, and amplification. _Rev. Mod. Phys._ , 82:1155, 2010. 

- [44] K. Kurokawa. Power waves and the scattering matrix. _IEEE T. Microw. Theory_ , 13(2):194–202, Mar 1965. 

- [45] C. W. Gardiner and M. J. Collett. Input and output in damped quantum systems: Quantum stochastic differential equations and the master equation. _Phys. Rev. A_ , 31:3761, 1985. 

- [46] H. A. Haus and J. A. Mullen. Quantum Noise in Linear Amplifiers. _Phys. Rev._ , 128(5):2407– 2413, December 1962. 

- [47] F. Schackert. _A Practical Quantum-Limited Parametric Amplifier ased on the Josephson Ring Modulator_ . PhD thesis, University of Yale, Yale, 2013. 

- [48] E. Flurin. _The Josephson Mixer, a Swiss army knife for microwave quantum optics_ . PhD thesis, Ecole Normale Supérieure, Paris, December 2014. 

- [49] M. A. Castellanos Beltran. _Development of a Josephson parametric amplifier for the preparation and detection of nonclassical states of microwave fields_ . PhD thesis, University of Colorado, 2010. 

- [50] C. Eichler, D. Bozyigit, C. Lang, M. Baur, L. Steffen, J. M. Fink, S. Filipp, and A. Wallraff. Observation of Two-Mode Squeezing in the Microwave Frequency Domain. _Phys. Rev. Lett._ , 107(11):113601, 2011. 

- [51] C. M. Wilson, T. Duty, M. Sandberg, F. Persson, V. Shumeiko, and P. Delsing. Photon Generation in an Electromagnetic Cavity with a Time-Dependent Boundary. _Phys. Rev. Lett._ , 105(23):233907, December 2010. 

- [52] J. Y. Mutus, T. C. White, E. Jeffrey, D. Sank, R. Barends, J. Bochmann, Yu Chen, Z. Chen, B. Chiaro, A. Dunsworth, J. Kelly, A. Megrant, C. Neill, P. J. J. O’Malley, P. Roushan, 

166 

_BIBLIOGRAPHY_ 

A. Vainsencher, J. Wenner, I. Siddiqi, R. Vijay, A. N. Cleland, and John M. Martinis. Design and characterization of a lumped element single-ended superconducting microwave parametric amplifier with on-chip flux bias line. _Appl. Phys. Lett._ , 103(12):122602, September 2013. 

- [53] Z. R. Lin, K. Inomata, W. D. Oliver, K. Koshino, Y. Nakamura, J. S. Tsai, and T. Yamamoto. Single-shot readout of a superconducting flux qubit with a flux-driven Josephson parametric amplifier. _Appl. Phys. Lett._ , 103(13):132602, 2013. 

- [54] X. Zhou, V. Schmitt, P. Bertet, D. Vion, W. Wustmann, V. Shumeiko, and D. Esteve. High-gain weakly nonlinear flux-modulated Josephson parametric amplifier using a SQUID array. _Phys. Rev. B_ , 89(21):214517, June 2014. 

- [55] W. Wustmann and V. Shumeiko. Parametric resonance in tunable superconducting cavities. _Phys. Rev. B_ , 87(18):184501, May 2013. 

- [56] C. Eichler and A. Wallraff. Controlling the dynamic range of a Josephson parametric amplifier. _EPJ Quantum Technology_ , 1(2), 2014. 

- [57] B. Josephson. Possible new effects in superconductive tunneling. _Physics Letters_ , 1:251–253, 1962. 

- [58] J. Clarke. _The SQUID Handbook: Fundamentals and Technology of SQUIDs and SQUID Systems_ . Wiley-VCH, 2005. 

- [59] L. D. Landau and E. M. Lifshitz. _Mechanics, Third Edition: Volume 1_ . Butterworth-Heinemann, 3rd edition, 1976. 

- [60] C. Macklin, K. O’Brien, D. Hover, M. E. Schwartz, V. Bolkhovsky, X. Zhang, W. D. Oliver, and I. Siddiqi. A near–quantum-limited Josephson traveling-wave parametric amplifier. _Science_ , 350(6258):307–310, October 2015. 

- [61] E. L. Hahn. Spin Echoes. _Phys. Rev._ , 80(4):580–594, November 1950. 

- [62] D. F. Walls and Gerard J. Milburn. _Quantum Optics_ . Springer Science & Business Media, 2008. 

- [63] M. Fox. _Quantum Optics: An Introduction_ . OUP Oxford, April 2006. 

- [64] B. Julsgaard and K. Mølmer. Measurement-induced two-qubit entanglement in a bad cavity: Fundamental and practical considerations. _Phys. Rev. A_ , 85(3):032327, March 2012. 

- [65] J. Wang, H. M. Wiseman, and G. J. Milburn. Dynamical creation of entanglement by homodynemediated feedback. _Phys. Rev. A_ , 71:042309, 2005. 

- [66] M. C. Butler. _Novel methods for force-detected nuclear magnetic resonance_ . PhD thesis, California Institute of Technology, 2007. 

- [67] M. Tavis and F. W. Cummings. Exact Solution for an N-Molecule-Radiation-Field Hamiltonian. _Phys. Rev._ , 170:379, 1968. 

- [68] P. F. Herskind, A. Dantan, J. P. Marler, M. Albert, and M. Drewsen. Realization of collective strong coupling with ion Coulomb crystals in an optical cavity. _Nature Phys._ , 5:494, 2009. 

- [69] J. M. Fink, R. Bianchetti, M. Baur, M. Göppl, L. Steffen, S. Filipp, P. J. Leek, A. Blais, and A. Wallraff. Dressed Collective Qubit States and the Tavis-Cummings Model in Circuit QED. _Phys. Rev. Lett._ , 103(8):083601, August 2009. 

- [70] Y. Kubo, C. Grezes, A. Dewes, T. Umeda, J. Isoya, H. Sumiya, N. Morishita, H. Abe, S. Onoda, T. Ohshima, V. Jacques, A. Dréau, J.-F. Roch, I. Diniz, A. Auffeves, D. Vion, D. Esteve, and P. Bertet. Hybrid Quantum Circuit with a Superconducting Qubit Coupled to a Spin Ensemble. _Phys. Rev. Lett._ , 107:220501, 2011. 

167 

_BIBLIOGRAPHY_ 

- [71] C. Grezes. _Towards a spin-ensemble quantum memory for superconducting qubits_ . PhD thesis, Université Pierre-et-Marie-Curie, 2014. 

- [72] R. H. Dicke. Coherence in spontaneous radiation processes. _Phys. Rev._ , 93:99, 1954. 

- [73] J. A. Mlynek, A. A. Abdumalikov, C. Eichler, and A. Wallraff. Observation of Dicke superradiance for two artificial atoms in a cavity with high decay rate. _Nat. Commun._ , 5(5186), 2014. 

- [74] G. Feher, J. P. Gordon, E. Buehler, E. A. Gere, and C. D. Thurmond. Spontaneous Emission of Radiation from an Electron Spin System. _Phys. Rev._ , 109(1):221–222, January 1958. 

- [75] V. V. Temnov and U. Woggon. Superradiance and Subradiance in an Inhomogeneously Broadened Ensemble of Two-Level Systems Coupled to a Low-Q Cavity. _Phys. Rev. Lett._ , 95:243602, 2005. 

- [76] C. J. Wood and D. G. Cory. Cavity cooling to the ground state of an ensemble quantum system. _Phys. Rev. A_ , 93(2):023414, February 2016. 

- [77] C. Grezes, B. Julsgaard, Y. Kubo, M. Stern, T. Umeda, J. Isoya, H. Sumiya, S. Abe, S. Onoda, T. Ohshima, V. Jacques, J. Esteve, D. Vion, D. Esteve, K. Moelmer, and P. Bertet. Multimode Storage and Retrieval of Microwave Fields in a Spin Ensemble. _Phys. Rev. X_ , 4:021049, 2014. 

- [78] B. Julsgaard, C. Grezes, P. Bertet, and K. Mølmer. Quantum Memory for Microwave Photons in an Inhomogeneously Broadened Spin Ensemble. _Phys. Rev. Lett._ , 110(25):250503, June 2013. 

- [79] A. Honig. Polarization of Arsenic Nuclei in a Silicon Semiconductor. _Phys. Rev._ , 96(1):234–235, October 1954. 

- [80] G. Feher, R. C. Fletcher, and E. A. Gere. Exchange Effects in Spin Resonance of Impurity Atoms in Silicon. _Phys. Rev._ , 100(6):1784–1786, December 1955. 

- [81] G. Feher and E. A. Gere. Electron Spin Resonance Experiments on Donors in Silicon. II. Electron Spin Relaxation Effects. _Phys. Rev._ , 114(5):1245–1256, June 1959. 

- [82] J. P. Gordon and K. D. Bowers. Microwave Spin Echoes from Donor Electrons in Silicon. _Phys. Rev. Lett._ , 1(10):368–370, November 1958. 

- [83] B. E. Kane. A silicon-based nuclear spin quantum computer. _Nature_ , 393(6681):133–137, May 1998. 

- [84] M. H. Mohammady, G. W. Morley, and T. S. Monteiro. Bismuth Qubits in Silicon: The Role of EPR Cancellation Resonances. _Phys. Rev. Lett._ , 105(6):067602, August 2010. 

- [85] G. W. Morley, P. Lueders, M. H. Mohammady, S. J. Balian, G. Aeppli, C. W. M. Kay, W. M. Witzel, G. Jeschke, and T. S. Monteiro. Quantum control of hybrid nuclear–electronic qubits. _Nat. Mater._ , 12(2):103–107, December 2012. 

- [86] E. B. Hale and R. L. Mieher. Shallow Donor Electrons in Silicon. I. Hyperfine Interactions from ENDOR Measurements. _Phys. Rev._ , 184(3):739–750, August 1969. 

- [87] R. Kh. Zhukavin, K. A. Kovalevsky, V. V. Tsyplenkov, V. N. Shastin, S. G. Pavlov, H.-W. Hübers, H. Riemann, N. V. Abrosimov, and A. K. Ramdas. Spin-orbit coupling effect on bismuth donor lasing in stressed silicon. _Appl. Phys. Lett._ , 99(17):171108, October 2011. 

- [88] A. K. Ramdas and S. Rodriguez. Spectroscopy of the solid-state analogues of the hydrogen atom: donors and acceptors in semiconductors. _Rep. Prog. Phys._ , 44(12):1297, 1981. 

- [89] A. R. Stegner. _Shallow dopants in nanostructered and in isotopically_ . PhD thesis, Technische Universität München, January 2011. 

- [90] A. Abragam and B. Bleaney. _Electron Paramagnetic Resonance of Transition Ions_ . OUP Oxford, June 2012. 

168 

_BIBLIOGRAPHY_ 

- [91] G. Wolfowicz, J. J. L. Morton, and S. Benjamin. _Quantum control of donor spins in silicon and their environment_ . PhD thesis, Oxford University, 2015. 

- [92] J. M. Luttinger and W. Kohn. Motion of Electrons and Holes in Perturbed Periodic Fields. _Phys. Rev._ , 97(4):869, 1955. 

- [93] P. Y. Yu and M. Cardona. _Fundamentals of Semiconductors_ . Graduate Texts in Physics. Springer Berlin Heidelberg, Berlin, Heidelberg, 2010. 

- [94] D. K. Wilson and G. Feher. Electron Spin Resonance Experiments on Donors in Silicon. III. Investigation of Excited States by the Application of Uniaxial Stress and Their Importance in Relaxation Processes. _Phys. Rev._ , 124(4):1068–1083, November 1961. 

- [95] D. A. Neamen. _Semiconductor Physics And Devices: Basic Principles_ . McGraw-Hill, New York, NY, 4th edition, January 2011. 

- [96] M. J. Calderón, B. Koiller, and S. Das Sarma. External field control of donor electron exchange at the Si _/_ Si O 2 interface. _Phys. Rev. B_ , 75(12):125311, March 2007. 

- [97] C. C. Lo, S. Simmons, R. Lo Nardo, C. D. Weis, A. M. Tyryshkin, J. Meijer, D. Rogalla, S. A. Lyon, J. Bokor, T. Schenkel, and J. J. L. Morton. Stark shift and field ionization of arsenic donors in 28Si-silicon-on-insulator structures. _Appl. Phys. Lett._ , 104(19):193502, May 2014. 

- [98] R. E. George, W. Witzel, H. Riemann, N. V. Abrosimov, N. Nötzel, M. L. W. Thewalt, and J. J. L. Morton. Electron Spin Coherence and Electron Nuclear Double Resonance of Bi Donors in Natural Si. _Phys. Rev. Lett._ , 105(6):067601, August 2010. 

- [99] S. J. Balian. _Quantum-Bath Decoherence of Hybrid Electron-Nuclear Spin Qubits_ . PhD thesis, University College London, 2015. 

- [100] M. H. Mohammady, G. W. Morley, A. Nazir, and T. S. Monteiro. Analysis of quantum coherence in bismuth-doped silicon: A system of strongly coupled spin qubits. _Phys. Rev. B_ , 85(9):094404, March 2012. 

- [101] D. Vion, A. Aassime, A. Cottet, P. Joyez, H. Pothier, C. Urbina, D. Esteve, and M. H. Devoret. Manipulating the Quantum State of an Electrical Circuit. _Science_ , 296(5569):886–889, 2002. 

- [102] E. B. Hale and T. G. Castner Jr. Ground-State Wave Function of Shallow Donors in Uniaxially Stressed Silicon: Piezohyperfine Constants Determined by Electron-Nuclear Double Resonance. _Phys. Rev. B_ , 1(12):4763, 1970. 

- [103] B. Koiller, Xuedong Hu, and S. Das Sarma. Strain effects on silicon donor exchange: Quantum computer architecture considerations. _Phys. Rev. B_ , 66(11):115201, September 2002. 

- [104] H. Huebl, A. R. Stegner, M. Stutzmann, M. S. Brandt, G. Vogg, F. Bensch, E. Rauls, and U. Gerstmann. Phosphorus Donors in Highly Strained Silicon. _Phys. Rev. Lett._ , 97(16):166402, October 2006. 

- [105] M. Usman, C. D. Hill, R. Rahman, G. Klimeck, M. Y. Simmons, S. Rogge, and L. C. L. Hollenberg. Strain and electric field control of hyperfine interactions for donor spin qubits in silicon. _Phys. Rev. B_ , 91(24), June 2015. 

- [106] L. Dreher, T. A. Hilker, A. Brandlmaier, S. T. B. Goennenwein, H. Huebl, M. Stutzmann, and M. S. Brandt. Electroelastic Hyperfine Tuning of Phosphorus Donors in Silicon. _Phys. Rev. Lett._ , 106(3):037601, January 2011. 

- [107] L. Dreher. _Spin Mechanics in Paramagnetic and Ferromagnetic_ . PhD thesis, Verein zur Förderung des Walter-Schottky-Inst. der Techn. Univ. München, April 2013. 

- [108] G. P. Lansbergen, R. Rahman, C. J. Wellard, I. Woo, J. Caro, N. Collaert, S. Biesemans, G. Klimeck, L. C. L. Hollenberg, and S. Rogge. Gate-induced quantum-confinement transition of a single dopant atom in a silicon FinFET. _Nat. Phys._ , 4(8):656–661, August 2008. 

169 

_BIBLIOGRAPHY_ 

- [109] G. Pica, G. Wolfowicz, M. Urdampilleta, M. L. W. Thewalt, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, J. J. L. Morton, R. N. Bhatt, S. A. Lyon, and B. W. Lovett. Hyperfine Stark effect of shallow donors in silicon. _Phys. Rev. B_ , 90(19):195204, November 2014. 

- [110] P. A. Mortemousque, S. Rosenius, G. Pica, D. P. Franke, T. Sekiguchi, A. Truong, M. P. Vlasenko, L. S. Vlasenko, M. S. Brandt, R. G. Elliman, and others. Quadrupole Shift of Nuclear Magnetic Resonance of Donors in Silicon at Low Magnetic Field. _arXiv preprint arXiv:1506.04028_ , 2015. 

- [111] D. P. Franke, M. P. D. Pflüger, P.-A. Mortemousque, K. M. Itoh, and M. S. Brandt. Quadrupolar effects on nuclear spins of neutral arsenic donors in silicon. _Phys. Rev. B_ , 93(16):161303, April 2016. 

- [112] C. P. Slichter. _Principles of Magnetic Resonance_ . Springer Science & Business Media, March 1996. 

- [113] A. Abragam and J. Combrisson. Résonance paramagnétique des impuretés dans un semiconducteur. _Il Nuovo Cimento (1955-1965)_ , 6(3):1197–1212, February 2008. 

- [114] A. Honig and E. Stupp. Electron Spin-Lattice Relaxation in Phosphorus-Doped Silicon. _Phys. Rev._ , 117(1):69–83, January 1960. 

- [115] T. G. Castner Jr. Direct measurement of the valley-orbit splitting of shallow donors in silicon. _Phys. Rev. Lett._ , 8(1):13, 1962. 

- [116] T. G. Castner Jr. Raman spin-lattice relaxation of shallow donors in silicon. _Phys. Rev._ , 130(1):58, 1963. 

- [117] T. G. Castner. Orbach spin-lattice relaxation of shallow donors in silicon. _Phys. Rev._ , 155(3):816, 1967. 

- [118] D. Pines, J. Bardeen, and C. P. Slichter. Nuclear Polarization and Impurity-State Spin Relaxation Processes in Silicon. _Phys. Rev._ , 106(3):489–498, May 1957. 

- [119] E. Abrahams. Donor Electron Spin Relaxation in Silicon. _Phys. Rev._ , 107(2):491–496, July 1957. 

- [120] L. M. Roth. g Factor and Donor Spin-Lattice Relaxation for Electrons in Germanium and Silicon. _Phys. Rev._ , 118(6):1534–1540, June 1960. 

- [121] H. Hasegawa. Spin-Lattice Relaxation of Shallow Donor States in Ge and Si through a Direct Phonon Process. _Phys. Rev._ , 118(6):1523–1534, June 1960. 

- [122] A. Morello, J. J. Pla, F. A. Zwanenburg, Kok W. Chan, Kuan Y. Tan, H. Huebl, M. Möttönen, C. D. Nugroho, Changyi Yang, J. A. van Donkelaar, and others. Single-shot readout of an electron spin in silicon. _Nature_ , 467(7316):687–691, 2010. 

- [123] M. Belli, M. Fanciulli, and N. V. Abrosimov. Pulse electron spin resonance investigation of bismuth-doped silicon: Relaxation and electron spin echo envelope modulation. _Phys. Rev. B_ , 83(23):235204, June 2011. 

- [124] G. Wolfowicz, S. Simmons, A. M. Tyryshkin, R. E. George, H. Riemann, N. V. Abrosimov, P. Becker, H.-J. Pohl, S. A. Lyon, M. L. W. Thewalt, and J. J. L. Morton. Decoherence mechanisms of 209Bi donor electron spins in isotopically pure 28Si. _Phys. Rev. B_ , 86(24):245301, December 2012. 

- [125] N. F. Mott. On the Transition to Metallic Conduction in Semiconductors. _Can. J. Phys._ , 34(12A):1356–1368, December 1956. 

- [126] A. M. Tyryshkin, S. Tojo, J. J. L. Morton, H. Riemann, N. V. Abrosimov, P. Becker, H. Joachim Pohl, T. Schenkel, M. L. W. Thewalt, K. M. Itoh, and S. A. Lyon. Electron spin coherence exceeding seconds in high-purity silicon. _Nat. Mater._ , 11(2):143–147, February 2012. 

- [127] H. Y. Carr and E. M. Purcell. Effects of Diffusion on Free Precession in Nuclear Magnetic Resonance Experiments. _Phys. Rev._ , 94(3):630–638, May 1954. 

170 

_BIBLIOGRAPHY_ 

- [128] S. Meiboom and D. Gill. Modified Spin-Echo Method for Measuring Nuclear Relaxation Times. _Rev. Sci. Instrum._ , 29(8):688–691, August 1958. 

- [129] W.-L. Ma, G. Wolfowicz, Shu-Shen Li, J. J. L. Morton, and Ren-Bao Liu. Classical nature of nuclear spin noise near clock transitions of Bi donors in silicon. _Phys. Rev. B_ , 92(16):161403, October 2015. 

- [130] A. Gruber, A. Dräbenstedt, C. Tietz, L. Fleury, J. Wrachtrup, and C. Von Borczyskowski. Scanning confocal optical microscopy and magnetic resonance on single defect centers. _Science_ , 276(5321):2012–2014, 1997. 

- [131] A. Yang, M. Steger, D. Karaiskaj, M. L. W. Thewalt, M. Cardona, K. M. Itoh, H. Riemann, N. V. Abrosimov, M. F. Churbanov, A. V. Gusev, A. D. Bulanov, A. K. Kaliteevskii, O. N. Godisov, P. Becker, H.-J. Pohl, J. W. Ager, and E. E. Haller. Optical Detection and Ionization of Donors in Specific Electronic and Nuclear Spin States. _Phys. Rev. Lett._ , 97(22), November 2006. 

- [132] A. Yang, M. Steger, T. Sekiguchi, M. L. W. Thewalt, T. D. Ladd, K. M. Itoh, H. Riemann, N. V. Abrosimov, P. Becker, and H.-J. Pohl. Simultaneous Subsecond Hyperpolarization of the Nuclear and Electron Spins of Phosphorus in Silicon by Optical Pumping of Exciton Transitions. _Phys. Rev. Lett._ , 102(25):257401, June 2009. 

- [133] M. Steger, K. Saeedi, M. L. W. Thewalt, J. J. L. Morton, H. Riemann, N. V. Abrosimov, P. Becker, and H.-J. Pohl. Quantum Information Storage for over 180 s Using Donor Spins in a 28Si Semiconductor Vacuum. _Science_ , 336(6086):1280–1283, 2012. 

- [134] T. Sekiguchi, M. Steger, K. Saeedi, M. L. W. Thewalt, H. Riemann, N. V. Abrosimov, and N. Nötzel. Hyperfine Structure and Nuclear Hyperpolarization Observed in the Bound Exciton Luminescence of Bi Donors in Natural Si. _Phys. Rev. Lett._ , 104(13):137402, April 2010. 

- [135] P. Becker, D. Schiel, H.-J. Pohl, A. K. Kaliteevski, O. N. Godisov, M. F. Churbanov, G. G. Devyatykh, A. V. Gusev, A. D. Bulanov, S. A. Adamchik, V. A. Gavva, I. D. Kovalev, N. V. Abrosimov, B. Hallmann-Seiffert, H. Riemann, S. Valkiers, P. Taylor, P. De Bièvre, and E. M. Dianov. Large-scale production of highly enriched<sup>28</sup> Si for the precise determination of the Avogadro constant. _Meas. Sci. Technol._ , 17(7):1854–1860, July 2006. 

- [136] P. Studer, S. R. Schofield, C. F. Hirjibehedin, and N. J. Curson. Studying atomic scale structural and electronic properties of ion implanted silicon samples using cross-sectional scanning tunneling microscopy. _Appl. Phys. Lett._ , 102(1):012107, 2013. 

- [137] C. D. Weis, C. C. Lo, V. Lang, A. M. Tyryshkin, R. E. George, K. M. Yu, J. Bokor, S. A. Lyon, J. J. L. Morton, and T. Schenkel. Electrical activation and electron spin resonance measurements of implanted bismuth in isotopically enriched silicon-28. _Appl. Phys. Lett._ , 100(17):172104, 2012. 

- [138] Y. Manassen, R. J. Hamers, J. E. Demuth, and A. J. Castellano Jr. Direct observation of the precession of individual paramagnetic spins on oxidized silicon surfaces. _Phys. Rev. Lett._ , 62(21):2531–2534, May 1989. 

- [139] D. Rugar, C. S. Yannoni, and J. A. Sidles. Mechanical detection of magnetic resonance. _Nature_ , 360(6404):563–566, 1992. 

- [140] D. Rugar, R. Budakian, H. J. Mamin, and B. W. Chui. Single spin detection by magnetic resonance force microscopy. _Nature_ , 430(6997):329–332, 2004. 

- [141] J. M. Taylor, P. Cappellaro, L. Childress, L. Jiang, P. R. Hemmer, A. Yacoby, R. Walsworth, and M. D. Lukin. High-sensitivity diamond magnetometer with nanoscale resolution. _Nat. Phys._ , 4:810, 2008. 

- [142] Y. Twig, E. Dikarov, W. D. Hutchison, and A. Blank. Note: High sensitivity pulsed electron spin resonance spectroscopy with induction detection. _Rev. Sci. Instrum._ , 82(7):076105, 2011. 

171 

_BIBLIOGRAPHY_ 

- [143] A. Blank, E. Dikarov, R. Shklyar, and Y. Twig. Induction-detection electron spin resonance with sensitivity of 1000 spins: En route to scalable quantum computations. _Physics Letters A_ , 377(31):1937–1942, 2013. 

- [144] C. Durkan and M. E. Welland. Electronic spin detection in molecules using scanning-tunnelingmicroscopy-assisted electron-spin resonance. _Appl. Phys. Lett._ , 80(3):458, 2002. 

- [145] J. Wrachtrup, C. Von Borczyskowski, J. Bernard, M. Orritt, and R. Brown. Optical detection of magnetic resonance in a single molecule. _Nature_ , 363:244–245, 1993. 

- [146] M. S. Grinolds, M. Warner, K. De Greve, Y. Dovzhenko, L. Thiel, R. L. Walsworth, S. Hong, P. Maletinsky, and A. Yacoby. Subnanometre resolution in three-dimensional magnetic resonance imaging of individual dark spins. _Nat. Nanotechnol._ , 9(4):279–284, 2014. 

- [147] J. Elzerman, R. Hanson, L. Willems van Beveren, B. Witkamp, L.M.K. Vandersypen, and L. Kouwenhoven. Single-shot read-out of an individual electron spin in a quantum dot. _Nature_ , 430:431, 2004. 

- [148] M. Xiao, I. Martin, E. Yablonovitch, and H. W. Jiang. Electrical detection of the spin resonance of a single electron in a silicon field-effect transistor. _Nature_ , 430(6998):435–439, July 2004. 

- [149] R. Vincent, S. Klyatskaya, M. Ruben, W. Wernsdorfer, and F. Balestro. Electronic read-out of a single nuclear spin using a molecular spin transistor. _Nature_ , 488(7411):357–360, 2012. 

- [150] M. Veldhorst, J. C. C. Hwang, C. H. Yang, A. W. Leenstra, B. de Ronde, J. P. Dehollain, J. T. Muhonen, F. E. Hudson, K. M. Itoh, A. Morello, and A. S. Dzurak. An addressable quantum dot qubit with fault-tolerant control fidelity. _Nat. Nanotechnol._ , 9(12):1–10, 2014. 

- [151] J. J. Pla, K. Y. Tan, J. P. Dehollain, W. H. Lim, J. J. L. Morton, D. N. Jamieson, A. S. Dzurak, and A. Morello. A single-atom electron spin qubit in silicon. _Nature_ , 489(7417):541–545, 2012. 

- [152] S. Thiele, F. Balestro, R. Ballou, S. Klyatskaya, M. Ruben, and . Wernsdorfer. Electrically driven nuclear spin resonance in single-molecule magnets. _Science_ , 344(6188):1135–1138, 2014. 

- [153] T. Sleator, E. L. Hahn, C. Hilbert, and J. Clarke. Nuclear-spin noise and spontaneous emission. _Phys. Rev. B_ , 36(4):1969–1980, August 1987. 

- [154] J. Schleeh, G. Alestig, J. Halonen, A. Malmros, B. Nilsson, P. A. Nilsson, J. P. Starski, N. Wadefalk, H. Zirath, and J. Grahn. Ultralow-Power Cryogenic InP HEMT With Minimum Noise Temperature of 1 K at 6 GHz. _IEEE Electr. Device L._ , 33(5):664–666, May 2012. 

- [155] S. E. de Graaf, D. Davidovikj, A. Adamyan, S. E. Kubatkin, and A. V. Danilov. Galvanically split superconducting microwave resonators for introducing internal voltage bias. _Appl. Phys. Lett._ , 104(5):052601, February 2014. 

- [156] I. Wisby, S. E. de Graaf, R. Gwilliam, A. Adamyan, S. E. Kubatkin, P. J. Meeson, A. Y. Tzalenchuk, and T. Lindström. Coupling of a locally implanted rare-earth ion ensemble to a superconducting micro-resonator. _Appl. Phys. Lett._ , 105(10):102601, 2014. 

- [157] N. Samkharadze, A. Bruno, P. Scarlino, G. Zheng, D. P. DiVincenzo, L. DiCarlo, and L. M. K. Vandersypen. High-Kinetic-Inductance Superconducting Nanowire Resonators for Circuit QED in a Magnetic Field. _Appl. Phys. Lett._ , 5(4):044004, April 2016. 

- [158] T. Roy, S. Kundu, M. Chand, A. M. Vadiraj, A. Ranadive, N. Nehra, M. P. Patankar, J. Aumentado, A. A. Clerk, and R. Vijay. Broadband parametric amplification with impedance engineering: Beyond the gain-bandwidth product. _Appl. Phys. Lett._ , 107(26):262601, December 2015. 

- [159] M. A. Castellanos-Beltran, K.D. Irwin, G. C. Hilton, L. R. Vale, and K. W. Lehnert. Amplification and squeezing of quantum noise with a tunable Josephson metamaterial. _Nat. Phys._ , 4(12):929–931, 2008. 

172 

_BIBLIOGRAPHY_ 

- [160] K. Cicak, D. Li, J. A. Strong, M. S. Allman, F. Altomare, A. J. Sirois, J. D. Whittaker, J. D. Teufel, and R. W. Simmonds. Low-loss superconducting resonant circuits using vacuum-gap-based microwave components. _Appl. Phys. Lett._ , 96(9):093502, 2010. 

- [161] A. Megrant, C. Neill, R. Barends, B. Chiaro, Yu Chen, L. Feigl, J. Kelly, Erik Lucero, Matteo Mariantoni, P. J. J. O’Malley, D. Sank, A. Vainsencher, J. Wenner, T. C. White, Y. Yin, J. Zhao, C. J. Palmstrom, John M. Martinis, and A. N. Cleland. Planar superconducting resonators with internal quality factors above one million. _Appl. Phys. Lett._ , 100:113510, 2012. 

- [162] C. Song, M. P. DeFeo, K. Yu, and B. L. T. Plourde. Reducing microwave loss in superconducting resonators due to trapped vortices. _Appl. Phys. Lett._ , 95(23):232501, 2009. 

- [163] R. Barends, J. Wenner, M. Lenander, Y. Chen, R. C. Bialczak, J. Kelly, E. Lucero, P. O’Malley, M. Mariantoni, D. Sank, H. Wang, T. C. White, Y. Yin, J. Zhao, A. N. Cleland, John M. Martinis, and J. J. A. Baselmans. Minimizing quasiparticle generation from stray infrared light in superconducting quantum circuits. _Appl. Phys. Lett._ , 99(11):113507, September 2011. 

- [164] Aaron D. O’Connell, M. Ansmann, R. C. Bialczak, M. Hofheinz, N. Katz, Erik Lucero, C. McKenney, M. Neeley, H. Wang, E. M. Weig, A. N. Cleland, and J. M. Martinis. Microwave dielectric loss at single photon energies and millikelvin temperatures. _Appl. Phys. Lett._ , 92(11):112903, 2008. 

- [165] D. S. Wisbey, J. Gao, M. R. Vissers, F. C. S. da Silva, J. S. Kline, L. Vale, and D. P. Pappas. Effect of metal/substrate interfaces on radio-frequency loss in superconducting coplanar waveguides. _J. Appl. Phys._ , 108(9):093918, November 2010. 

- [166] A. A. Houck, J. A. Schreier, B. R. Johnson, J. M. Chow, Jens Koch, J. M. Gambetta, D. I. Schuster, L. Frunzio, M. H. Devoret, S. M. Girvin, and R. J. Schoelkopf. Controlling the spontaneous emission of a superconducting transmon qubit. _Phys. Rev. Lett._ , 101:080502, Aug 2008. 

- [167] H. Paik, D. I. Schuster, L. S. Bishop, G. Kirchmair, G. Catelani, A. P. Sears, B. R. Johnson, M. J. Reagor, L. Frunzio, L. I. Glazman, S. M. Girvin, M. H. Devoret, and R. J. Schoelkopf. Observation of High Coherence in Josephson Junction Qubits Measured in a Three-Dimensional Circuit QED Architecture. _Phys. Rev. Lett._ , 107(24):240501, December 2011. 

- [168] M. Reagor, H. Paik, G. Catelani, L. Sun, C. Axline, E. Holland, I. M. Pop, N. A. Masluk, T. Brecht, L. Frunzio, M. H. Devoret, L. Glazman, and R. J. Schoelkopf. Reaching 10 ms single photon lifetimes for superconducting aluminum cavities. _Appl. Phys. Lett._ , 102(19):192604, 2013. 

- [169] C. Wang, C. Axline, Y. Y. Gao, T. Brecht, Y. Chu, L. Frunzio, M. H. Devoret, and R. J. Schoelkopf. Surface participation and dielectric loss in superconducting qubits. _Appl. Phys. Lett._ , 107(16):162601, October 2015. 

- [170] D. Ristè, S. Poletto, M.-Z. Huang, A. Bruno, V. Vesterinen, O.-P. Saira, and L. DiCarlo. Detecting bit-flip errors in a logical qubit using stabilizer measurements. _Nat. Commun._ , 6:6983, April 2015. 

- [171] J. W. C. De Vries. Temperature and thickness dependence of the resistivity of thin polycrystalline aluminium, cobalt, nickel, palladium, silver and gold films. _Thin Solid Films_ , 167(1):25–32, December 1988. 

- [172] J. Wenner, R. Barends, R. C. Bialczak, Yu Chen, J. Kelly, Erik Lucero, Matteo Mariantoni, A. Megrant, P. J. J. O’Malley, D. Sank, A. Vainsencher, H. Wang, T. C. White, Y. Yin, J. Zhao, A. N. Cleland, and John M. Martinis. Surface loss simulations of superconducting coplanar waveguide resonators. _Appl. Phys. Lett._ , 99(11):113513, 2011. 

- [173] T. Van Duzer and C. Turner. _Superconductive Devices and Circuits_ . Prentice Hall PTR, 1999. 

173 

_BIBLIOGRAPHY_ 

- [174] J. Romijn, T. M. Klapwijk, M. J. Renne, and J. E. Mooij. Critical pair-breaking current in superconducting aluminum strips far below tc. _Phys. Rev. B_ , 26(7):3648–3655, October 1982. 

- [175] C. M. Quintana, A. Megrant, Z. Chen, A. Dunsworth, B. Chiaro, R. Barends, B. Campbell, Yu Chen, I.-C. Hoi, E. Jeffrey, J. Kelly, J. Y. Mutus, P. J. J. O’Malley, C. Neill, P. Roushan, D. Sank, A. Vainsencher, J. Wenner, T. C. White, A. N. Cleland, and John M. Martinis. Characterization and reduction of microfabrication-induced decoherence in superconducting quantum circuits. _Appl. Phys. Lett._ , 105(6):062601, August 2014. 

- [176] A. Bruno, G. de Lange, S. Asaad, K. L. van der Enden, N. K. Langford, and L. DiCarlo. Reducing intrinsic loss in superconducting resonators by surface treatment and deep etching of silicon substrates. _Appl. Phys. Lett._ , 106(18):182601, May 2015. 

- [177] J. J. Pla, A. Bienfait, G. Pica, J. Mansir, F. A. Mohiyaddin, A. Morello, T. Schenkel, B. W. Lovett, J. J. L. Morton, and P. Bertet. Strain-induced nuclear quadrupole splittings in silicon devices. _arxiv_ , 2017. 

- [178] E. N. Kaufmann and R. J. Vianden. The electric field gradient in noncubic metals. _Rev. Mod. Phys._ , 51(1):161, 1979. 

- [179] F. D. Feiock and W. R. Johnson. Atomic Susceptibilities and Shielding Factors. _Phys. Rev._ , 187(1):39, 1969. 

- [180] B. V. Van Zeghbroeck. _Principles of Semiconductor Devices and Heterojunctions_ . Prentice Hall, Upper Saddle River, N.J.; London, 1 edition edition, December 2009. 

- [181] R. E. Hummel. _Electronic Properties of Materials_ . Springer New York, New York, NY, 2011. 

- [182] B. Julsgaard and K. Mølmer. Reflectivity and transmissivity of a cavity coupled to two-level systems: Coherence properties and the influence of phase decay. _Phys. Rev. A_ , 85:013844, 2012. 

- [183] F. Mentink-Vigier, A. Collauto, A. Feintuch, I. Kaminker, V. Tarle, and D. Goldfarb. Increasing sensitivity of pulse EPR experiments using echo train detection schemes. _J. Magn. Reson._ , 236:117–125, 2013. 

- [184] T. Gullion, D. B. Baker, and M. S. Conradi. New, compensated Carr-Purcell sequences. _J. Magn. Reson. (1969)_ , 89(3):479–484, October 1990. 

- [185] C. Santori, P. Tamarat, P. Neumann, Jörg Wrachtrup, D. Fattal, R. G. Beausoleil, J. Rabeau, P. Olivero, A. D. Greentree, S. Prawer, and others. Coherent population trapping of single spins in diamond under optical excitation. _Phys. Rev. Lett._ , 97(24):247401, 2006. 

- [186] M. G. Shapiro, G. G. Westmeyer, P. A. Romero, J. O. Szablowski, B. Küster, A. Shah, C. R. Otey, R. Langer, F. H. Arnold, and A. Jasanoff. Directed evolution of a magnetic resonance imaging contrast agent for noninvasive imaging of dopamine. _Nat. Biotechnol._ , 28(3):264–270, 2010. 

- [187] T. Sleator, E. L. Hahn, C. Hilbert, and J. Clarke. Nuclear-spin noise. _Phys. Rev. Lett._ , 55(17):1742– 1745, October 1985. 

- [188] E. M. Purcell. Spontaneous emission probabilities at radio frequencies. _Phys. Rev._ , 69:681, 1946. 

- [189] S. Haroche and D. Kleppner. Cavity Quantum Electrodynamics. _Physics Today_ , 42(1):24, 1989. 

- [190] M. O. Scully and M. Suhail Zubairy. _Quantum Optics_ . Cambridge University Press, 1997. 

- [191] D. Kleppner. Inhibited Spontaneous Emission. _Phys. Rev. Lett._ , 47(4):233–236, July 1981. 

- [192] I. V. Hertel and C.-P. Schulz. _Atoms, Molecules and Optical Physics 2: Molecules and Photons - Spectroscopy and Collisions_ . Springer, October 2014. 

- [193] K. H. Drexhage. Influence of a dielectric interface on fluorescence decay time. _J. Lumin._ , 1:693–701, January 1970. 

174 

_BIBLIOGRAPHY_ 

- [194] G. Gabrielse and H. Dehmelt. Observation of inhibited spontaneous emission. _Phys. Rev. Lett._ , 55(1):67–70, July 1985. 

- [195] R. G. Hulet, E. S. Hilfer, and D. Kleppner. Inhibited Spontaneous Emission by a Rydberg Atom. _Phys. Rev. Lett._ , 55(20):2137–2140, 1985. 

- [196] W. Jhe, A. Anderson, E. A. Hinds, D. Meschede, L. Moi, and S. Haroche. Suppression of spontaneous decay at optical frequencies: Test of vacuum-field anisotropy in confined space. _Phys. Rev. Lett._ , 58(7):666–669, February 1987. 

- [197] D. J. Heinzen, J. J. Childs, J. E. Thomas, and M. S. Feld. Enhanced and inhibited visible spontaneous emission by atoms in a confocal resonator. _Phys. Rev. Lett._ , 58(13):1320–1323, March 1987. 

- [198] F. De Martini, G. Innocenti, G. R. Jacobovitz, and P. Mataloni. Anomalous Spontaneous Emission Time in a Microscopic Optical Cavity. _Phys. Rev. Lett._ , 59(26):2955–2958, December 1987. 

- [199] E. Yablonovitch. Inhibited Spontaneous Emission in Solid-State Physics and Electronics. _Phys. Rev. Lett._ , 58(20):2059–2062, May 1987. 

- [200] Y. Yamamoto, S. Machida, Y. Horikoshi, K. Igeta, and G. Bjork. Enhanced and inhibited spontaneous emission of free excitons in GaAs quantum wells in a microcavity. _Opt. Commun._ , 80:337 – 342, 1991. 

- [201] B. Gayral, J.-M. Gérard, B. Sermage, A. Lemaı<sup>ˆ</sup> tre, and C. Dupuis. Time-resolved probing of the Purcell effect for InAs quantum boxes in GaAs microdisks. _Appl. Phys. Lett._ , 78(19):2828–2830, May 2001. 

- [202] D. Englund, D. Fattal, E. Waks, G. Solomon, B. Zhang, T. Nakaoka, Y. Arakawa, Y. Yamamoto, and J. Vuˇckovi´c. Controlling the Spontaneous Emission Rate of Single Quantum Dots in a Two-Dimensional Photonic Crystal. _Phys. Rev. Lett._ , 95(1):013904, July 2005. 

- [203] J. Riedrich-Möller, L. Kipfstuhl, C. Hepp, E. Neu, C. Pauly, F. Mücklich, A. Baur, M. Wandt, S. Wolff, M. Fischer, S. Gsell, M. Schreck, and C. Becher. One- and two-dimensional photonic crystal microcavities in single crystal diamond. _Nat. Nanotechnol._ , 7(1):69–74, jan 2012. 

- [204] S. Schietinger, M. Barth, T. Aichele, and O. Benson. Plasmon-Enhanced Single Photon Emission from a Nanoassembled Metal-Diamond Hybrid Structure at Room Temperature. _Nano Letters_ , 9(4):1694–1698, April 2009. 

- [205] R. C. Bialczak, M. Ansmann, M. Hofheinz, M. Lenander, E. Lucero, M. Neeley, A. D. O’Connell, D. Sank, H. Wang, M. Weides, J. Wenner, T. Yamamoto, A. N. Cleland, and J. M. Martinis. Fast Tunable Coupler for Superconducting Qubits. _Phys. Rev. Lett._ , 106(6), February 2011. 

- [206] J. Kerckhoff, R. W. Andrews, H. S. Ku, W. F. Kindel, K. Cicak, R. W. Simmonds, and K. W. Lehnert. Tunable Coupling to a Mechanical Oscillator Circuit Using a Coherent Feedback Network. _Phys. Rev. X_ , 3:021013, 2013. 

- [207] N. Bloembergen. On the interaction of nuclear spins in a crystalline lattice. _Physica_ , 15(3):386– 426, May 1949. 

- [208] A. Abragam and M. Goldman. Principles of dynamic nuclear polarisation. _Rep. Prog. Phys._ , 41(3):395, 1978. 

- [209] T. R. Carver and C. P. Slichter. Polarization of Nuclear Spins in Metals. _Phys. Rev._ , 92(1):212–213, October 1953. 

- [210] D. Stoler. Equivalence Classes of Minimum Uncertainty Packets. _Phys. Rev. D_ , 1(12):3217–3219, June 1970. 

175 

_BIBLIOGRAPHY_ 

- [211] H. P. Yuen. Two-photon coherent states of the radiation field. _Phys. Rev. A_ , 13(6):2226–2243, June 1976. 

- [212] T. Eberle, S. Steinlechner, J. Bauchrowitz, V. Händchen, H. Vahlbruch, M. Mehmet, H. MüllerEbhardt, and R. Schnabel. Quantum Enhancement of the Zero-Area Sagnac Interferometer Topology for Gravitational Wave Detection. _Phys. Rev. Lett._ , 104(25):251102, June 2010. 

- [213] The LIGO Scientific Collaboration. A gravitational wave observatory operating beyond the quantum shot-noise limit. _Nat. Phys._ , 7(12):962–965, December 2011. 

- [214] E. S. Polzik, J. Carri, and H. J. Kimble. Spectroscopy with squeezed light. _Phys. Rev. Lett._ , 68(20):3020–3023, May 1992. 

- [215] M. A. Taylor, J. Janousek, V. Daria, J. Knittel, B. Hage, H. A. Bachor, and W. P. Bowen. Biological measurement beyond the quantum limit. _Nat. Photonicsics_ , 7(3):229–233, February 2013. 

- [216] F. Mallet, M. A. Castellanos-Beltran, H. S. Ku, S. Glancy, E. Knill, K. D. Irwin, G. C. Hilton, L. R. Vale, and K. W. Lehnert. Quantum State Tomography of an Itinerant Squeezed Microwave Field. _Phys. Rev. Lett._ , 106(22):220502, June 2011. 

- [217] K. W. Murch, S. J. Weber, K. M. Beck, E. Ginossar, and I. Siddiqi. Reduction of the radiative decay of atomic coherence in squeezed vacuum. _Nature_ , 499(7456):62–65, July 2013. 

- [218] D. F. Walls. Squeezed states of light. _Nature_ , 306(5939):141–146, November 1983. 

- [219] N. Didier, A. Kamal, W. D. Oliver, A. Blais, and A. A. Clerk. Heisenberg-Limited Qubit Read-Out with Two-Mode Squeezed Light. _Phys. Rev. Lett._ , 115(9):093604, August 2015. 

- [220] N. Didier, J. Bourassa, and A. Blais. Fast Quantum Nondemolition Readout by Parametric Modulation of Longitudinal Qubit-Oscillator Interaction. _Phys. Rev. Lett._ , 115(20):203601, November 2015. 

- [221] C. W. Gardiner. Inhibition of Atomic Phase Decays by Squeezed Light: A Direct Effect of Squeezing. _Phys. Rev. Lett._ , 56(18):1917–1920, May 1986. 

- [222] T. Holstein and H. Primakoff. Field Dependence of the Intrinsic Domain Magnetization of a Ferromagnet. _Phys. Rev._ , 58:1098, 1940. 

- [223] Z. Kurucz, J. H. Wesenberg, and K. Mølmer. Spectroscopic properties of inhomogeneously broadened spin ensembles in a cavity. _Phys. Rev. A_ , 83:053852, 2011. 

- [224] I. Diniz, S. Portolan, R. Ferreira, J. M. Gérard, P. Bertet, and A. Auffèves. Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived solid-state quantum memories. _Phys. Rev. A_ , 84:063810, 2011. 

- [225] J. Kerckhoff, K. Lalumière, B. J. Chapman, A. Blais, and W. Lehnert, K.˙On-Chip Superconducting Microwave Circulator from Synthetic Rotation. _Appl. Phys. Lett._ , 4(3):034002, September 2015. 

- [226] M. Sliwa, K. M. Hatridge, A. Narla, S. Shankar, L. Frunzio, J. Schoelkopf, R. and H. Devoret, M.˙ Reconfigurable Josephson Circulator/Directional Amplifier. _Phys. Rev. X_ , 5(4):041020, November 2015. 

- [227] A. Facon, E.-K. Dietsche, D. Grosso, S. Haroche, J.-M. Raimond, M. Brune, and S. Gleyzes. A sensitive electrometer based on a Rydberg atom in a Schrödinger-cat state. _Nature_ , 535(7611):262–265, July 2016. 

- [228] H. Strobel, W. Muessel, D. Linnemann, T. Zibold, D. B. Hume, L. Pezzè, A. Smerzi, and M. K. Oberthaler. Fisher information and entanglement of non-Gaussian spin states. _Science_ , 345(6195):424–427, July 2014. 

176 

_BIBLIOGRAPHY_ 

- [229] V. Mourik, K. Zuo, S. M. Frolov, S. R. Plissard, E. P. a. M. Bakkers, and L. P. Kouwenhoven. Signatures of Majorana Fermions in Hybrid Superconductor-Semiconductor Nanowire Devices. _Science_ , 336(6084):1003–1007, May 2012. 

- [230] M. R. Delbecq, V. Schmitt, F. D. Parmentier, N. Roch, J. J. Viennot, G. Fève, B. Huard, C. Mora, A. Cottet, and T. Kontos. Coupling a Quantum Dot, Fermionic Leads, and a Microwave Cavity on a Chip. _Phys. Rev. Lett._ , 107(25):256804, December 2011. 

- [231] Y.-Y. Liu, D. Petersson, K. J. Stehlik, M. Taylor, J. and R. Petta, J.˙ Photon Emission from a Cavity-Coupled Double Quantum Dot. _Phys. Rev. Lett._ , 113(3):036801, July 2014. 

- [232] G. Tosi, F. A. Mohiyaddin, H. Huebl, and A. Morello. Circuit-quantum electrodynamics with direct magnetic coupling to single-atom spin qubits in isotopically enriched 28Si. _AIP Advances_ , 4(8):087122, August 2014. 

- [233] C. P. Poole. _Electron Spin Resonance: A Comprehensive Treatise on Experimental Techniques_ . Courier Corporation, 1996. 

- [234] M. Mas-Torrent, N. Crivillers, C. Rovira, and J. Veciana. Attaching Persistent Organic Free Radicals to Surfaces: How and Why. _Chem. Rev._ , 112(4):2506–2527, April 2012. 

- [235] E. J. Hill and J. H. Burgess. Vapor deposition of thin films of DPPH and BDPA. _Thin Solid Films_ , 11(1):99–103, July 1972. 

- [236] H. Bernien, B. Hensen, W. Pfaff, G. Koolstra, M. S. Blok, L. Robledo, T. H. Taminiau, M. Markham, D. J. Twitchen, and R. Hanson. Heralded entanglement between solid-state qubits separated by three metres. _Nature_ , 497:86, 2013. 

- [237] J. J. Pla, K. Y. Tan, J. P. Dehollain, W. H. Lim, J. J. L. Morton, F. Zwanenburg, D. N. Jamieson, A. S. Dzurak, and A. Morello. High-fidelity readout and control of a nuclear spin qubit in silicon. _Nature_ , 496:334–8, 2013. 

- [238] J. Koch, T. M. Yu, J. Gambetta, A. A. Houck, D. I. Schuster, J. Majer, A. Blais, M. H. Devoret, S. M. Girvin, and R. J. Schoelkopf. Charge-insensitive qubit design derived from the Cooper pair box. _Phys. Rev. A_ , 76:042319, 2007. 

- [239] J. Gambetta, A. Blais, D. I. Schuster, A. Wallraff, L. Frunzio, J. Majer, M. H. Devoret, S. M. Girvin, and R. J. Schoelkopf. Qubit-photon interactions in a cavity: Measurement-induced dephasing and number splitting. _Phys. Rev. A_ , 74(4):042318, 2006. 

- [240] A. Blais, J. Gambetta, A. Wallraff, D. I. Schuster, S. M. Girvin, M. H. Devoret, and R. J. Schoelkopf. Quantum-information processing with circuit quantum electrodynamics. _Phys. Rev. A_ , 75(3):032329, March 2007. 

- [241] V. Schmitt, X. Zhou, K. Juliusson, B. Royer, A. Blais, P. Bertet, D. Vion, and D Esteve. Multiplexed readout of transmon qubits with Josephson bifurcation amplifiers. _Phys. Rev. A_ , 90(6):062333, 2014. 

- [242] A. Wallraff, D. I. Schuster, A. Blais, L. Frunzio, J. Majer, M. H. Devoret, S. M. Girvin, and R. J. Schoelkopf. Approaching Unit Visibility for Control of a Superconducting Qubit with Dispersive Readout. _Phys. Rev. Lett._ , 95(6):060501, August 2005. 

- [243] M.D. Reed, L. DiCarlo, B. R. Johnson, L. Sun, D. I. Schuster, L. Frunzio, and R. J. Schoelkopf. High-fidelity readout in circuit quantum electrodynamics using the Jaynes-Cummings nonlinearity. _Phys. Rev. Lett._ , 105(17):173601, 2010. 

- [244] C. Rigetti, J. M. Gambetta, S. Poletto, B. L. T. Plourde, J. M. Chow, A. D. Córcoles, J. A. Smolin, S. T. Merkel, J. R. Rozen, G. A. Keefe, M. B. Rothwell, M. B. Ketchen, and M. Steffen. Superconducting qubit in a waveguide cavity with a coherence time approaching 0.1 ms. _Phys. Rev. B_ , 86(10):100506, September 2012. 

177 

_BIBLIOGRAPHY_ 

- [245] D. M. Pozar. _Microwave engineering_ . John Wiley & Sons, 2009. 

- [246] M. Boissonneault, J. M. Gambetta, and A. Blais. Dispersive regime of circuit QED: Photondependent qubit dephasing and relaxation rates. _Phys. Rev. A_ , 79(1):013819, 2009. 

178 

ECOLE DOCTORALE oS * i Physique universite : en Tle-de-France PARIS-SACLAY i: (EDPIF) 



