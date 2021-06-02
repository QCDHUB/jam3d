#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import pandas as pd
import math
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf
from scipy.integrate import quad
import matplotlib.pyplot as plt


###########
conf['tmc'] = False
###########


#AN_theory0.py - program to calculate A_N in ep -> hX (see 1407.5078, 1701.09170)

flavor = ['g','u','ub','d','db','s','sb']
        #  0   1   2    3    4   5    6
target = ['p']
hadron = ['pi+','pi-']

flavdict = {'g': 0, 'u': 1, 'ub': 2,'d': 3, 'db': 4, 's': 5, 'sb': 6}

eu2, ed2 = 4/9., 1/9.
e2 = []
e2.append(0)    # g
e2.append(eu2)  # u
e2.append(eu2)  # ub
e2.append(ed2)  # d
e2.append(ed2)  # db
e2.append(ed2)  # s
e2.append(ed2)  # sb
e2.append(0)    # c
e2.append(0)    # cb
e2.append(0)    # b
e2.append(0)    # bb
e2 = np.array(e2)

f = {}
d = {}
h = {}
H1p = {}
H = {}
f1Tp = {}

if 'basis' not in conf:
  conf['basis'] = 'default'

def get_f(x, Q2): # Collinear unpolarized PDF
  return conf['pdf'].get_C(x, Q2)

def get_d(z, Q2, had): # Collinear unpolarized FF
  if 'pi' in had:
      return conf['ffpi'].get_C(z, Q2)
  elif 'k' in had:
      return conf['ffk'].get_C(z, Q2)

def get_h(x, Q2): # Collinear transversity
  return conf['transversity'].get_C(x, Q2)

def get_H1p(z, Q2, had): # (H_1^{\perp(1)}(z) - z*dH_1^{\perp(1)}(z)/dz)
    if 'pi' in had:
        return conf['collinspi'].get_C(z, Q2) - z * conf['dcollinspi'].get_C(z, Q2)
    elif 'k' in had:
        return conf['collinsk'].get_C(z, Q2) - z * conf['dcollinsk'].get_C(z, Q2)

def get_H(z, Q2, had): # -2*z*H_1^{\perp(1)}(z)+\tilde{H}(z)
  if 'pi' in had:
      return -2. * z * conf['collinspi'].get_C(z,Q2) - conf['Htildepi'].get_C(z, Q2)
  elif 'k' in had:
      return -2. * z * conf['collinsk'].get_C(z,Q2) - conf['Htildek'].get_C(z, Q2)

def get_f1Tp(x, Q2): # (f_1T^{\perp(1)}(x) - x*df_1T^{\perp(1)}(x)/dx)
    return conf['sivers'].get_C(x, Q2) - x * conf['dsivers'].get_C(x, Q2)

class Class_Variables():    #Declaring all the class methods that are referenced throughout
    @classmethod
    def S_value(cls, rs):
        return rs**2
    @classmethod
    def T_value(cls, rs, pT, xF):
        return (-1 * rs) * math.sqrt((pT**2) + (xF**2 * 0.25 * CV.S_value(rs))) + (0.5 * xF * CV.S_value(rs))
    @classmethod
    def U_value(cls, rs, pT, xF):
        return (-1 * rs) * math.sqrt((pT**2) + (xF**2 * 0.25 * CV.S_value(rs))) - (0.5 * xF * CV.S_value(rs))
    @classmethod
    def Q2_value(cls, pT):
        return pT**2
    @classmethod
    def zmin_value(cls, rs, pT, xF): #zmin
        return (-1 * (CV.T_value(rs, pT, xF) + CV.U_value(rs, pT, xF))) / CV.S_value(rs)
    @classmethod
    def x_value(cls, z, rs, pT, xF): #x
        return (-1 * CV.U_value(rs, pT, xF) / z) / (CV.S_value(rs) + (CV.T_value(rs, pT, xF) / z))
    @classmethod
    def ss_value(cls, z, rs, pT, xF): #s
        return CV.x_value(z, rs, pT, xF)*CV.S_value(rs)
    @classmethod
    def tt_value(cls, z, rs, pT, xF): #t
        return (CV.x_value(z, rs, pT, xF) * CV.T_value(rs, pT, xF)) / z
    @classmethod
    def uu_value(cls, z, rs, pT, xF): #u
        return CV.U_value(rs, pT, xF) / z

