#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import pandas as pd
import math
import time
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf
from scipy.integrate import quad, dblquad, fixed_quad


#This includes the SFP term to AN in pp -> gam X (see 1410.3448)

flavor = ['g','u','ub','d','db','s','sb']
        #  0   1   2    3    4   5    6
target = ['p']

flavdict = {'g': 0, 'u': 1, 'ub': 2,'d': 3, 'db': 4, 's': 5, 'sb': 6}

# Common color factors and fractions
c = {'r3': 1. / 3., 'r4': 0.25, 'r6': 1. / 6., 'r8': 0.125,
         'r9': 1. / 9., 'r18': 1. / 18., 'r24': 1. / 24., 'r27': 1. / 27.}

m = {}
HPall = {}
HQS = {}
f = {}
ft = {}
f1Tp = {}
G = {}

eu2, ed2 = 4/9., 1/9.
e2 = []
e2.append(0) #g
e2.append(eu2) #u
e2.append(eu2) #ub
e2.append(ed2) #d
e2.append(ed2) #db
e2.append(ed2) #s
e2.append(ed2) #sb
e2.append(0) #c
e2.append(0) #cb
e2.append(0) #b
e2.append(0) #bb
e2 = np.array(e2)

e = []
e.append(0) #g
e.append(2.0/3.0) #u
e.append(-2.0/3.0) #ub
e.append(-1.0/3.0) #d
e.append(1.0/3.0) #db
e.append(-1.0/3.0) #s
e.append(1.0/3.0) #sb
e.append(0) #c
e.append(0) #cb
e.append(0) #b
e.append(0) #bb
e = np.array(e)

if 'basis' not in conf:
  conf['basis'] = 'default'

def get_f(x, Q2): # Collinear unpolarized PDF
  return conf['pdf'].get_C(x, Q2)

def get_ft(x, Q2): # Collinear unpolarized PDF
  return conf['pdf'].get_C(x, Q2)

def get_f1Tp(x, Q2): # (f_1T^{\perp(1)}(x) - x*df_1T^{\perp(1)}(x)/dx)
    return conf['sivers'].get_C(x, Q2) - x * conf['dsivers'].get_C(x, Q2)

def get_G(x, Q2): # (f_1T^{\perp(1)}(x) #This is F_FT(0,x) + \tild{F}(0,x), which we assume = F_FT(x,x)
    return conf['sivers'].get_C(x, Q2)

def get_mandelstam(rs, xF, pT, x):
# Convenient combinations of the partonic Mandelstam variables
   m['s'] = CV.ss_value(rs, xF, pT, x)
   m['s2'] = CV.ss_value(rs, xF, pT, x) * CV.ss_value(rs, xF, pT, x)
   m['s3'] = CV.ss_value(rs, xF, pT, x)**3.
   m['t'] = CV.tt_value(rs, xF, pT, x)
   m['t2'] = CV.tt_value(rs, xF, pT, x) * CV.tt_value(rs, xF, pT, x)
   m['t3'] = CV.tt_value(rs, xF, pT, x)**3.
   m['u'] = CV.uu_value(rs, xF, pT, x)
   m['u2'] = CV.uu_value(rs, xF, pT, x) * CV.uu_value(rs, xF, pT, x)
   m['u3'] = CV.uu_value(rs, xF, pT, x)**3.
   m['ostu'] = 1. / ( CV.ss_value(rs, xF, pT, x)* CV.tt_value(rs, xF, pT, x) * CV.uu_value(rs, xF, pT, x))
   m['os'] = 1. / CV.ss_value(rs, xF, pT, x)
   m['ot'] = 1. / CV.tt_value(rs, xF, pT, x)
   m['ou'] = 1. / CV.uu_value(rs, xF, pT, x)
   m['st'] = CV.ss_value(rs, xF, pT, x) / CV.tt_value(rs, xF, pT, x)
   m['su'] = CV.ss_value(rs, xF, pT, x) / CV.uu_value(rs, xF, pT, x)
   m['ts'] = CV.tt_value(rs, xF, pT, x) / CV.ss_value(rs, xF, pT, x)
   m['tu'] = CV.tt_value(rs, xF, pT, x) / CV.uu_value(rs, xF, pT, x)
   m['us'] = CV.uu_value(rs, xF, pT, x) / CV.ss_value(rs, xF, pT, x)
   m['ut'] = CV.uu_value(rs, xF, pT, x) / CV.tt_value(rs, xF, pT, x)
   m['st2'] = CV.ss_value(rs, xF, pT, x)**2. / CV.tt_value(rs, xF, pT, x)**2.
   m['su2'] = CV.ss_value(rs, xF, pT, x)**2. / CV.uu_value(rs, xF, pT, x)**2.
   m['ts2'] = CV.tt_value(rs, xF, pT, x)**2. / CV.ss_value(rs, xF, pT, x)**2.
   m['tu2'] = CV.tt_value(rs, xF, pT, x)**2. / CV.uu_value(rs, xF, pT, x)**2.
   m['us2'] = CV.uu_value(rs, xF, pT, x)**2. / CV.ss_value(rs, xF, pT, x)**2.
   m['ut2'] = CV.uu_value(rs, xF, pT, x)**2. / CV.tt_value(rs, xF, pT, x)**2.
   m['os2'] = 1. / CV.ss_value(rs, xF, pT, x)**2.
   m['ot2'] = 1. / CV.tt_value(rs, xF, pT, x)**2.
   m['ou2'] = 1. / CV.uu_value(rs, xF, pT, x)**2.
   m['os3'] = 1. / CV.ss_value(rs, xF, pT, x)**3.
   m['ot3'] = 1. / CV.tt_value(rs, xF, pT, x)**3.
   m['ou3'] = 1. / CV.uu_value(rs, xF, pT, x)**3.
   return m

