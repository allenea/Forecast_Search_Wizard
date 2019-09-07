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
import time as gettime
import re, sys, os
from src.utc_convert import utc_convert_reformat_time

stripwords = ["MIAMI","FL", "BRANCH", "ISSUED AT", "ISSUED","COR","HONOLULU HI","WASHINGTON DC",\
              "NWS NATIONAL HURRICANE CENTER","NWS CLIMATE PREDICTION CENTER COLLEGE PARK MD"]

stripwords2 = ["MARINE PREDICTION CENTER/MFB","OCEAN PREDICTION CENTER/OFB",\
              "OCEAN PREDICTION CENTER/MFB","PREDICTION CENTER/MFB","PREDICTION CENTER/OFB","CENTER/OFB"]

wk_days = ["MON","TUE","WED","THU","FRI","SAT","SUN", \
           "MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY", \
           "TUES","WEDS", "THURS","THUR"]

mo_str = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",\
          "JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST",\
          "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER","SEPT","0CT","N0V","0CT0BER","N0VEMBER"]

tzs = ["UTC","EST","EDT","CDT","CST","MST","MDT","PDT","PST", "AKDT", "AKST","HST",
       "HAST", "HADT","GMT","GUAM LST","ADT","AST","CHST","SST","SDT","ChST"]

