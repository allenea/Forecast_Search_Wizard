from __future__ import print_function

import glob
import os

backdir =  os.getcwd()
pyFiles = glob.glob(backdir+"/*.py")
pyFiles.sort()
count = 0
for pF in pyFiles:
    short_pf = pF.split("/")[-1][:-3]
    file1 = open(pF,'r').readlines()
    for i in range(len(file1)):
        if "print" in file1[i] and "(" in file1[i]:
            if (file1[i].strip())[0] == "#":
                continue
            print("File: ",short_pf,"  Row: ",i, " Line ", file1[i].strip())
            count +=1