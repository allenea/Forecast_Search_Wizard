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
from __future__ import print_function
import re, time, pytz, datetime#, os, sys

ADMIN_EARLIEST_YEAR = 1996
ADMIN_CURRENT_YEAR = int(time.ctime()[-4:])


wk_days = ["MON","TUE","WED","THU","FRI","SAT","SUN", \
           "MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY", \
           "TUES","WEDS", "THURS","THUR"]

mo_str = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",\
          "JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST",\
          "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER","SEPT","0CT","N0V","0CT0BER","N0VEMBER"]

tzs = ["UTC","EST","EDT","CDT","CST","MST","MDT","PDT","PST", "AKDT", "AKST","HST",
       "HAST", "HADT","GMT","GUAM LST","ADT","AST","CHST","SST","SDT","ChST"]

def findMonth(date):
    """ Find month information in the line. NO ASSUMPTIONS"""
    date_text = re.sub('[^A-Za-z0 ]+', ' ', date)
    date_text = (date_text.replace("0","O")).rstrip('0')
    t_text = date_text.split()

    #ONE OPTION - PROPER FORMAT
    if len( [item.strip() for item in t_text if item in mo_str]) == 1:
        month = [item.strip() for item in t_text if item in mo_str][0]
        return month
    else: # MORE THAN 1
        #NOT MORE THAN ONE UNIQUE
        if len(list(set([item.strip() for item in t_text if item in mo_str]))) == 1:
            month = [item.strip() for item in t_text if item in mo_str][0]
            return month
        #MORE THAN 1 OPTION
        else:
            month = "NAN"
            for idx in range(len(t_text)):
                if any(moes in t_text[idx] for moes in mo_str):
                    for moes in mo_str:
                        if moes in t_text[idx]:
                            return moes
                else:
                    if len(t_text[idx])>3:   
                        if t_text[idx][:3] in mo_str: #WORD 1
                            month = t_text[idx][:3] #WORD 1
                            return month
                        elif t_text[idx][3:] in mo_str: #WORD 2
                            month = t_text[idx][3:]#WORD 2
                            return month
                        else:
                            return "NAN"
    # ELSE CATCH ALL
    return month



def checkMonth(month):
    """ Get month information... This does have any other alternatives, but may need to be adjusted for UTC time. NO ASSUMPTIONS"""
    if len(month) == 3:
        return month[:3]
    elif len(month) > 3:
        return month[:3]
    else:
        return "NAN"
    
    
    
def getMonth(month):
    """ Get the month and return the integer value 1-12. NO ASSUMPTIONS"""
    if   month == "JAN": return 1
    elif month == "FEB": return 2
    elif month == "MAR": return 3
    elif month == "APR": return 4
    elif month == "MAY": return 5
    elif month == "JUN": return 6
    elif month == "JUL": return 7
    elif month == "AUG": return 8
    elif month == "SEP": return 9
    elif month == "OCT": return 10
    elif month == "NOV": return 11
    elif month == "DEC": return 12
    else: return None    



def getDDHHMM(DDHHMM):
    """ Get the DDHHMM variable from header. NO ASSUMPTIONS."""
    if len(DDHHMM) == 6:
        if DDHHMM == "999999":
            return None, None, None
        dayWMOHEAD = int(DDHHMM[:2])
        hrWMOHEAD  = DDHHMM[2:4]
        minWMOHEAD = DDHHMM[4:6]
        return dayWMOHEAD, hrWMOHEAD, minWMOHEAD
    else:
        return None, None, None
        
    

