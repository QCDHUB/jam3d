#!/usr/bin/env python
import sys
import os
import numpy as np
from tools.tools import load_config
from qcdlib.aux import AUX
from tools.config import conf

def get_h1(x,Q2,had='p'):
    return conf['transversity'].get_C(x, Q2)

if __name__ == '__main__':

    from qcdlib.pdf1 import PDF
    conf['aux']= AUX()
    conf['transversity']=PDF()

    x=0.3
    Q2=2.0

    print(get_h1(x,Q2,'p'))
