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
from src.time_functions import getDDHHMM, getFirstGuess
from src.time_functions import get_Issuing_Time_text as get_time
from src.time_functions import get_Issuing_Date_text as get_date
from src.convert_time import convert_time
from datetime import datetime
from src.check_everything import checkEverything

FMT_STRING = "%m-%d-%Y %H:%M"

def wfo_rft_time(trim_times, unique_hrs, ddhhmm_list, wfo, unique_keywords, \
                 make_assume, iYear, timezone):
    """ The primary method will be used to attempt an extract of date and time
    information. If not possible then try the alternative method or print warnings.

    Parameters:
        trim_times (str): Raw date info
        unique_hrs (str): Raw time info
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
                    print("TP: ", wfo, " - WMO Header Missing and MND Header Day Not Found. Exiting... "+\
                          "Check File:", iYear, " for  ", month, "-", "???", "-", year,\
                          " @", ddhhmm_list[idx], "Z", times.strip(), "   ", "___/",\
                          year, "/", iYear)
                    sys.stdout.flush()
                    continue
                else:
                    #Missing Timezone Info
                    if timezone[idx] == "":
                        timezone[idx] = replace_tz
                        final_assume_time = True


            #Missing Timezone Info
            if timezone[idx] == "":
                timezone[idx] = replace_tz

    # =============================================================================
    #       GET TIME INFO
    # =============================================================================
            if ddhhmm_list[idx] != "999999":
                _dd, _hh, _mm = getDDHHMM(ddhhmm_list[idx])
                first_guess = getFirstGuess(year, month, _dd, _hh, _mm)
            else:
                first_guess = None

            MND_Header, WMO_Header, is_assumed_time = get_time(unique_hrs[idx],\
                                                                       first_guess, timezone[idx])

            if (MND_Header, WMO_Header, is_assumed_time) == (None, None, None):
                if ddhhmm_list[idx] == "999999":
                    print("TP: ", wfo, " - Time Information Could Not Be Found. "+\
                                  "CONTINUING... Check File:", iYear, " for  ", month, "-", int_day,\
                                  "-", year, " @", ddhhmm_list[idx], "Z", times.strip())
                    sys.stdout.flush()
                    continue
                else:
                    fyr, fmon, fday, fhr, fmin, isAssumed  = checkEverything(ddhhmm_list[idx],\
                          ddhhmm_list[idx], year, month, int_day, iYear)
                    if isAssumed == False:
                        final_time_string = convert_time(wfo, fyr, fmon, fday,\
                             int(fhr), int(fmin))
                    elif isAssumed: #None or True use pre-check
                        final_assume_time = True
                        final_time_string = convert_time(fyr, year, fmon, fday,\
                                        int(fhr), int(fmin))
                    else:
                        final_assume_time = True
                        final_time_string = convert_time(wfo, year, month, _dd,\
                            int(_hh), int(_mm))

            # USE MND HEADER - ASSUMPTION. FLAGGED
            elif WMO_Header is None:
                if is_assumed_time: #True
                    final_assume_time = True
                elif is_assumed_time == False:
                    pass

                LST = "{:02d}".format(int_day) + "{:02d}".format(int(MND_Header[:2]))+\
                        "{:02d}".format(int(MND_Header[2:]))

                fyr, fmon, fday, fhr, fmin, isAssumed  = checkEverything(LST,\
                                          ddhhmm_list[idx], year, month, int_day, iYear)

                if isAssumed == False:
                    final_time_string = convert_time(wfo, fyr, fmon, fday,\
                         int(fhr), int(fmin))
                elif isAssumed: #None or True use pre-check
                    final_assume_time = True
                    final_time_string = convert_time(fyr, year, fmon, fday,\
                                    int(fhr), int(fmin), timezone=timezone[idx])
                else:
                    final_assume_time = True
                    final_time_string = convert_time(wfo, year, month, int_day,\
                        int(MND_Header[:2]), int(MND_Header[2:]), timezone=timezone[idx])

            else: #WMO HEADER IS NOT NONE
                if int_day is None and ddhhmm_list[idx] != "999999":
                    use_day = _dd
                    LST = "{:02d}".format(_dd) +\
                            "{:02d}".format(int(WMO_Header[:2])) +\
                            "{:02d}".format(int(WMO_Header[2:]))
                    fyr, fmon, fday, fhr, fmin, isAssumed  = checkEverything(LST,\
                                 ddhhmm_list[idx], year, month, use_day, iYear)

                elif ddhhmm_list[idx] == "999999":
                    use_day = int_day
                    LST = "{:02d}".format(int_day) +\
                            "{:02d}".format(int(MND_Header[:2])) +\
                            "{:02d}".format(int(MND_Header[2:]))

                else:
                    use_day = int_day
                    LST = "{:02d}".format(int_day) +\
                            "{:02d}".format(int(WMO_Header[:2])) +\
                            "{:02d}".format(int(WMO_Header[2:]))
                    fyr, fmon, fday, fhr, fmin, isAssumed  = checkEverything(LST,\
                                 ddhhmm_list[idx], year, month, use_day, iYear)

                if isAssumed == False:
                    final_time_string = convert_time(wfo, fyr, fmon, fday,\
                         int(fhr), int(fmin))
                elif isAssumed:
                    if is_assumed_date == False:
                        final_time_string = convert_time(wfo, year, month, use_day,\
                                        int(MND_Header[:2]), int(MND_Header[2:]))
                    else: #TRUE
                        final_time_string = convert_time(wfo, year, month, use_day,\
                                        int(_hh), int(_mm))
                        final_assume_time = True
                else:
                    if is_assumed_time == True:
                        final_assume_time = True

                    final_time_string = convert_time(wfo, year, month, use_day,\
                                    int(WMO_Header[:2]), int(WMO_Header[2:]), timezone=timezone[idx])

            try:
                dt_lst = datetime.strptime(LST,"%d%H%M")
                test_time_string = convert_time(wfo, year, month, use_day, dt_lst.hour, dt_lst.minute, timezone=timezone[idx])
                difference_time = abs((test_time_string - final_time_string).total_seconds()/(60*60))

                if final_assume_time:
                    major_assume = True
                else:
                    if difference_time <= 1:
                        pass
                    elif 2 < difference_time <= 24:
                        #pass
                        minor_assume = True
                        #print("TP: minor discrepancy - : ", final_time_string.strftime(FMT_STRING),\
                        #       isAssumed, "\t /// \tOther: ", test_time_string.strftime(FMT_STRING), "\t+++",\
                        #       "{:4.2f}".format(difference_time), "++++","\t", times.strip(), "\t",\
                        #       unique_hrs[idx].strip(), " DEFAULT - Day: ", _dd, " - Hour: ", _hh,\
                        #       " - Minute: ", _mm, "  UTC")
                        #sys.stdout.flush()
                    else:
                        major_assume = True
                        print("TP: MAJOR DISCREPANCY - : ",\
                              final_time_string.strftime(FMT_STRING), isAssumed, \
                              "\t /// \tOther: ", test_time_string.strftime(FMT_STRING), "\t+++",\
                              "{:4.2f}".format(difference_time), "++++",\
                              "\t", times.strip(),\
                              "\t", unique_hrs[idx].strip(), " DEFAULT - Day: ", use_day,\
                              " - Hour: ", _hh, " - Minute: ", _mm, "  UTC")
                        sys.stdout.flush()#continue
            except:
                major_assume = True

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
                    if major_assume == False or minor_assume == False:
                        times_found[count] = final_time_string
                        key_found[count] = unique_keywords[idx]
                    else:
                        print("TP: BOMBASTIC ERROR", times, unique_hrs[idx], ddhhmm_list[idx],\
                              wfo, unique_keywords[idx], make_assume, iYear, timezone[idx])
                        sys.stdout.flush()

                #increase the count by 1 after the iteration
                count += 1

        except:
            print("TP: CATASTROPHIC ERROR", times, unique_hrs[idx], ddhhmm_list[idx],\
                  wfo, unique_keywords[idx], make_assume, iYear, timezone[idx])
            sys.stdout.flush()
            continue

    #Trim down to the size actually used
    final_times_found = times_found[:count]
    key_found = unique_keywords[:count]

    #return the formatted times found
    return final_times_found, key_found