# Hard parts for all the functions
def get_HPall(m):
   N_C = 3.0

   #Found in SFP numerator
   HPall[1] = (2. * (m['s2'] + m['u2']) / (m['t2']*m['u'])) + (2. * m['s'] * (m['u'] - m['s']) / (N_C * m['t'] * m['u2']))
   HPall[2] = (-2. * (m['s2'] + m['u2']) / (m['t2']*m['u'])) + ((2. * N_C * m['s'] / (m['u2'])) + (2. * (m['u2'] + m['s']*m['t']) / (N_C * m['s'] * m['t'] * m['u'])))
   HPall[3] = 2. * (N_C * N_C * m['t'] * m['u'] - (m['s'] * (m['s'] - m['t']))) / ((N_C * N_C - 1.) * m['s'] * m['t'] * m['u'])

   #HPall[4] and [5] when the quarks are not the same, eq 27 & 28 in 1410.3448
   #Found in SFP numerator
   HPall[4] = (2. * (m['s2'] + m['u2']) / (m['t2']*m['u']))
   HPall[5] = -(2. * (m['s2'] + m['u2']) / (m['t2']*m['u']))

   # Found in unpolarized cross section and SGP numerator
   HPall[6] = m['ut'] + m['tu']
   HPall[7] = (-m['st']) - m['ts']
   HPall[8] = (-m['su']) - m['us']
   return HPall

class Class_Variables():
    #Declaring all the class methods that are referenced throughout
    @classmethod
    def S_value(cls, rs):
        return rs**2
    @classmethod
    def T_value(cls, rs, xF, pT):
        return (- rs * np.sqrt( (pT**2) + (xF * xF * CV.S_value(rs) / 4.0))) + (xF * CV.S_value(rs) / 2.0)
    @classmethod
    def U_value(cls, rs, xF, pT):
        return (- rs * np.sqrt( (pT**2) + (xF * xF * CV.S_value(rs) / 4.0))) - (xF * CV.S_value(rs) / 2.0)
    @classmethod
    def xp_value(cls, rs, xF, pT, x):
        return -x * CV.T_value(rs, xF, pT) / (x * CV.S_value(rs) + CV.U_value(rs, xF, pT))
    @classmethod
    def ss_value(cls, rs, xF, pT, x):
        return x * CV.xp_value(rs, xF, pT, x) * CV.S_value(rs)
    @classmethod
    def tt_value(cls, rs, xF, pT, x):
        return x * CV.T_value(rs, xF, pT)
    @classmethod
    def uu_value(cls, rs, xF, pT, x):
        return CV.xp_value(rs, xF, pT, x) * CV.U_value(rs, xF, pT)

################################################################################
#Defining Consistent Variables
CV = Class_Variables()

C_F = 4.0/3.0
N_C = 3.0
################################################################################