def wfo_rft_time_ALT(trimTimesFound,uniqueHours,wfo, timezone, uniqueKeyWords,makeAssume):
    """ The alternative method is required to attempt an extract of date and time information. If possible. This used to be the original primary function except it does it one at a time.
    
    Parameters:
        trimTimesFound (str): Raw date info
        uniqueHours (str): Raw time info
        wfo (str): Forecast product PIL
        timezone (str): Timezone information associated with this instance (tz_finder)
        uniqueKeyWords (str): Keyword that was found
        makeAssume (bool): Make assumptions
        
    Returns:
        FinalTimesFound (datetime tuple): A datetime tuple that has been converted to UTC.
        KeyFound (str):  The keyword that was found with any req. flags
    """   
    #SPC2003 coming in here and getting lost
    #store successfully identified cases in this array
    count = 0
    cYear = int(gettime.ctime()[-4:]) + 1
    #Loop through the times found list for keywords without duplicates
        
    # TODO Assumed because ...
    isAssumedAMPM = False; isAssumedInfo = True
    ##INITIALIZE to -1 - Impossible to be a date if all info isn't there
    year = -1; day = -1; hour = -1; minute = -1
    month = ""; AMPM = ""
 
    # HANDLES ONE OF THE LEGACY FORECASTS
    if "THRU" in trimTimesFound: tmp = trimTimesFound.split("THRU")[1]
    else: tmp = trimTimesFound.strip('\n')
    
    tmp = re.sub(r" ?\([^)]+\)", "", tmp) ## ( )
    tmp = re.sub(r" ?/([^)]+/)", "", tmp) ## / /
    date = tmp.split(".")[0]  #  removes any .... Correction forecasts
    date = re.sub('[^A-Za-z0-9 ]+', '', date)
    
    ## Using a second time/timezone... Use the first..... get rid of the other... So I think I looked into whether or not order mattered in the tz_finder file.
    #    line = re.sub(r" ?\([^)]+\)", "", line) ## remove between the ( ) used this to remove stuff in () but what if they didn't use ()
    if any(tz1 in date for tz1 in tzs):
        date = [date.split(tz1)[1]  for tz1 in tzs if tz1 in date][0]
        isAssumedInfo = True
         
    t_array = date.split()
    
    #remove empty values in array with time
    t_array = [item.strip() for item in t_array if item != '']
    
    #time am/pm time_zone day mon dd yyyy (Issuing Time/Date)   ... TZ_FINDER SHOULD HAVE SPLIT AT THE time_zone 
    #CASE 1.... FORECASTER ENTERED WEEK DAY WHICH IS FOLLOWING THE DIRECTIVE ON FORMATTING
    # Check if it's the week day or month name     
    # Iterate through each split index -> t_array
    for idx in range((len(t_array))):
        if t_array[idx].isalpha():
            #IF AM/PM
            if "AM" == t_array[idx] or "PM" == t_array[idx]:
                AMPM = t_array[idx] # BECAUSE THERE IS SECOND TIME INFO SINCE TZ_FINDER SPLIT AT THE TIME_ZONE
            #Find the week day name - get rid of it
            elif t_array[idx] in wk_days:
                pass # Handles condition without impacting loop
            #Month
            elif month == "":
                if t_array[idx] in mo_str:
                    month = t_array[idx]
                    
                # NOT SOMETHING WE EXPECTED BUT A STRING NONETHELESS     
                elif len(t_array[idx]) == 6:
                    if t_array[idx][:3] in mo_str: #WORD 1
                        month = t_array[idx][:3] #WORD 1
                    elif t_array[idx][3:] in mo_str: #WORD 2
                        month = t_array[idx][3:]#WORD 2
                
        # get the year which should be the length of 4 and a digit
        elif t_array[idx].isdigit():
            # Find the day. Shouldn't be more than length 2...  DO I NEED THE ! = 0
            if  len(t_array[idx]) < 3:
                t_array[idx] = int(t_array[idx]) # Is number already (speed)
                # Keep day if it's reasonable
                if  t_array[idx] < 32:
                    day =  t_array[idx]
                    
            elif len(t_array[idx]) == 4:
                t_array[idx] = int(t_array[idx]) # Is number already (speed)
                 # YEAR MINIMUM = 1900 FOR CPC but whatever data min is
                 # Keep year if it's reasonable AND ----
                 # Speeds it up by not checking extra stuff at the end
                if t_array[idx] >= 1900 and t_array[idx] <= cYear:
                    year = t_array[idx]
                    if month != "" and day != -1 and year != -1:
                        break # Reason: Increase speed/efficiency
 
            # TRYING SOMETHING NEW - FIXES 102000 DDYYYY situation
            elif len(t_array[idx]) <= 6:
                #t_array[idx] = int(t_array[idx]) # Is number already (speed)
                if  year == -1 or day == -1:
                    try:
                        tryyear = int(t_array[idx][-4:])
                        tryday = int(t_array[idx][:-4])
                        if tryday < 32:
                            day = tryday
                        if tryyear >= 1900 and tryyear <= cYear:
                            year = tryyear
                            if month != "" and day != -1 and year != -1:
                                break # Reason: Increase speed/efficiency
                    except:
                        pass
     
        elif t_array[idx].isalpha() == False and t_array[idx].isdigit() == False:
            if any(moes in t_array[idx] for moes in mo_str) and (month == "" or day == -1 or year == -1):
                for moes in mo_str:
                    if moes in t_array[idx]:
                        tmptarr = t_array[idx].split(moes)
                        if month == "":
                            month = moes
                            
                        try:
                            if int(tmptarr[1])  < 32:
                                day = int(tmptarr[1])
                                isAssumedInfo = True
                            elif int(tmptarr[1]) >= 1900 and int(tmptarr[1]) <= cYear:
                                year = int(tmptarr[1])
                                isAssumedInfo = True
                            else:
                                continue
                        except:
                            continue
                        
            elif ("TH" in t_array[idx] or "ST" in t_array[idx]) and day == -1:
                t_array[idx] = "".join(t_array[idx].split("TH"))
                t_array[idx] = "".join(t_array[idx].split("ST"))
                if t_array[idx].isdigit():
                    if  int(t_array[idx]) < 32:
                        day =  int(t_array[idx])    
                        

            elif len(t_array[idx]) == 2 and  day == -1:
                t_array[idx] = t_array[idx].replace("O","0")
                if t_array[idx].isdigit():
                    if  int(t_array[idx]) < 32:
                        day =  int(t_array[idx])
                        
            elif "AM" in t_array[idx] or "PM" in t_array[idx]:
                AMPM = re.sub('[^AMP]+', '', t_array[idx]) # BECAUSE THERE IS SECOND TIME INFO SINCE TZ_FINDER SPLIT AT THE TIME_ZONE

            else:
                if year == -1:
                    try:
                        if int(t_array[idx][:4]) >= 1900 and int(t_array[idx][:4]) <= cYear:
                            year = int(t_array[idx][:4])
                            isAssumedInfo = True
                        elif int(t_array[idx][4:]) >= 1900 and int(t_array[idx][4:]) <= cYear:
                            year = int(t_array[idx][4:])
                            isAssumedInfo = True
                    except:
                        pass
         # Something --- Not a valid day. extra numbers or characters
        elif month != "" and day != -1 and year != -1:
            break
        else:  
            pass                     