class Class_Variables_TMC():    #Declaring all the class methods that are referenced throughout
    @classmethod
    def S_value(cls, rs):
        return rs**2
    @classmethod
    def T_value(cls, rs, pT, xF):
        return (conf['aux'].Mpi**2) + 0.5 *(((conf['aux'].M**2)*(((-math.sqrt(4.0 * ((conf['aux'].Mpi**2) + (pT**2)) + (xF*xF*CV.S_value(rs))))/rs) - xF + 2.0))-(rs * math.sqrt(4.0*((conf['aux'].Mpi**2) + (pT**2)) + (xF*xF*CV.S_value(rs)))) + (xF*CV.S_value(rs)))
    @classmethod
    def U_value(cls, rs, pT, xF):
        return (conf['aux'].Mpi**2) - (((CV.S_value(rs) - (conf['aux'].M**2))/(2.0 * rs)) * (math.sqrt(4.0 * ((conf['aux'].Mpi**2) + (pT**2)) + (xF*xF*CV.S_value(rs))) + (xF * rs)))
    @classmethod
    def Q2_value(cls, pT):
        return pT**2
    @classmethod
    def zmin_value(cls, rs, pT, xF): #zmin
        return (-1.0 * (CV.T_value(rs, pT, xF) + CV.U_value(rs, pT, xF))) / CV.S_value(rs)
    @classmethod
    def x_value(cls, z, rs, pT, xF): #x
        return (-1.0 * CV.U_value(rs, pT, xF) / z) / (CV.S_value(rs) + (CV.T_value(rs, pT, xF) / z))
    @classmethod
    def ss_value(cls, z, rs, pT, xF): #s
        return CV.x_value(z, rs, pT, xF)*(CV.S_value(rs)-(conf['aux'].M**2))
    @classmethod
    def tt_value(cls, z, rs, pT, xF): #t
        if CV.T_value(rs, pT, xF) > 0:
            return (CV.x_value(z, rs, pT, xF)/(2.0*z))*(CV.T_value(rs, pT, xF) - (conf['aux'].M**2) - (conf['aux'].Mpi**2) + math.sqrt((conf['aux'].M**4) - ((2.0 * (conf['aux'].M**2)) * ((conf['aux'].Mpi**2) + (2.0 * pT * pT) + CV.T_value(rs, pT, xF))) + (((conf['aux'].Mpi**2) - CV.T_value(rs, pT, xF))**2)))
        elif CV.T_value(rs, pT, xF) < 0:
            return (CV.x_value(z, rs, pT, xF)/(2.0*z))*(CV.T_value(rs, pT, xF) - (conf['aux'].M**2) - (conf['aux'].Mpi**2) - math.sqrt((conf['aux'].M**4) - ((2.0 * (conf['aux'].M**2)) * ((conf['aux'].Mpi**2) + (2.0 * pT * pT) + CV.T_value(rs, pT, xF))) + (((conf['aux'].Mpi**2) - CV.T_value(rs, pT, xF))**2)))
    @classmethod
    def uu_value(cls, z, rs, pT, xF): #u
        return ((pT**2)*(CV.U_value(rs, pT, xF) - (conf['aux'].Mpi**2))) / (z * ((conf['aux'].Mpi**2) + (pT**2)))



if conf['tmc'] == False:
    CV = Class_Variables() #declare Class_Variables as a variable in order to utilize class methods
elif conf['tmc'] == True:
    CV = Class_Variables_TMC()



def get_frag(z, xF, pT, rs, tar, had):#Code for fragmentation of polarized cross-section equation
    if tar == 'p':
        h = get_h(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT))
    elif tar == 'n':
        h = conf['aux'].p2n(get_h(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT)))

    if had.endswith('+'):
        had = had.strip('+')
        H1p = get_H1p(z, CV.Q2_value(pT), had)
        H = get_H(z, CV.Q2_value(pT), had)
    elif had.endswith('-'):
        had = had.strip('-')
        H1p = conf['aux'].charge_conj(get_H1p(z, CV.Q2_value(pT), had))
        H = conf['aux'].charge_conj(get_H(z, CV.Q2_value(pT), had))
    elif had.endswith('0'):
        had = had.strip('0')
        plusH1p = get_H1p(z, CV.Q2_value(pT), had)
        minusH1p = conf['aux'].charge_conj(get_H1p(z, CV.Q2_value(pT), had))
        H1p = 0.5 * (plusH1p + minusH1p)

        plusH = get_H(z, CV.Q2_value(pT), had)
        minusH = conf['aux'].charge_conj(get_H(z, CV.Q2_value(pT), had))
        H = 0.5 * (plusH + minusH)

    return (1/(z**3)) * (1/CV.x_value(z, rs, pT, xF)) * ((-1 * 4 * pT) / (CV.S_value(rs) + (CV.T_value(rs, pT, xF)/z))) * np.sum(e2 * ((conf['aux'].Mpi / CV.tt_value(z, rs, pT, xF)) * h * (H1p * ((CV.ss_value(z, rs, pT, xF)*CV.uu_value(z, rs, pT, xF))/(CV.tt_value(z, rs, pT, xF)**2)) + (1/z)*H * ((CV.ss_value(z, rs, pT, xF)/(CV.tt_value(z, rs, pT, xF)**2))*(CV.uu_value(z, rs, pT, xF)-CV.ss_value(z, rs, pT, xF))))))

