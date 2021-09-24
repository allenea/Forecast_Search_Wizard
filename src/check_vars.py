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
import sys
#import os
import time

def AndTrue_OrFalse(option):
    """ SETS THE isAnd OPTION PROVIDED IN THE FSW_NAMELIST. Prints to display."""
    if isinstance(option, bool):
        if option:
            return True
        else:
        #elif not option:
            return False
    else:
        return None

def byforecast(option):
    """ SETS THE byforecast OPTION PROVIDED IN THE FSW_NAMELIST"""
    if isinstance(option, bool):
        if option:
            return True
        else:
        #elif not option:
            return False
    else:
        return None

def makeAssumptions(option):
    """ SETS THE byforecast OPTION PROVIDED IN THE FSW_NAMELIST"""
    if isinstance(option, bool):
        if option:
            return True
        else:
        #elif not option:
            return False
    else:
        return None

def grep_check(option):
    """docstring"""
    if isinstance(option, bool):
        if option:
            return True
        else:
        #elif not option:
            return False
    else:
        return None

def debug_check(option):
    """docstring"""
    if isinstance(option, bool):
        if option:
            return True
        else:
        #elif not option:
            return False
    else:
        return None

def bulk_check(option):
    """docstring"""
    if isinstance(option, bool):
        if option:
            return True
        else:
        #elif not option:
            return False
    else:
        return None


def input_words(lst, isGrep):
    """ SETS THE LIST OF KEYWORDS PROVIDED IN THE FSW_NAMELIST. Prints them to display."""
    remove = list.remove
    strip = str.strip
    upper = str.upper
    if isinstance(lst, list) and all(isinstance(item, str) for item in lst):
        if " " in lst:
            remove(lst, " ")
        if "" in lst:
            remove(lst, "")

        inputKeyLst = []
        if len(lst) < 1:
            print("Empty List of Words")
            sys.stdout.flush()
            return None
        else:
            i = 0
            for word in lst:
                if strip(word) == "":
                    continue
                elif upper(word) in inputKeyLst and isGrep:
                    continue
                elif " "+upper(word)+" " in inputKeyLst and not isGrep:
                    continue
                else:
                    i = i + 1
                    inputKey = upper(word)
                    if not isGrep:
                        inputKey = " "+inputKey+" "
                    inputKeyLst.append(inputKey)
            if isGrep:
                inputKeyLst = check_if_substring(inputKeyLst)
            return inputKeyLst
    #Not a list
    elif isinstance(lst, str) and all(isinstance(item, str) for item in lst):
        inputKeyLst = []
        if strip(lst) == "":
            return None
        else:
            i = 1
            inputKey = upper(lst)
            # ONLY FOR GREP - WE DON'T WANT TO WASTE TIMES FINDING A WORD AGAIN
            if not isGrep:
                inputKey = " "+inputKey+" "
            inputKeyLst.append(inputKey)

        if isGrep:
            inputKeyLst = check_if_substring(inputKeyLst)
        return inputKeyLst
    else:
        print("SETUP FAILURE: List of keywords contains something other than strings...")
        sys.stdout.flush()
        return None

def search_option(option):
    """ SETS THE LIST OF SEARCH OPTION PROVIDED IN THE FSW_NAMELIST. Prints to display."""
    remove = list.remove
    if isinstance(option, list) and all(isinstance(item, str) for item in option):
        if "" in option:
            remove(option, "")
        if not option:
            return None
        return True
    else:
        print("SETUP FAILURE: List of products contains something other than strings...")
        sys.stdout.flush()
        return None


def set_year_range(start, end):
    """ SETS THE YEAR RANGE PROVIDED IN THE FSW_NAMELIST. Prints to display."""
    ADMIN_SET_MIN = 1996
    ADMIN_SET_MAX = int(time.ctime()[-4:])  # Current year

    if not isinstance(start, int) or not isinstance(end, int):
        if str(start).isdigit() and str(end).isdigit():
            start = int(start)
            end = int(end)
        else:
            return None, None

    # You might be living in the future, but we're all living in the present.
    if end >= ADMIN_SET_MAX + 1:
        print("SETUP FAILURE: Invalid end year. Must not be higher than current year...")
        print("Redo with correct year range\n")
        sys.stdout.flush()
        return None, None

    # ha you're funny
    if (start < ADMIN_SET_MIN or start >= ADMIN_SET_MAX + 1) and end <= ADMIN_SET_MAX:
        print("SETUP FAILURE: Invalid start year... Valid options: 1996 - Current Year...")
        ## IEM DATA MESSAGE
        print("Start year out of range [1996 - Current Year]. Check your TEXT_DATA"+\
              " folder and refer below (from Iowa Mesonet)")

        print("1996 thru 2000: Very sparse and incomplete, selectively backfilled as"+\
              " archives have been found.")

        print("Also note that product source IDs are possibly different back then"+\
              " (prior to NWS Modernization).")

        print("Known holes exist at: 29 Oct-1 Nov 1998, 24-27 Dec 1998, 25-28 Jul"+\
              " 1999, 21-25 Jan 2000, 26-27 Mar 2000 \n\n")

        print("2001 thru 2007: More consistent archives, but still likely missing"+\
              " things. Much better coverage though.")

        print("2008 thru now: Very good data coverage and higher fidelity archiving.")

        print("\n\nIf your dataset does indeed exists prior to 1996. Then modify the"+\
              " get_year_range function in redo_finder_functions.py located in the"+\
              " src directory.\n")
        print("Otherwise redo with correct year range\n")
        sys.stdout.flush()

        return None, None

    # ASSUMPTION
    if start > end:
        tmp = end
        end = start
        start = tmp

    # Else: You didn't do something dumb! Yay!
    return start, end           ## NO PROBLEMS

def check_if_substring(lst):
    """ See if there are substring conflicts in the list of input keywords...Grep Only"""
    upper = str.upper
    lst2 = list(map(upper, lst))
    inputKeyNew = lst2[:]
    inputKeyNew.sort(key=len)
    keepKey = [inputKeyNew[0]]
    len_key = len(inputKeyNew)
    for ydx in range(1, len_key):
        print(inputKeyNew[ydx], keepKey)
        if any(kk in inputKeyNew[ydx] for kk in keepKey):
            print("REDUNDANT: REMOVING - ", inputKeyNew[ydx], "FROM THE LIST OF KEYWORDS...")
            sys.stdout.flush()
            continue
        elif inputKeyNew[ydx] not in keepKey:
            keepKey.append(inputKeyNew[ydx])
        else:
            print("REDUNDANT: REMOVING - ", inputKeyNew[ydx], "FROM THE LIST OF KEYWORDS...")
            sys.stdout.flush()
            continue

    output_lst = []
    for key in lst2:
        for new in keepKey:
            if key == new and key not in output_lst:
                output_lst.append(key)
                continue
    return output_lst
