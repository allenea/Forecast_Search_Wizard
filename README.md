# Forecast_Search_Wizard
 The Forecast Search Wizard makes it easier than ever before to analyze archived NOAA text products to obtain valuable information. The Forecast Search Wizard is a program that allows researchers to search keywords in NOAA/NWS text products (e.g., Area Forecast Discussions, Local Storm Reports, Watches/Warnings, etc.) to identify the occurrence of case studies, particular weather events, or other specific information. This tool will not only save the researcher time, but it will also improve the depth and quality of research by opening a door to a new source of data in the weather enterprise.
 
 
 python setup.py install
 
 TO RUN - IN RUN_ME folder:
 
     - Edit download_data.py to download your dataset. The preset configuration is AFDPHI and AFDLWX. You can remove that and use the list of all tested products, which is surrounded by """   """" in the file. 
     
     - run download_data.py to download the data. If you are doing the entire dataset with over 10 Million forecasts it might take 60-70 minutes. Internet connection is required for this step.
     
     - OPTIONAL: In /Search_Options/Search_Options.py, edit MY_SEARCH or create another variable to store your list of products you want searched. There are a few hundred preset options. You can then call Option.<YOUR OPTION> in the FSW_NAMELIST.py instead of creating the list there. How you do this is up to you.
     
     - Edit FSW_NAMELIST.py to your search criteria
     
     - run FSW_NAMELIST.py to run the Forecast Search Wizard
     
     
     
     A more complete set of instructions and documentation to come. Additional information can be found in the FSW_NAMELIST and download_data files.
