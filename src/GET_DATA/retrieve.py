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
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.split_list import split_list
from src.print_search_info import data_acknowledgement
from src.GET_DATA.wget_data import get_data
from src.GET_DATA.CheckData import CheckRemove_Data

ADMIN_EARLIEST_YEAR = 1996
ADMIN_CURRENT_YEAR = int(time.ctime()[-4:])

def retrieve(master_list, start_year=ADMIN_EARLIEST_YEAR, end_year=ADMIN_CURRENT_YEAR,\
             download_data=True, get_latest_year=False, remove_empty=True):
    """ Main Function to download data"""

    if not download_data:
        sys.exit("Download Data was not set to true, therefore no data will be downloaded."+\
              "Existing dataset will be preserved.")
    if start_year < ADMIN_EARLIEST_YEAR:
        start_year = ADMIN_EARLIEST_YEAR
    if end_year > ADMIN_CURRENT_YEAR:
        end_year = ADMIN_CURRENT_YEAR
    if start_year > end_year:
        tmp = start_year
        start_year = end_year
        end_year = tmp
    if get_latest_year:
        start_year = ADMIN_CURRENT_YEAR
        end_year = ADMIN_CURRENT_YEAR


    #Redict messages to out file over the course of the download
    fname = sys.stdout
    str_time = "_".join((time.ctime().replace(" ", "_")).split("_")[1:])

    ## LOCAL COMPUTER
    print("\n\nCheck: (", os.path.join(os.path.abspath("./.."), "downloadLogs", "Data_Download_Verbose_"+\
                str_time.replace(":", "")+".out"),\
                ") to view the progress of the data download.")

    sys.stdout = open(os.path.join(os.path.abspath("./.."), "downloadLogs", "Data_Download_Verbose_"+\
                str_time.replace(":", "")+".out"), 'w')
    
    
    ## AWS
    """
    print("\n\nCheck: (", os.path.join("/", "Forecast_Search_Wizard", "downloadLogs", "Data_Download_Verbose_"+\
                str_time.replace(":", "")+".out"),\
                ") to view the progress of the data download.")

	sys.stdout = open(os.path.join("/","Forecast_Search_Wizard", "downloadLogs", "Data_Download_Verbose_"+\
                                   str_time.replace(":", "")+".out"), 'w')
	"""

    #Start Timer
    start_time = time.time()

    #Print Statements
    print("IEM Text-Data Retrieval is Powered by the Forecast Search Wizard\n")
    sys.stdout.flush()

    print(time.ctime())
    sys.stdout.flush()

    print("\nDownload Data? " + str(download_data))
    sys.stdout.flush()

    print("Get the Latest Year? " + str(get_latest_year))
    if get_latest_year:
        print("Start: " + str(end_year)+"\t\t End: "+str(end_year))
        sys.stdout.flush()
    else:
        print("Start: " + str(start_year)+"\t\t End: "+str(end_year))
        sys.stdout.flush()

    print("Sorting text products alphabetically...")
    sys.stdout.flush()

    #Sort the list
    master_list.sort()

    #Neatly print out the list to the output file
    master_split = split_list(master_list, 10)
    first_row = True
    for allen in range(len(master_split)):
        master_split[allen] = str(master_split[allen]).replace("[", " ")
        master_split[allen] = str(master_split[allen]).replace("]", " ")
        if not first_row:
            print("\t\t\t", master_split[allen])
            sys.stdout.flush()

        else:
            print("Forecast Products: ", master_split[allen])
            sys.stdout.flush()
            first_row = False


    data_dir = get_data(master_list, start_year, end_year)

    #If folder contains only empty files... do what file says.
    if remove_empty:
        CheckRemove_Data(data_dir)

    #Print Lapse Time
    print("--- %s seconds ---"%(time.time() - start_time))
    sys.stdout.flush()
    data_acknowledgement()
    #Close log file
    sys.stdout.close()
    sys.stdout = fname
