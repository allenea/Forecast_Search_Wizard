"""Copyright (C) 2018-2019 Eric Allen - All Rights Reserved"""
# CREATE YOUR OWN TOOL - Used for analyzing FSW code
#IMPORTS
import glob
import os

BACK_DIR = os.path.abspath("./..")
PY_FILES = glob.glob(BACK_DIR+"/src/*.py")
PY_FILES.sort()

COUNT = 0
for p in PY_FILES:
    #Remove .py extension
    short_pf = p.split("/")[-1][:-3]
    file1 = open(p, 'r').readlines()
    for i, file_row in enumerate(file1):
        if "print" in file_row:#.upper(): #and "#" != (file_row.strip())[0]:# and "(" in file_row:
            #if (file_row.strip())[0] == "#":
            #    continue
            print("File: ", short_pf, "  Row: ", i+1, " Line ", file_row.strip())
            COUNT += 1


"""
OUTPUT:
    
File:  Pre2003_SPC   Row:  15  Line  from __future__ import print_function
File:  check_everything   Row:  15  Line  from __future__ import print_function
File:  check_vars   Row:  15  Line  from __future__ import print_function
File:  check_vars   Row:  89  Line  print("Empty List of Words")
File:  check_vars   Row:  127  Line  print("SETUP FAILURE: List of keywords contains something other than strings...")
File:  check_vars   Row:  141  Line  print("SETUP FAILURE: List of products contains something other than strings...")
File:  check_vars   Row:  160  Line  print("SETUP FAILURE: Invalid end year. Must not be higher than current year...")
File:  check_vars   Row:  161  Line  print("Redo with correct year range\n")
File:  check_vars   Row:  167  Line  print("SETUP FAILURE: Invalid start year... Valid options: 1996 - Current Year...")
File:  check_vars   Row:  169  Line  print("Start year out of range [1996 - Current Year]. Check your TEXT_DATA"+\
File:  check_vars   Row:  172  Line  print("1996 thru 2000: Very sparse and incomplete, selectively backfilled as"+\
File:  check_vars   Row:  175  Line  print("Also note that product source IDs are possibly different back then"+\
File:  check_vars   Row:  178  Line  print("Known holes exist at: 29 Oct-1 Nov 1998, 24-27 Dec 1998, 25-28 Jul"+\
File:  check_vars   Row:  181  Line  print("2001 thru 2007: More consistent archives, but still likely missing"+\
File:  check_vars   Row:  184  Line  print("2008 thru now: Very good data coverage and higher fidelity archiving.")
File:  check_vars   Row:  186  Line  print("\n\nIf your dataset does indeed exists prior to 1996. Then modify the"+\
File:  check_vars   Row:  189  Line  print("Otherwise redo with correct year range\n")
File:  check_vars   Row:  212  Line  print(inputKeyNew[ydx], keepKey)
File:  check_vars   Row:  214  Line  print("REDUNDANT: REMOVING - ", inputKeyNew[ydx], "FROM THE LIST OF KEYWORDS...")
File:  check_vars   Row:  220  Line  print("REDUNDANT: REMOVING - ", inputKeyNew[ydx], "FROM THE LIST OF KEYWORDS...")
File:  convert_time   Row:  15  Line  from __future__ import print_function
File:  convert_time   Row:  24  Line  #     print(tz)
File:  convert_time   Row:  49  Line  print("CT: "+wfo+" Convert_Time Failure on ", month, "-", day, "-", year, " @ ",\
File:  differentiate   Row:  19  Line  from __future__ import print_function
File:  driver   Row:  15  Line  from __future__ import print_function
File:  driver   Row:  24  Line  from src.print_search_info import final_message
File:  driver   Row:  75  Line  print("Program Failed To Run due to (6-hour) TimeoutException..."+\
File:  driver   Row:  77  Line  print("If second run yields the same problem. Try narrowing your search"+\
File:  driver   Row:  79  Line  print("--- %s seconds ---\n\n" % (time.time() - start_time))
File:  driver   Row:  87  Line  print("Program Failed on UnicodeEncodeError... Possibly caused by a corrupt file.")
File:  driver   Row:  88  Line  print("--- %s seconds ---\n\n" % (time.time() - start_time))
File:  driver   Row:  96  Line  print("Program Failed To Run To Completion..."+\
File:  driver   Row:  99  Line  print("--- %s seconds ---\n\n" % (time.time() - start_time))
File:  driver   Row:  110  Line  print("--- %s seconds ---\n\n" % (time.time() - start_time))
File:  find_header   Row:  15  Line  from __future__ import print_function
File:  finder   Row:  15  Line  from __future__ import print_function
File:  finder   Row:  24  Line  from src.print_search_info import algor_stats
File:  finder   Row:  62  Line  print("Start Time: " + t.ctime())
File:  finder   Row:  94  Line  print("Outfile: "+outfile)
File:  finder   Row:  95  Line  print()
File:  finder   Row:  129  Line  print("Begin Search")
File:  finder   Row:  141  Line  print("Searching: ", wfo)
File:  finder   Row:  192  Line  print("MISSING FILE: ", data_file)
File:  finder   Row:  232  Line  #print("Count: ", countZ, "||", countTry-reset_count,\
File:  finder   Row:  261  Line  print("FINDER: NO FORECAST HEADER WAS FOUND, ", wfo,\
File:  finder   Row:  268  Line  #print("FINDER: DUPLICATE AWIPS ID IN HEADER",\
File:  finder   Row:  274  Line  print("FINDER: NO FORECAST HEADER WAS FOUND, ", wfo,\
File:  finder   Row:  339  Line  #print(wfo, "  ", sYear, "  ", idx_holder, readData[idx_holder])
File:  finder   Row:  412  Line  print("TZ: TIMEZONE WARNING", idx_holder,\
File:  finder   Row:  433  Line  print("FINDER: idx_holder == 0. DDHHMM could not be found.")
File:  finder   Row:  458  Line  print("FINDER: NO FORECAST HEADER WAS FOUND (EOF), ", wfo, iYear, "Current: ",\
File:  finder   Row:  503  Line  print("End Search")
File:  finder   Row:  515  Line  print("Estimated Forecasts: ", testQuickCountFcst)
File:  finder   Row:  516  Line  print("Total Forecasts Attempted: ", countTry)
File:  finder   Row:  517  Line  print("Total Forecasts Searched: ", prods_issued)
File:  finder   Row:  518  Line  print("\nIndeterminable Forecasts", countTry-prods_issued)
File:  finder   Row:  519  Line  print("Duplicate Forecasts Issued", countDupFcst)
File:  finder   Row:  522  Line  print("\nExpected Forecasts (Experimental): ", experimental)
File:  finder   Row:  536  Line  print("\nMain-Search Elapsed Time:", elapsed_time)
File:  finder   Row:  537  Line  print()
File:  print_search_info   Row:  19  Line  from __future__ import print_function
File:  print_search_info   Row:  23  Line  def print_info(usr_vars):
File:  print_search_info   Row:  27  Line  print("SEARCH INFORMATION")
File:  print_search_info   Row:  28  Line  print("------------------------")
File:  print_search_info   Row:  29  Line  print("\nAPPLICATION DIRECTORY: ", usr_vars['APPLICATION_ROOT_DIRECTORY'])
File:  print_search_info   Row:  30  Line  print("\nTEXT DATA PATH: ", usr_vars['TEXT_DATA_PATH'])
File:  print_search_info   Row:  31  Line  print("\nWARNING DIRECTORY: ", usr_vars['WARNING_PATH'])
File:  print_search_info   Row:  32  Line  print("\nOUTPUT DIRECTORY: ", usr_vars['OUTPUT_PATH'])
File:  print_search_info   Row:  33  Line  print("\nPRODUCTS BEING SEARCHED: ", usr_vars['STATION_LIST'])
File:  print_search_info   Row:  34  Line  print("\nLIST OF KEYWORDS: ", usr_vars['KEYWORD_LIST'])
File:  print_search_info   Row:  35  Line  print("\nSTART YEAR: ", usr_vars['START_YEAR'])
File:  print_search_info   Row:  36  Line  print("END YEAR: ", usr_vars['END_YEAR'])
File:  print_search_info   Row:  37  Line  print("\nSearch By And (True) or Or (False): ", usr_vars['And_Or'])
File:  print_search_info   Row:  38  Line  print("Search By Forecast (True) or Day (False): ", usr_vars['ByForecast_ByDay'])
File:  print_search_info   Row:  39  Line  print("Is Grep Style Search: ", usr_vars['isGrep'])
File:  print_search_info   Row:  40  Line  print("Make Basic Assumptions: ", usr_vars['Make_Assumptions'])
File:  print_search_info   Row:  41  Line  print("\n\nThe Forecast Search Wizard was developed by Eric Allen",\
File:  print_search_info   Row:  49  Line  print("\n--------ALGORITHM STATISTICS---------")
File:  print_search_info   Row:  50  Line  print("Years Searched: "+str(start)+" - "+str(end))
File:  print_search_info   Row:  52  Line  print("Products Searched:")
File:  print_search_info   Row:  56  Line  print("\t", station_split_list[eric])
File:  print_search_info   Row:  58  Line  print("\nKeyword:  ", mainword)
File:  print_search_info   Row:  59  Line  print("\nTotal Cases Found: ", num_days)
File:  print_search_info   Row:  60  Line  print("\nTotal Mentions: ", total_mentions)
File:  print_search_info   Row:  61  Line  print("Unique Mentions: ", no_dups)
File:  print_search_info   Row:  62  Line  print("--------END ALGORITHM STATISTICS------\n")
File:  print_search_info   Row:  67  Line  """"This is the final message that prints once the program has run to completion.""""
File:  print_search_info   Row:  68  Line  print("****** A Note From Eric Allen ******")
File:  print_search_info   Row:  69  Line  print("- Remember that sometimes words are used when not referring to a forecasted"+\
File:  print_search_info   Row:  71  Line  print("- Validate the search by checking the forecast, surface analysis, or observations.")
File:  print_search_info   Row:  72  Line  print("- As great as NWS/NCEP forecasters are, sometimes forecasts busts and events"+\
File:  print_search_info   Row:  74  Line  print("- Hopefully a future version will include the ability to search-by-section to"+\
File:  print_search_info   Row:  76  Line  print("- Try again with different variations and misspellings of keyword, and take a"+\
File:  print_search_info   Row:  78  Line  print("\nThank You")
File:  print_search_info   Row:  79  Line  print("************************************\n")
File:  print_search_info   Row:  86  Line  print("\nThank you to Daryl Herzmann and the Iowa Env. Mesonet for the assistance and data.")
File:  print_search_info   Row:  87  Line  print("All Iowa Mesonet Data should be used for educational purposes only.\n")
File:  print_search_info   Row:  88  Line  print("WGET routine from https://bitbucket.org/techtonik/python-wget/src\n")
File:  print_search_info   Row:  94  Line  print("\n##  You are using the Forecast Search Wizard: a NOAA Text Product Keyword Finder. ")
File:  print_search_info   Row:  95  Line  print("\n##  This is an independently developed program by Eric Allen - All Rights Reserved.")
File:  print_search_info   Row:  96  Line  print("##  Please cite: 'Eric Allen. Forecast Search Wizard: A Tool to Search NOAA Text-Forecasts."+\
File:  read_time   Row:  15  Line  from __future__ import print_function
File:  read_time   Row:  28  Line  information. If not possible then try the alternative method or print warnings.
File:  read_time   Row:  68  Line  print("TP: ", wfo, " - ERR NO MONTH FOUND... FATAL.  ", "??-", int_day,\
File:  read_time   Row:  76  Line  print("TP: ", wfo, \
File:  read_time   Row:  118  Line  print("TP: ", wfo, " - Time Information Could Not Be Found. "+\
File:  read_time   Row:  126  Line  print("TP: ", wfo, " - Time Information Could Not Be Found. "+\
File:  read_time   Row:  175  Line  #print("TP: minor discrepancy - : ", final_time_string.strftime(FMT_STRING),\
File:  read_time   Row:  184  Line  print("TP: MAJOR DISCREPANCY - Using: ",\
File:  read_time   Row:  215  Line  print("TP: Unknown - Exception Thrown. Continuing without the time in question.",\
File:  setup   Row:  15  Line  from __future__ import print_function
File:  setup   Row:  19  Line  from src.print_search_info import print_info
File:  setup   Row:  34  Line  print("FAILURE IN SETUP...INVALID PRODUCT LIST SEARCH OPTION. Exiting....")
File:  setup   Row:  35  Line  print("Setup.py is designed to verify that only valid search criteria"+\
File:  setup   Row:  53  Line  print("FAILURE IN SETUP...INVALID INPUT KEYWORDS. Exiting....")
File:  setup   Row:  54  Line  print("Setup.py is designed to verify that only valid search criteria is"+\
File:  setup   Row:  61  Line  print_info(FSW_SEARCH)
File:  setup   Row:  64  Line  print("FAILURE IN SETUP...AT LEAST ONE USER DEFINED VARIABLE CAUSED A NoneType EXCEPTION."+\
File:  setup   Row:  66  Line  print("Setup.py is designed to verify that only valid search criteria is passed "+\
File:  setup   Row:  173  Line  print("PROJECT MUST BE RUN FROM PACKAGED FORECAST_SEARCH_WIZARD FOLDER. Exiting...")
File:  setup   Row:  178  Line  print("THE ./TEXT_DATA/ FOLDER COULD NOT BE FOUND. Creating... Exiting...")
File:  setup   Row:  179  Line  print("Make sure you have downloaded the data with DOWNLOAD_DATA.py")
File:  sort_time   Row:  19  Line  from __future__ import print_function
File:  time_functions   Row:  15  Line  from __future__ import print_function
File:  trimwarnings   Row:  15  Line  from __future__ import print_function
File:  tz_finder   Row:  15  Line  from __future__ import print_function
File:  write_output   Row:  15  Line  from __future__ import print_function
File:  write_output   Row:  116  Line  #     print("THIS HAS NOT BEEN IMPLEMENTED YET!!")

"""