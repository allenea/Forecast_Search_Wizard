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
import sys, os
import time as t
import re
# MY PACKAGES
from src.tz_finder import timezone_finder
from src.wfo_read_time import wfo_rft_time
from src.sort_time import sort_time
from src.print_search_info import algor_stats
from src.write_output import write_output_file
from search_options.search_options import Option
from src.Pre2003_SPC import covertSPC, timezone_finder_SPC


total_forecast = ['NATIONAL WEATHER SERVICE','NATIONAL HURRICANE CENTER','STORM PREDICTION CENTER','TROPICAL PREDICTION CENTER',
                 'NWS WEATHER PREDICTION CENTER','NWS CLIMATE PREDICTION CENTER','OCEAN PREDICTION CENTER',
                 'NCEP PROGNOSTIC DISCUSSION FROM','CENTRAL PACIFIC HURRICANE CENTER','HYDROMETEOROLOGICAL PREDICTION CENTER',
                 'MARINE PREDICTION CENTER', 'SPACE WEATHER MESSAGE CODE',':ISSUED:','HPC FORECAST VALID','ALASKA FORECAST DISCUSSION',
                 'SOUTHCENTRAL AND SOUTHWEST ALASKA',"IN SPC BACKUP CAPACITY", "NATIONAL CENTERS FOR ENVIRONMENTAL PREDICTION",
                 "CLIMATE PREDICTION CENTER NCEP","NEW YORK STATEWIDE POLICE INFORMATION NETWORK","HIGH SEAS FORECAST"]

ID_TOP_FCST = ["OCEAN PREDICTION CENTER",'MARINE PREDICTION CENTER','NATIONAL WEATHER SERVICE','NATIONAL HURRICANE CENTER',\
               'TROPICAL PREDICTION CENTER','ALASKA FORECAST DISCUSSION','SOUTHCENTRAL AND SOUTHWEST ALASKA'] #'TROPICAL ANALYSIS AND FORECAST BRANCH'

ID_TOP_FCST2 = ['NWS CLIMATE PREDICTION CENTER','NWS WEATHER PREDICTION CENTER', "IN SPC BACKUP CAPACITY",\
                'STORM PREDICTION CENTER','HYDROMETEOROLOGICAL PREDICTION CENTER',"CENTRAL PACIFIC HURRICANE CENTER",\
                "NATIONAL CENTERS FOR ENVIRONMENTAL PREDICTION","CLIMATE PREDICTION CENTER NCEP"]

ID_TOP_FCST3= ["NCEP PROGNOSTIC DISCUSSION FROM","HPC FORECAST VALID",'SPACE WEATHER MESSAGE CODE',':ISSUED:',\
               "NEW YORK STATEWIDE POLICE INFORMATION NETWORK","HIGH SEAS FORECAST"]

def AFD_finder(FSW_SEARCH, run_start_time): 
    """ Primary searching function to identify keywords and starts of forecasts...
    
    Parameters:
        inputKey (list): List of keywords
        station_list (list): List of products to be searched
        start (int): Start year
        end (int): End year
        run_start_time (str): yymmdd_HHMM for output file naming
        searchSEClist (None): Not implemented yet
        andor (bool): Search for all words or any words
        byforecast (bool): Search by forecast or by day
        makeAssume (bool): Make assumptions
            
    Returns:
        outputfileOUT (file): Search results
    """   
    startT = t.time()
    print("Start Time: " + t.ctime())#, flush=True)
    sys.stdout.flush()
    ## SET SOME DIRECTORY PATHS
    extension = ".txt"           # INPUT AND OUTPUT FILE THE SAME FORMAT
    indir = FSW_SEARCH['TEXT_DATA_PATH']
    outdir = FSW_SEARCH['OUTPUT_PATH']
    inputKey = FSW_SEARCH['KEYWORD_LIST']
    shortestword = len(min(inputKey, key=len)) # skip rows len shorter than shortest word.... but what if the word is longer than one row.....
    biggestword = len(max(inputKey, key=len))
    testQuickCountFcst = 0