#Code for generic values for AN
#Code to create equation for unpolarized cross-section
def get_unp(z, xF, pT, rs, tar, had):
    if tar == 'p':
        f = get_f(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT))
    elif tar == 'n':
        f = conf['aux'].p2n(get_f(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT)))

    if had.endswith('+'):
        had = had.strip('+')
        d = get_d(z, CV.Q2_value(pT), had)
    elif had.endswith('-'):
        had = had.strip('-')
        d = conf['aux'].charge_conj(get_d(z, CV.Q2_value(pT), had))
    elif had.endswith('0'):
        had = had.strip('0')
        plus = get_d(z, CV.Q2_value(pT), had)
        minus = conf['aux'].charge_conj(get_d(z, CV.Q2_value(pT), had))
        d = 0.5 * (plus + minus)

    return (1/(z**2)) * (1/CV.x_value(z, rs, pT, xF)) * (1/(CV.S_value(rs) + (CV.T_value(rs, pT, xF)/z))) * np.sum(e2 * f * d * ((CV.ss_value(z, rs, pT, xF)**2 + CV.uu_value(z, rs, pT, xF)**2) / (CV.tt_value(z, rs, pT, xF)**2)))

#z-integration for unpolarized cross-section
def get_denom(xF, pT, rs, tar, had):
    return quad(lambda z: get_unp(z, xF, pT, rs, tar, had), CV.zmin_value(rs, pT, xF), 1, limit = 150)[0]

#Code to create eqation for polarized cross-section
def get_pol(z, xF, pT, rs, tar, had):
    if tar == 'p':
        f = get_f(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT))
        f1Tp = get_f1Tp(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT))
        h = get_h(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT))
    elif tar == 'n':
        f = conf['aux'].p2n(get_f(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT)))
        f1Tp = conf['aux'].p2n(get_f1Tp(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT)))
        h = conf['aux'].p2n(get_h(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT)))

    if had.endswith('+'):
        had = had.strip('+')
        d = get_d(z, CV.Q2_value(pT), had)
        H1p = get_H1p(z, CV.Q2_value(pT), had)
        H = get_H(z, CV.Q2_value(pT), had)
    elif had.endswith('-'):
        had = had.strip('-')
        d = conf['aux'].charge_conj(get_d(z, CV.Q2_value(pT), had))
        H1p = conf['aux'].charge_conj(get_H1p(z, CV.Q2_value(pT), had))
        H = conf['aux'].charge_conj(get_H(z, CV.Q2_value(pT), had))
    elif had.endswith('0'):
        had = had.strip('0')
        plusd = get_d(z, CV.Q2_value(pT), had)
        minusd = conf['aux'].charge_conj(get_d(z, CV.Q2_value(pT), had))
        d = 0.5 * (plusd + minusd)

        plusH1p = get_H1p(z, CV.Q2_value(pT), had)
        minusH1p = conf['aux'].charge_conj(get_H1p(z, CV.Q2_value(pT), had))
        H1p = 0.5 * (plusH1p + minusH1p)

        plusH = get_H(z, CV.Q2_value(pT), had)
        minusH = conf['aux'].charge_conj(get_H(z, CV.Q2_value(pT), had))
        H = 0.5 * (plusH + minusH)

    return (1/(z**3)) * (1/CV.x_value(z, rs, pT, xF)) * ((-1 * 4 * pT) / (CV.S_value(rs) + (CV.T_value(rs, pT, xF)/z))) * np.sum(e2 * ((conf['aux'].M / CV.uu_value(z, rs, pT, xF)) * d * f1Tp * (0.5 * CV.ss_value(z, rs, pT, xF) *(CV.ss_value(z, rs, pT, xF)**2 + CV.uu_value(z, rs, pT, xF)**2) / (CV.tt_value(z, rs, pT, xF)**3)) + (conf['aux'].Mpi / CV.tt_value(z, rs, pT, xF)) * h * (H1p * ((CV.ss_value(z, rs, pT, xF)*CV.uu_value(z, rs, pT, xF))/(CV.tt_value(z, rs, pT, xF)**2)) + (1/z)*H * ((CV.ss_value(z, rs, pT, xF)/(CV.tt_value(z, rs, pT, xF)**2))*(CV.uu_value(z, rs, pT, xF)-CV.ss_value(z, rs, pT, xF))))))

