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
import datetime
from src.differentiate import word_in_list_sym

#%%TESTED
def sort_time(dt_tuple,KeyFound,byForecast):
    """ Sorting that combines the unique keywords while keeping the integrity and reformatting the date/time string. If the search is done by the day and not by the forecast then it is using the first instance.
    
    Parameters:
        dt_tuple (list): A list of datetime tuples of the cases found
        KeyFound (list): A list of the keywords found for each case
        byForecast (bool): Search by forecast (True) or search by day (False)
        
    Returns:
        final_reformat_2_str (list): A list without duplicate times (final list of cases) as string type
        final_Key_Found (list of lists):  A list without duplicate keywords for each case (final list of keywords per case)
    """    

    #Initialize 5 variables
    count2 = 0
    std_fmt_input = "%Y%m%d%H%M"
    std_fmt_output = "%m-%d-%Y %H:%M"
    
    # By forecast - Keep all instances
    if byForecast == True:
        t_fmt = "%m-%d-%Y %H:%M"
        lastday='00-00-0000 00:00'
        
    #By day - only keep the first instance
    else:        
        t_fmt = "%m-%d-%Y"
        lastday='00-00-0000'
    
    #makes a string of YYYYMMDDHHMM used for comparison in the sort.
    # Does this for all datetime objects 
    dt_list = [dt.strftime(std_fmt_input) for dt in dt_tuple]
    
    # Zips to make a tuple that is then sorted based on the dt and KeyFound is
    # Sorted based on the sorting of dt_list.. It's then unzipped  and 2 variables
    # get the data for each
    
    # ZIP/SORT/UNZIP
    dt_presort, keys = zip(*sorted(zip(dt_list, KeyFound)))
    # Put time back into the datetime object.... for comparison below
    dt_sorted = [datetime.datetime.strptime(dtf,std_fmt_input) for dtf in dt_presort]
    
    #declare/intialize an empty array
    final_reformat_2_str = [None] * len(dt_sorted)
    final_Key_Found = [None] * len(dt_sorted)

    #Iterate through the list of datetimes
    for idx in range(len(dt_sorted)):
        
        #year month and day only of dt for comparison in UTC time
        now = dt_sorted[idx].strftime(t_fmt)

        #Check and see if it's the same as the last date (only want one)
        if now == lastday:
            #If the key was not the same as what is already stored for that timestep add the new key to the string
            final_Key_Found[count2-1] = word_in_list_sym(keys[idx], final_Key_Found[count2-1])   

        # not the same as the last day add to the list - first instance in that day
        else:# elif now != lastday:
            #string format the dt object
            final_reformat_2_str[count2] = dt_sorted[idx].strftime(std_fmt_output)
            final_Key_Found[count2] = [keys[idx]]            # save the keyword
            lastday = now         #set last day to current day
            count2 +=1            #Increase the indexer
        

    #Trim and return the part of the array that WAS USED
    return final_reformat_2_str[:count2],final_Key_Found[:count2]
