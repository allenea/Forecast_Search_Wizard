"""Copyright (C) 2018-2019 Eric Allen - All Rights Reserved"""
# CREATE YOUR OWN TOOL - Used for analyzing FSW code
#IMPORTS
import glob
import os

BACK_DIR = os.path.abspath("./..")
PY_FILES = glob.glob(BACK_DIR+"/src/*.py")
PY_FILES.sort()

COUNT = 0
for p in PY_FILES:
    #Remove .py extension
    short_pf = p.split("/")[-1][:-3]
    file1 = open(p, 'r').readlines()
    for i, file_row in enumerate(file1):
        if "print" in file_row:#.upper(): #and "#" != (file_row.strip())[0]:# and "(" in file_row:
            #if (file_row.strip())[0] == "#":
            #    continue
            print("File: ", short_pf, "  Row: ", i+1, " Line ", file_row.strip())
            COUNT += 1
