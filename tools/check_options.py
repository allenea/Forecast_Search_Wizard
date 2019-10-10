# Copyright (C) 2018-2019 Eric Allen - All Rights Reserved
#
# Programs in the tools directory are at the sole responsibility of the user to
# modify for individual use. They can be used to get the user started on additional analysis. 
#
#
## MODIFY FOR YOUR OWN USE...
from __future__ import print_function
import glob,sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from search_options.search_options import Option

# TODO EDIT: YOUR DATA PATH
data_dir = os.path.join(os.path.abspath('../'),'TEXT_DATA')
#data_dir = os.path.abspath('../')+'/TEXT_DATA/LSR'


lsting = glob.glob(data_dir+"/*")
IDS = Option.ALL
#IDS = Option.ALL_LSR
count = 0
for lst in lsting:
    lst = lst.split("/")[-1]
    isFound = False
    for ids in IDS:
        if ids == lst:
            isFound = True
    if isFound == False:
         count +=1
         print(str(count)+". ",lst)