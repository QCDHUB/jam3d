#!/usr/bin/env python


# Adam Rilatt - 06 / 24 / 20
# Ben Gordon - confirmed results with separate code on 6/25/20
# Daniel Pitonyak - edits on 7/6/20
# Cahn term in the cos2phi asymmetry

'''
This script will construct and test the Cahn function.
'''

import sys
import os
import numpy as np
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf


''' Contains all the squares of the quark charges.
    We only care about the three lightest ones --
    up, down, and strange. Charm, bottom, and top
    are ignored.                                   '''
up_square   = 4.0 / 9.0
down_square = 1.0 / 9.0
quark_charges = np.array([
    0,              # gluon
    up_square,      # up
    up_square,      # anti-up
    down_square,    # down
    down_square,    # anti-down
    down_square,    # strange
    down_square,    # anti-strange
    0,              # charm
    0,              # anti-charm
    0,              # bottom
    0               # anti-bottom
])


def _get_cahn(x, z, Q2, pT, tar, had, F, D, w_tar, w_had):

    ''' _get_cahn accounts for charged and neutral hadrons.
        It represents the structure function used by get_cahn. '''

    def gen_cahn(z, w_tar, w_had, pT, collinear):
        # generates the Cahn function
        wq = (z ** 2) * np.abs(w_tar) + np.abs(w_had)
        new_term = ((z * np.abs(w_tar) * pT) / wq) ** 2

        if collinear:
            gauss = np.ones(len(quark_charges))
        else:
            gauss = np.exp((-pT ** 2) / wq) / (np.pi * wq)

        return np.sum(quark_charges * K * F * D * new_term * gauss)


    K = (2 * x) / Q2

    if had.endswith('+'):
        return gen_cahn(z, w_tar, w_had, pT, collinear = (pT == None))


    elif had.endswith('-'):
        # flip charges (particles to antiparticles)
        if pT != None:
            D     = conf['aux'].charge_conj(D)
            w_had = conf['aux'].charge_conj(w_had)
            return gen_cahn(z, w_tar, w_had, pT, collinear = False)

        else:
            return gen_cahn(z, w_tar, w_had, pT, collinear = True)


    elif had.endswith('0'):
        # essentially average the + and - operations above

        if pT != None:
            FUUp = gen_cahn(z, w_tar, w_had, pT, collinear = False)

            D     = conf['aux'].charge_conj(D)
            w_had = conf['aux'].charge_conj(w_had)
            FUUm = gen_cahn(z, w_tar, w_had, pT, collinear = False)

        else:
            FUUp = gen_cahn(z, w_tar, w_had, pT, collinear = True)

            D     = conf['aux'].charge_conj(D)
            w_had = conf['aux'].charge_conj(w_had)
            FUUm = gen_cahn(z, w_tar, w_had, pT, collinear = True)

        return 0.5 * (FUUp + FUUm)


def get_cahn(x, z, Q2, pT, tar, had):

    ''' Calls _get_cahn with the appropriate PDFs and FFs'''

    F     = conf['pdf'].get_C(x, Q2)
    w_tar = np.abs(conf['pdf'].get_widths(Q2))

    # select between several available fragmentation functions
    # based on what hadron is measured
    if 'pi' in had:
        D     = conf['ffpi'].get_C(z, Q2)
        w_had = np.abs(conf['ffpi'].get_widths(Q2))

    elif 'k' in had:
        D     = conf['ffk'].get_C(z, Q2)
        w_had = np.abs(conf['ffk'].get_widths(Q2))

    elif 'h' in had:
        D     = conf['ffpi'].get_C(z, Q2) #use pions for now
        w_had = np.abs(conf['ffpi'].get_widths(Q2)) #use pions for now

    # build function based on the target
    if tar == 'p':
        return _get_cahn(x, z, Q2, pT, tar, had, F, D, w_tar, w_had)

    elif tar == 'n':
        # convert PDF to its neutron counterpart
        F     = conf['aux'].p2n(F)
        w_tar = conf['aux'].p2n(w_tar)
        return _get_cahn(x, z, Q2, pT, tar, had, F, D, w_tar, w_had)


    elif tar == 'd':    # proton-neutron bound state ('deuteron'?)
        return (0.5 * (get_cahn(x, z, Q2, pT, 'p', had) +
                       get_cahn(x, z, Q2, pT, 'n', had)))


if __name__ == '__main__':

    ''' Testing space. '''

    from qcdlib.pdf0 import PDF
    from qcdlib.ff0 import FF

    conf['aux']  = AUX()
    conf['pdf']  = PDF()
    conf['ffpi'] = FF('pi')
    conf['ffk']  = FF('k')

    x   = 0.25
    z   = 0.5
    Q2  = 2.4
    mu2 = Q2
    pT  = 0.3

    for target in ['p', 'n', 'd']:
        for hadron in ['pi+', 'pi-', 'pi0']:
            s  = str(get_cahn(x, z, Q2, pT, target, hadron))
            s += '(target = ' + target + ', hadron = ' + hadron + ')'
            print(s)