def getYear(date,iYear):
   """ returns the year found... Give or take 1 year... Check later to see if it matches iYear. NO ASSUMPTIONS"""
   tmp_nums = re.sub('[^0-9O ]+', '', date)
   nums1 = (tmp_nums.replace("O","0")).strip()
   nums2 = (nums1.lstrip('0')).strip()
   date_nums = nums2.split()
   
   if str(iYear) in date_nums:
        year = iYear;
        date_nums.remove(str(year))
        return year, date_nums

   elif str(iYear+1) in date_nums:
        year = iYear+1;
        date_nums.remove(str(year))
        return year, date_nums

   elif str(iYear-1) in date_nums:
        year = iYear-1;
        date_nums.remove(str(year))
        return year, date_nums

   else:
       year = None
       if len(date_nums) > 0 and date_nums[0] == "0":
           date_nums.remove("0")

       t_array = [item.strip() for item in date_nums if item != '']
       
       if len(t_array) == 1 and len(t_array[0]) > 4 and t_array[0].isdigit():
           t_arr = t_array[0]
           if int(t_arr[:4]) >= 1900 and int(t_arr[:4]) <= ADMIN_CURRENT_YEAR:
               year = int(t_arr[:4])
               date_nums = ["".join( t_arr.split(str(year)))]
               return year, date_nums

           elif int(t_arr[-4:]) >= 1900 and int(t_arr[-4:]) <= ADMIN_CURRENT_YEAR:
              year = int(t_arr[-4:])
              date_nums = ["".join( t_arr.split(str(year)))]
              return year, date_nums
          
           elif str(iYear) in t_arr:
               year = iYear
               date_nums = [t_arr.split(str(year))[0]]
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
               print("time function - else")
               return year, date_nums

       else:
           for idx in range((len(t_array))):
               if t_array[idx].isdigit() and len(t_array[idx]) == 4:
                   if int(t_array[idx]) >= 1900 and int(t_array[idx]) <= ADMIN_CURRENT_YEAR:
                       year = int(t_array[idx])
                       date_nums.remove(str(year))
                       break
           return year, date_nums
       return year, date_nums



def checkYear(year,iYear, month, wfo):
    """ CHECKS THE YEAR AGAINST KNOWN INFORMATION. ASSUMPTIONS ARE MADE AND NOTED.
    wfo only matters for PMDTHR all others are treated the same."""
    isAssumed = False

    if year == iYear:
        return year, isAssumed
    elif year == None:
        return iYear, isAssumed
    elif wfo == "PMDTHR" and year < 1950:
        year = year + 100
        if year == iYear:
            return year, isAssumed
        elif  abs(iYear - year) == 1:
            if year > iYear: # year == iYear + 1
                if month == 1: return year, False
                else: return year, True
            else: #year == iYear - 1
                if month == 12: return year, False
                else:  return year, True
        elif abs(iYear - year) > 1:
            if year > iYear: return iYear, True #Shouldn't have happened yet. use iYear (when stored)
            else: return year, True
        else:
            return None, True
    else: #something stored in something else           
        if  abs(iYear - year) == 1:
            if year > iYear: # year == iYear + 1
                if month == 1:  return year, False
                else: return iYear, True
            else: #year == iYear - 1
                if month == 12: return year, False
                else: return year, True
        elif abs(iYear - year) > 1 and year > ADMIN_EARLIEST_YEAR:
            if year > iYear: return iYear, True #Shouldn't have happened yet. use iYear (when stored)
            else: return year, True
        else:
            return None, True
    
    
    
def getDay(t_nums, dayWMOHEAD):
    """Do not look at dayWMOHEAD unless there are multiple possible day-dates. NO ASSUMPTIONS."""
    possible = []
    for item in t_nums:
        if item.isdigit() and (int(item) > 0 and int(item) < 32):
            possible.append(item)
    
    possible = list(set(possible))
    
    if len(possible) == 1:
        return int(possible[0])
    elif len(possible) > 1:
        if str(dayWMOHEAD) in possible and dayWMOHEAD is not None:
            return dayWMOHEAD
        else:
            return None
    else:
        return None



