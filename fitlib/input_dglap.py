conf={}

#--setups
conf['bootstrap']=True
conf['flat par']=True
conf['ftol']=1e-8
conf['ncpus']=4
conf['Q20']   = 1.27**2
conf['order'] = 'LO'
conf['version'] = 'JAM20+' #DGLAP/CT3 evolution

#--datasets

conf['datasets']={}

conf['datasets']['sidis']={}
conf['datasets']['sidis']['filters']=["z>0.2 and z<0.6 and Q2>1.63 and pT>0.2 and pT<0.9"]
conf['datasets']['sidis']['xlsx']={}

#--Unpol multiplicities (HERMES only)
conf['datasets']['sidis']['xlsx'][1010]='sidis/expdata/1010.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1011]='sidis/expdata/1011.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1012]='sidis/expdata/1012.xlsx'  # |  proton | k+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1013]='sidis/expdata/1013.xlsx'  # |  proton | k-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1014]='sidis/expdata/1014.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1015]='sidis/expdata/1015.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1016]='sidis/expdata/1016.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1017]='sidis/expdata/1017.xlsx'  # |  deuteron | k-   | M_Hermes | hermes

#--Collins effect SIDIS
conf["datasets"]["sidis"]["xlsx"][4001]="sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+  pT
conf["datasets"]["sidis"]["xlsx"][4000]="sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+   x
conf["datasets"]["sidis"]["xlsx"][4002]="sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+   z
conf["datasets"]["sidis"]["xlsx"][4004]="sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
conf["datasets"]["sidis"]["xlsx"][3027]="sidis/expdata/3027.xlsx"  #  compass    proton   pi+ pt
conf["datasets"]["sidis"]["xlsx"][3025]="sidis/expdata/3025.xlsx"  #  compass    proton  pi+   x
conf["datasets"]["sidis"]["xlsx"][3010]="sidis/expdata/3010.xlsx"  #  compass    proton  pi+  z
conf["datasets"]["sidis"]["xlsx"][3012]="sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3026]="sidis/expdata/3026.xlsx"  #   HERMES    proton pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="sidis/expdata/3000.xlsx"  #   HERMES    proton pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="sidis/expdata/3003.xlsx"  #   HERMES    proton pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3006]="sidis/expdata/3006.xlsx"  #   HERMES    proton  pi0    z
conf["datasets"]["sidis"]["xlsx"][3014]="sidis/expdata/3014.xlsx"  #   HERMES    proton  pi0    x
conf["datasets"]["sidis"]["xlsx"][3015]="sidis/expdata/3015.xlsx"  #   HERMES    proton  pi0   pT

#--Sivers effect SIDIS
conf['datasets']['sidis']['xlsx'][2000]='sidis/expdata/2000.xlsx' # proton   | pi+    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2001]='sidis/expdata/2001.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2002]='sidis/expdata/2002.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2003]='sidis/expdata/2003.xlsx' # proton   | pi-    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2004]='sidis/expdata/2004.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2005]='sidis/expdata/2005.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2006]='sidis/expdata/2006.xlsx' # proton   | pi0    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2007]='sidis/expdata/2007.xlsx' # proton   | pi0    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2008]='sidis/expdata/2008.xlsx' # proton   | pi0    | AUTsivers  | hermes     | z

conf['datasets']['sidis']['xlsx'][2026]='sidis/expdata/2026.xlsx' # deuteron | pi+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2027]='sidis/expdata/2027.xlsx' # deuteron | pi+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2028]='sidis/expdata/2028.xlsx' # deuteron | pi+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2029]='sidis/expdata/2029.xlsx' # deuteron | pi-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2030]='sidis/expdata/2030.xlsx' # deuteron | pi-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2031]='sidis/expdata/2031.xlsx' # deuteron | pi-    | AUTsivers  | compass    | z

conf['datasets']['sidis']['xlsx'][2512]='sidis/expdata/2512.xlsx' # proton   | pi+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2513]='sidis/expdata/2513.xlsx' # proton   | pi+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2514]='sidis/expdata/2514.xlsx' # proton   | pi+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2515]='sidis/expdata/2515.xlsx' # proton   | pi-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2516]='sidis/expdata/2516.xlsx' # proton   | pi-    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2517]='sidis/expdata/2517.xlsx' # proton   | pi-    | AUTsivers  | compass    | PT

#A_{UT}^{\sin\phi_S}
conf["datasets"]["sidis"]["xlsx"][9011]="sidis/expdata/9011.xlsx"  #   COMPASS    proton  h+    z
conf["datasets"]["sidis"]["xlsx"][9022]="sidis/expdata/9022.xlsx"  #   COMPASS    proton  h-    z
conf["datasets"]["sidis"]["xlsx"][9033]="sidis/expdata/9033.xlsx"  #   COMPASS    proton  h+    x
conf["datasets"]["sidis"]["xlsx"][9044]="sidis/expdata/9044.xlsx"  #   COMPASS    proton  h-    x

conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}
#for k in [9011,9022,9033,9044]: conf['datasets']['sidis']['norm'][k]={'value':1.00000e+00,'fixed':True,'min':8.00000e-01,'max':1.20000e+00}

#Sivers effect DY
conf['datasets']['dy']={}
conf['datasets']['dy']['filters']=[]
conf['datasets']['dy']['xlsx']={}
conf['datasets']['dy']['xlsx'][1000]='dy/expdata/1000.xlsx'       # proton-pi- |    | AUTsivers  | compass    | xbeam
conf['datasets']['dy']['xlsx'][1001]='dy/expdata/1001.xlsx'       # proton-pi- |    | AUTsivers  | compass    | xtarget
conf['datasets']['dy']['xlsx'][1002]='dy/expdata/1002.xlsx'       # proton-pi- |    | AUTsivers  | compass    | xF
conf['datasets']['dy']['xlsx'][1003]='dy/expdata/1003.xlsx'       # proton-pi- |    | AUTsivers  | compass    | qT

conf['datasets']['dy']['norm']={}
for k in conf['datasets']['dy']['xlsx']: conf['datasets']['dy']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}

#Sivers effect WZ
conf['datasets']['wz']={}
conf['datasets']['wz']['filters']=[]
conf['datasets']['wz']['xlsx']={}
conf['datasets']['wz']['xlsx'][2000]='wz/expdata/2000.xlsx'       # proton-proton |W+/-| AUTsivers  | star    | pT
conf['datasets']['wz']['xlsx'][2001]='wz/expdata/2001.xlsx'       # proton-proton |W+/-| AUTsivers  | star    | y
conf['datasets']['wz']['xlsx'][2002]='wz/expdata/2002.xlsx'       # proton-proton |Z   | AUTsivers  | star    | y

conf['datasets']['wz']['norm']={}
for k in conf['datasets']['wz']['xlsx']: conf['datasets']['wz']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}

#--Collins effect SIA
conf['datasets']['sia']={}
conf['datasets']['sia']['filters']=[]
#conf['datasets']['sia']['filters'].append("pT/z1<3.5")
#conf['datasets']['sia']['filters'].append("z2<0.7")
conf['datasets']['sia']['xlsx']={}

conf['datasets']['sia']['xlsx'][1000]='sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001]='sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1002]='sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003]='sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1004]='sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005]='sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][2008]='sia/expdata/2008.xlsx' # babar | pi,pi | AUL-0     | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2009]='sia/expdata/2009.xlsx' # babar | pi,pi | AUC-0     | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][3000]='sia/expdata/3000.xlsx' # bes3 | pi,pi | AUL-0     | 6     | z1,z2        |
conf['datasets']['sia']['xlsx'][3001]='sia/expdata/3001.xlsx' # bes3 | pi,pi | AUC-0     | 6     | z1,z2        |
conf['datasets']['sia']['xlsx'][3002]='sia/expdata/3002.xlsx' # bes3 | pi,pi | AUL-0     | 5     | z1,z2,pT     |
conf['datasets']['sia']['xlsx'][3003]='sia/expdata/3003.xlsx' # bes3 | pi,pi | AUC-0     | 5     | z1,z2.pT     |

conf['datasets']['sia']['norm']={}
for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}


