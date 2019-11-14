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
#import datetime
from src.differentiate import word_in_list_sym

#%%TESTED
def sort_time(dt_tuple, key_found, by_forecast):
    """ Sorting that combines the unique keywords while keeping the integrity and
    reformatting the date/time string. If the search is done by the day and not by
    the forecast then it is using the first instance.

    Parameters:
        dt_tuple (list): A list of datetime tuples of the cases found
        key_found (list): A list of the keywords found for each case
        by_forecast (bool): Search by forecast (True) or search by day (False)

    Returns:
        final_reformat_2_str (list): A list w/o duplicate times (final list of cases) as str type
        final_Key_Found (list of lists):  A list w/o duplicate keywords for each case
                                        (final list of keywords per case)
    """
    count2 = 0
    strp_fmt = "%m-%d-%Y %H:%M"
    # By forecast - Keep all instances
    if by_forecast:
        t_fmt = "%m-%d-%Y %H:%M"
        lastday = '00-00-0000 00:00'
    #By day - Only keeping the first instance
    else:
        t_fmt = "%m-%d-%Y"
        lastday = '00-00-0000'

    # ZIP/SORT/UNZIP
    dt_sorted, keys = zip(*sorted(zip(dt_tuple, key_found)))

    #declare/intialize an empty array
    final_reformat_2_str = [None] * len(dt_sorted)
    final_key_found = [None] * len(dt_sorted)

    #Iterate through the list of datetimes
    for idx, dt_sort1 in enumerate(dt_sorted):

        #Format as a string depending on search type
        now = dt_sort1.strftime(t_fmt)

        #Check and see if it's the same as the last date (only want one)
        if now == lastday:
            #If the key was not the same as what is already stored for that timestep add the new key
            final_key_found[count2-1] = word_in_list_sym(keys[idx], final_key_found[count2-1])

        #elif now != lastday:  add to the list - first instance in that day
        else:

            #string format the dt object - !! Could consider ging with the t_fmt ONLY
            final_reformat_2_str[count2] = dt_sort1.strftime(strp_fmt)

            final_key_found[count2] = [keys[idx]]
            lastday = now
            count2 += 1

    #Trim and return the part of the array that WAS USED
    return final_reformat_2_str[:count2], final_key_found[:count2]
