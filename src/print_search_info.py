#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:58:29 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 11:56AM

Prints out important information to the console. 

This should help you find your files and see if/where something might be going
wrong so you can fix it in the main file (calls the core.py which runs when it 
has all the necessary info.
"""
from __future__ import print_function
from src.split_list import split_list
import sys


def print_info(usr_vars, isSetUp):
    welcome()
    ## PRINT OUT USER INFORMATION
    print("SEARCH INFORMATION")
    print("------------------------")
    print("\nSETUP SUCCESSFUL: ",isSetUp)
    print("\nAPPLICATION DIRECTORY: ", usr_vars['APPLICATION_ROOT_DIRECTORY'])
    print("\nTEXT DATA PATH: ", usr_vars['TEXT_DATA_PATH'])
    print("\nWARNING DIRECTORY: ", usr_vars['WARNING_PATH'])
    print("\nOUTPUT DIRECTORY: ",usr_vars['OUTPUT_PATH'])
    print("\nPRODUCTS BEING SEARCHED: ",usr_vars['STATION_LIST'])
    print("\nLIST OF KEYWORDS: ", usr_vars['KEYWORD_LIST'])
    print("\nSTART YEAR: ", usr_vars['START_YEAR'])
    print("END YEAR: ", usr_vars['END_YEAR'])
    print("\nSearch By And (True) or Or (False): ", usr_vars['And_Or'])
    print("Search By Forecast (True) or Day (False): ", usr_vars['ByForecast_ByDay'])
    print("Make Basic Assumptions: ", usr_vars['Make_Assumptions'])
    print("Is Grep Style Search: ", usr_vars['isGrep'])
    print("\n\nThe Forecast Search Wizard was developed by Eric Allen",\
          "\n(Follow on Twitter: @THE_Eric_Allen and Support: @WxSearchWizard)\n\n")
    sys.stdout.flush()


def algor_stats(station_list, mainword, total_mentions, num_days, no_dups, start, end, bad):   #ADD COUNT PER KEYWORD
    """ This function displays the FSW alorigthm's "Quick Statistics"."""
    print("\n--------ALGORITHM STATISTICS---------")
    print("Years Searched: "+str(start)+" - "+str(end)) 
    station_split_list = split_list(station_list,7)
    print("Products Searched:")
    for eric in range(len(station_split_list)):
        station_split_list[eric] = str(station_split_list[eric]).replace("[", " ")
        station_split_list[eric] = str(station_split_list[eric]).replace("]", " ")
        print("\t",station_split_list[eric])
        sys.stdout.flush()
    print("\nKeyword:  " , mainword)
    print("\nTotal Cases Found: ", num_days)
    print("\nTotal Mentions: ", total_mentions)
    print("Unique Mentions: ", no_dups)
    #print("Timezone Errors: ",bad, flush=True)
    print("--------END ALGORITHM STATISTICS------\n")
    sys.stdout.flush()

    
def final_message():
    """ This is the final message that prints once the program has run to completion."""
    print("****** A Note From Eric Allen ******")
    print("- Remember that sometimes words are used when not referring to a forecasted weather event (i.e. Hurricane Preparedness Week).")
    print("- Always go back and check the forecast, perform analysis on observations with a 'loose' threshold, or check surface analysis.")
    print("- As great as NWS/NCEP forecasters are, sometimes forecasts busts and events don't happen, especially in the long-term section.")
    print("- Hopefully a future version will include the ability to search-by-section to target ongoing or near-term forecast analysis.")
    print("- Try again with different variations and misspellings of keyword, and take a look at the NWS Contractions file in Documentation.")
    print("\nThank You")
    print("************************************\n")
    sys.stdout.flush()
 
    
def data_acknowledgement(): 
    """ This is the acknowledgement to IEM for using their data. Regardless of where you have gotten your data for this program. Make sure to give credits or acknowledgements."""
    print("\nThank you to Daryl Herzmann at Iowa Env. Mesonet for the assistance and data.")
    print("All Iowa Mesonet Data should be used for educational purposes only.\n")
    print("WGET routine from https://bitbucket.org/techtonik/python-wget/src  - UNLICENSED\n")
    sys.stdout.flush()
    
def welcome():
    """ This is the welcome message that is displayed at the beginning of the program."""
    print("\n##  You are using the Forecast Search Wizard: a NOAA Text Product Keyword Finder. ")
    print("\n##  This is an independently developed program by Eric Allen - All Rights Reserved.")
    print("##  Please cite: 'Allen, E., 2019: Forecast Search Wizard: A Tool to Search NOAA Text-Forecasts. Poster, Weather\n\t\t\tAnalysis and Forecasting, 44th Annual National Weather Association Meeting, Huntsville,\n\t\t\tAlabama, 10 September 2019.'  \n\n") ## TODO UPDATE DOI
    sys.stdout.flush()