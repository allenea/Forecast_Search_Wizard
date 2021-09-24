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
import os
import sys
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from search_options.search_options import Option
from src.GET_DATA.retrieve import retrieve

def main():
    """ This is a NAMELIST I/O program. The user can configure this file to
    download the desired search dataset which is required by the Forecast
    Search Wizard. Simply execute this file once properly configured.


    The Forecast Search Wizard (download_data.py) has 6 parameters.

       1. Download_Data :: Boolean value True (Download Data)
                                         False (Do Not Download)

       2. Get_Latest_Year :: Boolean value True (Download Latest Year)
                                           False (Do Not Download)
       3. Remove_Empty :: Boolean value True (Remove Empty Forecast Products)
                                        False (Keep All Products)

       4. start_year :: integer value for year between 1996 and Present
                        * Ignored if Get_Latest_Year is True

       5. end_year :: integer value for stop year between 1996 and Present

       6. MASTER_LIST ::  a list of forecast products as strings or
                                select from the preset search options

    It is suggested that you download your desired dataset, then switch Get_Latest_Year
    to True enabling you to quickly download the latest years worth of data. Download
    only the data that you need if you are concerned about storage space. If you want
    to download as much data as possible that will likely range from 30 - 50 GB.
    Ex. I can store 23 years worth of data for 580 forecast products in under 32GB.
    """
# =============================================================================
#     1. Do you want to download the data?
#           Data Type = Boolean: True, False
# =============================================================================
    Download_Data = True


# =============================================================================
#     2. Download only the latest year.
#           Data Type = Boolean: True, False
#
#        PRO-TIP: Switch to True after the initial dataset has been downloaded
#                ==> To maintain dataset with most current data.
# =============================================================================
    Get_Latest_Year = False


# =============================================================================
#      3. Remove and identify PIL (forecast codes) with no data history.
#
#        If there is no data or empty files from start - end. You will be notified
# =============================================================================
    Remove_Empty = True


# =============================================================================
#     4. The first year of the desired dataset
#
#        Default: 1996 is the earliest data in the IEM database
# =============================================================================
    start_year = int(1996)


# =============================================================================
#     5. The final year of the desired dataset (to include that year)
#
#        Default: Current Year
# =============================================================================
    end_year = int(time.ctime()[-4:])


# =============================================================================
#     6. The List of PILs for the NWS text products.
#
#        Alt. provide it a preset option from the search_options class.
# =============================================================================
    MASTER_LIST = ["AFDLWX", "AFDPHI"]
    #MASTER_LIST = Option.MASTER_LIST

# =============================================================================
# =============================================================================
# =============================================================================
# # #                       DO NOT TOUCH (BELOW)                          # # #
# =============================================================================
# =============================================================================
# =============================================================================
    retrieve(MASTER_LIST, start_year=start_year, end_year=end_year,\
             download_data=Download_Data, get_latest_year=Get_Latest_Year,\
             remove_empty=Remove_Empty)

if __name__ == "__main__":
    main()
##################  DO NOT TOUCH (ABOVE) ######################################
