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
import time
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.print_search_info import print_info
from src.check_vars import search_option, input_words, AndTrue_OrFalse, byforecast,\
                            set_year_range, makeAssumptions, grep_check, debug_check,\
                            bulk_check

def setup(input_word_list, forecast_product_list, start_year, end_year, AndOr, byForecast,\
          make_assumptions, isGrep, bulk_search=False, debug_flag=False):
    """Check for valid search criteria. Validate Search."""

    search = SEARCH_VARIABLES()

    #DEFAULT VARIABLES
    search.get_default_variables()
    if search_option(forecast_product_list):
        search.STATION_LIST = list(map(str.upper, forecast_product_list))
    else:
        print("FAILURE IN SETUP...INVALID PRODUCT LIST SEARCH OPTION. Exiting....")
        print("Setup.py is designed to verify that only valid search criteria"+\
              " is passed to the Finder program.")
        sys.stdout.flush()
        sys.exit(0)

    search.START_YEAR, search.END_YEAR = set_year_range(start_year, end_year)
    search.And_Or = AndTrue_OrFalse(AndOr)
    search.ByForecast_ByDay = byforecast(byForecast)

    search.Make_Assumptions = makeAssumptions(make_assumptions)
    search.isGrep = grep_check(isGrep)
    search.bulk_search = bulk_check(bulk_search)
    search.debug_mode = debug_check(debug_flag)

    search.RUN_START_TIME = datetime.datetime.today().strftime('%y%m%d_%H%M')

    tmp_in_key = input_words(input_word_list, search.isGrep)

    if  tmp_in_key is not None:
        search.KEYWORD_LIST = tmp_in_key
    else:
        print("FAILURE IN SETUP...INVALID INPUT KEYWORDS. Exiting....")
        print("Setup.py is designed to verify that only valid search criteria is"+\
              " passed to the Finder program.")
        sys.stdout.flush()
        sys.exit(0)

    FSW_SEARCH = search.status_variables()

    print_info(FSW_SEARCH)

    if None in FSW_SEARCH.values():
        print("FAILURE IN SETUP...AT LEAST ONE USER DEFINED VARIABLE CAUSED A NoneType EXCEPTION."+\
              " Exiting...")
        print("Setup.py is designed to verify that only valid search criteria is passed "+\
              "to the Finder program.")
        sys.stdout.flush()
        sys.exit(0)
    else:
        return FSW_SEARCH


# SETS DEFAULT VARIABLES
class SEARCH_VARIABLES:
    """SEARCH VARIABLES CLASS"""
    def __init__(self,
                 APPLICATION_ROOT_DIRECTORY=os.path.abspath('../'),
                 TEXT_DATA_PATH=os.path.abspath('../TEXT_DATA'),
                 WARNING_PATH=os.path.abspath('../FSW_WARN'),
                 OUTPUT_PATH=os.path.abspath('../FSW_OUTPUT'),
                 STATION_LIST=None,
                 KEYWORD_LIST=None,
                 START_YEAR=1996,
                 END_YEAR=int(time.ctime()[-4:]),
                 And_Or=False,
                 ByForecast_ByDay=True,
                 Make_Assumptions=True,
                 isGrep=True,
                 debug_mode=False,
                 bulk_search=False,
                 RUN_START_TIME=None,
                 WARNING_FILE=None):

#        os_system = sys.platform

        if APPLICATION_ROOT_DIRECTORY == "":
            self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../')
