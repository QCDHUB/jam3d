#!/usr/bin/env python
import sys
import os
import numpy as np
from scipy.integrate import quad
from tools.residuals import _RESIDUALS
from obslib.sia.reader import READER
from obslib.sia import collins0 as stfuncs
from tools.config import conf

class RESIDUALS(_RESIDUALS):

    def __init__(self):
        self.reaction = 'sia'
        self.tabs = conf['sia tabs']
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        obs = self.tabs[k]['obs'][i].strip()
        col = self.tabs[k]['col'][i].strip()
        z1 = self.tabs[k]['z1'][i]
        z2 = self.tabs[k]['z2'][i]
        Q2 = self.tabs[k]['Q2'][i]
        factor = self.tabs[k]['S2/1+C2'][i]

        if obs == 'AUL-0-PT':
            pT = self.tabs[k]['pT'][i]
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            thy = factor * (ZUcol / ZUuu - ZLcol / ZLuu)
        elif obs == 'AUC-0-PT':
            pT = self.tabs[k]['pT'][i]
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZCuu = ZUuu + ZLuu
            ZCcol = ZUcol + ZLcol
            thy = factor * (ZUcol / ZUuu - ZCcol / ZCuu)
        elif obs == 'AUL-0-PT-INT':
            #if self.tabs[k]['col'][i]=='BaBaR': pT = self.tabs[k]['pT'][i]
            #if self.tabs[k]['col'][i]=='belle': pT = None
            pT = None
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            thy = factor * (ZUcol / ZUuu - ZLcol / ZLuu)
        elif obs == 'AUC-0-PT-INT':
            #if self.tabs[k]['col'][i]=='BaBaR': pT = self.tabs[k]['pT'][i]
            #if self.tabs[k]['col'][i]=='belle': pT = None
            pT = None
            h1 = self.tabs[k]['hadron1'][i]
            h2 = self.tabs[k]['hadron2'][i]
            ZUuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLuu = stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(1, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZUcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '-') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '+')
            ZLcol = stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '+', h2 + '+') + \
                stfuncs.ZX(2, z1, z2, Q2, pT, h1 + '-', h2 + '-')
            ZCuu = ZUuu + ZLuu
            ZCcol = ZUcol + ZLcol
            thy = factor * (ZUcol / ZUuu - ZCcol / ZCuu)

        else:
            print('ERR: obs=%s  not implemented' % obs)
            sys.exit()

        if not col == 'BESIII':
            thy = thy * 100.  # from obs to %

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
            'idx', 'had1', 'had2', 'col', 'obs' ,'npts', 'chi2', 'chi2/npts', 'rchi2', 'nchi2'))

        for k in self.tabs:
            if len(self.tabs[k]['value']) == 0:
                continue
            res = self._get_residuals(k)
            rres = self._get_rres(k)
            nres = self._get_nres(k)

            chi2 = np.sum(res**2)
            rchi2 = np.sum(rres**2)
            nchi2 = nres**2
            col = self.tabs[k]['col'][0].split()[0]
            obs = self.tabs[k]['obs'][0].split()[0]
            had1 = self.tabs[k]['hadron1'][0].split()[0]
            had2 = self.tabs[k]['hadron2'][0].split()[0]
            npts = res.size
            L.append('%7d %10s %10s %10s %10s %5d %10.2f %10.2f %10.2f %10.2f' %
                     (k, had1, had2, col, obs, npts, chi2, chi2/npts, rchi2, nchi2))

        if level == 1:
            L.append('-' * 100)

            msg = 'had1=%7s '
            msg +='had2=%7s '
            msg += 'col=%7s  '
            msg += 'obs=%7s  '
            msg += 'z1=%10.3e  '
            msg += 'z2=%10.3e  '
            msg += 'Q2=%10.3e  '
            msg += 'exp=%10.3e  '
            msg += 'alpha=%10.3e  '
            msg += 'thy=%10.3e  '
            msg += 'shift=%10.3e  '
            msg += 'chi2=%10.3f  '

            for k in self.tabs:
                if len(self.tabs[k]['value']) == 0:
                    continue
                for i in range(len(self.tabs[k]['value'])):
                    z1 = self.tabs[k]['z1'][i]
                    z2 = self.tabs[k]['z2'][i]
                    Q2 = self.tabs[k]['Q2'][i]
                    res = self.tabs[k]['residuals'][i]
                    thy = self.tabs[k]['thy'][i]
                    exp = self.tabs[k]['value'][i]
                    alpha = self.tabs[k]['alpha'][i]
                    rres = self.tabs[k]['r-residuals'][i]
                    col = self.tabs[k]['col'][i]
                    obs = self.tabs[k]['obs'][i]
                    had1 = self.tabs[k]['hadron1'][i]
                    had2 = self.tabs[k]['hadron2'][i]
                    shift = self.tabs[k]['shift'][i]
                    if res < 0:
                        chi2 = -res**2
                    else:
                        chi2 = res**2
                    L.append(msg % (had1, had2, col, obs, z1, z2, Q2,
                                    exp, alpha, thy, shift, chi2))

        if verb == 0:
            return L
        elif verb == 1:
            for l in L:
                print(l)

