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
    conf['datasets']['dy'] = {}

    conf['datasets']['dy']['xlsx'] = {}
    conf['datasets']['dy']['xlsx'][1000] = '../../database/dy/expdata/1000.xlsx'
    conf['datasets']['dy']['xlsx'][1001] = '../../database/dy/expdata/1001.xlsx'
    conf['datasets']['dy']['xlsx'][1002] = '../../database/dy/expdata/1002.xlsx'
    conf['datasets']['dy']['xlsx'][1003] = '../../database/dy/expdata/1003.xlsx'

    TAB = READER().load_data_sets('dy')
    print(TAB)
