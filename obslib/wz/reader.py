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
        tab = self.apply_cuts(tab, k)
        return tab


if __name__ == "__main__":

    conf['datasets'] = {}
    conf['datasets']['wz'] = {}

    conf['datasets']['wz']['xlsx'] = {}
    conf['datasets']['wz']['xlsx'][2000] = '../../database/wz/expdata/2000.xlsx'
    conf['datasets']['wz']['xlsx'][2001] = '../../database/wz/expdata/2001.xlsx'
    conf['datasets']['wz']['xlsx'][2002] = '../../database/wz/expdata/2002.xlsx'

    TAB = READER().load_data_sets('wz')
    print(TAB)
