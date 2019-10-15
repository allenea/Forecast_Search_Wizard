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
import re,sys
 
def covertSPC(wfo, iYear, text, DDHHMM):
    """TESTED"""
    isSuccess = False; DATETIME_STRING = ""
    sYear = str(iYear); length_file = len(text)
    ADMIN_MAX_ALLOW = 150
    for lineIDX in range(0,ADMIN_MAX_ALLOW+1,1):
        
        #FAILURE
        if lineIDX == length_file:  return DATETIME_STRING, isSuccess          
        
        elif "NWS STORM PREDICTION CENTER NORMAN OK" in text[lineIDX]:
            if sYear in text[lineIDX + 1]:
                DATETIME_STRING = text[lineIDX + 1].strip()
                if DATETIME_STRING != "":  
                    isSuccess = True
                    return DATETIME_STRING, isSuccess
            
            
            elif str(iYear + 1) in text[lineIDX + 1]:
                DATETIME_STRING = text[lineIDX + 1].strip()
                if DATETIME_STRING != "":  
                    isSuccess = True
                    return DATETIME_STRING, isSuccess
            
        elif "...." in re.sub('[^.]+', '', text[lineIDX]):
            if  "//" in re.sub('[^/]+', '', text[lineIDX]):
                maybeDate = re.sub('[^0-9/]+', '', text[lineIDX])
                maybeDate = maybeDate.rstrip("/")
                maybeDate = maybeDate.lstrip("/")
                subLen = len(re.sub('[^0-9]+', '', maybeDate))
                if  subLen >=4 and subLen <= 8:
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
                            if abs(int(sYear) - int(year)) > 1:   continue
                            elif "2000-" in text[lineIDX]:   continue
                        else:
                            #...FOR THE PERIOD 25/12Z THROUGH 26/03Z...
                            #... 04/12Z-05/03Z ...
                            if abs(int(sYear[-2:]) - int(year)) > 1: continue
                        
                    if int(month) > 12: continue
                        
                    if int(day) > 31: continue
                        
                    if str(day) == str(DDHHMM[:2]):  day = DDHHMM[:2]
                    
                    ## EVERYTHING IS GOOD
                    DATETIME_STRING, isBad = make_string(DDHHMM, year, month, day,iYear,wfo)
                    
                    # IF IT'S GOOD....
                    if DATETIME_STRING != "" or isBad == False: isSuccess = True

                    return DATETIME_STRING, isSuccess
    # CERTAIN FAILURE
    return DATETIME_STRING, isSuccess
   
    
def make_string(DDHHMM, year, month, day,iYear,wfo):
    isBad = False
    """TESTED"""
    
    #WE'LL ALLOW IT WITHOUT ASSUMPTION... WITHIN "MARGIN OF ERROR"
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
                    if len(year) <2:
                        year = "0" + year
            # MONTH PLUS 1... If Dec --> JAN Year + 1
            
        # DOES NOT APPEAR TO EVER HAPPEN...
        elif DDHHMM[:2] == "31" and int(day) == 1:
            month = int(month) - 1
            if month == 0:
                month = 12
                year = iYear -1
                if year == -1:  year = "99"
                else:  year = str(year)
        #RARELY HAPPENS
        else:
            #print("PRE2003-SPC: DISCREPANCY BETWEEN DAY & DDHHMM TOO LARGE: ", DDHHMM, "Day: ", day, "Month: ", month, "Year/iYear: ", year, " / ", iYear)#, flush=True)
            #sys.stdout.flush()
            isBad = True
        
    #PUT IT TOGETHER
    strMONTH = getMonth(str(month)) 
    strYEAR = checkYear(year,iYear,strMONTH)

    if strYEAR == -9999:
        #print("PRE2003-SPC: AN UNSAFE ASSUMPTION WOULD HAVE TO BE MADE ON YEAR...", year,iYear, month)#, flush=True)
        #sys.stdout.flush()
        isBad = True

    HHMM = str(DDHHMM[2:])
    if int(DDHHMM[2:]) >= 1200: AMPM = "PM"
    else: AMPM = "AM"
    strNUMDAY = int(DDHHMM[:2])
    
    if isBad == False:
        DATETIME_STRING = HHMM+" "+AMPM+" UTC "+ "NOTADAY"  + " " + strMONTH + " "+ str(strNUMDAY)+" " + str(strYEAR)
        return DATETIME_STRING, isBad
    else:
        DATETIME_STRING = ""
        return DATETIME_STRING, isBad

def getMonth(mo):
    """TESTED"""
    if mo.isdigit():
        intMonth = int(mo)
        if   intMonth == 1: month = "JAN"
        elif intMonth == 2: month = "FEB"
        elif intMonth == 3: month = "MAR"
        elif intMonth == 4: month = "APR"
        elif intMonth == 5: month = "MAY"
        elif intMonth == 6: month = "JUN"
        elif intMonth == 7: month = "JUL"
        elif intMonth == 8: month = "AUG"
        elif intMonth == 9: month = "SEP"
        elif intMonth == 10: month = "OCT"
        elif intMonth == 11: month = "NOV"
        elif intMonth == 12: month = "DEC"
        else: month = "NAN"
        return month
    else:
        return "NAN"

def checkYear(year,iYear, month):
    """TESTED"""
    if len(year) == 4:
        year = int(year)
    else:
        if year > "90": year = int(str("19")+year)
        else: year = int(str("20")+year)
    
    if year == iYear:  return iYear
    elif year == iYear + 1:
        if month == "JAN":  return iYear + 1
        elif month == "DEC":  return iYear
        else: return -9999
    elif year == iYear - 1:
        if month == "DEC":  return iYear - 1
        elif month == "JAN":  return iYear
        else: return -9999
    else: return -9999
    
