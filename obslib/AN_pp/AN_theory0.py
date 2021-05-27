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


#AN_theory0.py - program to calculate A_N in pp -> hX
#This includes both the fragmentation term and the QS term (see 1701.09170)

flavor = ['g','u','ub','d','db','s','sb']
        #  0   1   2    3    4   5    6
target = ['p']
hadron = ['pi+','pi-','pi0']

flavdict = {'g': 0, 'u': 1, 'ub': 2,'d': 3, 'db': 4, 's': 5, 'sb': 6}

# Common color factors and fractions
c = {'r3': 1. / 3., 'r4': 0.25, 'r6': 1. / 6., 'r8': 0.125,
        'r9': 1. / 9., 'r18': 1. / 18., 'r24': 1. / 24., 'r27': 1. / 27.}

m = {}
Hupol = {}
HQS = {}
f = {}
ft = {}
d = {}
h = {}
H1p = {}
H = {}
HTffa = np.zeros(13)
HTffb = np.zeros(13)
Hxxpz = np.zeros((13, 7))

if 'basis' not in conf:
  conf['basis'] = 'default'

def get_f(x, Q2): # Collinear unpolarized PDF
  return conf['pdf'].get_C(x, Q2)

def get_ft(x, Q2): # Collinear unpolarized PDF
  return conf['pdf'].get_C(x, Q2)

def get_d(z, Q2, had): # Collinear unpolarized FF
  if 'pi' in had:
      return conf['ffpi'].get_C(z, Q2)
  elif 'k' in had:
      return conf['ffk'].get_C(z, Q2)

def get_h(x, Q2): # Collinear transversity
  return conf['transversity'].get_C(x, Q2)

#(H_1^{\perp(1)}(z) - z*dH_1^{\perp(1)}(z)/dz)
def get_H1p(z, Q2, had):
  if 'pi' in had:
      return conf['collinspi'].get_C(z, Q2) - z * conf['dcollinspi'].get_C(z, Q2)
  elif 'k' in had:
      return conf['collinsk'].get_C(z, Q2) - z * conf['dcollinsk'].get_C(z, Q2)

def get_H(z, Q2, had): # -2*z*H_1^{\perp(1)}(z)+\tilde{H}(z)
  if 'pi' in had:
      return -2. * z * conf['collinspi'].get_C(z,Q2) + conf['Htildepi'].get_C(z, Q2)
  elif 'k' in had:
      return -2. * z * conf['collinsk'].get_C(z,Q2) + conf['Htildek'].get_C(z, Q2)

def get_f1Tp(x, Q2): # (f_1T^{\perp(1)}(x) - x*df_1T^{\perp(1)}(x)/dx)
    
    return conf['sivers'].get_C(x, Q2) - x * conf['dsivers'].get_C(x, Q2)

def get_mandelstam(s, t, u):
# Convenient combinations of the partonic Mandelstam variables
   m['s2'] = s * s
   m['s3'] = s**3.
   m['t2'] = t * t
   m['t3'] = t**3.
   m['u2'] = u * u
   m['u3'] = u**3.
   m['ostu'] = 1. / (s * t * u)
   m['os'] = 1. / s
   m['ot'] = 1. / t
   m['ou'] = 1. / u
   m['st'] = s / t
   m['su'] = s / u
   m['ts'] = t / s
   m['tu'] = t / u
   m['us'] = u / s
   m['ut'] = u / t
   m['st2'] = s**2. / t**2.
   m['su2'] = s**2. / u**2.
   m['ts2'] = t**2. / s**2.
   m['tu2'] = t**2. / u**2.
   m['us2'] = u**2. / s**2.
   m['ut2'] = u**2. / t**2.
   m['os2'] = 1. / s**2.
   m['ot2'] = 1. / t**2.
   m['ou2'] = 1. / u**2.
   m['os3'] = 1. / s**3.
   m['ot3'] = 1. / t**3.
   m['ou3'] = 1. / u**3.
   return m

