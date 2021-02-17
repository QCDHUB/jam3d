#!/usr/bin/env python
import sys,os
import numpy as np

class MELLIN:

    def __init__(self,npts=16,extended=True,c=None):

        #--gen z and w values along coutour
        x,w=np.polynomial.legendre.leggauss(npts)
        znodes=[0.0,0.1,0.3,0.6,1.0,1.6,2.4,3.5,5,7,10,14,19,25,32,40,50,63]
        if extended: znodes.extend([70,80,90,100,110,120,130,140,150])
        #if extended: znodes.extend([70,80,90,100])

        Z,W,JAC=[],[],[]
        for i in range(len(znodes)-1):
            a,b=znodes[i],znodes[i+1]
            Z.extend(0.5*(b-a)*x+0.5*(a+b))
            W.extend(w)
            JAC.extend([0.5*(b-a) for j in range(x.size)])
        Z=np.array(Z)
        #--globalize
        self.W=np.array(W)
        self.Z=Z
        self.JAC=np.array(JAC)
        #--gen mellin contour
        if c==None: c=1.9
        phi=3.0/4.0*np.pi

        self.N=c+Z*np.exp(complex(0,phi))
        self.phase= np.exp(complex(0,phi))

    def invert(self,x,F):
        return np.sum(np.imag(self.phase * x**(-self.N) * F)/np.pi * self.W * self.JAC)

    def invert_deriv(self,x,F):
        return np.sum(np.imag(self.phase * (-self.N)*x**(-self.N-1) * F)/np.pi * self.W * self.JAC)

if __name__=='__main__':

  mell=MELLIN(8)
  a=-1.8
  b=6.0
  N=mell.N

  mom=gamma(N+a)*gamma(b+1)/gamma(N+a+b+1)
  X=10**np.linspace(-5,-1,10)
  f=lambda x: x**a*(1-x)**b
  for x in X:
      print('x=%10.4e  f=%10.4e  inv=%10.4e'%(x,f(x),mell.invert_deriv(x,mom)))
