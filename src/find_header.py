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
#import sys

STR_SWPC = ":PRODUCT: DAILY SPACE WEATHER SUMMARY AND FORCAST DAYDSF.TXT"
TOTAL_FORECAST = ['NATIONAL WEATHER SERVICE', 'NATIONAL HURRICANE CENTER',\
                  'STORM PREDICTION CENTER', 'TROPICAL PREDICTION CENTER',\
                 'NWS WEATHER PREDICTION CENTER', 'NWS CLIMATE PREDICTION CENTER',\
                 'OCEAN PREDICTION CENTER', 'NCEP PROGNOSTIC DISCUSSION FROM',\
                 'CENTRAL PACIFIC HURRICANE CENTER', 'HYDROMETEOROLOGICAL PREDICTION CENTER',\
                 'MARINE PREDICTION CENTER', 'SPACE WEATHER MESSAGE CODE', ':ISSUED:',\
                 'HPC FORECAST VALID', 'ALASKA FORECAST DISCUSSION',\
                 'SOUTHCENTRAL AND SOUTHWEST ALASKA', "IN SPC BACKUP CAPACITY",\
                 "NATIONAL CENTERS FOR ENVIRONMENTAL PREDICTION",\
                 "CLIMATE PREDICTION CENTER NCEP",\
                 "NEW YORK STATEWIDE POLICE INFORMATION NETWORK", "HIGH SEAS FORECAST"]

ID_TOP_FCST = ['NATIONAL WEATHER SERVICE', "OCEAN PREDICTION CENTER",\
               'MARINE PREDICTION CENTER', 'NATIONAL HURRICANE CENTER',\
               'TROPICAL PREDICTION CENTER', 'ALASKA FORECAST DISCUSSION',\
               'SOUTHCENTRAL AND SOUTHWEST ALASKA'] #'TROPICAL ANALYSIS AND FORECAST BRANCH'

ID_TOP_FCST2 = ['NWS CLIMATE PREDICTION CENTER', 'NWS WEATHER PREDICTION CENTER',\
                "IN SPC BACKUP CAPACITY", 'STORM PREDICTION CENTER',\
                'HYDROMETEOROLOGICAL PREDICTION CENTER', "CENTRAL PACIFIC HURRICANE CENTER",\
                "NATIONAL CENTERS FOR ENVIRONMENTAL PREDICTION", "CLIMATE PREDICTION CENTER NCEP"]

ID_TOP_FCST3 = ["NCEP PROGNOSTIC DISCUSSION FROM", "HPC FORECAST VALID",\
                'SPACE WEATHER MESSAGE CODE', ':ISSUED:',\
                "NEW YORK STATEWIDE POLICE INFORMATION NETWORK", "HIGH SEAS FORECAST"]

def find_header_nws(read_data, idx, int_year):
    """docstring"""
    str_year = str(int_year)
    str_year_plus = str(int_year+1)
    #check and see if the expected year is in the next row
    if str_year in read_data[idx+1]:
        return idx+1, True
    # if next line says product was issued by someone else
    elif "ISSUED BY" in read_data[idx+1]:
        #Check one line further for correct year
        if str_year in read_data[idx+2]:
            return idx+2, True
        #see if the next line down is empty and go the the next
        elif len(read_data[idx+2]) < 4:
            # Does the next line have the year if not then skip
            if str_year in read_data[idx+3]:
                return idx + 3, True
            elif str_year_plus in read_data[idx+3]:
                return idx + 3, True
            else:
                return None, False
        #if the next line has the next year because it's at the end/start of yr
        elif str_year_plus in read_data[idx+2]:
            return idx+2, True
        else:
            return None, False
    #if the next line has the next year because it's at the end/start of year
    elif str_year_plus in read_data[idx+1]:
        return idx+1, True
    elif str_year in read_data[idx]:
        return idx, True
    ## REQ FOR PSR 1999 - DEC.. 2 upside down backwards ? were causing problems
    elif read_data[idx+1] == '\n':
        #If it's the expected year
        if str_year in read_data[idx+2]:
            return idx+2, True
        #If the next year
        elif str_year_plus in read_data[idx+2]:
            return idx+2, True
        elif str(int_year-1) in read_data[idx+2]:
            return idx+2, True
        elif str(int_year-1) in read_data[idx]:
            return idx, True
        else:
            return None, False
    elif str(int_year-1) in read_data[idx+1]:
        return idx+1, True
    elif read_data[idx+1] == "":
        if str_year in read_data[idx+2]:
            return idx+2, True
        elif str_year_plus in read_data[idx+2]:
            return idx+2, True
        else:
            return None, False
    else:
        return None, False


