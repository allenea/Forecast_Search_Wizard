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
import re,sys

wk_days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
ST_lst = ["EST","CST","MST","PST","AST","SST","AKST","HAST","HST","CHST","ChST","GUAM LST","LST"]
DT_lst = ["EDT","CDT","MDT","PDT","AKDT","HADT","SDT","ADT"]
    
def timezone_finder(readData,iHolder,last_tz):
    """ Identifies the date/time information and an acceptable time zone. Stops.

    Parameters:
        readData (list of strings): Raw text data
        iHolder (int): Index of suspected date/time information in the list of strings
        last_tz (str): The last timezone used in this product (most likely the same as the next more times than not)
        
    Returns:
        date (str): Actually the time! info
        time (str): Actually the date! info
        timezone (str): pytz formatted time zone equivalent to the abbriviation
    """
    line = readData[iHolder]
    line = line.split("..")[0]
    
    #LEGACY PRODUCTS
    if "ISSUE" in line:
        #%% SPWC       #uses colons so use before the colon removal
        if  "ISSUED:" in line:
            if "UTC" in line:
                tmp = line.split("ISSUED:")
                d1 = tmp[1].strip()
                tmp2 = d1.split("UTC")
                date = tmp2[0].strip()
                return date[-4:].strip(), date[:-4].strip(),"UTC"
            
        elif "ISSUE:" in line:
            if "UTC" in line:
                tmp = line.split("ISSUE:")
                d1 = tmp[1].strip()
                tmp2 = d1.split("UTC")
                date = tmp2[0].strip()
                return date[-4:].strip(), date[:-4].strip(),"UTC"
            
        elif  "ISSUE TIME:" in line:
            if "UTC" in line:
                tmp = line.split("ISSUE TIME:")
                d1 = tmp[1].strip()
                tmp2 = d1.split("UTC")
                date = tmp2[0].strip()
                return date[-4:].strip(), date[:-4].strip(),"UTC"
            
    if "UT" in line:
        # ["HPC FORECAST VALID 00 UTC 1 JAN THRU 00 UTC 8 JAN 2002"]
        # [" 00 UTC 1 JAN THRU 00 UTC 8 JAN 2002"]
        # [" 00 UTC 1 JAN ", " 00 UTC 8 JAN 2002"]
        # [" 00 UTC 1 JAN "], +  [" 00 " "UTC"  "8" "JAN" "2002"] [ -1]
        # [" 00 UTC 1 JAN 2002"]
        # [00] ___ [1 JAN 2002] [UTC]
        if "HPC FORECAST" in line:  ### - WORKING
            #"HPC FORECAST VALID 00 UTC 1 JAN THRU 00 UTC 8 JAN 2002"
            tmp = line.split("VALID")[1]
            tmp = tmp.split("THRU")
            tmp2 = tmp[0]
            newString = ''.join([tmp2, tmp[1].split()[-1]])
            new = newString.split("UTC")
            return new[0].strip(), new[1].strip(),"UTC"
        
        if "UTC" in line:
            if ":" in line:
                tmp = line.split(":")
                tmp2 = tmp[2].split("UTC")
                date = tmp2[0].strip()
                return date[-4:].strip(), date[:-4].strip(),"UTC"
            else:
                tmp = line.split("UTC")
                date = tmp[0].strip()
                time = tmp[1].strip()
                return date.strip(), time.strip(), "UTC"

        # UTC SPELLED WRONG - FOR SWPC  - down here b/c it interfers with some cases higher w/ UTC
        if "UT" in line:  
            line = "".join(line.split(":"))
            tmp = line.split("ISSUED")
            d1 = tmp[1].strip()
            tmp2 = d1.split("UT")
            date = tmp2[0].strip()
            return date[-4:].strip(), date[:-4].strip(),"UTC"
    
    #Remove : from names
    line = "".join(line.split(":"))
    line = re.sub(r" ?\([^)]+\)", "", line) ## remove between the ( )
    
     # LEGACY PRODUCT
    if ("NCEP PROGNOSTIC DISCUSSION").upper() in line: # - WORKING
         #"NCEP PROGNOSTIC DISCUSSION FROM 0000Z MON DEC 24 2001
        tmp = line.split("FROM")[1]
        if "Z" in tmp:
            tmp2 = tmp.split("Z")
            return tmp2[0].strip(), tmp2[1].strip(),"UTC"
        else:
            tmp2 = tmp
            # Weekday name is included
            if any(word in tmp2 for word in wk_days):
                for word in wk_days:
                    if word in tmp2:
                        tmp3 = tmp2.split(word)
                        return tmp3[0].strip(), tmp3[1].strip(),"UTC"
                    
    #%% NWS MODERNIZATION. STANDARD FORM 
    if "DT" in line and any(dt in line for dt in DT_lst):
        if "EDT" in line:
            date = line.split("EDT")
            return date[0].strip(), date[1].strip(),"US/Eastern"
        
        elif "CDT" in line:
            date = line.split("CDT")
            return date[0].strip(), date[1].strip(),"US/Central"
        
        elif "MDT" in line:
            date = line.split("MDT")
            return date[0].strip(), date[1].strip(),"US/Mountain"
        
        elif "PDT" in line:
            date = line.split("PDT")
            return date[0].strip(), date[1].strip(),"US/Pacific"
        
        elif "AKDT" in line:
            date = line.split("AKDT")
            return date[0].strip(), date[1].strip(),"US/Alaska"
        
        elif "HADT" in line:
            date = line.split("HADT")
            return date[0].strip(), date[1].strip(),"Pacific/Honolulu"
        
        elif "SDT" in line:
            date = line.split("SDT")
            return date[0].strip(), date[1].strip(),"US/Samoa"
        
        elif "ADT" in line:
            date = line.split("ADT")  
            return date[0].strip(), date[1].strip(),"America/Halifax"       
        
        
    if "ST" in line and any(st in line for st in ST_lst):
        if "EST" in line:
            date = line.split("EST")  
            return date[0].strip(), date[1].strip(),"US/Eastern"
        
        elif "CST" in line:
            date = line.split("CST")  
            return date[0].strip(), date[1].strip(),"US/Central"
        
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
        
        elif "LST" in line and "TIYAN" in readData[iHolder-1] or "PAGO" in readData[iHolder-1]: ## NOT TESTED FOR BUT CHECKED THAT IT WORKS...
            date = line.split("LST")
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

    ## If you made it this far it is not one of the above so start if/elif/ over again
    ## FINAL EXCEPTION FOR MISSING TIME ZONE INFO.... OR NOT TIME
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

    elif len(line.strip()) < 9: # WAS 5... NOW 9
         iHolder +=1
         return timezone_finder(readData,iHolder,last_tz)
     
    # Used in like 4 cases for SWPC
    elif "SERIAL NUMBER" in line:
        iHolder+=1
        return timezone_finder(readData,iHolder,last_tz)
    
    
    elif "PM" in line:
        date = line.split("PM")
        return date[0].strip(), date[1].strip(),last_tz
    
    elif "AM" in line:
        date = line.split("AM")
        return date[0].strip(), date[1].strip(),last_tz
      
    #else:    #PRINT BADWARNING in finder.py
    #    print("TZ_BADWARNING ", line)#, flush = True)
    #    sys.stdout.flush()
    
    ### FOR TESTING PURPOSES ONLY... KEEP COMMENTED OUT
    
    # HAVING AN ELSE WOULD JUST REITERATE WHAT BADWARNING reports and any
    # keywords found at the header of a file before index has changed from 0