#  @profile
# Calculation of the unpolarized cross section
def get_upolden(x, xF, pT, rs):

  if pT > 1.:
    Q = pT
  else:
    Q = 1.

  Q2 = Q * Q

  M = conf['aux'].M
  xp = -x * CV.T_value(rs, xF, pT) / (x * CV.S_value(rs) + CV.U_value(rs, xF, pT))
  # Prefactor
  denfac = (1. / (N_C * (x * CV.S_value(rs) + CV.U_value(rs, xF, pT)))) * (1. / (x * CV.xp_value(rs, xF, pT, x)))

  #calling mandelstam variables
  m=get_mandelstam(rs, xF, pT, x)

  #Calling Hard Factors
  HPall=get_HPall(m)
  HPall1 = HPall[6]
  HPall2 = HPall[7]
  HPall3 = HPall[8]

  # Get arrays of the nonperturbative functions
  ft = get_ft(xp,Q2)
  ftg = ft[0]
  ftu = ft[1]
  ftub = ft[2]
  ftd = ft[3]
  ftdb = ft[4]
  fts = ft[5]
  ftsb = ft[6]

  f = get_f(x,Q2)
  fg = f[0]
  fu = f[1]
  fub = f[2]
  fd = f[3]
  fdb = f[4]
  fs = f[5]
  fsb = f[6]
############################################################################

  upol = 0

  upol += ((ftu * fub * 2. * C_F * HPall1) + (ftub * fg *HPall3) + (ftg * fu * HPall2)) * e2[1]

  upol += ((ftub * fu * 2. * C_F * HPall1) + (ftu * fg *HPall3) + (ftg * fub * HPall2)) * e2[2]

  upol += ((ftd * fdb * 2. * C_F * HPall1) + (ftdb * fg *HPall3) + (ftg * fd * HPall2)) * e2[3]

  upol += ((ftdb * fd * 2. * C_F * HPall1) + (ftd * fg *HPall3) + (ftg * fdb * HPall2)) * e2[4]

  upol += ((fts * fsb * 2. * C_F * HPall1) + (ftsb * fg *HPall3) + (ftg * fs * HPall2)) * e2[5]

  upol += ((ftsb * fs * 2. * C_F * HPall1) + (fts * fg *HPall3) + (ftg * fsb * HPall2)) * e2[6]

  return denfac * upol

#  @profile
# Calculation of the fragmentation term in the transversely polarized cross section
def get_polnum_SFP(x, xF, pT, rs):

  if pT > 1.:
    Q = pT
  else:
    Q = 1.

  Q2 = Q * Q

  M = conf['aux'].M

  # Prefactor
  numfac = (2.0 * M * pT) * (1. / (x * CV.xp_value(rs, xF, pT, x))) / (x * CV.S_value(rs) + CV.U_value(rs, xF, pT))

  #calling mandelstam variables
  m=get_mandelstam(rs, xF, pT, x)
  xp = -x * CV.T_value(rs, xF, pT) / (x * CV.S_value(rs) + CV.U_value(rs, xF, pT))
  #Calling Hard Factors
  HPall=get_HPall(m)
  HPall1 = HPall[1]
  HPall2 = HPall[2]
  HPall3 = HPall[3]
  HPall4 = HPall[4]
  HPall5 = HPall[5]

  # Get arrays of the nonperturbative functions
  ft = get_ft(xp,Q2)
  ftg = ft[0]
  ftu = ft[1]
  ftub = ft[2]
  ftd = ft[3]
  ftdb = ft[4]
  fts = ft[5]
  ftsb = ft[6]

  f = get_f(x,Q2)
  fg = f[0]
  fu = f[1]
  fub = f[2]
  fd = f[3]
  fdb = f[4]
  fs = f[5]
  fsb = f[6]

  G = get_G(x,Q2)
  Gg = G[0]
  Gu = G[1]
  Gub = G[2]
  Gd = G[3]
  Gdb = G[4]
  Gs = G[5]
  Gsb = G[6]
############################################################################

  SFPcs = 0
# a = u
  SFPcs += ((e[1]**2 * HPall1 *fu * Gu) + (e[1] * e[3] * HPall4 *fd * Gu) + (e[1] * e[5] * HPall4 *fs * Gu)) + ((e[1]**2 * HPall2 *fub * Gu) + (e[1] * e[3] * HPall5 *fdb * Gu) + (e[1] * e[5] * HPall5 *fsb * Gu)) + (e[1]**2 * HPall3 * Gu * fg)
