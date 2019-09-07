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
from src.split_list import split_list
from __future__ import print_function

## DO NOT TOUCH... Formatted for aesthetic purposes.
def write_output_file(outputfile, inputKey, station_list, start,end, eTime, isGrep, andor,\
                 byforecast,makeAssume,keywordCounts,keywordCountsFINAL,num_days,prodsIssued,\
                 countDupFcst,total_mentions,no_dups,countBad,masterList,masterList2,masterList3):
    """ Writes the output file.

    Parameters:
        outputfile (str):Output file name
        inputKey (lst): List of strings - Keywords to be searchedd for
        station_list (lst): List of strings - Products to be searched
        searchSEClist (lst): None Type - Not Yet Implemented
        start (int): Start Year
        end (int): End Year
        eTime (float): Elapsed Time (seconds)
        andor (bool): Search for And (all) or Or (any) keywords
        byforecast (bool): Search by forecast or by day
        makeAssume (bool): Make assumptions for incomplete date/time info
        keywordCounts (int): Count total occurances of each keyword by Keyword
        keywordCountsFINAL (int): Count total occurances of each keyword in a Forecast (Forecast Frequency)
        num_days (int): Number of cases or days (depending on search type)
        prodsIssued (int): Total Products Searched (only searches if a keyword was used in that year).
        countDupFcst (int): Duplicate forecasts. Same Date and Time in header and prior forecast. 
        total_mentions (int): Sum of forecast frequency of each keyword
        no_dups (int): Total cases without duplicates 
        countBad (int): Something went wrong when a keyword was found (time zone or date/time)
        masterList (lst):  List of cases (date/time) info
        masterList2 (lst): List of WFO/Forecast product for each case
        masterList3 (lst): List of keywords found for each case

    Returns:
        outputfile (str1):Output file with data   
    """
# WRITE OUTPUT TO TEXT FILE
# =============================================================================   
    firstRow = True;# firstRowSEC = True;
    with open(outputfile, "w") as text_file:
        ## TODO UPDATE THIS
        text_file.write("This code was developed by Eric Allen. \n")
        text_file.write("~Acknowledge: Eric Allen and the Forecast Search Wizard in presentations and publications.~\n"+\
                        "Allen, E., 2019: Forecast Search Wizard: A Tool to Search NOAA Text-Forecasts. Poster, Weather Analysis and Forecasting,\n\t\t\t44th Annual National Weather Association Meeting, Huntsville, Alabama, 10 September 2019. \n\n")

