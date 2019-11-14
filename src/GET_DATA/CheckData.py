"""Copyright (C) 2018-2019 Eric Allen - All Rights Reserved"""
#
# You may use, distribute and modify this code under the
# terms of the GNU General Public License v3.0 license.
#
# You should have received a copy of the GNU General Public
# License v3.0 packaged with the Forecast Search Wizard.
# If not vist https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Please properly cite code, derivative code, and outputs
# of the Forecast Search Wizard in all scholarly work and
# publications.
#
# Imports
from __future__ import print_function
import os
import shutil
import glob

#INDIR = /TEXT_DATA/ directory location
def CheckRemove_Data(indir):
    """If the dataset for any given ID is sufficiently small (50bytes).
    Then remove all data for that ID.

    Input: TEXT_DATA directory location.

    There is a chance this is not cross-platform compatible...
    That just means empty data won't get removed...
    The output will show if it worked or not.
    If not then use the os.walk and loop through and don't use glob...
    """

    print("\n\nChecking Data\nData Directory", indir)
    lst_paths = glob.glob(indir+"/*")
    print("Starting Number: ", len(lst_paths))
    lst_paths.sort()
    count = 0
    for path in lst_paths:
        ID = path.split("/")[-1]
        size_lst = []
        for fname in glob.glob(path+"/*"):
            if os.path.exists(fname):
                fsize = os.stat(fname).st_size
                if fsize > 50: #50 bytes
                    size_lst.append(fsize)
            else:
                print("FILE NOT FOUND", fname)

        if len(size_lst) < 1:
            if "LSR" in ID or "VOW" in ID:
                try:
                    shutil.rmtree(path)
                    count += 1
                    print("DELETE: ", ID)

                except:
                    print("Already Removed: ", ID)
            else:
                print("KEEP: ", ID)

    print("Total Products: ", len(lst_paths) - count)


# =============================================================================
# EXPECTED RESULT:
# KEEP: AFDDPQ
# KEEP: HSFEP
# DELETE: LSRADQ
# DELETE: LSRAKN
# DELETE: LSRANN
# DELETE: LSRAT1
# DELETE: LSRBA1
# DELETE: LSRBET
# DELETE: LSRBH1
# DELETE: LSRBR1
# DELETE: LSRCS1
# DELETE: LSRHO1
# DELETE: LSRJM1
# DELETE: LSRMCG
# DELETE: LSRNK1
# DELETE: LSRNY5
# DELETE: LSRNY6
# DELETE: LSROME
# DELETE: LSROTZ
# DELETE: LSRPPG
# DELETE: LSRSNP
# DELETE: LSRTD1
# DELETE: LSRYAK
# KEEP: TCUCP4
# DELETE: VOWLWX
# DELETE: VOWPHI
# =============================================================================