if __name__ == '__main__':

    from qcdlib.interpolator import INTERPOLATOR
    from qcdlib.ff0 import FF
    from qcdlib.ff1 import FF as COLLINS
    from qcdlib.aux import AUX
    from obslib.sia import collins0 as stfuncs

    conf['aux']    = AUX()
    conf['cpipff'] = INTERPOLATOR('dsspipNLO_0000')
    conf['cpimff'] = INTERPOLATOR('dsspimNLO_0000')
    conf['cKpff']  = INTERPOLATOR('dssKpNLO_0000')
    conf['cKmff']  = INTERPOLATOR('dssKmNLO_0000')

    conf['lam2'] = 0.4
    conf['Q02']  = 1.0
    conf['ffpi'] = FF('pi')
    conf['ffk'] = FF('k')
    conf['collinspi'] = COLLINS('pi')
    conf['collinsk'] = COLLINS('k')
    conf['sia stfuncs'] = stfuncs

    conf['datasets'] = {}
    conf['datasets']['sia'] = {}
    conf['datasets']['sia']['xlsx'] = {}
    conf['datasets']['sia']['xlsx'][1000]='sia/expdata/1000.xlsx' # babar      | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
    conf['datasets']['sia']['xlsx'][1001]='sia/expdata/1001.xlsx' # babar      | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
    conf['datasets']['sia']['xlsx'][1002]='sia/expdata/1002.xlsx' # babar      | pi,pi | AUC-0     | 36     | z1,z2      |
    conf['datasets']['sia']['xlsx'][1003]='sia/expdata/1003.xlsx' # babar      | pi,pi | AUL-0     | 36     | z1,z2      |
    conf['datasets']['sia']['xlsx'][1004]='sia/expdata/1004.xlsx' # belle      | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
    conf['datasets']['sia']['xlsx'][1005]='sia/expdata/1005.xlsx' # belle      | pi,pi | AUT-0     | 16     | z1,z2,qT   |
    conf['datasets']['sia']['norm'] = {}
    conf['datasets']['sia']['norm'][1000]={'value':1,'fixed': False}
    conf['datasets']['sia']['norm'][1001]={'value':1,'fixed': False}
    conf['datasets']['sia']['norm'][1002]={'value':1,'fixed':False}
    conf['datasets']['sia']['norm'][1003]={'value':1,'fixed':False}
    conf['datasets']['sia']['norm'][1004]={'value':1,'fixed':False}
    conf['datasets']['sia']['norm'][1005]={'value':1,'fixed':False}

    conf['sia tabs'] = READER().load_data_sets('sia')
    conf['residuals']= RESIDUALS()
    conf['residuals'].get_residuals()
    conf['residuals'].gen_report(verb=1, level=1)
