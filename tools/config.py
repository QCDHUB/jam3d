"""
This module provides the interface to the configuration settings.

*conf* is a dictionary containing all of the shared information.
"""

conf = {}



def load_config(fname):

    L=open(fname).readlines()
    D = {}
    for l in L:
        try:
            exec(l,D)
        except:
            print('ERR at the input.py. Look for %s'%l)
            sys.exit()   
 
    conf.update(D['conf'])






