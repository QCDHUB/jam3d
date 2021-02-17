#!/usr/bin/env python
import sys
import os
import numpy as np
import time
import fnmatch
try:
    import cPickle
except:
    import _pickle as cPickle
import zlib


def checkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def tex(x):
    return r'$\mathrm{' + x + '}$'

def save(data,name):  
  compressed=zlib.compress(cPickle.dumps(data))
  f=open(name,"wb")
  try:
      f.writelines(compressed)
  except:
      f.write(compressed)
  f.close()


def load(name):
    with open(name, "rb") as compressed:
        data = cPickle.loads(zlib.decompress(compressed.read()))
    return data


def isnumeric(value):
    try:
        int(value)
        return True
    except:
        return False


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



def lprint(msg):
    sys.stdout.write('\r')
    sys.stdout.write(msg)
    sys.stdout.flush()
