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
import sys, os
import time, datetime
import signal
import getpass
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.trimwarnings import trim_warnings
from src.print_search_info import final_message
from src.finder import AFD_finder

class TimeoutException(Exception):   # Custom exception class
    pass

class UnicodeException(Exception):
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException
        
def execute(FSW_SEARCH): 
    """ Executes the Forecast Search Wizard... Only if it passes the checks in Setup.py
    
    Parameters:
        FSW_SEARCH (Dictionary): Contains search specifications
    """           
    start_time = time.time()

    run_start_time = datetime.datetime.today().strftime('%y%m%d_%H%M')
    wfname = run_start_time+"_"+FSW_SEARCH['KEYWORD_LIST'][0][:9]+"_"+str(len(FSW_SEARCH['STATION_LIST']))+"_"+getpass.getuser()+"_errors.txt"
    warningfile = os.path.join(FSW_SEARCH['WARNING_PATH'],wfname)


    if FSW_SEARCH['debug_mode'] == False:
        f = sys.stdout
        sys.stdout = open(warningfile, 'w')
        # Change the behavior of SIGALRM
        signal.signal(signal.SIGALRM, timeout_handler)
        # Start the timer. Once time is up, a SIGALRM signal is sent.
        ADMIN_MAX_HOURS = 6
        signal.alarm(ADMIN_MAX_HOURS*3600)
    
        print()
        # This try/except loop ensures that you'll catch TimeoutException when it happens. 
        try:
            AFD_finder(FSW_SEARCH, run_start_time)
        except TimeoutException:
            print("The search was limited to 6 hours. No search should take more than 6 hours at this time.")
            print("If second run yields the same problem. Try narrowing your search and/or contact: allenea@udel.edu")
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            # close the file
            sys.stdout.close()
            sys.stdout = f
        
        #? Is it needed or what happened that one time. I think it was a computer thing and not the code....
        except UnicodeEncodeError:
            print("Failed UnicodeEncodeError... Possibly caused by a corrupt file.")
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            #close the files
            f.close()
            sys.stdout.close()
            sys.stdout = f

        except:       # ALL OTHER EXCEPTIONS  
            print("Program Failed To Run To Completion. Please alert allenea@udel.edu to identify the problem and fix it.")
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            #close the files
            f.close()
            sys.stdout.close()
            sys.stdout = f
            
        else:
            # Reset the alarm
            signal.alarm(0)
            #write error outputs then write the statistics to the file at the end.
            final_message()
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            # close the file
            sys.stdout.close()
            sys.stdout = f
    
        ## Remove duplicate consecutive warnings from the verbose output file
        trim_warnings(warningfile)
         
    else:
        ## DEBUG MODE: YOU WILL SEE THE ERRORS IN CMD LINE
        AFD_finder(FSW_SEARCH, run_start_time)
