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
import sys
import os
#from datetime import datetime, timezone
#import pytz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.check_everything import checkEverything

def test_check_everything():
    """Trust the text whenever possible"""
    #REGULAR
    assert checkEverything("310623", "", 2018, 6, 31, 2018) == (2018, 6, 31, "06", "23", False)
    assert checkEverything("310623", "", 2018, 12, 31, 2018) == (2018, 12, 31, "06", "23", False)
    assert checkEverything("010623", "", 2018, 1, 1, 2018) == (2018, 1, 1, "06", "23", False)
    assert checkEverything("010623", "", 2018, 12, 31, 2018) == (2019, 1, 1, "06", "23", False)
    assert checkEverything("310623", "", 2019, 1, 1, 2019) == (2018, 12, 31, "06", "23", False)

    ## DECEMBER TO JANUARY
    #Go forward a day to Jan 1 from last day of DEC. no year change IEM
    assert checkEverything("010623", "", 2018, 12, 31, 2018) == (2019, 1, 1, "06", "23", False)
    assert checkEverything("010623", "", 1995, 12, 31, 1995) == (1996, 1, 1, "06", "23", False)
    #Go forward a day to Jan 1 from last day of DEC. +1 year change IEM
    assert checkEverything("010623", "", 2018, 12, 31, 2019) == (2019, 1, 1, "06", "23", False)
    #Go forward a day to Jan 1 from last day of DEC. -1 year IEM plus move to next year
    assert checkEverything("010623", "", 2018, 12, 31, 2017) == (2019, 1, 1, "06", "23", True)
    #Go forward a day to Jan 1 from last day of DEC.
    assert checkEverything("010623", "", 2019, 12, 31, 2018) == (2020, 1, 1, "06", "23", True)
    assert checkEverything("010623", "", 2017, 12, 31, 2018) == (2018, 1, 1, "06", "23", False)
    #Go forward a day to Jan 1 from last day of DEC. +2 year IEM plus move to next year so +1
    assert checkEverything("010623", "", 2016, 12, 31, 2018) == (2017, 1, 1, "06", "23", False)
    assert checkEverything("010623", "", 2018, 12, 31, 2016) == (2019, 1, 1, "06", "23", True)
    assert checkEverything("010623", "", 1995, 12, 31, 1990) == (1996, 1, 1, "06", "23", True)

    #JANUARY BACK TO DECEMBER
    #Go backwards a day from Jan 1 to last day of DEC. no year change IEM
    assert checkEverything("310623", "", 2018, 1, 1, 2018) == (2017, 12, 31, "06", "23", False)
    #Go backwards a day from Jan 1 to last day of DEC. +1 year change IEM
    assert checkEverything("310623", "", 2018, 1, 1, 2019) == (2017, 12, 31, "06", "23", True)
    #Go backwards a day from Jan 1 to last day of DEC. -1 year IEM plus move to next yr
    assert checkEverything("310623", "", 2018, 1, 1, 2017) == (2017, 12, 31, "06", "23", False)
    #Go backwards a day from Jan 1 to last day of DEC. -1 year change IEM
    assert checkEverything("310623", "", 2019, 1, 1, 2018) == (2018, 12, 31, "06", "23", False)
    #Go backwards a day from Jan 1 to last day of DEC. +1 year IEM plus move to next YR
    assert checkEverything("310623", "", 2017, 1, 1, 2018) == (2016, 12, 31, "06", "23", True)

    assert checkEverything("310623", "", 1995, 1, 1, 1995) == (1994, 12, 31, "06", "23", False)
    assert checkEverything("310623", "", 2016, 1, 1, 2018) == (2015, 12, 31, "06", "23", True)
    assert checkEverything("310623", "", 2018, 1, 1, 2016) == (2017, 12, 31, "06", "23", False)
    assert checkEverything("310623", "", 1993, 1, 1, 1995) == (1992, 12, 31, "06", "23", True)
    assert checkEverything("310623", "", 1996, 1, 1, 1993) == (1995, 12, 31, "06", "23", True)

    #MID-YEAR - COMMENTS GO WITH TEST ABOVE
    assert checkEverything("310623", "", 2018, 7, 1, 2018) == (2018, 6, 31, "06", "23", False)
    assert checkEverything("310623", "", 2018, 4, 1, 2019) == (None, None, None, None, None, None)
    assert checkEverything("310623", "", 2018, 7, 1, 2017) == (None, None, None, None, None, None)
    assert checkEverything("310623", "", 2019, 8, 1, 2018) == (None, None, None, None, None, None)
    assert checkEverything("310623", "", 2017, 7, 1, 2018) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 2018, 6, 31, 2018) == (2018, 7, 1, "06", "23", False)
    assert checkEverything("010623", "", 2018, 9, 31, 2019) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 2018, 6, 31, 2017) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 2019, 10, 31, 2018) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 2017, 6, 31, 2018) == (None, None, None, None, None, None)

    #MID-YEAR NOT END-TO-START or START-TO-END
    assert checkEverything("010623", "", 2016, 6, 31, 2018) == (None, None, None, None, None, None)
    # clearly the wrong month...
    assert checkEverything("300623", "", 2018, 2, 28, 2018) == (None, None, None, None, None, None)

    assert checkEverything("010623", "", 2017, 6, 31, 2018) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 2018, 6, 31, 2017) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 1995, 6, 31, 1994) == (None, None, None, None, None, None)

    assert checkEverything("010623", "", 2018, 6, 27, 2018) == (None, None, None, None, None, None)
    assert checkEverything("020623", "", 2018, 6, 31, 2018) == (None, None, None, None, None, None)
    assert checkEverything("010623", "", 2018, 6, 3, 2018) == (None, None, None, None, None, None)
    assert checkEverything("020623", "", 2018, 6, 10, 2018) == (None, None, None, None, None, None)
    assert checkEverything("110623", "", 2018, 6, 8, 2018) == (None, None, None, None, None, None)
    assert checkEverything("090623", "", 2018, 6, 2, 2018) == (None, None, None, None, None, None)

    # iYear/Year don't matchs - DON'T RESOLVE
    assert checkEverything("120623", "", 2017, 12, 12, 2019) == (None, None, None, None, None, None)
    assert checkEverything("050623", "", 2001, 1, 5, 2003) == (None, None, None, None, None, None)

    assert checkEverything("120623", "", 2019, 12, 12, 2017) == (None, None, None, None, None, None)
    assert checkEverything("050623", "", 2003, 1, 5, 2001) == (None, None, None, None, None, None)

    # SHOULD NEVER GET TO HERE....
    assert checkEverything("120623", "", 2017, 12, 12, 2018) == (2017, 12, 12, "06", "23", False)
    assert checkEverything("050623", "", 2001, 1, 5, 2002) == (2002, 1, 5, "06", "23", False)

    assert checkEverything("120623", "", 2018, 12, 12, 2017) == (2017, 12, 12, "06", "23", False)
    assert checkEverything("050623", "", 2002, 1, 5, 2001) == (2002, 1, 5, "06", "23", False)

    assert checkEverything("310623", "", 2017, 6, 31, 2018) == (None, None, None, None, None, None)
    assert checkEverything("310623", "", 2001, 6, 31, 2002) == (None, None, None, None, None, None)

    assert checkEverything("310623", "", 2017, 6, 31, 2018) == (None, None, None, None, None, None)
    assert checkEverything("310623", "", 2001, 6, 31, 2002) == (None, None, None, None, None, None)