def get_Hupol(m):
  # Hard parts for the unpolarized cross section
   Hupol[1] = 4. * (m['st2'] + m['ut2']) * c['r9']
   Hupol[2] = 4. * (m['su2'] + m['tu2']) * c['r9']
   Hupol[3] = -8. * m['st'] * m['su'] * c['r27']
   Hupol[4] = 4. * (m['ts2'] + m['us2']) * c['r9']
   Hupol[5] = 4. * (m['st2'] + m['ut2']) * c['r9']
   Hupol[6] = -8. * m['ut'] * m['us'] * c['r27']
   Hupol[7] = 4. * (m['ts2'] + m['us2']) * c['r9']
   Hupol[8] = 4. * (m['su2'] + m['tu2']) * c['r9']
   Hupol[9] = -8. * m['tu'] * m['ts'] * c['r27']
   Hupol[10] = 32. * c['r27'] * (m['tu'] + m['ut']) * (1. - 9. * m['ts'] * m['us'] * c['r4'])
   Hupol[11] = 4. * c['r9'] * (- m['su'] - m['us']) * (1. - 9. * m['st'] * m['ut'] * c['r4'])
   Hupol[12] = 4. * c['r9'] * (- m['st'] - m['ts']) * (1. - 9. * m['su'] * m['tu'] * c['r4'])
   Hupol[13] = (m['tu'] + m['ut']) * c['r6'] - 3. * (m['ts2'] + m['us2']) * c['r8']
   Hupol[14] = 4.5 * (3. - m['ts'] * m['us'] - m['st'] * m['ut'] - m['su'] * m['tu'])

   return Hupol

def get_HTffa(m, s, t, u):
  # Hard parts for the transversely polarized fragmentation term
   HTffa[0] = 0
   HTffa[1] = - c['r9'] * m['ot'] + c['r8'] * s * (u - s) * m['ot3'] - m['st2'] * m['ou']
   HTffa[2] = c['r27'] * s * (t - u) * m['ot2'] * m['ou'] + c['r9'] * s * (u - 2. * t) * m['ot3'] + s * m['ot2']
   HTffa[3] = c['r27'] * s * m['ot2'] + c['r9'] * s * (t - s) * m['ot3'] - c['r3'] * m['ot']
   HTffa[4] = c['r27'] * s * m['ot'] * m['ou'] - c['r3'] * m['ot']
   HTffa[5] = c['r9'] * s * (u - 2. * t) * m['ot3'] + s * m['ot2']
   HTffa[6] = c['r9'] * s * (t - s) * m['ot3']
   HTffa[7] = HTffa[1]
   HTffa[8] = HTffa[2]
   HTffa[9] = HTffa[3]
   HTffa[10] = HTffa[4]
   HTffa[11] = HTffa[5]
   HTffa[12] = HTffa[6]
   return HTffa

def get_HTffb(m, s, t, u):
  # Hard parts for the transversely polarized fragmentation term
   HTffb[0] = 0
   HTffb[1] = c['r8'] * s * (u - s) * m['ot3'] + 0.5 * c['r9'] * (s - u) * m['ot'] * m['ou'] + 0.5 * (s - u) * (m['t2'] - 2. * t * u - 2. * m['u2']) * m['ot3'] * m['ou']
   HTffb[2] = c['r27'] * 0.5 * s * (t - 3. * u) * m['ot2'] * m['ou'] - s * u * m['ot3'] + c['r9'] * s * (2. * u - t) * m['ot3'] - c['r3'] * 0.5 * m['s2'] * m['ot2'] * m['ou']
   HTffb[3] = c['r27'] * 0.5 * (3. * s - t) * m['ot2'] + m['s2'] * m['ot3'] + c['r9'] * s * (t - 2. * s) * m['ot3'] + c['r3'] * 0.5 * u * m['ot2']
   HTffb[4] = 10. * c['r27'] * 0.5 * (s - u) * m['ot'] * m['ou']
   HTffb[5] = c['r9'] * s * (2. * u - t) * m['ot3'] - s * u * m['ot3']
   HTffb[6] = c['r9'] * s * (t - 2. * s) * m['ot3'] + m['s2'] * m['ot3']
   HTffb[7] = HTffb[1]
   HTffb[8] = HTffb[2]
   HTffb[9] = HTffb[3]
   HTffb[10] = HTffb[4]
   HTffb[11] = HTffb[5]
   HTffb[12] = HTffb[6]
   return HTffb