# =============================================================================
#  OUTFILE NAMING ...    --- REMOVE AND MODIFY FOR WEBSITE
# =============================================================================
    stLEN = len(FSW_SEARCH['STATION_LIST'])
    outfile = run_start_time +"_"+ inputKey[0].replace(" ", "_")+"_"+str(stLEN)+"_"+str(FSW_SEARCH['START_YEAR'])+"_"+str(FSW_SEARCH['END_YEAR']) +"_Forecast_Search_Wizard" + extension  
    print("Outfile: "+outfile)#, flush=True)
    print()
    sys.stdout.flush()

# =============================================================================
#  Sets variables and constants --- KEEP
# =============================================================================    
    ## FINAL OUTPUT FILE AND DIRECTORY LOCATION
    outputfile = os.path.join(outdir,outfile)
    ## Initialize Parameters and local variables
    masterList = []; masterList2 = []; masterList3 = []; ## Time ## Location
    no_dups = 0; prodsIssued = 0; countBad = 0; countDupFcst=0;countTry=0;
    reset_count=0; #lastIdxFnd = 0;lastfile_str="";
    
    # total = total_mentions # good = can be assertained by subtracting TZ Errors from Total Mentions
    keywordCounts = [0] * len(inputKey)    # USED TO COUNT FREQUENCY OF KEYWORDS
    keywordCountsFINAL = [0] * len(inputKey)    # USED TO COUNT FREQUENCY OF KEYWORDS
    falseList = [False] * len(inputKey)  # PERMENANT... ONLY MAKE A COPY OF THIS LATER

# =============================================================================
# ITERATE THROUGH PRODUCTS TO BE SEARCHED   -- KEEP
# =============================================================================
    print("Begin Search")#, flush=True)
    sys.stdout.flush()

    #Loops through all the files it's been told to loop through
    for wfo in FSW_SEARCH['STATION_LIST']:
        # Reset for each issuing branch
        last_tz = ""  # Uses last sucessful timezone if current is bad
        wfo = wfo.strip()

# =============================================================================
# INFILE NAMING?  -- MODIFY
# =============================================================================
        partInFile = indir + wfo + "/" + wfo + "_"
        print("Searching: ", wfo)#, flush=True)
        sys.stdout.flush()
        partInFile = os.path.join(indir,wfo)
# =============================================================================
#  Iterate through the file for each product (years)   --- KEEP
# =============================================================================   
        #Loops through all the years specified for that particular file
        for iYear in range(int(FSW_SEARCH['START_YEAR']),int(FSW_SEARCH['END_YEAR'])+1,1):
            sYear = str(iYear); sYear1 = str(iYear+1)
            fname = wfo + "_"+str(iYear)+extension
            data_file = os.path.join(partInFile,fname)

            ## OPEN/READ DATA FILE WITH ARCHIVED AFD
            if os.path.isfile(data_file) == True:
                readData = open(data_file,'r').readlines()
                readData = [rD.upper() for rD in readData]
    # =============================================================================
    #        DOES THIS ACTUALLY SPEED IT UP OR SLOW IT DOWN????          
    # =============================================================================
                # IF ANY OF THE KEYWORDS ARE IN THAT WFO/YEAR FILE THEN CONTINUE/ELSE SKIP
                rCheck = open(data_file,'r').read() # READ IN FILE
                rCheck = rCheck.replace("\n", " ") # FLATTEN AND REMOVE LINE SEPARATORS
                rCheck = rCheck.upper() ## MAKE EVERYTHING UPPER CASE
                if FSW_SEARCH['And_Or'] == False:
                    ## NEW - ANY SEARCH
                    if any(keyword in rCheck for keyword in inputKey):
                        for idy in range(len(inputKey)):
                            keywordCounts[idy] += rCheck.count(inputKey[idy]) # Could be done faster by doing once per forecast file
                        testQuickCountFcst += rCheck.count(wfo)
                    else:
                        testQuickCountFcst += rCheck.count(wfo)
                        #print("No Possible Search Matches in: ",wfo+"_"+sYear+" . Skipping...")#, flush=True)
                        #sys.stdout.flush()
                        continue
                ### IF ALL OF THE KEYWORDS ARE IN THAT WFO/YEAR FILE THEN CONTINUE/ELSE SKIP
                elif FSW_SEARCH['And_Or'] == True:
                    if all(keyword in rCheck for keyword in inputKey):
                        for idy in range(len(inputKey)):
                            keywordCounts[idy] += rCheck.count(inputKey[idy]) # Could be done faster by doing once per forecast file
                        testQuickCountFcst += rCheck.count(wfo)
                    else:
                        testQuickCountFcst += rCheck.count(wfo)
                        #print("No Possible Search Matches in: ",wfo+"_"+sYear+" . Skipping...")#, flush=True)
                        #sys.stdout.flush()
                        continue
    # =============================================================================
    # 
    # =============================================================================
    
            else:
                print("MISSING FILE: ", data_file)#, flush=True)
                sys.stdout.flush()
                continue

