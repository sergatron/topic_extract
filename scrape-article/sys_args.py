# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:50:06 2019

@author: smouz

"""
import os
import sys
import numpy as np
import pandas as pd

print('Current working dir:', os.getcwd())

#%%

# read commandline arguments, first
fullCmdArguments = sys.argv

# - further arguments
args = fullCmdArguments[1:]

print(args)
print("\nNumber of args provided:", len(args))

if args[0] == '-url':
    print('Input URL:', args[0])
    
if args[1] == '-outfile':
    print('Output path:', args[1])