def get_Hxxpz(z, Q2, had, m, s, t, u):
  HTffa = get_HTffa(m, s, t, u)
  HTffb = get_HTffb(m, s, t, u)

  if had=='jet':
      #These are dummy formulas so we don't get a runtime warning
      #We set the frag cross section to zero for jet
      H1p=np.ones(11)
      H=np.ones(11)
  else:
      H1p = get_H1p(z, Q2, 'pi+')
      H = get_H(z, Q2, 'pi+')

  if had.endswith('-'):
      H1p = conf['aux'].charge_conj(H1p)
      H = conf['aux'].charge_conj(H)

  elif had.endswith('0'):
      H1pp=H1p
      H1pm=conf['aux'].charge_conj(H1p)
      Hp=H
      Hm=conf['aux'].charge_conj(H)

      H1p=0.5*(H1pp+H1pm)
      #print z,2.0*z**2*0.135*H1pp,2.0*z**2*0.135*H1pm,2.0*z**2*0.135*H1p
      #sys.exit()
      H=0.5*(Hp+Hm)

  #print had,z,H1p[1],H1p[3]

  Hxxpz = np.einsum('i,j->ij', HTffa, H1p) + np.einsum('i,j->ij', HTffb, H) / z
  return Hxxpz

def get_HQS(m): #Note there is a 1/u in each hard factor compared to KQVY 2006
    fsi = 1. + m['ut']
    HQS[0] = 0
    HQS[1] = -m['ou']*(2.+fsi)*(m['st2']+m['ut2'])*c['r18']

    HQS[2] = -m['ou']*(2.-7.*fsi)*(m['su2']+m['tu2'])*c['r18']
    HQS[3] = -m['ou']*(-10.-fsi)*m['st']*m['su']*c['r27']

    HQS[4] = -m['ou']*(7.+fsi)*(m['st2']+m['ut2'])*c['r18']
    HQS[5] = -m['ou']*(-1. -7.*fsi)*(m['us2']+m['ts2'])*c['r18']

    HQS[6] = -m['ou']*(-1.-fsi)*m['us']*m['ut']*c['r27']

    HQS[7] = -m['ou']*(7.-2.*fsi)*(m['su2']+m['tu2'])*c['r18']
    HQS[8] = -m['ou']*(-1. -2.*fsi)*(m['us2']+m['ts2'])*c['r18']
    HQS[9] = -m['ou']*(-1. -fsi)*m['ts']*m['tu']*c['r27']

    HQS[10] = -m['ou']*c['r6']*c['r9']*(m['tu']+m['ut'])*(1.+18.*m['ts']*m['us'])-m['ou']*fsi*c['r6']*(m['tu']+m['ut'])*(1.-9.*(m['us'])*(m['us']))

    HQS[11] = -m['ou']*c['r4']*c['r4']*(m['su']+m['us'])*(1.-9.*m['ut']*m['ut'])-m['ou']*fsi*c['r8']*c['r18']*(m['su']+m['us'])*(1.+18.*m['st']*m['ut'])

    HQS[12] = -m['ou']*c['r4']*c['r4']*(m['ts']+m['st'])*(1.-9.*m['tu']*m['tu']) + m['ou']*fsi*c['r4']*c['r4']*(m['ts']+m['st'])*(1.-9.*m['su']*m['su'])

    return HQS

