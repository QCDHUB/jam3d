#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.residuals import _RESIDUALS
from tools.config import conf
from obslib.Soffer_Bound import SB0 as SB

class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'SB'
        self.tabs = conf['SB tabs']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        x = self.tabs[k]['x'][i]
        Q2 = self.tabs[k]['Q2'][i]
        exp = self.tabs[k]['value'][i]
        obs = self.tabs[k]['obs'][i].strip()
        err = self.tabs[k]['alpha'][i]

        if obs=='SBu':
            if np.abs(SB.get_h1(x,Q2)[1]) > exp+err: thy = SB.get_h1(x,Q2)[1]
            else: thy = exp
            #if np.abs(SB.get_h1(x,Q2)[1]) <= exp: thy = exp
            #thy = SB.get_h1(x,Q2)[1]

        elif obs=='SBd':
            if np.abs(SB.get_h1(x,Q2)[3]) > exp+err: thy = SB.get_h1(x,Q2)[3]
            else: thy = exp
            #if np.abs(SB.get_h1(x,Q2)[3]) <= exp: thy = exp
            #thy = SB.get_h1(x,Q2)[3]

        return thy

    def gen_report(self, verb=1, level=1):
        """
        verb = 0: Do not print on screen. Only return list of strings
        verv = 1: print on screen the report
        level= 0: only the total chi2s
        level= 1: include point by point
        """

        L = []

        L.append('reaction: %s' % self.reaction)

        L.append('%7s %10s %10s %10s %10s %5s %10s %10s %10s %10s' % (
            'idx', 'tar', 'had', 'col', 'obs', 'npts', 'chi2', 'chi2/npts', 'rchi2', 'nchi2'))
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
            tar = 'N/A' #self.tabs[k]['target'][0]
            col = 'N/A' #self.tabs[k]['col'][0].split()[0]
            obs = self.tabs[k]['obs'][0].split()[0]
            had = 'N/A' #self.tabs[k]['hadron'][0].split()[0]
            npts = res.size
            if npts>0:
                L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f  %10.2f %10.2f' %
                     (k, tar, had, col, obs, npts, chi2, chi2/npts, rchi2, nchi2))
            elif npts==0:
                L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f %10.2f %10.2f' %
                     (k, tar, had, col, obs, npts, chi2, 0.0, rchi2, nchi2))


        if level == 1:
            L.append('-' * 100)

            msg = 'idx=%7d,  '
            msg += 'col=%7s,  '
            msg += 'tar=%7s,  '
            msg += 'had=%7s,  '
            msg += 'obs=%7s,  '
            if 'dependence' in self.tabs[k]:
                msg += 'dep=%7s,  '
            if 'Dependence' in self.tabs[k]:
                msg += 'dep=%7s,  '
            msg += 'x=%10.3e,  '
            msg += 'z=%10.3e,  '
            msg += 'pT=%10.3e,  '
            msg += 'Q2=%10.3e,  '
            msg += 'yh=%10.3e,  '
            msg += 'yp=%10.3e,  '
            msg += 'dy=%10.3e,  '
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
                    if 'Dependence' in self.tabs[k]:
                        row.append(self.tabs[k]['Dependence'][i].strip())
                    row.append(self.tabs[k]['x'][i])
                    row.append(self.tabs[k]['z'][i])
                    row.append(self.tabs[k]['pT'][i])
                    row.append(self.tabs[k]['Q2'][i])
                    row.append(self.tabs[k]['yh'][i])
                    row.append(self.tabs[k]['yp'][i])
                    row.append(self.tabs[k]['dy'][i])
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

if __name__ == '__main__':

    from qcdlib.interpolator import INTERPOLATOR
    from qcdlib import pdf1
    from qcdlib.aux import AUX
    from reader import READER

    conf['aux']    = AUX()

    conf['transversity'] = pdf1.PDF()

    conf['datasets']={}
    conf['datasets']['SB']={}

    conf['datasets']['SB']['xlsx']={}

    # SB
    conf['datasets']['SB']['xlsx'][1000]='Soffer_Bound/expdata/1000.xlsx'  # | u   | SB
    conf['datasets']['SB']['xlsx'][2000]='Soffer_Bound/expdata/2000.xlsx'  # | d   | SB

    conf['datasets']['SB']['norm']={}
    for k in conf['datasets']['SB']['xlsx']: conf['datasets']['SB']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
    conf['datasets']['SB']['filters']={}

    conf['SB tabs'] = READER().load_data_sets('SB')

    conf['residuals']= RESIDUALS()
    print(conf['residuals'].get_residuals())

    #conf['residuals'].gen_report(verb=1, level=1)
