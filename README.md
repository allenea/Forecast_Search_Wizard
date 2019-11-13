# Forecast_Search_Wizard
 The Forecast Search Wizard makes it easier than ever before to analyze archived NOAA text products to obtain valuable information. The Forecast Search Wizard is a program that allows researchers to search keywords in NOAA/NWS text products (e.g., Area Forecast Discussions, Local Storm Reports, Watches/Warnings, etc.) to identify the occurrence of case studies, particular weather events, or other specific information. This tool will not only save the researcher time, but it will also improve the depth and quality of research by opening a door to a new source of data in the weather enterprise.
 
The only programs that need to be executed for the Forecast Search Wizard to run are located in the RUN_ME directory. These files are the FSW_NAMELIST.py and the DOWNLOAD_DATA.py. Each of these files are constructed so that minimal programming knowledge is required to use this program. 

Additional documentation can be found in the Documentation folder. This includes Frequently Used NWS Contractions, Preset [Search] Options, AWIPS and WFO ID's 


 
    - git clone https://github.com/allenea/Forecast_Search_Wizard.git
 
 Try (depending on your system... Tell it where to build):
 
    - python setup.py install
    
    - python setup.py build install --prefix $HOME/.local
    
    - python setup.py install --user


 
 ## TO RUN - RUN_ME folder:
 ### DOWNLOAD_DATA.py
 
_Execute in 2 steps. Internet connection is required for this step._
 
 1. Edit DOWNLOAD_DATA.py to download your dataset. There are 6 parameters that you can set in **DOWNLOAD_DATA**. For each parameter the _Default Value_ is given along with some _Valid Options_.The user can configure this file to download the desired search dataset which is required by the Forecast Search Wizard. Simply execute this file once properly configured. Currently the [Iowa Environmental Mesonet text archive](https://mesonet.agron.iastate.edu/wx/afos/list.phtml) is being used. All IEM data should be used for educational purposes only. IEM states "Please do not depend on this page for operational decision making, errors can and do occur with data processing, data reception and any other error possible with Internet communications." The Forecast Search Wizard only depends on the information in the written forecasts. The Forecast Search Wizard is not dependent upon sucessful archival in the IEM database, but in some instances the year the forecast was stored in the IEM database is used in the logic but this has more to do with the file naming structure. Other than that, all data retrieved by the Forecast Search Wizard is from the text products themselves. Currently, IEM is the only supported source of text data.
 
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

       Valid Options: Any year between 1996 and Present but later than the start_yar
      
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
                                               
 2. Execute this file once it has been properly configured. This step can take a few minutes to a few hours depending on the number and size of the forecasts.
      
              python DOWNLOAD_DATA.py


**DOWNLOAD OUTPUT:** A file that looks like *Data_Download_VerboseTue_Nov_12_195850_2019.out* will be stored in the RUN_ME folder. This is for your records to know what was downloaded and where. It explains everything that happened when you tried to download the dataset.

**DATA STORAGE:** The Forecast Search Wizard does require you to have available space to store the forecasts. I am able to download ~23 years of data for ~580 forecast products with a storage requirement of less than 32GB. This is an extreme scenario. If download Area Forecast Discussions for a single offices you might be able to expect that to take up 300 - 500 MB. Some forecasts are longer or more frequent and therefore take up more space.

**Preset Configurations:** You can create your own list, choose or modify existing options found in *~/search_options/search_options.py* by declaring *Option.<OPTION_NAME>*. By default the search_options module is imported for RUN_ME programs (DOWNLOAD_DATA and FSW_NAMELIST).

   **Example:**
   ```
   from search_options.search_options import Option
   MASTER_LIST = Option.ALL
   ```
*WGET routine from https://bitbucket.org/techtonik/python-wget/src*
     
     
     
     
### DOWNLOAD_DATA.py
 
_Execute in 2 steps. Internet connection is required for this step._
 
 1. Edit DOWNLOAD_DATA.py to download your dataset. There are 6 parameters that you can set in **DOWNLOAD_DATA**. For each parameter the _Default Value_ is given along with some _Valid Options_.The user can configure this file to download the desired search dataset which is required by the Forecast Search Wizard. Simply execute this file once properly configured. Currently the [Iowa Environmental Mesonet text archive](https://mesonet.agron.iastate.edu/wx/afos/list.phtml) is being used. All IEM data should be used for educational purposes only. IEM states "Please do not depend on this page for operational decision making, errors can and do occur with data processing, data reception and any other error possible with Internet communications." The Forecast Search Wizard only depends on the information in the written forecasts. The Forecast Search Wizard is not dependent upon sucessful archival in the IEM database, but in some instances the year the forecast was stored in the IEM database is used in the logic but this has more to do with the file naming structure. Other than that, all data retrieved by the Forecast Search Wizard is from the text products themselves. Currently, IEM is the only supported source of text data.
 
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

       Valid Options: Any year between 1996 and Present but later than the start_yar
      
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
                                               
 2. Execute this file once it has been properly configured. This step can take a few minutes to a few hours depending on the number and size of the forecasts.
      
              python FSW_NAMELIST.py



**OUTPUTS OF THE FORECAST SEARCH WIZARD:** Check the outputs when they are done. You will get one output located in the **FSW_WARN** folder with information about the run, any trouble it had, some statistics about the run, etc. The second output if the Forecast Search Wizard ran successfully will be located in the **FSW_OUTPUT** folder. This file will provide you with information about the search and the results of the search. In the future tools will become available to help analyze this data. Until then you are responsible for the analysis of the Forecast Search Wizard results.

**ASSUMPTIONS:** 

     - OPTIONAL: In /Search_Options/Search_Options.py, edit MY_SEARCH or create another variable to store your list of products you want searched. There are a few hundred preset options.  How you do this is up to you.
     
     - Edit FSW_NAMELIST.py to your search criteria
     
 





