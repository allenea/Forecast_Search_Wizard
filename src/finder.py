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
import sys
import os
import time as t
import re
# MY PACKAGES
from src.tz_finder import timezone_finder
from src.read_time import wfo_rft_time
from src.sort_time import sort_time
from src.print_search_info import algor_stats
from src.write_output import write_output_file
from src.Pre2003_SPC import covertSPC, timezone_finder_SPC
from src.find_header import find_header, find_header_nws
from search_options.search_options import Option

NWS = 'NATIONAL WEATHER SERVICE'
STR_SWPC = ":PRODUCT: DAILY SPACE WEATHER SUMMARY AND FORCAST DAYDSF.TXT"
TOTAL_FORECAST = ['NATIONAL WEATHER SERVICE', 'NATIONAL HURRICANE CENTER',\
                  'STORM PREDICTION CENTER', 'TROPICAL PREDICTION CENTER',\
                 'NWS WEATHER PREDICTION CENTER', 'NWS CLIMATE PREDICTION CENTER',\
                 'OCEAN PREDICTION CENTER', 'NCEP PROGNOSTIC DISCUSSION FROM',\
                 'CENTRAL PACIFIC HURRICANE CENTER', 'HYDROMETEOROLOGICAL PREDICTION CENTER',\
                 'MARINE PREDICTION CENTER', 'SPACE WEATHER MESSAGE CODE', ':ISSUED:',\
                 'HPC FORECAST VALID', 'ALASKA FORECAST DISCUSSION',\
                 'SOUTHCENTRAL AND SOUTHWEST ALASKA', "IN SPC BACKUP CAPACITY",\
                 "NATIONAL CENTERS FOR ENVIRONMENTAL PREDICTION",\
                 "CLIMATE PREDICTION CENTER NCEP",\
                 "NEW YORK STATEWIDE POLICE INFORMATION NETWORK", "HIGH SEAS FORECAST"]

