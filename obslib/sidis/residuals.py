#!/usr/bin/env python
import sys
import os
import numpy as np
from scipy import integrate
from tools.residuals import _RESIDUALS
from tools.config import conf
from obslib.sidis import upol0 as upol
from obslib.sidis import collins0 as collins
from obslib.sidis import sivers0 as sivers
from obslib.sidis import boermulders0 as boermulders
from obslib.sidis import cahn0 as cahn
from obslib.sidis import aUTsPs0 as AUTsinphiS
from obslib.idis.stfuncs import STFUNCS as DIS_STFUNCS

class RESIDUALS(_RESIDUALS):

    def __init__(self,react='sidis'):
        if react == 'sidis':
            self.reaction = 'sidis'
            self.tabs = conf['sidis tabs']
        elif react == 'sidisEIC':
            self.reaction = 'sidisEIC'
            self.tabs = conf['sidisEIC tabs']
        elif react == 'sidisSoLID':
            self.reaction = 'sidisSoLID'
            self.tabs = conf['sidisSoLID tabs']
        self.dis_stfuncs = DIS_STFUNCS()
        self.setup()

    def _get_theory(self, entry):
        k, i = entry
        x = self.tabs[k]['x'][i]
        try: y = self.tabs[k]['y'][i]
        except (ValueError,KeyError): y=None
        z = self.tabs[k]['z'][i]
        try: Q2 = self.tabs[k]['Q2'][i]
        except ValueError: Q2=None
        pT = self.tabs[k]['pT'][i]
        exp = self.tabs[k]['value'][i]
        tar = self.tabs[k]['target'][i]
        had = self.tabs[k]['hadron'][i]
        obs = self.tabs[k]['obs'][i].strip()
        col = self.tabs[k]['col'][i].strip().upper()
        try: F2 = self.tabs[k]['F2'][i]
        except KeyError: F2=None

        M = conf['aux'].M
        M2     = conf['aux'].M ** 2
        Mpi2     = conf['aux'].Mpi ** 2

        if   tar=='proton':    tar='p'
        elif tar=='neutron':   tar='n'
        elif tar=='deuteron':  tar='d'

        if obs == 'FUU':

            thy = upol.get_FUU(x,z,Q2,pT,tar,had)

        elif obs == 'M':

            if had=='h+': had='pi+'
            if had=='h-': had='pi-'

            FUU = upol.get_FUU(x,z,Q2,pT,tar,had)
            if F2==None: F2 = self.dis_stfuncs.get_F2(x, Q2,tar)
            thy = FUU / F2
            if col=='HERMES' or col=='hermes': thy=2*np.pi*pT*thy
            if col=='COMPASS' or col=='compass': thy=np.pi*thy

        elif obs == 'AUTcollins':

            # convention factor
            coeff = 1.
            if   col == 'HERMES':  coeff = 1  # hermes is sin(phi_s+phi_h)
            elif col == 'COMPASS': coeff = -1 # compass is sin(phi_s+phi_h+pi)

            # add depolarization factor
            if col == 'HERMES': coeff *= 2 * (1 - y) / (1 + (1 - y)**2)

            FUT = collins.get_FUT(x,z,Q2,pT,tar,had)
            FUU = upol.get_FUU(x,z,Q2,pT,tar,had)
            thy = coeff * FUT / FUU

        elif obs == 'AUTsivers':

            # convention factor
            coeff = 1.

            FUT = sivers.get_FUT(x,z,Q2,pT,tar,had)
            FUU = upol.get_FUU(x,z,Q2,pT,tar,had)
            thy = coeff * FUT / FUU

        elif obs == 'AUUcos2':

            if had=='h+': had='pi+'
            if had=='h-': had='pi-'

            ''' The data from JLab and HERMES do not require any integrations,
                but require a y-based coefficient. The COMPASS data requires an
                integration over y, and does not require the coefficient.    '''

            def yield_thy(accelerator, should_integrate, ny=10):

                # depending on input parameters, either selects the coefficient
                # method or the integration method of producing a residual value.
                # root_s and W2_min also fluctuate based on accelerator.

                # set known values based on the source of AUUcos2 data
                if  accelerator == 'COMPASS':
                    ROOT_S    = 17.3
                    W2_MIN    = 25.0
                    RANGE_MIN = 0.2
                    RANGE_MAX = 0.9

                elif accelerator == 'CLAS': #JLab col in the data files
                    ROOT_S    = 3.42
                    W2_MIN    = 4.0
                    RANGE_MIN = 0.2
                    RANGE_MAX = 0.85

                elif accelerator == 'HERMES':
                    ROOT_S    = 7.25
                    W2_MIN    = 10
                    RANGE_MIN = 0.2
                    RANGE_MAX = 0.85


                if should_integrate:

                    def fast_integrate(f, low, hi, ny):
                        f = np.vectorize(f)
                        return integrate.fixed_quad(f, low, hi, n=ny)

                    Q2_MIN = 1
                    Q2_MAX = 1000

                    yA = max(   # lower bound of integration
                            RANGE_MIN,
                            Q2_MIN / (x * ((ROOT_S ** 2) - M2)),
                            (W2_MIN - M2) / ((1 - x) * ((ROOT_S ** 2) - M2))
                            )
                    yB = min(   # upper bound of integration
                            Q2_MAX / (x * ((ROOT_S ** 2) - M2)),
                            RANGE_MAX
                            )

                    # any value dependent on y must be a function so that its value
                    # may be recalculated during the integration process
                    Q  = lambda y : np.sqrt(((ROOT_S ** 2) - M2) * x * y)


                    if accelerator=='HERMES':
                        FUU     = lambda y : (1.- y + 0.5*y**2) * upol.get_FUU(x, z, Q(y) ** 2, pT, tar, had)
                        FUUcos2 = lambda y : (1.-y) * (boermulders.get_FUU(x, z, Q(y) ** 2, pT, tar, had) + cahn.get_cahn(x, z, Q(y) ** 2, pT, tar, had))

                    elif accelerator=='COMPASS':
                        FUU     = lambda y : upol.get_FUU(x, z, Q(y) ** 2, pT, tar, had)
                        FUUcos2 = lambda y : (boermulders.get_FUU(x, z, Q(y) ** 2, pT, tar, had) + cahn.get_cahn(x, z, Q(y) ** 2, pT, tar, had))

                    elif accelerator=='CLAS':
                        # CLAS accelerators measure H4 / (H2 + H1), which can be related
                        # to the AUUcos2 asymmetry.
                        gamma   = lambda y : (2 * M * x) / Q(y)
                        kappa   = lambda y : 1 / (1 + gamma(x, y) ** 2)
                        zeta    = lambda y : 1 - y - (0.25 * (gamma(x, y) ** 2) * (y ** 2))
                        epsilon = lambda y : 1 / (1 + ((y ** 2) / (2 * kappa(x, y) * zeta(x, y))))
                        ppa_over_Eh = lambda y: np.sqrt(1-(pT**2 + Mpi**2)*(2.*M*x/(z*Q(y)**2))**2)

                        FUU     = lambda y : ppa_over_Eh*(kappa/epsilon)*(1+gamma**2/(2.*x)) * upol.get_FUU(x, z, Q(y) ** 2, pT, tar, had)
                        FUUcos2 = lambda y : (ppa_over_Eh/2.)*(1+gamma**2/(2.*x)) * (boermulders.get_FUU(x, z, Q(y) ** 2, pT, tar, had) + cahn.get_cahn(x, z, Q(y) ** 2, pT, tar, had))

                    # integrate over y for the numerator and denominator of AUUcos2
                    FUUcos2_integral = fast_integrate(lambda y : (1. / (Q(y) ** 4)) * FUUcos2(y), yA, yB, ny)[0]
                    FUU_integral     = fast_integrate(lambda y : (1. / (Q(y) ** 4)) * FUU(y),     yA, yB, ny)[0]

                    theory = FUUcos2_integral / FUU_integral

                else:   # no integration

                    if accelerator=='HERMES':    coeff  = (1 - y) / (1 - y + 0.5 * y ** 2)
                    elif accelerator=='COMPASS': coeff  = 1.
                    elif accelerator=='CLAS':
                        gamma   = (2.* M * x) / np.sqrt(Q2)
                        kappa   = 1. / (1. + gamma**2.)
                        zeta    = 1. - y - (0.25 * (gamma**2.) * (y ** 2.))
                        epsilon = 1. / (1. + ((y ** 2.) / (2. * kappa * zeta)))
                        
                        coeff =  epsilon / (2. * kappa)


                    FUUcos2 = (boermulders.get_FUU(x, z, Q2, pT, tar, had) + cahn.get_cahn(x, z, Q2, pT, tar, had))
                    FUU     = upol.get_FUU(x,z,Q2,pT,tar,had)

                    theory = coeff * FUUcos2 / FUU

                return theory

            if col=='COMPASS':   thy = yield_thy(col, should_integrate = True,  ny=10)
            elif col=='HERMES':  thy = yield_thy(col, should_integrate = False, ny=10)
            elif col=='CLAS':    thy = yield_thy(col, should_integrate = False, ny=10)

        elif obs == 'AUTsinphiS':  # This is for collinear!

            if tar == 'p':
                pT = None
                FUTsinphiS = AUTsinphiS.get_FX(x, z, Q2, pT, 'p', had)
                FUU = upol.get_FUU(x,z,Q2,pT,'p',had)

            coeff = 1.
            if col == 'HERMES':
                # add depolarization factor for HERMES
                coeff = np.sqrt(1.0 - y) * (2 - y) / (1 - y + 0.5 * y**2)
            if col == 'COMPASS':
                coeff = 1.

            thy = coeff * FUTsinphiS / FUU

        else:
            print 'ERR: exp=%d obs=%s and target=%s not implemented' % (k, obs, tar)
            sys.exit()

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
            tar = self.tabs[k]['target'][0]
            col = self.tabs[k]['col'][0].split()[0]
            obs = self.tabs[k]['obs'][0].split()[0]
            had = self.tabs[k]['hadron'][0].split()[0]
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
                print l
            return L

