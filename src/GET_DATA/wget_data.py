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
# The user is responsible for following the terms to use Iowa Environmental Mesonet Data
#  - Educational use only.... Advancing the sciences
#  - Not recommended for operational purposes
#
# Imports
import os    
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
    data_dir = os.path.join(root_path,"TEXT_DATA")
    
    #To my knowledge all should be upper-case when calling from IEM
    lst2 = [x.upper() for x in lst]
    
    print("\n\nData being stored to: " + data_dir + "\n\n", flush=True)
    
    # For forecast product
    for AWIPS_ID in lst2:
        
        print(AWIPS_ID, flush=True)
        
        # For year in product history
        for year in range(start,end+1):
            
            # End of year range
            nextyear = year +1
            
            # Output directory - standardized format
            outdir = os.path.join(data_dir,AWIPS_ID)

            # If the directory doesn't exist, make it
            if not os.path.exists(outdir): os.makedirs(outdir)
    
            # Url to get the data
            getFile = "https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?fmt=text&pil="+str(AWIPS_ID)+"&center=&limit=9999&sdate="+str(year)+"0101&edate="+str(nextyear)+"0101"
            
            # Output file name
            fname = AWIPS_ID +"_"+str(year)+".txt" 
            outfile = os.path.join(outdir,fname)
            
            # Don't Overwrite an existing file
            try:
                os.remove(outfile)
            except OSError:
                pass
            
            # Get the data
            wget.download(getFile, outfile)
            
            # If the file is less than 50 bytes it's likely empty and missing data, so inform the user for their records.
            # After checking, keep regardlessly
            if os.stat(outfile).st_size < 50: #bytes
                print("Empty File: " + outfile, flush=True)
    return data_dir