#--AN
conf['datasets']['AN']={}
conf['datasets']['AN']['filters']=[]
conf['datasets']['AN']['xlsx']={}
conf['datasets']['AN']['xlsx'][1000]='AN_pp/expdata/1000.xlsx' # BRAHMS pim 2.3
conf['datasets']['AN']['xlsx'][1001]='AN_pp/expdata/1001.xlsx' # BRAHMS pim 4
conf['datasets']['AN']['xlsx'][1002]='AN_pp/expdata/1002.xlsx' # BRAHMS pip 2.3
conf['datasets']['AN']['xlsx'][1003]='AN_pp/expdata/1003.xlsx' # BRAHMS pip 4
conf['datasets']['AN']['xlsx'][2000]='AN_pp/expdata/2000.xlsx' # STAR piz 04
conf['datasets']['AN']['xlsx'][2001]='AN_pp/expdata/2001.xlsx' # STAR piz 3.3
conf['datasets']['AN']['xlsx'][2002]='AN_pp/expdata/2002.xlsx' # STAR piz 3.68
conf['datasets']['AN']['xlsx'][2003]='AN_pp/expdata/2003.xlsx' # STAR piz 3.7

conf['datasets']['AN']['norm']={}
for k in conf['datasets']['AN']['xlsx']: conf['datasets']['AN']['norm'][k]={'value':1.000000,'fixed':False,'min':0.8000000,'max':1.2000000}



#--parameters
conf['params']={}


#--Parameters in gaussian approximation, parton model:
#--TMD PDF:
conf['params']['pdf']={}
conf['params']['pdf']['widths1_uv']  ={'value':    5.13614347e-01,'min': 0.1,'max':0.8,'fixed':False}
conf['params']['pdf']['widths2_uv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['widths1_dv']  ={'value':    5.89567437e-01,'min': 0.1,'max':0.8,'fixed':'widths1_uv'}
conf['params']['pdf']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}
conf['params']['pdf']['widths1_sea'] ={'value':    5.43879e-01,'min': 0.1,'max':0.8,'fixed':False}
conf['params']['pdf']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}

