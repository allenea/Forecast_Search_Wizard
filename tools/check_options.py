# Copyright (C) 2018-2019 Eric Allen - All Rights Reserved

## MODIFY FOR YOUR OWN USE...


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