#z-integration of polarized cross-section
def get_num(xF, pT, rs, tar, had):
    return quad(lambda z: get_pol(z, xF, pT, rs, tar, had), CV.zmin_value(rs, pT, xF), 1, limit = 150)[0]

#Code for polarized cross-section Qiu-Sterman portion of equation
def get_QS(z, xF, pT, rs, tar, had):
    if tar == 'p':
        f1Tp = get_f1Tp(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT))
    elif tar == 'n':
        f1Tp = conf['aux'].p2n(get_f1Tp(CV.x_value(z, rs, pT, xF), CV.Q2_value(pT)))

    if had.endswith('+'):
        had = had.strip('+')
        d = get_d(z, CV.Q2_value(pT), had)
    elif had.endswith('-'):
        had = had.strip('-')
        d = conf['aux'].charge_conj(get_d(z, CV.Q2_value(pT), had))
    elif had.endswith('0'):
        had = had.strip('0')

        plusd = get_d(z, CV.Q2_value(pT), had)
        minusd = conf['aux'].charge_conj(get_d(z, CV.Q2_value(pT), had))
        d = 0.5 * (plusd + minusd)
    return (1/(z**3)) * (1/CV.x_value(z, rs, pT, xF)) * ((-1 * 4 * pT) / (CV.S_value(rs) + (CV.T_value(rs, pT, xF)/z))) * np.sum(e2 * ((conf['aux'].M / CV.uu_value(z, rs, pT, xF)) * d * f1Tp * (0.5 * CV.ss_value(z, rs, pT, xF) *(CV.ss_value(z, rs, pT, xF)**2 + CV.uu_value(z, rs, pT, xF)**2) / (CV.tt_value(z, rs, pT, xF)**3))))

#z-integration of Qiu-Sterman polarized cross-section
def get_numQS(xF, pT, rs, tar, had):
    return quad(lambda z: get_QS(z, xF, pT, rs, tar, had), CV.zmin_value(rs, pT, xF), 1, limit =150)[0]

#z-integration of fragmentation portion of polarized cross-section
def get_numfrag(xF, pT, rs, tar, had):
    return quad(lambda z: get_frag(z, xF, pT, rs, tar, had), CV.zmin_value(rs, pT, xF), 1, limit = 150)[0]

#Calculation of AN total
def get_AN(xF, pT, rs, tar, had):
    return get_num(xF, pT, rs, tar, had)/get_denom(xF, pT, rs, tar, had)

#Calculation of AN fragmentation
def get_ANfrag(xF, pT, rs, tar, had):
    return get_numfrag(xF, pT, rs, tar, had)/get_denom(xF, pT, rs, tar, had)

#Calculation of AN Qiu-Sterman
def get_ANQS(xF, pT, rs, tar, had):
    return get_numQS(xF, pT, rs, tar, had)/get_denom(xF, pT, rs, tar, had)

