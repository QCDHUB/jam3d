#!/usr/bin/env python
import sys
import os
import numpy as np
import pandas as pd
from tools.tools import checkdir, load_config
from tools.reader import _READER
from tools.config import conf


class READER(_READER):

    def __init__(self):
        pass

    def get_Q2(self, tab):
        tab['Q2'] = pd.Series(tab.Q**2, index=tab.index)
        return tab

    def modify_table(self, tab, k):
        tab = self.get_Q2(tab)
        tab = self.apply_cuts(tab, k)
        return tab


if __name__ == "__main__":

    conf['datasets'] = {}
    conf['datasets']['sia'] = {}

    conf['datasets']['sia']['xlsx'] = {}
    # babar      | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
    conf['datasets']['sia']['xlsx'][1000] = '../../database/sia/expdata/1000.xlsx'
    # babar      | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
    conf['datasets']['sia']['xlsx'][1001] = '../../database/sia/expdata/1001.xlsx'
    # conf['datasets']['sia']['xlsx'][1002]='../../database/sia/expdata/1002.xlsx'  #   babar      | pi,pi | AUC-0     | 36     | z1,z2      |
    # conf['datasets']['sia']['xlsx'][1003]='../../database/sia/expdata/1003.xlsx'  #   babar      | pi,pi | AUL-0     | 36     | z1,z2      |
    # conf['datasets']['sia']['xlsx'][1004]='../../database/sia/expdata/1004.xlsx'  #   belle      | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
    # conf['datasets']['sia']['xlsx'][1005]='../../database/sia/expdata/1005.xlsx'  #   belle      | pi,pi | AUT-0     | 16     | z1,z2,qT   |

    # conf['datasets']['sia']['filters']=[]
    # conf['datasets']['sia']['filters'].append("z<0.6")
    # conf['datasets']['sia']['filters'].append("Q2>1.69")
    #conf['datasets']['sia']['filters'].append("pT>0.2 and pT<0.8")

    TAB = READER().load_data_sets('sia')
    print(TAB)
