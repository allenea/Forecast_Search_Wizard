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
import re
import sys
import pytz
import datetime
from src.missing_time import wfo_rft_time_ALT


wk_days = ["MON","TUE","WED","THU","FRI","SAT","SUN", \
           "MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY", \
           "TUES","WEDS", "THURS","THUR"]

mo_str = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",\
          "JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST",\
          "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER","SEPT","0CT","N0V","0CT0BER","N0VEMBER"]

tzs = ["UTC","EST","EDT","CDT","CST","MST","MDT","PDT","PST", "AKDT", "AKST","HST",
       "HAST", "HADT","GMT","GUAM LST","ADT","AST","CHST","SST","SDT","ChST"]

def wfo_rft_time(trimTimesFound,uniqueHours,wfo, uniqueKeyWords,makeAssume,iYear,timezone):    
    """ The primary method will be used to attempt an extract of date and time information. If not possible then try the alternative method or print warnings.
    
    Parameters:
        trimTimesFound (str): Raw date info
        uniqueHours (str): Raw time info
        wfo (str): Forecast product PIL
        uniqueKeyWords (str): Keyword that was found
        makeAssume (bool): Make assumptions
        iYear (int): The year of the file being searched. Used to help assume year if missing/incomplete/typo.
        timezone (str): Timezone information associated with this instance (tz_finder)
        
    Returns:
        FinalTimesFound (datetime tuple): A datetime tuple that has been converted to UTC.
        KeyFound (str):  The keyword that was found with any req. flags
    """   
    fmtString = "%m-%d-%Y %H:%M"
    #store successfully identified cases in this array
    TimesFound = [None] * len(trimTimesFound)
    KeyFound = [None] * len(trimTimesFound)
    count = 0
    cYear = int(gettime.ctime()[-4:]) + 1
    
    #Loop through the times found list for keywords without duplicates
    for x in range(len(trimTimesFound)):
        monthNext = False; yearNext = False
        isAssumedAMPM = False; isAssumedInfo = False
        month = ""; year = -1;
        
        try:        
            dayWMOHEAD = int(uniqueHours[x][:2])
            hrWMOHEAD = int(uniqueHours[x][2:4])
            minWMOHEAD = int(uniqueHours[x][4:6])

        except:
            alt_times ,alt_keys = wfo_rft_time_ALT(trimTimesFound[x],uniqueHours[x],wfo, timezone[x], uniqueKeyWords[x],makeAssume)
            if alt_times == None or alt_keys == None:
                continue
        
            ### IN UTC
            dayWMOHEAD = alt_times.day
            hrWMOHEAD = alt_times.hour
            minWMOHEAD = alt_times.minute
            uniqueKeyWords[x] = alt_keys
            continue
        
        tmp = re.sub(r" ?\([^)]+\)", "", trimTimesFound[x]) ## ( )
        date = re.sub(r" ?/([^)]+/)", "", tmp) ## / /
    
        if any(tz1 in date for tz1 in tzs):
            date = [date.split(tz1)[1]  for tz1 in tzs if tz1 in date][0]
            ###isAssumedInfo = True not anymore
            
        #date = date.split(".")[0]  #  removes any .... Correction forecasts
        date_text = re.sub('[^A-Za-z0 ]+', ' ', date) # SPACE TO SEPARATE THE THINGS
        date_numbers = re.sub('[^0-9O ]+', '', date)
        date_numbers = (date_numbers.replace("O","0")).lstrip('0')
        
        
        
        ## HANDLES MONTH
        t_text = date_text.split()
        if len( [item.strip() for item in t_text if item in mo_str]) == 1:
            month = [item.strip() for item in t_text if item in mo_str][0] #remove empty values in array with time_text
        else:
            if len(list(set([item.strip() for item in t_text if item in mo_str]))) == 1:
                month = [item.strip() for item in t_text if item in mo_str][0]
            else:
                month = ""
                    
        #MONTH
        #if the length of month is greater than 3 for the check
        # IF MONTH NEVER ASSIGNED
        if len(month) == 0:
            print("TP: ",wfo," - ERR NO MONTH... Check:",date.strip(),"  ","??-",dayWMOHEAD,"-",iYear,"?  @",uniqueHours[x][-4:],"Z")#, flush=True)
            sys.stdout.flush()
            continue
        
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
                            continue
                # is only one then there was no month, only the week day
                # warn and skip
                else:
                    print("TP: ",wfo," - ERR MONTH - not mo+wk_day: ",date)#, flush=True)
                    sys.stdout.flush()
                    continue  
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
            continue
        
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
            print("TP: ",wfo," - Reason for UTC FAIL: ", month, "...",month,"-",dayWMOHEAD,"-",iYear)#, flush=True)
            sys.stdout.flush()
            continue                    


        
        if timezone[x] == "UTC":                
                    
            ##INITIALIZE to -1 - Impossible to be a date if all info isn't there
            if str(iYear) in date_numbers:
                year = iYear;
                date_numbers = "".join(date_numbers.split(str(year)))
                t_nums = date_numbers.split() 
    
            else:
                if dayWMOHEAD == 1 and "DEC" in date_text:
                    ## IF NEW YEAR BUT STORED IN OLD YEAR FOLDER
                    if str(iYear+1) in date_numbers:
                        #yearNext = True
                        year = iYear
                        date_numbers = "".join(date_numbers.split(str(year+1)))
                        t_nums = date_numbers.split() 
                    # IF OLD YEAR BUT STORED IN NEW (NEXT) YEAR FOLDER
                    elif str(iYear-1) in date_numbers:
                        year = iYear  # ALREADY AHEAD OR IT'S BEING STORED IN THE WRONG FOLDER
                        date_numbers = "".join(date_numbers.split(str(year-1)))
                        t_nums = date_numbers.split() 
                        isAssumedInfo = True
                    else:
                        t_nums = date_numbers.split() 
                        try:
                            year = [int(item) for item in t_nums if (item != '' and len(item) >=4 and int(item) >= 1900 and int(item) <= cYear)][0]        #remove empty values in array with time_nums
                            isAssumedInfo = True
                        except:
                            ###print("BAD", flush=True)
                            pass
                elif dayWMOHEAD == 1 and "JAN" in date_text :
                    t_nums = date_numbers.split() 
                    year = [int(item) for item in t_nums if (item != '' and len(item) >=4 and int(item) >= 1900 and int(item) <= cYear)][0]
                    
                else:
                    t_nums = date_numbers.split() 
                    year = [int(item) for item in t_nums if (item != '' and len(item) >=4 and int(item) >= 1900 and int(item) <= cYear)][0]        #remove empty values in array with time_nums
                    if year != iYear:
                        if wfo != "PMDTHR":
                            #print("DW: ",wfo," - IEM DATA WARNING - ",trimTimesFound[x].strip(), uniqueHours[x].strip(),"   STORED IN FILE YEAR:",iYear,"PROCEEDING WITH ISSUING TIME/DATE LINE AS TRUTH", flush=True)
                            isAssumedInfo = True
                
        #NON-UTC          
        else:
            
            ##INITIALIZE to -1 - Impossible to be a date if all info isn't there
            if str(iYear) in date_numbers:
                year = iYear;
                date_numbers = "".join(date_numbers.split(str(year)))
                t_nums = date_numbers.split() 
    
            else:
                if dayWMOHEAD == 1 and "DEC" in date_text:
                    ## IF NEW YEAR BUT STORED IN OLD YEAR FOLDER
                    if str(iYear+1) in date_numbers:
                        yearNext = True
                        year = iYear
                        date_numbers = "".join(date_numbers.split(str(year+1)))
                        t_nums = date_numbers.split() 
                    # IF OLD YEAR BUT STORED IN NEW (NEXT) YEAR FOLDER
                    elif str(iYear-1) in date_numbers:
                        year = iYear  # ALREADY AHEAD OR IT'S BEING STORED IN THE WRONG FOLDER
                        date_numbers = "".join(date_numbers.split(str(year-1)))
                        t_nums = date_numbers.split() 
                        isAssumedInfo = True
                    else:
                        t_nums = date_numbers.split() 
                        try:
                            year = [int(item) for item in t_nums if (item != '' and len(item) >=4 and int(item) >= 1900 and int(item) <= cYear)][0]        #remove empty values in array with time_nums
                            isAssumedInfo = True
                        except:
                            ###print("BAD", flush=True)
                            pass
                            
                elif dayWMOHEAD == 1 and "JAN" in date_text :
                    t_nums = date_numbers.split() 
                    year = [int(item) for item in t_nums if (item != '' and len(item) >=4 and int(item) >= 1900 and int(item) <= cYear)][0]
                    
                else:
                    t_nums = date_numbers.split()
                    
                    try:
                        year = [int(item) for item in t_nums if (item != '' and len(item) >=4 and int(item) >= 1900 and int(item) <= cYear)][0]        #remove empty values in array with time_nums
                    except:
                        year = iYear
                        print("TP: ",wfo," - NON FATAL ERROR - YEAR REPLACED BY FILE-YEAR... Check: ", str(year),"....",date.strip())#, flush=True)
                        sys.stdout.flush()
                        isAssumedInfo = True
                        
                    if year != iYear:
                        if wfo != "PMDTHR":
                            #print("DW: ",wfo," - IEM DATA WARNING - ",trimTimesFound[x].strip(), uniqueHours[x].strip(),"   STORED IN FILE YEAR:",iYear,"PROCEEDING WITH ISSUING TIME/DATE LINE AS TRUTH", flush=True)
                            isAssumedInfo = True
                    
            try:    
                day1 = [item for item in t_nums if item.isdigit() and (int(item) >0 and int(item) < 32)]
                day = int(day1[0])       #remove empty values in array with time_nums
                if len(day1) != 1:
                    print("TP: DAY LONG",day1,trimTimesFound[x].strip(), uniqueHours[x].strip())#, flush=True)
                    sys.stdout.flush()
            except:
                #pass
                #print("warning on day, using UTC default")#, flush=True)
                print("TP: ",wfo," - ERR NO DAY... Check:",t_nums,month,"-??-",year," @",uniqueHours[x][-4:],"Z", trimTimesFound[x].strip())#, flush=True)
                sys.stdout.flush()
                continue
                
            if dayWMOHEAD == day:
                pass
            else:
                if dayWMOHEAD == 1 and day ==31 and "DEC" in date_text:
                    yearNext = True
                    monthNext = True
                elif dayWMOHEAD == 1 and day >= 28:
                    monthNext = True
                    isAssumedInfo = True
                    
                else:
                    if abs(dayWMOHEAD - day) >=3 and abs(dayWMOHEAD - day) < 27 :
                        #print(trimTimesFound[x].strip(), "  ",uniqueHours[x].strip(), dayWMOHEAD,"  ",day)#, flush=True)
                        #sys.stdout.flush()
                        isAssumedInfo = True
                        
                        
                        
                        
                        
            ## IF NOT UTC
            if monthNext == True and yearNext == True:
                mo = int(mo) + 1
                #day = 1
                if mo == 13:
                    mo = 1
                    year+=1
            elif monthNext == True:
                mo = int(mo) + 1
                #day = 1
                if mo == 13:
                    ####print("TP: NO yearNEXT FLAG",trimTimesFound[x].strip(), iYear,"\\\///",uniqueHours[x])#, flush=True)
                    ####sys.stdout.flush()
                    mo = 1
                    year+=1
                isAssumedInfo == True
            elif yearNext == True:
                year+=1
                ####print("TP: NO MONTH CHANGE",trimTimesFound[x].strip(),iYear,"\\\///",uniqueHours[x])#, flush=True)
                ####sys.stdout.flush()

