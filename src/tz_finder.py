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
import re
#import sys

WK_DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
ST_LST = ["EST", "CST", "MST", "PST", "AST", "SST", "AKST", "HAST",\
          "HST", "CHST", "ChST", "GUAM LST", "LST"]
DT_LST = ["EDT", "CDT", "MDT", "PDT", "AKDT", "HADT", "SDT", "ADT"]

def timezone_finder(read_data, iholder, last_tz):
    """ Identifies the date/time information and an acceptable time zone. Stops.

    Parameters:
        read_data (list of strings): Raw text data
        iholder (int): Index of suspected date/time information in the list of strings
        last_tz (str): The last timezone used in this product
                        (most likely the same as the next more times than not)

    Returns:
        date (str): Actually the time! info
        time (str): Actually the date! info
        timezone (str): pytz formatted time zone equivalent to the abbriviation
    """

    line = read_data[iholder]
    line = line.split("..")[0]
    strip = str.strip
    split = str.split

    #LEGACY PRODUCTS
    if "ISSUE" in line:
        # SPWC  - uses colons so use before the colon removal
        if  "ISSUED:" in line:
            if "UTC" in line:
                tmp = split(line, "ISSUED:")
                disc1 = strip(tmp[1])
                tmp2 = split(disc1, "UTC")
                date = strip(tmp2[0])
                return strip(date[-4:]), strip(date[:-4]), "UTC"

        elif "ISSUE:" in line:
            if "UTC" in line:
                tmp = split(line, "ISSUE:")
                disc1 = strip(tmp[1])
                tmp2 = split(disc1, "UTC")
                date = strip(tmp2[0])
                return strip(date[-4:]), strip(date[:-4]), "UTC"

        elif  "ISSUE TIME:" in line:
            if "UTC" in line:
                tmp = split(line, "ISSUE TIME:")
                disc1 = strip(tmp[1])
                tmp2 = split(disc1, "UTC")
                date = strip(tmp2[0])
                return strip(date[-4:]), strip(date[:-4]), "UTC"
    if "UT" in line:
        # ["HPC FORECAST VALID 00 UTC 1 JAN THRU 00 UTC 8 JAN 2002"]
        # [" 00 UTC 1 JAN THRU 00 UTC 8 JAN 2002"]
        # [" 00 UTC 1 JAN ", " 00 UTC 8 JAN 2002"]
        # [" 00 UTC 1 JAN "], +  [" 00 " "UTC"  "8" "JAN" "2002"] [ -1]
        # [" 00 UTC 1 JAN 2002"]
        # [00] ___ [1 JAN 2002] [UTC]
        if "HPC FORECAST" in line:
            tmp = split(line, "VALID")[1]
            tmp = split(tmp, "THRU")
            tmp2 = tmp[0]
            new_string = ''.join([tmp2, split(tmp[1])[-1]])
            new = split(new_string, "UTC")
            return strip(new[0]), strip(new[1]), "UTC"

        if "UTC" in line:
            if ":" in line:
                tmp = split(line, ":")
                tmp2 = split(tmp[2], "UTC")
                date = strip(tmp2[0])
                return strip(date[-4:]), strip(date[:-4]), "UTC"
            else:
                tmp = split(line, "UTC")
                date = strip(tmp[0])
                time = strip(tmp[1])
                return strip(date), strip(time), "UTC"

        # ASSUMPTION - UTC SPELLED WRONG - FOR SWPC
        if "DT" in line and any(dt in line for dt in DT_LST):
            pass
        elif "ST" in line and any(dt in line for dt in ST_LST):
            pass
        else:# "UT" in line:
            line = "".join(split(line, ":"))
            tmp = split(line, "ISSUED")
            disc1 = strip(tmp[1])
            tmp2 = split(disc1, "UT")
            date = strip(tmp2[0])
            return strip(date[-4:]), strip(date[:-4]), "UTC"

    #Remove : from names
    line = "".join(split(line, ":"))
    #Remove between the ( )
    line = re.sub(r" ?\([^)]+\)", "", line)

    # LEGACY PRODUCT
    if ("NCEP PROGNOSTIC DISCUSSION").upper() in line:
        #"NCEP PROGNOSTIC DISCUSSION FROM 0000Z MON DEC 24 2001
        tmp = split(line, "FROM")[1]
        if "Z" in tmp:
            tmp2 = split(tmp, "Z")
            return strip(tmp2[0]), strip(tmp2[1]), "UTC"
        else:
            tmp2 = tmp
            # Weekday name is included
            if any(word in tmp2 for word in WK_DAYS):
                for word in WK_DAYS:
                    if word in tmp2:
                        tmp3 = split(tmp2, word)
                        return strip(tmp3[0]), strip(tmp3[1]), "UTC"

    # NWS MODERNIZATION - STANDARD FORM
    if "DT" in line and any(dt in line for dt in DT_LST):
        if "EDT" in line:
            date = split(line, "EDT")
            return strip(date[0]), strip(date[1]), "US/Eastern"

        elif "CDT" in line:
            date = split(line, "CDT")
            return strip(date[0]), strip(date[1]), "US/Central"

        elif "MDT" in line:
            date = split(line, "MDT")
            return strip(date[0]), strip(date[1]), "US/Mountain"

        elif "PDT" in line:
            date = split(line, "PDT")
            return strip(date[0]), strip(date[1]), "US/Pacific"

        elif "AKDT" in line:
            date = split(line, "AKDT")
            return strip(date[0]), strip(date[1]), "US/Alaska"

        elif "HADT" in line:
            date = split(line, "HADT")
            return strip(date[0]), strip(date[1]), "Pacific/Honolulu"

        elif "SDT" in line:
            date = split(line, "SDT")
            return strip(date[0]), strip(date[1]), "US/Samoa"

        elif "ADT" in line:
            date = split(line, "ADT")
            return strip(date[0]), strip(date[1]), "America/Halifax"


    if "ST" in line and any(st in line for st in ST_LST):
        # COULD BE AN ASSUMPTION: "WEST OF THE ..."
        if "EST" in line:
            date = split(line, "EST")
            return strip(date[0]), strip(date[1]), "US/Eastern"

        elif "CST" in line:
            date = split(line, "CST")
            return strip(date[0]), strip(date[1]), "US/Central"

        elif "MST" in line:
            date = split(line, "MST")
            return strip(date[0]), strip(date[1]), "US/Mountain"

        elif "PST" in line:
            date = split(line, "PST")
            return strip(date[0]), strip(date[1]), "US/Pacific"

        elif "HAST" in line:
            date = split(line, "HAST")
            return strip(date[0]), strip(date[1]), "Pacific/Honolulu"

        elif "AST" in line:
            if "EASTERN" in line:
                date = split(line, "EASTERN")
                return strip(date[0]), strip(date[1]), "US/Eastern"
            else:
                date = split(line, "AST")
                return strip(date[0]), strip(date[1]), "America/Halifax"

        elif "SST" in line:
            date = split(line, "SST")
            return strip(date[0]), strip(date[1]), "US/Samoa"

        elif "AKST" in line:
            date = split(line, "AKST")
            return strip(date[0]), strip(date[1]), "US/Alaska"

        elif "CHST" in line:
            date = split(line, "CHST")
            return strip(date[0]), strip(date[1]), "Pacific/Guam"

        elif "ChST" in line:
            date = split(line, "ChST")
            return strip(date[0]), strip(date[1]), "Pacific/Guam"

        elif "HST" in line:
            date = split(line, "HST")
            return strip(date[0]), strip(date[1]), "Pacific/Honolulu"

        elif "GUAM LST" in line:
            date = split(line, "GUAM LST")
            return strip(date[0]), strip(date[1]), "Pacific/Guam"

        elif "LST" in line and "TIYAN" in read_data[iholder-1] or "PAGO" in read_data[iholder-1]:
            date = split(line, "LST")
            return strip(date[0]), strip(date[1]), "Pacific/Guam"

    if "GMT" in line:
        date = split(line, "GMT")
        return strip(date[0]), strip(date[1]), "UTC"

    # ASSUMPTION - FOR ONE MORON
    elif "EASTERN" in line:
        date = split(line, "EASTERN")
        return strip(date[0]), strip(date[1]), "US/Eastern"
    # ASSUMPTION
    elif "CENTRAL" in line:
        date = split(line, "CENTRAL")
        return strip(date[0]), strip(date[1]), "US/Central"

    ## If you made it this far it is not one of the above so start if/elif/ over again
    ## FINAL EXCEPTION FOR MISSING TIME ZONE INFO.... OR NOT TIME
    if any(word in line for word in WK_DAYS):
        for word in WK_DAYS:
            if word in line:
                if "." in line:
                    line = line.lstrip(".")
                    tmp = split(line, ".")
                    tmp2 = split(tmp[0], word)
                    return strip(tmp2[0]), strip(tmp2[1]), last_tz
                else:
                    tmp2 = split(line, word)
                    return strip(tmp2[0]), strip(tmp2[1]), last_tz

    elif len(strip(line)) < 9: # WAS 5... NOW 9
        iholder += 1
        if iholder < len(read_data):
            return timezone_finder(read_data, iholder, last_tz)
        else:
            return

    # Used in like 4 cases for SWPC
    elif "SERIAL NUMBER" in line:
        iholder += 1
        if iholder < len(read_data):
            return timezone_finder(read_data, iholder, last_tz)
        else:
            return

    elif "PM" in line:
        date = split(line, "PM")
        return strip(date[0]), strip(date[1]), last_tz

    elif "AM" in line:
        date = split(line, "AM")
        return strip(date[0]), strip(date[1]), last_tz


    else:
        total_forecast = ['NATIONAL WEATHER SERVICE', 'OCEAN PREDICTION CENTER',\
                 'NATIONAL HURRICANE CENTER',\
                 'STORM PREDICTION CENTER', 'TROPICAL PREDICTION CENTER',\
                 'NWS WEATHER PREDICTION CENTER', 'NWS CLIMATE PREDICTION CENTER',\
                 'NCEP PROGNOSTIC DISCUSSION FROM',\
                 'CENTRAL PACIFIC HURRICANE CENTER', 'HYDROMETEOROLOGICAL PREDICTION CENTER',\
                 'MARINE PREDICTION CENTER', 'SPACE WEATHER MESSAGE CODE', ':ISSUED:',\
                 'HPC FORECAST VALID', 'ALASKA FORECAST DISCUSSION',\
                 'SOUTHCENTRAL AND SOUTHWEST ALASKA', "IN SPC BACKUP CAPACITY",\
                 "NATIONAL CENTERS FOR ENVIRONMENTAL PREDICTION",\
                 "CLIMATE PREDICTION CENTER NCEP",\
                 "NEW YORK STATEWIDE POLICE INFORMATION NETWORK", "HIGH SEAS FORECAST"]

        if any(tf in line for tf in total_forecast):
            iholder += 1
            return timezone_finder(read_data, iholder, last_tz)
        else:
            return "", "", ""