#  @profile
# Calculation of the unpolarized cross section
def get_dsig(x, z, xF, pT, rs, tar, had):

  M = conf['aux'].M
  Mh = {}
  Mh['pi+'] = conf['aux'].Mpi
  Mh['pi-'] = conf['aux'].Mpi
  Mh['pi0'] = conf['aux'].Mpi
  Mh['k+'] = conf['aux'].Mk
  Mh['k-'] = conf['aux'].Mk
  Mh['jet']=1 #This is a dummy formula so we don't get a runtime error

  if pT > 1.:
    Q = pT
  else:
    Q = 1.

  Q2 = Q * Q

  xT = 2. * pT / rs
  xT2 = xT * xT
  xF2 = xF * xF

  # Mandelstam variables at the hadron level
  ss = rs * rs
  tt = -0.5 * ss * (np.sqrt(xF2 + xT2) - xF)
  uu = -0.5 * ss * (np.sqrt(xF2 + xT2) + xF)

  oz = 1. / z

  xp = -x * tt / (z * x * ss + uu)

  # Mandelstam variables at the parton level
  s = x * xp * ss
  t = x * tt * oz
  u = xp * uu * oz

  # Prefactor
  denfac = 1. / ((z * z * x * ss + uu * z) * x * xp)

  m=get_mandelstam(s, t, u)
  Hupol=get_Hupol(m)

  Hupol1 = Hupol[1]
  Hupol2 = Hupol[2]
  Hupol3 = Hupol[3]
  Hupol4 = Hupol[4]
  Hupol5 = Hupol[5]
  Hupol6 = Hupol[6]
  Hupol7 = Hupol[7]
  Hupol8 = Hupol[8]
  Hupol9 = Hupol[9]
  Hupol10 = Hupol[10]
  Hupol11 = Hupol[11]
  Hupol12 = Hupol[12]
  Hupol13 = Hupol[13]
  Hupol14 = Hupol[14]

  # Get arrays of the nonperturbative functions
  #print x,xp
  f = get_f(x, Q2)
  ft = get_ft(xp, Q2)

  if had=='jet': d=np.ones(11)
  else: d = get_d(z, Q2, 'pi+')

  if had.endswith('-'):
      d = conf['aux'].charge_conj(d)

  elif had.endswith('0'):
      dp=d
      dm=conf['aux'].charge_conj(d)
      d=0.5*(dp+dm)
      #print z,z*dp,z*dm,z*d

  fg = f[0]
  fu = f[1]
  fub = f[2]
  fd = f[3]
  fdb = f[4]
  fs = f[5]
  fsb = f[6]

  ftg = ft[0]
  ftu = ft[1]
  ftub = ft[2]
  ftd = ft[3]
  ftdb = ft[4]
  fts = ft[5]
  ftsb = ft[6]

  dg = d[0]
  du = d[1]
  dub = d[2]
  dd = d[3]
  ddb = d[4]
  ds = d[5]
  dsb = d[6]

  upol = 0

  upol += (fu * du + fd * dd + fs * ds) * (ftu + ftd + fts) * Hupol1
  + (fu + fd + fs) * (ftu * du + ftd * dd + fts * ds) * Hupol2
  + (fu * ftu * du + fd * ftd * dd + fs * fts * ds) * Hupol3

  upol += (fub * dub + fdb * ddb + fsb * dsb) * (ftub + ftdb + ftsb) * Hupol1
  + (fub + fdb + fsb) * (ftub * dub + ftdb * ddb + ftsb * dsb) * Hupol2
  + (fub * ftub * dub + fdb * ftdb * ddb + fsb * ftsb * dsb) * Hupol3

  upol += (fu * du + fd * dd + fs * ds) * (ftub + ftdb + ftsb) * Hupol5
  + (fu * ftub + fd * ftdb + fs * ftsb) * (du + dd + ds) * Hupol4
  + (fu * ftub * du + fd * ftdb * dd + fs * ftsb * ds) * Hupol6

  upol += (fub * dub + fdb * ddb + fsb * dsb) * (ftu + ftd + fts) * Hupol5
  + (fub * ftu + fdb * ftd + fsb * fts) * (dub + ddb + dsb) * Hupol4
  + (fub * ftu * dub + fdb * ftd * ddb + fsb * fts * dsb) * Hupol6

  upol += (fu + fd + fs) * (ftub * dub + ftdb * ddb + ftsb * dsb) * Hupol8
  + (fu * ftub + fd * ftdb + fs * ftsb) * (dub + ddb + dsb) * Hupol7
  + (fu * ftub * dub + fd * ftdb * ddb + fs * ftsb * dsb) * Hupol9

  upol += (fub + fdb + fsb) * (ftu * du + ftd * dd + fts * ds) * Hupol8
  + (fub * ftu + fdb * ftd + fsb * fts) * (du + dd + ds) * Hupol7
  + (fub * ftu * du + fdb * ftd * dd + fsb * fts * ds) * Hupol9

  upol += (fu * ftub + fd * ftdb + fs * ftsb) * dg * Hupol10

  upol += (fub * ftu + fdb * ftd + fsb * fts) * dg * Hupol10

  upol += (fu * du + fd * dd + fs * ds) * ftg * Hupol11

  upol += (fub * dub + fdb * ddb + fsb * dsb) * ftg * Hupol11

  upol += (fu + fd + fs) * ftg * dg * Hupol12

  upol += (fub + fdb + fsb) * ftg * dg * Hupol12

  upol += fg * ftg * (du + dd + ds) * Hupol13

  upol += fg * ftg * (dub + ddb + dsb) * Hupol13

  upol += fg * ftg * dg * Hupol14

  upol += fg * (ftu * du + ftd * dd + fts * ds) * Hupol12

  upol += fg * (ftub * dub + ftdb * ddb + ftsb * dsb) * Hupol12

  upol += fg * (ftu + ftd + fts) * dg * Hupol11

  upol += fg * (ftub + ftdb + ftsb) * dg * Hupol11

  return denfac * upol