# =============================================================================
# DONE WITH EXTRACTING YEAR, MONTH, DAY
# =============================================================================
            
    # NOW DEALING W/ TIME - Case 1 does not actually deal with time
    #DAY
    # if day is 0 (first check IMPORTANT)... don't accept since day !=0
    if day == -1:
        if month == "" and year == -1:
            print("OTHER: ",wfo," NON-HEADER - INVALID DATE/TIME LINE: NO MONTH, DAY, OR YEAR")#, flush=True)#,trimTimesFound, "&&", uniqueHours, "&&",timezone)
            sys.stdout.flush()
            return None, None
        elif month == "":
            print("OTHER: ",wfo," NON-HEADER - INVALID DATE/TIME LINE: NO MONTH OR DAY")#, flush=True)#,trimTimesFound, "&&", uniqueHours, "&&",timezone)
            sys.stdout.flush()
            return None, None
        else:    
            print("TP: ",wfo," - ERR NO DAY: ",str(day),"....",date)#, flush=True)
            sys.stdout.flush()
            return None, None
    # if day is less than 10 need to add a 0 in front for string sort
    elif day < 10: strdayEAA = '0'+ str(day)
    # if day is less than 32 but also greater than 10 since it passed prior condition
    elif day < 32: strdayEAA = str(day)
    #otherwise warn and skip
    else:
        print("TP: ",wfo," - ERR DAY... Check: ",str(day),"....",date)#, flush=True)
        sys.stdout.flush()
        return None, None
    
    #MONTH
    #if the length of month is greater than 3 for the check
    # IF MONTH NEVER ASSIGNED
    if len(month) == 0:
        print("TP: ",wfo," - ERR NO MONTH... Check:",date)#, flush=True)
        sys.stdout.flush()
        return None, None
    
    # PROPER ABBRIVIATION - 3 char
    # it'll be handled below. (capitalize)
    elif len(month) == 3:
        month = month[:3]
        
    elif len(month) > 3:
        # First check if the first 3 char are week day abbriviations
        if month[:3] in wk_days:
            #If it is -split at the whitespace. check if there is month too
            mArr = month.split(" ")
            # if there is 2 things in the split array
            if len(mArr) == 2:
                # iterate through the mo_str list 
                for mon in mo_str:
                    # since the first thing had the week day name the 2nd
                    # item in the list must have the month or not
                    # see if that is in the mo_str.... if so keep it
                    if mArr[1] in mo_str:
                        month = mArr[1]
                    # If at the end of mo_str - not found then not there
                    # warn and skip
                    else:# mon == mo_str[-1]:
                        print("TP: ",wfo," - ERR MONTH: ", mArr,"....",date)#, flush=True)
                        sys.stdout.flush()
                        return None, None
            # is only one then there was no month, only the week day
            # warn and skip
            else:
                print("TP: ",wfo," - ERR MONTH - not mo+wk_day: ",date)#, flush=True)
                sys.stdout.flush()
                return None, None
        # if not in weekdays then just take the first 3 characters.
        # Most likely this is the month but if not it'll be tossed below
        else:
            month = month[:3] #(capitalize)
            
    # if length of month less than 3 then it's too short for the check
    # warn and skip
    # LEN < 3 but not 0
    else:
        print("TP: ",wfo," - ERR UNKNOWN MONTH... Check:",date)#, flush=True)
        sys.stdout.flush()
        return None, None
    
    # IF 0 was used instead of O -- place below for months with O's or 0's and remove 
    if "0" in month: month = month.replace("0","O") 
        
    #Month match to abbriviation and assign the proper month number (as str)
    if   month == "JAN": mo = "01"
    elif month == "FEB": mo = "02"
    elif month == "MAR": mo = "03"
    elif month == "APR": mo = "04"
    elif month == "MAY": mo = "05"
    elif month == "JUN": mo = "06"
    elif month == "JUL": mo = "07"
    elif month == "AUG": mo = "08"
    elif "SEP" in month: mo = "09" # month == "SEP" or month=="SEPT": mo = '09'
    elif month == "OCT": mo = "10"
    elif month == "NOV": mo = "11"
    elif month == "DEC": mo = "12"
    # If else make it 999 where it can't possibly be used and warn us
    else:
        mo="99"
        print("TP: ",wfo," - Reason for UTC FAIL: ", month, "...",month,"-",day,"-",year)#, flush=True)
        sys.stdout.flush()
        return None, None
    
    #!!! Outside year range  - modify for CPC... don't because not processed in main search b/c year == year
    if year <1950:

        if wfo == "PMDTHR":
            year = year + 100
        else:
            #year = iYear
            print("TP: ",wfo," - ERR YEAR... Check: ", str(year),"....",date)#, flush=True)
            sys.stdout.flush()
            return None, None