def get_Issuing_Date_text(trimTimesFound,iYear,wfo,DDHHMM):
    # GET AUTOMATED INFO - SHOULD BE CORRECT UNLESS NOT FOUND
    dayWMOHEAD, hrWMOHEAD, minWMOHEAD = getDDHHMM(DDHHMM)
    
    isAssumed = False
    
    tmp = re.sub(r" ?\([^)]+\)", "", trimTimesFound) ## ( )
    date = re.sub(r" ?/([^)]+/)", "", tmp) ## / /

    if any(tz1 in date for tz1 in tzs):
        date = [date.split(tz1)[1]  for tz1 in tzs if tz1 in date][0]
    
    #Identify/Check/Verify/Set month based on human input text from Issuing Date/Time Line
    text_month = findMonth(date) 
    mo = checkMonth(text_month)
    month = getMonth(mo)

    #Gets/Checks/Sets year against all known information.
    tmp_year, t_nums = getYear(date, iYear)

    if tmp_year is None:
        tmp_year = iYear
        year, assume = checkYear(tmp_year,iYear, month, wfo)
        assume = True
        isAssumed = True
    else:
        year, assume = checkYear(tmp_year,iYear, month, wfo)
        
    #Gets/Checks/Sets day against all known information.
    text_day = getDay(t_nums, dayWMOHEAD)
    
    if month == None:  
        #USE PREVIOUS/NEXT MONTH IN THE FUTURE TO RESOLVE MORE CASES?
        return None, None, None, None
    
    if text_day == None:
        if year == None:
            return None, None, None, None
        return year, month,None, True
      
    if assume == True:
        if year == None:
            return None, None, None, None
        else:
            return year, month, text_day, True
        
    return year, month, text_day, isAssumed



def getFirstGuess(year,month, DD, HH, MM, timezone):
    """Guess the issuing date/time in utc..."""
    try:
        return datetime.datetime(year,month,DD,HH,MM,tzinfo=pytz.timezone("UTC"))
    except:
        return None
    
    
    
def guessAMPM(first_guess, timezone):
    """Guess AM or PM based off of the first guess time."""
    try:
        local_time=first_guess.astimezone(pytz.timezone(timezone))
        if local_time.hour < 12:
            return "AM"
        elif local_time.hour < 24:
            return "PM"
        else:
            return None
    except:
        return None
    
    
    
def getAMPM(timepre, first_guess, timezone):
    """Get AMPM from the time data, redundant check to make sure it matches up with the guess. 
    If a first guess cannot be made then only sure things will not be marked as assumptions"""

    likely = guessAMPM(first_guess, timezone)
    time22 = (re.sub('[^APMZ]+', '', timepre)).lstrip("M")
    
    #ABSOLUTE
    if likely is not None:
        if time22 == "AM" and "AM" == likely:
            return "AM", False
        elif time22 == "PM" and "PM" == likely:
            return "PM", False
        elif time22 == "Z":
            numTime = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
            numTime = numTime.replace("O","0")
            if numTime.isdigit() and len(numTime) >= 3:
                if int(numTime) < 1200 and "AM" == likely:
                    return "AM", False
                # otherwise greater than or equal to 1200 it's PM
                elif int(numTime) < 2400 and "PM" == likely:
                    return "PM", False
                else:
                    return likely, True  ## IMO False... But to be safe, True
            else:
                return likely, True ## IMO False... But to be safe, True
            
        elif "AM" in time22 or "PM" in time22:
            if "AM" in time22 and "PM" in time22:
                if time22.index("PM") < time22.index("AM") and "PM" == likely:
                    return "PM", False
                elif time22.index("AM") < time22.index("PM") and "AM" == likely:
                    return "AM", False
                else:
                    return likely, True ## IMO False... But to be safe, True
            elif "AM" in time22 and "AM" == likely:
                return "AM", False 
            elif "PM" in time22 and "PM" == likely:
                return "PM", False
            elif "AM" in time22:
                return "AM", True 
            elif "PM" in time22:
                return "PM", True 
            else:#SHOULD NEVER REACH HERE
                return likely, True
            
        elif "N00N" in timepre.replace("O","0"):
            if "PM" == likely:
                return "PM", False
            else: #TRUST THE DDHHMM
                return "AM", True  ## IMO False... But to be safe, True
            
        elif "MIDNIGHT" in timepre:
            if "AM" == likely:
                return "AM", False
            else: #TRUST THE DDHHMM
                return "PM", True ## IMO False... But to be safe, True
        else:
            return likely, False
    else:        
        if time22 == "AM":
            return "AM", False
        elif time22 == "PM":
            return "PM", False
        elif time22 == "Z":
            numTime = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
            numTime = numTime.replace("O","0")
            if numTime.isdigit() and len(numTime) >= 3:
                if int(numTime) < 1200:
                    return "AM", False # UGH IF IT WAS LIKE 15LT then it's still a valid thing... BECAUSE OF THE TRIMMING...
                # otherwise greater than or equal to 1200 it's PM
                elif int(numTime) < 2400:# UGH IF IT WAS LIKE 15LT then it's still a valid thing... BECAUSE OF THE TRIMMING...
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
            
        elif "N00N" in timepre.replace("O","0"):
            return "PM", True
        elif "MIDNIGHT" in timepre:
            return "AM", True
        else:
            return None, True