#  @profile
# Calculation of the fragmentation term in the transversely polarized cross section
def get_dsigST(x, z, xF, pT, rs, tar, had):

  M = conf['aux'].M
  Mh = {}
  Mh['pi+'] = conf['aux'].Mpi
  Mh['pi-'] = conf['aux'].Mpi
  Mh['pi0'] = conf['aux'].Mpi
  Mh['k+'] = conf['aux'].Mk
  Mh['k-'] = conf['aux'].Mk
  Mh['jet']= 1 #This is a dummy formula so we don't get a runtime error

  Mh = Mh[had]

  if pT > 1.:
    Q = pT
  else:
    Q = 1.

  Q2 = Q * Q

  xT = 2. * pT / rs
  xT2 = xT * xT
  xF2 = xF * xF

  # Mandelstam variables at the hadron level
  ss = rs * rs
  tt = -0.5 * ss * (np.sqrt(xF2 + xT2) - xF)
  uu = -0.5 * ss * (np.sqrt(xF2 + xT2) + xF)

  oz = 1. / z

  xp = -x * tt / (z * x * ss + uu)

  # Mandelstam variables at the parton level
  s = x * xp * ss
  t = x * tt * oz
  u = xp * uu * oz

  # Prefactor
  numfac = oz * (1. / ((z * z * x * ss + uu * z) * x * xp))

  m=get_mandelstam(s, t, u)

  # Get arrays of the nonperturbative functions
  f = get_f(x, Q2)
  ft = get_ft(xp, Q2)
  h = get_h(x, Q2)
  f1Tp = get_f1Tp(x, Q2)
  Hxxpz = get_Hxxpz(z, Q2, had, m, s, t, u)

  if had=='jet': d=np.ones(11)
  else: d = get_d(z, Q2, 'pi+')

  if had.endswith('-'):
      d = conf['aux'].charge_conj(d)

  elif had.endswith('0'):
      dp=d
      dm=conf['aux'].charge_conj(d)
      d=0.5*(dp+dm)

  hg = h[0]
  hu = h[1]
  hub = h[2]
  hd = h[3]
  hdb = h[4]
  hs = h[5]
  hsb = h[6]

  ftg = ft[0]
  ftu = ft[1]
  ftub = ft[2]
  ftd = ft[3]
  ftdb = ft[4]
  fts = ft[5]
  ftsb = ft[6]

  fg = f[0]
  fu = f[1]
  fub = f[2]
  fd = f[3]
  fdb = f[4]
  fs = f[5]
  fsb = f[6]

  dg = d[0]
  du = d[1]
  dub = d[2]
  dd = d[3]
  ddb = d[4]
  ds = d[5]
  dsb = d[6]

  uQS = f1Tp[1]
  ubQS = f1Tp[2]
  dQS = f1Tp[3]
  dbQS = f1Tp[4]
  sQS = f1Tp[5]
  sbQS = f1Tp[6]

  #Fragmentation term

  Hxxpz1u = Hxxpz[1][1]
  Hxxpz1d = Hxxpz[1][3]
  Hxxpz1s = Hxxpz[1][5]
  Hxxpz2u = Hxxpz[2][1]
  Hxxpz2d = Hxxpz[2][3]
  Hxxpz2s = Hxxpz[2][5]
  Hxxpz3u = Hxxpz[3][1]
  Hxxpz3d = Hxxpz[3][3]
  Hxxpz3s = Hxxpz[3][5]
  Hxxpz4u = Hxxpz[4][1]
  Hxxpz4d = Hxxpz[4][3]
  Hxxpz4s = Hxxpz[4][5]
  Hxxpz5u = Hxxpz[5][1]
  Hxxpz5d = Hxxpz[5][3]
  Hxxpz5s = Hxxpz[5][5]
  Hxxpz6u = Hxxpz[6][1]
  Hxxpz6d = Hxxpz[6][3]
  Hxxpz6s = Hxxpz[6][5]

  Hxxpz7ub = Hxxpz[7][2]
  Hxxpz7db = Hxxpz[7][4]
  Hxxpz7sb = Hxxpz[7][6]
  Hxxpz8ub = Hxxpz[8][2]
  Hxxpz8db = Hxxpz[8][4]
  Hxxpz8sb = Hxxpz[8][6]
  Hxxpz9ub = Hxxpz[9][2]
  Hxxpz9db = Hxxpz[9][4]
  Hxxpz9sb = Hxxpz[9][6]
  Hxxpz10ub = Hxxpz[10][2]
  Hxxpz10db = Hxxpz[10][4]
  Hxxpz10sb = Hxxpz[10][6]
  Hxxpz11ub = Hxxpz[11][2]
  Hxxpz11db = Hxxpz[11][4]
  Hxxpz11sb = Hxxpz[11][6]
  Hxxpz12ub = Hxxpz[12][2]
  Hxxpz12db = Hxxpz[12][4]
  Hxxpz12sb = Hxxpz[12][6]

  ffcs = 0

  ffcs += ftg * (hu * Hxxpz1u + hd * Hxxpz1d + hs * Hxxpz1s)

  ffcs += (hu * ftu * Hxxpz2u) + (hd * ftd * Hxxpz2d) + (hs * fts * Hxxpz2s)

  ffcs += (hu * ftub * Hxxpz3u) + (hd * ftdb * Hxxpz3d) + (hs * ftsb * Hxxpz3s)

  ffcs += (hub * ftu * Hxxpz4u) + (hdb * ftd * Hxxpz4d) + (hsb * fts * Hxxpz4s)

  ffcs += ftu * (hd * Hxxpz5d + hs * Hxxpz5s) + ftd * (hu * Hxxpz5u + hs * Hxxpz5s) + fts * (hu * Hxxpz5u + hd * Hxxpz5d)

  ffcs += ftub * (hd * Hxxpz6d + hs * Hxxpz6s) + ftdb * (hu * Hxxpz6u + hs * Hxxpz6s) + ftsb * (hu * Hxxpz6u + hd * Hxxpz6d)

  ffcs += ftg * (hub * Hxxpz7ub + hdb * Hxxpz7db + hsb * Hxxpz7sb)

  ffcs += (hub * ftub * Hxxpz8ub) + (hdb * ftdb * Hxxpz8db) + (hsb * ftsb * Hxxpz8sb)

  ffcs += (hub * ftu * Hxxpz9ub) + (hdb * ftd * Hxxpz9db) + (hsb * fts * Hxxpz9sb)

  ffcs += (hu * ftub * Hxxpz10ub) + (hd * ftdb * Hxxpz10db) + (hs * ftsb * Hxxpz10sb)

  ffcs += ftub * (hdb * Hxxpz11db + hsb * Hxxpz11sb) + ftdb * (hub * Hxxpz11ub + hsb * Hxxpz11sb) + fts * (hub * Hxxpz11ub + hdb * Hxxpz11db)

  ffcs += ftu * (hdb * Hxxpz12db + hsb * Hxxpz12sb) + ftd * (hub * Hxxpz12ub + hsb * Hxxpz12sb) + fts * (hub * Hxxpz12ub + hdb * Hxxpz12db)

  ffcs = 2. * Mh * pT * numfac * ffcs

  if had=='jet': ffcs=0.0


  #Qiu-Sterman term

  HQS = get_HQS(m)
  sig1 = HQS[1]
  sig2 = HQS[2]
  sig3 = HQS[3]
  sig4 = HQS[4]
  sig5 = HQS[5]
  sig6 = HQS[6]
  sig7 = HQS[7]
  sig8 = HQS[8]
  sig9 = HQS[9]
  sig10 = HQS[10]
  sig11 = HQS[11]
  sig12 = HQS[12]

  QScs = 0

  QScs += (uQS*du +dQS*dd +sQS*ds)*(ftu+ftd+fts)*sig1 + (uQS + dQS +sQS)*(ftu*du+ftd*dd+fts*ds)*sig2 + (uQS*ftu*du+dQS*ftd*dd+sQS*fts*ds)*sig3

  QScs += (ubQS*dub + dbQS* ddb + sbQS*dsb)*(ftub+ftdb+ftsb)*sig1 + (ubQS+dbQS+sbQS)*(ftub*dub+ftdb*ddb+ftsb*dsb)*sig2 + (ubQS*ftub*dub+dbQS*ftdb*ddb+sbQS*ftsb*dsb)*sig3

  QScs += (uQS*du + dQS*dd+ sQS*ds)*(ftub + ftdb +ftsb)*sig4 + (uQS*ftub+dQS*ftdb+sQS*fts)*(du+dd+ds)*sig5 + (uQS*ftub*du+dQS*ftdb*dd+sQS*ftsb*ds)*sig6

  QScs += (ubQS*dub + dbQS*ddb+sbQS*dsb)*(ftu+ftd+fts)*sig4 + (ubQS*ftu + dbQS*ftd + sbQS*fts)*(dub + ddb +dsb)*sig5 + (ubQS*ftu*dub+dbQS*ftd*ddb+sbQS*fts*dsb)*sig6

  QScs += (uQS +dQS +sQS)*(ftub*dub + ftdb*ddb + ftsb*dsb)*sig7 + (uQS*ftub + dQS*ftdb+sQS*ftsb)*(dub + ddb + dsb)*sig8 + (uQS*ftub*dub+dQS*ftdb*ddb+sQS*ftsb*dsb)*sig9

  QScs += (ubQS +dQS + sbQS)*(ftu*du+ftdb*ddb+ftsb*dsb)*sig7 + (ubQS*ftu+dbQS*ftd+sbQS*fts)*(du+dd+ds)*sig8 +(ubQS*ftu*du+dbQS*ftd*dd+sbQS*fts*ds)*sig9

  QScs += (uQS*ftub+dQS*ftdb +sQS*ftsb)*dg*sig10

  QScs += (ubQS*ftu + dbQS*ftd + sbQS*fts)*dg*sig10

  QScs += (uQS*du + dQS*dd + sQS*ds)*ftg*sig11

  QScs += (ubQS*dub + dbQS*ddb +sbQS*dsb)*ftg*sig11

  QScs += (uQS + dQS +sQS) *ftg *dg*sig12

  QScs += (ubQS+dbQS+sbQS)*ftg*dg*sig12

  QScs= 2. * pT * M * numfac * QScs #Note there is a 1/u in the hard factors

  return ffcs + QScs
  #return ffcs
  #return  QScs