# =============================================================================
#  Iterate through the file
# =============================================================================   
            ## Initialize Parameters // Setup blank lists to hold data
            findTime = []; findString = []; foundHEADER=False; foundDDHHMM=False;
            hourTime = []; keyWord = []; timeZone = []; countZ = 0;
            iHolder = 0 ; iHolderLast = 0; cFalse = falseList[:] #copy of the flaselist

            ## Index through the file [ line by line ]
            ## But stop before the last line of the file so we don't get a fatal error. 
            ## also the end of the files should have the least important information (forecaster names)
            length_file = len(readData)

            #Search Each row in the file            
            for idx in range(length_file-1):
                
                #print("Count: ", countZ, "||", countTry-reset_count, reset_count, prodsIssued, wfo, iYear, idx)#, flush=True) 

                #if the row is empty skip
                if readData[idx] == "\n":         continue
                # If the keyword can't be in the row because it isn't long enough

# =============================================================================
# FIND FILE HEADERS FOR EACH PRODUCT ISSUED - Find Date/Time Info On Next Line. Store Index.
# =============================================================================
                #511 
                #AXNT20 KNHC 010534   <=== DDHHMM in UTC/Z.. should be the last part...
                #TWDAT 
                elif wfo == readData[idx].strip():
                    #FOUND TOP BUT NOT DATE/LINE
                    if foundDDHHMM == True and foundHEADER == False:
                        if reset_count != prodsIssued:
                            reset_count -=1
                            #We already know to present... There is 100% data availability in SWPC products.. But some formatting complicates this step
                            if wfo in Option.ALL_SWPC:
                                if "SPACE WEATHER MESSAGE CODE:" in readData[idx]:
                                    pass
                                elif ":PRODUCT: DAILY SPACE WEATHER SUMMARY AND FORCAST DAYDSF.TXT" in readData[idx]:
                                    pass
                                elif "SWXALTK" in readData[idx]:
                                    pass
                                else:
                                    print("FINDER: NO FORECAST HEADER WAS FOUND, ", wfo, iYear, "Current: ", idx, "Last Good: ", iHolder)#, flush=True)
                                    sys.stdout.flush()
                            else:
                                if abs(idx-iHolder) < 8:
                                    #print("FINDER: DUPLICATE AWIPS ID IN HEADER", wfo, iYear, "Current: ", idx, "Last Good: ", iHolder)#, flush=True)
                                    sys.stdout.flush()
                                    countTry -= 1
                                    continue
                                print("FINDER: NO FORECAST HEADER WAS FOUND, ", wfo, iYear, "Current: ", idx, "Last Good: ", iHolder)#, flush=True)
                                sys.stdout.flush()

                    # FOUND THE TOP.... TRY TO FIND THE TIME DDHHMM
                    foundDDHHMM = False
                    try:
                        if len(re.sub('[^0-9 ]+', '', readData[idx-1])) >= 6:
                            DDHHMM = (re.sub('[^0-9 ]+', '', readData[idx-1])).split()[-1]
                        elif len(re.sub('[^0-9 ]+', '', readData[idx-2])) >= 6:
                            DDHHMM = (re.sub('[^0-9 ]+', '', readData[idx-2])).split()[-1]
                    except:
                        DDHHMM = ""
                        
                    if len(DDHHMM) == 6 and DDHHMM.isdigit():
                        countTry +=1
                        reset_count +=1
                        #lastfile_str = wfo+"_"+sYear
                        #lastIdxFnd = idx
                        foundDDHHMM = True
                        foundHEADER = False
                        
                    ## IF IT IS SPC TAKE SPECIAL APPROACH TO FIND DATE/TIME... BOTTOM OF THE FORECAST
                    if wfo in Option.ALL_SPC and "SWO" in wfo and foundHEADER == False:
                        if iYear <= 2003:
                            ADMIN_MAX_ALLOW = 150
                            text = readData[idx:idx+ADMIN_MAX_ALLOW]
                            DATETIME_STRING, isSuccess = covertSPC(wfo, iYear, text, DDHHMM)
                            if isSuccess == True:
                                iHolder = -999
                                prodsIssued +=1; 
                                cFalse = falseList[:];
                                foundHEADER = True
                            else:
                                countZ +=1;
                                continue
                                
                                

                if len(readData[idx]) < shortestword:                  continue
                elif any(TIPTOP in readData[idx] for TIPTOP in total_forecast) and foundHEADER == False:    
                    #DUPLICATE FOR TESTING ONLY....  
                    if any(TOP2 in readData[idx] for TOP2 in ID_TOP_FCST2) and ("ISSUED BY" not in readData[idx]):
                        #check and see if the expected year is in the next row
                        if sYear in readData[idx+1]:                iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        # if next line says product was issued by someone else 
                        elif "ISSUED BY" in readData[idx+1]:
                            #Check one line further for correct year
                            if sYear in readData[idx+2]:            iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                            #see if the next line down is empty and go the the next
                            elif len(readData[idx+2].strip()) < 4:
                                # Does the next line have the year if not then skip
                                if sYear in readData[idx+3]:        iHolder=idx + 3; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                                elif sYear1 in readData[idx+3]:     iHolder=idx + 3; prodsIssued +=1; cFalse = falseList[:];  foundHEADER = True 
                            #if the next line has the next year because it's at the end/start of year
                            elif sYear1 in readData[idx+2]:         iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:]; foundHEADER = True
                        #if the next line has the next year because it's at the end/start of year
                        elif sYear1 in readData[idx+1]:             iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        elif str(iYear) in readData[idx]:       iHolder = idx; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        ## REQUIRED FOR PSR 1999 - December.. 2 upside down backwards ? were causing problems
                        elif '\n' == readData[idx+1]:
                             #If it's the expected year
                             if sYear in readData[idx+2]:           iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             #If the next year
                             elif sYear1 in readData[idx+2]:        iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             elif str(iYear-1) in readData[idx+2]:       iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             elif str(iYear-1) in readData[idx]:       iHolder = idx; prodsIssued +=1; cFalse = falseList[:]; foundHEADER = True        
                        elif "CENTRAL PACIFIC HURRICANE CENTER" in readData[idx]:
                            if "HONOLULU HI" in readData[idx+1]:
                                #If it's the expected year
                                if sYear in readData[idx+2]:           iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                                #If the next year
                                elif sYear1 in readData[idx+2]:        iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];   foundHEADER = True  
                            else:
                                 #If it's the expected year
                                 if sYear in readData[idx+1]:           iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                                 #If the next year
                                 elif sYear1 in readData[idx+1]:        iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                                 elif str(iYear-1) in readData[idx+1]:       iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        elif str(iYear-1) in readData[idx+1]:       iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];     foundHEADER = True     
                        ### EXCEPTION BECAUSE AUTOFORMATTING OF PRODUCT DIDN'T ACCOUNT FOR THE TURN OF THE CENTURY - NWS END
                        elif wfo == "PMDTHR" and "CLIMATE PREDICTION CENTER NCEP" in readData[idx]:
                            if sYear in readData[idx+1]: iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True;
                            elif str(iYear-100) in readData[idx+1]: iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True;
                            elif str(iYear-100) in readData[idx+2]: iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True;
                            elif sYear in readData[idx+2]: iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True;
                        elif readData[idx+1].strip() == "":
                             if sYear in readData[idx+2]:           iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             elif sYear1 in readData[idx+2]:        iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                    elif any(TOP in readData[idx] for TOP in ID_TOP_FCST) and ("FORECASTER" not in readData[idx]):
                        #check and see if the expected year is in the next row
                        if sYear in readData[idx+1]:                iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        # if next line says product was issued by someone else 
                        elif "ISSUED BY" in readData[idx+1]:
                            #Check one line further for correct year
                            if sYear in readData[idx+2]:            iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                            #see if the next line down is empty and go the the next
                            elif len(readData[idx+2].strip()) < 4:
                                # Does the next line have the year if not then skip
                                if sYear in readData[idx+3]:        iHolder=idx + 3; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                                elif sYear1 in readData[idx+3]:     iHolder=idx + 3; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                            #if the next line has the next year because it's at the end/start of year
                            elif sYear1 in readData[idx+2]:         iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        #if the next line has the next year because it's at the end/start of year
                        elif sYear1 in readData[idx+1]:             iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        ## REQUIRED FOR PSR 1999 - December.. 2 upside down backwards ? were causing problems
                        elif '\n' == readData[idx+1]:
                             #If it's the expected year
                             if sYear in readData[idx+2]:           iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             #If the next year
                             elif sYear1 in readData[idx+2]:        iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             elif sYear in readData[idx]:           iHolder = idx; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        elif str(iYear-1) in readData[idx+1]:       iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        elif str(iYear) in readData[idx]:       iHolder = idx; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True  
                        #FOR OFFNT PRODUCTS
                        elif "ANALYSIS AND FORECAST BRANCH" in readData[idx+1]: 
                            #Check one line further for correct year
                            if sYear in readData[idx+2]:            iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                            #see if the next line down is empty and go the the next
                            elif len(readData[idx+2].strip()) < 4:
                                # Does the next line have the year if not then skip
                                if sYear in readData[idx+3]:        iHolder=idx + 3; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                                elif sYear1 in readData[idx+3]:     iHolder=idx + 3; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                            #if the next line has the next year because it's at the end/start of year
                            elif sYear1 in readData[idx+2]:         iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True  
                        elif readData[idx+1].strip() == "":
                             if sYear in readData[idx+2]:           iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                             elif sYear1 in readData[idx+2]:        iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                            
                    elif any(TOP3 in readData[idx] for TOP3 in ID_TOP_FCST3):
                        ## FOR OLD NCEP PRODUCTS - WORKING
                        if"NCEP PROGNOSTIC DISCUSSION FROM" in readData[idx]:
                            prodsIssued +=1
                            iHolder = idx                       
                            cFalse = falseList[:];
                            foundHEADER = True
                        ## FOR OLD NCEP HI PRODUCTS - WORKING
                        elif "HPC FORECAST VALID" in readData[idx]: 
                            prodsIssued +=1
                            iHolder = idx       
                            cFalse = falseList[:];
                            foundHEADER = True
                        ## ALL CASES FOR SWPC
                        elif 'SPACE WEATHER MESSAGE CODE' in readData[idx]:
                            if "SERIAL NUMBER" in readData[idx+1]:
                                if 'ISSUED BY' in readData[idx+2]:  
                                    if sYear in readData[idx+2]:        iHolder = idx +2; cFalse = falseList[:];prodsIssued +=1;foundHEADER = True
                                    elif sYear1 in readData[idx+2]:        iHolder = idx +2; cFalse = falseList[:];prodsIssued +=1;foundHEADER = True
                                elif 'ISSUE TIME' in readData[idx+2]:  
                                    if sYear in readData[idx+2]:        iHolder = idx +2; cFalse = falseList[:];prodsIssued +=1;foundHEADER = True
                                    elif sYear1 in readData[idx+2]:        iHolder = idx +2; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True
                            else:
                                if 'ISSUED BY' in readData[idx]:  
                                    if sYear in readData[idx+1]:    iHolder =idx+1; cFalse = falseList[:]; prodsIssued +=1;foundHEADER = True
                                    elif sYear1 in readData[idx+1]:    iHolder =idx+1; cFalse = falseList[:]; prodsIssued +=1;foundHEADER = True
                        elif ':ISSUED:' in readData[idx]:
                            if sYear in readData[idx]:        iHolder = idx; cFalse = falseList[:];prodsIssued +=1; foundHEADER = True
                            elif sYear1 in readData[idx]:        iHolder = idx; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True                 
                        #LSRNY products
                        #LSRNY4 - 2009 did not have a date/time
                        elif "TROOP" in readData[idx+1]:
                            if len(readData[idx+2].strip()) < 6:
                                if sYear in readData[idx+3]:        iHolder = idx+3; cFalse = falseList[:];prodsIssued +=1; foundHEADER = True
                                elif sYear1 in readData[idx+3]:        iHolder = idx+3; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True 
                            if sYear in readData[idx+2]:        iHolder = idx+2; cFalse = falseList[:];prodsIssued +=1; foundHEADER = True
                            elif sYear1 in readData[idx+2]:        iHolder = idx+2; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True 
                        elif len(readData[idx+1].strip()) < 6:
                            if "TROOP" in readData[idx+2]:
                                 if sYear in readData[idx+3]:        iHolder = idx+3; cFalse = falseList[:];prodsIssued +=1; foundHEADER = True
                                 elif sYear1 in readData[idx+3]:        iHolder = idx+3; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True             
                                 elif len(readData[idx+3].strip()) < 6:
                                     if sYear in readData[idx+4]:        iHolder = idx+4; cFalse = falseList[:];prodsIssued +=1; foundHEADER = True
                                     elif sYear1 in readData[idx+4]:        iHolder = idx+4; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True                                

                        elif sYear in readData[idx+1]:         iHolder = idx+1; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        elif sYear1 in readData[idx+1]:        iHolder = idx+1; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True   
                        elif sYear in readData[idx+2]:         iHolder = idx+2; prodsIssued +=1; cFalse = falseList[:];foundHEADER = True
                        elif sYear1 in readData[idx+2]:        iHolder = idx+2; cFalse = falseList[:];prodsIssued +=1;   foundHEADER = True    

                # CHECK TO SEE IF KEYWORDS ARE USED IN THE LINE     -  GET DATE/TIME     
                # =============================================================================
                # FIND KEYWORDS: If any keyword is in the row + partial row and not at before the first date/time (header)
                if any(keyword in readData[idx]+readData[idx+1][:biggestword] for keyword in inputKey) and foundHEADER ==True:
                    #print(wfo,"  ",sYear,"  ",iHolder, readData[iHolder], flush=True)
                    #Figure out which word was used.....
                    for idy in range(len(inputKey)):
                        #ACCURATE COUNT OF THE KEYWORDS
                        if inputKey[idy] in readData[idx]:
                            #keywordCounts[idy] += readData[idx].count(inputKey[idy]) # Could be done faster by doing once per forecast file
                            linestring = readData[idx]
                        # THIS MEANS THE WORD IS SPLIT BETWEEN TWO LINES.... If it goes to ELSE that means it's only in the next row....skip
                        elif inputKey[idy] not in readData[idx+1][:biggestword] and inputKey[idy] not in readData[idx]:
                            linestring = readData[idx]+readData[idx+1][:biggestword]
                        else: #Get it on the next iteration
                            continue
                        if inputKey[idy] in linestring: 
                            if iHolder == -999:
                                if "UTC" in DATETIME_STRING:
                                    tmp = DATETIME_STRING.split("UTC")
                                    date = tmp[0].strip() #TIME
                                    time = tmp[1].strip() #DATE
                                    tz_array = "UTC"
                                    
                                    last_tz = tz_array
                                    cFalse[idy] = True
                                    hourTime.append(date)         #hourTime gets the hour/minute
                                    findTime.append(time)         #findTime gets the date string
                                    timeZone.append(tz_array)
                                    keyWord.append(inputKey[idy])
                                    findString.append(readData[idx])
                                    keywordCountsFINAL[idy] += 1   ## COUNT NUMBER OF TIMES EACH KEYWORD THAT IS FORECASTED

                                else:
                                    date, time, tz_array = timezone_finder_SPC(DATETIME_STRING,last_tz)
                                    last_tz = tz_array
                                    cFalse[idy] = True
                                    ## Save to arrays for each station being searched
                                    # This is a little confusing but hourTime get's the date YEAR, MONTH, DAY, WEEKDAY
                                    # findTime gets the hour, minute, AM/PM, timezone
                                    hourTime.append(date)         #hourTime gets the hour/minute
                                    findTime.append(time)         #findTime gets the date string
                                    timeZone.append(tz_array)
                                    keyWord.append(inputKey[idy])
                                    findString.append(readData[idx])
                                    keywordCountsFINAL[idy] += 1   ## COUNT NUMBER OF TIMES EACH KEYWORD THAT IS FORECASTED
                            else:
                                ## DUPLICATE KEYWORD IN FORECAST - skip- don't add to the list
                                if readData[iHolder] == readData[iHolderLast]:
                                    ## SAME FORECAST BUT KEYWORD WAS ALREADY USED
                                    if iHolder == iHolderLast and cFalse[idy] == True:
                                        continue
                                    ## DUPLICATE FORECAST ISSUED ... Or had to use the previous (more recent) forecast - skip- don't add to the list
                                    elif iHolder != iHolderLast:
                                        countDupFcst +=1
                                        iHolderLast= iHolder
                                        continue
                                
                                ## USE THE AUTO GENERATED DDHHMM
                                if foundDDHHMM == True:
                                    try:
                                        #try:
                                        date, time, tz_array = timezone_finder(readData,iHolder,last_tz)
                                        #except:
                                        #    print("TZ WARNING: ", readData[iHolder-2:iHolder+2])#, flush = True)
                                        #    sys.stdout.flush()
                                        iHolderLast = iHolder
                                        last_tz = tz_array
                                        cFalse[idy] = True
                                        
                                        ## Save to arrays for each station being searched
                                        # This is a little confusing but hourTime get's the date YEAR, MONTH, DAY, WEEKDAY
                                        # findTime gets the hour, minute, AM/PM, timezone
                                        hourTime.append(DDHHMM)         #hourTime gets the hour/minute
                                        findTime.append(time)         #findTime gets the date string
                                        timeZone.append(tz_array)
                                        keyWord.append(inputKey[idy])
                                        findString.append(readData[idx])
                                        keywordCountsFINAL[idy] += 1   ## COUNT NUMBER OF TIMES EACH KEYWORD THAT IS FORECASTED
        
                                    except:
                                        # COULD NOT FIND DATE/TIME and the time zone.... use the last known forecast
                                        try:
                                            date, time, tz_array = timezone_finder(readData,iHolderLast,last_tz)
                                            #print("TZ WARNING: ", readData[iHolder-2:iHolder+2])#, flush = True)
                                            #    sys.stdout.flush()
                                            ###isAssume = True
                                            iHolderLast = iHolderLast
                                            last_tz = tz_array
                                            cFalse[idy] = True
        
                                            ## Save to arrays for each station being searched
                                            # This is a little confusing but hourTime get's the date YEAR, MONTH, DAY, WEEKDAY
                                            # findTime gets the hour, minute, AM/PM, timezone
                                            hourTime.append(DDHHMM)         #hourTime gets the hour/minute
                                            findTime.append(time)         #findTime gets the date string
                                            timeZone.append(tz_array)
                                            keyWord.append(inputKey[idy])
                                            findString.append(readData[idx])
                                            keywordCountsFINAL[idy] += 1   ## COUNT NUMBER OF TIMES EACH KEYWORD IS FORECASTED
        
                                        except:
                                            countBad +=1
                                            continue   # LEAVE GO TO THE NEXT IN THE LOOP
                                
                                
                                ## DDHHMM WAS NEVER FOUND SO USE THE TIME PROVIDED IN THE TEXT
                                else:   
                                    if iHolder == 0:
                                        countBad +=1
                                        continue
                                    date, time, tz_array = timezone_finder(readData,iHolder,last_tz)
                                    iHolderLast = iHolder
                                    last_tz = tz_array
                                    cFalse[idy] = True
                                    
                                    ## Save to arrays for each station being searched
                                    # This is a little confusing but hourTime get's the date YEAR, MONTH, DAY, WEEKDAY
                                    # findTime gets the hour, minute, AM/PM, timezone
                                    hourTime.append(date)         #hourTime gets the hour/minute
                                    findTime.append(time)         #findTime gets the date string
                                    timeZone.append(tz_array)
                                    keyWord.append(inputKey[idy])
                                    findString.append(readData[idx])
                                    keywordCountsFINAL[idy] += 1   ## COUNT NUMBER OF TIMES EACH KEYWORD THAT IS FORECASTED
                               
                                
