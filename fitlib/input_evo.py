conf={}

#--setups
conf['bootstrap']=False
conf['flat par']=True
conf['ftol']=1e-8

conf['order']='LO'
conf['Q20']=1
#--datasets

conf['datasets']={}

conf['datasets']['sidis']={}
conf['datasets']['sidis']['filters']=["z>0.2 and z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9"]
conf['datasets']['sidis']['xlsx']={}

#--Unpol multiplicities (HERMES only)
conf['datasets']['sidis']['xlsx'][1000]='sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1001]='sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1004]='sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1005]='sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes

#--Collins effect SIDIS
#conf["datasets"]["sidis"]["xlsx"][4007]="sidis/expdata/4007.xlsx"  #  compass  deuteron   k+   pT
#conf["datasets"]["sidis"]["xlsx"][4006]="sidis/expdata/4006.xlsx"  #  compass  deuteron   k+    x
#conf["datasets"]["sidis"]["xlsx"][4008]="sidis/expdata/4008.xlsx"  #  compass  deuteron   k+    z
#conf["datasets"]["sidis"]["xlsx"][4010]="sidis/expdata/4010.xlsx"  #  compass  deuteron   k-   pT
#conf["datasets"]["sidis"]["xlsx"][4009]="sidis/expdata/4009.xlsx"  #  compass  deuteron   k-    x
#conf["datasets"]["sidis"]["xlsx"][4011]="sidis/expdata/4011.xlsx"  #  compass  deuteron   k-    z
conf["datasets"]["sidis"]["xlsx"][4001]="sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+  pT
conf["datasets"]["sidis"]["xlsx"][4000]="sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+   x
conf["datasets"]["sidis"]["xlsx"][4002]="sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+   z
conf["datasets"]["sidis"]["xlsx"][4004]="sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
#conf["datasets"]["sidis"]["xlsx"][6003]="sidis/expdata/6003.xlsx"  #  compass    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][6004]="sidis/expdata/6004.xlsx"  #  compass    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][6005]="sidis/expdata/6005.xlsx"  #  compass    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][6000]="sidis/expdata/6000.xlsx"  #  compass    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][6001]="sidis/expdata/6001.xlsx"  #  compass    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][6002]="sidis/expdata/6002.xlsx"  #  compass    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3027]="sidis/expdata/3027.xlsx"  #  compass    proton   pi+ pt
conf["datasets"]["sidis"]["xlsx"][3025]="sidis/expdata/3025.xlsx"  #  compass    proton  pi+   x
conf["datasets"]["sidis"]["xlsx"][3010]="sidis/expdata/3010.xlsx"  #  compass    proton  pi+  z
conf["datasets"]["sidis"]["xlsx"][3012]="sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
#conf["datasets"]["sidis"]["xlsx"][3024]="sidis/expdata/3024.xlsx"  #   HERMES    proton   k+   pt
#conf["datasets"]["sidis"]["xlsx"][3007]="sidis/expdata/3007.xlsx"  #   HERMES    proton   k+    x
#conf["datasets"]["sidis"]["xlsx"][3008]="sidis/expdata/3008.xlsx"  #   HERMES    proton   k+    z
#conf["datasets"]["sidis"]["xlsx"][3021]="sidis/expdata/3021.xlsx"  #   HERMES    proton   k-   pt
#conf["datasets"]["sidis"]["xlsx"][3017]="sidis/expdata/3017.xlsx"  #   HERMES    proton   k-    x
#conf["datasets"]["sidis"]["xlsx"][3023]="sidis/expdata/3023.xlsx"  #   HERMES    proton   k-    z
conf["datasets"]["sidis"]["xlsx"][3026]="sidis/expdata/3026.xlsx"  #   HERMES    proton pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="sidis/expdata/3000.xlsx"  #   HERMES    proton pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="sidis/expdata/3003.xlsx"  #   HERMES    proton pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z

#--A_{UT}^{}\sin\phi_S}
conf["datasets"]["sidis"]["xlsx"][9011]="sidis/expdata/9011.xlsx"  #   COMPASS    proton  h+    z
conf["datasets"]["sidis"]["xlsx"][9022]="sidis/expdata/9022.xlsx"  #   COMPASS    proton  h-    z
conf["datasets"]["sidis"]["xlsx"][9033]="sidis/expdata/9033.xlsx"  #   COMPASS    proton  h+    x
conf["datasets"]["sidis"]["xlsx"][9044]="sidis/expdata/9044.xlsx"  #   COMPASS    proton  h-    x

#--Sivers effect
conf['datasets']['sidis']['xlsx'][2000]='sidis/expdata/2000.xlsx' # proton   | pi+    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2001]='sidis/expdata/2001.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2002]='sidis/expdata/2002.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2003]='sidis/expdata/2003.xlsx' # proton   | pi-    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2004]='sidis/expdata/2004.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2005]='sidis/expdata/2005.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2006]='sidis/expdata/2006.xlsx' # proton   | pi0    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2007]='sidis/expdata/2007.xlsx' # proton   | pi0    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2008]='sidis/expdata/2008.xlsx' # proton   | pi0    | AUTsivers  | hermes     | z

