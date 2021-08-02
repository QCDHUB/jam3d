#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:00:53 2019

@author: avp5627
"""
import sys
import os
import numpy as np
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf

eu2, ed2 = 4/9., 1/9.
e2 = []
e2.append(0)    # g  0
e2.append(eu2)  # u  1
e2.append(eu2)  # ub 2
e2.append(ed2)  # d  3
e2.append(ed2)  # db 4
e2.append(ed2)  # s  5
e2.append(ed2)  # sb 6
e2.append(0)    # c  7
e2.append(0)    # cb 8
e2.append(0)    # b  9
e2.append(0)    # bb 10
e2 = np.array(e2)


def _get_FUWZ(xA,xB,qT,hadronA,hadronB,boson,PDFA,PDFB,w_hadronA,w_hadronB):
    """
    We use notations form Phys.Rev. D79 (2009) 034005 http://inspirehep.net/record/796530
    hadronA - moves along +Z in cm frame
    hadronB - moves along -Z in cm frame
    boson = W+,W-,Z
    xA - x of a parton in hadronA
    xB - x of a parton in hadronB
    PDFA - hadronA pdf distributions
    PDFB - hadronB pdf distributions
    w_hadronA - widths of hadronA TMDs
    w_hadronB - widths of hadronB TMDs
    """
    
    if boson == 'W+':
        # uA dbarB + dbarA uB + uA sbarB + sbarA uB
        uA    = PDFA[1]
        dbarA = PDFA[4]
        sbarA = PDFA[6]

        uB    = PDFB[1]
        dbarB = PDFB[4]
        sbarB = PDFB[6]   

        wq = np.abs(w_hadronA[1]) + np.abs(w_hadronB[4]) # u dbar factor 2 in the formula is vq**2+aq**2, vq=1, aq=1
        res = conf['aux'].Vud**2 * 2. * uA * dbarB * np.exp(-qT**2 / wq) / (np.pi * wq)  
        
        wq = np.abs(w_hadronA[4]) + np.abs(w_hadronB[1]) # dbar u
        res += conf['aux'].Vud**2 * 2. * dbarA * uB * np.exp(-qT**2 / wq) / (np.pi * wq) 

        wq = np.abs(w_hadronA[1]) + np.abs(w_hadronB[6]) # u sbar
        res += conf['aux'].Vus**2 * 2. * uA * sbarB * np.exp(-qT**2 / wq) / (np.pi * wq)  
        
        wq = np.abs(w_hadronA[6]) + np.abs(w_hadronB[1]) # sbar u
        res += conf['aux'].Vus**2 * 2. * sbarA * uB * np.exp(-qT**2 / wq) / (np.pi * wq) 
        
    elif boson == 'W-':
        # ubarA dB + dA ubarB + ubarA sB + sA ubarB
        ubarA = PDFA[2]
        dA    = PDFA[3]
        sA    = PDFA[5]

        ubarB = PDFB[2]
        dB    = PDFB[3]
        sB    = PDFB[5]

        wq = np.abs(w_hadronA[2]) + np.abs(w_hadronB[3]) # ubar d
        res = conf['aux'].Vud**2 * 2. * ubarA * dB * np.exp(-qT**2 / wq) / (np.pi * wq)  
        
        wq = np.abs(w_hadronA[3]) + np.abs(w_hadronB[2]) # d ubar
        res += conf['aux'].Vud**2 * 2. * dA * ubarB * np.exp(-qT**2 / wq) / (np.pi * wq) 

        wq = np.abs(w_hadronA[2]) + np.abs(w_hadronB[5]) # ubar s
        res += conf['aux'].Vus**2 * 2. * ubarA * sB * np.exp(-qT**2 / wq) / (np.pi * wq)  
        
        wq = np.abs(w_hadronA[5]) + np.abs(w_hadronB[2]) # s ubar
        res += conf['aux'].Vus**2 * 2. * sA * ubarB * np.exp(-qT**2 / wq) / (np.pi * wq)  
        
    elif boson == 'Z':
        # uA abarB + ubarA uB + dA dbarB + dbarA dA + sA sbarB + sbarA sbarB
        uA    = PDFA[1]
        ubarA = PDFA[2]
        dA    = PDFA[3]
        dbarA = PDFA[4]
        sA    = PDFA[5]
        sbarA = PDFA[6]

        uB    = PDFB[1]
        ubarB = PDFB[2]
        dB    = PDFB[3]
        dbarB = PDFB[4]
        sB    = PDFB[5]
        sbarB = PDFB[6]
 
        wq = np.abs(w_hadronA[1]) + np.abs(w_hadronB[2]) # u ubar
        res = (conf['aux'].cvuz**2 + conf['aux'].cauz**2) * uA * ubarB * np.exp(-qT**2 / wq) / (np.pi * wq)  

        wq = np.abs(w_hadronA[2]) + np.abs(w_hadronB[1]) # ubar u
        res += (conf['aux'].cvuz**2 + conf['aux'].cauz**2) * ubarA * uB * np.exp(-qT**2 / wq) / (np.pi * wq)  

        wq = np.abs(w_hadronA[3]) + np.abs(w_hadronB[4]) # d dbar
        res += (conf['aux'].cvdz**2 + conf['aux'].cadz**2) * dA * dbarB * np.exp(-qT**2 / wq) / (np.pi * wq)  

        wq = np.abs(w_hadronA[4]) + np.abs(w_hadronB[3]) # dbar d
        res += (conf['aux'].cvdz**2 + conf['aux'].cadz**2) * dbarA * dB * np.exp(-qT**2 / wq) / (np.pi * wq)  

        wq = np.abs(w_hadronA[5]) + np.abs(w_hadronB[6]) # s sbar
        res += (conf['aux'].cvsz**2 + conf['aux'].casz**2) * sA * sbarB * np.exp(-qT**2 / wq) / (np.pi * wq)  

        wq = np.abs(w_hadronA[6]) + np.abs(w_hadronB[5]) # sbar s
        res += (conf['aux'].cvsz**2 + conf['aux'].casz**2) * sbarA * sB * np.exp(-qT**2 / wq) / (np.pi * wq)  
        
    else:
        print('ERR: boson = %s' % (boson))
        sys.exit()
       

    return res   

def get_FUWZ(xA,xB,qT,hadronA,hadronB,boson):
    """
    Unpolarized distribution
    We use notations form Phys.Rev. D79 (2009) 034005 http://inspirehep.net/record/796530
    hadronA - moves along +Z in cm frame
    hadronB - moves along -Z in cm frame
    boson = W+,W-,Z
    xA - x of a parton in hadronA
    xB - x of a parton in hadronB
    PDFA - hadronA pdf distributions
    PDFB - hadronB pdf distributions
    w_hadronA - widths of hadronA TMDs
    w_hadronB - widths of hadronB TMDs
    """

    if boson == 'W+' or boson == 'W-':
        Q2 = conf['aux'].mW2
    elif boson == 'Z':
        Q2 = conf['aux'].mZ2
    
    # Set up unpolarized functions for hadron A
    if hadronA == 'p':  
        PDFA = conf['pdf'].get_C(xA, Q2)
        w_hadronA = conf['pdf'].get_widths(Q2)
    elif hadronA == 'n':  
        PDFA = conf['aux'].p2n(conf['pdf'].get_C(xA, Q2))
        w_hadronA = conf['aux'].p2n(conf['pdf'].get_widths(Q2))
    else:
        print('ERR: hadronA = %s is not implemented' % (hadronA))
        sys.exit()
      
        
    # Set up unpolarized functions for hadron B
    if hadronB == 'p':  
        PDFB = conf['pdf'].get_C(xB, Q2)
        w_hadronB = conf['pdf'].get_widths(Q2)
    elif hadronB == 'n':  
        PDFB = conf['aux'].p2n(conf['pdf'].get_C(xB, Q2))
        w_hadronB = conf['aux'].p2n(conf['pdf'].get_widths(Q2))
    else:
        print('ERR: hadronB = %s is not implemented' % (hadronB))
        sys.exit()

                

    # build structure function
    return _get_FUWZ(xA,xB,qT,hadronA,hadronB,boson,PDFA,PDFB,w_hadronA,w_hadronB)

    
    
def get_FUWZY(y,qT,energy,hadronA,hadronB,boson):
    """
    Unpolarized distribution
    We use notations form Phys.Rev. D79 (2009) 034005 http://inspirehep.net/record/796530
    hadronA - moves along +Z in cm frame (polarized one for RHIC)
    hadronB - moves along -Z in cm frame
    boson = W+,W-,Z
    y  - rapidity
    xA - x of a parton in hadronA
    xB - x of a parton in hadronB
    """ 

    
    if boson == 'W+' or boson == 'W-':
        Q2 = conf['aux'].mW2
    elif boson == 'Z':
        Q2 = conf['aux'].mZ2

    xA = np.sqrt(Q2/energy) * np.exp(+y) # A is polarized
    xB = np.sqrt(Q2/energy) * np.exp(-y) # B is unpolarized
                

    # build structure function
    return get_FUWZ(xA,xB,qT,hadronA,hadronB,boson)
    
    
if __name__ == '__main__':

    from qcdlib import pdf0 
    from qcdlib import pdf1 
    conf['aux']= AUX()
    conf['pdf']=pdf0.PDF('p')
    conf['pdfpi-']=pdf0.PDF('pi-')

    xA = 0.25
    xB = 0.5
    Q2 = 16
    qT = 0.3
    hadronA = 'p'
    hadronB = 'p'
 
    print(get_FUWZ(xA,xB,qT,hadronA,hadronB,'W+'))
    
    energy = 500.**2
    y = 0.5
    
    print(get_FUWZY(y,qT,energy,hadronA,hadronB,'W+'))