# =============================================================================
#  NOW DEAL WITH TIME AND AM/PM
# =============================================================================
    timepre = "".join((uniqueHours.strip()).split()[-3:]) ## WAS 2
    numTime = (re.sub('[^0-9O]+', '', timepre)).lstrip("O")
    numTime = numTime.replace("O","0")
    time22 = (re.sub('[^APMZ]+', '', timepre)).lstrip("M")
    short_time = "" #Initialize short_time
    
    
    if len(uniqueHours) == 0:
        print("TP: ",wfo," - WARN NO TIME INFORMATION: ",year, month, day, "  ",uniqueHours)#, flush=True)
        sys.stdout.flush()
        return None, None
    elif len(numTime) == 0:
        try:
            timeTMP2 = uniqueHours.split()[0]
            numTime = re.sub('[^0-9]+', '', timeTMP2)
        except:
            pass
        
        if len(numTime) == 0:
            if "NOON" in uniqueHours or "MIDNIGHT" in uniqueHours:
                if "AFTERNOON" in uniqueHours:
                    print("TP: ",wfo," - WARN 'AFTERNOON' IS NOT AN ACCEPTABLE TIME: ",year, month, day, "  ",uniqueHours)#, flush=True)
                    sys.stdout.flush()
                    return None, None
                else:
                     if "NOON" in uniqueHours:
                        numTime = str(1200)
                        time22 = "PM"
                     elif "MIDNIGHT" in uniqueHours:
                        numTime = str(0000)
                        time22 = "AM"
            else:
                print("TP: ",wfo," - WARN NO TIME INFORMATION: ",year, month, day, "  ",uniqueHours)#, flush=True)
                sys.stdout.flush()
                return None, None
        
    elif len(numTime) <= 4:
         pass
     
    else:
        if str(12000) in uniqueHours or "NOON" in uniqueHours or "MIDNIGHT" in uniqueHours:
            if "MIDNIGHT" in uniqueHours:
                numTime = str(0000)
                time22 = "AM"
            elif "AFTERNOON" not in uniqueHours:
                numTime = str(1200)
                time22 = "PM"
        else:
            timeTMP = uniqueHours.split("/")[-1]
            timeTMP2 = "".join(timeTMP.split()[-1])
            timeTMP2 = (timeTMP2.replace("O","0"))
            numTime = re.sub('[^0-9]+', '', timeTMP2)
            if len(numTime) == 0:
                print("TP: ",wfo," - WARN NO TIME INFORMATION: ",year, month, day, "  ",uniqueHours)#, flush=True)
                sys.stdout.flush()
                return None, None

    #ABSOLUTE
    if time22 == "AM":  AMPM = "AM";  short_time = numTime;
    elif time22 == "PM":  AMPM = "PM";  short_time = numTime
    
    #EITHER AM AND PM OR BOTH IN IT - NOT ABSOLUTE
    elif "AM" in time22 or "PM" in time22:
        if "AM" in time22 and "PM" in time22:
            if time22.index("PM") < time22.index("AM"):     AMPM = "PM";    short_time = numTime;   isAssumedAMPM = True
            elif time22.index("AM") < time22.index("PM"):   AMPM = "AM";    short_time = numTime;   isAssumedAMPM = True
            
        #NOT ABSOLUTE BUT AM IN TIME or PM IN TIME
        elif "AM" in time22:    AMPM = "AM";    short_time = numTime;
        elif "PM" in time22:    AMPM = "PM";    short_time = numTime;
        elif "NOON" in time22 and "PM" in time22:   AMPM = "PM";    short_time = str(1200);

        
    #UTC TIME
    elif timezone == "UTC" and (len(time22) == 0 or (len(time22) == 1 and (time22 =="P" or time22 == "A"))) and numTime.isdigit():
        time2 = int(numTime)
        if time2 <1200:
            AMPM = "AM"
            if time2 < 100:
                short_time = str("00")+str(time2); ### FLAG 
                isAssumedInfo = True  #NHC FORMATTING ISSUE
            else:
                short_time = str(time2)
        elif time2 >= 1200:     short_time = str(time2);    AMPM = "PM" # FOR WPC ONLY ASSUME PM IF NOT GIVEN AMPM
    
    #NO AM OR PM AND NOT UTC TIME    
    elif len(time22) == 0:
        if len(numTime) !=0:
            time2 = int(numTime)
            if time2 >= 2400 or time2 < 0:
                # on forecaster typo exception for 12000 should be 1200
                print("TP: ",wfo," - ERR TIME INVALID - DIGITS: ", str(numTime), "...",month,"-",day,"-",year, uniqueHours)#, flush=True);
                sys.stdout.flush()
                return None, None
            
            else:
                # Same assumptions as above < 1200 is AM
                if time2 < 1200:    AMPM = "AM";    short_time = str(time2);    isAssumedAMPM = True
                # otherwise greater than or equal to 1200 it's PM
                elif time2 >= 1200: AMPM = "PM";    short_time = str(time2)
        else:
            if  "NOON" in uniqueHours:
                AMPM = "PM"
                short_time = str(1200)

            elif "MIDNIGHT" in uniqueHours:
                AMPM = "AM"
                short_time = str(0000)
            else:
                print("TP: ",wfo," - ERR TIME - NO DIGITS: ",uniqueHours, "  ",AMPM," ",year, month, day)#, flush=True)
                sys.stdout.flush()
                return None, None
            
    #PRETTY SAFE BET THAT IT WAS GOING TO BE AM OR PM            
    elif len(time22) == 1: 
        if time22 =="P" or time22 == "A":
            if time22 == "A":   AMPM = "AM";    short_time = numTime
            elif time22 == "P": AMPM = "PM";    short_time = numTime
            
        elif time22 == "Z":
            if int(numTime) < 1200:    AMPM = "AM";    short_time = str(numTime);
            # otherwise greater than or equal to 1200 it's PM
            elif int(numTime) >= 1200: AMPM = "PM";    short_time = str(numTime);

    elif len(time22) == 2: 
        if numTime.isdigit() and int(numTime) < 1200:    AMPM = "AM";    short_time = str(numTime);    isAssumedAMPM = True;
        # otherwise greater than or equal to 1200 it's PM
        elif numTime.isdigit() and int(numTime) >= 1200: AMPM = "PM";    short_time = str(numTime);    isAssumedAMPM = True;
        elif  "NOON" in uniqueHours:      AMPM = "PM";   short_time = str(1200);

    # NO AM OR PM OR IT'S INDISTIGUISHABLE
    else:
        # Same assumptions as above < 1200 is AM
        try:
            time22 = int(re.sub('[^0-9]+', '', uniqueHours))
            if time22 < 1200:    AMPM = "AM";    short_time = str(time22);    isAssumedAMPM = True;   isAssumedInfo = True
            # otherwise greater than or equal to 1200 it's PM
            elif time22 >= 1200: AMPM = "PM";    short_time = str(time22);    isAssumedAMPM = True;   isAssumedInfo = True

        except:
            print("TP: ",wfo," - ERR NO NUMERICAL TIME: ",time22, "  ",AMPM," ",year, month, day, uniqueHours)#, flush=True)
            sys.stdout.flush()
            return None, None

    
    #def get_hr_min(short_time):
    lShortTy = len(short_time)
    # If it's time is 4 then assuming first 2 = hour, last 2 = minute
    if lShortTy == 4:
        hour = int(short_time[0:2])
        minute = int(short_time[2:4])
        #return hour,minute
    # if length is only 2 then assume you are only being given the hour
    elif lShortTy == 2:
        if AMPM == "AM": ## IT IS UTC
            hour = int(00)
            minute = int(short_time)
            isAssumedInfo = True  #NHC FORMATTING ISSUE
            #return hour,minute
        else:
            hour = int(short_time)
            minute = int(00)
            #return hour,minute

    # if time is length 3 then assume it's an AM/PM time < 1000 hrs
    elif lShortTy ==3:
        hour = int(short_time[0])
        minute = int(short_time[-2:])
        #return hour,minute
        
    # rare but if only 1 value given then assume it's only hour <10 AM/PM
    elif lShortTy == 1:
        hour = int(short_time)
        minute = int(00)
        #return hour,minute
        
    # If length is > than 5 then we aren't expecting that warn and skip
    else:
        print("TP: ",wfo," - ERR CATCH-ALL HHMM: ",uniqueHours, "  ",AMPM," ",year, month, day, uniqueHours)#, flush=True)
        sys.stdout.flush()
        return None, None


