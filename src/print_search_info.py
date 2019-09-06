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
from src.split_list import split_list

def print_info(usr_vars, isSetUp):
    welcome()
    ## PRINT OUT USER INFORMATION
    print("SEARCH INFORMATION", flush=True)
    print("------------------------", flush=True)
    print("SETUP SUCCESSFUL: ",isSetUp, flush=True)
    print(flush=True)
    print("APPLICATION DIRECTORY: ", usr_vars['APPLICATION_ROOT_DIRECTORY'], flush=True)
    print(flush=True)
    print("TEXT DATA PATH: ", usr_vars['TEXT_DATA_PATH'], flush=True)
    print(flush=True)
    print("WARNING DIRECTORY: ", usr_vars['WARNING_PATH'], flush=True)
    print(flush=True)
    print("OUTPUT DIRECTORY: ",usr_vars['OUTPUT_PATH'], flush=True)
    print(flush=True)
    print("PRODUCTS BEING SEARCHED: ",usr_vars['STATION_LIST'], flush=True)
    print(flush=True)
    print("LIST OF KEYWORDS: ", usr_vars['KEYWORD_LIST'], flush=True)
    print(flush=True)
    print("START YEAR: ", usr_vars['START_YEAR'], flush=True)
    print("END YEAR: ", usr_vars['END_YEAR'], flush=True)
    print(flush=True)
    print("Search By And (True) or Or (False): ", usr_vars['And_Or'], flush=True)
    print("Search By Forecast (True) or Day (False): ", usr_vars['ByForecast_ByDay'], flush=True)
    print("Make Basic Assumptions: ", usr_vars['Make_Assumptions'], flush=True)
    print("Is Grep Style Search: ", usr_vars['isGrep'], flush=True)
    print(flush=True)
    print(flush=True)
    print("The Forecast Search Wizard was developed by Eric Allen",\
          "\n(Follow on Twitter: @THE_Eric_Allen and Support: @WxSearchWizard)", flush=True)
    print(flush=True)
    print(flush=True)



def algor_stats(station_list, mainword, total_mentions, num_days, no_dups, start, end, bad):   #ADD COUNT PER KEYWORD
    """ This function displays the FSW alorigthm's "Quick Statistics"."""
    print(flush=True)
    print(flush=True)
    print("--------ALGORITHM STATISTICS---------", flush=True)
    print("Years Searched: "+str(start)+" - "+str(end), flush=True) 
    station_split_list = split_list(station_list,7)
    print("Products Searched:", flush=True)
    for eric in range(len(station_split_list)):
        station_split_list[eric] = str(station_split_list[eric]).replace("[", " ")
        station_split_list[eric] = str(station_split_list[eric]).replace("]", " ")
        print("\t",station_split_list[eric], flush=True)
    print(flush=True)
    print("Keyword:  " , mainword, flush=True)
    print("Total Mentions: ", total_mentions, flush=True)
    print("Total Cases Found: ", num_days, flush=True)
    print("Unique Mentions: ", no_dups, flush=True)
    #print("Timezone Errors: ",bad, flush=True)
    print("--------END ALGORITHM STATISTICS------", flush=True)
    print(flush=True)
    print(flush=True)
    
    
def final_message():
    """ This is the final message that prints once the program has run to completion."""
    print(flush=True)
    print(flush=True)
    print("****** A Note From Eric Allen ******", flush=True)
    print("- Remember that sometimes words are used when not referencing about a forecasted event. i.e. Hurricane Preparedness Week.", flush=True)
    print("- Always go back and check the forecast, perform analysis on observations with a 'loose' threshold, or check surface analysis.", flush=True)
    print("- As great as NWS/NCEP forecasters are, sometimes forecasts busts and events don't happen.", flush=True)
    print("- Hopefully a future version will include the ability to search by section to target current, ongoing, or near-term forecast analysis.", flush = True)
    print("- Try again with different variations and misspellings of keywords.", flush=True)
    print("- Try to remove spaces? Think of potential typos for better coverage.", flush=True)
    print(flush=True)
    print("Thank You", flush=True)
    print("************************************", flush=True)   
    
    
def data_acknowledgement(): 
    """ This is the acknowledgement to IEM for using their data. Regardless of where you have gotten your data for this program. Make sure to give credits or acknowledgements."""
    print(flush=True)
    print("Thank you to Daryl Herzmann at Iowa Env. Mesonet for the assistance", flush=True)
    print("All Iowa Mesonet Data should be used for educational purposes only.", flush=True)
    print(flush=True)
    print("WGET routine from https://bitbucket.org/techtonik/python-wget/src  - UNLICENSED", flush=True)
    print(flush=True)
    
    
def welcome():
    """ This is the welcome message that is displayed at the beginning of the program."""
    print(flush=True)
    print("##  You are using the Forecast Search Wizard: a NOAA Archive Text Product Keyword Finder program. ", flush=True)
    print(flush=True)
    print("##  This is an independently developed program by Eric Allen - All Rights Reserved.", flush=True)
    print("##  Please cite: 'Allen, E., 2019: Forecast Search Wizard: A Tool to Search NOAA Text-Forecasts. Poster, Weather\n\t\t\tAnalysis and Forecasting, 44th Annual National Weather Association Meeting, Huntsville,\n\t\t\tAlabama, 10 September 2019.'  " , flush=True) ## TODO UPDATE DOI
    print(flush=True)
    print(flush=True)
    print(flush=True)