if __name__ == '__main__':

    from qcdlib.interpolator import INTERPOLATOR
    from qcdlib import pdf0,ff0,pdf1,ff1
    from qcdlib.aux import AUX
    from reader import READER

    conf['aux']    = AUX()

    conf['pdf']          = pdf0.PDF()
    conf['transversity'] = pdf1.PDF()
    conf['sivers']       = pdf1.PDF()
    conf['boermulders']  = pdf1.PDF()
    conf['ffpi']         = ff0.FF('pi')
    conf['ffk']          = ff0.FF('k')
    conf['collinspi']    = ff1.FF('pi')
    conf['collinsk']     = ff1.FF('k')


    conf['datasets']={}
    conf['datasets']['sidis']={}

    conf['datasets']['sidis']['xlsx']={}

    ''' For AUUcos2 testing purposes, most entries have been commented out.
        Uncomment for full program functionality. '''

    '''
    # upol
    conf['datasets']['sidis']['xlsx'][1000]='sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1001]='sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1004]='sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1005]='sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1002]='sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1003]='sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1006]='sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes
    conf['datasets']['sidis']['xlsx'][1007]='sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes
    # sivers
    conf['datasets']['sidis']['xlsx'][2000]='sidis/expdata/2000.xlsx' # | proton   | pi+    | AUTsivers        | hermes     | PT
    conf['datasets']['sidis']['xlsx'][2001]='sidis/expdata/2001.xlsx' # | proton   | pi+    | AUTsivers        | hermes     | x
    conf['datasets']['sidis']['xlsx'][2002]='sidis/expdata/2002.xlsx' # | proton   | pi+    | AUTsivers        | hermes     | z
    conf['datasets']['sidis']['xlsx'][2003]='sidis/expdata/2003.xlsx' # | proton   | pi-    | AUTsivers        | hermes     | PT
    conf['datasets']['sidis']['xlsx'][2004]='sidis/expdata/2004.xlsx' # | proton   | pi-    | AUTsivers        | hermes     | x
    conf['datasets']['sidis']['xlsx'][2005]='sidis/expdata/2005.xlsx' # | proton   | pi-    | AUTsivers        | hermes     | z
    conf['datasets']['sidis']['xlsx'][2006]='sidis/expdata/2006.xlsx' # | proton   | pi0    | AUTsivers        | hermes     | PT
    conf['datasets']['sidis']['xlsx'][2007]='sidis/expdata/2007.xlsx' # | proton   | pi0    | AUTsivers        | hermes     | x
    conf['datasets']['sidis']['xlsx'][2008]='sidis/expdata/2008.xlsx' # | proton   | pi0    | AUTsivers        | hermes     | z
    conf['datasets']['sidis']['xlsx'][2009]='sidis/expdata/2009.xlsx' # | proton   | k+     | AUTsivers        | hermes     | PT
    conf['datasets']['sidis']['xlsx'][2010]='sidis/expdata/2010.xlsx' # | proton   | k+     | AUTsivers        | hermes     | x
    conf['datasets']['sidis']['xlsx'][2011]='sidis/expdata/2011.xlsx' # | proton   | k+     | AUTsivers        | hermes     | z
    conf['datasets']['sidis']['xlsx'][2012]='sidis/expdata/2012.xlsx' # | proton   | k-     | AUTsivers        | hermes     | PT
    conf['datasets']['sidis']['xlsx'][2013]='sidis/expdata/2013.xlsx' # | proton   | k-     | AUTsivers        | hermes     | x
    conf['datasets']['sidis']['xlsx'][2014]='sidis/expdata/2014.xlsx' # | proton   | k-     | AUTsivers        | hermes     | z
    conf['datasets']['sidis']['xlsx'][2015]='sidis/expdata/2015.xlsx' # | neutron  | pi+    | AUTsivers        | jlab       | x
    conf['datasets']['sidis']['xlsx'][2016]='sidis/expdata/2016.xlsx' # | neutron  | pi-    | AUTsivers        | jlab       | x
    conf['datasets']['sidis']['xlsx'][2017]='sidis/expdata/2017.xlsx' # | proton   | k0     | AUTsivers        | compass    | PT
    conf['datasets']['sidis']['xlsx'][2018]='sidis/expdata/2018.xlsx' # | proton   | k0     | AUTsivers        | compass    | x
    conf['datasets']['sidis']['xlsx'][2019]='sidis/expdata/2019.xlsx' # | proton   | k0     | AUTsivers        | compass    | z
    conf['datasets']['sidis']['xlsx'][2026]='sidis/expdata/2026.xlsx' # | deuteron | pi+    | AUTsivers        | compass    | PT
    conf['datasets']['sidis']['xlsx'][2027]='sidis/expdata/2027.xlsx' # | deuteron | pi+    | AUTsivers        | compass    | x
    conf['datasets']['sidis']['xlsx'][2028]='sidis/expdata/2028.xlsx' # | deuteron | pi+    | AUTsivers        | compass    | z
    conf['datasets']['sidis']['xlsx'][2029]='sidis/expdata/2029.xlsx' # | deuteron | pi-    | AUTsivers        | compass    | PT
    conf['datasets']['sidis']['xlsx'][2030]='sidis/expdata/2030.xlsx' # | deuteron | pi-    | AUTsivers        | compass    | x
    conf['datasets']['sidis']['xlsx'][2031]='sidis/expdata/2031.xlsx' # | deuteron | pi-    | AUTsivers        | compass    | z
    conf['datasets']['sidis']['xlsx'][2032]='sidis/expdata/2032.xlsx' # | deuteron | k+     | AUTsivers        | compass    | PT
    conf['datasets']['sidis']['xlsx'][2033]='sidis/expdata/2033.xlsx' # | deuteron | k+     | AUTsivers        | compass    | x
    conf['datasets']['sidis']['xlsx'][2034]='sidis/expdata/2034.xlsx' # | deuteron | k+     | AUTsivers        | compass    | z
    conf['datasets']['sidis']['xlsx'][2035]='sidis/expdata/2035.xlsx' # | deuteron | k-     | AUTsivers        | compass    | PT
    conf['datasets']['sidis']['xlsx'][2036]='sidis/expdata/2036.xlsx' # | deuteron | k-     | AUTsivers        | compass    | x
    conf['datasets']['sidis']['xlsx'][2037]='sidis/expdata/2037.xlsx' # | deuteron | k-     | AUTsivers        | compass    | z
    conf['datasets']['sidis']['xlsx'][2038]='sidis/expdata/2038.xlsx' # | neutron  | k+     | AUTsivers        | jlab       | x
    conf['datasets']['sidis']['xlsx'][2039]='sidis/expdata/2039.xlsx' # | neutron  | k-     | AUTsivers        | jlab       | x
    conf['datasets']['sidis']['xlsx'][2500]='sidis/expdata/2500.xlsx' # | neutron  | pi+    | AUTsivers        | solid      | x
    conf['datasets']['sidis']['xlsx'][2501]='sidis/expdata/2501.xlsx' # | neutron  | pi-    | AUTsivers        | solid      | x
    conf['datasets']['sidis']['xlsx'][2502]='sidis/expdata/2502.xlsx' # | proton   | pi+    | AUTsivers        | solid      | x
    conf['datasets']['sidis']['xlsx'][2503]='sidis/expdata/2503.xlsx' # | proton   | pi-    | AUTsivers        | solid      | x
    conf['datasets']['sidis']['xlsx'][2504]='sidis/expdata/2504.xlsx' # | proton   | pi+    | AUTsivers        | clas12     | x
    conf['datasets']['sidis']['xlsx'][2505]='sidis/expdata/2505.xlsx' # | proton   | pi-    | AUTsivers        | clas12     | x
    conf['datasets']['sidis']['xlsx'][2506]='sidis/expdata/2506.xlsx' # | neutron  | pi+    | AUTsivers        | sbs        | x
    conf['datasets']['sidis']['xlsx'][2507]='sidis/expdata/2507.xlsx' # | neutron  | pi-    | AUTsivers        | sbs        | x
    conf['datasets']['sidis']['xlsx'][2508]='sidis/expdata/2508.xlsx' # | neutron  | pi+    | AUTsivers        | solid stat | x
    conf['datasets']['sidis']['xlsx'][2509]='sidis/expdata/2509.xlsx' # | neutron  | pi-    | AUTsivers        | solid stat | x
    conf['datasets']['sidis']['xlsx'][2510]='sidis/expdata/2510.xlsx' # | proton   | pi+    | AUTsivers        | solid stat | x
    conf['datasets']['sidis']['xlsx'][2511]='sidis/expdata/2511.xlsx' # | proton   | pi-    | AUTsivers        | solid stat | x
    # collins
    conf['datasets']['sidis']['xlsx'][3000]='sidis/expdata/3000.xlsx' # | proton   | pi+    | AUTcollins       | hermes     | x
    conf['datasets']['sidis']['xlsx'][3003]='sidis/expdata/3003.xlsx' # | proton   | pi+    | AUTcollins       | hermes     | z
    conf['datasets']['sidis']['xlsx'][3026]='sidis/expdata/3026.xlsx' # | proton   | pi+    | AUTcollins       | hermes     | pt
    conf['datasets']['sidis']['xlsx'][3004]='sidis/expdata/3004.xlsx' # | proton   | pi-    | AUTcollins       | hermes     | x
    conf['datasets']['sidis']['xlsx'][3018]='sidis/expdata/3018.xlsx' # | proton   | pi-    | AUTcollins       | hermes     | z
    conf['datasets']['sidis']['xlsx'][3016]='sidis/expdata/3016.xlsx' # | proton   | pi-    | AUTcollins       | hermes     | pt
    conf['datasets']['sidis']['xlsx'][3006]='sidis/expdata/3006.xlsx' # | proton   | pi0    | AUTcollins       | hermes     | z
    conf['datasets']['sidis']['xlsx'][3014]='sidis/expdata/3014.xlsx' # | proton   | pi0    | AUTcollins       | hermes     | x
    conf['datasets']['sidis']['xlsx'][3015]='sidis/expdata/3015.xlsx' # | proton   | pi0    | AUTcollins       | hermes     | pt
    conf['datasets']['sidis']['xlsx'][3007]='sidis/expdata/3007.xlsx' # | proton   | k+     | AUTcollins       | hermes     | x
    conf['datasets']['sidis']['xlsx'][3008]='sidis/expdata/3008.xlsx' # | proton   | k+     | AUTcollins       | hermes     | z
    conf['datasets']['sidis']['xlsx'][3024]='sidis/expdata/3024.xlsx' # | proton   | k+     | AUTcollins       | hermes     | pt
    conf['datasets']['sidis']['xlsx'][3017]='sidis/expdata/3017.xlsx' # | proton   | k-     | AUTcollins       | hermes     | x
    conf['datasets']['sidis']['xlsx'][3023]='sidis/expdata/3023.xlsx' # | proton   | k-     | AUTcollins       | hermes     | z
    conf['datasets']['sidis']['xlsx'][3021]='sidis/expdata/3021.xlsx' # | proton   | k-     | AUTcollins       | hermes     | pt
    conf['datasets']['sidis']['xlsx'][3025]='sidis/expdata/3025.xlsx' # | proton   | pi+    | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][3010]='sidis/expdata/3010.xlsx' # | proton   | pi+    | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][3027]='sidis/expdata/3027.xlsx' # | proton   | pi+    | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][3005]='sidis/expdata/3005.xlsx' # | proton   | pi-    | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][3013]='sidis/expdata/3013.xlsx' # | proton   | pi-    | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][3012]='sidis/expdata/3012.xlsx' # | proton   | pi-    | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][6000]='sidis/expdata/6000.xlsx' # | proton   | k-     | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][6001]='sidis/expdata/6001.xlsx' # | proton   | k-     | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][6002]='sidis/expdata/6002.xlsx' # | proton   | k-     | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][6003]='sidis/expdata/6003.xlsx' # | proton   | k+     | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][6004]='sidis/expdata/6004.xlsx' # | proton   | k+     | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][6005]='sidis/expdata/6005.xlsx' # | proton   | k+     | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][4000]='sidis/expdata/4000.xlsx' # | deuteron | pi+    | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][4002]='sidis/expdata/4002.xlsx' # | deuteron | pi+    | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][4001]='sidis/expdata/4001.xlsx' # | deuteron | pi+    | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][4003]='sidis/expdata/4003.xlsx' # | deuteron | pi-    | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][4005]='sidis/expdata/4005.xlsx' # | deuteron | pi-    | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][4004]='sidis/expdata/4004.xlsx' # | deuteron | pi-    | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][4006]='sidis/expdata/4006.xlsx' # | deuteron | k+     | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][4008]='sidis/expdata/4008.xlsx' # | deuteron | k+     | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][4007]='sidis/expdata/4007.xlsx' # | deuteron | k+     | AUTcollins       | compass    | pt
    conf['datasets']['sidis']['xlsx'][4009]='sidis/expdata/4009.xlsx' # | deuteron | k-     | AUTcollins       | compass    | x
    conf['datasets']['sidis']['xlsx'][4011]='sidis/expdata/4011.xlsx' # | deuteron | k-     | AUTcollins       | compass    | z
    conf['datasets']['sidis']['xlsx'][4010]='sidis/expdata/4010.xlsx' # | deuteron | k-     | AUTcollins       | compass    | pt
    #conf['datasets']['sidis']['xlsx'][3001]='sidis/expdata/3001.xlsx' # | neutron  | pi-    | AUTcollins       | jlab       | x
    #conf['datasets']['sidis']['xlsx'][3002]='sidis/expdata/3002.xlsx' # | neutron  | pi+    | AUTcollins       | jlab       | x
    '''

    conf['datasets']['sidis']['xlsx'][5003]='sidis/expdata/5003.xlsx' # | hermes. i don't know the rest of the info

    conf['datasets']['sidis']['norm']={}
    for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1}
    conf['datasets']['sidis']['filters']={}

    conf['sidis tabs'] = READER().load_data_sets('sidis')

    conf['residuals'] = RESIDUALS()

    print conf['residuals'].get_residuals()

    #conf['residuals'].gen_report(verb=1, level=1)