# =============================================================================
# Check Time Information: Hours and Minutes            
# =============================================================================
    #MINUTE  
    # IF still not resolved
    if minute == -1:
        print("TP: ",wfo," - ERR NO MINUTE: ", minute," at hour: ",hour, AMPM," ... ",short_time, " ... ",month,"-",day,"-",year, uniqueHours)#, flush=True)
        sys.stdout.flush()
        return None, None
    
    #If minute is a single digit less than 10 add a 0 to make it 2 digits
    elif minute < 10:   minute = '0'+ str(minute)
    # If minute less than  60 
    elif minute < 60: minute = str(minute)
    # otherwise warn and print
    else:
        print("TP: ",wfo," - ERR INVALID MINUTE: ", minute," at hour: ",hour, AMPM," ... ",short_time, " ... ",month,"-",day,"-",year, uniqueHours)#, flush=True)
        sys.stdout.flush()
        return None, None
            
    #HOUR        
    if hour == -1:        #If still not resolved
        print("TP: ",wfo," - ERR NO HOUR: ", hour, "is", AMPM," ... ",time22, " ... ",month,"-",day,"-",year, uniqueHours)#, flush=True)
        sys.stdout.flush()
        return None, None
            
    elif hour <= 11 and AMPM == 'PM':  strHour = str(hour+ 12)
    elif hour == 12 and AMPM == "AM": strHour = str("00") ## ORIGINALLY FORGOT THIS WHOOPS!!!
    elif hour == 12 and AMPM == 'PM': strHour = str(hour)
    elif hour < 10 and AMPM == 'AM': strHour = '0' + str(hour)
    elif hour >= 10 and hour <= 11 and AMPM=='AM': strHour = str(hour)
    elif hour >12  and hour < 24 and AMPM !='AM': strHour = str(hour)
    else: # i.e. >24
        if timezone == "UTC" and hour < 24:
            if hour<=11:
                AMPM == "AM"
                if len(str(hour)) != 2:
                    strHour = '0' + str(hour)
                else:
                    strHour = str(hour)
            #Change to ELSE        
            elif hour < 24:
                AMPM == "PM"
                strHour = str(hour)
            else:
                print("TP: ",wfo," - ERR INVALID HOUR (UTC): ", hour, "is", AMPM," ... ",time22, " ... ",month,"-",day,"-",year, uniqueHours)#, flush=True)
                sys.stdout.flush()
                return None, None

        elif hour < 24:
            isAssumedAMPM = True
            isAssumedInfo = True
            if hour<=11:
                AMPM == "AM"
                if len(str(hour)) != 2:
                    strHour = '0' + str(hour)
                else:
                    strHour = str(hour)
            #Change to ELSE        
            elif hour < 24:
                AMPM == "PM"
                strHour = str(hour)
            else:
                print("TP: ",wfo," - ERR INVALID HOUR (NON-UTC): ", hour, "is", AMPM," ... ",time22, " ... ",month,"-",day,"-",year, uniqueHours)#, flush=True)
                sys.stdout.flush()
                return None, None
        else:         
            print("TP: ",wfo," - ERR INVALID HOUR: ", hour, "is", AMPM," ... ",time22, " ... ",month,"-",day,"-",year, uniqueHours)#, flush=True)
            sys.stdout.flush()
            return None, None

    if AMPM != "":
        # datetime reformat with timezone info
        #combine into one string for time
        dtf = str(year) + str(mo) + str(strdayEAA) + str(strHour) + str(minute)
        
        if timezone == "":
            replace_tz = max(((item, timezone.count(item)) for item in set(timezone)), key=lambda a: a[1])[0]
            print("WARNING TZ: Substituting TZ (w/ most common TZ in sequence): ", replace_tz," at ",wfo)#, flush=True)
            sys.stdout.flush()
            TimesFound = utc_convert_reformat_time(dtf, replace_tz)
            if TimesFound == None:
                print ("ERROR CONVERTING: NOAA/NWS messed up time...Check manually for this day: ", dtf, timezone, "at ",wfo)#, flush=True)
                sys.stdout.flush()
                return None, None
            isAssumedAMPM = True
            isAssumedInfo = True

        else:
            TimesFound = utc_convert_reformat_time(dtf, timezone)
            if TimesFound == None:
                print ("ERROR CONVERTING: NOAA/NWS messed up time...Check manually for this day: ", dtf, timezone, "at ",wfo)#, flush=True)
                sys.stdout.flush()
                return None, None
            
    else:
        print("TP: ",wfo," - AMPM MISSING - FINAL CHECK: ", hour,":",minute, " ... ",date)#, flush=True)
        sys.stdout.flush()
        return None, None

    ## If there wasn't an error in CONVERTING TIME        
    if TimesFound is not None:
        if makeAssume == True:
            if isAssumedAMPM == True or isAssumedInfo == True:
                if isAssumedAMPM == True:
                    uniqueKeyWords = uniqueKeyWords+"*"
                    KeyFound = uniqueKeyWords+"*"

                if isAssumedInfo == True:
                    uniqueKeyWords = uniqueKeyWords+"#"
                    KeyFound = uniqueKeyWords+"#"
            else:
                KeyFound = uniqueKeyWords 
        else:
            if isAssumedAMPM == False and isAssumedInfo == False:
                KeyFound = uniqueKeyWords  
        #increase the count by 1 after the iteration
        count +=1      

    #Trim down to the size actually used
    FinalTimesFound = TimesFound
    KeyFound = uniqueKeyWords
    
    #return the formatted times found
    return FinalTimesFound,KeyFound