# END OF FILE NO HEADER FOUND... MUST BE WITHIN FOR LOOP @ END...
# =============================================================================      
                if idx == (length_file-1) and foundHEADER == False and foundDDHHMM == True:
                    reset_count -=1
                    print("FINDER: NO FORECAST HEADER WAS FOUND (EOF), ", wfo, iYear, "Current: ", idx, "Last Good: ", iHolder)#, flush=True)   
                    sys.stdout.flush()
                
# TIME HANDLE FUNCTIONS FOR ALL CASES FOUND   - AFTER EACH FILE... OUTSIDE FOR LOOP
# =============================================================================
            ## If time was found and stored 
            if len(findTime) != 0:  
                # REFORMAT TIME STRING TO BE SORTABLE AND NUMERICAL
                #TODO SPC2003 is getting lost here
                TimesFound,keyFound = wfo_rft_time(findTime,hourTime,wfo,keyWord,FSW_SEARCH['Make_Assumptions'],iYear,timeZone)

                if len(TimesFound) != 0:
                    #sort the date time objects created above
                    final_reformat_2_str,final_Key_Found = sort_time(TimesFound,keyFound,FSW_SEARCH['ByForecast_ByDay'])
                    
                    #  IF ALL SEARCH WORDS FOUND IN THAT FORECAST
                    if FSW_SEARCH['And_Or'] == True:
                        trimFKF = []
                        trimFR2S = []
                        for ijk2 in range(len(final_reformat_2_str)):
                            if len(final_Key_Found[ijk2]) == len(inputKey):
                                trimFR2S.append(final_reformat_2_str[ijk2])
                                trimFKF.append(final_Key_Found[ijk2])

                        #Append to master list(s)
                        masterList.extend(trimFR2S)  
                        masterList2.extend([wfo] * len(trimFR2S))
                        masterList3.extend(trimFKF)

                    #  IF ANY SEARCH WORDS FOUND IN THAT FORECAST
                    else:
                        ## Append to master list(s)
                        masterList.extend(final_reformat_2_str)  
                        masterList2.extend([wfo] * len(final_reformat_2_str))
                        masterList3.extend(final_Key_Found)
            ## Calculate Algorithm Statistics
            no_dups += len(list(set(findString)))
            
    
