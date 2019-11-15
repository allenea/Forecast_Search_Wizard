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
import calendar
from datetime import datetime
import pytz
from src.time_functions import getDDHHMM

def checkEverything(LST, GMT, year, month, text_day, iYear, timezone):
    """Take all the given information and create the best timestamp"""
    fday = -1
    fmon = -1
    fyr = -1
    is_assumed = False
    had_to_use_local = False
    #cmonthdays = calendar.monthlen(year, month) #V3.7 and future
    cmonthdays = calendar.monthrange(year, month)[1] #BEST PRE 3.7

    if LST is None:
        if GMT != "999999":
            gday, ghr, gmin = getDDHHMM(GMT)
            if gday >= text_day:
                if gday == text_day:
                    fday = gday
                elif abs(gday - text_day) == 1:
                    fday = text_day + 1
                else:
                    if gday >= cmonthdays and text_day == 1:
                        fday = gday
                        month = month - 1
                        if month == 0:
                            month = 12
                            fyr = year - 1
                    else:
                        return None, None

            else:
                if abs(gday - text_day) == 1:
                    fday = gday
                if gday == 1 and text_day >= cmonthdays:
                    fday = gday
                    month = month + 1
                    if month > 12:
                        month = 1
                        fyr = year + 1
                else:
                    return None, None
        fhour = int(ghr)
        fminute = int(gmin)

    elif GMT != "999999":
        gday, ghr, gmin = getDDHHMM(GMT)
        if text_day is None:
            fday = gday
            fhour = int(ghr)
            fminute = int(gmin)
        elif gday == text_day:
            fday = gday
            fhour = int(ghr)
            fminute = int(gmin)

        elif gday > text_day:
            if abs(gday - text_day) == 1:
                fday = gday
            else:
                if gday >= cmonthdays and text_day == 1:
                    #More reason to go with the header.... than text_day
                    fday = gday
                    month = month - 1
                    if month == 0:
                        month = 12
                        fyr = year - 1
                else:
                    return None, None
        else:
            if abs(text_day - gday) == 1:
                fday = gday
            else:
                if gday == 1 and text_day >= cmonthdays:
                    fday = gday
                    month = month + 1
                    if month > 12:
                        month = 1
                        fyr = year + 1
                else:
                    return None, None
        fhour = int(ghr)
        fminute = int(gmin)
    else:
        fday = text_day
        fhour = int(LST[:2])
        fminute = int(LST[2:])
        had_to_use_local = True
        timezone_str = timezone

    if fday > cmonthdays:
        fday = 1
        month = month + 1
        if month > 12:
            fyr = year + 1

    if fyr == -1:
        if year == iYear:
            fyr = year
        elif year is None:
            fyr = iYear
            is_assumed = True
        elif year == iYear + 1:
            if month == 1:
                fyr = year
            elif month == 12:
                fyr = iYear
            else:
                fyr = year
                is_assumed = True
        elif year == iYear - 1:
            if month == 12:
                fyr = year
            elif month == 1:
                fyr = iYear
            else:
                fyr = year
                is_assumed = True
        else:
            fyr = year
            is_assumed = True
    else:
        if abs(fyr - iYear) <= 1 and month in (1, 12):
            pass
        else:
            is_assumed = True
            fyr = year

    if abs(fyr-iYear) > 1:
        fyr = year
        is_assumed = True

    fmon = month
    if had_to_use_local:
        dt_tuple = datetime(fyr, fmon, fday, fhour, fminute, tzinfo=pytz.timezone(timezone_str))
    else:
        try:
            dt_tuple = datetime(fyr, fmon, fday, fhour, fminute, tzinfo=pytz.timezone("UTC"))
        except:
            return None, None

    return dt_tuple, is_assumed
