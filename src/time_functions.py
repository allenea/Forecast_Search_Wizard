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
import time
import datetime
import pytz

ADMIN_EARLIEST_YEAR = 1996
ADMIN_CURRENT_YEAR = int(time.ctime()[-4:])


WK_DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN", \
           "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", \
           "TUES", "WEDS", "THURS", "THUR"]

MO_STR = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", \
          "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", \
          "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", "SEPT", "0CT", "N0V", "0CT0BER", \
          "N0VEMBER"]

TZS = ["UTC", "EST", "EDT", "CDT", "CST", "MST", "MDT", "PDT", "PST", "AKDT", "AKST", "HST",
       "HAST", "HADT", "GMT", "GUAM LST", "ADT", "AST", "CHST", "SST", "SDT", "ChST"]

def getDay(t_nums, day_wmohead):
    """Do not look at dayWMOHEAD unless there are multiple possible day-dates. NO ASSUMPTIONS."""
    possible = []
    for item in t_nums:
        if item.isdigit() and (int(item) > 0 and int(item) < 32):
            possible.append(item)

    possible = list(set(possible))

    if len(possible) == 1:
        return int(possible[0])
    elif len(possible) > 1:
        if str(day_wmohead) in possible and day_wmohead is not None:
            return day_wmohead
        else:
            return None
    else:
        return None


def findMonth(date):
    """ Find month information in the line. NO ASSUMPTIONS"""
    date_text = re.sub('[^A-Za-z0 ]+', ' ', date)
    date_text = (date_text.replace("0", "O")).rstrip('0')
    t_text = date_text.split()
    strip = str.strip
    tmp = [strip(item) for item in t_text if item in MO_STR]
    #ONE OPTION - PROPER FORMAT
    if len(tmp) == 1:
        return tmp[0]
    # MORE THAN 1
    else:
        #NOT MORE THAN ONE UNIQUE!
        if len(list(set(tmp))) == 1:
            return tmp[0]
        #MORE THAN 1 OPTION
        else:
            month = "NAN"
            for text in t_text:
                if any(moes in text for moes in MO_STR):
                    for moes in MO_STR:
                        if moes in text:
                            return moes
                else:
                    if len(text) > 3:
                        if text[:3] in MO_STR: #WORD 1
                            month = text[:3] #WORD 1
                            return month
                        elif text[3:] in MO_STR: #WORD 2
                            month = text[3:]#WORD 2
                            return month
                        else:
                            return "NAN"
    # ELSE CATCH ALL
    return month


def checkMonth(month):
    """ Get month information... This does have any other alternatives, but may
    need to be adjusted for UTC time. NO ASSUMPTIONS"""
    if len(month) == 3:
        return month[:3]
    elif len(month) > 3:
        return month[:3]
    else:
        return "NAN"


def getMonth(month):
    """ Get the month and return the integer value 1-12. NO ASSUMPTIONS"""
    if   month == "JAN":
        return 1
    elif month == "FEB":
        return 2
    elif month == "MAR":
        return 3
    elif month == "APR":
        return 4
    elif month == "MAY":
        return 5
    elif month == "JUN":
        return 6
    elif month == "JUL":
        return 7
    elif month == "AUG":
        return 8
    elif month == "SEP":
        return 9
    elif month == "OCT":
        return 10
    elif month == "NOV":
        return 11
    elif month == "DEC":
        return 12
    else:
        return None


def getDDHHMM(ddhhmm):
    """ Get the DDHHMM variable from header. NO ASSUMPTIONS."""
    if len(ddhhmm) == 6:
        if ddhhmm == "999999":
            return None, None, None

        day_wmohead = int(ddhhmm[:2])
        hr_wmohead = ddhhmm[2:4]
        min_wmohead = ddhhmm[4:6]
        return day_wmohead, hr_wmohead, min_wmohead
    else:
        return None, None, None



