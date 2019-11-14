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
import sys
from src.time_functions import get_Issuing_Time_text as get_time
from src.time_functions import get_Issuing_Date_text as get_date
from src.convert_time import convert_time
from src.check_everything import checkEverything
import pytz

FMT_STRING = "%m-%d-%Y %H:%M"

def wfo_rft_time(trim_times, unique_hrs, ddhhmm_list, wfo, unique_keywords, \
                 make_assume, iYear, timezone):
    """ The primary method will be used to attempt an extract of date and time
    information. If not possible then try the alternative method or print warnings.

    Parameters:
        trim_times (str): Raw date info
        unique_hrs (str): Raw time info
        unique_hrs (str): ddhhmm from top of the forecast
        wfo (str): Forecast product PIL
        unique_keywords (str): Keyword that was found
        make_assume (bool): Make assumptions
        iYear (int): The year of the file being searched. Used to help assume year
                            if missing/incomplete/typo.
        timezone (str): Timezone information associated with this instance (tz_finder)

    Returns:
        final_times_found (datetime tuple): A datetime tuple that has been converted to UTC.
        key_found (str):  The keyword that was found with any req. flags
    """

    #store successfully identified cases in this array
    times_found = [None] * len(trim_times)
    key_found = [None] * len(trim_times)
    count = 0
    replace_tz = max(((item, timezone.count(item)) for item in set(timezone)),\
                     key=lambda a: a[1])[0]

    if replace_tz == "" and "LSRNY" in wfo:
        replace_tz = "US/Eastern"

    #Loop through the times found list for keywords without duplicates
    for idx, times in enumerate(trim_times):
        try:
            major_assume = False
            minor_assume = False
            final_assume_time = False

            year, month, int_day, is_assumed_date = get_date(times, iYear, wfo, ddhhmm_list[idx])

            #NO MONTH INFORMATION AVAILABLE
            if is_assumed_date is None:
                if month is None:
                    print("TP: ", wfo, " - ERR NO MONTH FOUND... FATAL.  ", "??-", int_day,\
                          "-", year, " @", ddhhmm_list[idx], "Z  Check:",\
                          times.strip())
                    sys.stdout.flush()
                    continue
            elif is_assumed_date is True:
                if int_day is None and ddhhmm_list[idx] == "999999":
                    final_assume_time = True
                    print("TP: ", wfo, \
                          " - WMO Header Missing and MND Header Day Not Found. Exiting... "+\
                          "Check File:", iYear, " for  ", month, "-", "???", "-", year,\
                          " @", ddhhmm_list[idx], "Z", times.strip(), "   ", "___/",\
                          year, "/", iYear)
                    sys.stdout.flush()
                    continue

            #Missing Timezone Info
            if timezone[idx] == "":
                timezone[idx] = replace_tz

    # =============================================================================
    #       GET TIME INFO
    # =============================================================================
            MND_Header, is_assumed_time = get_time(unique_hrs[idx])

            #IF NEITHER _dd or int_day exists the program should quit above
            #If month is missing the program already quit
            #If year was missing and FSW guessed check_everything will look into it
            if ddhhmm_list[idx] != "999999":
                if int_day is None: #is_assumed_date == True
                    use_day = int(ddhhmm_list[idx][:2])
                    dt_tuple, is_assumed = checkEverything(MND_Header,\
                                ddhhmm_list[idx], year, month, use_day, iYear, timezone[idx])
                else:# is_assumed_time == False:
                    use_day = int_day
                    dt_tuple, is_assumed = checkEverything(MND_Header,\
                                    ddhhmm_list[idx], year, month, int_day, iYear, timezone[idx])
            # No DD HH MM - UTC
            else:
                if is_assumed_time is not None:
                    if int_day is not None:#is_assumed_date == True or False
                        if is_assumed_date:
                            final_assume_time = True
                        elif is_assumed_time:
                            final_assume_time = True

                        use_day = int_day
                        dt_tuple, is_assumed = checkEverything(MND_Header,\
                                          "999999", year, month, int_day, iYear, timezone[idx])
                    else:#is_assumed_date == None. No Day Info
                        print("TP: ", wfo, " - Time Information Could Not Be Found. "+\
                                  "(CONTINUING)... Check File:", iYear, " for  ", month, "-",\
                                  int_day,\
                                  "-", year, " @", ddhhmm_list[idx], "Z", times.strip())
                        sys.stdout.flush()
                        continue

                else:
                    print("TP: ", wfo, " - Time Information Could Not Be Found. "+\
                                  "[CONTINUING]... Check File:", iYear, " for  ", month, "-",\
                                  int_day,\
                                  "-", year, " @", ddhhmm_list[idx], "Z", times.strip())
                    sys.stdout.flush()
                    continue

            if is_assumed is not None:
                if is_assumed:
                    final_assume_time = True

                if dt_tuple.tzname() != "UTC":
                    final_time_string = dt_tuple.astimezone(pytz.timezone("UTC"))
                else:
                    final_time_string = dt_tuple
            else:
                if ddhhmm_list[idx] != "999999":
                    if is_assumed_date:
                        final_assume_time = True
                    final_time_string = convert_time(wfo, year, month, use_day,\
                                    int(ddhhmm_list[idx][2:4]), int(ddhhmm_list[idx][4:6]))
                else: #TRUE
                    if is_assumed_time:
                        final_assume_time = True
                    final_time_string = convert_time(wfo, year, month, use_day,\
                                    int(MND_Header[:2]), int(MND_Header[2:]),\
                                    timezone=timezone[idx])


            if final_time_string.day != use_day:
                try:
                    test_time_string = convert_time(wfo, year, month, use_day,\
                                                    int(MND_Header[:2]), int(MND_Header[2:]),\
                                                    timezone=timezone[idx], s='silence')
                    tots = (test_time_string - final_time_string).total_seconds()
                    difference_time = abs(tots/(60*60))
                except:
                    difference_time = 0 #Cannot resolve
            else:
                difference_time = 0 #Close enough - might lose a few minor assumption
                # this is because we are using use_day and not the converted day.

            if final_assume_time:
                major_assume = True
            else:
                if difference_time <= 2:
                    pass
                elif difference_time < 36:
                    minor_assume = True
                    #print("TP: minor discrepancy - : ", final_time_string.strftime(FMT_STRING),\
                    #       is_assumed, "\t /// \tOther: ", test_time_string.strftime(FMT_STRING),\
                    #"\t+++",\
                    #       "{:4.2f}".format(difference_time), "++++","\t", times.strip(), "\t",\
                    #       unique_hrs[idx].strip(), " DEFAULT - Day: ", _dd, " - Hour: ", _hh,\
                    #       " - Minute: ", _mm, "  UTC")
                    #sys.stdout.flush()
                else:
                    major_assume = True
                    print("TP: MAJOR DISCREPANCY - Using: ",\
                          final_time_string.strftime(FMT_STRING), \
                          "  ///  Other: ", test_time_string.strftime(FMT_STRING), "\t+++",\
                          "{:4.2f}".format(difference_time), "++++",\
                          "\t", times.strip(),\
                          "\t", unique_hrs[idx].strip(), " WMO - Day: ", ddhhmm_list[idx][0:2],\
                          " - Hour: ", ddhhmm_list[idx][2:4], " - Minute: ",\
                          ddhhmm_list[idx][4:6], "  UTC")
                    sys.stdout.flush()

            if final_time_string is not None:
                if make_assume:
                    times_found[count] = final_time_string
                    if major_assume or minor_assume:
                        if major_assume:
                            unique_keywords[idx] = unique_keywords[idx]+"*"
                            key_found[count] = unique_keywords[idx]+"*"
                        if minor_assume:
                            unique_keywords[idx] = unique_keywords[idx]+"#"
                            key_found[count] = unique_keywords[idx]+"#"
                    else:
                        key_found[count] = unique_keywords[idx]

                else:
                    if not major_assume and not minor_assume:
                        times_found[count] = final_time_string
                        key_found[count] = unique_keywords[idx]

                #increase the count by 1 after the iteration
                count += 1
        except:
            print("TP: Unknown - Exception Thrown. Continuing without the time in question.",\
                  times, unique_hrs[idx], ddhhmm_list[idx], wfo,\
                  unique_keywords[idx], iYear, timezone[idx])
            sys.stdout.flush()
            continue

    #Trim down to the size actually used
    final_times_found = times_found[:count]
    key_found = unique_keywords[:count]

    #return the formatted times found
    return final_times_found, key_found
