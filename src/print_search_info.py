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
# Please properly cite code, derivative code, and outputs
# of the Forecast Search Wizard in all scholarly work and
# publications.
#
# Imports
from __future__ import print_function
import sys
from src.split_list import split_list

def print_info(usr_vars):
    """Print Information Related To The Search"""
    welcome()
    ## PRINT OUT USER INFORMATION
    print("SEARCH INFORMATION")
    print("------------------------")
    print("\nAPPLICATION DIRECTORY: ", usr_vars['APPLICATION_ROOT_DIRECTORY'])
    print("\nTEXT DATA PATH: ", usr_vars['TEXT_DATA_PATH'])
    print("\nWARNING DIRECTORY: ", usr_vars['WARNING_PATH'])
    if not usr_vars['bulk_search']:
        print("\nWARNING FILE NAME: ", usr_vars['WARNING_FILE'])
    print("\nOUTPUT DIRECTORY: ", usr_vars['OUTPUT_PATH'])
    print("\nPRODUCTS BEING SEARCHED: ", usr_vars['STATION_LIST'])
    print("\nLIST OF KEYWORDS: ", usr_vars['KEYWORD_LIST'])
    print("\nSTART YEAR: ", usr_vars['START_YEAR'])
    print("END YEAR: ", usr_vars['END_YEAR'])
    print("\nSearch By And (True) or Or (False): ", usr_vars['And_Or'])
    print("Search By Forecast (True) or Day (False): ", usr_vars['ByForecast_ByDay'])
    print("Is Grep Style Search: ", usr_vars['isGrep'])
    print("Is [Special] Bulk Search (default: False): ", usr_vars['bulk_search'])
    print("Make Basic Assumptions: ", usr_vars['Make_Assumptions'])
    print("\n\nThe Forecast Search Wizard was developed by Eric Allen",\
          "\n(Follow on Twitter: @THE_Eric_Allen and Support: @WxSearchWizard)\n\n")
    sys.stdout.flush()


#ADD COUNT PER KEYWORD
def algor_stats(fsw_search, mainword, total_mentions, num_days, no_dups):
    """ This function displays the FSW alorigthm's "Quick Statistics"."""
    print("\n--------ALGORITHM STATISTICS---------")
    print("Years Searched: "+str(fsw_search["START_YEAR"])+" - "+str(fsw_search["END_YEAR"]))
    station_split_list = split_list(fsw_search["STATION_LIST"], 7)
    print("Products Searched:")
    for eric in range(len(station_split_list)):
        station_split_list[eric] = str(station_split_list[eric]).replace("[", " ")
        station_split_list[eric] = str(station_split_list[eric]).replace("]", " ")
        print("\t", station_split_list[eric])
        sys.stdout.flush()
    print("\nKeyword:  ", mainword)
    print("\nTotal Cases Found: ", num_days)
    print("\nTotal Mentions: ", total_mentions)
    print("Unique Mentions: ", no_dups)
    print("--------END ALGORITHM STATISTICS------\n")
    sys.stdout.flush()


def final_message():
    """ This is the final message that prints once the program has run to completion."""
    print("****** A Note From Eric Allen ******")
    print("- Remember that sometimes words are used when not referring to a forecasted"+\
          " weather event (i.e. Hurricane Preparedness Week).")
    print("- Validate the search by checking the forecast, surface analysis, or observations.")
    print("- As great as NWS/NCEP forecasters are, sometimes forecasts busts and events"+\
          " don't happen, especially in the long-term section.")
    print("- Hopefully a future version will include the ability to search-by-section to"+\
          " target ongoing or near-term forecasts.")
    print("- Try again with different variations and misspellings of keyword, and take a"+\
          " look at the NWS Contractions file in Documentation.")
    print("\nThank You")
    print("************************************\n")
    sys.stdout.flush()


def data_acknowledgement():
    """ This is the acknowledgement to IEM for using their data. Regardless of where you have
    gotten your data for this program. Make sure to give credits or acknowledgements."""
    print("\nThank you to Daryl Herzmann and the Iowa Env. Mesonet for the assistance and data.")
    print("All Iowa Mesonet Data should be used for educational purposes only.\n")
    print("WGET routine from https://bitbucket.org/techtonik/python-wget/src\n")
    sys.stdout.flush()


def welcome():
    """ This is the welcome message that is displayed at the beginning of the program."""
    print("\n##  You are using the Forecast Search Wizard: a NOAA Text Product Keyword Finder. ")
    print("\n##  This is an independently developed program by Eric Allen - All Rights Reserved.")
    print("##  Please cite: 'Eric Allen. Forecast Search Wizard: A Tool to Search NOAA Text-"+\
          "Forecasts." + "\n\t\t\tPoster, Data Science Institute Symposium, Newark, Delaware, "+\
            "15 November 2019.\n\t\t\tdoi:10.5281/zenodo.3542412.'\n\n")
    sys.stdout.flush()
