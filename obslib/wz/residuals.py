#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.residuals import _RESIDUALS
from tools.config import conf
from obslib.wz import upol0 as upol
from obslib.wz import sivers0 as sivers

class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'wz'
        self.tabs = conf['wz tabs']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        y = self.tabs[k]['y'][i]
        energy = self.tabs[k]['sqrtenergy'][i]**2
        qT = self.tabs[k]['pT'][i]

        exp = self.tabs[k]['value'][i]
        hadronB = self.tabs[k]['target'][i]
        TransversePolarizationB=self.tabs[k]['TargetTransversePolarization'][i]
        hadronA = self.tabs[k]['beam'][i]
        TransversePolarizationA=self.tabs[k]['BeamTransversePolarization'][i]
        obs = self.tabs[k]['obs'][i].strip()
        col = self.tabs[k]['col'][i].strip().upper()

        if 'W+' in obs: boson = 'W+'
        elif 'W-' in obs: boson = 'W-'
        elif 'Z' in obs: boson = 'Z'
        
        if obs == 'FU1':

            thy = upol.get_FUWZY(y,qT,energy,hadronA,hadronB,boson)


        elif 'AN' in obs:

            # convention factor
            coeff = 1.

            FUT = sivers.get_FUTWZY(y,qT,energy,hadronA,hadronB,boson,TransversePolarizationA,TransversePolarizationB)
            FU1 = upol.get_FUWZY(y,qT,energy,hadronA,hadronB,boson)
            thy = coeff * FUT / FU1

        else:
            print('ERR: exp=%d obs=%s and hadronB=%s not implemented' % (k, obs, hadronB))
            sys.exit()

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

        L.append('%7s %10s %10s %10s %10s  %5s %10s %10s %10s %10s' % (
            'idx', 'target', 'beam', 'col', 'obs','npts', 'chi2', 'chi2/npts','rchi2', 'nchi2'))
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
            if 'W' in obs: obs='ANW+-'
            if 'Z' in obs: obs='ANZ'
            had = self.tabs[k]['beam'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f %10.2f %10.2f' %
                     (k, tar, had, col, obs, npts, chi2, chi2/npts, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'idx=%7d,  '
            msg += 'col=%7s,  '
            msg += 'tar=%7s,  '
            msg += 'beam=%7s,  '
            msg += 'obs=%7s,  '
            if 'dependence' in self.tabs[k]:
                msg += 'dep=%7s,  '
            msg += 'y=%10.3e,  '
            msg += 'qT=%10.3e,  '
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
                    row.append(self.tabs[k]['beam'][i])
                    row.append(self.tabs[k]['obs'][i])
                    if 'dependence' in self.tabs[k]:
                        row.append(self.tabs[k]['dependence'][i].strip())
                    row.append(self.tabs[k]['y'][i])
                    row.append(self.tabs[k]['qT'][i])
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

    from qcdlib import pdf0
    from qcdlib import pdf1
    from qcdlib.aux import AUX
    from reader import READER

    conf['aux']    = AUX()

    conf['pdf']          = pdf0.PDF('p')
    conf['sivers']       = pdf1.PDF()

    conf['datasets']={}
    conf['datasets']['wz']={}

    conf['datasets']['wz']['xlsx']={}

    # STAR Sivers
    conf['datasets']['wz']['xlsx'][2000]='wz/expdata/2000.xlsx'  
    conf['datasets']['wz']['xlsx'][2001]='wz/expdata/2001.xlsx'  
    conf['datasets']['wz']['xlsx'][2001]='wz/expdata/2002.xlsx'    

    conf['datasets']['wz']['norm']={}
    for k in conf['datasets']['wz']['xlsx']: conf['datasets']['wz']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
    conf['datasets']['wz']['filters']={}

    conf['wz tabs'] = READER().load_data_sets('wz')

    conf['residuals']= RESIDUALS()
    print(conf['residuals'].get_residuals())