def get_sig(xF, pT, rs, tar, had, mode='gauss', nx=10, nz=10):
    xT = 2. * pT / rs
    xF2 = xF * xF
    xT2 = xT * xT

    # Mandelstam variables at the hadron level
    ss = rs * rs
    tt = -0.5 * ss * (np.sqrt(xF2 + xT2) - xF)
    uu = -0.5 * ss * (np.sqrt(xF2 + xT2) + xF)

    # Lower limits of the z and x integrations
    zmin = np.sqrt(xF2 + xT2)

    def xmin(z): return -uu / (z * ss + tt)

    if had=='jet':
        z = 1.0
        xmin = -uu / (ss + tt)
        dsig = np.vectorize(lambda x: get_dsig(x, z, xF, pT, rs, tar, had))
        sig = fixed_quad(dsig, xmin, 1, n=nx)[0]
    else:
        if mode == 'gauss':
            dsigdzdx = np.vectorize(lambda x, z: get_dsig(x, z, xF, pT, rs, tar, had))
            dsigdz = np.vectorize(lambda z: fixed_quad(lambda x: dsigdzdx(x, z), xmin(z), 1., n=nx)[0])
            sig = fixed_quad(dsigdz, zmin, 1., n=nz)[0]
        elif mode == 'quad':
            sig = dblquad(lambda x, z: get_dsig(x, z, xF, pT, rs, tar, had), zmin, 1., xmin, lambda x: 1.)[0]
    return sig