# DO NOT TOUCH OUTPUT FORMATTING BELOW  
# =============================================================================           
        
        text_file.write("SEARCH CRITERIA:\n")
        text_file.write("----------------\n")

        text_file.write("\tYears Searched: "+str(start) + " - " + str(end)+"\n\n")
        
        if andor == True:
            if byforecast == True:
                text_file.write("\tSearched forecasts that use all keywords.\n\n")
            elif byforecast == False:
                text_file.write("\tSearched for days that use all keywords.\n\t\t* Results: Limited to the first forecast per day\n\n")
        elif andor == False:
            if byforecast == True:
                text_file.write("\tSearched for forecasts that use any of the keywords.\n\n")
            elif byforecast == False:
                text_file.write("\tSearched for days that use any of the keywords.\n\t\t* Results: Limited to the first forecast per day\n\n")
                
        if isGrep == True:
            text_file.write("\tThis is a GREP style search.\n")
            text_file.write("\t\t- See documentation for more information...\n\n")

        else:
            text_file.write("\tThis search is looking for whole words or phrases.\n")
            text_file.write("\t\t- See documentation for more information...\n\n")

                
        if makeAssume == True:
            text_file.write("\tThis search may make basic 'safe' assumptions for cases with incomplete date or time information.\n")
            text_file.write("\t\t- Any assumption made on whether the forecast was issued in the AM or PM will be indicated with a ' * '.\n")
            text_file.write("\t\t- Any assumption made on the date or time (year, month, day, hour, minute) will be indicated with a ' # '.\n")
            text_file.write("\t\t- See documentation for more information...\n\n")

        else:
            text_file.write("\tThis search makes no assumptions on incomplete date or time information.\n")
            text_file.write("\t\t- As a result, this search may not accurately account for all cases for this search criteria.\n")
            text_file.write("\t\t- The 'warnings_and_errors' output file can be used to manually add these cases.\n")
            text_file.write("\t\t- See documentation for more information... \n\n")

        #NOT IMPLEMENTED IN V3... List of SECTIONS being searched... For now the entire text product is searched.
        """if searchSEClist == None:
            text_file.write("\tSearched all sections of the forecast.\n\n")
        else:
            ## Search By Section
            print("THIS HAS NOT BEEN IMPLEMENTED YET!!")
            searchSEC_split_list = split_list(searchSEClist,4)
            for allen in range(len(searchSEC_split_list)):
                searchSEC_split_list[allen] = str(searchSEC_split_list[allen]).replace("[", " ")
                searchSEC_split_list[allen] = str(searchSEC_split_list[allen]).replace("]", " ")
                if firstRowSEC == False:
                    text_file.write("\t\t%s\n" % searchSEC_split_list[allen])
                else:
                    text_file.write("\tForecast Sections Searched:  \n\t\t%s\n" % searchSEC_split_list[allen])
                    firstRowSEC = False
        """            
                    
        #List of PRODUCTS being searched
        station_split_list = split_list(station_list,7)
        for eric in range(len(station_split_list)):
            station_split_list[eric] = str(station_split_list[eric]).replace("[", " ")
            station_split_list[eric] = str(station_split_list[eric]).replace("]", " ")
            if firstRow == False:
                text_file.write("\t\t%s\n" % station_split_list[eric])
            else: # If True it is the first row
                text_file.write("\tProducts Searched:  \n\t\t%s\n" % station_split_list[eric])
                firstRow = False
                
                
        text_file.write("\n\t%55s"%" Keyword"+"\t -%11s"%" Forecast"+"\n")
        text_file.write("\t%-43s"%"Keywords" + "-%11s"%" Frequency"+"\t -%11s"%"Frequency"+"\n")
        text_file.write("\t---------------------------------------------------------------------\n")
        for idx in range(len(inputKey)):
            text_file.write("\tKeyword "+str(idx+1)+":  %-30s" % inputKey[idx] +" - %10s"%str(keywordCounts[idx])+"\t - %10s"%str(keywordCountsFINAL[idx])+"\n")
        
        
        text_file.write("\nSEARCH RESULTS:\n")
        text_file.write("---------------\n")
        if byforecast == True:
            text_file.write("Total Cases Found:  %d\n\n" % num_days)
        elif byforecast == False:
            text_file.write("Total Cases Found:  %d\n\n" % num_days)
            
        text_file.write("Total Products Searched: %d\n"%prodsIssued)
        text_file.write("Duplicate Forecasts Issued: %d\n"%countDupFcst)
        text_file.write("Main-Search Elapsed Time: %f"%(eTime)+" seconds\n\n")

        if byforecast == True:
            text_file.write("Stats are limited to first instance of each keyword in the forecast:\n")
        elif byforecast == False:
            text_file.write("Stats are limited to first instance of each keyword for that day:\n")
        text_file.write("\tTotal Mentions:  %d\n" % total_mentions)        
        text_file.write("\tUnique Mentions: %d\n"  % no_dups)
        text_file.write("\tTimezone Errors: %d\n\n"  % countBad)
        
        ## This should be used to identify start of the dates when analyzing the outputs
        text_file.write("!!TIMES ARE IN UTC!!\n") 
    
        for idy, eachTime in enumerate(masterList):
            text_file.write("\n%s"%eachTime +"\t %s" % masterList2[idy]+"\t %s" % masterList3[idy])

    return outputfile