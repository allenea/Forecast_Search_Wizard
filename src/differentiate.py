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
# Please properly cite code, derivative code, and outputs
# of the Forecast Search Wizard in all scholarly work and
# publications.
#
# Imports
from __future__ import print_function
import re

def word_in_list_sym(key_check, lst):
    """ Prevents duplicates for a single keyword in the output file.

    Parameters:
        key_check (str): Keyword being checked against the list
        lst (list of str): Original list of strings being processed in sort_t for each iteration.
                            (keywords found)

    Returns:
        lst (list): Modified list of strings (Keywords with any flags required)
    """
    # IF WORD OR SUBWORD IN THE LIST ALREADY
    if re.sub('[#*]', '', key_check) in str(lst):
    #if re.sub('[#*]', '', key_check) in lst: -- doesn't help with the not identicals

        # SEE IF THERE IS AN IDENTICAL MATCH.. If there is move on.
        if key_check in lst:
            pass

        # NOT AN IDENTICAL MATCH: new keyword (different prefix/suffix) or sub-word
        else:
            word = re.sub('[#*]', '', key_check)
            symbol = re.sub('[^#*]', '', key_check)
            fkf = [re.sub('[#*]', '', k1) for k1 in lst]
            indices = [i for i, s in enumerate(fkf) if word == s]

            # IS IT A NEW KEYWORD??
            # No: IF SUBWORD WITH SYMBOLS
            if len(indices) == 0:
                lst.append(key_check)
            
            elif word == fkf[indices[0]]:
                lst[indices[0]] = lst[indices[0]] + symbol

            #Yes: Add it
            else:
                lst.append(key_check)

    # IF WORD OR SUBWORD IS NOT IN LIST ADD IT....
    else:
        lst.append(key_check)

    return lst
