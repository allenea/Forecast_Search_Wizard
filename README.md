# Forecast Search Wizard

**Author:** [Eric Allen](mailto:allenea@udel.edu)

**Version:** 1.0.0

**LICENSE:** GNU GPLv3

**DOI:** https://doi.org/10.5281/zenodo.3542411

(Draft)


Testimonial: "Even with my nominal python and linux background I was able to run your program without issue.” - NWS Employee

Note From Eric: Today, this tool is being used at various level of the National Weather Services and in different parts of the Weather Enterprise. Less than one year from its release (V1), I have seen this tool used in a variety of different ways. This week at the National Weather Association conference I saw the first project that used/cited the Forecast Search Wizard. It's being used in ways I did not imagine. The possibilities are endless. This tool will continue to grow with the support of the community. (9/16/2020)

## Overview
The Forecast Search Wizard makes it easier than ever before to analyze archived NOAA text products to obtain valuable information. Thanks to the hard working individuals at the National Weather Service and National Centers for Environmental Prediction there is a large record of very detailed weather forecasts from across the country. This program, the Forecast Search Wizard, allows users to search for keywords in NOAA/NWS text products (e.g., Area Forecast Discussions, Local Storm Reports, Watches/Warnings, etc.) to identify the occurrence of case studies, particular weather events, or other specific information. This one-of-a-kind tool will not only save the researcher time, but it will also improve the depth and quality of research by opening a door to a new source of data in the weather enterprise.
 
