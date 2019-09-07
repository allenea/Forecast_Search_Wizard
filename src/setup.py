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
import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.check_vars import search_option, input_words, AndTrue_OrFalse, byforecast, set_year_range, makeAssumptions, grep_check, debug_check
from src.software_require import setup_FSW
from src.print_search_info import print_info

def setup(input_word_list,forecast_product_list,start_year,end_year, AndOr, byForecast, make_assumptions, isGrep, debug_flag=False):
    """ Check to make sure everything passed to the FSW is valid. And the FSW is properly installed with required packages. No PyTests"""

    if setup_FSW() != True:
        print("INVALID SYSTEM REQUIREMENTS. Killed by software_require.py in setup.py")#,flush=True)
        sys.stdout.flush()
        sys.exit(0)
    else:
        isSetUp = True
        
    search = SEARCH_VARIABLES()
    
    #DEFAULT VARIABLES
    search.get_default_variables()
    if search_option(forecast_product_list) == True:
        search.STATION_LIST = [x.upper() for x in forecast_product_list]
    
    search.START_YEAR, search.END_YEAR = set_year_range(start_year, end_year)
    search.And_Or = AndTrue_OrFalse(AndOr)
    search.ByForecast_ByDay = byforecast(byForecast)

    search.Make_Assumptions = makeAssumptions(make_assumptions)
    search.isGrep = grep_check(isGrep)
    search.debug_mode = debug_check(debug_flag)

    if input_words(input_word_list, search.isGrep) != None:
        search.KEYWORD_LIST = input_words(input_word_list, search.isGrep) 
    
    FSW_SEARCH = search.status_variables()
 
    print_info(FSW_SEARCH, isSetUp)

    if None in FSW_SEARCH.values():
        print("FAILURE IN SETUP...AT LEAST ONE USER DEFINED VARIABLE CAUSED A NoneType EXCEPTION. Exiting....")#,flush=True)
        print("Setup.py is designed to verify that only valid search criteria is passed to the Finder program.")#,flush=True)
        sys.stdout.flush()
        sys.exit(0)
    else:
        return FSW_SEARCH


# SETS DEFAULT VARIABLES
class SEARCH_VARIABLES(object):
    
    def __init__(self,
                 APPLICATION_ROOT_DIRECTORY = "",
                 TEXT_DATA_PATH = "",
                 WARNING_PATH="",
                 OUTPUT_PATH="",
                 STATION_LIST=[],
                 KEYWORD_LIST=[],
                 START_YEAR=1996,
                 END_YEAR=2019,
                 And_Or=False,
                 ByForecast_ByDay=True,
                 Make_Assumptions=True,
                 isGrep=True,
                 debug_mode=False):

        
        #USER_ID = getpass.getuser()
        OS_SYSTEM = sys.platform
        
        #FOR NOT CODED THIS STRUCTURE IN CASE I NEED TO DO SOMETHING WITH IT THAT I AM NOT FORSEEING....? #Needed it for installing Exiftools on different os for the PyDatPicture program...
        if APPLICATION_ROOT_DIRECTORY == "":
            if OS_SYSTEM == "darwin":
                self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../') 
                
            # FOR MICROSOFT - WINDOWS USERS
            elif OS_SYSTEM == "win32" or OS_SYSTEM == "cygwin":
                self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../') 
                
            # FOR LINUX USERS   
            else: 
               self.APPLICATION_ROOT_DIRECTORY = os.path.abspath('../') 
        else:
            self.APPLICATION_ROOT_DIRECTORY=APPLICATION_ROOT_DIRECTORY
            
        #Output path.. try to keep all the outputs together - by default
        if TEXT_DATA_PATH == "":
            self.TEXT_DATA_PATH = os.path.abspath("../")#+'/TEXT_DATA/'
            self.TEXT_DATA_PATH = os.path.join(self.APPLICATION_ROOT_DIRECTORY,'TEXT_DATA')

        else:
            self.TEXT_DATA_PATH = TEXT_DATA_PATH  ## Run directory?
            
         #Output path.. try to keep all the outputs together - by default
        if WARNING_PATH == "":
            self.WARNING_PATH = os.path.join(self.APPLICATION_ROOT_DIRECTORY,'FSW_WARN')
        else:
            self.WARNING_PATH = WARNING_PATH  ## Run directory?
        
        #Output path.. try to keep all the outputs together - by default
        if OUTPUT_PATH == "":
            self.OUTPUT_PATH = os.path.join(self.APPLICATION_ROOT_DIRECTORY,'FSW_OUTPUT')
        else:
            self.OUTPUT_PATH = OUTPUT_PATH  ## Run directory?
            
            
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
        self.debug_mode = debug_mode

        
        #Dictionary of Variables... Used by the other programs
        self._user_vars = {'APPLICATION_ROOT_DIRECTORY':self.APPLICATION_ROOT_DIRECTORY,\
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
               'debug_mode':self.debug_mode}

        
        SEARCH_VARIABLES.get_default_variables(self)
    
    def get_default_variables(self):
        return self._user_vars 


    def status_variables(cls):
        """ CALL/SET BEFORE PASSING TO MAIN"""
        
        # IF DOES NOT EXIST... WHAT ARE YOU DOING!?
        if not os.path.exists(cls.APPLICATION_ROOT_DIRECTORY):
            print("PROJECT MUST BE RUN FROM PACKAGED NWS_AFD_KEYWORD_FINDER folder (directory). Exiting...")#,flush=True)
            sys.stdout.flush()
            sys.exit(0)    
            
        if not os.path.exists(cls.TEXT_DATA_PATH):
            print("THE ./TEXT_DATA/ FOLDER COULD NOT BE FOUND. CREATING NEW ONE. DOES NOT HAVE DATA. Exiting...")#,flush=True)
            sys.stdout.flush()
            os.makedirs(cls.TEXT_DATA_PATH) 
            sys.exit(0)
            
        if not os.path.exists(cls.WARNING_PATH):
            os.makedirs(cls.WARNING_PATH)    
        
        if not os.path.exists(cls.OUTPUT_PATH):
            os.makedirs(cls.OUTPUT_PATH)          
        
        cls.user_vars = {'APPLICATION_ROOT_DIRECTORY':cls.APPLICATION_ROOT_DIRECTORY,\
               'TEXT_DATA_PATH':cls.TEXT_DATA_PATH,\
               'WARNING_PATH':cls.WARNING_PATH,\
               'OUTPUT_PATH':cls.OUTPUT_PATH,\
               'STATION_LIST':cls.STATION_LIST,\
               'KEYWORD_LIST':cls.KEYWORD_LIST,\
               'START_YEAR':cls.START_YEAR,\
               'END_YEAR':cls.END_YEAR,
               'And_Or':cls.And_Or,\
               'ByForecast_ByDay':cls.ByForecast_ByDay,\
               'Make_Assumptions':cls.Make_Assumptions,\
               'isGrep':cls.isGrep,\
               'debug_mode':cls.debug_mode}
                
        return cls.user_vars
    
    
    
    