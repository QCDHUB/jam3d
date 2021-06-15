#!/usr/bin/env python
import sys
import os
import numpy as np
from mpmath import fp, mp
from scipy.integrate import quad
import pandas as pd
import time
from tools.residuals import _RESIDUALS
from obslib.moments.reader import READER
from qcdlib.aux import AUX
from qcdlib.alphaS import ALPHAS
from obslib.idis.stfuncs import STFUNCS as DIS_STFUNCS
from tools.config import conf


class RESIDUALS(_RESIDUALS):

    def __init__(self):
        if 'version' in conf: self.version=conf['version']
        else: self.version=0 #--for back compatibility
        self.reaction = 'moments'
        self.tabs = conf['moments tabs']
        #self.moments = conf['moments']
        self.setup()

    def _get_theory(self, entry):
        #if self.version==0:
        #    k, i = entry
        #    obs = self.tabs[k]['obs'][i].strip()
        #    Q = self.tabs[k]['Q'][i]
        #    Q2=Q**2
        #    if obs == 'gT':
        #        u  =conf['transversity'].get_mom(Q2,1,1)
        #        ub =conf['transversity'].get_mom(Q2,2,1)
        #        d  =conf['transversity'].get_mom(Q2,3,1)
        #        db =conf['transversity'].get_mom(Q2,4,1)
        #        thy = (u-ub)-(d-db)
        #    elif obs == 'gTu':
        #        u  =conf['transversity'].get_mom(Q2,1,1)
        #        ub =conf['transversity'].get_mom(Q2,2,1)
        #        thy = u-ub
        #    elif obs == 'gTd':
        #        d  =conf['transversity'].get_mom(Q2,3,1)
        #        db =conf['transversity'].get_mom(Q2,4,1)
        #        thy = d-db
        #    elif obs == 'gTs':
        #        s  =conf['transversity'].get_mom(Q2,5,1)
        #        sb =conf['transversity'].get_mom(Q2,6,1)
        #        thy = s-sb
        #    elif obs == 'gTc':
        #        c  =conf['transversity'].get_mom(Q2,7,1)
        #        cb =conf['transversity'].get_mom(Q2,8,1)
        #        thy = c-cb
        #    elif obs == 'gT(u-d)':
        #        u  =conf['transversity'].get_mom(Q2,1,1)
        #        ub =conf['transversity'].get_mom(Q2,2,1)
        #        d  =conf['transversity'].get_mom(Q2,3,1)
        #        db =conf['transversity'].get_mom(Q2,4,1)
        #        thy = (u-ub)-(d-db)
        #    elif obs == 'gT(u+d)':
        #        u  =conf['transversity'].get_mom(Q2,1,1)
        #        ub =conf['transversity'].get_mom(Q2,2,1)
        #        d  =conf['transversity'].get_mom(Q2,3,1)
        #        db =conf['transversity'].get_mom(Q2,4,1)
        #        thy = (u-ub)+(d-db)
        #    return thy

        #elif self.version=='JAM20+':
        k, i = entry
        obs = self.tabs[k]['obs'][i].strip()
        Q = self.tabs[k]['Q'][i]
        Q2=Q**2
        if obs == 'gT':
            u  =conf['transversity'].get_mom(Q2)[1]
            ub =conf['transversity'].get_mom(Q2)[2]
            d  =conf['transversity'].get_mom(Q2)[3]
            db =conf['transversity'].get_mom(Q2)[4]
            thy = (u-ub)-(d-db)
        elif obs == 'gTu':
            u  =conf['transversity'].get_mom(Q2)[1]
            ub =conf['transversity'].get_mom(Q2)[2]
            thy = u-ub
        elif obs == 'gTd':
            d  =conf['transversity'].get_mom(Q2)[3]
            db =conf['transversity'].get_mom(Q2)[4]
            thy = d-db
        elif obs == 'gTs':
            s  =conf['transversity'].get_mom(Q2)[5]
            sb =conf['transversity'].get_mom(Q2)[6]
            thy = s-sb
        elif obs == 'gTc':
            c  =conf['transversity'].get_mom(Q2)[7]
            cb =conf['transversity'].get_mom(Q2)[8]
            thy = c-cb
        elif obs == 'gT(u-d)':
            u  =conf['transversity'].get_mom(Q2)[1]
            ub =conf['transversity'].get_mom(Q2)[2]
            d  =conf['transversity'].get_mom(Q2)[3]
            db =conf['transversity'].get_mom(Q2)[4]
            thy = (u-ub)-(d-db)
        elif obs == 'gT(u+d)':
            u  =conf['transversity'].get_mom(Q2)[1]
            ub =conf['transversity'].get_mom(Q2)[2]
            d  =conf['transversity'].get_mom(Q2)[3]
            db =conf['transversity'].get_mom(Q2)[4]
            thy = (u-ub)+(d-db)
        return thy

    def gen_report(self, verb=1, level=1):
        """
        verb = 0: Do not print on screen. Only return list of strings
        verv = 1: print on screen the report
        level= 0: only the total chi2s
        level= 1: include point by point
        """

        L = []

        L.append(self.reaction)

        for k in self.tabs:
            print(k, len(self.tabs[k]['value']))
            if self.tabs[k]['value'].size == 0:
                continue
            res = self._get_residuals(k)
            rres = self._get_rres(k)
            nres = self._get_nres(k)

            chi2 = np.sum(res**2)
            rchi2 = np.sum(rres**2)
            nchi2 = nres**2
            obs = self.tabs[k]['obs'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %5d %10.2f %10.2f %10.2f' %
                     (k, obs, npts, chi2, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'obs=%7s  '
            msg += 'exp=%10.3e  '
            msg += 'dexp=%10.3e  '
            msg += 'thy=%10.3e  '
            msg += 'chi2=%10.3f  '

            for k in self.tabs:
                if len(self.tabs[k]['value']) == 0:
                    continue
                for i in range(len(self.tabs[k]['value'])):
                    obs = self.tabs[k]['obs'][i]
                    res = self.tabs[k]['residuals'][i]
                    thy = self.tabs[k]['thy'][i]
                    exp = self.tabs[k]['value'][i]
                    alpha = self.tabs[k]['alpha'][i]
                    rres = self.tabs[k]['r-residuals'][i]
                    col = self.tabs[k]['col'][i]
                    shift = self.tabs[k]['shift'][i]
                    if res < 0:
                        chi2 = -res**2
                    else:
                        chi2 = res**2
                    L.append(msg % (obs, exp, alpha, thy, chi2))

        if verb == 0:
            return L
        elif verb == 1:
            for l in L:
                print(l)
