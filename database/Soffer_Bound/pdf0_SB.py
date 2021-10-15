#!/usr/bin/env python
import sys
import os
import numpy as np
import time
from qcdlib.core import CORE
from qcdlib.interpolator import INTERPOLATOR
from tools.config import conf

class PDF(CORE):
    """
    upol PDF for proton. Use SU2 symetry to get for n
    """

    def __init__(self,hadron='p',file='CJ15lo_0000'):
        self.aux = conf['aux']
        if hadron=='p': self.pdf=INTERPOLATOR(file)

    def get_C(self, x, Q2):
        return self.pdf.get_f(x,Q2)

if __name__ == '__main__':

    from qcdlib.aux import AUX

    conf['aux']  = AUX()
    conf['pdf']  = PDF('p','/CJ15lo/CJ15lo_0001')

    x = 0.15
    Q2 = 2.4
    print(conf['pdf'].get_C(x, Q2))