def checkMinute(minute):
    """Check the minute found and properly format it"""
    if minute == None:
        return None
    else:
        if minute < 0: #Includes -1 which means not assigned
            return None
        #If minute is a single digit less than 10 add a 0 to make it 2 digits
        elif minute < 10:
            return '0'+ str(minute)
        # If minute less than  60 
        elif minute < 60:
            return str(minute)
        else:
            return None
    
    
    
def checkHour(hour, AMPM):
    """Check the hour found and properly format it"""
    if hour < 0:
        return None
    elif hour <= 11 and AMPM == 'PM':
        return str(hour + 12)
    elif hour == 12 and AMPM == "AM":
        return str("00")
    elif hour == 12 and AMPM == 'PM':
        return str(hour)
    elif hour < 10 and AMPM == 'AM':
        return '0' + str(hour)
    elif hour >= 10 and hour <= 11 and AMPM =='AM':
        return str(hour)
    elif hour > 12  and hour < 24 and AMPM == 'PM':
        return str(hour)
    else: # i.e. >24 or AMPM missing
        if AMPM == None and hour >= 24:
            return None
        elif AMPM == None and hour < 24:  
            if hour<=11:
                if len(str(hour)) != 2:
                    return '0' + str(hour)
                else:
                    return str(hour)
            else:# hour < 24:
                return str(hour)
        else:         
            return None



def getHHMM(short_time, AMPM):
    """Get the HH and MM from the time stamp... in the local time. format it"""
    lShortTy = len(short_time)
    # If it's time is 4 then assuming first 2 = hour, last 2 = minute
    if short_time.isdigit():
        if lShortTy == 4:
            hour = int(short_time[0:2])
            minute = int(short_time[2:4])
            return hour, minute
        # if length is only 2 then assume you are only being given the hour
        elif lShortTy == 2:
            if AMPM == "AM": ## IT IS UTC
                hour = int(00)
                minute = int(short_time)
                return hour, minute
    
            elif AMPM == "PM":
                hour = int(short_time)
                minute = int(00)
                return hour, minute
            else:
                return None, None
        # if time is length 3 then assume it's an AM/PM time < 1000 hrs
        elif lShortTy ==3:
            hour = int(short_time[0])
            minute = int(short_time[-2:])
            return hour, minute
    
        # rare but if only 1 value given then assume it's only hour <10 AM/PM
        elif lShortTy == 1:
            hour = int(short_time)
            minute = int(00)
            return hour, minute
        # If length is > than 5 then we aren't expecting that warn and skip
        else:
            return None, None
    else:
        return None, None
    
    
    
