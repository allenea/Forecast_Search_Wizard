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

def covertSPC(iYear, text, DDHHMM):
    """TESTED - removed wfo as first arg"""
    isSuccess = False
    DATETIME_STRING = ""
    sYear = str(iYear)
    length_file = len(text)
    strip = str.strip

    for lineIDX in range(0, 151, 1):#ADMIN_MAX_ALLOW = 150
        #FAILURE
        if lineIDX == length_file:
            return DATETIME_STRING, isSuccess

        elif "NWS STORM PREDICTION CENTER NORMAN OK" in text[lineIDX]:
            if sYear in text[lineIDX + 1]:
                DATETIME_STRING = strip(text[lineIDX + 1])
                if DATETIME_STRING != "":
                    isSuccess = True
                    return DATETIME_STRING, isSuccess


            elif str(iYear + 1) in text[lineIDX + 1]:
                DATETIME_STRING = strip(text[lineIDX + 1])
                if DATETIME_STRING != "":
                    isSuccess = True
                    return DATETIME_STRING, isSuccess

        elif "...." in re.sub('[^.]+', '', text[lineIDX]):
            if  "//" in re.sub('[^/]+', '', text[lineIDX]):
                maybeDate = re.sub('[^0-9/]+', '', text[lineIDX])
                maybeDate = maybeDate.rstrip("/")
                maybeDate = maybeDate.lstrip("/")
                subLen = len(re.sub('[^0-9]+', '', maybeDate))
                if 4 <= subLen <= 8:
                #if  subLen >= 4 and subLen <= 8:
                    dateSPC = maybeDate.split("/")

                    if len(dateSPC) != 3:
                        continue
                    else:
                        month = dateSPC[-3]
                        day = dateSPC[-2]
                        year = dateSPC[-1]


                    if str(year) != sYear[-2:] or str(year) != sYear:
                        if len(year) == 4:
                            #LAPSE RATES ARE MARGINAL /I.E. 6.5 C/KM/...THOUGH 35-40 KT OF SWLY
                            if abs(int(sYear) - int(year)) > 1:
                                continue
                            #2000-2500 J/Kg
                            elif "2000-" in text[lineIDX]:
                                continue
                        else:
                            #...FOR THE PERIOD 25/12Z THROUGH 26/03Z...
                            #... 04/12Z-05/03Z ...
                            if abs(int(sYear[-2:]) - int(year)) > 1:
                                continue

                    if int(month) > 12:
                        continue

                    if int(day) > 31:
                        continue

                    if str(day) == str(DDHHMM[:2]):
                        day = DDHHMM[:2]

                    ## EVERYTHING IS GOOD
                    DATETIME_STRING, isBad = make_string(DDHHMM, year, month, day, iYear)#, wfo)

                    # IF IT'S GOOD....
                    if DATETIME_STRING != "" or not isBad:
                        isSuccess = True

                    return DATETIME_STRING, isSuccess
    # CERTAIN FAILURE
    return DATETIME_STRING, isSuccess


def make_string(DDHHMM, year, month, day, iYear):
    """TESTED"""
    isBad = False

    # ASSUMPTION - WE'LL ALLOW IT IF WITHIN "MARGIN OF ERROR"
    if abs(int(DDHHMM[:2]) - int(day)) > 1:
        # HAPPENS FREQUENTLY
        if DDHHMM[:2] == "01" and int(day) >= 28:
            month = int(month) + 1
            if month > 12:
                month = 1
                year = int(year) + 1
                if year == 100:
                    year = "00"
                else:
                    year = str(year)
                    if len(year) < 2:
                        year = "0" + year

        # DOES NOT APPEAR TO EVER HAPPEN...
        elif DDHHMM[:2] == "31" and int(day) == 1:
            month = int(month) - 1
            if month == 0:
                month = 12
                year = iYear - 1
                if year == -1:
                    year = "99"
                else:
                    year = str(year)
        #RARELY HAPPENS
        else:
            isBad = True

    #PUT IT TOGETHER
    strMONTH = getMonth(str(month))
    strYEAR = checkYear(year, iYear, strMONTH)

    if strYEAR == -9999:
        isBad = True

    HHMM = str(DDHHMM[2:])
    if int(DDHHMM[2:]) >= 1200:
        AMPM = "PM"
    else:
        AMPM = "AM"
    strNUMDAY = int(DDHHMM[:2])

    if not isBad:
        DATETIME_STRING = HHMM+" "+AMPM+" UTC "+ "NOTADAY"  + " " + strMONTH +\
                            " "+ str(strNUMDAY)+" " + str(strYEAR)
        return DATETIME_STRING, isBad
    else:
        DATETIME_STRING = ""
        return DATETIME_STRING, isBad


