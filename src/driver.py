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
import signal
#import getpass
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.trimwarnings import trim_warnings
from src.print_search_info import final_message
from src.finder import AFD_finder

class TimeoutException(Exception):
    """Custom exception class"""
    #pass

def timeout_handler(signum, frame):
    """Custom signal handler"""
    raise TimeoutException

def execute(FSW_SEARCH, filen=sys.stdout):
    """ Executes the Forecast Search Wizard... Only if it passes the checks in Setup.py

    Parameters:
        FSW_SEARCH (Dictionary): Contains search specifications

        filen=sys.stdout --> your console reference point which you are about to change
                                to the WARNING_FILE if you are working in debug mode.
    """
    start_time = time.time()

    if not FSW_SEARCH['debug_mode']:
            
        if FSW_SEARCH['bulk_search']:
            sys.stdout = open(FSW_SEARCH['WARNING_FILE'], 'a+')
        else:
            sys.stdout = open(FSW_SEARCH['WARNING_FILE'], 'w')

        # Change the behavior of SIGALRM
        signal.signal(signal.SIGALRM, timeout_handler)

        # Start the timer. Once time is up, a SIGALRM signal is sent.
        admin_max_hours = 6
        signal.alarm(admin_max_hours*3600)

        # This try/except loop ensures that you'll catch TimeoutException when it happens.
        try:
            outfile = AFD_finder(FSW_SEARCH)

        except TimeoutException:
            print("Program Failed To Run due to (6-hour) TimeoutException..."+\
                  " Even poorly configured searches should take less than 6 hours.")
            print("If second run yields the same problem. Try narrowing your search"+\
                  " and/or contact: allenea@udel.edu")
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            # close the file
            sys.stdout.close()
            sys.stdout = filen
            sys.exit("TIMEOUT ERROR...")

        #RARE - REDOWNLOAD DATA OR CORRUPT DATA
        except UnicodeEncodeError:
            print("Program Failed on UnicodeEncodeError... Possibly caused by a corrupt file.")
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            #close the files
            sys.stdout.close()
            sys.stdout = filen
            sys.exit("UNICODE ENCODE ERROR...")

        # ALL OTHER EXCEPTIONS
        except:
            print("Program Failed To Run To Completion..."+\
                  " Please alert allenea@udel.edu to"+\
                  " identify the problem and fix it.")
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            #close the files
            sys.stdout.close()
            sys.stdout = filen
            sys.exit("ERROR...")

        else:
            # Reset the alarm
            signal.alarm(0)
            #write error outputs then write the statistics to the file at the end.
            final_message()
            print("--- %s seconds ---\n\n" % (time.time() - start_time))
            # close the file
            sys.stdout.close()
            sys.stdout = filen

        ## Remove duplicate consecutive warnings from the verbose output file
        if not FSW_SEARCH['bulk_search']:
            trim_warnings(FSW_SEARCH['WARNING_FILE'])
    else:
        ## DEBUG MODE: YOU WILL SEE THE ERRORS IN CMD LINE
        outfile = AFD_finder(FSW_SEARCH)

    return outfile
