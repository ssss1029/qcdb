"""
| Database of <description of members and reference energy type>.
| Geometries from <Reference>.
http://www.thch.uni-bonn.de/tc/downloads/GMTKN/GMTKN30/PCONF.html
| Reference interaction energies from <Reference>.
Taken from Reha, D.; Valdes, H.; Vondrasek, J.; Hobza, P.; Abu-Riziq, A.; Crews, B.; de Vries, M. S. Chem. Eur. J. 2005, 11, 6803-6817.
(estimated CCSD(T)/CBS); all values are in kcal/mol.


- **benchmark**

  - ``'<benchmark_name>'`` <Reference>.
  - |dl| ``'<default_benchmark_name>'`` |dr| <Reference>.

- **subset**

  - ``'small'`` <members_description>
  - ``'large'`` <members_description>
  - ``'<subset>'`` <members_description>

"""
import re
import qcdb

# <<< PCONF Database Module >>>
dbse = 'PCONF'

# <<< Database Members >>>
HRXN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]

# <<< Chemical Systems Involved >>>
RXNM = {}     # reaction matrix of reagent contributions per reaction
ACTV = {}     # order of active reagents per reaction
ACTV['%s-%s'            % (dbse, '1'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '444') ]
RXNM['%s-%s'            % (dbse, '1'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '1')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '2'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '357') ]
RXNM['%s-%s'            % (dbse, '2'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '2')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '3'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '366') ]
RXNM['%s-%s'            % (dbse, '3'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '3')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '4'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '215') ]
RXNM['%s-%s'            % (dbse, '4'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '4')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '5'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '300') ]
RXNM['%s-%s'            % (dbse, '5'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '5')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '6'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '114') ]
RXNM['%s-%s'            % (dbse, '6'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '6')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '7'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '412') ]
RXNM['%s-%s'            % (dbse, '7'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '7')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '8'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '691') ]
RXNM['%s-%s'            % (dbse, '8'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '8')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '9'                     )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '470') ]
RXNM['%s-%s'            % (dbse, '9'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '9')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '10'                    )] = ['%s-%s-reagent'      % (dbse, '99'),
                                                               '%s-%s-reagent'      % (dbse, '224') ]
RXNM['%s-%s'            % (dbse, '10'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '10')], [-1, +1]))

# <<< Reference Values [kcal/mol] >>>
BIND = {}
# Original publication
BIND_PCONF0 = {}
BIND_PCONF0['%s-%s'            % (dbse, '1'                     )] =    0.14
BIND_PCONF0['%s-%s'            % (dbse, '2'                     )] =    0.90
BIND_PCONF0['%s-%s'            % (dbse, '3'                     )] =    1.15
BIND_PCONF0['%s-%s'            % (dbse, '4'                     )] =    0.79
BIND_PCONF0['%s-%s'            % (dbse, '5'                     )] =    1.31
BIND_PCONF0['%s-%s'            % (dbse, '6'                     )] =    1.87
BIND_PCONF0['%s-%s'            % (dbse, '7'                     )] =    2.37
BIND_PCONF0['%s-%s'            % (dbse, '8'                     )] =    2.07
BIND_PCONF0['%s-%s'            % (dbse, '9'                     )] =    2.51
BIND_PCONF0['%s-%s'            % (dbse, '10'                    )] =    2.04
# Current revision
BIND_PCONFA = {}
BIND_PCONFA['%s-%s'            % (dbse, '1'                     )] =    0.421
BIND_PCONFA['%s-%s'            % (dbse, '2'                     )] =    1.122
BIND_PCONFA['%s-%s'            % (dbse, '3'                     )] =    1.716
BIND_PCONFA['%s-%s'            % (dbse, '4'                     )] =    1.097
BIND_PCONFA['%s-%s'            % (dbse, '5'                     )] =    1.833
BIND_PCONFA['%s-%s'            % (dbse, '6'                     )] =    2.040
BIND_PCONFA['%s-%s'            % (dbse, '7'                     )] =    2.391
BIND_PCONFA['%s-%s'            % (dbse, '8'                     )] =    2.544
BIND_PCONFA['%s-%s'            % (dbse, '9'                     )] =    2.717
BIND_PCONFA['%s-%s'            % (dbse, '10'                    )] =    2.254
# Set default
BIND = BIND_PCONFA
# Reference information
BINDINFO_PCONF0 = {}
BINDINFO_PCONFA = {}
for rxn in HRXN:
    BINDINFO_PCONF0['%s-%s' % (dbse, rxn)] = {'citation': 'pconf0', 'method': 'CCSDT', 'mode': 'unCP', 'basis': 'tqz631gs025'}
    BINDINFO_PCONFA['%s-%s' % (dbse, rxn)] = {'citation': 'dfit', 'method': 'CCSDTAF12', 'mode': 'dfhf_dfmp_unCP', 'basis': 'aq5zadz'}  # non-f12 mp2 xtpl