def getYear(date, iYear):
    """ returns the year found... Give or take 1 year...
    Check later to see if it matches iYear. NO ASSUMPTIONS"""
    tmp_nums = re.sub('[^0-9O ]+', '', date)
    strip = str.strip
    nums1 = strip((tmp_nums.replace("O", "0")))
    nums2 = strip((nums1.lstrip('0')).strip())
    date_nums = nums2.split()

    if str(iYear) in date_nums:
        date_nums.remove(str(iYear))
        return iYear, date_nums
    elif str(iYear+1) in date_nums:
        date_nums.remove(str(iYear+1))
        return iYear+1, date_nums
    elif str(iYear-1) in date_nums:
        date_nums.remove(str(iYear-1))
        return  iYear-1, date_nums
    else:
        year = None
        if len(date_nums) > 0 and date_nums[0] == "0":
            date_nums.remove("0")
        t_array = [strip(item) for item in date_nums if item != '']
        if len(t_array) == 1 and len(t_array[0]) > 4 and t_array[0].isdigit():
            t_arr = t_array[0]
            #NOT QUITE AN ASSUMPTION
            #Sept. 17, 2021 -- Moved this higher to give preference to iYear.
            #previous method gave preference to year in text (first 4 digits)
            if str(iYear) in t_arr:
                year = iYear
                date_nums = [t_arr.split(str(year))[0]]
                return year, date_nums
            elif int(t_arr[-4:]) >= 1900 and int(t_arr[-4:]) <= ADMIN_CURRENT_YEAR:
                year = int(t_arr[-4:])
                date_nums = ["".join(t_arr.split(str(year)))]
                return year, date_nums
            elif int(t_arr[:4]) >= 1900 and int(t_arr[:4]) <= ADMIN_CURRENT_YEAR:
                year = int(t_arr[:4])
                date_nums = ["".join(t_arr.split(str(year)))]
                return year, date_nums
            elif str(iYear+1) in t_arr:
                year = iYear+1
                date_nums = [t_arr.split(str(year))[0]]
                return year, date_nums
            elif str(iYear-1) in t_arr:
                year = iYear-1
                date_nums = [t_arr.split(str(year))[0]]
                return year, date_nums
            else:
                return year, date_nums
        else:
            for item in t_array:
                if item.isdigit() and len(item) == 4:
                    #NOT QUITE AN ASSUMPTION
                    if int(item) >= 1900 and int(item) <= ADMIN_CURRENT_YEAR:
                        year = int(item)
                        date_nums.remove(str(year))
                        break

            return year, date_nums
        return year, date_nums


def checkYear(year, iYear, wfo):
    """See if it is valid or if we should look into it later. YES ASSUMPTIONS
    for missing or invalid years"""
    if year == iYear:
        return year, False
    # ASSUMPTION - YEAR MISSING USE iYear
    elif year is None:
        return iYear, True
    # ASSUMPTION - PMDTHR TURN OF THE CENTURY
    elif wfo == "PMDTHR" and year < 1950:
        year = year + 100
        if year == iYear:
            return year, False
        else:
            return year, True
    elif year < ADMIN_EARLIEST_YEAR:
        return iYear, True
    else:
        return year, True


def get_Issuing_Date_text(trimTimesFound, iYear, wfo, DDHHMM):
    """NO ASSUMPTIONS. COMPILE DATE INFO"""
    # GET AUTOMATED INFO - SHOULD BE CORRECT UNLESS NOT FOUND
    dayWMOHEAD, _, _ = getDDHHMM(DDHHMM) #NO ASSUMPTIONS


    tmp = re.sub(r" ?\([^)]+\)", "", trimTimesFound) ## ( )
    date = re.sub(r" ?/([^)]+/)", "", tmp) ## / /

    if any(tz1 in date for tz1 in TZS):
        date = [date.split(tz1)[1]  for tz1 in TZS if tz1 in date][0]

    #Identify/Check/Verify/Set month based on human input text from Issuing Date/Time Line
    text_month = findMonth(date) #NO ASSUMPTIONS
    mo = checkMonth(text_month) #NO ASSUMPTIONS
    month = getMonth(mo) #NO ASSUMPTIONS

    #Gets/Checks/Sets year against all known information.
    tmp_year, t_nums = getYear(date, iYear) #NO ASSUMPTIONS

    year, assume = checkYear(tmp_year, iYear, wfo) #YES MINOR ASSUMPTIONS

    #Gets/Checks/Sets day against all known information.
    text_day = getDay(t_nums, dayWMOHEAD) #NO ASSUMPTIONS

    if month is None:
        #USE PREVIOUS/NEXT MONTH IN THE FUTURE TO RESOLVE MORE CASES?
        return None, None, None, None

    if text_day is None:
        return year, month, None, True

    return year, month, text_day, assume