def getMonth(mo):
    """TESTED"""
    if mo.isdigit():
        intMonth = int(mo)
        if   intMonth == 1:
            month = "JAN"
        elif intMonth == 2:
            month = "FEB"
        elif intMonth == 3:
            month = "MAR"
        elif intMonth == 4:
            month = "APR"
        elif intMonth == 5:
            month = "MAY"
        elif intMonth == 6:
            month = "JUN"
        elif intMonth == 7:
            month = "JUL"
        elif intMonth == 8:
            month = "AUG"
        elif intMonth == 9:
            month = "SEP"
        elif intMonth == 10:
            month = "OCT"
        elif intMonth == 11:
            month = "NOV"
        elif intMonth == 12:
            month = "DEC"
        else:
            month = "NAN"
        return month
    else:
        return "NAN"

def checkYear(year, iYear, month):
    """TESTED"""
    if len(year) == 4:
        year = int(year)
    else:
        # They usually only used a 2 digit year
        if year > "90":
            year = int(str("19")+year)
        else:
            year = int(str("20")+year)

    if year == iYear:
        return iYear
    elif year == iYear + 1:
        # ASSUMPTION
        if month == "JAN":
            return iYear + 1
        # ASSUMPTION
        elif month == "DEC":
            return iYear
        else: return -9999
    elif year == iYear - 1:
        # ASSUMPTION
        if month == "DEC":
            return iYear - 1
        # ASSUMPTION
        elif month == "JAN":
            return iYear
        else:
            return -9999
    else:
        return -9999

ST_LST = ["EST", "MST", "PST", "AST", "SST", "AKST",\
          "HAST", "HST", "CHST", "ChST", "GUAM LST", "LST"]
DT_LST = ["EDT", "MDT", "PDT", "AKDT", "HADT", "SDT", "ADT"]
WK_DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
def timezone_finder_SPC(DATETIME_STRING, last_tz):
    """ Identifies the date/time information and an acceptable time zone. Stops.

    Parameters:
        DATETIME_STRING (str): Raw text data line created in Pre2003_SPC
        last_tz (str): The last timezone used in this product

    Returns:
        date (str): Actually the time! info
        time (str): Actually the date! info
        timezone (str): pytz formatted time zone equivalent to the abbriviation
    """
    line = DATETIME_STRING
    line = line.split("..")[0]
    strip = str.strip
    split = str.split

    if "CDT" in line:
        date = line.split("CDT")
        return date[0].strip(), date[1].strip(), "US/Central"
    if "CST" in line:
        date = line.split("CST")
        return date[0].strip(), date[1].strip(), "US/Central"

    if "UTC" in line:
        date = line.split("UTC")
        return date[0].strip(), date[1].strip(), "UTC"

    #Remove : from names
    line = "".join(line.split(":"))
    # remove between the ( )
    line = re.sub(r" ?\([^)]+\)", "", line)


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

    if "GMT" in line:
        date = split(line, "GMT")
        return strip(date[0]), strip(date[1]), "UTC"

    ## ASSUMPTION - 1 case
    elif "EASTERN" in line:
        date = split(line, "EASTERN")
        return strip(date[0]), strip(date[1]), "US/Eastern"

    # ASSUMPTION
    elif "CENTRAL" in line:
        date = split(line, "CENTRAL")
        return strip(date[0]), strip(date[1]), "US/Central"

    else:
        if any(word in line for word in WK_DAYS):
            for word in WK_DAYS:
                if word in line:
                    if "." in line:
                        tmp = split(line, ".")
                        tmp2 = split(tmp[0], word)
                        return strip(tmp2[0]), strip(tmp2[1]), last_tz
                    else:
                        tmp2 = split(line, word)
                        return strip(tmp2[0]), strip(tmp2[1]), last_tz

        elif "PM" in line:
            date = split(line, "PM")
            return strip(date[0]), strip(date[1]), last_tz

        elif "AM" in line:
            date = split(line, "AM")
            return strip(date[0]), strip(date[1]), last_tz

        else:
            return "", "", ""