# =============================================================================
#
#             if os_system == "darwin":
#                 self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../')
#
#             # FOR MICROSOFT - WINDOWS USERS
#             elif os_system in ("win32", "cygwin"):
#                 self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../')
#
#             # FOR LINUX USERS
#             else:
#                 self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../')
# =============================================================================
        else:
            self.APPLICATION_ROOT_DIRECTORY = APPLICATION_ROOT_DIRECTORY


        if TEXT_DATA_PATH == "":
            #self.TEXT_DATA_PATH = os.path.abspath("../")
            self.TEXT_DATA_PATH = os.path.join(self.APPLICATION_ROOT_DIRECTORY, 'TEXT_DATA')
        else:
            self.TEXT_DATA_PATH = TEXT_DATA_PATH


        if WARNING_PATH == "":
            self.WARNING_PATH = os.path.join(self.APPLICATION_ROOT_DIRECTORY, 'FSW_WARN')
        else:
            self.WARNING_PATH = WARNING_PATH


        if OUTPUT_PATH == "":
            self.OUTPUT_PATH = os.path.join(self.APPLICATION_ROOT_DIRECTORY, 'FSW_OUTPUT')
        else:
            self.OUTPUT_PATH = OUTPUT_PATH

        #File Names
        self.STATION_LIST = STATION_LIST
        self.KEYWORD_LIST = KEYWORD_LIST
        self.START_YEAR = START_YEAR
        self.END_YEAR = END_YEAR

        #Booleans and associated QC
        self.And_Or = And_Or
        self.ByForecast_ByDay = ByForecast_ByDay
        self.Make_Assumptions = Make_Assumptions
        self.isGrep = isGrep
        self.bulk_search = bulk_search
        self.debug_mode = debug_mode

        self.RUN_START_TIME = RUN_START_TIME
        self.WARNING_FILE = WARNING_FILE


        #Dictionary of Variables... Used by the other programs
        self.user_vars = {'APPLICATION_ROOT_DIRECTORY':self.APPLICATION_ROOT_DIRECTORY,\
                          'TEXT_DATA_PATH':self.TEXT_DATA_PATH,\
                          'WARNING_PATH':self.WARNING_PATH,\
                          'OUTPUT_PATH':self.OUTPUT_PATH,\
                          'STATION_LIST':self.STATION_LIST,\
                          'KEYWORD_LIST':self.KEYWORD_LIST,\
                          'START_YEAR':self.START_YEAR,\
                          'END_YEAR':self.END_YEAR,
                          'And_Or':self.And_Or,\
                          'ByForecast_ByDay':self.ByForecast_ByDay,\
                          'Make_Assumptions':self.Make_Assumptions,\
                          'isGrep':self.isGrep,\
                          'debug_mode':self.debug_mode,\
                          'bulk_search':self.bulk_search,\
                          'RUN_START_TIME':self.RUN_START_TIME,\
                          'WARNING_FILE':self.WARNING_FILE}


        SEARCH_VARIABLES.get_default_variables(self)

    def get_default_variables(self):
        """docstring"""
        return self.user_vars


    def status_variables(self):
        """ CALL/SET BEFORE PASSING TO MAIN"""

        # IF DOES NOT EXIST... WHAT ARE YOU DOING!?
        if not os.path.exists(self.APPLICATION_ROOT_DIRECTORY):
            print("PROJECT MUST BE RUN FROM PACKAGED FORECAST_SEARCH_WIZARD FOLDER. Exiting...")
            sys.stdout.flush()
            sys.exit(0)

        if not os.path.exists(self.TEXT_DATA_PATH):
            print("THE ./TEXT_DATA/ FOLDER COULD NOT BE FOUND. Creating... Exiting...")
            print("Make sure you have downloaded the data with DOWNLOAD_DATA.py")
            sys.stdout.flush()
            os.makedirs(self.TEXT_DATA_PATH)
            sys.exit(0)

        if not os.path.exists(self.WARNING_PATH):
            os.makedirs(self.WARNING_PATH)

        if not os.path.exists(self.OUTPUT_PATH):
            os.makedirs(self.OUTPUT_PATH)

        if len(self.STATION_LIST) == 1:
            wfname = self.RUN_START_TIME+"_"+str.replace(self.KEYWORD_LIST[0][:9], " ", "_")+"_"+\
                self.STATION_LIST[0]+"_"+str(self.START_YEAR)+\
                str(self.END_YEAR)+"_errors.txt"
        else:
            wfname = self.RUN_START_TIME+"_"+str.replace(self.KEYWORD_LIST[0][:9], " ", "_")+"_"+\
                str(len(self.STATION_LIST))+"_"+str(self.START_YEAR)+\
                str(self.END_YEAR)+ "_errors.txt"


        wfname = str.replace(wfname, "__", "_")
        self.WARNING_FILE = os.path.join(self.WARNING_PATH, wfname)


        self.user_vars = {'APPLICATION_ROOT_DIRECTORY':self.APPLICATION_ROOT_DIRECTORY,\
                          'TEXT_DATA_PATH':self.TEXT_DATA_PATH,\
                          'WARNING_PATH':self.WARNING_PATH,\
                          'OUTPUT_PATH':self.OUTPUT_PATH,\
                          'STATION_LIST':self.STATION_LIST,\
                          'KEYWORD_LIST':self.KEYWORD_LIST,\
                          'START_YEAR':self.START_YEAR,\
                          'END_YEAR':self.END_YEAR,
                          'And_Or':self.And_Or,\
                          'ByForecast_ByDay':self.ByForecast_ByDay,\
                          'Make_Assumptions':self.Make_Assumptions,\
                          'isGrep':self.isGrep,\
                          'debug_mode':self.debug_mode,\
                          'bulk_search':self.bulk_search,\
                          'RUN_START_TIME':self.RUN_START_TIME,\
                          'WARNING_FILE':self.WARNING_FILE}

        return self.user_vars