def getFirstGuess(year, month, DD, HH, MM):
    """Guess the issuing date/time in utc... Timezone not needed
    NO ASSUMPTION... First Guess Only Given True Info"""
    try:
        return datetime.datetime(year, month, DD, int(HH), int(MM), tzinfo=pytz.timezone("UTC"))
    except:
        return None



def guessAMPM(first_guess, timezone):
    """UNUSED....Guess AM or PM based off of the first guess time. NO ASSUMPTION"""
    try:
        #unused this isn't done
        local_time = first_guess.astimezone(pytz.timezone(timezone))
        if local_time.hour < 12:
            return "AM"
        elif local_time.hour < 24:
            return "PM"
        else:
            return None
    except:
        return None



def getAMPM(timepre):
    """Get AMPM from the time data. ASSUMPTIONS will be made. Will not necessarily
    impact the output unless the WMO Header is missing
    """
    if timepre is None:
        return None, True

    time22 = (re.sub('[^APMZ]+', '', timepre)).lstrip("M")
    num_time = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
    num_time = num_time.replace("O", "0")
    if time22 == "AM":
        return "AM", False
    elif time22 == "PM":
        return "PM", False
    elif time22 == "Z":
        num_time = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
        num_time = num_time.replace("O", "0")
        if num_time.isdigit() and len(num_time) >= 3:
            # UGH IF IT WAS LIKE 15LT then it's still b/c trimming
            if int(num_time) < 1200:
                return "AM", False
            # otherwise greater than or equal to 1200 it's PM
            elif int(num_time) < 2400:
                return "PM", False
            else:
                return None, True
        else:
            return None, True

    elif "AM" in time22 or "PM" in time22:
        if "AM" in time22 and "PM" in time22:
            if time22.index("PM") < time22.index("AM"):
                return "PM", True
            elif time22.index("AM") < time22.index("PM"):
                return "AM", True
            else: #SHOULD NEVER REACH HERE
                return None, True

        elif "AM" in time22:
            return "AM", True
        elif "PM" in time22:
            return "PM", True
        else: #SHOULD NEVER REACH HERE
            return None, True

    elif "N00N" in timepre.replace("O", "0"):
        return "PM", True
    elif "MIDNIGHT" in timepre:
        return "AM", True
    else:
        num_time = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
        num_time = num_time.replace("O", "0")
        if num_time.isdigit() and len(num_time) >= 3:
            # ASSUMPTION 1230 would still be assumed AM
            if int(num_time) < 1300:
                return "AM", True
            # otherwise greater than or equal to 1200 it's PM
            elif int(num_time) < 2400:
                return "PM", False
            else:
                return None, True
        else:
            return None, True


def checkMinute(minute):
    """Check the minute found and properly format it"""
    if minute is None:
        return None
    elif 0 <= minute < 60:
        return "{:02d}".format(minute)
    else:
        return None