# PRINT STATISTICS - SEARCH = DONE...
# =============================================================================   
    print("End Search")#, flush=True)
    sys.stdout.flush()
    endT = t.time()
    eTime = endT-startT
    
    num_days = len(masterList) # NUMBER OF CASES/DAYS
    total_mentions = sum(keywordCountsFINAL) # TOTAL MENTIONS: SUM OF FORECAST FREQUENCY OF EACH KEYWORD

    #Print Algorithm Statistics to the console
    algor_stats(FSW_SEARCH['STATION_LIST'],inputKey, total_mentions,num_days,no_dups,FSW_SEARCH['START_YEAR'],FSW_SEARCH['END_YEAR'],countBad)
    sys.stdout.flush()
    print("Estimated Forecasts: ",testQuickCountFcst)
    print("Total Forecasts Attempted: ",countTry)#, flush=True)
    print("Total Forecasts Searched: ",prodsIssued)#, flush=True)
    print("\nIndeterminable Forecasts", countTry-prodsIssued)#, flush=True)  
    print("Duplicate Forecasts Issued", countDupFcst)#, flush=True)  
    experimental = testQuickCountFcst  - ((testQuickCountFcst - reset_count) - (countTry-prodsIssued))
    print("\nExpected Forecasts (Experimental): ", experimental)
    sys.stdout.flush()

# WRITE OUTPUT
# =============================================================================   
    outputfileOUT = write_output_file(outputfile, inputKey, FSW_SEARCH['STATION_LIST'], FSW_SEARCH['START_YEAR'],FSW_SEARCH['END_YEAR'], eTime, FSW_SEARCH['isGrep'], FSW_SEARCH['And_Or'],\
                 FSW_SEARCH['ByForecast_ByDay'],FSW_SEARCH['Make_Assumptions'],keywordCounts,keywordCountsFINAL,num_days,prodsIssued,\
                 countDupFcst,total_mentions,no_dups,countBad,masterList,masterList2,masterList3)
   
    print("\nMain-Search Elapsed Time:",endT-startT)#, flush=True)
    print()#, flush=True)
    sys.stdout.flush()

    return outputfileOUT