#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf

eu2, ed2 = 4 / 9., 1 / 9.
e2 = []
e2.append(0)   # g
e2.append(eu2)  # u
e2.append(eu2)  # ub
e2.append(ed2)  # d
e2.append(ed2)  # db
e2.append(ed2)  # s
e2.append(ed2)  # sb
e2.append(eu2)   # c
e2.append(eu2)   # cb
e2.append(ed2)   # b
e2.append(ed2)   # bb
e2 = np.array(e2)

#def get_cc(A):
#    Acc = np.zeros(A.size)
#    Acc[1] = A[2]
#    Acc[2] = A[1]
#    Acc[3] = A[4]
#    Acc[4] = A[3]
#    Acc[5] = A[6]
#    Acc[6] = A[5]
#    Acc[7] = A[8]
#    Acc[8] = A[7]
#    Acc[9] = A[10]
#    Acc[10] = A[9]
#    return Acc

def get_K(i, z1, z2, pT, wq, k1, k2, hadron1, hadron2):

    Mh = {}
    Mh['pi+'] =  conf['aux'].Mpi
    Mh['pi-'] =  conf['aux'].Mpi
    Mh['k+'] =   conf['aux'].Mk
    Mh['k-'] =   conf['aux'].Mk

    if i == 1:
        if pT != None:
            return np.ones(11)
        else:
            return 1. / (2. * np.pi) * np.ones(11)
    elif i == 2:
        if pT != None:
            return 4. *  Mh[hadron1]**2 * z1**2 * pT**2 / wq**2
        else:
            return 2. *  Mh[hadron1]**2 * z1**2 / (np.pi * wq)


def get_Wq(z1, z2, k1, k2, Q2, hadron1, hadron2):
    had1 = hadron1[:-1]
    had2 = hadron2[:-1]

    W1 = conf[k2+had1].get_widths(Q2)
    W2 = conf['aux'].charge_conj(conf[k1+had2].get_widths(Q2))

    if hadron1.endswith('-'):
        W1 = conf['aux'].charge_conj(W1)

    if hadron2.endswith('-'):
        W2 = conf['aux'].charge_conj(W2)

    return (z1**2*W2 + z2**2*W1)/(z2**2)

def get_gauss(z1, z2, pT, k1, k2, wq):
    if pT != None:
        return np.exp(-pT**2 / wq) / (np.pi * wq)
    else:
        return np.ones(11)

def ZX(i, z1, z2, Q2, pT, hadron1, hadron2):
    D = {}
    D[1] = {'k1': 'ff', 'k2': 'ff'}
    D[2] = {'k1': 'collins', 'k2': 'collins'}

    k1 = D[i]['k1']
    k2 = D[i]['k2']
    if k1 == None or k2 == None:
        return 0

    had1 = hadron1[:-1]
    had2 = hadron2[:-1]

    D1 = conf[k1+had1].get_C(z1, Q2)
    D2 = conf['aux'].charge_conj(conf[k2+had2].get_C(z2, Q2))

    if hadron1.endswith('-'):
        D1 = conf['aux'].charge_conj(D1)

    if hadron2.endswith('-'):
        D2 = conf['aux'].charge_conj(D2)

    #print hadron1,hadron2,D1,conf['aux'].charge_conj(D1)

    Wq = get_Wq(z1, z2, k1, k2, Q2, hadron1, hadron2)
    gauss = get_gauss(z1, z2, pT, k1, k2, Wq)
    K = get_K(i, z1, z2, pT, Wq, k1, k2, hadron1, hadron2)
    return np.sum(e2 * K * D1 * D2 * gauss)

if __name__ == '__main__':

    from qcdlib.interpolator import INTERPOLATOR
    from qcdlib.ff0 import FF as FF0
    from qcdlib.ff1 import FF as FF1

    conf['aux']    = AUX()
    conf['cpipff'] = INTERPOLATOR('dsspipNLO_0000')
    conf['cpimff'] = INTERPOLATOR('dsspimNLO_0000')
    conf['cKpff']  = INTERPOLATOR('dssKpNLO_0000')
    conf['cKmff']  = INTERPOLATOR('dssKmNLO_0000')

    conf['lam2'] = 0.4
    conf['Q02']  = 1.0
    conf['ffpi']  = FF0('pi')
    conf['ffpi']  = FF0('k')
    conf['collinspi'] = FF1('pi')
    conf['collinsk'] = FF1('k')

    z1 = 0.5
    z2 = 0.3
    Q2 = 2.5
    pT = 1.0
    hadron1 = 'pi+'
    hadron2 = 'pi-'
    #for i in [1,2]:
    print(1, ZX(1, z1, z2, Q2, pT, hadron1, hadron2))
    print(2, ZX(2, z1, z2, Q2, pT, hadron1, hadron2))
