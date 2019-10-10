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
from src.time_functions import get_Issuing_Time_text, get_Issuing_Date_text, getDDHHMM, checkEverything, getFirstGuess
from src.convert_time import convert_time
import sys

wk_days = ["MON","TUE","WED","THU","FRI","SAT","SUN", \
           "MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY", \
           "TUES","WEDS", "THURS","THUR"]

mo_str = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",\
          "JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST",\
          "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER","SEPT","0CT","N0V","0CT0BER","N0VEMBER"]

tzs = ["UTC","EST","EDT","CDT","CST","MST","MDT","PDT","PST", "AKDT", "AKST","HST",
       "HAST", "HADT","GMT","GUAM LST","ADT","AST","CHST","SST","SDT","ChST"]


fmtString = "%m-%d-%Y %H:%M"

def wfo_rft_time(trimTimesFound,uniqueHours,DDHHMM_LIST, wfo, uniqueKeyWords,makeAssume,iYear,timezone):
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

    #store successfully identified cases in this array
    TimesFound = [None] * len(trimTimesFound)
    KeyFound = [None] * len(trimTimesFound)
    count = 0
    replace_tz = max(((item, timezone.count(item)) for item in set(timezone)), key=lambda a: a[1])[0]

    #Loop through the times found list for keywords without duplicates
    for x in range(len(trimTimesFound)):
        try:
            majorAssume = False; minorAssume = False; missingDDHHMM=False;
            _DD, _HH, _MM = getDDHHMM(DDHHMM_LIST[x])
            if DDHHMM_LIST[x] == "999999": missingDDHHMM = True
                
            year, month, text_day, isAssumed2 = get_Issuing_Date_text(trimTimesFound[x], iYear, wfo, DDHHMM_LIST[x])
            
            if isAssumed2 == None:
                if year == None:
                    print("TP: ",wfo," - ERR YEAR... None Found. FATAL. Check File:",iYear," for ", year,"    ",month,"-",text_day,"-????"," @",DDHHMM_LIST[x],"Z")
                    sys.stdout.flush()
                if month == None:
                    print("TP: ",wfo," - ERR NO MONTH FOUND... FATAL.  ","??-",_DD,"-",year," @",DDHHMM_LIST[x],"Z  Check:", trimTimesFound[x].strip())
                    sys.stdout.flush()
                continue 
            
            if isAssumed2 == True:
                majorAssume = True
                if text_day == None:
                    #print("TP: ",wfo," - ERR NO DAY FOUND...ASSUMPTION THAT DDHHMM IS CORRECT. ", month,"-??-",year," @",DDHHMM_LIST[x],"Z  Check:", trimTimesFound[x].strip())
                    sys.stdout.flush()
                    fyr, fmon, fday, HH, MM, isAssumedNew = checkEverything(DDHHMM_LIST[x], year, month, _DD, iYear)
                    if isAssumedNew == None or isAssumedNew == True:
                        print("TP: ",wfo," - UNABLE TO VERIFY DAY ASSUMPTION WITH CONFIDENCE...  FATAL. ", month,"-??-",year," @",DDHHMM_LIST[x],"Z  Check:", trimTimesFound[x].strip())
                        sys.stdout.flush()
                        continue
                    else:
                        print("TF: ",wfo," - ERR NO DAY FOUND...ASSUMPTION THAT DDHHMM IS CORRECT WAS VERIFIED!","  ", month,"-??-",year," @",DDHHMM_LIST[x],"Z")
                        sys.stdout.flush()
                        continue
                else:
                    if missingDDHHMM == True:
                        print("TF: ",wfo," - IEM Error with an None Type value. Exiting... Check File:",iYear," for  ",month,"-",text_day,"-",year," @",DDHHMM_LIST[x],"Z",trimTimesFound[x].strip(),"   ","___/",year,"/",iYear)
                        sys.stdout.flush()
                    else:
                        print("TF: ",wfo," - Possible IEM Error with an unexpected value. CONTINUING... Check File:",iYear," for  ",month,"-",text_day,"-",year," @",DDHHMM_LIST[x],"Z",trimTimesFound[x].strip(),"   ","___/",year,"/",iYear)
                        sys.stdout.flush()
                    
                if timezone == "":
                    timezone[x] = replace_tz
            else:
                if timezone == "":
                    timezone[x] = replace_tz
    
    
            if _DD != None: #THEN ALL NONE
                first_guess = getFirstGuess(year, month, int(_DD),int(_HH),int(_MM), timezone[x])
                hour, minute, AMPM, isAssumed1 = get_Issuing_Time_text(uniqueHours[x], first_guess, timezone[x], wfo)
                fyr, fmon, fday, HH, MM, isAssumedNew = checkEverything(DDHHMM_LIST[x], year, month, text_day, iYear)
            else:#IS NONE
                hour, minute, AMPM, isAssumed1 = get_Issuing_Time_text(uniqueHours[x], None, timezone[x], wfo)
                isAssumedNew = None
                if isAssumed1 == None:
                    print("TP: NO DDHHMM or Time Information....")
                    sys.stdout.flush()
                    continue
    
    
    
            if isAssumedNew == False and isAssumed1 == True:
                #No assumption just use the WMO HEADER
                final_time_string = convert_time(int(fyr),int(fmon), int(fday),int(HH),int(MM))
            
            elif isAssumedNew == False and isAssumed1 == False:
                #No assumption just use the MND HEADER
                final_time_string = convert_time(year,month, int(text_day),int(hour),int(minute), timezone=timezone[x])
                    
            elif(hour, minute, AMPM, isAssumed1) != (None, None, None, None) and isAssumed2 == False:
                if missingDDHHMM == True:
                    final_time_string = convert_time(int(year),int(month), int(text_day),int(hour),int(minute), timezone=timezone[x])
                    #IF MND HEADER WAS GOOD FOR EVERYTHING BUT TIME.. EXCEPT NO DDHHMM header :(
                    majorAssume = True
                else:
                    final_time_string = convert_time(int(year),int(month), int(_DD),int(_HH),int(_MM))
                    #IF MND HEADER WAS GOOD FOR EVERYTHING BUT TIME.. USE DDHHMM from WMO HEADER
                    minorAssume = True
                
            elif isAssumedNew == True and isAssumed1 == False:
                if isAssumed2 == True:
                    print("TP: SOMETHING WRONG WITH YYYY MM DD")
                    majorAssume = True
                else:
                    minorAssume = True
                #YES assumption just use the MND HEADER
                final_time_string = convert_time(year,month, int(text_day),int(hour),int(minute), timezone=timezone[x])
                
            elif isAssumedNew == True and isAssumed1 == True:
                #YES assumption just use the MND HEADER
                majorAssume = True
                final_time_string = convert_time(int(year),int(month), int(_DD),int(_HH),int(_MM))
    
            else:#isAssumedNew == None
                if isAssumed2 == True:
                    print("TP: SOMETHING WRONG WITH YYYY MM DD")
                    majorAssume = True
                else:
                    minorAssume = True
                final_time_string = convert_time(int(year),int(month), int(_DD),int(_HH),int(_MM))
    
    
    
            
            if isAssumedNew != None and final_time_string is not None:
                Test3 = convert_time(int(fyr),int(fmon), int(fday),int(HH),int(MM))
                difference_time = abs((Test3 - final_time_string).total_seconds()/(60*60))
                if difference_time > 6:
                    minorAssume = True
                    print("TP: MINOR DISCREPANCY - Using: ", final_time_string.strftime(fmtString), isAssumedNew, "\t /// \tOther: ", Test3.strftime(fmtString), "\t+++", "{:4.2f}".format(difference_time),"\t", trimTimesFound[x].strip(),"\t",uniqueHours[x].strip(), "\tTIME DEFAULT - Day: ", _DD," - Hour: ",_HH," - Minute: ", _MM,"  UTC")
                    sys.stdout.flush()
            else:
                if (hour, minute, AMPM, isAssumed1) != (None, None, None, None) and final_time_string is not None:
                    Test3 = convert_time(year,month, int(text_day),int(hour),int(minute), timezone[x])
                    difference_time = abs((Test3 - final_time_string).total_seconds()/(60*60))
    
                    if difference_time > 6:
                        majorAssume = True
                        print("TP: Major DISCREPANCY - Using: ", final_time_string.strftime(fmtString), isAssumedNew, "\t /// \tOther: ", Test3.strftime(fmtString), "\t+++", "{:4.2f}".format(difference_time),"\t", trimTimesFound[x].strip(),"\t",uniqueHours[x].strip(), "\tTIME DEFAULT - Day: ", _DD," - Hour: ",_HH," - Minute: ", _MM,"  UTC")
                        sys.stdout.flush()
                    else:
                        print("TP: MNBVFDRTYU: ", final_time_string, year,month, text_day,hour,minute, timezone[x])
                #else: just use WMO HEADER FOR TIME...
    

            if final_time_string is not None:
                if makeAssume == True:
                    TimesFound[count] = final_time_string
                    if majorAssume == True or minorAssume == True:
                        if majorAssume == True:
                            uniqueKeyWords[x] = uniqueKeyWords[x]+"*"
                            KeyFound[count] = uniqueKeyWords[x]+"*"
                        if minorAssume == True:
                            uniqueKeyWords[x] = uniqueKeyWords[x]+"#"
                            KeyFound[count] = uniqueKeyWords[x]+"#"
                    #if Assumption == True:
                    #    uniqueKeyWords[x] = uniqueKeyWords[x]+"#"
                    #    KeyFound[count] = uniqueKeyWords[x]+"#"       
            
                    else:
                        KeyFound[count] = uniqueKeyWords[x]   
                        
                else:
                    if majorAssume == False or minorAssume == False:
                        TimesFound[count] = final_time_string
                        KeyFound[count] = uniqueKeyWords[x]  
                        
                #increase the count by 1 after the iteration
                count +=1      
        except:
            print("TP: CATASTROPHIC ERROR")
            sys.stdout.flush()
            continue
    #Trim down to the size actually used
    FinalTimesFound = TimesFound[:count]
    KeyFound = uniqueKeyWords[:count]

    #return the formatted times found
    return FinalTimesFound,KeyFound