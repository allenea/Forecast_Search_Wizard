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
# Default: In honor of my sea breeze/coastal wind research
#
# Imports
from __future__ import print_function
import os, sys           
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from search_options.search_options import Option
from src.driver import execute
from src.setup import setup

def main():
   
    """1. List of keywords you want to search....
    
    Not case sensitive. It is sensitive to spaces and characters.
    For robustness, try some possible common mispellings."""
    
    input_word_list = ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES", "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"] 
    
    
    
    """2. List of forecast products you want to search....
    
    See /search_options/search_options.py for preset options or create your own.
    Set = Option.<OPTION_NAME> below"""
    ## Example of a subset of all options... or manipulating the default search options.
    ## They must be sets since you cannot subtract lists. Then convert them back to a list. Sort for your benefit if you would like...
    #
    #list1 = list(set(Option.ALL) - set(Option.ALL_SPC))
    #list1.sort()
    #
    
    forecast_product_list = Option.MT_HOLLY_PHILADELPHIA_NJ_AFD
    
    
    
    
    """3. Set the start year....
    
    For IEM data the start year can be no earlier than 1996. This is a hard limit.
    If you are supplying your own data, make sure it's in the right format, 
    then change the ADMIN variable in the src/finder_functions.py program
    """
    
    start_year = 1996
    
    
    
    
    """4. Set the end year....
    This cannot exceed the current year.
    """
    
    end_year = 2019
    
    
    
    
    """5. How to search?
    
        Search for All of the words: Select True
        Search for ANY of the words: Select False
        
    Boolean: True/False
    """
    
    isAnd = False       
    
    
    
    
    """6. How to search?
    
        Search by forecast: Select True
        Search by day: Select False
        
    Boolean: True/False
    """
    
    byForecast = True 
    
    
    
    
    """7. How to search?
    
        GREP-Style Search: Select True
            Example:
                Input: ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES", "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"]
                Actual: ["SEA BREEZE", "SEA BREAZE", "SEABREEZE", "SEABREAZE"]
                
                
        Search for whole word or phrase: Select False
            Example:
                Input: ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES", "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"]
                Actual: [" SEA BREEZE ", " SEA BREAZE ", " SEABREEZES ", " SEABREEZE ", " SEABREAZES ", " SEABREAZE ", " SEA BREEZES ", " SEA BREAZES "]
                
                
    Boolean: True/False
    """
    
    isGrep = True
    
    
    
    
    
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
    ### DO NOT EDIT BELOW ####
    
    # HIGHLY RECOMMENDED THAT YOU DO NOT TOUCH make_assumptions... WORK IN PROGRESS... HOPING TO FIND A PERMENANT SOLUTION.
    # make_assumptions = True allows this search to make basic 'safe' assumptions for cases with incomplete date or time information. 
    # Any assumption made based on whether the forecast was issued in the AM or PM will be indicated with a '*'.
    # Any assumption made based on the date or time (year, month, day, hour, minute) will be indicated with a '#'.\
    # See documentation for more information.
    make_assumptions = True
    
    # DO NOT TOUCH THIS OR A FISH WILL DROWN AND IT WILL BE YOUR FAULT. ~If fish are already drowning, switch debug_flag to True.~
    FSW_SEARCH = setup(input_word_list, forecast_product_list, start_year, end_year, isAnd, byForecast, make_assumptions, isGrep, debug_flag=False)
    execute(FSW_SEARCH)
    
    
#EXECUTE THIS BY RUNNING FSW_NAMELIST.py
if __name__ == "__main__":  
    main()