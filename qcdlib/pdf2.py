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
from scipy.integrate import fixed_quad


class PDF(CORE):

    def __init__(self,spl,shape='nderiv'):

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

        params['g1']    =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        params['uv1']   =np.array([0.25,1.,4.,0.,0.,0.,0.,0.,0.,0.])
        params['dv1']   =np.array([-0.1,1.,6.,0.,0.,0.,0.,0.,0.,0.])
        params['sea1']  =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        params['sea2']  =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        params['db1']   =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        params['ub1']   =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        params['s1']    =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        params['sb1']   =np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
        self.params=params

        #--widths
        self._widths1_uv  = 0.3
        self._widths1_dv  = 0.3
        self._widths1_sea = 0.3
        self._widths2_uv  = 0
        self._widths2_dv  = 0
        self._widths2_sea = 0

        # internal
        self.widths1 = np.ones(11)
        self.widths2 = np.ones(11)

    def set_sumrules(self):

        #--valence
        self.params['uv1'][0]=1
        self.params['uv1'][0]=2/self.get_moments('uv1',1)

        self.params['dv1'][0]=1
        self.params['dv1'][0]=1/self.get_moments('dv1',1)

        #--strange
        self.params['s1'][0]=1
        self.params['s1'][0]=self.get_moments('sb1',1)/self.get_moments('s1',1)

        #--msr
        sea1=self.get_moments('sea1',2)
        sea2=self.get_moments('sea2',2)
        up=self.get_moments('uv1',2)+2*(sea1+self.get_moments('ub1',2))
        dp=self.get_moments('dv1',2)+2*(sea1+self.get_moments('db1',2))
        sp=(sea2+self.get_moments('s1',2))+(sea2+self.get_moments('sb1',2))
        self.params['g1'][0]=1
        self.params['g1'][0]=(1-up-dp-sp)/self.get_moments('g1',2)
        g=self.get_moments('g1',2)
        msr=g+up+dp+sp

        #--share
        self.sr={}
        self.sr['msr']      = msr
        self.sr['uv(1)']    = self.get_moments('uv1',1)
        self.sr['dv(1)']    = self.get_moments('dv1',1)
        self.sr['s-sb(1)']  = self.get_moments('s1',1)-self.get_moments('sb1',1)
        self.sr['s-sb(2)']  = self.get_moments('s1',2)-self.get_moments('sb1',2)
        self.sr['db-ub(1)'] = self.get_moments('db1',1)-self.get_moments('ub1',1)
        self.sr['db-ub(2)'] = self.get_moments('db1',2)-self.get_moments('ub1',2)

        #for _ in sorted(self.sr): print _, self.sr[_]

    def set_moms(self):

        sea1=self.get_moments('sea1')
        sea2=self.get_moments('sea2')

        moms={}
        moms['g']  = self.get_moments('g1')
        moms['up'] = self.get_moments('uv1')+2*(sea1+self.get_moments('ub1'))
        moms['dp'] = self.get_moments('dv1')+2*(sea1+self.get_moments('db1'))
        moms['sp'] = 2*sea2+self.get_moments('s1')+self.get_moments('sb1')
        moms['um'] = self.get_moments('uv1')
        moms['dm'] = self.get_moments('dv1')
        moms['sm'] = self.get_moments('s1')-self.get_moments('sb1')
        self.moms0=moms
        self.get_BC(moms)

    def set_widths(self):
        for i in range(11):
            if   i == 1: self.widths1[i] = self._widths1_uv
            elif i == 3: self.widths1[i] = self._widths1_dv
            else:        self.widths1[i] = self._widths1_sea
        for i in range(11):
            if   i == 1: self.widths2[i] = self._widths2_uv
            elif i == 3: self.widths2[i] = self._widths2_dv
            else:        self.widths2[i] = self._widths2_sea

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
        if N==None: then parametrization is to be used to compute moments along mellin contour
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
        #    m1 = a1*self.beta(a1+N-1, b1+1) - b1*self.beta(a1+N, b1) #- b1*c1*self.beta(a1+N+1, b1) - b1*d1*self.beta(a1+N+2, b1)
        #    #m2 = (c1 + a1*c1)*self.beta(a1+N, b1+1) + (2*d1 + a1*d1)*self.beta(a1+N+1, b1+1)
        #    #m3 = M2 * ((a1 + a2)*self.beta(a1+a2+N-1, b1+b2+1) - (b1 + b2)*self.beta(a1+a2+N, b1+b2))
        #    #m4 = M2 * ((c1 + a1*c1 + a2*c1 + c2 + a1*c2 + a2*c2)*self.beta(a1+a2+N, b1+b2+1))
        #    #m5 = M2 * (-(b1*c1 + b2*c1 + b1*c2 + b2*c2)*self.beta(a1+a2+N+1, b1+b2))
        #    #m6 = M2 * ((2*c1*c2 + a1*c1*c2 + a2*c1*c2 + 2*d1 + a1*d1 + a2*d1 + 2*d2 + a1*d2 + a2*d2)*self.beta(a1+a2+N+1, b1+b2+1))
        #    #m7 = M2 * (-(b1*c1*c2 + b2*c1*c2 + b1*d1 + b2*d1 + b1*d2 + b2*d2)*self.beta(a1+a2+N+2, b1+b2))
        #    #m8 = M2 * ((3*c2*d1 + a1*c2*d1 + a2*c2*d1 + 3*c1*d2 + a1*c1*d2 + a2*c1*d2)*self.beta(a1+a2+N+2, b1+b2+1))
        #    #m9 = M2 * (-(b1*c2*d1 + b2*c2*d1 + b1*c1*d2 + b2*c1*d2)*self.beta(a1+a2+N+3, b1+b2))
        #    #m10 = M2 * ((4*d1*d2 + a1*d1*d2 + a2*d1*d2)*self.beta(a1+a2+N+3, b1+b2+1))
        #    #m11 = M2 * (-(b1*d1*d2 + b2*d1*d2)*self.beta(a1+a2+N+4, b1+b2))
        #    mom=m1#+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11
        #    return M1*mom/norm

    def _get_BC(self,g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,tp,tm):
        N=self.mellin.N

        # flav composition
        vm,vp={},{}
        vm[35]= bm + cm + dm + sm - 5*tm + um
        vm[24]= -4*bm + cm + dm + sm + um
        vm[15]= -3*cm + dm + sm + um
        vm[8] = dm - 2*sp + 2*(-sm + sp) + um
        vm[3] = -dm + um
        vm[0] = np.zeros(N.size,dtype=complex)
        vp[0] = np.zeros(N.size,dtype=complex)
        vp[3] = -dp + up
        vp[8] = dp - 2*sp + up
        vp[15]= -3*cp + dp + sp + up
        vp[24]= -4*bp + cp + dp + sp + up
        vp[35]= bp + cp + dp + sp - 5*tp + up
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

        ###############################################
        # BC for Nf=3
        g   = moms['g']
        up  = moms['up']
        um  = moms['um']
        dp  = moms['dp']
        dm  = moms['dm']
        sp  = moms['sp']
        sm  = moms['sm']
        cp  = zero
        cm  = zero
        bp  = zero
        bm  = zero
        self.BC3=self._get_BC(g,up,um,dp,dm,sp,sm,zero,zero,zero,zero,zero,zero)

        ###############################################
        # BC for Nf=4
        BC4=self.dglap.evolve(self.BC3,self.Q20,self.mc2,3)
        g =BC4['g']
        up=BC4['up']
        dp=BC4['dp']
        sp=BC4['sp']
        cp=BC4['cp']
        bp=BC4['bp']
        tp=BC4['tp']
        um=BC4['um']
        dm=BC4['dm']
        sm=BC4['sm']
        cm=BC4['cm']
        bm=BC4['bm']
        tm=BC4['tm']
        self.BC4=self._get_BC(g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,tp,tm)

        ###############################################
        # BC for Nf=5
        BC5=self.dglap.evolve(self.BC4,self.mc2,self.mb2,4)
        g =BC5['g']
        up=BC5['up']
        dp=BC5['dp']
        sp=BC5['sp']
        cp=BC5['cp']
        bp=BC5['bp']
        tp=BC5['tp']
        um=BC5['um']
        dm=BC5['dm']
        sm=BC5['sm']
        cm=BC5['cm']
        bm=BC5['bm']
        tm=BC5['tm']
        self.BC5=self._get_BC(g,up,um,dp,dm,sp,sm,cp,cm,bp,bm,tp,tm)

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

        #return x*self.mellin.invert(x,self.storage[Q2][flav])
        if self.shape=='nderiv':
            return x*self.mellin.invert(x,self.storage[Q2][flav])

        if self.shape=='deriv':
            return x*self.mellin.invert_deriv(x,self.storage[Q2][flav])

    def get_xF0(self,x,flav):
        if   flav=='um': mom=self.moms0['um']
        elif flav=='dm': mom=self.moms0['dm']
        elif flav=='sm': mom=self.moms0['sm']

        #return x*conf['mellin'].invert(x,mom)
        if self.shape=='nderiv': return x*conf['mellin'].invert(x,mom)
        if self.shape=='deriv': return x*conf['mellin'].invert_deriv(x,mom)

    def get_C(self,x, Q2):
        self.evolve(Q2)

        #return np.array([self.mellin.invert(x,self.storage[Q2][_]) for _ in self.ford])
        if self.shape=='nderiv':
            return np.array([self.mellin.invert(x,self.storage[Q2][_]) for _ in self.ford])

        if self.shape=='deriv':
            return np.array([self.mellin.invert_deriv(x,self.storage[Q2][_]) for _ in self.ford])

    def get_mom(self,Q2): #used for calculating the tensor charge for lattice data
        mom_arr=[]
        mom_arr.append(0.)
        for i in [1,2,3,4,5,6]:
            #mom_arr.append(quad(lambda x: self.get_C(x,Q2)[i], 0., 1.)[0])
            h1=np.vectorize(lambda x: self.get_C(x,Q2)[i])
            mom_arr.append(fixed_quad(h1, 0, 1, n=25)[0])

        return np.array(mom_arr)


if __name__ == '__main__':

    from qcdlib.aux import AUX
    from scipy.integrate import quad
    conf['order']='NLO'
    conf['Q20'] = 1.27**2
    conf['dglap mode']='truncated'
    conf['aux']=AUX()
    conf['mellin']=MELLIN(npts=16)
    conf['alphaS']=ALPHAS()
    conf['pdf']  = PDF('h1')

    x=0.3
    Q2=125.0
    print(conf['pdf'].get_mom(Q2))
