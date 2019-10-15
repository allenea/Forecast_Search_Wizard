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
from __future__ import print_function
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.print_search_info import data_acknowledgement
from search_options.search_options import Option ## IF you want to provide the MASTER_LIST with one of the preset options.

def main():
    """ This program serves as the "NAMELIST" which provides options that the user can input to configure his search dataset."""
    # 1. Do you want to download the data? 
        # This could take up considerable space on your computer. Expect 30-50GB for the exhausitve archive.
    Download_Data = True
    
    # 2. Download only the latest year. 
        # Should be run whenever analyzing the current and fullest extent of the records... 
        # Switch to True after the initial dataset has been downloaded to maintain the dataset.
    Get_Latest_Year = True
    
    # 3. Remove and identify PIL (forecast codes) with no data history (from start - end... empty files). You will be notified. 
    Remove_Empty = True
    
    # 4. The first year of the desired dataset
    start_year = int(1996) # 1996 is the earliest data in the IEM database 

    # 5. The final year of the desired dataset (to include that year)
    end_year = int(time.ctime()[-4:]) ## CURRENT YEAR
    
    # 6. The List of PILs for the NWS text products. Alt. provide it a preset option from the search_options class.
    MASTER_LIST = ["AFDLWX","AFDPHI"]
    
    ## Remove the 3- " in ther row below and at the end of the master list (green?) -  FOR FULL DATASET
    """
    MASTER_LIST = ['AFDABQ', 'AFDABR', 'AFDAFC', 'AFDAFG', 'AFDAJK', 'AFDAKQ', 'AFDALY', 'AFDAMA', 'AFDAPX', 'AFDARX',
			  'AFDBGM', 'AFDBIS', 'AFDBMX', 'AFDBOI', 'AFDBOU', 'AFDBOX', 'AFDBRO', 'AFDBTV', 'AFDBUF', 'AFDBYZ',
			  'AFDCAE', 'AFDCAR', 'AFDCHS', 'AFDCLE', 'AFDCRP', 'AFDCTP', 'AFDCYS', 'AFDDDC', 'AFDDLH', 'AFDDMX',
			  'AFDDPQ', 'AFDDTX', 'AFDDVN', 'AFDEAX', 'AFDEKA', 'AFDEPZ', 'AFDEWX', 'AFDEYW', 'AFDFFC', 'AFDFGF',
			  'AFDFGZ', 'AFDFSD', 'AFDFWD', 'AFDGGW', 'AFDGID', 'AFDGJT', 'AFDGLD', 'AFDGRB', 'AFDGRR', 'AFDGSP',
			  'AFDGYX', 'AFDHFO', 'AFDHGX', 'AFDHNX', 'AFDHUN', 'AFDICT', 'AFDILM', 'AFDILN', 'AFDILX', 'AFDIND',
			  'AFDIWX', 'AFDJAN', 'AFDJAX', 'AFDJKL', 'AFDKEY', 'AFDLBF', 'AFDLCH', 'AFDLIX', 'AFDLKN', 'AFDLMK',
              'AFDLOT',  'AFDLOX', 'AFDLSX', 'AFDLUB', 'AFDLWX', 'AFDLZK', 'AFDMAF', 'AFDMEG', 'AFDMFL', 'AFDMFR',
              'AFDMHX', 'AFDMKX', 'AFDMLB', 'AFDMOB', 'AFDMPX', 'AFDMQT', 'AFDMRX', 'AFDMSO', 'AFDMTR', 'AFDOAX', 'AFDOHX',
              'AFDOKX', 'AFDOTX', 'AFDOUN', 'AFDPAH', 'AFDPBZ', 'AFDPDT', 'AFDPHI', 'AFDPIH', 'AFDPPG', 'AFDPQ', 'AFDPQR',
              'AFDPSR', 'AFDPUB', 'AFDRAH', 'AFDREV', 'AFDRIW', 'AFDRLX', 'AFDRNK', 'AFDSDF', 'AFDSEW', 'AFDSGF', 'AFDSGX',
              'AFDSHV', 'AFDSJT', 'AFDSJU', 'AFDSLC', 'AFDSTO', 'AFDTAE', 'AFDTBW', 'AFDTFX', 'AFDTOP', 'AFDTSA', 'AFDTWC', 
              'AFDUNR', 'AFDVEF', 'ALTK04', 'ALTK05', 'ALTK06', 'ALTK07', 'ALTK08', 'ALTK09', 'DAYDIS', 'DAYDSF', 'DAYTDF',
              'FFALWX', 'FFAPHI', 'FFGMPD', 'FFSLWX', 'FFSPHI', 'FFWLWX', 'FFWPHI', 'FLSLWX', 'FLSPHI', 'FLWLWX', 'FLWPHI', 
              'FWDD38', 'FWDDY1', 'FWDDY2', 'HSFAT1', 'HSFAT2', 'HSFEP', 'HSFEP1', 'HSFEP2', 'HSFEP3', 'HSFEPI', 'HSFNP', 
              'HSFSP', 'HWOLWX', 'HWOPHI', 'LSRABQ', 'LSRABR', 'LSRAFC', 'LSRAFG', 'LSRAJK', 'LSRAKQ', 'LSRALY', 'LSRAMA', 
              'LSRAPX', 'LSRARX', 'LSRBGM', 'LSRBIS', 'LSRBMX', 'LSRBOI', 'LSRBOU', 'LSRBOX', 'LSRBRO', 'LSRBRW', 'LSRBTV',
              'LSRBUF', 'LSRBYZ', 'LSRCAE', 'LSRCAR', 'LSRCDB', 'LSRCHS', 'LSRCLE', 'LSRCRP', 'LSRCTP', 'LSRCYS', 'LSRDDC',
              'LSRDLH', 'LSRDMX', 'LSRDTX', 'LSRDVN', 'LSREAX', 'LSREKA', 'LSREPZ', 'LSREWX', 'LSRFFC', 'LSRFGF', 'LSRFGZ',
              'LSRFSD', 'LSRFWD', 'LSRGGW', 'LSRGID', 'LSRGJT', 'LSRGLD', 'LSRGRB', 'LSRGRR', 'LSRGSP', 'LSRGUM', 'LSRGYX',
              'LSRHFO', 'LSRHGX', 'LSRHNX', 'LSRHUN', 'LSRICT', 'LSRILM', 'LSRILN', 'LSRILX', 'LSRIND', 'LSRISN', 'LSRIWX',
              'LSRJAN', 'LSRJAX', 'LSRJKL', 'LSRKEY', 'LSRLBF', 'LSRLCH', 'LSRLIX', 'LSRLKN', 'LSRLMK', 'LSRLOT', 'LSRLOX',
              'LSRLSX', 'LSRLUB', 'LSRLWX', 'LSRLZK', 'LSRMAF', 'LSRMEG', 'LSRMFL', 'LSRMFR', 'LSRMHX', 'LSRMKX', 'LSRMLB',
              'LSRMOB', 'LSRMPX', 'LSRMQT', 'LSRMRX', 'LSRMSO', 'LSRMTR', 'LSRNY1', 'LSRNY2', 'LSRNY3', 'LSRNY4', 'LSRNY7',
              'LSROAX', 'LSROHX', 'LSROKX', 'LSROTX', 'LSROUN', 'LSRPAH', 'LSRPBZ', 'LSRPDT', 'LSRPHI', 'LSRPIH', 'LSRPQR',
              'LSRPSR',  'LSRPUB', 'LSRRAH', 'LSRREV', 'LSRRIW', 'LSRRLX', 'LSRRNK', 'LSRSEW', 'LSRSGF', 'LSRSGX', 'LSRSHV',
              'LSRSJT', 'LSRSJU', 'LSRSLC', 'LSRSTO', 'LSRTAE', 'LSRTBW', 'LSRTFX', 'LSRTOP', 'LSRTSA', 'LSRTWC', 'LSRUNR',
              'LSRVEF', 'LSRVWS', 'MIMATN', 'MIMATS', 'MIMPAC', 'NOWABQ', 'NOWABR', 'NOWADQ', 'NOWAFC', 'NOWAFG', 'NOWAJK',
              'NOWAKN', 'NOWAKQ', 'NOWALY', 'NOWAMA', 'NOWANN', 'NOWAPX', 'NOWARX', 'NOWBET', 'NOWBGM', 'NOWBIS', 'NOWBMX',
              'NOWBOI', 'NOWBOU', 'NOWBOX', 'NOWBRO', 'NOWBRW', 'NOWBTV', 'NOWBUF', 'NOWBYZ', 'NOWCAE', 'NOWCAR', 'NOWCDB',
              'NOWCHS', 'NOWCLE', 'NOWCRP', 'NOWCTP', 'NOWCYS', 'NOWDDC', 'NOWDLH', 'NOWDMX', 'NOWDTX', 'NOWDVN', 'NOWEAX',
              'NOWEKA', 'NOWEPZ', 'NOWEWX', 'NOWEYW', 'NOWFFC', 'NOWFGF', 'NOWFGZ', 'NOWFSD', 'NOWFWD', 'NOWGGW', 'NOWGID',
              'NOWGJT', 'NOWGLD', 'NOWGRB', 'NOWGRR', 'NOWGSP', 'NOWGYX', 'NOWHFO', 'NOWHGX', 'NOWHNX', 'NOWHUN', 'NOWICT',
              'NOWILM', 'NOWILN', 'NOWILX', 'NOWIND', 'NOWISN', 'NOWIWX', 'NOWJAN', 'NOWJAX', 'NOWJKL', 'NOWKEY', 'NOWLBF',
              'NOWLCH', 'NOWLIX', 'NOWLKN', 'NOWLMK', 'NOWLOT', 'NOWLOX', 'NOWLSX', 'NOWLUB', 'NOWLWX', 'NOWLZK', 'NOWMAF',
              'NOWMCG', 'NOWMEG', 'NOWMFL', 'NOWMFR', 'NOWMHX', 'NOWMKX', 'NOWMLB', 'NOWMOB', 'NOWMPX', 'NOWMQT', 'NOWMRX',
              'NOWMSO', 'NOWMTR', 'NOWMY', 'NOWOAX', 'NOWOHX', 'NOWOKX', 'NOWOME', 'NOWOTX', 'NOWOTZ', 'NOWOUN', 'NOWPAH', 
              'NOWPBZ',  'NOWPDT', 'NOWPHI', 'NOWPIH', 'NOWPQR', 'NOWPSR', 'NOWPUB', 'NOWRAH', 'NOWREV', 'NOWRIW', 'NOWRLX',
              'NOWRNK', 'NOWSDF', 'NOWSEW', 'NOWSGF', 'NOWSGX', 'NOWSHV', 'NOWSJT', 'NOWSJU', 'NOWSLC', 'NOWSNP', 'NOWSTO', 
              'NOWTAE', 'NOWTBW', 'NOWTFX', 'NOWTOP', 'NOWTSA', 'NOWTWC', 'NOWUNR', 'NOWVEF', 'NOWVWS', 'NOWYAK', 'OFFAER', 
              'OFFAFG',  'OFFAJK', 'OFFALU', 'OFFHFO', 'OFFN01', 'OFFN02', 'OFFN03', 'OFFN04', 'OFFN05', 'OFFN06', 'OFFN07',
              'OFFN08', 'OFFN09', 'OFFN10', 'OFFN11', 'OFFN12', 'OFFN13', 'OFFN14', 'OFFN15', 'OFFNT1', 'OFFNT2', 'OFFNT3', 
              'OFFNT4', 'OFFPZ5', 'OFFPZ6', 'PMD30D', 'PMD90D', 'PMDAHU', 'PMDAK', 'PMDCA', 'PMDDRK', 'PMDDRO', 'PMDENS', 
              'PMDEPD',  'PMDEPH', 'PMDHCO', 'PMDHI', 'PMDHMD', 'PMDMRD', 'PMDSA', 'PMDSPD', 'PMDTHR', 'PNSLWX', 'PNSPHI',
              'QPFERD',  'QPFHSD', 'SCCNS1', 'SCCNS2', 'SCCNS3', 'SCCNS4', 'SCCNS5', 'SEL0', 'SEL1', 'SEL2', 'SEL3', 'SEL4',
              'SEL5', 'SEL6', 'SEL7', 'SEL8', 'SEL9', 'SMWLWX', 'SMWPHI', 'SVRLWX', 'SVRPHI', 'SVSLWX', 'SVSPHI', 'SWOD48',
              'SWODY1', 'SWODY2', 'SWODY3', 'SWOMCD', 'TCDAT1', 'TCDAT2', 'TCDAT3', 'TCDAT4', 'TCDAT5', 'TCDCP1', 'TCDCP2',
              'TCDCP3', 'TCDCP4', 'TCDCP5', 'TCDEP1', 'TCDEP2', 'TCDEP3', 'TCDEP4', 'TCDEP5', 'TCPAT1', 'TCPAT2', 'TCPAT3',
              'TCPAT4',  'TCPAT5', 'TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5', 'TCPEP1', 'TCPEP2', 'TCPEP3', 'TCPEP4',
              'TCPEP5', 'TCUAT', 'TCUAT1', 'TCUAT2', 'TCUAT3', 'TCUAT4', 'TCUAT5', 'TCUCP1', 'TCUCP2', 'TCUCP3', 'TCUCP4',
              'TCUCP5', 'TCUEP', 'TCUEP1', 'TCUEP2', 'TCUEP3', 'TCUEP4', 'TCUEP5', 'TORLWX', 'TORPHI', 'TWDAT', 'TWDEP',
              'WSWLWX', 'WSWPHI', "LSRADQ", "LSRAKN", "LSRANN", "LSRAT1", "LSRBA1", "LSRBET", "LSRBH1", "LSRBR1", "LSRCS1",
              "LSRHO1", "LSRJM1", "LSRMCG", "LSRNK1", "LSRNY5", "LSRNY6", "LSROME", "LSROTZ", "LSRPPG", "LSRSNP", "LSRTD1",
              "LSRYAK", "VOWLWX","VOWPHI"]
    """