def get_Issuing_Time_text(uniqueHours, first_guess, timezone, wfo):
    if len(uniqueHours) == 0:
        return None, None, None, None
    else:
        timepre = "".join((uniqueHours.strip()).split()[-3:]) ## WAS 2
        AMPM, Time_Assume = getAMPM(timepre, first_guess, timezone)

        short_time = ""
    
        numTime = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
        numTime = numTime.replace("O","0")
    
    if len(numTime) <=4 and len(numTime.strip('0')) >= 1:
        pass
    
    elif len(numTime) == 0:
        timeTMP2 = uniqueHours.split()
        if len(timeTMP2) > 0:
            numTime = re.sub('[^0-9]+', '', timeTMP2[0])
        else:
            return None, None, None, None

        if "N00N" in uniqueHours.replace("O","0") or "MIDNIGHT" in uniqueHours:
            if "AFTERNOON" in uniqueHours:
                return None, None, None, None
            else:
                 if "N00N" in uniqueHours.replace("O","0"):
                    numTime = str(1200)
                 elif "MIDNIGHT" in uniqueHours:
                    numTime = str(0000)
                 else:
                     pass
        else:
            return None, None, None, None
        
    else:# len(numTime) > 4:
        if str(12000) in uniqueHours or "N00N" in uniqueHours or "MIDNIGHT" in uniqueHours:
            if "MIDNIGHT" in uniqueHours:
                numTime = str(0000)
            elif "AFTERN00N" not in uniqueHours.replace("O","0"):
                numTime = str(1200)
            else:
                 pass
        else:
            timeTMP = uniqueHours.split("/")[-1]
            timeTMP2 = "".join(timeTMP.split()[-1])
            timeTMP2 = (timeTMP2.replace("O","0"))
            numTime = re.sub('[^0-9]+', '', timeTMP2)
            if len(numTime) == 0 or len(numTime) > 4:
                return None, None, None, None
            else:
                pass
    short_time = numTime
    hour, minute = getHHMM(short_time, AMPM)

# =============================================================================
# Check Time Information: Hours and Minutes            
# =============================================================================
    checked_min = checkMinute(minute)
    if checked_min is None:
        return None, None, None, None
    
    strHour = checkHour(hour,AMPM)
    if strHour is None:
        return None, None, None, None
    
    if AMPM is None:
        if int(strHour) <12:
            AMPM = "AM"
        else:
            AMPM = "PM"
            
    #combine into one string for time
    return str(strHour), str(checked_min), AMPM, Time_Assume



def checkEverything(DDHHMM, year, month, text_day, iYear):
    fday = -1; fmon = -1; fyr = -1; isAssumed = False
           
    dayWMOHEAD, hrWMOHEAD, minWMOHEAD = getDDHHMM(DDHHMM)
    
    if text_day == dayWMOHEAD: ## == 0
        fday = text_day
    elif abs(int(dayWMOHEAD) - int(text_day)) == 1:
        fday = dayWMOHEAD
    else:
        if abs(int(dayWMOHEAD) - int(text_day)) > 1:
            if dayWMOHEAD == 1 and int(text_day) >= 28:
                fday = dayWMOHEAD
                #isAssumed = True # assumed because 28 is February no 30/31
                month = month + 1
                if month > 12: 
                    month = 1
                    fyr = year + 1
            elif dayWMOHEAD >= 28 and int(text_day) == 1:
                fday = dayWMOHEAD
                #isAssumed = True # assumed because 28 is February no 30/31
                month = month - 1
                if month == 0:
                    month = 12
                    fyr = year - 1
            else:
                return None, None, None, None, None, None

    if fyr == -1:
        if year == iYear: #==0
            fyr = iYear
        elif year == iYear + 1:# == +1
            if month == 1:
                fyr = iYear + 1
            elif month == 12:
                fyr = iYear
            else:
                return None, None, None, None, None, None
    
        elif year == iYear - 1: # == -1     #2001 stored in 2002
            if month == 12:
                fyr = iYear - 1
            elif month == 1:
                fyr = iYear
            else:
                return None, None, None, None, None, None
        else:
            return None, None, None, None, None, None

    else:
        if abs(fyr - iYear) <= 1 and (month == 1 or month == 12):
            pass
        else:
            isAssumed = True

    if abs(fyr-iYear) >1:
        isAssumed = True
    
    fmon = month
    
    return fyr, fmon, fday, hrWMOHEAD, minWMOHEAD, isAssumed