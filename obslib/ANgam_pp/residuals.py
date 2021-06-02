#!/usr/bin/env python
import sys
import os
import numpy as np
from mpmath import fp, mp
from scipy.integrate import quad
import pandas as pd
import time
from tools.residuals import _RESIDUALS
from obslib.ANgam_pp.reader import READER
from obslib.ANgam_pp import AN_theory0 as AN_theory
from qcdlib.aux import AUX
from qcdlib.alphaS import ALPHAS
from tools.config import conf


class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'ANgam'
        self.tabs = conf['ANgam tabs']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        xF = self.tabs[k]['xF'][i]
        pT = self.tabs[k]['pT'][i]
        rs = self.tabs[k]['rs'][i]
        eta = self.tabs[k]['eta'][i]
        target = self.tabs[k]['target'][i]
        #hadron = self.tabs[k]['hadron'][i]
        obs = self.tabs[k]['obs'][i].strip()
        col = self.tabs[k]['col'][i].strip().upper()

        if obs == 'ANgam':
            thy = AN_theory.get_AN(xF, pT, rs, nx=10)
            #print hadron,xF,thy
            print(thy, xF, eta, rs)
        return thy

    def gen_report(self, verb=1, level=1):
        """
        verb = 0: Do not print on screen. Only return list of strings
        verb = 1: print on screen the report
        level= 0: only the total chi2s
        level= 1: include point by point
        """

        L = []

        L.append('reaction: %s' % self.reaction)

        L.append('%7s %10s %10s %10s %10s %5s %10s %10s %10s %10s' % (
            'idx', 'tar', 'had', 'col', 'obs', 'npts', 'chi2', 'chi2/npts','rchi2', 'nchi2'))
        for k in self.tabs:
            #print k,len(self.tabs[k]['value'])
            if self.tabs[k]['value'].size == 0:
                continue
            res = self._get_residuals(k)
            rres = self._get_rres(k)
            nres = self._get_nres(k)

            chi2 = np.sum(res**2)
            rchi2 = np.sum(rres**2)
            nchi2 = nres**2
            tar = self.tabs[k]['target'][0]
            col = self.tabs[k]['col'][0].split()[0]
            obs = self.tabs[k]['obs'][0].split()[0]
            had = self.tabs[k]['hadron'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f %10.2f %10.2f' %
                     (k, tar, had, col, obs, npts, chi2, chi2/npts, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'idx=%7d,  '
            msg += 'col=%7s,  '
            msg += 'tar=%7s,  '
            msg += 'had=%7s,  '
            msg += 'obs=%7s,  '
            if 'dependence' in self.tabs[k]:
                msg += 'dep=%7s,  '
            msg += 'xF=%10.3e,  '
            msg += 'pT=%10.3e,  '
            msg += 'rs=%10.3e,  '
            msg += 'exp=%10.3e,  '
            msg += 'alpha=%10.3e,  '
            msg += 'thy=%10.3e,  '
            if 'dthy' in self.tabs[k]:
                msg += 'dthy=%10.3e,  '
            msg += 'shift=%10.3e,  '
            msg += 'chi2=%10.3f  '

            for k in self.tabs:
                if len(self.tabs[k]['value']) == 0:
                    continue
                for i in range(len(self.tabs[k]['value'])):
                    row = [k]
                    row.append(self.tabs[k]['col'][i])
                    row.append(self.tabs[k]['target'][i])
                    row.append(self.tabs[k]['hadron'][i])
                    row.append(self.tabs[k]['obs'][i])
                    if 'dependence' in self.tabs[k]:
                        row.append(self.tabs[k]['dependence'][i].strip())
                    row.append(self.tabs[k]['xF'][i])
                    row.append(self.tabs[k]['pT'][i])
                    row.append(self.tabs[k]['rs'][i])
                    row.append(self.tabs[k]['value'][i])
                    row.append(self.tabs[k]['alpha'][i])
                    row.append(self.tabs[k]['thy'][i])
                    if 'dthy' in self.tabs[k]:
                        row.append(self.tabs[k]['dthy'][i])
                    row.append(self.tabs[k]['shift'][i])
                    # row.append(self.tabs[k]['residuals'][i])
                    # row.append(self.tabs[k]['r-residuals'][i])
                    res = self.tabs[k]['residuals'][i]
                    if res < 0:
                        chi2 = -res**2
                    else:
                        chi2 = res**2
                    row.append(chi2)
                    row = tuple(row)
                    L.append(msg % row)

        if verb == 0:
            return L
        elif verb == 1:
            for l in L:
                print(l)
            return L