# a = ub
  SFPcs += ((e[2]**2 * HPall1 *fub * Gub) + (e[2] * e[4] * HPall4 *fdb * Gub) + (e[2] * e[6] * HPall4 *fsb * Gub)) + ((e[2]**2 * HPall2 *fu * Gub) + (e[2] * e[4] * HPall5 *fd * Gub) + (e[2] * e[6] * HPall5 *fs * Gub)) + (e[2]**2 * HPall3 * Gub * fg)
# a = d
  SFPcs += ((e[3] * e[1] * HPall4 *fu * Gd) + (e[3]**2 * HPall1 *fd * Gd) + (e[3] * e[5] * HPall4 *fs * Gd)) + ((e[3] * e[1] * HPall5 *fub * Gd) + (e[3]**2 * HPall2 *fdb * Gd) + (e[3] * e[5] * HPall5 *fsb * Gd)) + (e[3]**2 * HPall3 * Gd * fg)
# a = db
  SFPcs += ((e[4] * e[2] * HPall4 *fub * Gdb) + (e[4]**2 * HPall1 *fdb * Gdb) + (e[4] * e[6] * HPall4 *fsb * Gdb)) + ((e[4] * e[2] * HPall5 *fu * Gdb) + (e[4]**2 * HPall2 *fd * Gdb) + (e[4] * e[6] * HPall5 *fs * Gdb)) + (e[4]**2 * HPall3 * Gdb * fg)
# a = s
  SFPcs += ((e[5] * e[1] * HPall4 *fu * Gs) + (e[5] * e[3] * HPall4 *fd * Gs) + (e[5]**2 * HPall1 *fs * Gs)) + ((e[5] * e[1] * HPall5 *fub * Gs) + (e[5] * e[3] * HPall5 *fdb * Gs) + (e[5]**2 * HPall2 *fsb * Gs)) + (e[5]**2 * HPall3 * Gs * fg)
# a = sb
  SFPcs += ((e[6] * e[2] * HPall4 *fub * Gsb) + (e[6] * e[4] * HPall4 *fdb * Gsb) + (e[6]**2 * HPall1 *fsb * Gsb)) + ((e[6] * e[2] * HPall5 *fu * Gsb) + (e[6] * e[4] * HPall5 *fd * Gsb) + (e[6]**2 * HPall2 *fs * Gsb)) + (e[6]**2 * HPall3 * Gsb * fg)

  return (1./(2.*N_C)) * SFPcs * numfac

def get_polnum_SGP(x, xF, pT, rs):

  if pT > 1.:
    Q = pT
  else:
    Q = 1.

  Q2 = Q * Q

  M = conf['aux'].M

  # Prefactor
  numfac = (-2.0 * M * pT) * (1. / (x * CV.xp_value(rs, xF, pT, x))) / (x * CV.S_value(rs) + CV.U_value(rs, xF, pT))

  #calling mandelstam variables
  m=get_mandelstam(rs, xF, pT, x)
  xp = -x * CV.T_value(rs, xF, pT) / (x * CV.S_value(rs) + CV.U_value(rs, xF, pT))
  #Calling Hard Factors
  HPall=get_HPall(m)
  HPall1 = HPall[6]
  HPall2 = HPall[7]
  HPall3 = HPall[8]

  # Get arrays of the nonperturbative functions
  ft = get_ft(xp,Q2)
  ftg = ft[0]
  ftu = ft[1]
  ftub = ft[2]
  ftd = ft[3]
  ftdb = ft[4]
  fts = ft[5]
  ftsb = ft[6]

  f = get_f(x,Q2)
  fg = f[0]
  fu = f[1]
  fub = f[2]
  fd = f[3]
  fdb = f[4]
  fs = f[5]
  fsb = f[6]

  uQS = get_f1Tp(x,Q2)[1]
  ubQS = get_f1Tp(x,Q2)[2]
  dQS = get_f1Tp(x,Q2)[3]
  dbQS = get_f1Tp(x,Q2)[4]
  sQS = get_f1Tp(x,Q2)[5]
  sbQS = get_f1Tp(x,Q2)[6]
