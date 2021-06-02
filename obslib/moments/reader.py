#!/usr/bin/env python
import sys
import os
import numpy as np
import pandas as pd
from tools.reader import _READER
from tools.config import conf


class READER(_READER):

    def __init__(self):
        pass

    def modify_table(self, tab, k):
        pass
        # tab=self.apply_cuts(tab,k)
        return tab


if __name__ == "__main__":

    conf['datasets'] = {}
    conf['datasets']['lattice'] = {}
    conf['datasets']['lattice']['xlsx'] = {}
    # lattice gT(u-d)
    conf['datasets']['lattice']['xlsx'][1000] = '../../database/lattice/1000.xlsx'
    TAB = READER(conf).load_data_sets('lattice')
    print(TAB)
