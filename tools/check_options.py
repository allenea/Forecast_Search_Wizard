"""Copyright (C) 2018-2019 Eric Allen - All Rights Reserved"""
#
# Programs in the tools directory are at the sole responsibility of the user to
# modify for individual use. They can be used to get the user started on additional analysis.
# This one identifies PILS not found in the TEXT_DATA directory.
#
## MODIFY FOR YOUR OWN USE...
from __future__ import print_function
import glob
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from search_options.search_options import Option

DATA_DIR = os.path.join(os.path.abspath('../'), 'TEXT_DATA')
#data_dir = os.path.abspath('../')+'/TEXT_DATA/LSR'

LIST = glob.glob(DATA_DIR+"/*")
IDS = Option.ALL

COUNT = 0
for lst in LIST:
    lst = lst.split("/")[-1]
    isFound = False
    for ids in IDS:
        if ids == lst:
            isFound = True
    if not isFound:
        COUNT += 1
        print(str(COUNT)+". ", lst)