# <<< Comment Lines >>>
TAGL = {}
TAGL['%s-%s'            % (dbse, '1'                     )] = """FGG 444 vs. 99"""
TAGL['%s-%s'            % (dbse, '2'                     )] = """FGG 357 vs. 99"""
TAGL['%s-%s'            % (dbse, '3'                     )] = """FGG 366 vs. 99"""
TAGL['%s-%s'            % (dbse, '4'                     )] = """FGG 215 vs. 99"""
TAGL['%s-%s'            % (dbse, '5'                     )] = """FGG 300 vs. 99"""
TAGL['%s-%s'            % (dbse, '6'                     )] = """FGG 114 vs. 99"""
TAGL['%s-%s'            % (dbse, '7'                     )] = """FGG 412 vs. 99"""
TAGL['%s-%s'            % (dbse, '8'                     )] = """FGG 691 vs. 99"""
TAGL['%s-%s'            % (dbse, '9'                     )] = """FGG 470 vs. 99"""
TAGL['%s-%s'            % (dbse, '10'                    )] = """FGG 224 vs. 99"""
TAGL['%s-%s-reagent'    % (dbse, '114'                   )] = """FGG 114"""
TAGL['%s-%s-reagent'    % (dbse, '215'                   )] = """FGG 215"""
TAGL['%s-%s-reagent'    % (dbse, '224'                   )] = """FGG 224"""
TAGL['%s-%s-reagent'    % (dbse, '300'                   )] = """FGG 300"""
TAGL['%s-%s-reagent'    % (dbse, '357'                   )] = """FGG 357"""
TAGL['%s-%s-reagent'    % (dbse, '366'                   )] = """FGG 366"""
TAGL['%s-%s-reagent'    % (dbse, '412'                   )] = """FGG 412"""
TAGL['%s-%s-reagent'    % (dbse, '444'                   )] = """FGG 444"""
TAGL['%s-%s-reagent'    % (dbse, '470'                   )] = """FGG 470"""
TAGL['%s-%s-reagent'    % (dbse, '691'                   )] = """FGG 691"""
TAGL['%s-%s-reagent'    % (dbse, '99'                    )] = """FGG 99"""

TAGL['dbse'] = 'comformation energies for tripeptides'
TAGL['default'] = 'entire database'

# <<< Geometry Specification Strings >>>
GEOS = {}