conf['params']['pdfpi-']={}
conf['params']['pdfpi-']['widths1_ubv'] ={'value':    5.51292e-01,'min': 0.1,'max':0.8,'fixed':'proton widths uv'}
conf['params']['pdfpi-']['widths2_ubv'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdfpi-']['widths1_dv']  ={'value':    5.51292e-01,'min': 0.1,'max':0.8,'fixed':'widths1_ubv'}
conf['params']['pdfpi-']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_ubv'}
conf['params']['pdfpi-']['widths1_sea'] ={'value':    5.43879e-01,'min': 0.1,'max':0.8,'fixed':'proton widths sea'}
conf['params']['pdfpi-']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_ubv'}

#--TMD FF:
conf['params']['ffpi']={}
conf['params']['ffpi']['widths1_fav']  ={'value':    1.23498207e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffpi']['widths2_fav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffpi']['widths1_ufav'] ={'value':    1.45926107e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffpi']['widths2_ufav'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}

conf['params']['ffk']={}
conf['params']['ffk']['widths1_fav']   ={'value':    1.25339421e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffk']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']['widths1_ufav']  ={'value':    1.92328958e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffk']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}

conf['params']['ffh']={}
conf['params']['ffh']['widths1_fav']   ={'value':    1.24050e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']['widths1_ufav']  ={'value':    1.43730e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}


# Transversity
conf['params']['transversity']={}
conf['params']['transversity']['widths1_uv']  ={'value':    1.43015652e+00, 'min':0.1, 'max':2.0, 'fixed':False}
conf['params']['transversity']['widths1_dv']  ={'value':    3.12697e-01, 'min':0.2, 'max':0.8, 'fixed': 'widths1_uv'}
conf['params']['transversity']['widths1_sea'] ={'value':    8.35004e-01, 'min':0.05, 'max':2.0, 'fixed': True}
conf['params']['transversity']['widths2_uv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': True}
conf['params']['transversity']['widths2_dv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}
conf['params']['transversity']['widths2_sea'] ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}

conf['params']['transversity']['uv1 N 1'] ={'value':    2.87481627e-01, 'min': 0.25, 'max': 0.4, 'fixed':False}
conf['params']['transversity']['uv1 a 1'] ={'value':    8.12509723e-01, 'min': -0.5, 'max':5, 'fixed':False}
conf['params']['transversity']['uv1 b 1'] ={'value':    3.41264178e+00, 'min':0, 'max':12, 'fixed':False}
conf['params']['transversity']['uv1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 0.0, 'fixed': True}
conf['params']['transversity']['uv1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['uv1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['uv1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['uv1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['uv1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['uv1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['dv1 N 1'] ={'value':   4.46024666e-03, 'min': -0.5, 'max':0.1, 'fixed':False}
conf['params']['transversity']['dv1 a 1'] ={'value':    8.46492417e-01, 'min': -0.5, 'max': 4, 'fixed':False}
conf['params']['transversity']['dv1 b 1'] ={'value':    3.413e+00, 'min': 0, 'max':12, 'fixed': 'uv1 b 1'}
conf['params']['transversity']['dv1 c 1'] ={'value':    0.00000e+00, 'min':-1000.0, 'max': 0.0, 'fixed':True}
conf['params']['transversity']['dv1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['dv1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['dv1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['dv1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['dv1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['dv1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['sea1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': True}
conf['params']['transversity']['sea1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea1 b 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['sea2 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': True}
conf['params']['transversity']['sea2 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea2 b 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea2 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea2 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea2 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea2 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea2 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['sea2 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['sea2 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['s1 N 1'] ={'value':    0.00000e+00, 'min': -0.1, 'max': 0.1, 'fixed': True}
conf['params']['transversity']['s1 a 1'] ={'value':    0.00000e+00, 'min': 0.5, 'max':5, 'fixed': True}
conf['params']['transversity']['s1 b 1'] ={'value':    0.00000e+00, 'min': 0, 'max':20.0, 'fixed': True}
conf['params']['transversity']['s1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['ub1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's1 N 1'}
conf['params']['transversity']['ub1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 1'}
conf['params']['transversity']['ub1 b 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 1'}
conf['params']['transversity']['ub1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 1'}
conf['params']['transversity']['ub1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 1'}
conf['params']['transversity']['ub1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's1 N 2'}
conf['params']['transversity']['ub1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 2'}
conf['params']['transversity']['ub1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 2'}
conf['params']['transversity']['ub1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 2'}
conf['params']['transversity']['ub1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 2'}

conf['params']['transversity']['db1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's1 N 1'}
conf['params']['transversity']['db1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 1'}
conf['params']['transversity']['db1 b 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 1'}
conf['params']['transversity']['db1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 1'}
conf['params']['transversity']['db1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 1'}
conf['params']['transversity']['db1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's1 N 2'}
conf['params']['transversity']['db1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 2'}
conf['params']['transversity']['db1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 2'}
conf['params']['transversity']['db1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 2'}
conf['params']['transversity']['db1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 2'}

conf['params']['transversity']['sb1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's1 N 1'}
conf['params']['transversity']['sb1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 1'}
conf['params']['transversity']['sb1 b 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 1'}
conf['params']['transversity']['sb1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 1'}
conf['params']['transversity']['sb1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 1'}
conf['params']['transversity']['sb1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's1 N 2'}
conf['params']['transversity']['sb1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 2'}
conf['params']['transversity']['sb1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 2'}
conf['params']['transversity']['sb1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 2'}
conf['params']['transversity']['sb1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 2'}

conf['params']['transversity']['g1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': True}
conf['params']['transversity']['g1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['g1 b 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['g1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['g1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['g1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['g1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['g1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['g1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['g1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


# Collins TMD FF:
conf['params']['collinspi']={}
conf['params']['collinspi']['widths1_fav']   ={'value':    1.16272399e-01,'min':0.025, 'max':0.25, 'fixed':False}
conf['params']['collinspi']['widths1_ufav'] ={'value':    5.07490208e-02,'min':0.01, 'max':0.15, 'fixed':False}
conf['params']['collinspi']['widths2_fav']   ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['collinspi']['widths2_ufav'] ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}

conf['params']['collinspi']['u1 N 1'] ={'value':    1.58871529e-01,'min': -0.05, 'max':1.0, 'fixed':False}
conf['params']['collinspi']['u1 a 1'] ={'value':    1.86698145e+00,'min':-1, 'max':7, 'fixed':False}
conf['params']['collinspi']['u1 b 1'] ={'value':    1.96053905e+00,'min': 0, 'max': 5, 'fixed':False}
conf['params']['collinspi']['u1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u1 N 2'] ={'value':    1000,'min': 0, 'max': 1000, 'fixed':False}
conf['params']['collinspi']['u1 a 2'] ={'value':    0,'min':-1, 'max': 7, 'fixed':True}
conf['params']['collinspi']['u1 b 2'] ={'value':    1.21973804e+01,'min':5, 'max':15, 'fixed':False}
conf['params']['collinspi']['u1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['d1 N 1'] ={'value':   -4.01224215e-01,'min': -1.0, 'max':0.05, 'fixed':False}
conf['params']['collinspi']['d1 a 1'] ={'value':    0.5e+00,'min':-1, 'max': 3, 'fixed':False}
conf['params']['collinspi']['d1 b 1'] ={'value':    3.31336404e+00,'min': 0, 'max':10, 'fixed':False}
conf['params']['collinspi']['d1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d1 N 2'] ={'value':    200,'min':0, 'max':200, 'fixed':False}
conf['params']['collinspi']['d1 a 2'] ={'value':    0,'min': -1, 'max': 7, 'fixed':True}
conf['params']['collinspi']['d1 b 2'] ={'value':    1.89338073e+01,'min': 5, 'max':25, 'fixed':False}
conf['params']['collinspi']['d1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['s1 N 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10, 'fixed':'d1 N 1'}
conf['params']['collinspi']['s1 a 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20, 'fixed':'d1 a 1'}
conf['params']['collinspi']['s1 b 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10, 'fixed':'d1 b 1'}
conf['params']['collinspi']['s1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 c 1'}
conf['params']['collinspi']['s1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 d 1'}
conf['params']['collinspi']['s1 N 2'] ={'value':   -3.06065e+02,'min': 0, 'max': 1, 'fixed':'d1 N 2'}
conf['params']['collinspi']['s1 a 2'] ={'value':    8.69912e-01,'min':-2, 'max': 2, 'fixed':'d1 a 2'}
conf['params']['collinspi']['s1 b 2'] ={'value':    1.39667e+01,'min': 0, 'max':10, 'fixed':'d1 b 2'}
conf['params']['collinspi']['s1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 c 2'}
conf['params']['collinspi']['s1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 d 2'}

conf['params']['collinspi']['ub1 N 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10,  'fixed':'d1 N 1'}
conf['params']['collinspi']['ub1 a 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20,  'fixed':'d1 a 1'}
conf['params']['collinspi']['ub1 b 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10,    'fixed':'d1 b 1'}
conf['params']['collinspi']['ub1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 1'}
conf['params']['collinspi']['ub1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 1'}
conf['params']['collinspi']['ub1 N 2'] ={'value':   -3.06065e+02,'min': -10, 'max': 10, 'fixed':'d1 N 2'}
conf['params']['collinspi']['ub1 a 2'] ={'value':    8.69912e-01,'min':-2, 'max': 20,   'fixed':'d1 a 2'}
conf['params']['collinspi']['ub1 b 2'] ={'value':    1.39667e+01,'min': 0, 'max':10,    'fixed':'d1 b 2'}
conf['params']['collinspi']['ub1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 2'}
conf['params']['collinspi']['ub1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 2'}

conf['params']['collinspi']['db1 N 1'] ={'value':    1.56490e+00,'min': -15, 'max': 15,  'fixed':'u1 N 1'}
conf['params']['collinspi']['db1 a 1'] ={'value':    1.23346e-01,'min':-0.228, 'max': 5,  'fixed':'u1 a 1'}
conf['params']['collinspi']['db1 b 1'] ={'value':    2.90807e+00,'min': 0.9, 'max':15,    'fixed':'u1 b 1'}
conf['params']['collinspi']['db1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 c 1'}
conf['params']['collinspi']['db1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 d 1'}
conf['params']['collinspi']['db1 N 2'] ={'value':    2.93621e+00,'min': -15, 'max': 15, 'fixed':'u1 N 2'}
conf['params']['collinspi']['db1 a 2'] ={'value':    7.95023e-01,'min':-0.228, 'max': 20,   'fixed':'u1 a 2'}
conf['params']['collinspi']['db1 b 2'] ={'value':    5.72097e+00,'min': 1.20, 'max':10,    'fixed':'u1 b 2'}
conf['params']['collinspi']['db1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 c 2'}
conf['params']['collinspi']['db1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 d 2'}

conf['params']['collinspi']['sb1 N 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10,  'fixed':'d1 N 1'}
conf['params']['collinspi']['sb1 a 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20,  'fixed':'d1 a 1'}
conf['params']['collinspi']['sb1 b 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10,    'fixed':'d1 b 1'}
conf['params']['collinspi']['sb1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 1'}
conf['params']['collinspi']['sb1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 1'}
conf['params']['collinspi']['sb1 N 2'] ={'value':   -3.06065e+02,'min': -10, 'max': 10, 'fixed':'d1 N 2'}
conf['params']['collinspi']['sb1 a 2'] ={'value':    8.69912e-01,'min':-2, 'max': 20,   'fixed':'d1 a 2'}
conf['params']['collinspi']['sb1 b 2'] ={'value':    1.39667e+01,'min': 0, 'max':10,    'fixed':'d1 b 2'}
conf['params']['collinspi']['sb1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 2'}
conf['params']['collinspi']['sb1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 2'}

conf['params']['collinspi']['g1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':True}
conf['params']['collinspi']['g1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':True}
conf['params']['collinspi']['g1 b 1'] ={'value':   1.0,'min': 2.19, 'max':10,    'fixed':True}
conf['params']['collinspi']['g1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['g1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['g1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['collinspi']['g1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':True}
conf['params']['collinspi']['g1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':True}
conf['params']['collinspi']['g1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['g1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}

conf['params']['collinspi']['c1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':True}
conf['params']['collinspi']['c1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':True}
conf['params']['collinspi']['c1 b 1'] ={'value':   1.0,'min': 2.19, 'max':10,    'fixed':True}
conf['params']['collinspi']['c1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['c1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['c1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['collinspi']['c1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':True}
conf['params']['collinspi']['c1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':True}
conf['params']['collinspi']['c1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['c1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}

conf['params']['collinspi']['b1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':True}
conf['params']['collinspi']['b1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':True}
conf['params']['collinspi']['b1 b 1'] ={'value':   1.0,'min': 2.19, 'max':10,    'fixed':True}
conf['params']['collinspi']['b1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['b1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['b1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['collinspi']['b1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':True}
conf['params']['collinspi']['b1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':True}
conf['params']['collinspi']['b1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['collinspi']['b1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}

conf['params']['collinspi']['cb1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':'c1 N 1'}
conf['params']['collinspi']['cb1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':'c1 a 1'}
conf['params']['collinspi']['cb1 b 1'] ={'value':   1.0,'min': 2.19, 'max':10,    'fixed':'c1 b 1'}
conf['params']['collinspi']['cb1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 c 1'}
conf['params']['collinspi']['cb1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 d 1'}
conf['params']['collinspi']['cb1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':'c1 N 2'}
conf['params']['collinspi']['cb1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':'c1 a 2'}
conf['params']['collinspi']['cb1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':'c1 b 2'}
conf['params']['collinspi']['cb1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 c 2'}
conf['params']['collinspi']['cb1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 d 2'}

conf['params']['collinspi']['bb1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':'b1 N 1'}
conf['params']['collinspi']['bb1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':'b1 a 1'}
conf['params']['collinspi']['bb1 b 1'] ={'value':   1.0,'min': 2.19, 'max':10,    'fixed':'b1 b 1'}
conf['params']['collinspi']['bb1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 c 1'}
conf['params']['collinspi']['bb1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 d 1'}
conf['params']['collinspi']['bb1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':'b1 N 2'}
conf['params']['collinspi']['bb1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':'b1 a 2'}
conf['params']['collinspi']['bb1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':'b1 b 2'}
conf['params']['collinspi']['bb1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 c 2'}
conf['params']['collinspi']['bb1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 d 2'}

#mimic Collins, widths not required, but only 1 shape
conf['params']['Htildepi']={}
conf['params']['Htildepi']['widths1_fav']   ={'value':    1.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths1_ufav'] ={'value':    1.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths2_fav']   ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths2_ufav'] ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}

conf['params']['Htildepi']['u1 N 1'] ={'value':    0.0e+00,'min': -0.5, 'max': 0.5, 'fixed':True}
conf['params']['Htildepi']['u1 a 1'] ={'value':    4.0e+00,'min':1.0, 'max': 5, 'fixed':True}
conf['params']['Htildepi']['u1 b 1'] ={'value':    2.44590e+00,'min': 1, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u1 N 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed': True}
conf['params']['Htildepi']['u1 a 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20, 'fixed':True}
conf['params']['Htildepi']['u1 b 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['Htildepi']['d1 N 1'] ={'value':    0.0e+00,'min': -0.5, 'max': 0.5, 'fixed':True}
conf['params']['Htildepi']['d1 a 1'] ={'value':    3.0e+00,'min':1.0, 'max': 5, 'fixed':True}
conf['params']['Htildepi']['d1 b 1'] ={'value':    4.13470e+00,'min': 1, 'max':10, 'fixed':True}
conf['params']['Htildepi']['d1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d1 N 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['d1 a 2'] ={'value':    0.00000e+00,'min':-2, 'max': 5, 'fixed':True}
conf['params']['Htildepi']['d1 b 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['d1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['Htildepi']['s1 N 1'] ={'value':    5.68651e+00,'min': 0, 'max': 1, 'fixed':'d1 N 1'}
conf['params']['Htildepi']['s1 a 1'] ={'value':    1.79259e+00,'min':-2, 'max': 2, 'fixed':'d1 a 1'}
conf['params']['Htildepi']['s1 b 1'] ={'value':    4.13470e+00,'min': 0, 'max':10, 'fixed':'d1 b 1'}
conf['params']['Htildepi']['s1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 c 1'}
conf['params']['Htildepi']['s1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 d 1'}
conf['params']['Htildepi']['s1 N 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d1 N 2'}
conf['params']['Htildepi']['s1 a 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d1 a 2'}
conf['params']['Htildepi']['s1 b 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d1 b 2'}
conf['params']['Htildepi']['s1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 c 2'}
conf['params']['Htildepi']['s1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d1 d 2'}

conf['params']['Htildepi']['ub1 N 1'] ={'value':    5.68651e+00,'min': -15, 'max': 2,  'fixed':'d1 N 1'}
conf['params']['Htildepi']['ub1 a 1'] ={'value':    1.79259e+00,'min':-2.5, 'max': 5,  'fixed':'d1 a 1'}
conf['params']['Htildepi']['ub1 b 1'] ={'value':    4.13470e+00,'min': 0, 'max':10,    'fixed':'d1 b 1'}
conf['params']['Htildepi']['ub1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 1'}
conf['params']['Htildepi']['ub1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 1'}
conf['params']['Htildepi']['ub1 N 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d1 N 2'}
conf['params']['Htildepi']['ub1 a 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'d1 a 2'}
conf['params']['Htildepi']['ub1 b 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d1 b 2'}
conf['params']['Htildepi']['ub1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 2'}
conf['params']['Htildepi']['ub1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 2'}

conf['params']['Htildepi']['db1 N 1'] ={'value':   -6.31163e+00,'min': -15, 'max': 2,  'fixed':'u1 N 1'}
conf['params']['Htildepi']['db1 a 1'] ={'value':    5.33063e+00,'min':-2.5, 'max': 5,  'fixed':'u1 a 1'}
conf['params']['Htildepi']['db1 b 1'] ={'value':    1.44590e+00,'min': 0, 'max':10,    'fixed':'u1 b 1'}
conf['params']['Htildepi']['db1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 c 1'}
conf['params']['Htildepi']['db1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 d 1'}
conf['params']['Htildepi']['db1 N 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u1 N 2'}
conf['params']['Htildepi']['db1 a 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'u1 a 2'}
conf['params']['Htildepi']['db1 b 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u1 b 2'}
conf['params']['Htildepi']['db1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 c 2'}
conf['params']['Htildepi']['db1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u1 d 2'}

conf['params']['Htildepi']['sb1 N 1'] ={'value':    5.68651e+00,'min': -15, 'max': 2,  'fixed':'d1 N 1'}
conf['params']['Htildepi']['sb1 a 1'] ={'value':    1.79259e+00,'min':-2.5, 'max': 5,  'fixed':'d1 a 1'}
conf['params']['Htildepi']['sb1 b 1'] ={'value':    4.13470e+00,'min': 0, 'max':10,    'fixed':'d1 b 1'}
conf['params']['Htildepi']['sb1 c 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 1'}
conf['params']['Htildepi']['sb1 d 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 1'}
conf['params']['Htildepi']['sb1 N 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d1 N 2'}
conf['params']['Htildepi']['sb1 a 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'d1 a 2'}
conf['params']['Htildepi']['sb1 b 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d1 b 2'}
conf['params']['Htildepi']['sb1 c 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 c 2'}
conf['params']['Htildepi']['sb1 d 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d1 d 2'}

conf['params']['Htildepi']['g1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':True}
conf['params']['Htildepi']['g1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':True}
conf['params']['Htildepi']['g1 b 1'] ={'value':   0.0,'min': 2.19, 'max':10,    'fixed':True}
conf['params']['Htildepi']['g1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['g1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['g1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['g1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':True}
conf['params']['Htildepi']['g1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':True}
conf['params']['Htildepi']['g1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['g1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}

conf['params']['Htildepi']['c1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':True}
conf['params']['Htildepi']['c1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':True}
conf['params']['Htildepi']['c1 b 1'] ={'value':   0.0,'min': 2.19, 'max':10,    'fixed':True}
conf['params']['Htildepi']['c1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['c1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['c1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['c1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':True}
conf['params']['Htildepi']['c1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':True}
conf['params']['Htildepi']['c1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['c1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}

conf['params']['Htildepi']['b1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':True}
conf['params']['Htildepi']['b1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':True}
conf['params']['Htildepi']['b1 b 1'] ={'value':   0.0,'min': 2.19, 'max':10,    'fixed':True}
conf['params']['Htildepi']['b1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['b1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['b1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['b1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':True}
conf['params']['Htildepi']['b1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':True}
conf['params']['Htildepi']['b1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}
conf['params']['Htildepi']['b1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':True}

conf['params']['Htildepi']['cb1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':'c1 N 1'}
conf['params']['Htildepi']['cb1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':'c1 a 1'}
conf['params']['Htildepi']['cb1 b 1'] ={'value':   0.0,'min': 2.19, 'max':10,    'fixed':'c1 b 1'}
conf['params']['Htildepi']['cb1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 c 1'}
conf['params']['Htildepi']['cb1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 d 1'}
conf['params']['Htildepi']['cb1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':'c1 N 2'}
conf['params']['Htildepi']['cb1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':'c1 a 2'}
conf['params']['Htildepi']['cb1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':'c1 b 2'}
conf['params']['Htildepi']['cb1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 c 2'}
conf['params']['Htildepi']['cb1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'c1 d 2'}

conf['params']['Htildepi']['bb1 N 1'] ={'value':   0.0,'min': -15, 'max': 10,  'fixed':'b1 N 1'}
conf['params']['Htildepi']['bb1 a 1'] ={'value':   0.0,'min':-1, 'max': 20,  'fixed':'b1 a 1'}
conf['params']['Htildepi']['bb1 b 1'] ={'value':   0.0,'min': 2.19, 'max':10,    'fixed':'b1 b 1'}
conf['params']['Htildepi']['bb1 c 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 c 1'}
conf['params']['Htildepi']['bb1 d 1'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 d 1'}
conf['params']['Htildepi']['bb1 N 2'] ={'value':   0.0,'min': -10, 'max': 10, 'fixed':'b1 N 2'}
conf['params']['Htildepi']['bb1 a 2'] ={'value':   0.0,'min':-2, 'max': 20,   'fixed':'b1 a 2'}
conf['params']['Htildepi']['bb1 b 2'] ={'value':   0.0,'min': 0, 'max':10,    'fixed':'b1 b 2'}
conf['params']['Htildepi']['bb1 c 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 c 2'}
conf['params']['Htildepi']['bb1 d 2'] ={'value':   0.0,'min':-1, 'max': 1,    'fixed':'b1 d 2'}

#Sivers function
conf['params']['sivers']={}
conf['params']['sivers']['widths1_uv']  ={'value':    1.90375278e-01, 'min':0.1, 'max':1.0, 'fixed': False}
conf['params']['sivers']['widths1_dv']  ={'value':    3.27437e-01, 'min':0, 'max':2, 'fixed': 'widths1_uv'}
conf['params']['sivers']['widths1_sea'] ={'value':    4.88407e-01, 'min':0.1, 'max':2.0, 'fixed': True}
conf['params']['sivers']['widths2_uv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': True}
conf['params']['sivers']['widths2_dv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}
conf['params']['sivers']['widths2_sea'] ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}

conf['params']['sivers']['uv1 N 1'] ={'value':   -7.36742867e-03, 'min': -0.05, 'max': 0, 'fixed': False}
conf['params']['sivers']['uv1 a 1'] ={'value':    5.40346961e-01, 'min': -1.0, 'max':2.0, 'fixed': False}
conf['params']['sivers']['uv1 b 1'] ={'value':    7.70085858e+00, 'min': 0.5, 'max':17.0, 'fixed': False}
conf['params']['sivers']['uv1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['uv1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['uv1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['uv1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['uv1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['uv1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['uv1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['sivers']['dv1 N 1'] ={'value':    7.92889006e-03, 'min': 0, 'max': 0.05, 'fixed': False}
conf['params']['sivers']['dv1 a 1'] ={'value':    3.26290054e-01, 'min': -1.0, 'max':2, 'fixed': False}
conf['params']['sivers']['dv1 b 1'] ={'value':    1.95150e+01, 'min': 0, 'max':17.0, 'fixed': 'uv1 b 1'}
conf['params']['sivers']['dv1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['dv1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['dv1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['dv1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['dv1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['dv1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['dv1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['sivers']['sea1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': True}
conf['params']['sivers']['sea1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea1 b 1'] ={'value':    1.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['sivers']['sea2 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': True}
conf['params']['sivers']['sea2 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea2 b 1'] ={'value':    1.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea2 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea2 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea2 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea2 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea2 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['sea2 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['sea2 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['sivers']['s1 N 1'] ={'value':    0.00000e+00, 'min': -0.05, 'max': 0.05, 'fixed': True}
conf['params']['sivers']['s1 a 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max':10, 'fixed': True}
conf['params']['sivers']['s1 b 1'] ={'value':    1.00000e+00, 'min': 0, 'max':20.0, 'fixed': True}
conf['params']['sivers']['s1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['sivers']['ub1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's1 N 1'}
conf['params']['sivers']['ub1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 1'}
conf['params']['sivers']['ub1 b 1'] ={'value':    1.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 1'}
conf['params']['sivers']['ub1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 1'}
conf['params']['sivers']['ub1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 1'}
conf['params']['sivers']['ub1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's1 N 2'}
conf['params']['sivers']['ub1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 2'}
conf['params']['sivers']['ub1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 2'}
conf['params']['sivers']['ub1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 2'}
conf['params']['sivers']['ub1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 2'}

conf['params']['sivers']['db1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's1 N 1'}
conf['params']['sivers']['db1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 1'}
conf['params']['sivers']['db1 b 1'] ={'value':    1.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 1'}
conf['params']['sivers']['db1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 1'}
conf['params']['sivers']['db1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 1'}
conf['params']['sivers']['db1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's1 N 2'}
conf['params']['sivers']['db1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 2'}
conf['params']['sivers']['db1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 2'}
conf['params']['sivers']['db1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 2'}
conf['params']['sivers']['db1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 2'}

conf['params']['sivers']['sb1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's1 N 1'}
conf['params']['sivers']['sb1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 1'}
conf['params']['sivers']['sb1 b 1'] ={'value':    1.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 1'}
conf['params']['sivers']['sb1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 1'}
conf['params']['sivers']['sb1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 1'}
conf['params']['sivers']['sb1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's1 N 2'}
conf['params']['sivers']['sb1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's1 a 2'}
conf['params']['sivers']['sb1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's1 b 2'}
conf['params']['sivers']['sb1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 c 2'}
conf['params']['sivers']['sb1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's1 d 2'}

conf['params']['sivers']['g1 N 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': True}
conf['params']['sivers']['g1 a 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['g1 b 1'] ={'value':    1.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['g1 c 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['g1 d 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['g1 N 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['g1 a 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['g1 b 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['g1 c 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['g1 d 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


#--steps
conf['steps']={}


#'pdf'
#'ffpi'
#'transversity'
#'collinspi'
#'Htildepi'
#'sivers'

#--unpol sidis multiplicities (HERMES only)
#conf['steps'][1]={}
#conf['steps'][1]['dep']=[]
#conf['steps'][1]['active distributions']=['pdf','ffpi','ffk']
#conf['steps'][1]['datasets']={}
#conf['steps'][1]['datasets']['sidis']=[]
#conf['steps'][1]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][1]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes

##--sidis Sivers
#conf['steps'][2]={}
#conf['steps'][2]['dep']=[1]
#conf['steps'][2]['active distributions']=['pdf','ffpi','sivers','ffk']
#
#conf['steps'][2]['datasets']={}
#conf['steps'][2]['datasets']['sidis']=[]
#
#conf['steps'][2]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes
#
#conf['steps'][2]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][2]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][2]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][2]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
#conf['steps'][2]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
#conf['steps'][2]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
#conf['steps'][2]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
#conf['steps'][2]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
#conf['steps'][2]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
#conf['steps'][2]['datasets']['sidis'].append(2512) # proton   | pi+    | AUTsivers  | compass    | x
#conf['steps'][2]['datasets']['sidis'].append(2513) # proton   | pi+    | AUTsivers  | compass    | z
#conf['steps'][2]['datasets']['sidis'].append(2514) # proton   | pi+    | AUTsivers  | compass    | PT
#conf['steps'][2]['datasets']['sidis'].append(2515) # proton   | pi-    | AUTsivers  | compass    | x
#conf['steps'][2]['datasets']['sidis'].append(2516) # proton   | pi-    | AUTsivers  | compass    | z
#conf['steps'][2]['datasets']['sidis'].append(2517) # proton   | pi-    | AUTsivers  | compass    | PT

##--sidis collins
#conf['steps'][3]={}
#conf['steps'][3]['dep']=[1]
#conf['steps'][3]['active distributions']=['ffpi','collinspi','pdf','transversity','ffk']
#
#conf['steps'][3]['datasets']={}
#conf['steps'][3]['datasets']['sidis']=[]
#
#conf['steps'][3]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][3]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes
#
#conf['steps'][3]['datasets']['sidis'].append(4001)  #  compass  deuteron  pi+  pT
#conf['steps'][3]['datasets']['sidis'].append(4000)  #  compass  deuteron  pi+   x
#conf['steps'][3]['datasets']['sidis'].append(4002)  #  compass  deuteron  pi+   z
#conf['steps'][3]['datasets']['sidis'].append(4004)  #  compass  deuteron  pi-  pT
#conf['steps'][3]['datasets']['sidis'].append(4003)  #  compass  deuteron  pi-   x
#conf['steps'][3]['datasets']['sidis'].append(4005)  #  compass  deuteron  pi-   z
#conf['steps'][3]['datasets']['sidis'].append(3027)  #  compass    proton   pi+ pt
#conf['steps'][3]['datasets']['sidis'].append(3025)  #  compass    proton  pi+   x
#conf['steps'][3]['datasets']['sidis'].append(3010)  #  compass    proton  pi+   z
#conf['steps'][3]['datasets']['sidis'].append(3012)  #  compass    proton  pi-  pt
#conf['steps'][3]['datasets']['sidis'].append(3005)  #  compass    proton  pi-   x
#conf['steps'][3]['datasets']['sidis'].append(3013)  #  compass    proton  pi-   z
#conf['steps'][3]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][3]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][3]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][3]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][3]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][3]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#conf['steps'][3]['datasets']['sidis'].append(3006)  #   HERMES    proton  pi0   z
#conf['steps'][3]['datasets']['sidis'].append(3014)  #   HERMES    proton  pi0   x
#conf['steps'][3]['datasets']['sidis'].append(3015)  #   HERMES    proton  pi0  pt


##--(sia Collins) + (sidis Collins)
#conf['steps'][4]={}
#conf['steps'][4]['dep']=[1] #[3]
#conf['steps'][4]['active distributions']=['pdf','ffpi','transversity','collinspi','ffk']
#conf['steps'][4]['datasets']={}
#
#conf['steps'][4]['datasets']['sia']=[]
#conf['steps'][4]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
#conf['steps'][4]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
#conf['steps'][4]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
#conf['steps'][4]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
#conf['steps'][4]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
#conf['steps'][4]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
#conf['steps'][4]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
#conf['steps'][4]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
#
#conf['steps'][4]['datasets']['sidis']=[]
#conf['steps'][4]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][4]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes
#
#conf['steps'][4]['datasets']['sidis'].append(4001)  #  compass  deuteron  pi+  pT
#conf['steps'][4]['datasets']['sidis'].append(4000)  #  compass  deuteron  pi+   x
#conf['steps'][4]['datasets']['sidis'].append(4002)  #  compass  deuteron  pi+   z
#conf['steps'][4]['datasets']['sidis'].append(4004)  #  compass  deuteron  pi-  pT
#conf['steps'][4]['datasets']['sidis'].append(4003)  #  compass  deuteron  pi-   x
#conf['steps'][4]['datasets']['sidis'].append(4005)  #  compass  deuteron  pi-   z
#conf['steps'][4]['datasets']['sidis'].append(3027)  #  compass    proton   pi+ pt
#conf['steps'][4]['datasets']['sidis'].append(3025)  #  compass    proton  pi+   x
#conf['steps'][4]['datasets']['sidis'].append(3010)  #  compass    proton  pi+   z
#conf['steps'][4]['datasets']['sidis'].append(3012)  #  compass    proton  pi-  pt
#conf['steps'][4]['datasets']['sidis'].append(3005)  #  compass    proton  pi-   x
#conf['steps'][4]['datasets']['sidis'].append(3013)  #  compass    proton  pi-   z
#conf['steps'][4]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][4]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][4]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][4]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][4]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][4]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#conf['steps'][4]['datasets']['sidis'].append(3006)  #   HERMES    proton  pi0   z
#conf['steps'][4]['datasets']['sidis'].append(3014)  #   HERMES    proton  pi0   x
#conf['steps'][4]['datasets']['sidis'].append(3015)  #   HERMES    proton  pi0  pt

##--(sia Collins) + (sidis Collins) + (sidis Sivers)
#conf['steps'][5]={}
#conf['steps'][5]['dep']=[1] #[3]
#conf['steps'][5]['active distributions']=['pdf','ffpi','sivers','transversity','collinspi','ffk','Htildepi']
#conf['steps'][5]['datasets']={}
#
#conf['steps'][5]['datasets']['sia']=[]
#conf['steps'][5]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
#conf['steps'][5]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
#conf['steps'][5]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
#conf['steps'][5]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
#conf['steps'][5]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
#conf['steps'][5]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
#conf['steps'][5]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
#conf['steps'][5]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
#
#conf['steps'][5]['datasets']['sidis']=[]
#conf['steps'][5]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][5]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes
#
#conf['steps'][5]['datasets']['sidis'].append(4001)  #  compass  deuteron  pi+  pT
#conf['steps'][5]['datasets']['sidis'].append(4000)  #  compass  deuteron  pi+   x
#conf['steps'][5]['datasets']['sidis'].append(4002)  #  compass  deuteron  pi+   z
#conf['steps'][5]['datasets']['sidis'].append(4004)  #  compass  deuteron  pi-  pT
#conf['steps'][5]['datasets']['sidis'].append(4003)  #  compass  deuteron  pi-   x
#conf['steps'][5]['datasets']['sidis'].append(4005)  #  compass  deuteron  pi-   z
#conf['steps'][5]['datasets']['sidis'].append(3027)  #  compass    proton   pi+ pt
#conf['steps'][5]['datasets']['sidis'].append(3025)  #  compass    proton  pi+   x
#conf['steps'][5]['datasets']['sidis'].append(3010)  #  compass    proton  pi+   z
#conf['steps'][5]['datasets']['sidis'].append(3012)  #  compass    proton  pi-  pt
#conf['steps'][5]['datasets']['sidis'].append(3005)  #  compass    proton  pi-   x
#conf['steps'][5]['datasets']['sidis'].append(3013)  #  compass    proton  pi-   z
#conf['steps'][5]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][5]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][5]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][5]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][5]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][5]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#conf['steps'][5]['datasets']['sidis'].append(3006)  #   HERMES    proton  pi0   z
#conf['steps'][5]['datasets']['sidis'].append(3014)  #   HERMES    proton  pi0   x
#conf['steps'][5]['datasets']['sidis'].append(3015)  #   HERMES    proton  pi0  pt
#
#conf['steps'][5]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][5]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][5]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][5]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][5]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][5]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][5]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][5]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][5]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#conf['steps'][5]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
#conf['steps'][5]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
#conf['steps'][5]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
#conf['steps'][5]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
#conf['steps'][5]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
#conf['steps'][5]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
#conf['steps'][5]['datasets']['sidis'].append(2512) # proton   | pi+    | AUTsivers  | compass    | x
#conf['steps'][5]['datasets']['sidis'].append(2513) # proton   | pi+    | AUTsivers  | compass    | z
#conf['steps'][5]['datasets']['sidis'].append(2514) # proton   | pi+    | AUTsivers  | compass    | PT
#conf['steps'][5]['datasets']['sidis'].append(2515) # proton   | pi-    | AUTsivers  | compass    | x
#conf['steps'][5]['datasets']['sidis'].append(2516) # proton   | pi-    | AUTsivers  | compass    | z
#conf['steps'][5]['datasets']['sidis'].append(2517) # proton   | pi-    | AUTsivers  | compass    | PT
#
##conf['steps'][5]['datasets']['AN']=[]
##conf['steps'][5]['datasets']['AN'].append(1000) # BRAHMS pim 2.3
##conf['steps'][5]['datasets']['AN'].append(1001) # BRAHMS   pim 4
##conf['steps'][5]['datasets']['AN'].append(1002) # BRAHMS pip 2.3
##conf['steps'][5]['datasets']['AN'].append(1003) # BRAHMS   pip 4
##conf['steps'][5]['datasets']['AN'].append(2000) # STAR    piz 04
##conf['steps'][5]['datasets']['AN'].append(2001) # STAR   piz 3.3
##conf['steps'][5]['datasets']['AN'].append(2002) # STAR  piz 3.68
##conf['steps'][5]['datasets']['AN'].append(2003) # STAR   piz 3.7

##--unpol + (sidis Sivers) + (sia Collins) + (sidis Collins) + (pp A_N)
#conf['steps'][6]={}
#conf['steps'][6]['dep']=[1,5] #[2,4]
#conf['steps'][6]['active distributions']=['pdf','ffpi','sivers','collinspi','transversity','ffk','Htildepi']
#conf['steps'][6]['datasets']={}
#
#conf['steps'][6]['datasets']['sidis']=[]
#conf['steps'][6]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][6]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes
#
#conf['steps'][6]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][6]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][6]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][6]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][6]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][6]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][6]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][6]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][6]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#conf['steps'][6]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
#conf['steps'][6]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
#conf['steps'][6]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
#conf['steps'][6]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
#conf['steps'][6]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
#conf['steps'][6]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
#conf['steps'][6]['datasets']['sidis'].append(2512) # proton   | pi+    | AUTsivers  | compass    | x
#conf['steps'][6]['datasets']['sidis'].append(2513) # proton   | pi+    | AUTsivers  | compass    | z
#conf['steps'][6]['datasets']['sidis'].append(2514) # proton   | pi+    | AUTsivers  | compass    | PT
#conf['steps'][6]['datasets']['sidis'].append(2515) # proton   | pi-    | AUTsivers  | compass    | x
#conf['steps'][6]['datasets']['sidis'].append(2516) # proton   | pi-    | AUTsivers  | compass    | z
#conf['steps'][6]['datasets']['sidis'].append(2517) # proton   | pi-    | AUTsivers  | compass    | PT
#
#conf['steps'][6]['datasets']['sidis'].append(4001)  #  compass  deuteron  pi+  pT
#conf['steps'][6]['datasets']['sidis'].append(4000)  #  compass  deuteron  pi+   x
#conf['steps'][6]['datasets']['sidis'].append(4002)  #  compass  deuteron  pi+   z
#conf['steps'][6]['datasets']['sidis'].append(4004)  #  compass  deuteron  pi-  pT
#conf['steps'][6]['datasets']['sidis'].append(4003)  #  compass  deuteron  pi-   x
#conf['steps'][6]['datasets']['sidis'].append(4005)  #  compass  deuteron  pi-   z
#conf['steps'][6]['datasets']['sidis'].append(3027)  #  compass    proton   pi+ pt
#conf['steps'][6]['datasets']['sidis'].append(3025)  #  compass    proton  pi+   x
#conf['steps'][6]['datasets']['sidis'].append(3010)  #  compass    proton  pi+   z
#conf['steps'][6]['datasets']['sidis'].append(3012)  #  compass    proton  pi-  pt
#conf['steps'][6]['datasets']['sidis'].append(3005)  #  compass    proton  pi-   x
#conf['steps'][6]['datasets']['sidis'].append(3013)  #  compass    proton  pi-   z
#conf['steps'][6]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][6]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][6]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][6]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][6]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][6]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#conf['steps'][6]['datasets']['sidis'].append(3006)  #   HERMES    proton  pi0   z
#conf['steps'][6]['datasets']['sidis'].append(3014)  #   HERMES    proton  pi0   x
#conf['steps'][6]['datasets']['sidis'].append(3015)  #   HERMES    proton  pi0  pt
#
#
#conf['steps'][6]['datasets']['sia']=[]
#conf['steps'][6]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
#conf['steps'][6]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
#conf['steps'][6]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
#conf['steps'][6]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
#conf['steps'][6]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
#conf['steps'][6]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
#conf['steps'][6]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
#conf['steps'][6]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
#
#conf['steps'][6]['datasets']['AN']=[]
#conf['steps'][6]['datasets']['AN'].append(1000) # BRAHMS pim 2.3
#conf['steps'][6]['datasets']['AN'].append(1001) # BRAHMS   pim 4
#conf['steps'][6]['datasets']['AN'].append(1002) # BRAHMS pip 2.3
#conf['steps'][6]['datasets']['AN'].append(1003) # BRAHMS   pip 4
#conf['steps'][6]['datasets']['AN'].append(2000) # STAR    piz 04
#conf['steps'][6]['datasets']['AN'].append(2001) # STAR   piz 3.3
#conf['steps'][6]['datasets']['AN'].append(2002) # STAR  piz 3.68
#conf['steps'][6]['datasets']['AN'].append(2003) # STAR   piz 3.7

##--unpol + (sidis Sivers) + (sia Collins) + (sidis Collins) + (pp A_N)
conf['steps'][1]={}
conf['steps'][1]['dep']=[] #[1,6] #[2,4]
conf['steps'][1]['active distributions']=['pdf','pdfpi-','ffpi','sivers','collinspi','transversity','ffk','Htildepi']
#conf['steps'][1]['active distributions']=['pdf','pdfpi-','ffpi','sivers','ffk']
#conf['steps'][1]['active distributions']=['pdf','ffpi','collinspi', 'transversity','ffk']
#conf['steps'][1]['active distributions']=['pdf','pdfpi-','ffpi','sivers','collinspi','transversity','ffk']
conf['steps'][1]['datasets']={}

conf['steps'][1]['datasets']['sidis']=[]
conf['steps'][1]['datasets']['sidis'].append(1010) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1011) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1012) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1013) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1014) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1015) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1016) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1017) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes

conf['steps'][1]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
conf['steps'][1]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
conf['steps'][1]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
conf['steps'][1]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
conf['steps'][1]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
conf['steps'][1]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
conf['steps'][1]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
conf['steps'][1]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
conf['steps'][1]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
conf['steps'][1]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
conf['steps'][1]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
conf['steps'][1]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
conf['steps'][1]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
conf['steps'][1]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
conf['steps'][1]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
conf['steps'][1]['datasets']['sidis'].append(2512) # proton   | pi+    | AUTsivers  | compass    | x
conf['steps'][1]['datasets']['sidis'].append(2513) # proton   | pi+    | AUTsivers  | compass    | z
conf['steps'][1]['datasets']['sidis'].append(2514) # proton   | pi+    | AUTsivers  | compass    | PT
conf['steps'][1]['datasets']['sidis'].append(2515) # proton   | pi-    | AUTsivers  | compass    | x
conf['steps'][1]['datasets']['sidis'].append(2516) # proton   | pi-    | AUTsivers  | compass    | z
conf['steps'][1]['datasets']['sidis'].append(2517) # proton   | pi-    | AUTsivers  | compass    | PT

conf['steps'][1]['datasets']['dy']=[]
conf['steps'][1]['datasets']['dy'].append(1000)       # proton-pi- |    | AUTsivers  | compass    | xbeam
conf['steps'][1]['datasets']['dy'].append(1001)       # proton-pi- |    | AUTsivers  | compass    | xtarget
conf['steps'][1]['datasets']['dy'].append(1002)       # proton-pi- |    | AUTsivers  | compass    | xF
conf['steps'][1]['datasets']['dy'].append(1003)       # proton-pi- |    | AUTsivers  | compass    | qT

conf['steps'][1]['datasets']['wz']=[]
conf['steps'][1]['datasets']['wz'].append(2000)       # proton-proton |W+/-| AUTsivers  | star    | pT
conf['steps'][1]['datasets']['wz'].append(2001)       # proton-proton |W+/-| AUTsivers  | star    | y
conf['steps'][1]['datasets']['wz'].append(2002)       # proton-proton |Z   | AUTsivers  | star    | y

#conf['steps'][1]['datasets']['sidis'].append(4001)  #  compass  AUTcollins deuteron  pi+  pT
#conf['steps'][1]['datasets']['sidis'].append(4000)  #  compass  AUTcollins deuteron  pi+   x
#conf['steps'][1]['datasets']['sidis'].append(4002)  #  compass  AUTcollins deuteron  pi+   z
#conf['steps'][1]['datasets']['sidis'].append(4004)  #  compass  AUTcollins deuteron  pi-  pT
#conf['steps'][1]['datasets']['sidis'].append(4003)  #  compass  AUTcollins deuteron  pi-   x
#conf['steps'][1]['datasets']['sidis'].append(4005)  #  compass  AUTcollins deuteron  pi-   z
#conf['steps'][1]['datasets']['sidis'].append(3027)  #  compass  AUTcollins  proton   pi+ pt
#conf['steps'][1]['datasets']['sidis'].append(3025)  #  compass  AUTcollins  proton  pi+   x
#conf['steps'][1]['datasets']['sidis'].append(3010)  #  compass  AUTcollins  proton  pi+   z
#conf['steps'][1]['datasets']['sidis'].append(3012)  #  compass  AUTcollins  proton  pi-  pt
#conf['steps'][1]['datasets']['sidis'].append(3005)  #  compass  AUTcollins  proton  pi-   x
#conf['steps'][1]['datasets']['sidis'].append(3013)  #  compass  AUTcollins  proton  pi-   z
#conf['steps'][1]['datasets']['sidis'].append(3026)  #   HERMES  AUTcollins  proton pi+   pt
#conf['steps'][1]['datasets']['sidis'].append(3000)  #   HERMES  AUTcollins  proton pi+    x
#conf['steps'][1]['datasets']['sidis'].append(3003)  #   HERMES  AUTcollins  proton pi+    z
#conf['steps'][1]['datasets']['sidis'].append(3016)  #   HERMES  AUTcollins  proton  pi-  pt
#conf['steps'][1]['datasets']['sidis'].append(3004)  #   HERMES  AUTcollins  proton  pi-   x
#conf['steps'][1]['datasets']['sidis'].append(3018)  #   HERMES  AUTcollins  proton  pi-   z
#conf['steps'][1]['datasets']['sidis'].append(3006)  #   HERMES  AUTcollins  proton  pi0   z
#conf['steps'][1]['datasets']['sidis'].append(3014)  #   HERMES  AUTcollins  proton  pi0   x
#conf['steps'][1]['datasets']['sidis'].append(3015)  #   HERMES  AUTcollins  proton  pi0  pt

#conf['steps'][1]['datasets']['sidis'].append(9011)  #   COMPASS  AUTsinphiS  proton  h+    z
#conf['steps'][1]['datasets']['sidis'].append(9022)  #   COMPASS  AUTsinphiS  proton  h-    z
#conf['steps'][1]['datasets']['sidis'].append(9033)  #   COMPASS  AUTsinphiS  proton  h+    x
#conf['steps'][1]['datasets']['sidis'].append(9044)  #   COMPASS  AUTsinphiS  proton  h-    x

conf['steps'][1]['datasets']['sia']=[]
conf['steps'][1]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['steps'][1]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['steps'][1]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['steps'][1]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['steps'][1]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['steps'][1]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['steps'][1]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
conf['steps'][1]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
conf['steps'][1]['datasets']['sia'].append(3000) # bes3 | pi,pi | AUL-0     | 6     | z1,z2        |
conf['steps'][1]['datasets']['sia'].append(3001) # bes3 | pi,pi | AUC-0     | 6     | z1,z2        |
conf['steps'][1]['datasets']['sia'].append(3002) # bes3 | pi,pi | AUL-0     | 5     | z1,z2,pT     |
conf['steps'][1]['datasets']['sia'].append(3003) # bes3 | pi,pi | AUC-0     | 5     | z1,z2.pT     |

#conf['steps'][1]['datasets']['AN']=[]
#conf['steps'][1]['datasets']['AN'].append(1000) # BRAHMS pim 2.3
#conf['steps'][1]['datasets']['AN'].append(1001) # BRAHMS   pim 4
#conf['steps'][1]['datasets']['AN'].append(1002) # BRAHMS pip 2.3
#conf['steps'][1]['datasets']['AN'].append(1003) # BRAHMS   pip 4
#conf['steps'][1]['datasets']['AN'].append(2000) # STAR    piz 04
#conf['steps'][1]['datasets']['AN'].append(2001) # STAR   piz 3.3
#conf['steps'][1]['datasets']['AN'].append(2002) # STAR  piz 3.68
#conf['steps'][1]['datasets']['AN'].append(2003) # STAR   piz 3.7

###--unpol + (sidis Sivers) + (sia Collins) + (sidis Collins) + (pp A_N)
#conf['steps'][2]={}
#conf['steps'][2]['dep']=[1] #[1,6] #[2,4]
#conf['steps'][2]['active distributions']=['pdf','pdfpi-','ffpi','sivers','collinspi','transversity','ffk','Htildepi']
##conf['steps'][2]['active distributions']=['pdf','pdfpi-','ffpi','sivers','ffk']
##conf['steps'][2]['active distributions']=['pdf', 'pdfpi-','ffpi','collinspi', 'transversity','ffk']
##conf['steps'][2]['active distributions']=['pdf','pdfpi-','ffpi','sivers','collinspi','transversity','ffk']
#conf['steps'][2]['datasets']={}
#
#conf['steps'][2]['datasets']['sidis']=[]
#conf['steps'][2]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1002) #'sidis/expdata/1002.xlsx'  # |  proton   | k+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1003) #'sidis/expdata/1003.xlsx'  # |  proton   | k-   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1006) #'sidis/expdata/1004.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
#conf['steps'][2]['datasets']['sidis'].append(1007) #'sidis/expdata/1005.xlsx'  # |  deuteron | k-   | M_Hermes | hermes
#
#conf['steps'][2]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][2]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][2]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][2]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
#conf['steps'][2]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
#conf['steps'][2]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
#conf['steps'][2]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
#conf['steps'][2]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
#conf['steps'][2]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
#conf['steps'][2]['datasets']['sidis'].append(2512) # proton   | pi+    | AUTsivers  | compass    | x
#conf['steps'][2]['datasets']['sidis'].append(2513) # proton   | pi+    | AUTsivers  | compass    | z
#conf['steps'][2]['datasets']['sidis'].append(2514) # proton   | pi+    | AUTsivers  | compass    | PT
#conf['steps'][2]['datasets']['sidis'].append(2515) # proton   | pi-    | AUTsivers  | compass    | x
#conf['steps'][2]['datasets']['sidis'].append(2516) # proton   | pi-    | AUTsivers  | compass    | z
#conf['steps'][2]['datasets']['sidis'].append(2517) # proton   | pi-    | AUTsivers  | compass    | PT
#
#conf['steps'][2]['datasets']['dy']=[]
#conf['steps'][2]['datasets']['dy'].append(1000)       # proton-pi- |    | AUTsivers  | compass    | xbeam
#conf['steps'][2]['datasets']['dy'].append(1001)       # proton-pi- |    | AUTsivers  | compass    | xtarget
#conf['steps'][2]['datasets']['dy'].append(1002)       # proton-pi- |    | AUTsivers  | compass    | xF
#conf['steps'][2]['datasets']['dy'].append(1003)       # proton-pi- |    | AUTsivers  | compass    | qT
#
#conf['steps'][2]['datasets']['wz']=[]
#conf['steps'][2]['datasets']['wz'].append(2000)       # proton-proton |W+/-| AUTsivers  | star    | pT
#conf['steps'][2]['datasets']['wz'].append(2001)       # proton-proton |W+/-| AUTsivers  | star    | y
#conf['steps'][2]['datasets']['wz'].append(2002)       # proton-proton |Z   | AUTsivers  | star    | y
#
#conf['steps'][2]['datasets']['sidis'].append(4001)  #  compass  AUTcollins deuteron  pi+  pT
#conf['steps'][2]['datasets']['sidis'].append(4000)  #  compass  AUTcollins deuteron  pi+   x
#conf['steps'][2]['datasets']['sidis'].append(4002)  #  compass  AUTcollins deuteron  pi+   z
#conf['steps'][2]['datasets']['sidis'].append(4004)  #  compass  AUTcollins deuteron  pi-  pT
#conf['steps'][2]['datasets']['sidis'].append(4003)  #  compass  AUTcollins deuteron  pi-   x
#conf['steps'][2]['datasets']['sidis'].append(4005)  #  compass  AUTcollins deuteron  pi-   z
#conf['steps'][2]['datasets']['sidis'].append(3027)  #  compass  AUTcollins  proton   pi+ pt
#conf['steps'][2]['datasets']['sidis'].append(3025)  #  compass  AUTcollins  proton  pi+   x
#conf['steps'][2]['datasets']['sidis'].append(3010)  #  compass  AUTcollins  proton  pi+   z
#conf['steps'][2]['datasets']['sidis'].append(3012)  #  compass  AUTcollins  proton  pi-  pt
#conf['steps'][2]['datasets']['sidis'].append(3005)  #  compass  AUTcollins  proton  pi-   x
#conf['steps'][2]['datasets']['sidis'].append(3013)  #  compass  AUTcollins  proton  pi-   z
#conf['steps'][2]['datasets']['sidis'].append(3026)  #   HERMES  AUTcollins  proton pi+   pt
#conf['steps'][2]['datasets']['sidis'].append(3000)  #   HERMES  AUTcollins  proton pi+    x
#conf['steps'][2]['datasets']['sidis'].append(3003)  #   HERMES  AUTcollins  proton pi+    z
#conf['steps'][2]['datasets']['sidis'].append(3016)  #   HERMES  AUTcollins  proton  pi-  pt
#conf['steps'][2]['datasets']['sidis'].append(3004)  #   HERMES  AUTcollins  proton  pi-   x
#conf['steps'][2]['datasets']['sidis'].append(3018)  #   HERMES  AUTcollins  proton  pi-   z
#conf['steps'][2]['datasets']['sidis'].append(3006)  #   HERMES  AUTcollins  proton  pi0   z
#conf['steps'][2]['datasets']['sidis'].append(3014)  #   HERMES  AUTcollins  proton  pi0   x
#conf['steps'][2]['datasets']['sidis'].append(3015)  #   HERMES  AUTcollins  proton  pi0  pt
#
##conf['steps'][2]['datasets']['sidis'].append(9011)  #   COMPASS  AUTsinphiS  proton  h+    z
##conf['steps'][2]['datasets']['sidis'].append(9022)  #   COMPASS  AUTsinphiS  proton  h-    z
##conf['steps'][2]['datasets']['sidis'].append(9033)  #   COMPASS  AUTsinphiS  proton  h+    x
##conf['steps'][2]['datasets']['sidis'].append(9044)  #   COMPASS  AUTsinphiS  proton  h-    x
#
#conf['steps'][2]['datasets']['sia']=[]
#conf['steps'][2]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
#conf['steps'][2]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
#conf['steps'][2]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
#conf['steps'][2]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
#conf['steps'][2]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
#conf['steps'][2]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
#conf['steps'][2]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
#conf['steps'][2]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
#conf['steps'][2]['datasets']['sia'].append(3000) # bes3 | pi,pi | AUL-0     | 6     | z1,z2        |
#conf['steps'][2]['datasets']['sia'].append(3001) # bes3 | pi,pi | AUC-0     | 6     | z1,z2        |
#conf['steps'][2]['datasets']['sia'].append(3002) # bes3 | pi,pi | AUL-0     | 5     | z1,z2,pT     |
#conf['steps'][2]['datasets']['sia'].append(3003) # bes3 | pi,pi | AUC-0     | 5     | z1,z2.pT     |
#
#conf['steps'][2]['datasets']['AN']=[]
#conf['steps'][2]['datasets']['AN'].append(1000) # BRAHMS pim 2.3
#conf['steps'][2]['datasets']['AN'].append(1001) # BRAHMS   pim 4
#conf['steps'][2]['datasets']['AN'].append(1002) # BRAHMS pip 2.3
#conf['steps'][2]['datasets']['AN'].append(1003) # BRAHMS   pip 4
#conf['steps'][2]['datasets']['AN'].append(2000) # STAR    piz 04
#conf['steps'][2]['datasets']['AN'].append(2001) # STAR   piz 3.3
#conf['steps'][2]['datasets']['AN'].append(2002) # STAR  piz 3.68
#conf['steps'][2]['datasets']['AN'].append(2003) # STAR   piz 3.7
