import numpy as np

# slope for linearization of secondaries on the [300,500] ilvl range
LINEARIZATION_SLOPE = -0.00263604654

POINTS_PER_PCT = np.array([72, 68, 85, 72]) # crit, haste, vers, mastery

# stats on a main piece (pants, in this case) at the given ilvl
BASE=470
STATS_AT_BASE = {
    'stamina': 1377,
    'primary': 725,
    'secondaries': 165 + 165,
    #'wdps': 186.9,
    'armor': 513
}

# total stats at the given avg ilvl. azerite honestly fucks with this, with the
# frankly INSANE stat budget on it plus Heart of Darkness adding passive stats.
TOTAL_BASE=473
TOTAL_AT_BASE = {
    'stamina': 39665,
    'primary': 12324,
    'armor': 4696,
    'secondaries': 1613 + 1287 + 826 + 1940
}

# Secondary stat linearization multipliers
MULT = np.array([
    1, 1, 1, 1, 1,                                                   #    5
    1, 1, 1, 1, 1,                                                   #   10
    1, 1, 1, 1, 1,                                                   #   15
    1, 1, 1, 1, 1,                                                   #   20
    1, 1, 1, 1, 1,                                                   #   25
    1, 1, 1, 1, 1,                                                   #   30
    1, 1, 1, 1, 1,                                                   #   35
    1, 1, 1, 1, 1,                                                   #   40
    1, 1, 1, 1, 1,                                                   #   45
    1, 1, 1, 1, 1,                                                   #   50
    1, 1, 1, 1, 1,                                                   #   55
    1, 1, 1, 1, 1,                                                   #   60
    1, 1, 1, 1, 1,                                                   #   65
    1, 1, 1, 1, 1,                                                   #   70
    1, 1, 1, 1, 1,                                                   #   75
    1, 1, 1, 1, 1,                                                   #   80
    1, 1, 1, 1, 1,                                                   #   85
    1, 1, 1, 1, 1,                                                   #   90
    1, 1, 1, 1, 1,                                                   #   95
    1, 1, 1, 1, 1,                                                   #  100
    1, 1, 1, 1, 1,                                                   #  105
    1, 1, 1, 1, 1,                                                   #  110
    1, 1, 1, 1, 1,                                                   #  115
    1, 1, 1, 1, 1,                                                   #  120
    1, 1, 1, 1, 1,                                                   #  125
    1, 1, 1, 1, 1,                                                   #  130
    1, 1, 1, 1, 1,                                                   #  135
    1, 1, 1, 1, 1,                                                   #  140
    1, 1, 1, 1, 1,                                                   #  145
    1, 1, 1, 1, 1,                                                   #  150
    1, 1, 1, 1, 1,                                                   #  155
    1, 1, 1, 1, 1,                                                   #  160
    0.994435486, 0.992604783, 0.994487319, 0.99265652, 0.994539154,  #  165
    0.99270826, 0.994590992, 0.992760002, 0.994642833, 0.992811747,  #  170
    0.994694676, 0.992863495, 0.994746522, 0.992915246, 0.994798371, #  175
    0.992966999, 0.994850222, 0.993018755, 0.994902077, 0.993070514, #  180
    0.994953934, 0.993122276, 0.995005793, 0.99317404, 0.995057655,  #  185
    0.993225807, 0.99510952, 0.993277576, 0.995161388, 0.993329348,  #  190
    0.995213259, 0.993381123, 0.995265132, 0.993432901, 0.991604043, #  195
    0.986086249, 0.980599158, 0.9751426, 0.969716406, 0.964320406,   #  200
    0.958954431, 0.953618316, 0.948311894, 0.943034999, 0.937787468, #  205
    0.932569136, 0.927379842, 0.922219425, 0.917087722, 0.911984574, #  210
    0.906909824, 0.901863311, 0.89684488, 0.891854375, 0.886891639,  #  215
    0.881956518, 0.877048859, 0.872168508, 0.867315314, 0.862489126, #  220
    0.857689793, 0.852917167, 0.848171097, 0.843451437, 0.83875804,  #  225
    0.83409076, 0.82944945, 0.824833967, 0.820244167, 0.815679907,   #  230
    0.811141045, 0.806627439, 0.80213895, 0.797675436, 0.79323676,   #  235
    0.788822783, 0.784433368, 0.780068378, 0.775727676, 0.771411129, #  240
    0.767118601, 0.762849959, 0.75860507, 0.754383801, 0.750186022,  #  245
    0.746011602, 0.74186041, 0.737732317, 0.733627196, 0.729544917,  #  250
    0.725485354, 0.721448381, 0.717433871, 0.7134417, 0.709471744,   #  255
    0.705523879, 0.701597981, 0.69769393, 0.693811602, 0.689950878,  #  260
    0.686111637, 0.682293759, 0.678497126, 0.674721619, 0.670967121, #  265
    0.674618275, 0.678289297, 0.681980296, 0.685691379, 0.689422657, #  270
    0.693174239, 0.696946235, 0.700738758, 0.704551918, 0.708385827, #  275
    0.7122406, 0.716116349, 0.720013188, 0.723931232, 0.727870597,   #  280
    0.731831398, 0.735813753, 0.739817778, 0.743843591, 0.747891312, #  285
    0.751961058, 0.756052951, 0.76016711, 0.764303657, 0.768462714,  #  290
    0.772644402, 0.776848846, 0.781076169, 0.785326495, 0.78959995,  #  295
    0.793896659, 0.79821675, 0.802560349, 0.806927584, 0.811318584,  #  300
    0.808817976, 0.806293968, 0.803747209, 0.801178339, 0.798587986, #  305
    0.79597677, 0.793345301, 0.790694179, 0.788023995, 0.785335331,  #  310
    0.782628758, 0.779904841, 0.777164134, 0.774407182, 0.771634523, #  315
    0.768846685, 0.766044188, 0.763227544, 0.760397257, 0.757553821, #  320
    0.754697723, 0.751829445, 0.748949456, 0.74605822, 0.743156195,  #  325
    0.740243829, 0.737321564, 0.734389832, 0.731449063, 0.728499674, #  330
    0.725542079, 0.722576685, 0.719603889, 0.716624085, 0.713637657, #  335
    0.710644986, 0.707646443, 0.704642396, 0.701633203, 0.69861922,  #  340
    0.695600793, 0.692578265, 0.68955197, 0.68652224, 0.683489397,   #  345
    0.68045376, 0.677415642, 0.67437535, 0.671333185, 0.668289445,   #  350
    0.665244419, 0.662198393, 0.659151648, 0.656104459, 0.653057097, #  355
    0.650009826, 0.646962908, 0.643916597, 0.640871144, 0.637826796, #  360
    0.634783795, 0.631742376, 0.628702772, 0.625665211, 0.622629917, #  365
    0.61959711, 0.616567003, 0.613539807, 0.61051573, 0.607494974,   #  370
    0.604477737, 0.601464214, 0.598454595, 0.595449068, 0.592447815, #  375
    0.589451015, 0.586458845, 0.583471475, 0.580489074, 0.577511808, #  380
    0.574539836, 0.571573318, 0.568612407, 0.565657255, 0.56270801,  #  385
    0.559764816, 0.556827814, 0.553897144, 0.550972939, 0.548055333, #  390
    0.545144454, 0.542240429, 0.53934338, 0.536453429, 0.533570692,  #  395
    0.530695284, 0.527827318, 0.524966903, 0.522114145, 0.519269148, #  400
    0.516432015, 0.513602842, 0.510781728, 0.507968765, 0.505164046, #  405
    0.502367659, 0.499579691, 0.496800226, 0.494029347, 0.491267133, #  410
    0.488513662, 0.485769009, 0.483033248, 0.480306449, 0.477588682, #  415
    0.474880013, 0.472180509, 0.469490231, 0.466809241, 0.464137598, #  420
    0.461475359, 0.458822579, 0.456179312, 0.45354561, 0.450921523,  #  425
    0.448307099, 0.445702384, 0.443107422, 0.440522259, 0.437946933, #  430
    0.435381487, 0.432825957, 0.430280381, 0.427744793, 0.425219228, #  435
    0.422703717, 0.420198292, 0.417702981, 0.415217812, 0.412742813, #  440
    0.410278008, 0.40782342, 0.405379073, 0.402944988, 0.400521184,  #  445
    0.39810768, 0.395704493, 0.39331164, 0.390929136, 0.388556995,   #  450
    0.386195229, 0.38384385, 0.381502868, 0.379172293, 0.376852134,  #  455
    0.374542396, 0.372243087, 0.369954212, 0.367675775, 0.36540778,  #  460
    0.363150228, 0.360903121, 0.358666459, 0.356440243, 0.35422447,  #  465
    0.352019138, 0.349824245, 0.347639786, 0.345465756, 0.343302151, #  470
    0.341148963, 0.339006186, 0.336873811, 0.33475183, 0.332640234,  #  475
    0.330539013, 0.328448155, 0.326367649, 0.324297483, 0.322237645, #  480
    0.32018812, 0.318148894, 0.316119953, 0.314101282, 0.312092864,  #  485
    0.310094683, 0.308106722, 0.306128963, 0.304161387, 0.302203977, #  490
    0.300256712, 0.298319573, 0.296392539, 0.294475591, 0.292568705, #  495
    0.290671862, 0.288785037, 0.28690821, 0.285041356, 0.283184451,  #  500
    0.281608668, 0.280041652, 0.278483357, 0.276933732, 0.275392731, #  505
    0.273860304, 0.272336404, 0.270820985, 0.269313998, 0.267815396, #  510
    0.266325134, 0.264843164, 0.26336944, 0.261903917, 0.260446549,  #  515
    0.258997291, 0.257556097, 0.256122922, 0.254697723, 0.253280454, #  520
    0.251871071, 0.250469531, 0.24907579, 0.247689804, 0.246311531,  #  525
    0.244940927, 0.24357795, 0.242222557, 0.240874706, 0.239534356,  #  530
    0.238201463, 0.236875988, 0.235557888, 0.234247123, 0.232943652, #  535
    0.231647434, 0.230358428, 0.229076596, 0.227801896, 0.226534289, #  540
    0.225273736, 0.224020197, 0.222773633, 0.221534006, 0.220301277, #  545
    0.219075408, 0.21785636, 0.216644095, 0.215438576, 0.214239765,  #  550
    0.213047625, 0.211862118, 0.210683209, 0.209510859, 0.208345033, #  555
    0.207185694, 0.206032806, 0.204886334, 0.203746241, 0.202612492, #  560
    0.201485052, 0.200363886, 0.199248958, 0.198140235, 0.197037681, #  565
    0.195941262, 0.194850944, 0.193766693, 0.192688476, 0.191616258, #  570
    0.190550007, 0.189489689, 0.188435271, 0.18738672, 0.186344004,  #  575
    0.18530709, 0.184275946, 0.18325054, 0.18223084, 0.181216814,    #  580
    0.180208431, 0.179205658, 0.178208466, 0.177216822, 0.176230697, #  585
    0.175250059, 0.174274877, 0.173305122, 0.172340764, 0.171381771, #  590
    0.170428115, 0.169479765, 0.168536693, 0.167598868, 0.166666262, #  595
    0.165738845, 0.164816589, 0.163899465, 0.162987444, 0.162080498, #  600
    0.161178599, 0.160281718, 0.159389828, 0.158502901, 0.15762091,  #  605
    0.156743826, 0.155871623, 0.155004273, 0.15414175, 0.153284026,  #  610
    0.152431075, 0.15158287, 0.150739385, 0.149900594, 0.14906647,   #  615
    0.148236987, 0.14741212, 0.146591844, 0.145776131, 0.144964958,  #  620
    0.144158298, 0.143356128, 0.14255842, 0.141765152, 0.140976298,  #  625
    0.140191833, 0.139411734, 0.138635975, 0.137864534, 0.137097385, #  630
    0.136334504, 0.135575869, 0.134821455, 0.134071239, 0.133325198, #  635
    0.132583308, 0.131845547, 0.13111189, 0.130382316, 0.129656802,  #  640
    0.128935325, 0.128217863, 0.127504392, 0.126794893, 0.126089341, #  645
    0.125387715, 0.124689993, 0.123996154, 0.123306176, 0.122620037, #  650
    0.121937716, 0.121259192, 0.120584443, 0.119913449, 0.119246189, #  655
    0.118582642, 0.117922787, 0.117266604, 0.116614073, 0.115965172, #  660
    0.115319882, 0.114678183, 0.114040055, 0.113405477, 0.112774431, #  665
    0.112146896, 0.111522853, 0.110902283, 0.110285166, 0.109671482, #  670
    0.109061214, 0.108454341, 0.107850845, 0.107250708, 0.10665391,  #  675
    0.106060433, 0.105470258, 0.104883367, 0.104299742, 0.103719365, #  680
    0.103142217, 0.102568281, 0.101997538, 0.101429971, 0.100865563, #  685
    0.100304295, 0.09974615, 0.099191112, 0.098639161, 0.098090282,  #  690
    0.097544458, 0.09700167, 0.096461903, 0.095925139, 0.095391363,  #  695
    0.094860556, 0.094332703, 0.093807788, 0.093285793, 0.092766703, #  700
    0.092250501, 0.091737172, 0.091226699, 0.090719067, 0.090214259, #  705
    0.089712261, 0.089213056, 0.088716629, 0.088222964, 0.087732046, #  710
    0.08724386, 0.08675839, 0.086275622, 0.08579554, 0.085318129,    #  715
    0.084843375, 0.084371263, 0.083901778, 0.083434906, 0.082970631, #  720
    0.08250894, 0.082049817, 0.08159325, 0.081139223, 0.080687723,   #  725
    0.080238735, 0.079792246, 0.07934824, 0.078906706, 0.078467629,  #  730
    0.078030994, 0.07759679, 0.077165001, 0.076735616, 0.076308619,  #  735
    0.075883999, 0.075461741, 0.075041833, 0.074624262, 0.074209014, #  740
    0.073796077, 0.073385438, 0.072977084, 0.072571002, 0.072167179, #  745
    0.071765604, 0.071366263, 0.070969145, 0.070574236, 0.070181525, #  750
    0.069790999, 0.069402646, 0.069016454, 0.068632411, 0.068250505, #  755
    0.067870724, 0.067493056, 0.06711749, 0.066744014, 0.066372616,  #  760
    0.066003285, 0.065636008, 0.065270776, 0.064907576, 0.064546397, #  765
    0.064187227, 0.063830057, 0.063474873, 0.063121667, 0.062770425, #  770
    0.062421138, 0.062073795, 0.061728385, 0.061384896, 0.061043319, #  775
    0.060703643, 0.060365856, 0.06002995, 0.059695912, 0.059363734,  #  780
    0.059033403, 0.058704911, 0.058378247, 0.0580534, 0.057730361,   #  785
    0.05740912, 0.057089666, 0.05677199, 0.056456081, 0.056141931,   #  790
    0.055829528, 0.055518864, 0.055209928, 0.054902712, 0.054597205, #  795
    0.054293398, 0.053991282, 0.053690847, 0.053392083, 0.053094982, #  800
    0.052799534, 0.052505731, 0.052213562, 0.051923019, 0.051634092, #  805
    0.051346774, 0.051061054, 0.050776924, 0.050494375, 0.050213398, #  810
    0.049933985, 0.049656127, 0.049379815, 0.04910504, 0.048831794,  #  815
    0.048560069, 0.048289856, 0.048021146, 0.047753932, 0.047488205, #  820
    0.047223956, 0.046961177, 0.046699861, 0.046439999, 0.046181583, #  825
    0.045924605, 0.045669057, 0.045414931, 0.045162219, 0.044910913, #  830
    0.044661006, 0.044412489, 0.044165355, 0.043919596, 0.043675205, #  835
    0.043432174, 0.043190495, 0.042950161, 0.042711164, 0.042473497, #  840
    0.042237153, 0.042002124, 0.041768402, 0.041535981, 0.041304854, #  845
    0.041075012, 0.04084645, 0.040619159, 0.040393133, 0.040168365,  #  850
    0.039944848, 0.039722574, 0.039501537, 0.039281731, 0.039063147, #  855
    0.038845779, 0.038629621, 0.038414666, 0.038200907, 0.037988338, #  860
    0.037776951, 0.037566741, 0.0373577, 0.037149823, 0.036943102,   #  865
    0.036737532, 0.036533105, 0.036329816, 0.036127659, 0.035926626, #  870
    0.035726711, 0.03552791, 0.035330214, 0.035133619, 0.034938117,  #  875
    0.034743704, 0.034550372, 0.034358116, 0.034166929, 0.033976807, #  880
    0.033787743, 0.03359973, 0.033412764, 0.033226838, 0.033041947,  #  885
    0.032858085, 0.032675246, 0.032493424, 0.032312614, 0.03213281,  #  890
    0.031954006, 0.031776198, 0.031599379, 0.031423543, 0.031248687, #  895
    0.031074803, 0.030901887, 0.030729933, 0.030558936, 0.03038889,  #  900
    0.030219791, 0.030051632, 0.029884409, 0.029718117, 0.02955275,  #  905
    0.029388304, 0.029224772, 0.02906215, 0.028900434, 0.028739617,  #  910
    0.028579695, 0.028420663, 0.028262515, 0.028105248, 0.027948856, #  915
    0.027793334, 0.027638678, 0.027484882, 0.027331942, 0.027179853, #  920
    0.027028611, 0.02687821, 0.026728645, 0.026579913, 0.026432009,  #  925
    0.026284928, 0.026138665, 0.025993216, 0.025848576, 0.025704742, #  930
    0.025561707, 0.025419469, 0.025278022, 0.025137362, 0.024997485, #  935
    0.024858386, 0.024720061, 0.024582506, 0.024445716, 0.024309688, #  940
    0.024174416, 0.024039897, 0.023906127, 0.023773101, 0.023640815, #  945
    0.023509266, 0.023378448, 0.023248358, 0.023118992, 0.022990346, #  950
    0.022862416, 0.022735198, 0.022608688, 0.022482881, 0.022357775, #  955
    0.022233365, 0.022109647, 0.021986618, 0.021864273, 0.021742609, #  960
    0.021621622, 0.021501308, 0.021381664, 0.021262685, 0.021144369, #  965
    0.02102671, 0.020909707, 0.020793355, 0.02067765, 0.020562589,   #  970
    0.020448168, 0.020334384, 0.020221233, 0.020108711, 0.019996816, #  975
    0.019885544, 0.01977489, 0.019664853, 0.019555427, 0.019446611,  #  980
    0.0193384, 0.019230791, 0.019123781, 0.019017367, 0.018911544,   #  985
    0.018806311, 0.018701663, 0.018597597, 0.01849411, 0.0183912,    #  990
    0.018288862, 0.018187093, 0.018085891, 0.017985251, 0.017885172, #  995
    0.01778565, 0.017686681, 0.017588264, 0.017490394, 0.017393068,  # 1000
    0.017296284, 0.017200039, 0.017104329, 0.017009151, 0.016914504, # 1005
    0.016820383, 0.016726786, 0.016633709, 0.016541151, 0.016449107, # 1010
    0.016357576, 0.016266554, 0.016176038, 0.016086027, 0.015996516, # 1015
    0.015907503, 0.015818985, 0.01573096, 0.015643425, 0.015556377,  # 1020
    0.015469814, 0.015383732, 0.015298129, 0.015213002, 0.015128349, # 1025
    0.015044167, 0.014960454, 0.014877206, 0.014794422, 0.014712098, # 1030
    0.014630232, 0.014548822, 0.014467865, 0.014387358, 0.0143073,   # 1035
    0.014227686, 0.014148516, 0.014069787, 0.013991495, 0.013913639, # 1040
    0.013836217, 0.013759225, 0.013682661, 0.013606524, 0.01353081,  # 1045
    0.013455518, 0.013380645, 0.013306188, 0.013232145, 0.013158515, # 1050
    0.013085294, 0.013012481, 0.012940073, 0.012868067, 0.012796463, # 1055
    0.012725257, 0.012654447, 0.012584031, 0.012514007, 0.012444373, # 1060
    0.012375126, 0.012306264, 0.012237786, 0.012169689, 0.01210197,  # 1065
    0.012034629, 0.011967662, 0.011901067, 0.011834844, 0.011768989, # 1070
    0.0117035, 0.011638376, 0.011573614, 0.011509212, 0.011445169,   # 1075
    0.011381482, 0.01131815, 0.01125517, 0.01119254, 0.011130259,    # 1080
    0.011068325, 0.011006735, 0.010945488, 0.010884581, 0.010824014, # 1085
    0.010763784, 0.010703888, 0.010644327, 0.010585096, 0.010526195, # 1090
    0.010467622, 0.010409375, 0.010351452, 0.010293851, 0.010236571, # 1095
    0.010179609, 0.010122964, 0.010066635, 0.010010619, 0.009954915, # 1100
    0.009899521, 0.009844435, 0.009789655, 0.00973518, 0.009681009,  # 1105
    0.009627139, 0.009573568, 0.009520296, 0.00946732, 0.009414639,  # 1110
    0.009362251, 0.009310155, 0.009258349, 0.00920683, 0.009155599,  # 1115
    0.009104652, 0.009053989, 0.009003608, 0.008953508, 0.008903686, # 1120
    0.008854141, 0.008804872, 0.008755877, 0.008707155, 0.008658704, # 1125
    0.008610522, 0.008562609, 0.008514962, 0.008467581, 0.008420463, # 1130
    0.008373607, 0.008327012, 0.008280676, 0.008234598, 0.008188777, # 1135
    0.00814321, 0.008097897, 0.008052836, 0.008008026, 0.007963465,  # 1140
    0.007919153, 0.007875086, 0.007831265, 0.007787688, 0.007744353, # 1145
    0.00770126, 0.007658406, 0.007615791, 0.007573413, 0.00753127,   # 1150
    0.007489362, 0.007447688, 0.007406245, 0.007365033, 0.00732405,  # 1155
    0.007283295, 0.007242767, 0.007202465, 0.007162387, 0.007122531, # 1160
    0.007082898, 0.007043485, 0.007004291, 0.006965316, 0.006926557, # 1165
    0.006888014, 0.006849686, 0.006811571, 0.006773668, 0.006735976, # 1170
    0.006698493, 0.006661219, 0.006624153, 0.006587293, 0.006550638, # 1175
    0.006514186, 0.006477938, 0.006441892, 0.006406046, 0.006370399, # 1180
    0.006334951, 0.0062997, 0.006264645, 0.006229785, 0.00619512,    # 1185
    0.006160647, 0.006126366, 0.006092276, 0.006058375, 0.006024663, # 1190
    0.005991139, 0.005957801, 0.005924649, 0.005891681, 0.005858897, # 1195
    0.005826295, 0.005793874, 0.005761634, 0.005729574, 0.005697691, # 1200
    0.005665986, 0.005634458, 0.005603105, 0.005571926, 0.005540921, # 1205
    0.005510089, 0.005479428, 0.005448937, 0.005418617, 0.005388465, # 1210
    0.005358481, 0.005328663, 0.005299012, 0.005269525, 0.005240203, # 1215
    0.005211044, 0.005182047, 0.005153211, 0.005124536, 0.005096021, # 1220
    0.005067664, 0.005039465, 0.005011423, 0.004983536, 0.004955805, # 1225
    0.004928229, 0.004900806, 0.004873535, 0.004846416, 0.004819448, # 1230
    0.00479263, 0.004765962, 0.004739441, 0.004713069, 0.004686843,  # 1235
    0.004660763, 0.004634828, 0.004609037, 0.00458339, 0.004557886,  # 1240
    0.004532524, 0.004507302, 0.004482221, 0.00445728, 0.004432477,  # 1245
    0.004407813, 0.004383285, 0.004358895, 0.004334639, 0.004310519, # 1250
    0.004286533, 0.004262681, 0.004238961, 0.004215373, 0.004191917, # 1255
    0.004168591, 0.004145395, 0.004122328, 0.004099389, 0.004076578, # 1260
    0.004053894, 0.004031336, 0.004008903, 0.003986596, 0.003964412, # 1265
    0.003942352, 0.003920415, 0.0038986, 0.003876906, 0.003855333,   # 1270
    0.00383388, 0.003812546, 0.003791331, 0.003770234, 0.003749255,  # 1275
    0.003728392, 0.003707645, 0.003687014, 0.003666497, 0.003646095, # 1280
    0.003625806, 0.003605631, 0.003585567, 0.003565615, 0.003545774, # 1285
    0.003526044, 0.003506423, 0.003486911, 0.003467508, 0.003448213, # 1290
    0.003429026, 0.003409945, 0.00339097, 0.003372101, 0.003353337,  # 1295
    0.003334677, 0.003316121, 0.003297669, 0.003279319, 0.003261071, # 1300
])

SCALARS = {
    'main': 1,
    'bracers': 0.563,
    'off': 0.75,
    'ring': 1.765,
}