conf['datasets']['sidis']['xlsx'][2020]='sidis/expdata/2020.xlsx' # proton | h+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2021]='sidis/expdata/2021.xlsx' # proton | h+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2022]='sidis/expdata/2022.xlsx' # proton | h+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2023]='sidis/expdata/2023.xlsx' # proton | h-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2024]='sidis/expdata/2024.xlsx' # proton | h-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2025]='sidis/expdata/2025.xlsx' # proton | h-    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2026]='sidis/expdata/2026.xlsx' # deuteron | pi+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2027]='sidis/expdata/2027.xlsx' # deuteron | pi+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2028]='sidis/expdata/2028.xlsx' # deuteron | pi+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2029]='sidis/expdata/2029.xlsx' # deuteron | pi-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2030]='sidis/expdata/2030.xlsx' # deuteron | pi-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2031]='sidis/expdata/2031.xlsx' # deuteron | pi-    | AUTsivers  | compass    | z

conf['datasets']['sidis']['xlsx'][2046]='sidis/expdata/2046.xlsx' # proton | h-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2047]='sidis/expdata/2047.xlsx' # proton | h-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2048]='sidis/expdata/2048.xlsx' # proton | h-    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2049]='sidis/expdata/2049.xlsx' # proton | h+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2050]='sidis/expdata/2050.xlsx' # proton | h+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2051]='sidis/expdata/2051.xlsx' # proton | h+    | AUTsivers  | compass    | z

conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}


#--Collins effect SIA
conf['datasets']['sia']={}
conf['datasets']['sia']['filters']=[]
#conf['datasets']['sia']['filters'].append("z1<0.7")
#conf['datasets']['sia']['filters'].append("z2<0.7")
#conf['datasets']['sia']['filters'].append("Q2>1.69")
#conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.9")
conf['datasets']['sia']['xlsx']={}

conf['datasets']['sia']['xlsx'][1000]='sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001]='sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1002]='sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003]='sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1004]='sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005]='sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][2008]='sia/expdata/2008.xlsx' # babar | pi,pi | AUL-0     | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2009]='sia/expdata/2009.xlsx' # babar | pi,pi | AUC-0     | 16     | z1,z2      |

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
conf['params']['pdf']['widths1_uv']  ={'value':    5.40344e-01,'min': 0.1,'max':0.8,'fixed':False}
conf['params']['pdf']['widths2_uv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['widths1_dv']  ={'value':    5.40344e-01,'min': 0.1,'max':0.8,'fixed':'widths1_uv'}
conf['params']['pdf']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}
conf['params']['pdf']['widths1_sea'] ={'value':    5.85373e-01,'min': 0.1,'max':0.8,'fixed':False}
conf['params']['pdf']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}

#--TMD FF:
conf['params']['ffpi']={}
conf['params']['ffpi']['widths1_fav']  ={'value':    1.22011e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffpi']['widths2_fav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffpi']['widths1_ufav'] ={'value':    1.43665e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffpi']['widths2_ufav'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}