# =============================================================================
# DONE WITH EXTRACTING YEAR, MONTH, DAY
# =============================================================================

        #!!! Outside year range  - modify for CPC... don't because not processed in main search b/c year == year
        if year <1950:
            if wfo == "PMDTHR":
                year = year + 100
            else:
                print("TP: ",wfo," - NON FATAL ERROR - YEAR REPLACED BY FILE-YEAR... Check: ",\
                       str(year),"....",date)#, flush=True)
                sys.stdout.flush()
                #year = iYear  ## idea?
                continue  
            

        # puts it in a datetime tuple
        try:
            #tz = pytz.timezone(timezone[x])
            dt_str = datetime.datetime(int(year),int(mo),\
                                    int(dayWMOHEAD),int(hrWMOHEAD),int(minWMOHEAD))
            #offset_seconds = tz.utcoffset(dt_str).seconds
            #offset_hours = offset_seconds / 3600.0
   
        except:
                if dayWMOHEAD == 31:
                    mo = int(mo) - 1
                    try:
                        dt_str = datetime.datetime(int(year),int(mo),\
                            int(dayWMOHEAD),int(hrWMOHEAD),int(minWMOHEAD))
                        isAssumedInfo = True
                    except:
                        dtf = str(year) + str(mo) + str(dayWMOHEAD) + str(hrWMOHEAD) + str(minWMOHEAD)
                        print("TP: FORMATTING FAILED", dtf,"  ",trimTimesFound[x].strip(), uniqueHours[x].strip())#, flush=True)
                        sys.stdout.flush()

                        continue
                else:
                    dtf = str(year) + str(mo) + str(dayWMOHEAD) + str(hrWMOHEAD) + str(minWMOHEAD)
                    print("TP: FORMATTING FAILED", dtf,"  ",trimTimesFound[x].strip(), uniqueHours[x].strip())#, flush=True)
                    sys.stdout.flush()
                    continue

        #Formats the date to a text string
        fmtDate=dt_str.strftime(fmtString)
        #get's the datetime tuple again
        naive = datetime.datetime.strptime(fmtDate,fmtString)
        # What the computer originally thinks the time-zone info is (what it was given by tz_finder)
        local = pytz.timezone("UTC")
        #Assign that timezone to the time and localize the time
        final_time_string = local.localize(naive)
        #print(final_time_string)#, flush=True)
        #sys.stdout.flush()

        
        #Handles Assumptions
        if final_time_string is not None:
            if makeAssume == True:
                TimesFound[count] = final_time_string
                if isAssumedAMPM == True or isAssumedInfo == True:
                    if isAssumedAMPM == True:
                        uniqueKeyWords[x] = uniqueKeyWords[x]+"*"
                        KeyFound[count] = uniqueKeyWords[x]+"*"

                    if isAssumedInfo == True:
                        uniqueKeyWords[x] = uniqueKeyWords[x]+"#"
                        KeyFound[count] = uniqueKeyWords[x]+"#"
                else:
                    KeyFound[count] = uniqueKeyWords[x]   
            else:
                if isAssumedAMPM == False and isAssumedInfo == False:
                    TimesFound[count] = final_time_string
                    KeyFound[count] = uniqueKeyWords[x]   
            #increase the count by 1 after the iteration
            count +=1      

    #Trim down to the size actually used
    FinalTimesFound = TimesFound[:count]
    KeyFound = uniqueKeyWords[:count]

    #return the formatted times found
    return FinalTimesFound,KeyFound