##################  DO NOT TOUCH (BELOW) ##################
    # Path of the main functions
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from src.GET_DATA.wget_data import get_data
    from src.split_list import split_list
    from src.GET_DATA.CheckData import CheckRemove_Data
    
    #Redict messages to out file over the course of the download
    f = sys.stdout
    strTime = time.ctime().replace(" ","_")
    print("\n\nCheck: (", os.path.join(os.getcwd(),"Data_Download_Verbose"+strTime.replace(":","")+".out"),") to view the progress of the data download.")
    
    sys.stdout = open(os.path.join(os.getcwd(),"Data_Download_Verbose"+strTime.replace(":","")+".out"),'w')
    
    #Timer
    start_time = time.time()
    
    #Print Statements
    print("IEM Text-Data Retrieval is Powered by the Forecast Search Wizard\n")
    sys.stdout.flush()

    print(time.ctime())
    sys.stdout.flush()

    print("\nDownload Data? " + str(Download_Data))
    sys.stdout.flush()

    print("Get the Latest Year? " + str(Get_Latest_Year))
    if Get_Latest_Year == True:
        print("Start: " + str(end_year)+"\t\t End: "+str(end_year))
        sys.stdout.flush()
    else:
        print("Start: " + str(start_year)+"\t\t End: "+str(end_year))
        sys.stdout.flush()
    print("Sorting text products alphabetically...")
    sys.stdout.flush()

    #Sort the list
    MASTER_LIST.sort()
 
    #Neatly print out the list to the output file
    MASTER_SPLIT = split_list(MASTER_LIST,10)
    firstRow = True;
    for allen in range(len(MASTER_SPLIT)):
        MASTER_SPLIT[allen] = str(MASTER_SPLIT[allen]).replace("[", " ")
        MASTER_SPLIT[allen] = str(MASTER_SPLIT[allen]).replace("]", " ")
        if firstRow == False:
            print("\t\t\t", MASTER_SPLIT[allen])
            sys.stdout.flush()

        else:
            print("Forecast Products: ", MASTER_SPLIT[allen])
            sys.stdout.flush()
            firstRow = False
            
    if Get_Latest_Year == True and Download_Data == True: 
        data_dir = get_data(MASTER_LIST, end_year, end_year)
        pass
    elif Download_Data == True:
        data_dir = get_data(MASTER_LIST, start_year, end_year)
        pass
    else:
        print("Download Data was not set to true, therefore no data will be downloaded. Existing dataset will be preserved.")
        sys.stdout.flush()
        sys.exit(0)
    
    #If folder contains only empty files... do what file says. currently removes LSRs and VOW files but you can change that to what you want.
    if Remove_Empty == True:
        CheckRemove_Data(data_dir)
    else:
        pass
    
    #Print Lapse Time
    print("--- %s seconds ---"%(time.time() - start_time))
    sys.stdout.flush()
    data_acknowledgement()
    #Close log file
    sys.stdout.close()
    sys.stdout = f

#EXECUTE THIS
if __name__ == "__main__":  
    main()
##################  DO NOT TOUCH (ABOVE) ##################