if __name__ == '__main__':

  from qcdlib.ff0 import FF as FF0
  from qcdlib.ff1 import FF as FF1
  from qcdlib.pdf0 import PDF as PDF0
  from qcdlib.pdf1 import PDF as PDF1
  conf['aux']= AUX()
  conf['pdf']=PDF0()
  conf['collinspi']=FF1('pi')
  conf['dcollinspi']=FF1('pi','deriv')
  conf['dcollinsk']=FF1('k','deriv')
  conf['Htildepi']=FF1('pi')
  conf['transversity']=PDF1()
  conf['sivers']=PDF1()
  conf['dsivers']=PDF1('deriv')
  conf['ffpi']=FF0('pi')

  rs = 7.25
  tar = 'p'
  had = 'pi+'
  pT = 1.0
  xF = 0.3
  Q2 = 2.0

  print(get_AN(xF, pT, rs, tar, had))
  print(get_ANfrag(xF, pT, rs, tar, had))
  print(get_ANQS(xF, pT, rs, tar, had))

  #CV=Class_Variables()
  #x=np.linspace(-1,1,1000)
  #tt_array3 = np.empty(len(x))
  #tt_array6 = np.empty(len(x))
  #ss_array = np.empty(len(x))
  #uu_array = np.empty(len(x))
  #for i in range(len(x)):
      #tt_array3[i] = CV.tt_value(0.3, 63.0, 3.0, x[i])
      #tt_array6[i] = CV.tt_value(0.6, 63.0, 3.0, x[i])
      #ss_array[i] = CV.ss_value(0.3, 63.0, 3.0, x[i])
      #uu_array[i] = CV.uu_value(0.3, 63.0, 3.0, x[i])
  #print(tt_array3[900])
  #print(ss_array[900])
  #print(uu_array[900])
  #print(x[900])
  #plt.plot(x, tt_array3, color ='blue', label = '_nolegend_')
  ##formatting
  #plt.xlabel(r'$x_F$', fontsize = 20) #axis labels
  #plt.ylabel('t', fontsize = 20)
  ##plt.text(-0.55, -0.2, 'EIC ' + r'$\pi^0$', fontsize=15)
  #plt.locator_params(axis='y', nbins = 4) #tick label density
  #plt.locator_params(axis='x', nbins = 6)
  #plt.axhline(y=0 , xmin=0, xmax=1, color='black', alpha = 0.5, linewidth = '0.3') #line at y=0
  #plt.tick_params(direction='in', length=4, which='minor', labelsize=15); plt.tick_params(direction='in', length=9, which='major', labelsize=15) #ticks
  #plt.minorticks_on()
  #plt.legend(loc = 'best', framealpha = 0.0, borderaxespad = 1.5)  #legend that only presents plots with labels
  ##save and clear
  #plt.savefig('t_vs_xF_at_z3.pdf', bbox_inches='tight')
  #plt.clf()

  #plt.plot(x, tt_array6, color ='blue', label = '_nolegend_')
  ##formatting
  #plt.xlabel(r'$x_F$', fontsize = 20) #axis labels
  #plt.ylabel('t', fontsize = 20)
  ##plt.text(-0.55, -0.2, 'EIC ' + r'$\pi^0$', fontsize=15)
  #plt.locator_params(axis='y', nbins = 4) #tick label density
  #plt.locator_params(axis='x', nbins = 6)
  #plt.axhline(y=0 , xmin=0, xmax=1, color='black', alpha = 0.5, linewidth = '0.3') #line at y=0
  #plt.tick_params(direction='in', length=4, which='minor', labelsize=15); plt.tick_params(direction='in', length=9, which='major', labelsize=15) #ticks
  #plt.minorticks_on()
  #plt.legend(loc = 'best', framealpha = 0.0, borderaxespad = 1.5)  #legend that only presents plots with labels
  ##save and clear
  #plt.savefig('t_vs_xF_at_z6.pdf', bbox_inches='tight')
  #plt.clf()

  #plt.plot(x, (ss_array*uu_array)/(tt_array3**3), color ='blue', label = r' $su/t^3$')
  #plt.plot(x, ss_array/(tt_array3**2), color ='red', label = r' $s/t^2$')
  ##formatting
  #plt.xlabel(r'$x_F$', fontsize = 20) #axis labels
  ##plt.ylabel('t', fontsize = 20)
  ##plt.text(-0.55, -0.2, 'EIC ' + r'$\pi^0$', fontsize=15)
  #plt.locator_params(axis='y', nbins = 4) #tick label density
  #plt.locator_params(axis='x', nbins = 6)
  #plt.axhline(y=0 , xmin=0, xmax=1, color='black', alpha = 0.5, linewidth = '0.3') #line at y=0
  #plt.tick_params(direction='in', length=4, which='minor', labelsize=15); plt.tick_params(direction='in', length=9, which='major', labelsize=15) #ticks
  #plt.minorticks_on()
  #plt.legend(loc = 'best', framealpha = 0.0, borderaxespad = 1.5)  #legend that only presents plots with labels
  ##save and clear
  #plt.savefig('tcubed_vs_xF.pdf', bbox_inches='tight')
  #plt.clf()