GEOS['%s-%s-%s' % (dbse, '114', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                7.830003625384     2.454703174284    -0.833369225059
C                7.053326184342     0.353327713364    -0.391173309722
O                7.688274165340    -1.647892262459    -1.795239827225
H                6.909706998164    -3.171011526399    -1.052577456594
C                5.307219236599    -0.230597662018     1.829254897636
H                4.885810308734     1.524957916395     2.796794678203
H                6.297435730774    -1.504273076281     3.116158394836
N                2.946951295331    -1.421125126388     1.097930883808
H                1.391706687114    -0.340201777785     0.850376760265
C                2.869472523840    -3.873989648218     0.453534272141
O                4.783765097503    -5.211915751034     0.347709608642
C                0.310783338511    -4.994597245633    -0.158736995249
H                0.240863471556    -6.831411047805     0.771008262640
H                0.220076484083    -5.321519866802    -2.190192589215
N               -1.805709931481    -3.426124554479     0.496997973221
H               -2.130742826515    -2.842199179097     2.286568622045
C               -3.568824414429    -2.734484789463    -1.232101439317
O               -3.497014821340    -3.299512903506    -3.475206360281
C               -5.658861518546    -1.056407982541    -0.181413708856
N               -5.617287543600    -1.001605924658     2.585145351204
H               -6.531914992418    -2.534173819268     3.280564568487
H               -6.588606776435     0.521513339283     3.218203606068
H               -7.425755453763    -1.797180627038    -0.954311697630
C               -5.279026565628     1.604326414020    -1.283124044933
H               -5.666420423082     1.483383941449    -3.301351555960
H               -6.698210892203     2.855325114676    -0.453534272141
C               -2.674983953084     2.670131953551    -0.893840461345
C               -0.858957138386     2.450923722017    -2.806243308873
H               -1.352175659340     1.483383941449    -4.541011899813
C                1.552333408497     3.469486108200    -2.501997401312
H                2.937502664662     3.293741577745    -3.994881047110
C                2.187281389495     4.726153987258    -0.274010289419
H                4.059999988211     5.510390332835    -0.052912331750
C                0.401490192939     4.928354683587     1.655400093315
H                0.873921726420     5.903453368691     3.390168684255
C               -2.006020901676     3.904123119002     1.347374733486
H               -3.387410705573     4.102544363064     2.844037831551
""")

GEOS['%s-%s-%s' % (dbse, '215', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                6.411993993433    -4.041868832061     0.654866715923
C                6.209793297103    -1.840337886043     0.074720792809
O                6.529157013736    -1.029645374591    -2.291216326861
H                6.434670707040     0.835514319590    -2.302554683664
C                5.661772718266     0.215684147663     2.026807889149
H                7.377644047866     1.343850649614     2.247905846818
H                5.246032968803    -0.714061110226     3.806929907303
N                3.571735614149     1.888091776184     1.410757169491
H                1.978696483253     1.888091776184     2.480342161291
C                3.781495215014     3.690890507945    -0.358026491859
O                5.642875456927     3.896870656542    -1.762093009363
C                1.559177281523     5.505027596509    -0.535660748448
H                1.961688948048     6.812718081183    -2.062559464656
H                1.396660834006     6.542487244032     1.238792091304
N               -0.814318742682     4.242690539050    -1.030768995535
H               -1.609893445063     4.225683003844    -2.767427312609
C               -2.195708546579     3.182554177920     0.819272889574
O               -1.481392067956     3.067280883751     3.039701096931
C               -4.748728553506     2.150763708799    -0.032993596825
N               -4.852663490872     2.048718497567    -2.791993752350
H               -6.670580031704     2.007144522621    -3.381588306133
H               -4.040081253286     0.415995117859    -3.391036936803
H               -6.139566988072     3.545381595633     0.592505753503
C               -5.308087489147    -0.364461775450     1.325719493465
H               -5.308087489147    -0.016752166809     3.355285361296
H               -7.201593075336    -0.967284412171     0.775809188494
C               -3.397574367753    -2.356233120603     0.673763977262
C               -3.613003147020    -3.792424982383    -1.539105325560
H               -5.287300501674    -3.603452368991    -2.705066350189
C               -1.732725643768    -5.506406585850    -2.228855364441
H               -1.927367435562    -6.587329934453    -3.952285598577
C                0.379988173956    -5.833329207018    -0.694397743697
H                1.865312915218    -7.129681334888    -1.229190239597
C                0.570850513482    -4.484064747399     1.560045534071
H                2.188456084119    -4.782641476558     2.769470259781
C               -1.292419454564    -2.754965334861     2.229008585479
H               -1.146910542252    -1.700498152133     3.975115533222
""")

GEOS['%s-%s-%s' % (dbse, '224', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                6.851125488013    -2.296834431583     3.011712720678
C                6.575225472460    -0.839855582330     1.271274951336
O                6.713175480236    -1.578738500693    -1.138125869414
H                6.280428195568    -0.127428829841    -2.234167027088
C                6.066889142435     1.968277452677     1.664337987192
H                7.555993335965     3.051090527414     0.732703003168
H                6.114132295783     2.336774048792     3.678786045952
N                3.631032155811     2.777080237996     0.693018754356
H                2.217517007638     3.325100816833     1.883546218727
C                3.203954049545     3.030303539941    -1.788191659482
O                4.753529479360     2.421811724818    -3.436032848262
C                0.684949113028     4.235948813383    -2.483610876765
H                0.598021710867     4.302089228070    -4.530184279802
H                0.666051851688     6.159690017715    -1.740948506134
N               -1.524140737526     2.920699424174    -1.548196440474
H               -2.635299704272     1.894578133454    -2.716047191238
C               -2.306487356970     3.071877514887     0.863094106409
O               -1.091393452858     4.130124149883     2.556288722402
C               -4.817933388951     1.798202100624     1.413004411380
N               -6.280581416606     1.497735645331    -0.909469007209
H               -7.006236252032     3.189040535190    -1.446151229243
H               -7.779134240806     0.350671882041    -0.580656659907
H               -5.734450563903     2.990619291129     2.830299011821
C               -4.313376511194    -0.788832976714     2.643216124563
H               -3.442212763456    -0.439233641938     4.478140200600
H               -6.144521134964    -1.678893985791     2.994705185472
C               -2.650417513344    -2.500924854047     1.106868777685
C               -0.112515315487    -2.835406379751     1.773942102959
H                0.624477876742    -1.896212491192     3.436901100810
C                1.467295732471    -4.398209892503     0.358537228652
H                3.408044472008    -4.666551003520     0.929234521096
C                0.528101843912    -5.622752427284    -1.774963576545
H                1.754534104827    -6.826507974592    -2.880453364889
C               -1.996572271007    -5.314727067455    -2.457154710891
H               -2.744903820040    -6.286046300291    -4.093657542866
C               -3.574493592831    -3.776489994443    -1.017183396843
H               -5.539808772109    -3.578068750382    -1.544416988207
""")

GEOS['%s-%s-%s' % (dbse, '300', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O               -2.998740006137    -2.883671006685     0.532545254011
C               -4.843112712844    -3.875777226993    -0.391530825477
O               -5.283418902047    -6.379664354439    -0.304603423316
H               -3.881242110678    -7.112878094400     0.617582930037
C               -6.925590912425    -2.526512767373    -1.823943234989
H               -8.724610191918    -3.119886773425    -1.028368532608
H               -6.861340223872    -3.146342939300    -3.783589235865
N               -6.685595693417     0.168236699598    -1.672765144275
H               -5.324992876994     1.022392912131    -2.721563148602
C               -7.180703940504     1.277505940210     0.608134299368
O               -8.342885512866     0.228707935884     2.306998093763
C               -5.997735380670     3.881548552754     0.891593219456
H               -6.867009402273     4.835860250384     2.482742624217
H               -6.226392242874     5.000266424035    -0.820498657877
N               -3.318103722769     3.554625931585     1.365914479070
H               -2.692604372441     3.070856041301     3.108241974545
C               -1.700498152133     3.016053983418    -0.529480833253
O               -2.280644075246     3.129437551453    -2.783924111021
C                0.941338983089     2.265832708251     0.349241819020
N                0.792050618509     1.207586073255     2.894702921412
H                2.557054827592     1.007275103059     3.609019400035
H                0.038049891075    -0.555528409694     2.781319353377
H                2.044939045299     4.010049929860     0.472074017725
C                2.169660970138     0.544292200249    -1.636860347731
H                1.011258850044    -1.150792141879    -1.823943234989
H                2.148873982665     1.517501159218    -3.449107710161
C                4.811498105360    -0.139788660231    -0.875300715761
C                5.319834435385    -2.407460020936     0.381367163297
H                3.791045993043    -3.730268314681     0.702620606064
C                7.759470874277    -2.989495670184     1.190169948615
H                8.118518839722    -4.758279331534     2.150150824647
C                9.728565505823    -1.298190780325     0.757422663947
H               11.623960818146    -1.747945600198     1.379142562007
C                9.248575067807     0.967590854247    -0.495465762842
H               10.773584057882     2.282840243456    -0.852624002154
C                6.808938628915     1.538288146691    -1.300489095893
H                6.448000937336     3.295733451238    -2.286926137800
""")

GEOS['%s-%s-%s' % (dbse, '357', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O               -7.379227331925     3.060488084404     0.875351789440
C               -6.891677989373     0.879744125859     0.404809982094
O               -7.785518450718    -1.038327900071     1.782420333722
H               -7.192144444666    -2.642705387770     1.039757963091
C               -5.232498443790     0.101176958684    -1.823177129800
H               -4.588101832123     1.800040753079    -2.768040196760
H               -6.372003302545    -1.023210090999    -3.123308709937
N               -3.040416128441    -1.384147782578    -1.099412020508
H               -1.356670143118    -0.518653213242    -0.872644884437
C               -3.250175729307    -3.829453399872    -0.453125682707
O               -5.306197763013    -4.934943188216    -0.332183210136
C               -0.818098194950    -5.216512382171     0.157255858550
H               -0.929592036851    -7.057105636610    -0.759261316402
H               -0.761406410932    -5.526427468134     2.192490904783
N                1.436345082818    -3.869137648685    -0.528714728064
H                2.027829362735    -3.721739010239    -2.339072364360
C                3.114421889740    -3.041437602027     1.226840850349
O                2.868757492330    -3.338124605053     3.507740293992
C                5.336739823232    -1.565561491435     0.119461335871
N                5.170443923446    -1.418162852989    -2.635759367386
H                4.216132225816     0.165427647237    -3.142205971277
H                6.918440597324    -1.274543666811    -3.397318999356
H                7.029934439225    -2.631367030966     0.610790130691
C                5.444454212865     1.019583859769     1.466836069357
H                5.710905597748     0.681322881798     3.479394401983
H                7.080957044841     2.051374328890     0.754409316869
C                3.063399284124     2.506798327165     1.034088784689
C                1.016825881088     2.274362012693     2.700827234808
H                1.207688220614     1.078165369921     4.348668423587
C               -1.239507122814     3.555596331492     2.251072414935
H               -2.802310635567     3.372292896501     3.556873173474
C               -1.500289329296     5.082495047700     0.117571609737
H               -3.267183264512     6.051924554402    -0.218799642101
C                0.527386812402     5.348946432583    -1.541607935845
H                0.362980638751     6.564040336694    -3.178110767821
C                2.793168446973     4.077160744454    -1.078625033035
H                4.386207577869     4.360619664542    -2.335292912092
""")

GEOS['%s-%s-%s' % (dbse, '366', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O               -4.327166404604     3.067485178468     0.704101742763
C               -6.462556935935     3.558813973287     0.050256500426
O               -7.558598093609     5.826485333993     0.424422274943
H               -6.313268571355     6.858275803114     1.282357939743
C               -8.246458406357     1.776802229000    -1.308456589863
H               -8.648970072882     2.555369396175    -3.167947105641
H              -10.007683163171     1.716330992714    -0.250209954867
N               -7.212778211102    -0.719525993910    -1.523885369130
H               -5.782255527723    -0.993536283329    -2.774884069786
C               -7.054041215852    -2.127371963682     0.637961328076
O               -8.269135119964    -1.668168513139     2.550364175604
C               -5.090615762708    -4.221188520066     0.492452415764
H               -5.156756177395    -5.188728300634    -1.321684672800
H               -5.415648657743    -5.549665992213     2.019351131972
N               -2.615074527271    -3.077904209044     0.777801061986
H               -1.983905998542    -2.558229522216     2.508790200658
C               -1.494466929856    -1.857141126531    -1.159168225283
O               -2.254136835692    -1.940289076423    -3.362588897435
C                0.877139368215    -0.413390360215    -0.439182568259
N                0.778873609251     0.321713105880     2.215882649900
H                2.498524391120     0.969889169815     2.758234050336
H               -0.468345639137     1.765463872196     2.419973072364
H                0.975405127179     1.181538496814    -1.748762779067
C                3.171266894796    -2.125482237548    -0.909724375606
H                3.018199077948    -3.769543974059     0.324266789845
H                3.088118944903    -2.773658301483    -2.865590924214
C                5.599564976884    -0.745982159785    -0.416505854652
C                6.890247926353    -1.036999984409     1.868173041259
H                6.170262269329    -2.354139099752     3.260901201959
C                9.087999420103     0.329272010416     2.361391562212
H               10.068767283608     0.074158982337     4.137734128098
C               10.025303582528     2.009238543472     0.566151734987
H               11.733616007593     3.065595452334     0.940317509503
C                8.755407620533     2.313484451033    -1.724196339326
H                9.481062455959     3.604167400501    -3.132042309097
C                6.559545852916     0.947212456208    -2.206076503476
H                5.582557441679     1.179648770681    -3.989977973897
""")

GEOS['%s-%s-%s' % (dbse, '412', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                6.883097611251     0.014607072278     0.980767863505
C                4.896995444500    -1.045529288851     0.604712362855
O                2.799399435848    -0.643017622326     1.999330249689
H                3.271830969328     0.689239302088     3.170960452720
C                4.517160491582    -2.954152684112    -1.500442550333
H                5.841858511461    -4.486720578722    -1.139504858755
H                5.078409153357    -2.035745783026    -3.252218676478
N                2.013273364136    -3.965156165760    -1.734768590940
H                0.664008904516    -2.976829397719    -2.668293301097
C                1.208250031086    -5.722601470306    -0.034015070411
O                2.614206274723    -6.824311806383     1.430522683378
C               -1.639567252734    -6.128892589100    -0.071809593089
H               -2.076093989669    -7.710593363192     1.156512393960
H               -2.287743316669    -6.525735077223    -1.986102166751
N               -2.939698832871    -3.891456846537     0.820141142122
H               -3.183473504147    -3.562644499235     2.687190562436
C               -3.448035162896    -1.929921119527    -0.712426752488
O               -2.985052260085    -1.926141667259    -2.998995374533
C               -4.742497564632     0.294286540099     0.597153458319
N               -4.135895475643     0.264050921956     3.290013199157
H               -2.374670718829     0.980257126712     3.543236501102
H               -5.339651022951     1.397886602309     4.251883801323
H               -6.770173706330    -0.074210056016     0.427078106266
C               -4.183138628992     2.775496953937    -0.806913059184
H               -4.734938660097     2.533612008795    -2.776007690730
H               -5.385004450165     4.240034707726     0.013228082937
C               -1.465712448413     3.580520286988    -0.653845242337
C               -0.577541165470     4.948682007947     1.430522683378
H               -1.887121376277     5.502371765186     2.902619341703
C                1.950912401717     5.685675200176     1.594928857030
H                2.593419287250     6.760929370377     3.212534427666
C                3.628989208639     5.080962837321    -0.340150704106
H                5.588635209515     5.640321772962    -0.219208231535
C                2.757825460901     3.750595639041    -2.441526165026
H                4.042839231968     3.310289449837    -3.970314607369
C                0.240710250518     2.992815459338    -2.588924803472
H               -0.435811705426     1.961024990217    -4.217868730912
""")

GEOS['%s-%s-%s' % (dbse, '444', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                4.895003571008    -5.152057398900     2.153572761160
C                5.480818672523    -3.396501820487     0.811867206076
O                5.340978938613    -3.523113471460    -1.707137730441
H                5.868212529977    -1.880941461082    -2.423343935197
C                6.427571465618    -0.885055788506     1.858775484268
H                8.338084587012    -0.548684536668     1.155797362450
H                6.469145440564    -1.028674974684     3.903459161171
N                4.842091239258     1.240886112155     1.159576814718
H                3.574085003397     1.996776565724     2.397347432436
C                4.868547405133     2.208425892723    -1.183683591345
O                6.134663914860     1.308916252977    -2.933569991356
C                3.213147311818     4.530899311312    -1.544621282924
H                3.594871990870     5.267892503542    -3.419229607774
H                3.702586380503     5.946304185619    -0.127326682483
N                0.542964284587     3.958312292734    -1.346200038862
H               -0.630555644578     4.054688325564    -2.850422041463
C               -0.615437835507     3.659735563575     0.891235703701
O                0.510838940310     3.610602684093     2.937809106737
C               -3.487821559067     3.440527332040     0.749506243657
N               -4.343867497733     3.410291713897    -1.877213082494
H               -6.054069648932     4.247440391224    -2.030280899342
H               -4.563075729268     1.590485446931    -2.453579553340
H               -4.177571597948     5.171516470712     1.635787800466
C               -4.383551746546     1.180414875870     2.353883731356
H               -3.446247584121     1.288129265503     4.183138628992
H               -6.415007340511     1.375056667664     2.656239912783
C               -3.841200346110    -1.289457181165     1.065090508021
C               -5.685573052818    -2.425182587652    -0.454249303651
H               -7.545063568596    -1.576695553521    -0.571412323954
C               -5.177236722793    -4.653169699545    -1.763829514459
H               -6.630436119778    -5.509215638211    -2.918452182285
C               -2.807520150855    -5.777556749228    -1.565408270397
H               -2.406898210464    -7.512325340168    -2.568852847509
C               -0.955588539613    -4.683405317688    -0.042289006456
H                0.873666358023    -5.571576600631     0.156132237605
C               -1.471483774173    -2.449749027393     1.252173395280
H               -0.039071364661    -1.623938706869     2.459708394855
""")

GEOS['%s-%s-%s' % (dbse, '470', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O               -5.256962736172     1.546511009058     3.466217392725
C               -6.184818267928     1.754380883789     1.389408371546
O               -7.741952602279     3.664894005183     0.731783676941
H               -7.919586858867     4.700463926572     2.232226227275
C               -5.767188792331    -0.006843873026    -0.795115039267
H               -4.984842172888     1.077858927845    -2.371146634958
H               -7.588884785431    -0.724939803916    -1.437621924800
N               -4.123127055820    -2.026961110187    -0.043004037967
H               -3.206609880868    -1.941923434161     1.638852221223
C               -3.535422228170    -3.861885186225    -1.722970571023
O               -4.455718855390    -3.986607111064    -3.847022745550
C               -1.600342667035    -5.759170224682    -0.755430790455
H               -1.505856360339    -7.295517571560    -2.110364428476
H               -2.180488590149    -6.481045607840     1.085162463984
N                0.880867746804    -4.632893448865    -0.496538310108
H                2.235801384825    -4.836983871328    -1.825015782254
C                1.544161619810    -3.313864607388     1.568932354268
O                0.104190305762    -2.903794036327     3.356613276958
C                4.276705609460    -2.380339897231     1.576491258804
N                5.418100194349    -2.690254983194    -0.919836964106
H                5.008029623288    -1.157687088584    -1.998870586575
H                7.321054411207    -2.763954302417    -0.770548599526
H                5.270701555903    -3.635118050154     2.880402291210
C                4.386309725228     0.318189022009     2.663083785809
H                3.456564467338     0.304960939071     4.499897587980
H                6.370522165845     0.815186995230     2.942763253629
C                3.150428833643     2.204135703662     0.941543277806
C                0.578511565376     2.776722722240     1.179648770681
H               -0.504301509360     1.922566509708     2.689539951684
C               -0.570441924048     4.469917338234    -0.475751322634
H               -2.547095460129     4.944238597848    -0.245204734296
C                0.816617058250     5.596194114051    -2.414610336038
H               -0.084782307630     6.907664050992    -3.695844654836
C                3.379085695848     5.053842713616    -2.660274733447
H                4.482685758058     5.945793448826    -4.132371391772
C                4.533708363674     3.379545358961    -0.984087652659
H                6.544376970166     3.016717941248    -1.140934921775
""")

GEOS['%s-%s-%s' % (dbse, '691', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                5.989359297265    -2.663032712129     0.465689807813
C                7.937666941338    -1.852340200677    -0.407363666058
O               10.131638982821    -3.154361506949    -0.414922570594
H                9.768811565108    -4.749290363978     0.407108297662
C                8.272148467042     0.700679806250    -1.660252092848
H                8.827727950415     0.396433898689    -3.618008367590
H                9.804716361652     1.683337395889    -0.707830121352
N                6.012036010872     2.191673725914    -1.526081537340
H                4.498365377601     1.626645611872    -2.565430910996
C                5.420551730955     3.268817622249     0.743479549500
O                6.934222364226     3.552276542338     2.466909783636
C                2.646433766358     3.992582731541     0.966467233302
H                1.964242632013     4.854297848609    -0.772080809905
H                2.427225534824     5.296493763947     2.534939924457
N                1.166778203498     1.736249727639     1.448347397452
H                0.977805590106     1.025712701285     3.213351606535
C                0.590411732652     0.109195526333    -0.413032844460
O                1.006151482115     0.519266097394    -2.675035026764
C               -0.586887648781    -2.368235435238     0.473248712349
N               -1.185930833234    -2.269969676274     3.166108453187
H               -1.148136310555    -4.027414980821     3.914440002220
H               -2.966052851388    -1.597227172598     3.406103672195
H                0.923003532222    -3.751514965268     0.212466505868
C               -2.812985034540    -3.069323830922    -1.263409604725
H               -2.155360339935    -2.967278619691    -3.211717248797
H               -3.362895339511    -5.015741748861    -0.862787664333
C               -5.023964611228    -1.340224418385    -0.855228759798
C               -6.985500338238    -2.020525826596     0.781274072178
H               -6.959044172363    -3.872457437839     1.656217272184
C               -8.984830587927    -0.374574363951     1.265043962462
H              -10.489052590528    -0.941492204127     2.529270746055
C               -9.047191550346     1.989473029585     0.112311020770
H              -10.596766980162     3.270707348383     0.477028164617
C               -7.110222263077     2.686781973002    -1.533640441875
H               -7.157465416425     4.512257418370    -2.450157616827
C               -5.114671465656     1.040830510356    -2.011741153757
H               -3.612339189189     1.581292184658    -3.291085746422
""")

GEOS['%s-%s-%s' % (dbse, '99', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
O                2.214299365842     0.377996300464    -2.200049809319
C                4.126702213370     0.461144250356    -0.950940834797
O                6.245085209496    -0.823869520710    -1.532976484044
H                5.836904364569    -1.802747658082    -3.025860129842
C                4.491419357217     1.995601871100     1.439562724614
H                6.163826985737     3.167232074131     1.188229148802
H                4.844798144260     0.699249743230     2.994807332831
N                2.335241838413     3.550846479317     1.972465494379
H                0.808343122205     2.742043693999     2.794496362635
C                1.851471948129     5.501043849524     0.349190745341
O                3.431282996087     6.372207597262    -1.092670294841
C               -0.881072041521     6.394884310869     0.398323624823
H               -1.015242597029     8.139101532478    -0.671261366976
H               -1.534917283858     6.687791861627     2.325844281423
N               -2.460883089479     4.474922558805    -0.756299043003
H               -2.451434458810     4.227368435261    -2.651694355326
C               -3.271575600931     2.464253952313     0.579737333679
O               -3.033470108057     2.280950517322     2.892762121599
C               -4.586824990141     0.444136715151    -1.007632618814
N               -3.549365342618     0.493269594633    -3.562542351876
H               -1.757904967660    -0.198370170382    -3.545534816671
H               -4.592494168542    -0.608440741443    -4.726613650371
H               -6.563478526222     1.037510721202    -1.139913448189
C               -4.550920193596    -2.122111374714     0.358639376011
H               -5.337046265307    -1.853770263697     2.242696331530
H               -5.805698346520    -3.390117610575    -0.676930545378
C               -1.973333746927    -3.299410756147     0.538163358733
C               -1.041698762904    -4.799853306481    -1.427151820545
H               -2.217108418203    -5.149452641256    -3.065544378655
C                1.348804796506    -5.897784190289    -1.285422360501
H                2.023437026316    -7.069414393320    -2.819879981245
C                2.847357620706    -5.519838963505     0.846188718562
H                4.695509779681    -6.381554080573     0.974690095669
C                1.930840445754    -4.045852579046     2.830401159180
H                3.060896673839    -3.790739550967     4.516036870637
C               -0.455883661389    -2.944142242970     2.675443616198
H               -1.175869318413    -1.814086014885     4.221239593746
""")