ST_lst = ["EST","MST","PST","AST","SST","AKST","HAST","HST","CHST","ChST","GUAM LST","LST"]
DT_lst = ["EDT","MDT","PDT","AKDT","HADT","SDT","ADT"] 
wk_days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]   
def timezone_finder_SPC(DATETIME_STRING,last_tz):
    """ Identifies the date/time information and an acceptable time zone. Stops.

    Parameters:
        DATETIME_STRING (str): Raw text data line created in Pre2003_SPC
        last_tz (str): The last timezone used in this product (most likely the same as the next more times than not)
        
    Returns:
        date (str): Actually the time! info
        time (str): Actually the date! info
        timezone (str): pytz formatted time zone equivalent to the abbriviation
    """       
    line = DATETIME_STRING
    line = line.split("..")[0]

    if "CDT" in line:
            date = line.split("CDT")
            return date[0].strip(), date[1].strip(),"US/Central"
    if "CST" in line:
        date = line.split("CST")  
        return date[0].strip(), date[1].strip(),"US/Central"
    
    if "UTC" in line:
        date = line.split("UTC")
        return date[0].strip(), date[1].strip(), "UTC"
    
    #Remove : from names
    line = "".join(line.split(":"))
    line = re.sub(r" ?\([^)]+\)", "", line) ## remove between the ( )
    
                    
    # NWS MODERNIZATION. STANDARD FORM 
    if "DT" in line and any(dt in line for dt in DT_lst):
        if "EDT" in line:
            date = line.split("EDT")
            return date[0].strip(), date[1].strip(),"US/Eastern"

        elif "MDT" in line:
            date = line.split("MDT")
            return date[0].strip(), date[1].strip(),"US/Mountain"
        
        elif "PDT" in line:
            date = line.split("PDT")
            return date[0].strip(), date[1].strip(), "US/Pacific"
        
        elif "AKDT" in line:
            date = line.split("AKDT")
            return date[0].strip(), date[1].strip(), "US/Alaska"
        
        elif "HADT" in line:
            date = line.split("HADT")
            return date[0].strip(), date[1].strip(),"Pacific/Honolulu"
        
        elif "SDT" in line:
            date = line.split("SDT")
            return date[0].strip(), date[1].strip(),"US/Samoa"
        
        elif "ADT" in line:
            date = line.split("ADT")  
            return date[0].strip(), date[1].strip(), "America/Halifax"       
        
        
    if "ST" in line and any(st in line for st in ST_lst):
        if "EST" in line:
            date = line.split("EST")  
            return date[0].strip(), date[1].strip(),"US/Eastern"

        elif "MST" in line:
            date = line.split("MST")  
            return date[0].strip(), date[1].strip(),"US/Mountain"
        
        elif "PST" in line:
            date = line.split("PST")  
            return date[0].strip(), date[1].strip(),"US/Pacific"
        
        elif "HAST" in line:
            date = line.split("HAST")  
            return date[0].strip(), date[1].strip(),"Pacific/Honolulu"      
        
        elif "AST" in line:
            if "EASTERN" in line:
                date = line.split("EASTERN")  
                return date[0].strip(), date[1].strip(),"US/Eastern"
            else:
                date = line.split("AST")  
                return date[0].strip(), date[1].strip(),"America/Halifax"
        
        elif "SST" in line:
            date = line.split("SST")  
            return date[0].strip(), date[1].strip(),"US/Samoa"   
        
        elif "AKST" in line:
            date = line.split("AKST")  
            return date[0].strip(), date[1].strip(),"US/Alaska"
        
        elif "CHST" in line:
            date = line.split("CHST")
            return date[0].strip(), date[1].strip(),"Pacific/Guam"  
        
        elif "ChST" in line:
            date = line.split("ChST")  
            return date[0].strip(), date[1].strip(),"Pacific/Guam"
        
        elif "HST" in line:
            date = line.split("HST")  
            return date[0].strip(), date[1].strip(),"Pacific/Honolulu"
        
        elif "GUAM LST" in line:  
            date = line.split("GUAM LST")
            return date[0].strip(), date[1].strip(),"Pacific/Guam"
    
    if "GMT" in line:  
        date = line.split("GMT")
        return date[0].strip(), date[1].strip(),"UTC"
    
    ## FOR ONE MORON
    elif "EASTERN" in line:
        date = line.split("EASTERN")  
        return date[0].strip(), date[1].strip(),"US/Eastern" 
    
    elif "CENTRAL" in line:
        date = line.split("CENTRAL")  
        return date[0].strip(), date[1].strip(),"US/Central" 
    else:
        if any(word in line for word in wk_days):
            for word in wk_days:
                if word in line:
                    if "." in line:
                        tmp = line.split(".")
                        tmp2 = tmp[0].split(word)
                        return tmp2[0].strip(), tmp2[1].strip(),last_tz
                    else:
                        tmp2 = line.split(word)
                        return tmp2[0].strip(), tmp2[1].strip(),last_tz
        elif "PM" in line:
            date = line.split("PM")
            return date[0].strip(), date[1].strip(),last_tz
    
        elif "AM" in line:
            date = line.split("AM")
            return date[0].strip(), date[1].strip(),last_tz
        
        else:
            return "","",""