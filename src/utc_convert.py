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
import datetime
import pytz

def utc_convert_reformat_time(time,timezone):   
    """ Alternative: Converts date/time information to UTC time given the specified or implied time zone.

    Parameters:
        time (str): Time - str(YYYYmmddHHMM)
        timezone (str): Timezone string name - As required by Pytz for supported TZs
        
    Returns:
        utc_dt (datetime tuple): Datetime tuple with timezone info
    """
    strTime = str(time)
    fmtString = "%m-%d-%Y %H:%M"
    strYear = strTime[0:4]; strMonth = strTime[4:6];
    stringDay = strTime[6:8];
    strHour = strTime[8:10]; strMinute = strTime[10:12];
    zone = timezone

    try:
        # Puts it in a datetime tuple
        dt_str = datetime.datetime(int(strYear),int(strMonth),\
                                int(stringDay),int(strHour),int(strMinute))
        # Formats the date to a text string
        fmtDate=dt_str.strftime(fmtString)
        # Gets the datetime tuple again
        naive = datetime.datetime.strptime(fmtDate,fmtString)
        # What the computer originally thinks the time-zone info is (what it was given by tz_finder)
        local = pytz.timezone(zone)
        # Assign that timezone to the time and localize the time
        local_dt = local.localize(naive)
        # Assign the tuple a UTC time so convert it over to UTC from local tz
        utc_dt=local_dt.astimezone(pytz.utc)    
        # Everything worked and it's reformatted as dt tuple
        return utc_dt
    except:
        return None