############################################################################

  SGPcs = 0

  SGPcs += (((-1 / (N_C**2)) * ftub * HPall1) + ((1 / (2. * C_F)) * ftg *HPall2)) * (1. / CV.uu_value(rs, xF, pT, x)) * uQS * e2[1]

  SGPcs += (((-1 / (N_C**2)) * ftu * HPall1) + ((1 / (2.* C_F)) * ftg *HPall2)) * (1. / CV.uu_value(rs, xF, pT, x)) * ubQS * e2[2]

  SGPcs += (((-1 / (N_C**2)) * ftdb * HPall1) + ((1 / (2. * C_F)) * ftg *HPall2)) * (1. / CV.uu_value(rs, xF, pT, x)) * dQS * e2[3]

  SGPcs += (((-1 / (N_C**2)) * ftd * HPall1) + ((1 / (2.* C_F)) * ftg *HPall2)) * (1. / CV.uu_value(rs, xF, pT, x)) * dbQS * e2[4]

  SGPcs += (((-1 / (N_C**2)) * ftsb * HPall1) + ((1 / (2. * C_F)) * ftg *HPall2)) * (1. / CV.uu_value(rs, xF, pT, x)) * sQS * e2[5]

  SGPcs += (((-1 / (N_C**2)) * fts * HPall1) + ((1 / (2.* C_F)) * ftg *HPall2)) * (1. / CV.uu_value(rs, xF, pT, x)) * sbQS * e2[6]

  return SGPcs * numfac


#### INTEGRAL OF NUMERATORS ####
def get_numint_SFP(xF, pT, rs, nx = 10):
    # Lower limits of the x integration
    xmin = -CV.U_value(rs, xF, pT) / (CV.S_value(rs) + CV.T_value(rs, xF, pT))

    dnumerdx = np.vectorize(lambda x: get_polnum_SFP(x, xF, pT, rs))
    numer = fixed_quad(dnumerdx, xmin, 1., n = nx)[0]
    return numer

def get_numint_SGP(xF, pT, rs, nx = 10):
    # Lower limits of the x integration
    xmin = -CV.U_value(rs, xF, pT) / (CV.S_value(rs) + CV.T_value(rs, xF, pT))

    dnumerdx = np.vectorize(lambda x: get_polnum_SGP(x, xF, pT, rs))
    numer = fixed_quad(dnumerdx, xmin, 1., n = nx)[0]
    return numer


#### INTEGRAL OF DENOMINATOR ####
def get_denomint(xF, pT, rs, nx = 10):
    # Lower limits of the x integration
    xmin = -CV.U_value(rs, xF, pT) / (CV.S_value(rs) + CV.T_value(rs, xF, pT))

    ddenomdx = np.vectorize(lambda x: get_upolden(x, xF, pT, rs))
    denom = fixed_quad(ddenomdx, xmin, 1., n = nx)[0]
    return denom

#### DIFFERENT ASPECTS ####
def get_SFP(xF, pT, rs, nx=10):
    return get_numint_SFP(xF, pT, rs, nx) / get_denomint(xF, pT, rs, nx)

def get_SGP(xF, pT, rs, nx=10):
    return get_numint_SGP(xF, pT, rs, nx) / get_denomint(xF, pT, rs, nx)

def get_AN(xF, pT, rs, nx=10):
    return get_SFP(xF, pT, rs, nx=10) + get_SGP(xF, pT, rs, nx=10)

# def get_vars(rs, n):
#     xF_over_pT = 2 * np.sinh(n) / rs
#     return xF_over_pT
if __name__ == '__main__':


  from qcdlib.ff0 import FF as FF0
  from qcdlib.ff1 import FF as FF1
  from qcdlib.pdf0 import PDF as PDF0
  from qcdlib.pdf1 import PDF as PDF1
  conf['aux']= AUX()
  conf['pdf']=PDF0()
  conf['sivers']=PDF1()
  conf['dsivers']=PDF1('deriv')
  conf['ffpi']=FF0('pi')
  conf['ffk']=FF0('k')

  rs = 200.
  tar = 'p'
  pT = 2.
  xF = 0.3
  C_F = 4.0/3.0
  N_C = 3.0

  def test():
    AN = get_AN(xF, pT, rs, nx = 10)

    print(AN)

  test()