def find_header(read_data, idx, int_year, wfo):
    """function to finder header line"""
    str_year = str(int_year)
    str_year_plus = str(int_year+1)
    #DUPLICATE FOR TESTING ONLY....
    if any(TOP2 in read_data[idx] for TOP2 in ID_TOP_FCST2)\
                    and ("ISSUED BY" not in read_data[idx]):
        #check and see if the expected year is in the next row
        if str_year in read_data[idx+1]:
            return idx+1, True
        # if next line says product was issued by someone else
        elif "ISSUED BY" in read_data[idx+1]:
            #Check one line further for correct year
            if str_year in read_data[idx+2]:
                return idx+2, True
            #see if the next line down is empty and go the the next
            elif len(read_data[idx+2]) < 4:
                # Does the next line have the year if not then skip
                if str_year in read_data[idx+3]:
                    return idx + 3, True
                elif str_year_plus in read_data[idx+3]:
                    return idx + 3, True
                else:
                    return None, False
            #if the next line has the next year because it's at the end/start of yr
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        #if the next line has the next year because it's at the end/start of year
        elif str_year_plus in read_data[idx+1]:
            return idx+1, True
        elif str_year in read_data[idx]:
            return idx, True
        ## REQ FOR PSR 1999 - DEC.. 2 upside down backwards ? were causing problems
        elif read_data[idx+1] == '\n':
            #If it's the expected year
            if str_year in read_data[idx+2]:
                return idx+2, True
            #If the next year
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            elif str(int_year-1) in read_data[idx+2]:
                return idx+2, True
            elif str(int_year-1) in read_data[idx]:
                return idx, True
            else:
                return None, False
        elif "CENTRAL PACIFIC HURRICANE CENTER" in read_data[idx]:
            if "HONOLULU HI" in read_data[idx+1]:
                #If it's the expected year
                if str_year in read_data[idx+2]:
                    return idx+2, True
                #If the next year
                elif str_year_plus in read_data[idx+2]:
                    return idx+2, True
                else:
                    return None, False
            else:
                #If it's the expected year
                if str_year in read_data[idx+1]:
                    return idx+1, True
                #If the next year
                elif str_year_plus in read_data[idx+1]:
                    return idx+1, True
                elif str(int_year-1) in read_data[idx+1]:
                    return idx+1, True
                else:
                    return None, False
        elif str(int_year-1) in read_data[idx+1]:
            return idx+1, True
        ### EXCEPTION BECAUSE AUTOFORMATTING OF PRODUCT DIDN'T ACCOUNT
        ####    FOR THE TURN OF THE CENTURY - NWS END
        elif wfo == "PMDTHR" and "CLIMATE PREDICTION CENTER NCEP" in read_data[idx]:
            if str_year in read_data[idx+1]:
                return idx+1, True
            elif str(int_year-100) in read_data[idx+1]:
                return idx+1, True
            elif str(int_year-100) in read_data[idx+2]:
                return idx+2, True
            elif str_year in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        elif read_data[idx+1] == "":
            if str_year in read_data[idx+2]:
                return idx+2, True
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        else:
            return None, False
    elif any(TOP in read_data[idx] for TOP in ID_TOP_FCST) and\
                            ("FORECASTER" not in read_data[idx]):
        #check and see if the expected year is in the next row
        if str_year in read_data[idx+1]:
            return idx+1, True
        # if next line says product was issued by someone else
        elif "ISSUED BY" in read_data[idx+1]:
            #Check one line further for correct year
            if str_year in read_data[idx+2]:
                return idx+2, True
            #see if the next line down is empty and go the the next
            elif len(read_data[idx+2]) < 4:
                # Does the next line have the year if not then skip
                if str_year in read_data[idx+3]:
                    return idx + 3, True
                elif str_year_plus in read_data[idx+3]:
                    return idx + 3, True
                else:
                    return None, False
            #if the next line has the next year because it's at the end/start of yr
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        #if the next line has the next year because it's at the end/start of yr
        elif str_year_plus in read_data[idx+1]:
            return idx+1, True
        elif read_data[idx+1] == '\n':
            #If it's the expected year
            if str_year in read_data[idx+2]:
                return idx+2, True
            #If the next year
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            elif str_year in read_data[idx]:
                return idx, True
            else:
                return None, False
        elif str(int_year-1) in read_data[idx+1]:
            return idx+1, True
        elif str(int_year) in read_data[idx]:
            return idx, True
        #FOR OFFNT PRODUCTS
        elif "ANALYSIS AND FORECAST BRANCH" in read_data[idx+1]:
            #Check one line further for correct year
            if str_year in read_data[idx+2]:
                return idx+2, True
            #see if the next line down is empty and go the the next
            elif len(read_data[idx+2]) < 4:
                # Does the next line have the year if not then skip
                if str_year in read_data[idx+3]:
                    return idx + 3, True
                elif str_year_plus in read_data[idx+3]:
                    return idx + 3, True
                else:
                    return None, False
            #if the next line has the next year because it's at the end/start of yr
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        elif read_data[idx+1] == "":
            if str_year in read_data[idx+2]:
                return idx+2, True
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        else:
            return None, False
    elif any(TOP3 in read_data[idx] for TOP3 in ID_TOP_FCST3):
        ## FOR OLD NCEP PRODUCTS - WORKING
        if"NCEP PROGNOSTIC DISCUSSION FROM" in read_data[idx]:
            return idx, True
        ## FOR OLD NCEP HI PRODUCTS - WORKING
        elif "HPC FORECAST VALID" in read_data[idx]:
            return idx, True
        ## ALL CASES FOR SWPC
        elif 'SPACE WEATHER MESSAGE CODE' in read_data[idx]:
            if "SERIAL NUMBER" in read_data[idx+1]:
                if 'ISSUED BY' in read_data[idx+2]:
                    if str_year in read_data[idx+2]:
                        return idx +2, True
                    elif str_year_plus in read_data[idx+2]:
                        return idx +2, True
                    else:
                        return None, False
                elif 'ISSUE TIME' in read_data[idx+2]:
                    if str_year in read_data[idx+2]:
                        return idx +2, True
                    elif str_year_plus in read_data[idx+2]:
                        return idx +2, True
                    else:
                        return None, False
                else:
                    return None, False
            else:
                if 'ISSUED BY' in read_data[idx]:
                    if str_year in read_data[idx+1]:
                        return idx+1, True
                    elif str_year_plus in read_data[idx+1]:
                        return idx+1, True
                    else:
                        return None, False
                else:
                    return None, False
        elif ':ISSUED:' in read_data[idx]:
            if str_year in read_data[idx]:
                return idx, True
            elif str_year_plus in read_data[idx]:
                return idx, True
            else:
                return None, False
        #LSRNY products
        #LSRNY4 - 2009 did not have a date/time
        elif "TROOP" in read_data[idx+1]:
            if len(read_data[idx+2]) < 6:
                if str_year in read_data[idx+3]:
                    return idx+3, True
                elif str_year_plus in read_data[idx+3]:
                    return idx+3, True
                else:
                    return None, False
            if str_year in read_data[idx+2]:
                return idx+2, True
            elif str_year_plus in read_data[idx+2]:
                return idx+2, True
            else:
                return None, False
        elif len(read_data[idx+1]) < 6:
            if "TROOP" in read_data[idx+2]:
                if str_year in read_data[idx+3]:
                    return idx+3, True
                elif str_year_plus in read_data[idx+3]:
                    return idx+3, True
                elif len(read_data[idx+3]) < 6:
                    if str_year in read_data[idx+4]:
                        return idx+4, True
                    elif str_year_plus in read_data[idx+4]:
                        return idx+4, True
                    else:
                        return None, False
                else:
                    return None, False
            else:
                return None, False
        elif str_year in read_data[idx+1]:
            return idx+1, True
        elif str_year_plus in read_data[idx+1]:
            return idx+1, True
        elif str_year in read_data[idx+2]:
            return idx+2, True
        elif str_year_plus in read_data[idx+2]:
            return idx+2, True
        else:
            return None, False
    else:
        return None, False