def checkHour(hour, AMPM):
    """Check the hour found and properly format it. DECISIONS BASED ON getAMPM"""
    #"{:02d}".format(hour) isn't adaquate
    if hour == None or hour < 0:
        return None
    elif hour <= 11 and AMPM == 'PM':
        return str(hour + 12)
    elif hour < 10 and AMPM == 'AM':
        return '0' + str(hour)
    elif hour == 12 and AMPM == "AM":
        return str("00")
    elif hour == 12 and AMPM == 'PM':
        return str(hour)
    elif 10 <= hour <= 11 and AMPM == 'AM':
        return str(hour)
    elif 12 < hour < 24 and AMPM == 'PM':
        return str(hour)
    else: # i.e. >24 or AMPM missing
        if AMPM is None and hour >= 24:
            return None
        elif AMPM is None and hour < 24:
            if hour <= 11:
                if len(str(hour)) != 2:
                    return '0' + str(hour)
                else:
                    return str(hour)
            else:# hour < 24:
                return str(hour)
        else:
            return None



def getHHMM(short_time, AMPM):
    """Get the HH and MM from the time stamp... in the local time. format it.
    return <hour>, <minute>"""
    lShortTy = len(short_time)
    # If it's time is 4 then assuming first 2 = hour, last 2 = minute
    if short_time.isdigit():
        if lShortTy == 4:
            return int(short_time[0:2]), int(short_time[2:4])
        # if length is only 2 then assume you are only being given the hour
        elif lShortTy == 2:
            if AMPM == "AM": ## IT IS UTC
                return int(00), int(short_time)

            elif AMPM == "PM":
                return int(short_time), int(00)
            else:
                return None, None
        # if time is length 3 then assume it's an AM/PM time < 1000 hrs
        elif lShortTy == 3:
            return int(short_time[0]), int(short_time[-2:])
        # rare but if only 1 value given then assume it's only hour only <10 AM/PM
        elif lShortTy == 1:
            return int(short_time), int(00)
        # If length is > than 5 then we aren't expecting that warn and skip
        else:
            return None, None
    else:
        return None, None



def get_Issuing_Time_text(uniqueHours):
    """NO ASSUMPTIONS OUTSIDE OF getAMPM"""
    if len(uniqueHours) == 0:
        return None, None
    else:
        timepre = "".join((uniqueHours.strip()).split()[-3:]) ## WAS 2

        AMPM, Time_Assume = getAMPM(timepre) #ASSUMPTION

        short_time = ""

        num_time = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
        num_time = num_time.replace("O", "0")

    if len(num_time) <= 4 and len(num_time.strip('0')) >= 1:
        pass

    elif len(num_time) == 0:
        timeTMP2 = uniqueHours.split()
        if len(timeTMP2) > 0:
            num_time = re.sub('[^0-9]+', '', timeTMP2[0])
        else:
            return None, None

        if "N00N" in uniqueHours.replace("O", "0") or "MIDNIGHT" in uniqueHours:
            if "AFTERNOON" in uniqueHours:
                return None, None
            else:
                if "N00N" in uniqueHours.replace("O", "0"):
                    num_time = str(1200)
                elif "MIDNIGHT" in uniqueHours:
                    num_time = str(0000)
                else:
                    pass
        else:
            return None, None

    else:
        if str(12000) in uniqueHours or "N00N" in uniqueHours or "MIDNIGHT" in uniqueHours:
            if "MIDNIGHT" in uniqueHours:
                num_time = str(0000)
            elif "AFTERN00N" not in uniqueHours.replace("O", "0"):
                num_time = str(1200)
            else:
                return None, None
        else:
            tmpt = uniqueHours.split("/")[-1]
            tmpt2 = "".join(tmpt.split()[-1])
            tmpt2 = (tmpt2.replace("O", "0"))
            num_time = re.sub('[^0-9]+', '', tmpt2)
            if len(num_time) == 0 or len(num_time) > 4:
                return None, None

    short_time = num_time
    hour, minute = getHHMM(short_time, AMPM)

# == == == == == == == == == == == == == == == == == == == == == == == ==
# Check Time Information: Hours and Minutes
# == == == == == == == == == == == == == == == == == == == == == == == ==
    checked_min = checkMinute(minute)
    strHour = checkHour(hour, AMPM)
    if checked_min is None or strHour is None:
        return None, None
    else:
        MND_Header = str(strHour)+str(checked_min)

    return MND_Header, Time_Assume
