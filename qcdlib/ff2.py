#!/usr/bin/env python
import sys
import os
import numpy as np
import time
from qcdlib.core import CORE
from qcdlib.interpolator import INTERPOLATOR
from tools.config import conf

from scipy.special import gamma
from qcdlib.alphaS import ALPHAS
from qcdlib.aux import AUX
from qcdlib.dglap import DGLAP
from qcdlib.kernels import KERNELS
from qcdlib.mellin import MELLIN
from scipy.integrate import quad


class FF(CORE):

    def __init__(self,spl,hadron,shape='nderiv'):

        self.hadron=hadron
        self.shape=shape

        self.Q20=conf['Q20']
        self.mc2=conf['aux'].mc2
        self.mb2=conf['aux'].mb2

        self.mellin=conf['mellin']
        self.kernel=KERNELS(self.mellin,spl)
        self.dglap=DGLAP(self.mellin,conf['alphaS'],self.kernel,'truncated','LO')

        self.set_default_params()
        self.setup()
        self.ford=['g','u','ub','d','db','s','sb','c','cb','b','bb']

    def set_default_params(self):

        #--f(x) = norm * x**a1 * (1-x)**b1 * (1+c1*x+d1*x**2) * (1+ N2 * x**a2 * (1-x)**b2 * (1+c2*x+d2*x**2))
        params={}
        params['g1']   = np.array([0,0,0,0,0,0,0,0,0,0])
        params['u1']   = np.array([0.2,2.5,2.5,0,0,10.0,0,0,0,0])
        params['d1']   = np.array([-0.4,0.5,3.4,0,0,10.0,0,0,0,0])
        params['s1']   = np.array([-0.4,0.5,3.4,0,0,10.0,0,0,0,0])
        params['c1']   = np.array([0,0,0,0,0,0,0,0,0,0])
        params['b1']   = np.array([0,0,0,0,0,0,0,0,0,0])
        params['ub1']  = np.array([-0.4,0.5,3.4,0,0,10.0,0,0,0,0])
        params['db1']  = np.array([0.2,2.5,2.5,0,0,10.0,0,0,0,0])
        params['sb1']  = np.array([-0.4,0.5,3.4,0,0,10.0,0,0,0,0])
        params['cb1']  = np.array([0,0,0,0,0,0,0,0,0,0])
        params['bb1']  = np.array([0,0,0,0,0,0,0,0,0,0])
        self.params=params

        #--widths
        self._widths1_fav  = 0.3
        self._widths1_ufav  = 0.3
        self._widths2_fav  = 0
        self._widths2_ufav  = 0

        # internal
        self.widths1 = np.ones(11)
        self.widths2 = np.ones(11)

    def set_sumrules(self):
        pass

    def set_moms(self):
        moms={}
        moms['g']  =self.get_moments('g1')
        moms['u1'] =self.get_moments('u1')
        moms['d1'] =self.get_moments('d1')
        moms['s1'] =self.get_moments('s1')
        moms['c1'] =self.get_moments('c1')
        moms['b1'] =self.get_moments('b1')
        moms['ub1']=self.get_moments('ub1')
        moms['db1']=self.get_moments('db1')
        moms['sb1']=self.get_moments('sb1')
        moms['cb1']=self.get_moments('cb1')
        moms['bb1']=self.get_moments('bb1')

        moms['up']=moms['u1']+moms['ub1']
        moms['dp']=moms['d1']+moms['db1']
        moms['sp']=moms['s1']+moms['sb1']
        moms['cp']=moms['c1']+moms['cb1']
        moms['bp']=moms['b1']+moms['bb1']
        moms['um']=moms['u1']-moms['ub1']
        moms['dm']=moms['d1']-moms['db1']
        moms['sm']=moms['s1']-moms['sb1']
        moms['cm']=moms['c1']-moms['cb1']
        moms['bm']=moms['b1']-moms['bb1']

        self.moms0=moms
        self.get_BC(moms)

    def set_widths(self):
        # 1,  2,  3,  4,  5,  6,  7,  8,  9, 10
        # u, ub,  d, db,  s, sb,  c, cb,  b, bb
        if self.hadron=='pi':
            for i in range(1, 11):
                if   i == 1 or i==4: self.widths1[i] = self._widths1_fav
                else:                  self.widths1[i] = self._widths1_ufav
                if   i == 1 or i==4: self.widths2[i] = self._widths2_fav
                else:                  self.widths2[i] = self._widths2_ufav
        elif self.hadron=='k':
            for i in range(1, 11):
                if   i == 1 or i==6: self.widths1[i] = self._widths1_fav
                else:                  self.widths1[i] = self._widths1_ufav
                if   i == 1 or i==6: self.widths2[i] = self._widths2_fav
                else:                  self.widths2[i] = self._widths2_ufav
        elif self.hadron=='h':
            for i in range(1, 11):
                if   i == 1 or i==4 or i==6: self.widths1[i] = self._widths1_fav
                else:                  self.widths1[i] = self._widths1_ufav
                if   i == 1 or i==4 or i==6: self.widths2[i] = self._widths2_fav
                else:                  self.widths2[i] = self._widths2_ufav

    def setup(self):
        #self.set_sumrules()
        self.set_moms()
        self.set_widths()
        #--store moments of a given Q2 that has been already calculated
        self.storage={}

    def beta(self,a,b):
        return gamma(a)*gamma(b)/gamma(a+b)

    def get_moments(self,flav,N=None):
        """
        if N==None: then parametrization is to be use to compute moments along mellin contour
        else the Nth moment is returned
        """
        if N==None: N=self.mellin.N
        M1,a1,b1,c1,d1,M2,a2,b2,c2,d2=self.params[flav]
        n1 = self.beta(a1+2,b1+1) + c1*self.beta(a1+3,b1+1) + d1*self.beta(a1+4,b1+1)
        n2 = M2 * (self.beta(a1+a2+2,b1+b2+1) + d1*d2*self.beta(a1+a2+6,b1+b2+1))
        n3 = M2 * (c1+c2)*self.beta(a1+a2+3,b1+b2+1)
        n4 = M2 * (c1*d2+c2*d1)*self.beta(a1+a2+5,b1+b2+1)
        n5 = M2 * (c1*c2+d1+d2)*self.beta(a1+a2+4,b1+b2+1)
        norm=n1+n2+n3+n4+n5

        m1 = self.beta(a1+N,b1+1) + c1*self.beta(a1+N+1,b1+1) + d1*self.beta(a1+N+2,b1+1)
        m2 = M2 * (self.beta(a1+a2+N,b1+b2+1) + d1*d2*self.beta(a1+a2+N+4,b1+b2+1))
        m3 = M2 * (c1+c2)*self.beta(a1+a2+N+1,b1+b2+1)
        m4 = M2 * (c1*d2+c2*d1)*self.beta(a1+a2+N+3,b1+b2+1)
        m5 = M2 * (c1*c2+d1+d2)*self.beta(a1+a2+N+2,b1+b2+1)
        mom=m1+m2+m3+m4+m5
        return M1*mom/norm

        #if self.shape=='nderiv':
        #    m1 = self.beta(a1+N,b1+1) + c1*self.beta(a1+N+1,b1+1) + d1*self.beta(a1+N+2,b1+1)
        #    m2 = M2 * (self.beta(a1+a2+N,b1+b2+1) + d1*d2*self.beta(a1+a2+N+4,b1+b2+1))
        #    m3 = M2 * (c1+c2)*self.beta(a1+a2+N+1,b1+b2+1)
        #    m4 = M2 * (c1*d2+c2*d1)*self.beta(a1+a2+N+3,b1+b2+1)
        #    m5 = M2 * (c1*c2+d1+d2)*self.beta(a1+a2+N+2,b1+b2+1)
        #    mom=m1+m2+m3+m4+m5
        #    return M1*mom/norm
        #elif self.shape=='deriv':
        #    m1 = a1*self.beta(a1+N-1, b1+1) - b1*self.beta(a1+N, b1) - b1*c1*self.beta(a1+N+1, b1) - b1*d1*self.beta(a1+N+2, b1)
        #    m2 = (c1 + a1*c1)*self.beta(a1+N, b1+1) + (2*d1 + a1*d1)*self.beta(a1+N+1, b1+1)
        #    m3 = M2 * ((a1 + a2)*self.beta(a1+a2+N-1, b1+b2+1) - (b1 + b2)*self.beta(a1+a2+N, b1+b2))
        #    m4 = M2 * ((c1 + a1*c1 + a2*c1 + c2 + a1*c2 + a2*c2)*self.beta(a1+a2+N, b1+b2+1))
        #    m5 = M2 * (-(b1*c1 + b2*c1 + b1*c2 + b2*c2)*self.beta(a1+a2+N+1, b1+b2))
        #    m6 = M2 * ((2*c1*c2 + a1*c1*c2 + a2*c1*c2 + 2*d1 + a1*d1 + a2*d1 + 2*d2 + a1*d2 + a2*d2)*self.beta(a1+a2+N+1, b1+b2+1))
        #    m7 = M2 * (-(b1*c1*c2 + b2*c1*c2 + b1*d1 + b2*d1 + b1*d2 + b2*d2)*self.beta(a1+a2+N+2, b1+b2))
        #    m8 = M2 * ((3*c2*d1 + a1*c2*d1 + a2*c2*d1 + 3*c1*d2 + a1*c1*d2 + a2*c1*d2)*self.beta(a1+a2+N+2, b1+b2+1))
        #    m9 = M2 * (-(b1*c2*d1 + b2*c2*d1 + b1*c1*d2 + b2*c1*d2)*self.beta(a1+a2+N+3, b1+b2))
        #    m10 = M2 * ((4*d1*d2 + a1*d1*d2 + a2*d1*d2)*self.beta(a1+a2+N+3, b1+b2+1))
        #    m11 = M2 * (-(b1*d1*d2 + b2*d1*d2)*self.beta(a1+a2+N+4, b1+b2))
        #    mom=m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11
        #    return M1*mom/norm

    def _get_BC(self,g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,tp,tm):
        N=self.mellin.N

        # flav composition
        vm,vp={},{}
        vm[35]= bm + cm + dm + sm - 5.0*tm + um
        vm[24]= -4*bm + cm + dm + sm + um
        vm[15]= -3*cm + dm + sm + um
        vm[8] = dm - 2.0*sp + 2.0*(-sm + sp) + um
        vm[3] = -dm + um
        vm[0] = np.zeros(N.size,dtype=complex)
        vp[0] = np.zeros(N.size,dtype=complex)
        vp[3] = -dp + up
        vp[8] = dp - 2.0*sp + up
        vp[15]= -3.0*cp + dp + sp + up
        vp[24]= -4.0*bp + cp + dp + sp + up
        vp[35]= bp + cp + dp + sp - 5.0*tp + up
        qs    = bp + cp + dp + sp + tp + up
        qv    = bm + cm + dm + sm + tm + um
        q     = np.zeros((2,N.size),dtype=complex)
        q[0]=np.copy(qs)
        q[1]=np.copy(g)

        BC={}
        BC['vm']=vm
        BC['vp']=vp
        BC['qv']=qv
        BC['q'] =q
        return BC

    def get_state(self):
        return (self.widths1,self.widths2,self.BC3,self.BC4,self.BC5)

    def set_state(self,state):
        self.widths1,self.widths2,self.BC3, self.BC4, self.BC5 = state[:]
        self.storage = {}

    def get_BC(self,moms):
        N=self.mellin.N
        zero=np.zeros(N.size,dtype=complex)

        ######################################
        # BC3
        g   = moms['g']
        up  = moms['up']
        dp  = moms['dp']
        sp  = moms['sp']
        cp  = zero
        bp  = zero
        um  = moms['um']
        dm  = moms['dm']
        sm  = moms['sm']
        cm  = zero
        bm  = zero
        self.BC3=self._get_BC(g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,zero,zero)

        ######################################
        # BC for Nf=4
        BC4=self.dglap.evolve(self.BC3,self.Q20,self.mc2,3)
        g =BC4['g']
        up=BC4['up']
        dp=BC4['dp']
        sp=BC4['sp']
        cp=moms['cp']
        bp=zero
        um=BC4['um']
        dm=BC4['dm']
        sm=BC4['sm']
        cm=moms['cm']
        bm=zero
        self.BC4=self._get_BC(g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,zero,zero)

        ######################################
        # BC for Nf=5
        BC5=self.dglap.evolve(self.BC4,self.mc2,self.mb2,4)
        g =BC5['g']
        up=BC5['up']
        dp=BC5['dp']
        sp=BC5['sp']
        cp=BC5['cp']
        bp=moms['bp']
        um=BC5['um']
        dm=BC5['dm']
        sm=BC5['sm']
        cm=BC5['cm']
        bm=moms['bm']
        self.BC5=self._get_BC(g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,zero,zero)

    def evolve(self,Q2):

        if Q2 not in self.storage:
            if self.mb2<Q2:
                self.storage[Q2]=self.dglap.evolve(self.BC5,self.mb2,Q2,5)
            elif self.mc2<=Q2 and Q2<=self.mb2:
                self.storage[Q2]=self.dglap.evolve(self.BC4,self.mc2,Q2,4)
            elif Q2<self.mc2:
                self.storage[Q2]=self.dglap.evolve(self.BC3,self.Q20,Q2,3)

    def get_xF(self,x,Q2,flav,evolve=True):
        if evolve: self.evolve(Q2)

        if self.shape=='nderiv':
            return x*self.mellin.invert(x,self.storage[Q2][flav])
        elif self.shape=='deriv':
            return x*self.mellin.invert_deriv(x,self.storage[Q2][flav])

    def get_xF0(self,x,flav):
        if   flav=='um': mom=self.moms0['um']
        elif flav=='dm': mom=self.moms0['dm']
        elif flav=='sm': mom=self.moms0['sm']

        if self.shape=='nderiv': return x*conf['mellin'].invert(x,mom)
        elif self.shape=='deriv': return x*conf['mellin'].invert_deriv(x,mom)

    def get_C(self,x, Q2):
        self.evolve(Q2)

        if self.shape=='nderiv':
            return np.array([self.mellin.invert(x,self.storage[Q2][_]) for _ in self.ford])
        elif self.shape=='deriv':
            return np.array([self.mellin.invert_deriv(x,self.storage[Q2][_]) for _ in self.ford])


if __name__ == '__main__':

    from qcdlib.aux import AUX
    from scipy.integrate import quad
    conf['order']='NLO'
    conf['Q20'] = 1.27**2
    conf['dglap mode']='truncated'
    conf['aux']=AUX()
    conf['mellin']=MELLIN(npts=16)
    conf['alphaS']=ALPHAS()
    conf['d1']  = FF('Col','pi','deriv')


    x = 0.15
    Q2 = 200.4
    print(conf['d1'].get_C(x, Q2))
