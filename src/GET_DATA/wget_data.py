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
# The user is responsible for following the terms to use Iowa Environmental Mesonet Data
#  - Educational use only.... Advancing the sciences
#  - Not recommended for operational purposes
#
# Imports
from __future__ import print_function
import os
import sys
import src.GET_DATA.wget as wget

#This program could be broken if something changes on Iowa Environmental Mesonet's end
def get_data(lst, start, end):
    """ Retrieves the data from IEM. Requires the wget script that I have packaged (techtonik)

    Parameters:
        lst (list)  = a list of string forecast PILs
        start (int) = first year of data
        end (int)   = last year of data

    Returns:
        A directory full of sub-directories. Each subdirectory consists of a
        forecast product and each years archive using a standardized naming practice
    """

    # Parent Data Directory
    root_path = os.path.abspath('../')
    data_dir = os.path.join(root_path, "TEXT_DATA")

    #To my knowledge all should be upper-case when calling from IEM
    lst2 = list(map(str.upper, lst))

    print("\n\nData being stored to: " + data_dir + "\n\n")
    sys.stdout.flush()

    # For forecast product
    for awips_id in lst2:

        print(awips_id)
        sys.stdout.flush()

        # For year in product history
        for year in range(start, end+1):

            # End of year range
            nextyear = year + 1

            # Output directory - standardized format
            outdir = os.path.join(data_dir, awips_id)

            # If the directory doesn't exist, make it
            if not os.path.exists(outdir):
                os.makedirs(outdir)

            # Url to get the data
            get_file = "https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?fmt=text&"+\
                "pil="+str(awips_id)+"&center=&limit=9999&sdate="+str(year)+"-01-01&edate="+\
                str(nextyear)+"-01-01"

            # Output file name
            fname = awips_id +"_"+str(year)+".txt"
            outfile = os.path.join(outdir, fname)

            # Don't overwrite an existing file
            try:
                os.remove(outfile)
            except OSError:
                pass

            # Get the data
            wget.download(get_file, outfile)

            #Inform user that the file is less than 50 bytes and likely empty.
            # After checking, keep regardlessly
            if os.stat(outfile).st_size < 50: #bytes
                print("Empty File: " + outfile)
                sys.stdout.flush()

    return data_dir