def AFD_finder(FSW_SEARCH):
    """ Primary searching function to identify keywords and starts of forecasts...

    FSW_SEARCH Parameters:
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
    start_time = t.time()
    print("Start Time: " + t.ctime())
    sys.stdout.flush()
    ## SET SOME DIRECTORY PATHS
    extension = ".txt"           # INPUT AND OUTPUT FILE THE SAME FORMAT
    indir = FSW_SEARCH['TEXT_DATA_PATH']
    outdir = FSW_SEARCH['OUTPUT_PATH']
    inputKey = FSW_SEARCH['KEYWORD_LIST']
    shortestword = len(min(inputKey, key=len)) # skip rows len shorter
    biggestword = len(max(inputKey, key=len))
    upper = str.upper
    replace = str.replace
    strip = str.strip
    count_frequency_str = str.count
    len_inputkey = len(inputKey)
    testQuickCountFcst = 0
# =============================================================================
#  OUTFILE NAMING ...    --- REMOVE AND MODIFY FOR WEBSITE
# =============================================================================
    str_len = str(len(FSW_SEARCH['STATION_LIST']))

    if int(str_len) == 1:
        outfile = FSW_SEARCH['RUN_START_TIME'] +"_"+ replace(inputKey[0], " ", "_")+\
                "_" + FSW_SEARCH['STATION_LIST'][0]+\
                "_"+str(FSW_SEARCH['START_YEAR'])+"_"+str(FSW_SEARCH['END_YEAR']) +\
                "_Forecast_Search_Wizard" + extension
    else:
        outfile = FSW_SEARCH['RUN_START_TIME'] +"_"+ replace(inputKey[0], " ", "_")+\
                "_" + str_len + "_" + str(FSW_SEARCH['START_YEAR']) + "_" +\
                str(FSW_SEARCH['END_YEAR']) + "_Forecast_Search_Wizard" + extension

    outfile = replace(outfile, "__", "_")
    print("Outfile: "+outfile)
    print()
    sys.stdout.flush()

# =============================================================================
# Sets variables and constants --- KEEP
# =============================================================================
    ## FINAL OUTPUT FILE AND DIRECTORY LOCATION
    outputfile = os.path.join(outdir, outfile)
    ## Initialize Parameters and local variables
    master_list = []
    extend_ml1 = master_list.extend
    master_list2 = []
    extend_ml2 = master_list2.extend
    master_list3 = []
    extend_ml3 = master_list3.extend

    no_dups = 0
    prods_issued = 0

    #TODO VERIFY REMOVAL -- CURRENTLY WAS UNUSED
    #countBad (int): Something went wrong when a keyword was found (time zone or date/time)
    #count_bad = 0

    countDupFcst = 0
    countTry = 0
    reset_count = 0
    #lastIdxFnd = 0
    #lastfile_str = ""

    # total = total_mentions
    # good = can be assertained by subtracting TZ Errors from Total Mentions
    keywordCounts = [0] * len_inputkey   # USED TO COUNT KEYWORD FREQUENCY
    keywordCountsFINAL = [0] * len_inputkey    # USED TO COUNT FORECAST FREQUENCY
                # frequency of search criteria met - not individul keyword counts
    falseList = [False] * len_inputkey  # PERMENANT... ONLY MAKE A COPY OF THIS LATER

# =============================================================================
# ITERATE THROUGH PRODUCTS TO BE SEARCHED   -- KEEP
# =============================================================================
    print("Begin Search")
    sys.stdout.flush()

    #Loops through all the files it's been told to loop through
    for wfo in FSW_SEARCH['STATION_LIST']:
        # Reset for each issuing branch
        last_tz = ""  # Uses last sucessful timezone if current is bad
        wfo = strip(wfo)
# =============================================================================
# INFILE NAMING?  -- MODIFY
# =============================================================================
        partInFile = indir + wfo + "/" + wfo + "_"
        print("Searching: ", wfo)
        sys.stdout.flush()
        partInFile = os.path.join(indir, wfo)
# =============================================================================
# Iterate through the file for each product (years)   --- KEEP
# =============================================================================
        #Loops through all the years specified for that particular file
        for iYear in range(int(FSW_SEARCH['START_YEAR']), int(FSW_SEARCH['END_YEAR'])+1, 1):

            fname = wfo + "_"+str(iYear)+extension
            data_file = os.path.join(partInFile, fname)

            ## OPEN/READ DATA FILE WITH ARCHIVED AFD
            if os.path.isfile(data_file):
    # =============================================================================
    #        ONLY INCREASES PERFORMANCE WHEN "GOOD SEARCHES" are made.
    #           Searching for something like "THE" will slow it a little bit...
    # =============================================================================
                # IF ANY OF THE KEYWORDS ARE IN THAT WFO/YEAR FILE THEN CONTINUE/ELSE SKIP
                read_check = open(data_file, 'r').read() # READ IN FILE
                read_check = replace(read_check, "\n", " ") # FLATTEN AND REMOVE LINE SEPARATORS
                read_check = upper(read_check) ## MAKE EVERYTHING UPPER CASE


                if not FSW_SEARCH['And_Or']:
                    ## NEW - ANY SEARCH
                    if any(keyword in read_check for keyword in inputKey):
                        for idy in range(len_inputkey):
                            keywordCounts[idy] += count_frequency_str(read_check, inputKey[idy])
                            # Could be done faster by doing once per forecast file
                        testQuickCountFcst += count_frequency_str(read_check, wfo)
                    else:
                        #NO Search Criteria MATCHES
                        testQuickCountFcst += count_frequency_str(read_check, wfo)
                        continue

                ### IF ALL OF THE KEYWORDS ARE IN THAT WFO/YEAR FILE THEN CONTINUE/ELSE SKIP
                elif FSW_SEARCH['And_Or']:
                    if all(keyword in read_check for keyword in inputKey):
                        for idy in range(len_inputkey):
                            keywordCounts[idy] += count_frequency_str(read_check, inputKey[idy])
                            # Could be done faster by doing once per forecast file
                        testQuickCountFcst += count_frequency_str(read_check, wfo)
                    else:
                        #Adding -- in case say 4 of 5 keywords are found
                            # -- we still get a count on those 4.
                        for idy in range(len_inputkey):
                            keywordCounts[idy] += count_frequency_str(read_check, inputKey[idy])
                        #NO Search Criteria MATCHES
                        testQuickCountFcst += count_frequency_str(read_check, wfo)
                        continue
# =============================================================================
#
# =============================================================================
            else:
                print("MISSING FILE: ", data_file)
                sys.stdout.flush()
                continue
# =============================================================================
#        ACTUALLY READ THE DATA. THIS FILE IS WORTH READING
# =============================================================================
            readData = open(data_file, 'r').readlines()
            readData = list(map(str.upper, readData))#[upper(rD) for rD in readData]
# =============================================================================
#  Iterate through the file
# =============================================================================
            ## Initialize Parameters // Setup blank lists to hold data
            findTime = []
            append_findTime = findTime.append
            findString = []
            append_findString = findString.append
            hourTime = []
            append_hourTime = hourTime.append
            keyWord = []
            append_keyWord = keyWord.append
            timeZone = []
            append_timeZone = timeZone.append
            DDHHMM_lst = []
            append_DDHHMM_lst = DDHHMM_lst.append

            found_header = False
            foundDDHHMM = False
            countZ = 0
            idx_holder = 0
            holder_last = 0
            copy_false = falseList[:] #copy of the flaselist

            ## Index through the file [ line by line ]
            ## But stop before the last line of the file so we don't get a fatal error.
            ## There should be nothing meaningful there anyways: forecaster names or blank line.
            length_file = len(readData)

            #Search Each row in the file
            for idx in range(length_file-1):

                #print("Count: ", countZ, "||", countTry-reset_count,\
                    #reset_count, prods_issued, wfo, iYear, idx)

                #if the row is empty skip
                if readData[idx] == "\n":
                    continue
# =============================================================================
# FIND FILE HEADERS FOR EACH PRODUCT ISSUED - Find Date/Time Info On Next Line. Store Index.
# =============================================================================
                #511
                #AXNT20 KNHC 010534   <==  = DDHHMM in UTC/Z.. should be the last part...
                #TWDAT
                elif wfo == strip(readData[idx]):
                    #FOUND TOP BUT NOT DATE/LINE
                    if foundDDHHMM and not found_header:
                        #TODO ONCE VERIFIED REMOVE AND UNTAB THIS BLOCK
                        if reset_count != prods_issued:
                            reset_count -= 1
                            #We already know to present...
                            #There is 100% data availability in SWPC products..
                            # But some formatting complicates this step
                            if wfo in Option.ALL_SWPC:
                                if "SPACE WEATHER MESSAGE CODE:" in readData[idx]:
                                    pass
                                elif STR_SWPC in readData[idx]:
                                    pass
                                elif "SWXALTK" in readData[idx]:
                                    pass
                                else:
                                    print("FINDER: NO FORECAST HEADER WAS FOUND, ", wfo,\
                                          iYear, "Current: ",\
                                          idx, "Last Good: ", idx_holder)
                                    sys.stdout.flush()
                            else:
                                if abs(idx-idx_holder) < 8:
                                    #print("FINDER: DUPLICATE AWIPS ID IN HEADER",\
                                    #    wfo, iYear, "Current: ",\
                                    #    idx, "Last Good: ", idx_holder)
                                    sys.stdout.flush()
                                    countTry -= 1
                                    continue
                                print("FINDER: NO FORECAST HEADER WAS FOUND, ", wfo,\
                                      iYear, "Current: ", idx,\
                                      "Last Good: ", idx_holder)
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
                        countTry += 1
                        reset_count += 1
                        #lastfile_str = wfo+"_"+sYear
                        #lastIdxFnd = idx
                        foundDDHHMM = True
                        found_header = False


                    ## IF IT IS SPC TAKE SPECIAL APPROACH TO FIND DATE/TIME. BOTTOM OF THE FORECAST
                    if wfo in Option.ALL_SPC and "SWO" in wfo and not found_header:
                        if iYear <= 2003:
                            #ADMIN_MAX_ALLOW and len(text) should be the same...
                            # check in the convertSPC function
                            ADMIN_MAX_ALLOW = 150
                            text = readData[idx:idx+ADMIN_MAX_ALLOW]
                            DATETIME_STRING, isSuccess = covertSPC(iYear, text, DDHHMM)#(wfo,
                            if isSuccess:
                                idx_holder = -999
                                prods_issued += 1
                                copy_false = falseList[:]
                                found_header = True
                            else:
                                countZ += 1
                                continue

                #keyword can't be in the row because it isn't long enough
                if len(readData[idx]) < shortestword:
                    continue
                elif found_header:
                    pass
                #SPENDS LIKE 41 MINUTES HERE
                elif not found_header:
                    if NWS in readData[idx] and "ISSUED BY" not in readData[idx]:
                        idx_h, found = find_header_nws(readData, idx, iYear)
                        if found:
                            found_header = True
                            idx_holder = idx_h
                            copy_false = falseList[:]
                            prods_issued += 1
                    elif any(TIPTOP in readData[idx] for TIPTOP in TOTAL_FORECAST):
                        idx_h, found = find_header(readData, idx, iYear, wfo)
                        if found:
                            found_header = True
                            idx_holder = idx_h
                            copy_false = falseList[:]
                            prods_issued += 1

                # FIND KEYWORDS: CHECK TO SEE IF KEYWORDS ARE USED IN THE LINE
                # =============================================================================
                long_string = readData[idx]+readData[idx+1][:biggestword]
                if found_header and any(keyword in long_string for keyword in inputKey):
                    #print(wfo, "  ", sYear, "  ", idx_holder, readData[idx_holder])
                    #Figure out which word was used.....
                    for idy in range(len_inputkey):
                        if inputKey[idy] in readData[idx]:
                            linestring = readData[idx]
                        # THIS MEANS THE WORD IS SPLIT BETWEEN TWO LINES....
                        # If it goes to ELSE that means it's only in the next row....skip
                        elif inputKey[idy] not in readData[idx+1][:biggestword] and\
                                                inputKey[idy] not in readData[idx]:
                            linestring = long_string
                        else: #Get it on the next iteration
                            continue
                        if inputKey[idy] in linestring:
                            if idx_holder == -999:
                                if "UTC" in DATETIME_STRING:

                                    tmp = DATETIME_STRING.split("UTC")
                                    date = strip(tmp[0]) #TIME
                                    time = strip(tmp[1]) #DATE
                                    tz_array = "UTC"

                                    last_tz = tz_array
                                    copy_false[idy] = True

                                    append_hourTime(date)         #hourTime gets the hour/minute
                                    append_DDHHMM_lst(DDHHMM)
                                    append_findTime(time)         #findTime gets the date string
                                    append_timeZone(tz_array)
                                    append_keyWord(inputKey[idy])
                                    append_findString(readData[idx])
                                    keywordCountsFINAL[idy] += 1
                                    ## COUNT NUMBER OF TIMES EACH SEARCH CRITERIA IS FOUND

                                else:
                                    date, time, tz_array = timezone_finder_SPC(DATETIME_STRING,\
                                                                               last_tz)

                                    last_tz = tz_array
                                    copy_false[idy] = True

                                    append_hourTime(date)         #hourTime gets the hour/minute
                                    append_DDHHMM_lst(DDHHMM)
                                    append_findTime(time)         #findTime gets the date string
                                    append_timeZone(tz_array)
                                    append_keyWord(inputKey[idy])
                                    append_findString(readData[idx])
                                    keywordCountsFINAL[idy] += 1
                                    ## COUNT NUMBER OF TIMES EACH SEARCH CRITERIA IS FOUND
                            else:
                                ## DUPLICATE KEYWORD IN FORECAST - skip- don't add to the list
                                if readData[idx_holder] == readData[holder_last]:
                                    #TODO WHAT IF BOTH ARE 0?
                                    ## SAME FORECAST BUT KEYWORD WAS ALREADY USED
                                    if idx_holder == holder_last and copy_false[idy]:
                                        continue
                                    ## DUPLICATE FORECAST ISSUED ...
                                    #  Or had to use the previous (more recent)
                                    # forecast - skip- don't add to the list
                                    elif idx_holder != holder_last:
                                        countDupFcst += 1
                                        holder_last = idx_holder
                                        continue

                                ## USE THE AUTO GENERATED DDHHMM
                                if foundDDHHMM:
                                    try:
                                        date, time, tz_array = timezone_finder(readData,\
                                                                               idx_holder,\
                                                                               last_tz)
                                        holder_last = idx_holder
                                        ### IF "" "" "" CHECK IT OUT

                                    except:
                                        print("TZ: TIMEZONE WARNING ", idx_holder,\
                                              readData[idx_holder-1:idx_holder+1])
                                        #count_bad += 1
                                        sys.stdout.flush()
                                        continue   # LEAVE GO TO THE NEXT IN THE LOOP

                                    last_tz = tz_array
                                    copy_false[idy] = True

                                    append_hourTime(date)         #hourTime gets the hour/minute
                                    append_DDHHMM_lst(DDHHMM)
                                    append_findTime(time)         #findTime gets the date string
                                    append_timeZone(tz_array)
                                    append_keyWord(inputKey[idy])
                                    append_findString(readData[idx])
                                    keywordCountsFINAL[idy] += 1
                                    ## COUNT NUMBER OF TIMES EACH SEARCH CRITERIA IS FOUND

                                ## DDHHMM WAS NEVER FOUND SO USE THE TIME PROVIDED IN THE TEXT
                                else:
                                    if idx_holder == 0:
                                        print("FINDER: idx_holder == 0. DDHHMM could not be found.")
                                        #count_bad += 1
                                        continue

                                    date, time, tz_array = timezone_finder(readData,\
                                                                           idx_holder,\
                                                                           last_tz)
                                    holder_last = idx_holder
                                    last_tz = tz_array
                                    copy_false[idy] = True

                                    append_hourTime(date)         #hourTime gets the hour/minute
                                    append_DDHHMM_lst("999999")
                                    append_findTime(time)         #findTime gets the date string
                                    append_timeZone(tz_array)
                                    append_keyWord(inputKey[idy])
                                    append_findString(readData[idx])
                                    keywordCountsFINAL[idy] += 1
                                    ## COUNT NUMBER OF TIMES EACH SEARCH CRITERIA IS FOUND


# END OF FILE NO HEADER FOUND... MUST BE WITHIN FOR LOOP @ END...
# =============================================================================
                if idx == (length_file-1) and not found_header and foundDDHHMM:
                    reset_count -= 1
                    print("FINDER: NO FORECAST HEADER WAS FOUND (EOF), ", wfo, iYear, "Current: ",\
                          idx, "Last Good: ", idx_holder)
                    sys.stdout.flush()

# TIME HANDLE FUNCTIONS FOR ALL CASES FOUND   - AFTER EACH FILE... OUTSIDE FOR LOOP
# =============================================================================
            ## If time was found and stored
            if len(findTime) != 0:
                # REFORMAT TIME STRING TO BE SORTABLE AND NUMERICAL
                TimesFound, key_found = wfo_rft_time(findTime, hourTime, DDHHMM_lst,\
                                                    wfo, keyWord, FSW_SEARCH['Make_Assumptions'],\
                                                    iYear, timeZone)
                if len(TimesFound) != 0:
                    #sort the date time objects created above
                    final_reformat_2_str, final_key_found = sort_time(TimesFound,\
                                                        key_found, FSW_SEARCH['ByForecast_ByDay'])

                    #  IF ALL SEARCH WORDS FOUND IN THAT FORECAST
                    if FSW_SEARCH['And_Or']:
                        trimFKF = []
                        append_trimFKF = trimFKF.append
                        trimFR2S = []
                        append_trimFR2S = trimFR2S.append
                        for ijk2 in range(len(final_reformat_2_str)):
                            if len(final_key_found[ijk2]) == len_inputkey:
                                append_trimFR2S(final_reformat_2_str[ijk2])
                                append_trimFKF(final_key_found[ijk2])

                        #Append to master list(s)
                        extend_ml1(trimFR2S)
                        extend_ml2([wfo] * len(trimFR2S))
                        extend_ml3(trimFKF)

                    #  IF ANY SEARCH WORDS FOUND IN THAT FORECAST
                    else:
                        ## Append to master list(s)
                        extend_ml1(final_reformat_2_str)
                        extend_ml2([wfo] * len(final_reformat_2_str))
                        extend_ml3(final_key_found)
            ## Calculate Algorithm Statistics
            no_dups += len(list(set(findString)))


# PRINT STATISTICS - SEARCH = DONE...
# =============================================================================
    print("End Search")
    sys.stdout.flush()
    elapsed_time = t.time() - start_time

    num_days = len(master_list) # NUMBER OF CASES/DAYS
    total_mentions = sum(keywordCountsFINAL)
    # TOTAL MENTIONS: SUM OF FORECAST FREQUENCY OF EACH KEYWORD

    #Print Algorithm Statistics to the console
    algor_stats(FSW_SEARCH, inputKey, total_mentions, num_days, no_dups)#, count_bad)
    sys.stdout.flush()
    print("Estimated Forecasts: ", testQuickCountFcst)
    print("Total Forecasts Attempted: ", countTry)
    print("Total Forecasts Searched: ", prods_issued)
    print("\nIndeterminable Forecasts", countTry-prods_issued)
    print("Duplicate Forecasts Issued", countDupFcst)
    #guesstimate (AWIPS ID) - (guesstimate-AWIPS ID -
    # actual (which subtracts when next ID is found before the next header)) -
    # (total attempted - the actual forecast products definitively ID'd)) FAILED TO SEARCH
    experimental = testQuickCountFcst  - ((testQuickCountFcst - reset_count) -\
                                          (countTry-prods_issued))
    print("\nExpected Total Forecasts (Experimental): ", experimental)
    sys.stdout.flush()

# WRITE OUTPUT
# =============================================================================
    outputfileOUT = write_output_file(outputfile, FSW_SEARCH, elapsed_time,\
                 keywordCounts, keywordCountsFINAL, num_days, prods_issued, \
                 countDupFcst, total_mentions, no_dups, experimental, master_list,\
                 master_list2, master_list3)#, count_bad)

    print("\nMain-Search Elapsed Time:", elapsed_time)
    print()
    sys.stdout.flush()

    return outputfileOUT
