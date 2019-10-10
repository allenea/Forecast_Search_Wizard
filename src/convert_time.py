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
import datetime, pytz

"""
TO SEE VALID PYTZ TIMEZONES

for tz in pytz.all_timezones:
    print(tz)
    
"""

def convert_time(year, month, day, hour, minute, timezone="UTC"):   
    """Converts date/time information to UTC time given the specified or implied time zone.

    If you are in UTC time function call without timezone="UTC"
    
    Parameters:
        year (int)
        month (int)
        day (int)
        hour (int)
        minute (int) 
        timezone (str): Timezone string name - As required by Pytz for supported TZs
        
    Returns:
        utc_dt (datetime tuple): Datetime tuple with timezone info
    """
    fmtString = "%m-%d-%Y %H:%M"
    try:
        dt = datetime.datetime(int(year),int(month), int(day),int(hour),int(minute)) ## RAISE VALUE_ERROR -> RETURN NONE
        local = pytz.timezone(timezone) #RAISE TIMEZONE_ERROR -> RETURN NONE
    except:
        return None
    
    # Formats the date to a text string
    fmtDate=dt.strftime(fmtString)
    # Gets the datetime tuple again
    naive = datetime.datetime.strptime(fmtDate,fmtString)
    # What the computer originally thinks the time-zone info is (what it was given by tz_finder)
    # Assign that timezone to the time and localize the time
    local_dt = local.localize(naive)
    # Assign the tuple a UTC time so convert it over to UTC from local tz
    utc_dt=local_dt.astimezone(pytz.utc)    
    # Everything worked and it's reformatted as dt tuple
    return utc_dt