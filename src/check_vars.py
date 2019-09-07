# Copyright (C) 2018-2019 Eric Allen - All Rights Reserved
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
import sys, os 
import time
from __future__ import print_function

def AndTrue_OrFalse(option):
    """ SETS THE isAnd OPTION PROVIDED IN THE FSW_NAMELIST. Prints to display."""
    if isinstance(option,bool):
        if option == True:
            return True
        elif option == False:
            return False
    else:
        return None   

def byforecast(option):
    """ SETS THE byforecast OPTION PROVIDED IN THE FSW_NAMELIST"""
    if isinstance(option,bool):
        if option == True:
            return True
        elif option == False:
            return False
    else:
        return None   

def makeAssumptions(option):
    """ SETS THE byforecast OPTION PROVIDED IN THE FSW_NAMELIST"""
    if isinstance(option,bool):
        if option == True:
            return True
        elif option == False:
            return False
    else:
        return None   

def grep_check(option):
    if isinstance(option,bool):
        if option == True:
            return True
        elif option == False:
            return False
    else:
        return None   
        
def debug_check(option):
    if isinstance(option,bool):
        if option == True:
            return True
        elif option == False:
            return False
    else:
        return None   
        
        
def input_words(lst, isGrep):
    """ SETS THE LIST OF KEYWORDS PROVIDED IN THE FSW_NAMELIST. Prints them to display."""
    if all(isinstance(item, str) for item in lst) and isinstance(lst,list):
        
        if " " in lst:
            lst.remove(" ")
            
        if "" in lst:
            lst.remove("")
            
        inputKeyLst = []
        if len(lst) < 1:
            print("Empty List of Words")#, flush=True)
            sys.stdout.flush()
            return None
        else:
            i = 0
            for word in lst:
                if word.strip() == "":
                    continue
                elif word.upper() in inputKeyLst and isGrep == True:
                    continue
                elif " "+word.upper()+" " in inputKeyLst and isGrep == False:
                    continue
                else:
                    i = i + 1
                    inputKey = word.upper()
                    if isGrep == False:
                        inputKey = " "+inputKey+" "
                    #print ("WORD "+str(i)+":  ", inputKey, flush=True)
                    inputKeyLst.append(inputKey)
            if isGrep == True:
                inputKeyLst = check_if_substring(inputKeyLst)
            return inputKeyLst
        
    elif all(isinstance(item, str) for item in lst) and isinstance(lst,str): # NOT A LIST...
        inputKeyLst = []
        if lst.strip() == "":
            return None
        else:
            i = 1
            inputKey = lst.upper()
            
            # ONLY FOR GREP SINCE WE DON'T WANT TO WASTE TIMES FINDING A WORD THAT WAS/WILL BE FOUND AGAIN
            if isGrep == False:
                inputKey = " "+inputKey+" "
            #print ("WORD "+str(i)+":  ", inputKey, flush=True)
            inputKeyLst.append(inputKey)
            
        # ONLY FOR GREP SINCE WE DON'T WANT TO WASTE TIMES FINDING A WORD THAT WAS/WILL BE FOUND AGAIN
        if isGrep == True:
            inputKeyLst = check_if_substring(inputKeyLst)
        return inputKeyLst
    else:
        print("List of keywords contains something other than all strings...")#,flush=True)
        sys.stdout.flush()
        return None

def search_option(option):
    """ SETS THE LIST OF SEARCH OPTION PROVIDED IN THE FSW_NAMELIST. Prints to display."""

    if all(isinstance(item, str) for item in option) and isinstance(option,list):
        if "" in option:
            option.remove("") 
        if not option:
            return False
        return True
    else:
        print("FAILURE... USE DEFAULT SEARCH OPTIONS")
        sys.stdout.flush()
        return False


def set_year_range(start, end):
    """ SETS THE YEAR RANGE PROVIDED IN THE FSW_NAMELIST. Prints to display."""
    ADMIN_SET_MIN = 1996
    ADMIN_SET_MAX = int(time.ctime()[-4:])  # Current year
    
    if type(start) != int or type(end) != int:
        if str(start).isdigit() and str(end).isdigit():
            start = int(start)
            end = int(end)
        else:
            return None, None
        
    # You might be living in the future, but we're all living in the present.    
    if end >= ADMIN_SET_MAX + 1:
        print("\nThis year has not happened yet. Choose a more recent end date - year\n")#, flush=True)
        print("Redo with correct year range\n")#, flush=True)
        sys.stdout.flush()
        return None, None
        
    # ha you're funny
    if (start < ADMIN_SET_MIN or start >= ADMIN_SET_MAX + 1) and end <= ADMIN_SET_MAX:
        
        ## IEM DATA MESSAGE
        print("Start year out of range [1996 - Current Year]. Check your TEXT_DATA folder and refer below (from Iowa Mesonet)")#, flush=True)
        print("1996 thru 2000: Very sparse and incomplete, selectively backfilled as archives have been found.")#, flush=True)
        print("Also note that product source IDs are possibly different back then (prior to NWS Modernization).")#, flush=True)
        print("Known holes exist at: 29 Oct-1 Nov 1998, 24-27 Dec 1998, 25-28 Jul 1999, 21-25 Jan 2000, 26-27 Mar 2000 \n\n")#, flush=True)
        print("2001 thru 2007: More consistent archives, but still likely missing things. Much better coverage though.")#, flush=True)
        print("2008 thru now: Very good data coverage and higher fidelity archiving.")#, flush=True)
        print("\n\nIf your dataset does indeed exists prior to 1996. Then modify the get_year_range function in redo_finder_functions.py located in the src directory.\n")#, flush=True)
        print("Otherwise redo with correct year range\n")#, flush=True)
        sys.stdout.flush()

        return None, None
    
    if start > end:
        tmp = end
        end = start
        start = tmp
        
    # Else: You didn't do something dumb! Yay!
    return start, end           ## NO PROBLEMS

def check_if_substring(lst):
    """ See if there are substring conflicts in the list of input keywords...Grep Only"""
    lst2 = [l.upper() for l in lst]
    inputKeyNew = lst2[:]
    inputKeyNew.sort(key=len)
    keepKey = [inputKeyNew[0].upper()]
    for y in range(1, len(inputKeyNew)):
        if any(kk in inputKeyNew[y].upper() for kk in keepKey):
            print("REDUNDANT: REMOVING: ", inputKeyNew[y].upper(),"FROM THE LIST OF KEYWORDS...")#,flush=True)
            sys.stdout.flush()
            continue
        elif inputKeyNew[y].upper() not in keepKey:
            keepKey.append(inputKeyNew[y].upper())
        else:
            print("REDUNDANT: REMOVING: ", inputKeyNew[y].upper(),"FROM THE LIST OF KEYWORDS...")#,flush=True)
            sys.stdout.flush()
            continue
            
            
    output_lst = []
    for key in lst2:
        for new in keepKey:
            if key == new and key not in output_lst:
                output_lst.append(key)
                continue
    return output_lst