The Forecast Search Wizard is a robust and efficient program, but more importantly it is user friendly. The only programs that need to be executed for the Forecast Search Wizard to run are located in the RUN_ME directory. These files are the DOWNLOAD_DATA.py and [FSW_NAMELIST.py](https://github.com/allenea/Forecast_Search_Wizard/blob/Forecast_Search_Wizard_beta/RUN_ME/FSW_NAMELIST.py) which is a namelist file. Each of these files are constructed so that minimal programming knowledge is required to use this program. These files are modeled after the [WRF](https://esrl.noaa.gov/gsd/wrfportal/namelist_input_options.html) namelist files. This enables users to construct their own searches without worrying about breaking the program. In fact, the user never touches the Forecast Search Wizard. An instance of your search is checked and validated before being sent to the Forecast Search Wizard. This enables to user to run multiple searches at once. _Note: The DOWNLOAD_DATA.py does not have these validation checks._

The Forecast Search Wizard is not case sensitive. However, please consider that these forecasts are written by humans. Humans do make mistakes from time to time. Consider accounting for abbreviations or contractions, typos, or slang for a robust search. In the folder Documentation there is a list of [Common NWS Contractions](https://www.weather.gov/phi/contractions). The [AMS Glossary](http://glossary.ametsoc.org/wiki/Main_Page) is another place you might consider. Additionally, there is information about [Preset Search Options](https://github.com/allenea/Forecast_Search_Wizard/blob/Forecast_Search_Wizard_beta/Documentation/Frequently_Used_NWS_Contractions.txt) and AWIPS/WFO ID's in this [folder](https://github.com/allenea/Forecast_Search_Wizard/tree/Forecast_Search_Wizard_beta/Documentation).

The Forecast Search Wizard was designed to identify case studies and specific weather information. It should not be taken as fact. It should be used to identify possible case studies. Always verify with observations or surface analysis. For example, if you are searching "Hurricane" you might get results referencing Hurricane Preparedness Week.

Information about namelist options, assumptions, tracking print statements and error codes can be found below.

This work was not funded and done independently and in my free time. If you would like to share or contribute code or *tools* to analyze or improve the Forecast Search Wizard please contact me at [email](mailto:allenea@udel.edu). If you create a program to read and parse the outputs and would like to share, then please contact me.

## Installation

    - git clone https://github.com/allenea/Forecast_Search_Wizard.git
 
 Try (depending on your system... Tell it where to build):
 
    - python setup.py install
    
    - python setup.py install --user

    - python setup.py build install --prefix $HOME/.local (University of Delaware HPC Users)
 
 
 **SUPPORTED VERSIONS**: I hope to support Python 2.6+ and Python 3.0+. I have personally tested a few versions between 2.6 and 3.7.4. Please let me know if you're having any problems.
 
 **REQUIRED LIBRARIES**: python-dateutil, pytz>=2019.1, wget>=3.2
 
 *Written in Python3.6 and Python3.7*
 
 
 ## USING THE FORECAST SEARCH WIZARD
 
 ### DOWNLOAD_DATA.py
 
_Execute in 2 steps. Internet connection is required for this step._
 
1. Edit DOWNLOAD_DATA.py. The user can configure this file to download the desired search dataset. This dataset is required by the Forecast Search Wizard. There are 6 parameters that you can set in the **DOWNLOAD_DATA** program. You will see the _Variable Name_, _Data Type_, _Default Value_, and some _Valid Options_ for each parameter (below) to guide you. Simply execute this file once properly configured. 
 
Currently the [Iowa Environmental Mesonet text archive](https://mesonet.agron.iastate.edu/wx/afos/list.phtml) is being used. All IEM data should be used for educational purposes only. IEM states "Please do not depend on this page for operational decision making, errors can and do occur with data processing, data reception and any other error possible with Internet communications." The Forecast Search Wizard only depends on the information in the written forecasts. The Forecast Search Wizard is not dependent upon sucessful archival in the IEM database however these instances may be flagged as assumptions in the Forecast Search Wizard. Other than that, all data retrieved by the Forecast Search Wizard is from the text products themselves. Currently, IEM is the only supported source of text data. I would be happy to work with NCEI to make their archives more accessible to the public.
 
   #### PARAMETERS ####
   
   **1. Download_Data** :: Boolean value
       
          > download_data = True
          
        Valid Options:
       
                 True (Download Data)
                 False (Do Not Download)

   **2. Get_Latest_Year** :: Boolean value
           
          > Get_Latest_Year = False
          
        Valid Options:
       
                 True (Download Latest Year)
                 False (Do Not Download)
                                      
   **3. Remove_Empty** :: Boolean value 
       
          > Remove_Empty = True
          
        Valid Options:
       
                 True (Remove Empty Forecast Products)
                 False (Keep All Products)

   **4. start_year** :: integer value
       
          > start_year = int(1996)

        Valid Options: Any year between 1996 and Present
      
                 1996 - 2019
           
   **5. end_year** :: integer value
                 
          > end_year = int(time.ctime()[-4:])

        Valid Options: Any year between 1996 and Present but later than the start_year
      
                 1996 - 2019

   **6. MASTER_LIST** ::  a list of strings or by selecting a **preset configuration**.
       
          > MASTER_LIST = ["AFDLWX", "AFDPHI"]

        Valid Options: Valid forecast products as strings or select from the preset search options (537 options) or create your own.
         
                 MASTER_LIST = Option.MASTER_LIST
                 MASTER_LIST = Option.ALL
                 MASTER_LIST = Option.MY_SEARCH
                 MASTER_LIST = Option.ALL_NCEP
                 MASTER_LIST = Option.ALL_LSR
                 MASTER_LIST = ["AFDCAR", "AFDGYX", "AFDBOX", "AFDPHI", "AFDALY", "AFDBGM",\
                                "AFDBUF", "AFDOKX", "AFDMHX", "AFDILM", "AFDRAH", "AFDILN",\
                                "AFDCLE", "AFDPBZ", "AFDCTP", "AFDCHS", "AFDCAE", "AFDGSP",\
                                "AFDBTV", "AFDLWX", "AFDRNK", "AFDAKQ", "AFDRLX"]
                                               
 2. Execute this file once DOWNLOAD_DATA has been properly configured. This step can take a few minutes to a few hours depending on the number and size of the forecasts as well as network connectivity.
      
          > python DOWNLOAD_DATA.py


**DOWNLOAD OUTPUT:** A file that looks like *Data_Download_VerboseTue_Nov_12_195850_2019.out* will be stored in the RUN_ME folder. This is for your records to know what was downloaded and where that data can be found. All FSW data should be stored in _Forecast_Search_Wizard/TEXT_DATA/_. Otherwise you will need to set the new path. This is not recommended. Please keep the file structure otherwise things might break. This file also explains everything that happened when you tried to download the dataset.

**DATA STORAGE:** The Forecast Search Wizard does require you to have available space to store the forecasts. I am able to download ~23 years of data for ~580 forecast products (>10,000,000 forecasts) with a storage requirement of less than 32GB. This is an extreme scenario. If you are downloading only Area Forecast Discussions for a single offices, then you might be able to expect that to take up 300 - 500 MB. Some forecasts are longer or more frequent and therefore take up more space.

**Preset Configurations:** You can create your own list, choose or modify existing options found in *~/search_options/search_options.py* by declaring *Option.<OPTION_NAME>*. By default the search_options module is imported for RUN_ME programs (DOWNLOAD_DATA and FSW_NAMELIST).

   **General Example:**
   ```
   > from search_options.search_options import Option
   > MASTER_LIST = Option.ALL
   ```
   **Example When Combining Preset Search Options:** The following example will allow you to search or download ALL options except all SPC forecasts. The search or download will proceed alphabetically.
   ```
   > from search_options.search_options import Option
   > lst = list(set(Option.ALL) - set(Option.ALL_SPC))
   > lst.sort()
   > forecast_product_list = lst # FOR FSW_NAMELIST.py
   > MASTER_LIST = lst # FOR DOWNLOAD_DATA.py
   ```
*WGET routine from https://bitbucket.org/techtonik/python-wget/src*
     
     

### FSW_NAMELIST.py
  
 1. Edit FSW_NAMELIST.py to your search criteria. .... This is the main program which you will be using once you have your data and everything installed.
 
       #### PARAMETERS ####

       **1. input_word_list** :: a list of strings. It is not case sensitive nor is it sensitive to spaces and characters. For robustness, try some possible common mispellings.
       
          > input_word_list = ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES",\
                       "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES",\
                       "SEA BREAZES"] 
                       
        Valid Options:  ANYTHING! FOLLOW THE STRUCTURE ABOVE. LIST OF STRINGS!

                 input_word_list = ["dorian", "alabama"] #Too Soon?
                 input_word_list = ["cold air damming", "cad"] #Too Soon?

       **2. forecast_product_list** :: a list of strings or by selecting a **preset configuration** (see above).
       
          > forecast_product_list = ["AFDPHI"]

        Valid Options: Valid forecast products as strings or select from the preset search options (537 options) or create your own.
         
                 forecast_product_list = Option.MASTER_LIST
                 forecast_product_list = Option.ALL
                 forecast_product_list = Option.MY_SEARCH
                 forecast_product_list = Option.ALL_NCEP
                 forecast_product_list = Option.ALL_LSR
                 forecast_product_list = ["AFDCAR", "AFDGYX", "AFDBOX", "AFDPHI", "AFDALY", "AFDBGM",\
                                "AFDBUF", "AFDOKX", "AFDMHX", "AFDILM", "AFDRAH", "AFDILN",\
                                "AFDCLE", "AFDPBZ", "AFDCTP", "AFDCHS", "AFDCAE", "AFDGSP",\
                                "AFDBTV", "AFDLWX", "AFDRNK", "AFDAKQ", "AFDRLX"]
       **3. start_year** :: integer value
       
                 > start_year = int(1996)
                 
        Valid Options: Any year between 1996 and Present. This is a hard limit. Internal controls prevent other options.
      
                 1996 - 2019
           
       **4. end_year** :: integer value
                 
                 > end_year = int(time.ctime()[-4:])

       Valid Options: Any year between 1996 and Present but later than the start_year. Internal controls prevent other options.
      
                 1996 - 2019

       **5. isAnd** :: Boolean value 
       
          > isAnd = True
          
        Valid Options:
       
                 True (Search for All of the words)
                 False (Search for ANY of the words)

       
       **6. byForecast** :: Boolean value
       
          > byForecast = True
          
        Valid Options:
       
                 True (Search by forecast)
                 False (Search by day)

       **7. isGrep** :: Boolean value
           
          > isGrep = True
          
        Valid Options:
       
                 True (GREP-Style Search)
                              Example:
                                     Input: ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES",
                                             "SEABREEZE","SEABREAZES", "SEABREAZE", "SEA BREEZES",
                                                 "SEA BREAZES"]
                                     Actual: ["SEA BREEZE", "SEA BREAZE", "SEABREEZE", "SEABREAZE"]
                 False (Search for whole word or phrase)
                               Example:
                                   Input: ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES",
                                           "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES",
                                               "SEA BREAZES"]
                                   Actual: [" SEA BREEZE ", " SEA BREAZE ", " SEABREEZES ", " SEABREEZE ",
                                            " SEABREAZES ", " SEABREAZE ", " SEA BREEZES ", " SEA BREAZES "]                                                      
       **8. make_assumptions** :: Boolean value 
       
          > make_assumptions = True
          
        Valid Options: I advise that you enable assumptions. Any assumptions that are made are indicated in the output with a # or *<star>*. 
       
                                      True (make likely assumptions)
                                      False (no assumptions)

       **8. debug_flag** :: Boolean value. 
           
           > debug_flag = False
           
        If you are having issues try switching the debut flag to True. No output will be saved. If there is something wrong with the program which I expect in the beginning there might be a few hiccups. Either email me (email is in the overview section) or create an issue here and I will look into what might be going wrong. 
       
                                             
 2. Execute this file once it has been properly configured. This step can take a few seconds to an hour depending on the scope of your search. The time also depends on the system/computer it is being run on. This program likely could be easily parallelized for runs on HPCC. Ask for details (I personally haven't done it but I know how I would try to do it). There is an internal alarm that kills the program if the search exceeds 6 hours. If this happens either you are doing something wrong or something internally has gone horribly wrong.
      
              python FSW_NAMELIST.py
              

**OUTPUTS OF THE FORECAST SEARCH WIZARD:** Check the outputs when they are done. You will get one output located in the **FSW_WARN** folder with information about the run, any trouble it had, some statistics about the run, etc. The second output if the Forecast Search Wizard ran successfully will be located in the **FSW_OUTPUT** folder. This file will provide you with information about the search and the results of the search. In the future tools will become available to help analyze this data. Until then you are responsible for the analysis of the Forecast Search Wizard results.



## Assumptions 
- If month is missing from Issuing Date then the forecast CANNOT be resolved.

- If year cannot be found in the Issuing Date, then assume the year the forecast was stored in the IEM database was correct. Other cases default to the year found in the forecast. If December or January then there are exceptions to that rule. If year does not match database +/- 1 for December or January, then mark as an assumption.

- Use ddhhmm found in the WMO Header for day and time. Check it against the day found in the Issuing Date. Adjust the month or year accordingly if it goes from one month or day to another. If day cannot be resolved then try to use day from ddhhmm. Check to make sure that works or raise assumption.

- If ddhhmm cannot be found, then use Issuing Time. Assumptions may have been made on hour, year, AM or PM. If this is the case, then a warning will be issued at this time.

- If AM and PM found in the Issuing Time, then mark as an assumption, but use whichever is found first. Indicate the assumption if ddhhmm is not available. If ddhhmm is available this will not matter. 

- If timezone cannot be found, use the most frequently used timezone for that year in that forecast product

- Check Everything takes all known information and checks to make sure everything checks out. If it does not and it can be fixed without triggering an assumption, then use the new date and time information. Whenever available ddhhmm is the default day, hour, and minute. But month can change if for example day in Issuing Date was 31 and the day in the ddhhmm was 1. If the day ends up being larger than possible for the month. Try moving the day to the next month. Mark as an assumption.

- If Check Everything indicated that an assumption likely occured in the function, then mark as an assumption if and only if the Issuing Date triggered an assumption to either day or year. Use ddhhmm for day, hour and minute. If ddhhmm cannot be found then if there was an assumption indicated when resolving Issuing Time then mark as an assumption.

**Major assumptions are marked with a ( * ) symbol.** All of these above are "major assumptions". Additionally if the difference in time between ddhhmm and the Issuing Time is greater than 36 hours.


**Minor assumptions are indicated with a ( # ).** A minor assumption occurs if the day from the Issuing Date and ddhhmm do not equal each other. Since the Check Everything makes adjustments this can often be the case. However **ddhhmm is the Truth**. But if the difference in time between ddhhmm and the issuing time is less than 36 hours and greater than 2 hours, then mark as a minor assumption.

I've had this time check thing working better but it does slow the program down a bit. At the end of the day it is redundant. If enough people want this feature of redundant checks, then I could consider making this better in the future. For now if there is a large difference just note it. There are many times when people forget what day it is and are off slightly. But this would impact less than 1% of all forecasts. Possibly even as small as 0.3%.

## Error Codes Index
The following is a list of warnings you might find in the warnings file associated with your search. The purpose of the warnings program is to enable transparency.

File:  setup   Row:  34  - FAILURE IN SETUP...INVALID PRODUCT LIST SEARCH OPTION. Exiting....

File:  setup   Row:  53  - FAILURE IN SETUP...INVALID INPUT KEYWORDS. Exiting....

File:  setup   Row:  64/65  - FAILURE IN SETUP...AT LEAST ONE USER DEFINED VARIABLE CAUSED A NoneType EXCEPTION. Exiting...

File:  setup   Row:  173  - PROJECT MUST BE RUN FROM PACKAGED FORECAST_SEARCH_WIZARD FOLDER. Exiting...

File:  setup   Row:  178  - THE ./TEXT_DATA/ FOLDER COULD NOT BE FOUND. Creating... Exiting...

File:  check_vars   Row:  88  - Empty List of Words

File:  check_vars   Row:  127  - SETUP FAILURE: List of keywords contains something other than strings...

File:  check_vars   Row:  141  - SETUP FAILURE: List of products contains something other than strings...

File:  check_vars   Row:  160  - SETUP FAILURE: Invalid end year. Must not be higher than current year...

File:  check_vars   Row:  167  - SETUP FAILURE: Invalid start year... Valid options: 1996 - Current Year...

File:  check_vars   Row:  214/220  - REDUNDANT: REMOVING - <INPUT KEYWORD FROM THE LIST OF KEYWORDS...

File:  driver   Row:  68  -  Program Failed To Run due to (6-hour) TimeoutException...

File:  driver   Row:  80  -  Program Failed on UnicodeEncodeError... Possibly caused by a corrupt file.

File:  driver   Row:  89  -  Program Failed To Run To Completion...

File:  finder   Row:  182  - MISSING FILE: </path/data_file>

File:  finder   Row:  251/264  - FINDER: NO FORECAST HEADER WAS FOUND, <wfo> <iYear> Current: <idx> Last Good:  <idx_holder>

File:  finder   Row:  402  - TZ: TIMEZONE WARNING -  <idx_holder> <readData[idx_holder-1:idx_holder+1]>

File:  finder   Row:  423  - FINDER: idx_holder == 0. DDHHMM could not be found.

File:  finder   Row:  448  -  FINDER: NO FORECAST HEADER WAS FOUND (EOF),  <wfo> <iYear> Current: <idx> Last Good: <idx_holder>

File:  convert_time   Row:  55/56  - CT: Convert_Time Failure on <month>-<day>-<year> @ <hour><minute> <timezone>
 
File:  read_time   Row:  68  - TP: <wfo> - ERR NO MONTH FOUND... FATAL.  ?? - <int_day> - <year> @ <ddhhmm_list[idx]> Z  Check:<times.strip()>

File:  read_time   Row:  76  - TP: <wfo> - WMO Header Missing and MND Header Day Not Found. Exiting... Check File: <iYear> for <month> - ??? - <year> @ <ddhhmm_list[idx]> Z <times.strip()>
 
 File:  read_time   Row:  118  - TP: wfo - Time Information Could Not Be Found. (CONTINUING)... Check File: <iYear> for <month> - <int_day> - <year> @ <ddhhmm_list[idx]> Z <times.strip()>

File:  read_time   Row:  126  - TP: wfo - Time Information Could Not Be Found. [CONTINUING]... Check File: <iYear> for <month> - <int_day> - <year> @ <ddhhmm_list[idx]> Z <times.strip()>

File:  read_time   Row:  184  -TP: MAJOR DISCREPANCY - Using:  06-20-1998 21:42   ///  Other:  06-19-1998 07:24 	+++ 38.30 ++++ 	 FRI JUN 19 1998 	 124 AM  WMO - Day:  20  - Hour:  21  - Minute:  42   UTC

File:  read_time   Row:  215  -TP: Unknown - Exception Thrown. Continuing without the time in question. (Could be calendar, datetime, pytz issue or something else not expected)



## OTHER USES
Components of the Forecast Search Wizard could be used universally for parsing NWS/NOAA text products. The Forecast Search Wizard was carefully written in a way that this would be possible. This would enable a wide variety of applications dealing with NWS/NOAA text products. That includes making a database for NOAA/NWS text forecasts (@NOAA @NWS) or relaying NWS Forecasts (Impacts/Hazards/Warnings) to customers via apps. I would be open to consulting on a case-by-case basis.



## FUTURE

--- V1.0 Release ----
- Redo tests for changed arguments in wfo_rft_time.py and checkEverything
- Test find_header_nws, find_header, sort_time.py
- Edit/finalize documentation
- Add tools to analyze the output

---- V1.1 ----
- Enable user provided datasets (If you are able to do this elegantly please let me know.)
- Search-By-Section
- Parallel Version
