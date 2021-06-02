#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf

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

def get_K(x, Q2, z, hadron):
    Mh = {}
    Mh['pi+'] = conf['aux'].Mpi
    Mh['pi-'] = conf['aux'].Mpi
    Mh['k+'] = conf['aux'].Mk
    Mh['k-'] = conf['aux'].Mk
    return -2.0 * (x / z) * Mh[hadron] / np.sqrt(Q2)

def combine(K, F, D, gauss):
    if 'basis' not in conf:
        conf['basis'] = 'default'

    if conf['basis'] == 'default':
        return np.sum(e2 * K * F * D * gauss)
    elif conf['basis'] == 'valence':
        _F = np.copy(F)
        _F[1] -= _F[2]
        _F[3] -= _F[4]
        out = np.sum(e2 * _F * D * gauss)
        out += e2[1] * _F[2] * D[1] * gauss[2] + \
            e2[3] * _F[4] * D[3] * gauss[4]
        out *= K
        return out

def _get_FX(x, z, Q2, pT, target, hadron, F, D):

    if hadron.endswith('+'):
        gauss = np.ones(11)
        K = get_K(x, Q2, z, hadron)
        return combine(K, F, D, gauss)

    elif hadron.endswith('-'):

        D=conf['aux'].charge_conj(D)
        gauss = np.ones(11)
        K = get_K(x, Q2, z, hadron)
        return combine(K, F, D, gauss)

    elif hadron.endswith('0'):

        Dp=D
        Dm=conf['aux'].charge_conj(D)

        gaussp = np.ones(11)
        gaussm = np.ones(11)
        had = hadron[:-1]
        Kp = get_K(x, Q2, z, had+'+')
        Km = get_K(x, Q2, z, had+'-')

        FXp=combine(Kp, F, Dp, gaussp)
        FXm=combine(Km, F, Dm, gaussm)
        return 0.5*(FXp+FXm)

def get_FX(x, z, Q2, pT, target, hadron):

    # get collinear parts (proton and positive hadrons)
    F = conf['transversity'].get_C(x, Q2)
    if   'pi' in hadron:  D = conf['Htildepi'].get_C(z, Q2)
    elif  'k' in hadron:  D = conf['Htildek'].get_C(z, Q2)
    F[0],D[0]=0,0  # set glue to zero
    if target=='p':

        return _get_FX(x, z, Q2, pT, target, hadron, F, D)

    elif target=='n':

        F=conf['aux'].p2n(F)
        return  _get_FX(x, z, Q2, pT, target, hadron, F, D)

    elif target=='d':

      return 0.5*(get_FX(x, z, Q2, pT, 'p', hadron)+get_FX(x, z, Q2, pT, 'n', hadron))

if __name__ == '__main__':


    from qcdlib.ff1 import FF as FF1
    from qcdlib.pdf1 import PDF as PDF1

    conf['aux']= AUX()
    conf['Htildepi']=FF1('pi')
    conf['Htildek']=FF1('k')
    conf['transversity']=PDF1()

    x = 0.25
    z = 0.5
    Q2 = 2.4
    pT = 0.3


    print(get_FX(x,z,Q2,pT,'p','pi+'))
    print(get_FX(x,z,Q2,pT,'p','pi-'))
    print(get_FX(x,z,Q2,pT,'p','pi0'))

    print(get_FX(x,z,Q2,pT,'n','pi+'))
    print(get_FX(x,z,Q2,pT,'n','pi-'))
    print(get_FX(x,z,Q2,pT,'n','pi0'))

    print(get_FX(x,z,Q2,pT,'d','pi+'))
    print(get_FX(x,z,Q2,pT,'d','pi-'))
    print(get_FX(x,z,Q2,pT,'d','pi0'))

