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
import os
import sys
import datetime
from datetime import timezone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.split_list import split_list
from src.tz_finder import timezone_finder
from src.differentiate import word_in_list_sym
from src.convert_time import convert_time


def test_split_list():
    """docstring"""

    lst1 = ["MIMPAC", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6",\
                      "HSFEP1", "HSFEP2", "HSFEPI", 'HSFNP']
    output1 = [['MIMPAC', 'OFFN07', 'OFFN08', 'OFFN09', 'OFFPZ5', 'OFFPZ6', 'HSFEP1'],\
         ['HSFEP2', 'HSFEPI', 'HSFNP']]

    assert split_list(lst1, 7) == output1

    lst2 = ["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU", "OFFN11", "OFFN12", \
            "OFFN13", "OFFN14", "OFFN15", "HSFEP3", "HSFSP", "OFFHFO", "OFFN10", \
               "HSFEPI", "HSFEP", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5", "OFFPZ6", \
               "HSFEP1", "MIMATN", "MIMATS", "OFFN01", "OFFN02", "OFFN03", \
               "OFFN04", "OFFN05", "OFFN06", "OFFNT1", "OFFNT2", "OFFNT3", "OFFNT4", \
               "HSFAT1", "HSFAT2", 'HSFEP2', 'HSFNP']

    output2 = [["MIMPAC", "OFFAER", "OFFAFG", "OFFAJK", "OFFALU"], \
               ["OFFN11", "OFFN12", "OFFN13", "OFFN14", "OFFN15"], \
               ["HSFEP3", "HSFSP", "OFFHFO", "OFFN10", "HSFEPI"], \
               ["HSFEP", "OFFN07", "OFFN08", "OFFN09", "OFFPZ5"], \
               ["OFFPZ6", "HSFEP1", "MIMATN", "MIMATS", "OFFN01"], \
               ["OFFN02", "OFFN03", "OFFN04", "OFFN05", "OFFN06"], \
               ["OFFNT1", "OFFNT2", "OFFNT3", "OFFNT4", "HSFAT1"], \
               ["HSFAT2", 'HSFEP2', 'HSFNP']]

    assert split_list(lst2, 5) == output2

    lst3 = ['TCPCP1', 'TCPCP2', 'TCPCP3', 'TCPCP4', 'TCPCP5']

    output3 = [['TCPCP1'], ['TCPCP2'], ['TCPCP3'], ['TCPCP4'], ['TCPCP5']]

    assert split_list(lst3, 7) == [lst3]
    assert split_list(lst3, 1) == output3
    assert split_list(lst3, 0) == [lst3]

    #EMPTY
    assert split_list([], 12) == []
    assert split_list([""], 12) == [[""]]
    assert split_list([""], 12) == [[""]]


def test_tz_finder():
    """0 is iHolder value... Since these are 1 line strings"""

    expect1 = ["0058 AM UTC SUN JAN 28 1998"]
    expect2 = ["2203 PM EST SAT AUG 02 2002"]
    expect3 = ["2203 PM EDT SAT AUG 02 2002"]
    expect4 = ["2203 PM CDT SAT AUG 02 2002"]
    expect5 = ["2203 PM CDT SAT AUG 02 2002"]
    expect6 = ["2203 PM MDT SAT AUG 02 2002"]
    expect7 = ["2203 PM MST SAT AUG 02 2002"]
    expect8 = ["2203 PM PDT SAT AUG 02 2002"]
    expect9 = ["2203 PM PST SAT AUG 02 2002"]
    expect10 = ["2203 PM AKDT SAT AUG 02 2002"]
    expect15 = ["2203 PM AKST SAT AUG 02 2002"]

    expect11 = ["2203 PM AST SAT AUG 02 2002"]
    expect11b = ["2203 PM ADT SAT AUG 02 2002"]

    expect13 = ["2203 PM SDT SAT AUG 02 2002"]
    expect14 = ["2203 PM SST SAT AUG 02 2002"]
    expect12 = ["2203 PM HADT SAT AUG 02 2002"]
    expect16 = ["2203 PM HAST SAT AUG 02 2002"]
    expect17 = ["2203 PM HST SAT AUG 02 2002"]
    expect18 = ["2203 PM CHST SAT AUG 02 2002"]
    expect19 = ["2203 PM ChST SAT AUG 02 2002"]
    expect20 = ["2203 PM GUAM LST SAT AUG 02 2002"]

    expect22 = ["2203 PM EASTERN SAT AUG 02 2002"]
    expect23 = ["2203 PM CENTRAL SAT AUG 02 2002"]
    expect24 = ["2203 PM GMT SAT AUG 02 2002"]

    expect25 = ["2203 PM SAT AUG 02 2002"]
    expect26 = ["2203 PM FRI SAT AUG 02 2002"]
    expect27 = ["0203 AM AUG 02 2002"]
    expect28 = ["2203 PM AUG 02 2002"]
    expect31 = ["JIMBO WENT TO THE EASTERN SHORE"]

    extra_space = [" 300 PM EST THU 21 NOV 2002"]
    less_time = ["3 PM EST FRI DEC 20 2002"]
    last_tz = "UTC"

    irrelevant = "SAT AUG 02 2002"

    assert timezone_finder(expect1, 0, last_tz) == ("0058 AM", "SUN JAN 28 1998", "UTC")
    assert timezone_finder(expect2, 0, last_tz) == ("2203 PM", irrelevant, "US/Eastern")
    assert timezone_finder(expect3, 0, last_tz) == ("2203 PM", irrelevant, "US/Eastern")
    assert timezone_finder(expect4, 0, last_tz) == ("2203 PM", irrelevant, "US/Central")
    assert timezone_finder(expect5, 0, last_tz) == ("2203 PM", irrelevant, "US/Central")
    assert timezone_finder(expect6, 0, last_tz) == ("2203 PM", irrelevant, "US/Mountain")
    assert timezone_finder(expect7, 0, last_tz) == ("2203 PM", irrelevant, "US/Mountain")
    assert timezone_finder(expect8, 0, last_tz) == ("2203 PM", irrelevant, "US/Pacific")
    assert timezone_finder(expect9, 0, last_tz) == ("2203 PM", irrelevant, "US/Pacific")
    assert timezone_finder(expect10, 0, last_tz) == ("2203 PM", irrelevant, "US/Alaska")
    assert timezone_finder(expect11, 0, last_tz) == ("2203 PM", irrelevant, "America/Halifax")
    assert timezone_finder(expect11b, 0, last_tz) == ("2203 PM", irrelevant, "America/Halifax")
    assert timezone_finder(expect12, 0, last_tz) == ("2203 PM", irrelevant, "Pacific/Honolulu")
    assert timezone_finder(expect13, 0, last_tz) == ("2203 PM", irrelevant, "US/Samoa")
    assert timezone_finder(expect14, 0, last_tz) == ("2203 PM", irrelevant, "US/Samoa")
    assert timezone_finder(expect15, 0, last_tz) == ("2203 PM", irrelevant, "US/Alaska")
    assert timezone_finder(expect16, 0, last_tz) == ("2203 PM", irrelevant, "Pacific/Honolulu")
    assert timezone_finder(expect17, 0, last_tz) == ("2203 PM", irrelevant, "Pacific/Honolulu")
    assert timezone_finder(expect18, 0, last_tz) == ("2203 PM", irrelevant, "Pacific/Guam")
    assert timezone_finder(expect19, 0, last_tz) == ("2203 PM", irrelevant, "Pacific/Guam")
    assert timezone_finder(expect20, 0, last_tz) == ("2203 PM", irrelevant, "Pacific/Guam")
    assert timezone_finder(expect22, 0, last_tz) == ("2203 PM", irrelevant, "US/Eastern")
    assert timezone_finder(expect23, 0, last_tz) == ("2203 PM", irrelevant, "US/Central")
    assert timezone_finder(expect24, 0, last_tz) == ("2203 PM", irrelevant, "UTC")
    #VARIATIONS
    assert timezone_finder(extra_space, 0, last_tz) == ("300 PM", "THU 21 NOV 2002", "US/Eastern")
    assert timezone_finder(less_time, 0, last_tz) == ("3 PM", "FRI DEC 20 2002", "US/Eastern")
    #LAST_TZ
    assert timezone_finder(expect25, 0, last_tz) == ("2203 PM", "AUG 02 2002", "UTC")
    assert timezone_finder(expect26, 0, last_tz) == ("2203 PM", irrelevant, "UTC")
    assert timezone_finder(expect27, 0, last_tz) == ("0203", "AUG 02 2002", "UTC")
    assert timezone_finder(expect28, 0, last_tz) == ("2203", "AUG 02 2002", "UTC")
    # WILL BE TOSSED IN wfo_read_time
    assert timezone_finder(expect31, 0, last_tz) == ("JIMBO WENT TO THE", "SHORE", "US/Eastern")

    #SPECIALS
    try1 = ["ISSUE TIME: 2018 Nov 05 0517 UTC"]
    try2 = [":ISSUED: 2018 Jan 01 0030 UTC"]
    try3 = [":ISSUE: 2018 Jan 01 0030 UTC"]
    try4 = [":ISSUED: 2018 Jan 01 0030 UT"]
    try5 = [":OTHER WORD: 2018 Jan 01 0030 UTC"]
    try6 = ["NCEP PROGNOSTIC DISCUSSION FROM 1200Z WED 31 DEC 1997"]
    try7 = ["NCEP PROGNOSTIC DISCUSSION FROM 0000 MON DEC 31 2001"]
    try8 = ["HPC FORECAST VALID 00 UTC 1 JAN THRU 00 UTC 8 JAN 2002"]

    assert timezone_finder(try1, 0, last_tz) == ("0517", "2018 Nov 05", "UTC")
    assert timezone_finder(try2, 0, last_tz) == ("0030", "2018 Jan 01", "UTC")
    assert timezone_finder(try3, 0, last_tz) == ("0030", "2018 Jan 01", "UTC")
    assert timezone_finder(try4, 0, last_tz) == ("0030", "2018 Jan 01", "UTC")
    assert timezone_finder(try5, 0, last_tz) == ("0030", "2018 Jan 01", "UTC")
    assert timezone_finder(try6, 0, last_tz) == ("1200", "WED 31 DEC 1997", "UTC")
    assert timezone_finder(try7, 0, last_tz) == ("0000", "DEC 31 2001", "UTC")
    assert timezone_finder(try8, 0, last_tz) == ("00", "1 JAN 2002", "UTC")

    try9 = ["HPC FORECAST VALID 00 UTC 06 JAN 2001 THRU 00 UTC 13 JAN  2001"]
    assert timezone_finder(try9, 0, last_tz) == ("00", "06 JAN 2001 2001", "UTC")


def test_word_trim_list():
    """
    TEST = ["SEA BREEZE", "SEA BREEZES", "SEA BREEZE*",
                "SEA BREEZE#", "SEA BREEZES", "SEA BREEZES*"]
    RESULT = ['SEA BREEZE*#', 'SEA BREEZES*']
    """
    #EACH STEP IS A FUNCTION CALL FROM SORT_T.py
    step1 = ['SEA BREEZE']
    step2 = ['SEA BREEZE', 'SEA BREEZES']
    step3 = ['SEA BREEZE*', 'SEA BREEZES']
    step4 = ['SEA BREEZE*#', 'SEA BREEZES']
    step5 = ['SEA BREEZE*#', 'SEA BREEZES']
    step6 = ['SEA BREEZE*#', 'SEA BREEZES*']
    step7 = ['SEA BREEZE*#', 'SEA BREEZES*', "IRON MAN"]

    step1b = [' ECMWF ']
    step2b = [' ECMWF ', ' ECMWF ENSEMBLE ']
    step3b = [' ECMWF ', ' ECMWF ENSEMBLE ', ' ENSEMBLE ']

    
    assert word_in_list_sym("SEA BREEZES", step1) == step2
    assert word_in_list_sym("SEA BREEZE*", step2) == step3
    assert word_in_list_sym("SEA BREEZE#", step3) == step4
    assert word_in_list_sym("SEA BREEZES", step4) == step5
    assert word_in_list_sym("SEA BREEZES*", step5) == step6
    assert word_in_list_sym("IRON MAN", step6) == step7
    
    assert word_in_list_sym(' ECMWF ENSEMBLE ', step1b) == step2b
    assert word_in_list_sym(' ENSEMBLE ', step2b) == step3b


def test_convert_time():
    """docstring"""

    tz1 = "US/Eastern"
    tz2 = "UTC"
    tz3 = "US/Central"
    tz4 = "US/Pacific"
    tz6 = "EST5EDT" #THIS IS A VALID PYTZ OPTION WITHOUT TIME CHANGES
    tz7 = ""
    #None is NOT A PYTZ OPTION

    pil = "AFDPHI"

    assert convert_time(pil, int("2013"), int("01"), int("01"), int("00"), int("00"), tz1) == \
                        datetime.datetime(2013, 1, 1, 5, 0, tzinfo=timezone.utc)

    assert convert_time(pil, int("1995"), int("12"), int("31"), int("23"), int("59"), tz2) == \
                        datetime.datetime(1995, 12, 31, 23, 59, tzinfo=timezone.utc)

    assert convert_time(pil, int("2019"), int("05"), int("31"), int("03"), int("45"), tz4) == \
                        datetime.datetime(2019, 5, 31, 10, 45, tzinfo=timezone.utc)

    assert convert_time(pil, int("2019"), int("01"), int("31"), int("03"), int("45"), tz4) == \
                        datetime.datetime(2019, 1, 31, 11, 45, tzinfo=timezone.utc)

    assert convert_time(pil, int("2013"), int("06"), int("01"), int("00"), int("00"), tz1) == \
                        datetime.datetime(2013, 6, 1, 4, 0, tzinfo=timezone.utc)

    assert convert_time(pil, int("2013"), int("06"), int("01"), int("00"), int("00"), tz6) == \
                        datetime.datetime(2013, 6, 1, 4, 0, tzinfo=timezone.utc)

    assert convert_time(pil, int("2013"), int("06"), int("01"), int("00"), int("00"), "EST") == \
                        datetime.datetime(2013, 6, 1, 5, 0, tzinfo=timezone.utc)

    assert convert_time(pil, int("1995"), int("12"), int("31"), int("23"), int("59")) == \
                        datetime.datetime(1995, 12, 31, 23, 59, tzinfo=timezone.utc)

    assert convert_time(pil, int("2019"), int("05"), int("31"), int("03"), int("45")) == \
                        datetime.datetime(2019, 5, 31, 3, 45, tzinfo=timezone.utc)

    #BAD CONVERSIONS
    bad = "US/BOOM"
    assert convert_time(pil, int("2013"), int("06"), int("01"), int("00"), int("00"), tz7) is None
    assert convert_time(pil, int("2013"), int("06"), int("01"), int("00"), int("00"), bad) is None
    assert convert_time(pil, int("2013"), int("06"), int("01"), int("00"), int("00"), "EDT") is None
    assert convert_time(pil, int("2014"), int("02"), int("30"), int("12"), int("00"), tz3) is None
