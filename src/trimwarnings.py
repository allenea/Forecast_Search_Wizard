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
import os

def trim_warnings(warningfile):
    """ Trims down the files to save space and remove duplicate warnings.

    Parameters:
        warningfile (str):The string filename and path for the file with the logged messages.

    Returns:
        trim_warn_file (str1):The trimmed time removing duplicate warnings and errors for the same forecast.
    """
    #switch suffix
    trim_warn_file = warningfile.replace("_errors.txt","_errors_trm.txt")
    
    #open file and the new file
    f = open(warningfile,'r').readlines()
    outfile = open(trim_warn_file,'w')
    
    #constants
    be4Begin = False ; afterEnd = False
    countTP = 0; countTZ = 0; utc_convert = 0; countOther=0; countCR = 0; rowLast = "";
    
    #Iterate through file
    for row in f:
        #Begin Search marks the starting point
        if "Begin Search" in row and be4Begin==False:
            outfile.write("%s" % row)
            be4Begin = True
            
        elif afterEnd == True:
            outfile.write("%s" % row)
    
        elif "Begin Search" not in row and be4Begin==False:
             outfile.write("%s" % row)
        
        # Outputs once the search has begun
        elif "Begin Search" not in row and be4Begin == True:
            if row == "End Search":
                outfile.write("%s" % row)
                afterEnd = True
            else:
                if row.strip() == "":
                    outfile.write("%s" % row)
                elif row == rowLast:
                    continue
                else:
                    ## TODO UPDATE THESE FOR FINAL VERSION
                    if "ERROR CONVERTING" in row: # utc_convert.py
                        utc_convert +=1
                    elif "TP:" in row:
                        countTP +=1
                    elif "WARNING TZ_FINDER: " in row:
                        countTZ +=1
                    elif "WARNING TZ: " in row: # Guessing TZ if missing
                        countTZ +=1
                    elif "OTHER:" in row: #missing_time.py
                        countOther +=1
                    elif "FINDER:" in row: #finder.py
                        countCR +=1 
                        continue

                    outfile.write("%s" % row)
                    rowLast = row
                    
                    
    #Write some numbers   
    outfile.write("\nFINDER: Could Not Access An Expected Forecast: %d\n" % countCR)             
    outfile.write("TZ: Timezone Errors: %d\n" % countTZ)
    outfile.write("TP: Time Problem Errors: %d\n" % countTP)
    outfile.write("UTC Conversion Error: %d\n" % utc_convert)
    outfile.write("Other Issues: %d\n" % countOther)
    
    outfile.write("\n\n\n** LOGGING POSSIBLE FORECASTS NOT ACCESSIBLE **\n\n")
    
    be4Begin = False ; rowLast = "";
    for row in f:
        #Begin Search marks the starting point
        if "Begin Search" in row and be4Begin==False:
            be4Begin = True

        # Outputs once the search has begun
        elif "Begin Search" not in row and be4Begin == True:
            if row == "End Search":
                outfile.write("%s" % row)
            else:
                if row.strip() == "":
                    continue
                elif row == rowLast:
                    continue
                else:
                    if "FINDER:" in row:
                        outfile.write("%s" % row)
                        rowLast = row

    #Close file
    outfile.close()
    
    #Remove the long-version of the warning file
    os.remove(warningfile)
    
    #Return the trimmed warning file that removes duplicate consecutive warnings
    return trim_warn_file