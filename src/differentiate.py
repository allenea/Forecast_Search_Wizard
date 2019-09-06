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
# Please properly cite code, derivative code, and outputs
# of the Forecast Search Wizard in all scholarly work and
# publications.
#
# Imports
import re

def word_in_list_sym(keyCheck,lst):
    """ Prevents duplicates for a single keyword in the output file.

    Parameters:
        keyCheck (str): Keyword being checked against the list
        lst (list of str): Original list of strings being processed in sort_t for each iteration. (keywords found) 
        
    Returns:
        lst (list): Modified list of strings (Keywords with any flags required)
    """
    # IF WORD OR SUBWORD IN THE LIST ALREADY 
    if re.sub('[#*]', '', keyCheck) in str(lst):
            
        # SEE IF THERE IS AN IDENTICAL MATCH.. If there is move on.
        if keyCheck in lst:
            pass
        
        # NOT AN IDENTICAL MATCH: new keyword (different prefix/suffix) or subword
        else:
            word = re.sub('[#*]', '', keyCheck)
            symbol = re.sub('[^#*]', '', keyCheck)                  
            fKf = [re.sub('[#*]', '', k1) for k1 in lst]
            indices = [i for i, s in enumerate(fKf) if word == s]
            
            # IS IT A NEW KEYWORD??
            # No: IF SUBWORD WITH SYMBOLS
            if word == fKf[indices[0]]:
                lst[indices[0]] = lst[indices[0]] + symbol
                
            #Yes: Add it
            else:
                lst.append(keyCheck)
                
    # IF WORD OR SUBWORD IS NOT IN LIST ADD IT.... ###  elif re.sub('[#*]', '', keyCheck) not in str(lst):
    else:
        lst.append(keyCheck)
    
    return lst