def get_sigST(xF, pT, rs, tar, had, mode='gauss', nx=10, nz=10):
    xT = 2. * pT / rs
    xF2 = xF * xF
    xT2 = xT * xT

    # Mandelstam variables at the hadron level
    ss = rs * rs
    tt = -0.5 * ss * (np.sqrt(xF2 + xT2) - xF)
    uu = -0.5 * ss * (np.sqrt(xF2 + xT2) + xF)

    # Lower limits of the z and x integrations
    zmin = np.sqrt(xF2 + xT2)

    def xmin(z): return -uu / (z * ss + tt)

    if had=='jet':
        z = 1.0
        xmin = -uu / (ss + tt)
        dsig=np.vectorize(lambda x: get_dsigST(x, z, xF, pT, rs, tar, had))
        sig = fixed_quad(dsig, xmin, 1, n=nx)[0]
    else:
        if mode == 'gauss':
            dsigdzdx = np.vectorize(lambda x, z: get_dsigST(x, z, xF, pT, rs, tar, had))
            dsigdz = np.vectorize(lambda z: fixed_quad(lambda x: dsigdzdx(x, z), xmin(z), 1., n=nx)[0])
            sig = fixed_quad(dsigdz, zmin, 1., n=nz)[0]
        elif mode == 'quad':
            sig = dblquad(lambda x, z: get_dsigST(x, z, xF, pT, rs, tar, had), zmin, 1., xmin, lambda x: 1.)[0]

    #print had,sig
    return sig