conf['params']['ffk']={}
conf['params']['ffk']['widths1_fav']   ={'value':    1.32333e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffk']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']['widths1_ufav']  ={'value':    2.02660e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffk']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}

conf['params']['ffh']={}
conf['params']['ffh']['widths1_fav']   ={'value':    1.24050e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']['widths1_ufav']  ={'value':    1.43730e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}


# Transversity
conf['params']['transversity']={}
conf['params']['transversity']['widths1_uv']  ={'value':    7.11165e-01, 'min':0.2, 'max':0.8, 'fixed': False}
conf['params']['transversity']['widths1_dv']  ={'value':    2.12697e-01, 'min':0.2, 'max':0.8, 'fixed': 'widths1_uv'}
conf['params']['transversity']['widths1_sea'] ={'value':    5.35004e-01, 'min':0, 'max':1, 'fixed': True}
conf['params']['transversity']['widths2_uv']  ={'value':    0.00000e+00, 'min':0, 'max':0.5, 'fixed': False}
conf['params']['transversity']['widths2_dv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}
conf['params']['transversity']['widths2_sea'] ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}

conf['params']['transversity']['u N0 1'] ={'value':    7.48868e+00, 'min': 3.5, 'max': 20.0, 'fixed': False}
conf['params']['transversity']['u N1 1'] ={'value':    0.00000e+00, 'min': -10.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u a0 1'] ={'value':    6.29014e-01, 'min':-0.38, 'max':1.0, 'fixed': False}
conf['params']['transversity']['u a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b0 1'] ={'value':    4.94728e+00, 'min': 4.55, 'max':10.0, 'fixed': False}
conf['params']['transversity']['u b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['transversity']['d N0 1'] ={'value':   -1.72890e+02, 'min': -500, 'max': -50, 'fixed': False}
conf['params']['transversity']['d N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 'u N1 1'}
conf['params']['transversity']['d a0 1'] ={'value':    1.62862e+00, 'min':0.16, 'max':3.0, 'fixed': False}
conf['params']['transversity']['d a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 'u a1 1'}
conf['params']['transversity']['d b0 1'] ={'value':    8.87162e+00, 'min': 6.55, 'max':15.0, 'fixed': False}
conf['params']['transversity']['d b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 'u b1 1'}
conf['params']['transversity']['d c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['s N0 1'] ={'value':    0.00000e+00, 'min': -10.0, 'max': 10.0, 'fixed': True}
conf['params']['transversity']['s N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['transversity']['ub N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['transversity']['ub N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['transversity']['ub a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['transversity']['ub a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['transversity']['ub b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['transversity']['ub b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['transversity']['ub c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['transversity']['ub c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['transversity']['ub d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['transversity']['ub d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['transversity']['ub N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['transversity']['ub N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['transversity']['ub a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['transversity']['ub a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['transversity']['ub b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['transversity']['ub b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['transversity']['ub c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['transversity']['ub c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['transversity']['ub d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['transversity']['ub d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['transversity']['db N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['transversity']['db N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['transversity']['db a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['transversity']['db a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['transversity']['db b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['transversity']['db b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['transversity']['db c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['transversity']['db c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['transversity']['db d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['transversity']['db d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['transversity']['db N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['transversity']['db N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['transversity']['db a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['transversity']['db a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['transversity']['db b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['transversity']['db b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['transversity']['db c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['transversity']['db c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['transversity']['db d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['transversity']['db d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['transversity']['sb N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['transversity']['sb N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['transversity']['sb a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['transversity']['sb a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['transversity']['sb b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['transversity']['sb b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['transversity']['sb c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['transversity']['sb c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['transversity']['sb d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['transversity']['sb d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['transversity']['sb N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['transversity']['sb N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['transversity']['sb a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['transversity']['sb a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['transversity']['sb b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['transversity']['sb b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['transversity']['sb c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['transversity']['sb c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['transversity']['sb d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['transversity']['sb d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}



# Collins TMD FF:
conf['params']['collinspi']={}

conf['params']['collinspi']['widths1_fav']   ={'value':    1.22288e-01,'min':0.005, 'max':0.5, 'fixed':False}
conf['params']['collinspi']['widths1_ufav'] ={'value':    6.11536e-02,'min':0.005, 'max':0.5, 'fixed':False}
conf['params']['collinspi']['widths2_fav']   ={'value':    0.00000e+00,'min':0, 'max':0.5, 'fixed':False}
conf['params']['collinspi']['widths2_ufav'] ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':'widths2_fav'}

conf['params']['collinspi']['u N0 1'] ={'value':    1.56490e+00,'min': 0.5, 'max': 50.0, 'fixed':False}
conf['params']['collinspi']['u N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':True}
conf['params']['collinspi']['u a0 1'] ={'value':    1.23346e-01,'min':-0.228, 'max': 10.0, 'fixed':False}
conf['params']['collinspi']['u a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5, 'fixed':True}
conf['params']['collinspi']['u b0 1'] ={'value':    2.90807e+00,'min': 2.20, 'max':5.0, 'fixed':False}
conf['params']['collinspi']['u b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['u c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u N0 2'] ={'value':    2.93621e+00,'min': 1.0, 'max': 100.0, 'fixed':False}
conf['params']['collinspi']['u N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u a0 2'] ={'value':    7.95023e-01,'min':-0.228, 'max': 1.5, 'fixed':False}
conf['params']['collinspi']['u a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['u b0 2'] ={'value':    5.72097e+00,'min': 2.20, 'max':12, 'fixed':False}
conf['params']['collinspi']['u b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['u c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['d N0 1'] ={'value':   -5.94721e+00,'min': -100, 'max': -0.5, 'fixed':False}
conf['params']['collinspi']['d N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'u N1 1'}
conf['params']['collinspi']['d a0 1'] ={'value':    4.25846e+00,'min':0.123, 'max': 12.0, 'fixed':False}
conf['params']['collinspi']['d a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'u a1 1'}
conf['params']['collinspi']['d b0 1'] ={'value':    4.19000e+00,'min': 4.19, 'max':25, 'fixed':False}
conf['params']['collinspi']['d b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'u b1 1'}
conf['params']['collinspi']['d c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d N0 2'] ={'value':   -3.06065e+02,'min': -750, 'max': 50, 'fixed':False}
conf['params']['collinspi']['d N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d a0 2'] ={'value':    8.69912e-01,'min':0.123, 'max': 10, 'fixed':False}
conf['params']['collinspi']['d a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':True}
conf['params']['collinspi']['d b0 2'] ={'value':    1.39667e+01,'min': 3.19, 'max':100, 'fixed':False}
conf['params']['collinspi']['d b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['collinspi']['d c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['s N0 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10, 'fixed':'d N0 1'}
conf['params']['collinspi']['s N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 1'}
conf['params']['collinspi']['s a0 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20, 'fixed':'d a0 1'}
conf['params']['collinspi']['s a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 1'}
conf['params']['collinspi']['s b0 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10, 'fixed':'d b0 1'}
conf['params']['collinspi']['s b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 1'}
conf['params']['collinspi']['s c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 1'}
conf['params']['collinspi']['s c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 1'}
conf['params']['collinspi']['s d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 1'}
conf['params']['collinspi']['s d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 1'}
conf['params']['collinspi']['s N0 2'] ={'value':   -3.06065e+02,'min': 0, 'max': 1, 'fixed':'d N0 2'}
conf['params']['collinspi']['s N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 2'}
conf['params']['collinspi']['s a0 2'] ={'value':    8.69912e-01,'min':-2, 'max': 2, 'fixed':'d a0 2'}
conf['params']['collinspi']['s a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 2'}
conf['params']['collinspi']['s b0 2'] ={'value':    1.39667e+01,'min': 0, 'max':10, 'fixed':'d b0 2'}
conf['params']['collinspi']['s b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 2'}
conf['params']['collinspi']['s c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 2'}
conf['params']['collinspi']['s c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 2'}
conf['params']['collinspi']['s d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 2'}
conf['params']['collinspi']['s d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 2'}


conf['params']['collinspi']['ub N0 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10,  'fixed':'d N0 1'}
conf['params']['collinspi']['ub N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['collinspi']['ub a0 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20,  'fixed':'d a0 1'}
conf['params']['collinspi']['ub a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['collinspi']['ub b0 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10,    'fixed':'d b0 1'}
conf['params']['collinspi']['ub b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['collinspi']['ub c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['collinspi']['ub c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['collinspi']['ub d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['collinspi']['ub d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['collinspi']['ub N0 2'] ={'value':   -3.06065e+02,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['collinspi']['ub N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['collinspi']['ub a0 2'] ={'value':    8.69912e-01,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['collinspi']['ub a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['collinspi']['ub b0 2'] ={'value':    1.39667e+01,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['collinspi']['ub b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['collinspi']['ub c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['collinspi']['ub c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['collinspi']['ub d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['collinspi']['ub d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

conf['params']['collinspi']['db N0 1'] ={'value':    1.56490e+00,'min': -15, 'max': 15,  'fixed':'u N0 1'}
conf['params']['collinspi']['db N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u N1 1'}
conf['params']['collinspi']['db a0 1'] ={'value':    1.23346e-01,'min':-0.228, 'max': 5,  'fixed':'u a0 1'}
conf['params']['collinspi']['db a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'u a1 1'}
conf['params']['collinspi']['db b0 1'] ={'value':    2.90807e+00,'min': 0.9, 'max':15,    'fixed':'u b0 1'}
conf['params']['collinspi']['db b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 1'}
conf['params']['collinspi']['db c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 1'}
conf['params']['collinspi']['db c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 1'}
conf['params']['collinspi']['db d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 1'}
conf['params']['collinspi']['db d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 1'}
conf['params']['collinspi']['db N0 2'] ={'value':    2.93621e+00,'min': -15, 'max': 15, 'fixed':'u N0 2'}
conf['params']['collinspi']['db N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'u N1 2'}
conf['params']['collinspi']['db a0 2'] ={'value':    7.95023e-01,'min':-0.228, 'max': 20,   'fixed':'u a0 2'}
conf['params']['collinspi']['db a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'u a1 2'}
conf['params']['collinspi']['db b0 2'] ={'value':    5.72097e+00,'min': 1.20, 'max':10,    'fixed':'u b0 2'}
conf['params']['collinspi']['db b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 2'}
conf['params']['collinspi']['db c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 2'}
conf['params']['collinspi']['db c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 2'}
conf['params']['collinspi']['db d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 2'}
conf['params']['collinspi']['db d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 2'}

conf['params']['collinspi']['sb N0 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10,  'fixed':'d N0 1'}
conf['params']['collinspi']['sb N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['collinspi']['sb a0 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20,  'fixed':'d a0 1'}
conf['params']['collinspi']['sb a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['collinspi']['sb b0 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10,    'fixed':'d b0 1'}
conf['params']['collinspi']['sb b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['collinspi']['sb c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['collinspi']['sb c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['collinspi']['sb d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['collinspi']['sb d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['collinspi']['sb N0 2'] ={'value':   -3.06065e+02,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['collinspi']['sb N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['collinspi']['sb a0 2'] ={'value':    8.69912e-01,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['collinspi']['sb a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['collinspi']['sb b0 2'] ={'value':    1.39667e+01,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['collinspi']['sb b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['collinspi']['sb c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['collinspi']['sb c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['collinspi']['sb d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['collinspi']['sb d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

#mimic Collins, widths not required, but only 1 shape
conf['params']['Htildepi']={}
conf['params']['Htildepi']['widths1_fav']   ={'value':    1.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths1_ufav'] ={'value':    1.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths2_fav']   ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths2_ufav'] ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}

conf['params']['Htildepi']['u N0 1'] ={'value':   -6.31163e+00,'min': -15, 'max': -2.0, 'fixed':False}
conf['params']['Htildepi']['u N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['u a0 1'] ={'value':    5.33063e+00,'min':0.772, 'max': 10, 'fixed':False}
conf['params']['Htildepi']['u a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5, 'fixed':True}
conf['params']['Htildepi']['u b0 1'] ={'value':    1.44590e+00,'min': 1.2, 'max':5.0, 'fixed':False}
conf['params']['Htildepi']['u b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed': True}
conf['params']['Htildepi']['u N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20, 'fixed':True}
conf['params']['Htildepi']['u a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':True}
conf['params']['Htildepi']['u b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['Htildepi']['d N0 1'] ={'value':    5.68651e+00,'min': 2.0, 'max': 15, 'fixed':False}
conf['params']['Htildepi']['d N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'u N1 1'}
conf['params']['Htildepi']['d a0 1'] ={'value':    1.79259e+00,'min':1.123, 'max': 5.0, 'fixed':False}
conf['params']['Htildepi']['d a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'u a1 1'}
conf['params']['Htildepi']['d b0 1'] ={'value':    4.13470e+00,'min': 3.19, 'max':8.0, 'fixed':False}
conf['params']['Htildepi']['d b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'u b1 1'}
conf['params']['Htildepi']['d c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['d N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 5, 'fixed':True}
conf['params']['Htildepi']['d a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':True}
conf['params']['Htildepi']['d b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['d b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['d c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['Htildepi']['s N0 1'] ={'value':    5.68651e+00,'min': 0, 'max': 1, 'fixed':'d N0 1'}
conf['params']['Htildepi']['s N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 1'}
conf['params']['Htildepi']['s a0 1'] ={'value':    1.79259e+00,'min':-2, 'max': 2, 'fixed':'d a0 1'}
conf['params']['Htildepi']['s a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 1'}
conf['params']['Htildepi']['s b0 1'] ={'value':    4.13470e+00,'min': 0, 'max':10, 'fixed':'d b0 1'}
conf['params']['Htildepi']['s b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 1'}
conf['params']['Htildepi']['s c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 1'}
conf['params']['Htildepi']['s c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 1'}
conf['params']['Htildepi']['s d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 1'}
conf['params']['Htildepi']['s d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 1'}
conf['params']['Htildepi']['s N0 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N0 2'}
conf['params']['Htildepi']['s N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 2'}
conf['params']['Htildepi']['s a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a0 2'}
conf['params']['Htildepi']['s a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 2'}
conf['params']['Htildepi']['s b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b0 2'}
conf['params']['Htildepi']['s b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 2'}
conf['params']['Htildepi']['s c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 2'}
conf['params']['Htildepi']['s c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 2'}
conf['params']['Htildepi']['s d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 2'}
conf['params']['Htildepi']['s d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 2'}


conf['params']['Htildepi']['ub N0 1'] ={'value':    5.68651e+00,'min': -15, 'max': 2,  'fixed':'d N0 1'}
conf['params']['Htildepi']['ub N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['Htildepi']['ub a0 1'] ={'value':    1.79259e+00,'min':-2.5, 'max': 5,  'fixed':'d a0 1'}
conf['params']['Htildepi']['ub a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['Htildepi']['ub b0 1'] ={'value':    4.13470e+00,'min': 0, 'max':10,    'fixed':'d b0 1'}
conf['params']['Htildepi']['ub b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['Htildepi']['ub c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['Htildepi']['ub c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['Htildepi']['ub d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['Htildepi']['ub d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['Htildepi']['ub N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['Htildepi']['ub N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['Htildepi']['ub a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['Htildepi']['ub a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['Htildepi']['ub b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['Htildepi']['ub b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['Htildepi']['ub c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['Htildepi']['ub c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['Htildepi']['ub d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['Htildepi']['ub d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

conf['params']['Htildepi']['db N0 1'] ={'value':   -6.31163e+00,'min': -15, 'max': 2,  'fixed':'u N0 1'}
conf['params']['Htildepi']['db N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u N1 1'}
conf['params']['Htildepi']['db a0 1'] ={'value':    5.33063e+00,'min':-2.5, 'max': 5,  'fixed':'u a0 1'}
conf['params']['Htildepi']['db a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'u a1 1'}
conf['params']['Htildepi']['db b0 1'] ={'value':    1.44590e+00,'min': 0, 'max':10,    'fixed':'u b0 1'}
conf['params']['Htildepi']['db b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 1'}
conf['params']['Htildepi']['db c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 1'}
conf['params']['Htildepi']['db c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 1'}
conf['params']['Htildepi']['db d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 1'}
conf['params']['Htildepi']['db d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 1'}
conf['params']['Htildepi']['db N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u N0 2'}
conf['params']['Htildepi']['db N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'u N1 2'}
conf['params']['Htildepi']['db a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'u a0 2'}
conf['params']['Htildepi']['db a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'u a1 2'}
conf['params']['Htildepi']['db b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b0 2'}
conf['params']['Htildepi']['db b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 2'}
conf['params']['Htildepi']['db c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 2'}
conf['params']['Htildepi']['db c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 2'}
conf['params']['Htildepi']['db d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 2'}
conf['params']['Htildepi']['db d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 2'}

conf['params']['Htildepi']['sb N0 1'] ={'value':    5.68651e+00,'min': -15, 'max': 2,  'fixed':'d N0 1'}
conf['params']['Htildepi']['sb N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['Htildepi']['sb a0 1'] ={'value':    1.79259e+00,'min':-2.5, 'max': 5,  'fixed':'d a0 1'}
conf['params']['Htildepi']['sb a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['Htildepi']['sb b0 1'] ={'value':    4.13470e+00,'min': 0, 'max':10,    'fixed':'d b0 1'}
conf['params']['Htildepi']['sb b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['Htildepi']['sb c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['Htildepi']['sb c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['Htildepi']['sb d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['Htildepi']['sb d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['Htildepi']['sb N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['Htildepi']['sb N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['Htildepi']['sb a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['Htildepi']['sb a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['Htildepi']['sb b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['Htildepi']['sb b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['Htildepi']['sb c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['Htildepi']['sb c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['Htildepi']['sb d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['Htildepi']['sb d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

#Sivers function
conf['params']['sivers']={}
conf['params']['sivers']['widths1_uv']  ={'value':    2.47890e-01, 'min':0.01, 'max':0.8, 'fixed': False}
conf['params']['sivers']['widths1_dv']  ={'value':    3.27437e-01, 'min':0, 'max':1, 'fixed': 'widths1_uv'}
conf['params']['sivers']['widths1_sea'] ={'value':    3.88407e-01, 'min':0, 'max':1, 'fixed': True}
conf['params']['sivers']['widths2_uv']  ={'value':    0.00000e+00, 'min':0, 'max':0.5, 'fixed': False}
conf['params']['sivers']['widths2_dv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}
conf['params']['sivers']['widths2_sea'] ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}

conf['params']['sivers']['u N0 1'] ={'value':   -3.43648e+00, 'min': -8.0, 'max': -1.0, 'fixed': False}
conf['params']['sivers']['u N1 1'] ={'value':    0.00000e+00, 'min': -10.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u a0 1'] ={'value':    7.58691e-01, 'min':0.62, 'max':1.5, 'fixed': False}
conf['params']['sivers']['u a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u b0 1'] ={'value':    1.16529e+01, 'min': 4.55, 'max':20.0, 'fixed': False}
conf['params']['sivers']['u b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['sivers']['d N0 1'] ={'value':    3.01373e+01, 'min': 10.0, 'max': 50.0, 'fixed': False}
conf['params']['sivers']['d N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 'u N1 1'}
conf['params']['sivers']['d a0 1'] ={'value':    1.19070e+00, 'min':1.16, 'max':2.5, 'fixed': False}
conf['params']['sivers']['d a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 'u a1 1'}
conf['params']['sivers']['d b0 1'] ={'value':    1.95150e+01, 'min': 7.55, 'max':35.0, 'fixed': False}
conf['params']['sivers']['d b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 'u b1 1'}
conf['params']['sivers']['d c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['sivers']['s N0 1'] ={'value':    0.00000e+00, 'min': -10.0, 'max': 10.0, 'fixed': True}
conf['params']['sivers']['s N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['sivers']['ub N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['sivers']['ub N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['sivers']['ub a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['sivers']['ub a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['sivers']['ub b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['sivers']['ub b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['sivers']['ub c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['sivers']['ub c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['sivers']['ub d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['sivers']['ub d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['sivers']['ub N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['sivers']['ub N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['sivers']['ub a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['sivers']['ub a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['sivers']['ub b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['sivers']['ub b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['sivers']['ub c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['sivers']['ub c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['sivers']['ub d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['sivers']['ub d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['sivers']['db N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['sivers']['db N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['sivers']['db a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['sivers']['db a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['sivers']['db b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['sivers']['db b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['sivers']['db c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['sivers']['db c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['sivers']['db d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['sivers']['db d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['sivers']['db N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['sivers']['db N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['sivers']['db a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['sivers']['db a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['sivers']['db b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['sivers']['db b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['sivers']['db c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['sivers']['db c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['sivers']['db d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['sivers']['db d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['sivers']['sb N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['sivers']['sb N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['sivers']['sb a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['sivers']['sb a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['sivers']['sb b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['sivers']['sb b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['sivers']['sb c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['sivers']['sb c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['sivers']['sb d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['sivers']['sb d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['sivers']['sb N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['sivers']['sb N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['sivers']['sb a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['sivers']['sb a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['sivers']['sb b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['sivers']['sb b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['sivers']['sb c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['sivers']['sb c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['sivers']['sb d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['sivers']['sb d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}



#--steps
conf['steps']={}


#'pdf'
#'ffpi'
#'transversity'
#'collinspi'
#'Htildepi'
#'sivers'

#--unpol sidis multiplicities (HERMES only)
conf['steps'][1]={}
conf['steps'][1]['dep']=[]
conf['steps'][1]['active distributions']=['pdf','ffpi']
conf['steps'][1]['datasets']={}
conf['steps'][1]['datasets']['sidis']=[]
conf['steps'][1]['datasets']['sidis'].append(1000) #'sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1001) #'sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1004) #'sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
conf['steps'][1]['datasets']['sidis'].append(1005) #'sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes

##--sidis Sivers (HERMES only)
#conf['steps'][2]={}
#conf['steps'][2]['dep']=[1]
#conf['steps'][2]['active distributions']=['pdf','ffpi','sivers']
#
#conf['steps'][2]['datasets']={}
#conf['steps'][2]['datasets']['sidis']=[]
#conf['steps'][2]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][2]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][2]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][2]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][2]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][2]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#
##--sidis Sivers (HERMES + COMPASS)
#conf['steps'][3]={}
#conf['steps'][3]['dep']=[2]
#conf['steps'][3]['active distributions']=['pdf','ffpi','sivers']
#
#conf['steps'][3]['datasets']={}
#conf['steps'][3]['datasets']['sidis']=[]
#conf['steps'][3]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][3]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][3]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][3]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][3]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][3]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][3]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][3]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][3]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#conf['steps'][3]['datasets']['sidis'].append(2020) # proton | h+    | AUTsivers  | compass   | PT
#conf['steps'][3]['datasets']['sidis'].append(2021) # proton | h+    | AUTsivers  | compass    | x
#conf['steps'][3]['datasets']['sidis'].append(2022) # proton | h+    | AUTsivers  | compass    | z
#conf['steps'][3]['datasets']['sidis'].append(2023) # proton | h-    | AUTsivers  | compass   | PT
#conf['steps'][3]['datasets']['sidis'].append(2024) # proton | h-    | AUTsivers  | compass    | x
#conf['steps'][3]['datasets']['sidis'].append(2025) # proton | h-    | AUTsivers  | compass    | z
#conf['steps'][3]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
#conf['steps'][3]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
#conf['steps'][3]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
#conf['steps'][3]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
#conf['steps'][3]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
#conf['steps'][3]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
#conf['steps'][3]['datasets']['sidis'].append(2046) # proton | h-    | AUTsivers  | compass   | PT
#conf['steps'][3]['datasets']['sidis'].append(2047) # proton | h-    | AUTsivers  | compass    | x
#conf['steps'][3]['datasets']['sidis'].append(2048) # proton | h-    | AUTsivers  | compass    | z
#conf['steps'][3]['datasets']['sidis'].append(2049) # proton | h+    | AUTsivers  | compass   | PT
#conf['steps'][3]['datasets']['sidis'].append(2050) # proton | h+    | AUTsivers  | compass    | x
#conf['steps'][3]['datasets']['sidis'].append(2051) # proton | h+    | AUTsivers  | compass    | z
#
##--sidis Collins (HERMES only)
#conf['steps'][4]={}
#conf['steps'][4]['dep']=[1]
#conf['steps'][4]['active distributions']=['pdf','ffpi','transversity','collinspi']
#conf['steps'][4]['datasets']={}
#
#conf['steps'][4]['datasets']['sidis']=[]
#conf['steps'][4]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][4]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][4]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][4]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][4]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][4]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#
##--sidis Collins (HERMES + COMPASS)
#conf['steps'][5]={}
#conf['steps'][5]['dep']=[4]
#conf['steps'][5]['active distributions']=['pdf','ffpi','transversity','collinspi']
#conf['steps'][5]['datasets']={}
#
#conf['steps'][5]['datasets']['sidis']=[]
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
#
##--(sia Collins) + (sidis Collins)
#conf['steps'][6]={}
#conf['steps'][6]['dep']=[5]
#conf['steps'][6]['active distributions']=['pdf','ffpi','transversity','collinspi']
#conf['steps'][6]['datasets']={}
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
#conf['steps'][6]['datasets']['sidis']=[]
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
#
##--(sia collins) + (sidis Collins) + (sidis AUT\sin\phi_S)
#conf['steps'][7]={}
#conf['steps'][7]['dep']=[6]
#conf['steps'][7]['active distributions']=['pdf','ffpi','transversity','Htildepi','collinspi']
#conf['steps'][7]['datasets']={}
#
#conf['steps'][7]['datasets']['sidis']=[]
#conf['steps'][7]['datasets']['sidis'].append(9011)  #   COMPASS    proton  h+    z
#conf['steps'][7]['datasets']['sidis'].append(9022)  #   COMPASS    proton  h-    z
#conf['steps'][7]['datasets']['sidis'].append(9033)  #   COMPASS    proton  h+    x
#conf['steps'][7]['datasets']['sidis'].append(9044)  #   COMPASS    proton  h-    x
#
#conf['steps'][7]['datasets']['sidis'].append(4001)  #  compass  deuteron  pi+  pT
#conf['steps'][7]['datasets']['sidis'].append(4000)  #  compass  deuteron  pi+   x
#conf['steps'][7]['datasets']['sidis'].append(4002)  #  compass  deuteron  pi+   z
#conf['steps'][7]['datasets']['sidis'].append(4004)  #  compass  deuteron  pi-  pT
#conf['steps'][7]['datasets']['sidis'].append(4003)  #  compass  deuteron  pi-   x
#conf['steps'][7]['datasets']['sidis'].append(4005)  #  compass  deuteron  pi-   z
#conf['steps'][7]['datasets']['sidis'].append(3027)  #  compass    proton   pi+ pt
#conf['steps'][7]['datasets']['sidis'].append(3025)  #  compass    proton  pi+   x
#conf['steps'][7]['datasets']['sidis'].append(3010)  #  compass    proton  pi+   z
#conf['steps'][7]['datasets']['sidis'].append(3012)  #  compass    proton  pi-  pt
#conf['steps'][7]['datasets']['sidis'].append(3005)  #  compass    proton  pi-   x
#conf['steps'][7]['datasets']['sidis'].append(3013)  #  compass    proton  pi-   z
#conf['steps'][7]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][7]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][7]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][7]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][7]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][7]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#
#conf['steps'][7]['datasets']['sia']=[]
#conf['steps'][7]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
#conf['steps'][7]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
#conf['steps'][7]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
#conf['steps'][7]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
#conf['steps'][7]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
#conf['steps'][7]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
#conf['steps'][7]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
#conf['steps'][7]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
#
##--unpol + (sidis Sivers) + (sia Collins) + (sidis Collins) + (sidis AUT\sin\phi_S) + (pp A_N)
#conf['steps'][8]={}
#conf['steps'][8]['dep']=[3,7]
#conf['steps'][8]['active distributions']=['pdf','ffpi','sivers','collinspi','transversity','Htildepi']
#conf['steps'][8]['datasets']={}
#
#conf['steps'][8]['datasets']['sidis']=[]
#conf['steps'][8]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
#conf['steps'][8]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][8]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][8]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
#conf['steps'][8]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][8]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][8]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
#conf['steps'][8]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
#conf['steps'][8]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
#conf['steps'][8]['datasets']['sidis'].append(2020) # proton | h+    | AUTsivers  | compass   | PT
#conf['steps'][8]['datasets']['sidis'].append(2021) # proton | h+    | AUTsivers  | compass    | x
#conf['steps'][8]['datasets']['sidis'].append(2022) # proton | h+    | AUTsivers  | compass    | z
#conf['steps'][8]['datasets']['sidis'].append(2023) # proton | h-    | AUTsivers  | compass   | PT
#conf['steps'][8]['datasets']['sidis'].append(2024) # proton | h-    | AUTsivers  | compass    | x
#conf['steps'][8]['datasets']['sidis'].append(2025) # proton | h-    | AUTsivers  | compass    | z
#conf['steps'][8]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
#conf['steps'][8]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
#conf['steps'][8]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
#conf['steps'][8]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
#conf['steps'][8]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
#conf['steps'][8]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
#conf['steps'][8]['datasets']['sidis'].append(2046) # proton | h-    | AUTsivers  | compass   | PT
#conf['steps'][8]['datasets']['sidis'].append(2047) # proton | h-    | AUTsivers  | compass    | x
#conf['steps'][8]['datasets']['sidis'].append(2048) # proton | h-    | AUTsivers  | compass    | z
#conf['steps'][8]['datasets']['sidis'].append(2049) # proton | h+    | AUTsivers  | compass   | PT
#conf['steps'][8]['datasets']['sidis'].append(2050) # proton | h+    | AUTsivers  | compass    | x
#conf['steps'][8]['datasets']['sidis'].append(2051) # proton | h+    | AUTsivers  | compass    | z
#
#conf['steps'][8]['datasets']['sidis'].append(4001)  #  compass  deuteron  pi+  pT
#conf['steps'][8]['datasets']['sidis'].append(4000)  #  compass  deuteron  pi+   x
#conf['steps'][8]['datasets']['sidis'].append(4002)  #  compass  deuteron  pi+   z
#conf['steps'][8]['datasets']['sidis'].append(4004)  #  compass  deuteron  pi-  pT
#conf['steps'][8]['datasets']['sidis'].append(4003)  #  compass  deuteron  pi-   x
#conf['steps'][8]['datasets']['sidis'].append(4005)  #  compass  deuteron  pi-   z
#conf['steps'][8]['datasets']['sidis'].append(3027)  #  compass    proton   pi+ pt
#conf['steps'][8]['datasets']['sidis'].append(3025)  #  compass    proton  pi+   x
#conf['steps'][8]['datasets']['sidis'].append(3010)  #  compass    proton  pi+   z
#conf['steps'][8]['datasets']['sidis'].append(3012)  #  compass    proton  pi-  pt
#conf['steps'][8]['datasets']['sidis'].append(3005)  #  compass    proton  pi-   x
#conf['steps'][8]['datasets']['sidis'].append(3013)  #  compass    proton  pi-   z
#conf['steps'][8]['datasets']['sidis'].append(3026)  #   HERMES    proton pi+   pt
#conf['steps'][8]['datasets']['sidis'].append(3000)  #   HERMES    proton pi+    x
#conf['steps'][8]['datasets']['sidis'].append(3003)  #   HERMES    proton pi+    z
#conf['steps'][8]['datasets']['sidis'].append(3016)  #   HERMES    proton  pi-  pt
#conf['steps'][8]['datasets']['sidis'].append(3004)  #   HERMES    proton  pi-   x
#conf['steps'][8]['datasets']['sidis'].append(3018)  #   HERMES    proton  pi-   z
#
#conf['steps'][8]['datasets']['sidis'].append(9011)  #   COMPASS    proton  h+    z
#conf['steps'][8]['datasets']['sidis'].append(9022)  #   COMPASS    proton  h-    z
#conf['steps'][8]['datasets']['sidis'].append(9033)  #   COMPASS    proton  h+    x
#conf['steps'][8]['datasets']['sidis'].append(9044)  #   COMPASS    proton  h-    x
#
#conf['steps'][8]['datasets']['sia']=[]
#conf['steps'][8]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
#conf['steps'][8]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
#conf['steps'][8]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
#conf['steps'][8]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
#conf['steps'][8]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
#conf['steps'][8]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
#conf['steps'][8]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
#conf['steps'][8]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
#
#conf['steps'][8]['datasets']['AN']=[]
#conf['steps'][8]['datasets']['AN'].append(1000) # BRAHMS pim 2.3
#conf['steps'][8]['datasets']['AN'].append(1001) # BRAHMS   pim 4
#conf['steps'][8]['datasets']['AN'].append(1002) # BRAHMS pip 2.3
#conf['steps'][8]['datasets']['AN'].append(1003) # BRAHMS   pip 4
#conf['steps'][8]['datasets']['AN'].append(2000) # STAR    piz 04
#conf['steps'][8]['datasets']['AN'].append(2001) # STAR   piz 3.3
#conf['steps'][8]['datasets']['AN'].append(2002) # STAR  piz 3.68
#conf['steps'][8]['datasets']['AN'].append(2003) # STAR   piz 3.7