if __name__ == '__main__':


  from qcdlib.ff0 import FF as FF0
  from qcdlib.ff1 import FF as FF1
  from qcdlib.pdf0 import PDF as PDF0
  from qcdlib.pdf1 import PDF as PDF1
  conf['aux']= AUX()
  conf['pdf']=PDF0()
  conf['collinspi']=FF1('pi')
  conf['collinsk']=FF1('k')
  conf['dcollinspi']=FF1('pi','deriv')
  conf['dcollinsk']=FF1('k','deriv')
  conf['Htildepi']=FF1('pi')
  conf['Htildek']=FF1('k')
  conf['transversity']=PDF1()
  conf['sivers']=PDF1()
  conf['dsivers']=PDF1('deriv')
  conf['ffpi']=FF0('pi')
  conf['ffk']=FF0('k')

  rs = 200.
  tar = 'p'
  #had = 'pi+'
  had='jet'
  pT = 3.0
  xF = 0.2375
  xT = 2. * pT / rs
  xF2 = xF * xF
  xT2 = xT * xT

  def test():
    den = get_sig(xF, pT, rs, tar, had, mode='gauss', nx=10, nz=10)
    num = get_sigST(xF, pT, rs, tar, had,
               mode='gauss', nx=10, nz=10)

    AN = num / den
    print AN

  test()

# from timeit import Timer
# t = Timer("test()", "from __main__ import test")
# print 't elapsed ',t.timeit(number=1)

# def test2():
#  den = anthy.get_dsig(0.3,0.6,xF,pT,rs,tar,had)
#  num = anthy.get_dsigST(0.3,0.6,xF,pT,rs,tar,had)
#
#  print den,num
#
# from timeit import Timer
# t = Timer("test2()", "from __main__ import test2")
# print 't elapsed ',t.timeit(number=1)

# start = time.time()
# print anthy.get_dsig(0.3,0.6,xF,pT,rs,tar,had)
# print anthy.get_dsigST(0.3,0.6,xF,pT,rs,tar,had)
# end = time.time()
# print 'time=',(end-start)

#  start = time.time()
#  test()
#  end = time.time()
#  print 'time=', (end - start)

  # Integration of the numerator from xmin to 1 and from zmin to 1 (the values for xmin and zmin are above)

  # Integration of the denominator from xmin to 1 and from zmin to 1 (the values for xmin and zmin are above)
  #den = dblquad(lambda x,z: ANTHEORY().get_dsig(x,z,xF,pT,rs,tar,had),zmin,1.,xmin,lambda x: 1.)

  #AN = num[0]/den[0]
  # print(AN)
