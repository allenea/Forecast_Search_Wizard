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
import sys,os
from datetime import datetime, timezone
import pytz

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.time_functions import findMonth, checkMonth, getMonth, getDDHHMM, getYear, checkYear,\
         getDay,get_Issuing_Date_text, getFirstGuess, guessAMPM, getAMPM, checkMinute, checkHour,\
         getHHMM, get_Issuing_Time_text,checkEverything


def test_findMonth():
    # ONLY USE RIGHT OF TIMEZONE... IN ANY SITUATION
    #PROPER ABBRIVIATIONS
    assert findMonth("SUN JAN 15 2019") == "JAN"
    assert findMonth("SUN FEB 15 2019") == "FEB"
    assert findMonth("SUN MAR 15 2019") == "MAR"
    assert findMonth("SUN APR 15 2019") == "APR"
    assert findMonth("SUN MAY 15 2019") == "MAY"
    assert findMonth("SUN JUN 15 2019") == "JUN"
    assert findMonth("SUN JUL 15 2019") == "JUL"
    assert findMonth("SUN AUG 15 2019") == "AUG"
    assert findMonth("SUN SEP 15 2019") == "SEP"
    assert findMonth("SUN OCT 15 2019") == "OCT"
    assert findMonth("SUN NOV 15 2019") == "NOV"
    assert findMonth("SUN DEC 15 2019") == "DEC"
    #FULL NAME
    assert findMonth("SUN JANUARY 15 2019") == "JANUARY"
    assert findMonth("SUN FEBRUARY 15 2019") == "FEBRUARY"
    assert findMonth("SUN MARCH 15 2019") == "MARCH"
    assert findMonth("SUN APRIL 15 2019") == "APRIL"
    assert findMonth("SUN MAY 15 2019") == "MAY"
    assert findMonth("SUN JUNE 15 2019") == "JUNE"
    assert findMonth("SUN JULY 15 2019") == "JULY"
    assert findMonth("SUN AUGUST 15 2019") == "AUGUST"
    assert findMonth("SUN SEPTEMBER 15 2019") == "SEPTEMBER"
    assert findMonth("SUN OCTOBER 15 2019") == "OCTOBER"
    assert findMonth("SUN NOVEMBER 15 2019") == "NOVEMBER"
    assert findMonth("SUN DECEMBER 15 2019") == "DECEMBER"
    #0's
    assert findMonth("SUN SEPT 15 2019") == "SEPT"
    assert findMonth("SUN 0CT 15 2019") == "OCT"
    assert findMonth("SUN N0V 15 2019") == "NOV"
    assert findMonth("SUN OCT0BER 15 2019") == "OCTOBER"
    assert findMonth("SUN N0VEMBER 15 2019") == "NOVEMBER"
    #no space between week day and month
    assert findMonth("SUNSEPT 15 2019") == "SEP"
    assert findMonth("MONJAN 15 2019") == "JAN"
    assert findMonth("SATJUL 15 2019") == "JUL"
    assert findMonth("SUNSEPTEMBER 15 2019") == "SEP"
    #INCORRECT ABBRIVIATIONS/WORDING
    assert findMonth("SUN OCTO 15 2019") == "OCT"
    assert findMonth("SUN NOVEM 15 2019") == "NOV"
    assert findMonth("NEW YEARS 2019") == "NAN"
    assert findMonth("CHRISTMAS 2014") == "NAN"
    #no space between month and day
    assert findMonth("SUN SEPT15 2019") == "SEPT"
    assert findMonth("MON JAN5 2019") == "JAN"
    assert findMonth("SAT JUL12 2019") == "JUL"
    assert findMonth("SUN SEPTEMBER15 2019") == "SEPTEMBER"
    assert findMonth("SUN AUG15 2019") == "AUG"
    assert findMonth("SUN OCT15 2019") == "OCT"
    assert findMonth("SUN NOVEMBER15 2019") == "NOVEMBER"
    assert findMonth("SUN DECEMBER15 2019") == "DECEMBER"
    # NO MONTH INFO   
    assert findMonth("SUN     15 2019") == "NAN"
    assert findMonth("SUN15 2019") == "NAN"
    assert findMonth("SUN  15 2019") == "NAN"
    assert findMonth("SUN  15 2019") == "NAN"
    assert findMonth("SUN 15 2019") == "NAN"
    #OTHER
    assert findMonth("SATJAN 15 2019") == "JAN"
    assert findMonth("MONFEB 15 2019") == "FEB"
    assert findMonth("TUEMAR 15 2019") == "MAR"
    assert findMonth("WEDAPR 15 2019") == "APR"
    assert findMonth("THURMAY 15 2019") == "MAY"
    assert findMonth("FRIJUN 15 2019") == "JUN"
    assert findMonth("SATJUL 15 2019") == "JUL"
    assert findMonth("SUNAUG 15 2019") == "AUG"
    assert findMonth("THUSEP 15 2019") == "SEP"
    assert findMonth("SATURDAYOCT 15 2019") == "OCT"
    assert findMonth("MONDAYNOV 15 2019") == "NOV"
    assert findMonth("WEDNESDAYDEC 15 2019") == "DEC"
    
    
    
def test_checkMonth():
    assert checkMonth("") == "NAN"
    assert checkMonth(" ") =="NAN"
    assert checkMonth("NAN") == "NAN"
    assert checkMonth("JAN") == "JAN"
    assert checkMonth("FEB") == "FEB"
    assert checkMonth("MAR") == "MAR"
    assert checkMonth("APR") == "APR"
    assert checkMonth("MAY") == "MAY"
    assert checkMonth("JUN") == "JUN"
    assert checkMonth("JUL") == "JUL"
    assert checkMonth("AUG") == "AUG"
    assert checkMonth("SEP") == "SEP"
    assert checkMonth("OCT") == "OCT"
    assert checkMonth("NOV") == "NOV"
    assert checkMonth("DEC") == "DEC"
    assert checkMonth("JANUARY") == "JAN" 
    assert checkMonth("FEBRUARY") == "FEB" 
    assert checkMonth("MARCH") == "MAR" 
    assert checkMonth("APRIL") == "APR"
    assert checkMonth("MAY") == "MAY"
    assert checkMonth("JUNE") == "JUN"
    assert checkMonth("JULY") == "JUL"
    assert checkMonth("AUGUST") == "AUG" 
    assert checkMonth("SEPTEMBER") == "SEP"
    assert checkMonth("OCTOBER") == "OCT"
    assert checkMonth("NOVEMBER") == "NOV"
    assert checkMonth("DECEMBER") == "DEC"
    assert checkMonth("SEPT") == "SEP"
    
    
    
def test_getMonth():
    assert getMonth("NAN") == None
    assert getMonth("JAN") == 1
    assert getMonth("FEB") == 2
    assert getMonth("MAR") == 3
    assert getMonth("APR") == 4
    assert getMonth("MAY") == 5
    assert getMonth("JUN") == 6
    assert getMonth("JUL") == 7
    assert getMonth("AUG") == 8
    assert getMonth("SEP") == 9
    assert getMonth("OCT") == 10
    assert getMonth("NOV") == 11
    assert getMonth("DEC") == 12
    assert getMonth("") == None
    assert getMonth(" ") == None
    assert getMonth("BOO") == None
    assert getMonth("JIM") == None



def test_getDDHHMM():
    assert getDDHHMM("999999") == (None, None, None)
    assert getDDHHMM(" ") == (None, None, None)
    assert getDDHHMM("") == (None, None, None)
    assert getDDHHMM("12345") == (None, None, None)
    assert getDDHHMM("345") == (None, None, None)
    assert getDDHHMM("012345") == (1,"23","45")
    assert getDDHHMM("020000") == (2,"00","00")
    assert getDDHHMM("312359") == (31,"23","59")
    assert getDDHHMM("302359") == (30,"23","59")
    assert getDDHHMM("041200") == (4,"12","00")
    assert getDDHHMM("071301") == (7,"13","01")
    assert getDDHHMM("110434") == (11,"04","34")
    assert getDDHHMM("220612") == (22,"06","12")
    assert getDDHHMM("22061122") == (None, None, None)



def test_getYear():
    assert getYear("SUN JAN 15 1903", 2003) == (1903, ["15"])
    assert getYear("MON FEB 15 1900", 2000) == (1900, ["15"])
    assert getYear("WED APR 15 1980",1980) == (1980, ["15"])
    assert getYear("TUR MAY 15 2013", 2013) == (2013, ["15"])
    assert getYear("FRI JUN 15 2015", 2015) == (2015, ["15"])
    assert getYear("SUN AFA 15 2013", 2013) == (2013, ["15"])
    assert getYear("WED AUG 15 2014", 2014) == (2014, ["15"])
    assert getYear("SUN OCT 152018", 2018) == (2018, ["15"])
    assert getYear("SUN DEC 152000", 2000) == (2000, ["15"])
    assert getYear("SUN JANUARY 15 2001", 2001) == (2001, ["15"])
    assert getYear("MON FEBRUARY 15 2003", 2003) == (2003, ["15"])
    assert getYear("MARCH 15 2005", 2005) == (2005, ["15"])
    assert getYear("SUN APRIL 15 2012", 2012) == (2012, ["15"])
    assert getYear(" MAY 15 2007", 2007) == (2007, ["15"])
    assert getYear("FRI JUNE 15 2009", 2009) == (2009, ["15"])
    assert getYear("JULY 15 2010", 2010) == (2010, ["15"])
    assert getYear("THU AUGUST 15 2011", 2011) == (2011, ["15"])
    assert getYear("TUE SEPTEMBER 15 2004", 2004) == (2004, ["15"])
    assert getYear("OCTOBER 15 2002", 2002) == (2002, ["15"])
    assert getYear("MON N0VEMBER 15 1893", 2013) == (None, ["15", "1893"])
    assert getYear(" DECEMBER 15 1133", 2015) == (None, ["15","1133"])
    assert getYear("SAT NOV 1520000", 2000) == (2000, ["15"])
    assert getYear("FRIDAY SEP 152019", 2019) == (2019, ["15"])
    assert getYear("1000 AM TUE MAR 15 2020", 2020) == (2020, ["1000","15"])
    assert getYear("TUE MAR 15 2020", 2020) == (2020, ["15"])
    assert getYear("TUE DEC 31 2020", 2019) == (2020, ["31"])
    assert getYear("TUE DEC 31", 2019) == (None, ["31"])
    assert getYear("TUE DEC 2019", 2019) == (2019, [])

    
    
def test_checkYear():
    #NONE INPUT - YEAR
    assert checkYear(None,2019, 6, "AFDPHI") == (2019, False)
    assert checkYear(None,1996, 5, "AFDPHI") == (1996, False)
    
    #REGULAR
    assert checkYear(2011,2011, 12, "AFDPHI") == (2011, False)
    assert checkYear(2000,2000, 1, "AFDPHI") == (2000, False)
    assert checkYear(2019,2019, 6, "AFDPHI") == (2019, False)
    assert checkYear(1996,1996, 5, "AFDPHI") == (1996, False)
    
    #PMDTHR
    assert checkYear(1900,2000, 1, "PMDTHR") == (2000, False)
    assert checkYear(1901,2001, 12, "PMDTHR") == (2001, False)
    assert checkYear(1902,2002, 6, "PMDTHR") == (2002, False)
    assert checkYear(1903,2003, 6, "PMDTHR") == (2003, False)
    
    
    #PMDTHR - RARE
    assert checkYear(1901,2004, 12, "PMDTHR") == (2001, True)
    assert checkYear(1902,2006, 6, "PMDTHR") == (2002, True)
    assert checkYear(1903,2000, 6, "PMDTHR") == (2000, True)

    
    #WEIRDNESS IN THE LIMITED CASES FOLLOW THE BELOW RULES
    assert checkYear(1901,2000, 1, "PMDTHR") == (2001, False)
    assert checkYear(1901,2002, 12, "PMDTHR") == (2001, False)
    assert checkYear(1901,2000, 6, "PMDTHR") == (2000, True)
    assert checkYear(1901,2002, 6, "PMDTHR") == (2001, True) #Year off by 1 and do conversion
    
    #EXCEPTIONS AND ASSUMPTIONS
    assert checkYear(2018,2017, 1, "PMDTHR") == (2018, False) # JAN -1YR EXCEPTION - USE HIGHER
    assert checkYear(2017,2017, 1, "PMDTHR") == (2017, False)
    assert checkYear(2017,2018, 1, "PMDTHR") == (2017, True) # JAN +1YR EXCEPTION - USE HIGHER
    assert checkYear(2017,2017, 12, "PMDTHR") == (2017, False)
    assert checkYear(2018,2017, 12, "PMDTHR") == (2017, True) # DEC -1YR EXCEPTION - USE LOWER
    assert checkYear(1903,1902, 12, "PMDTHR") == (1902, True) # DEC -1YR EXCEPTION - USE LOWER
    assert checkYear(1903,1902, 12, "AFDLWX") == (1902, True) # DEC -1YR EXCEPTION - USE LOWER

    assert checkYear(2017,2018, 12, "PMDTHR") == (2017, False) # DEC +1YR EXCEPTION - USE LOWER
    assert checkYear(2018,2017, 6, "PMDTHR") == (2017, True) #WARN 2018 hasn't happened yet
    assert checkYear(2017,2018, 6, "PMDTHR") == (2017, True) #WARN USE TEXT - MORE REALISTIC
    assert checkYear(2018,2017, 7, "PMDTHR") == (2017, True) #WARN 2018 hasn't happened yet
    assert checkYear(2017,2018, 7, "PMDTHR") == (2017, True) #WARN USE TEXT - MORE REALISTIC
    
    assert checkYear(2018,2017, 1, "AFDPHI") == (2018, False) # JAN -1YR EXCEPTION - USE HIGHER
    assert checkYear(2017,2017, 1, "AFDPHI") == (2017, False)
    assert checkYear(2017,2018, 1, "AFDPHI") == (2017, True) # JAN +1YR EXCEPTION - USE HIGHER
    assert checkYear(2017,2017, 12, "AFDPHI") == (2017, False)
    assert checkYear(2018,2017, 12, "AFDPHI") == (2017, True) # DEC -1YR EXCEPTION - USE LOWER
    assert checkYear(2017,2018, 12, "AFDPHI") == (2017, False) # DEC +1YR EXCEPTION - USE LOWER
    assert checkYear(2018,2017, 6, "AFDPHI") == (2017, True) #WARN 2018 hasn't happened yet
    assert checkYear(2017,2018, 6, "AFDPHI") == (2017, True) #WARN USE TEXT - MORE REALISTIC
    assert checkYear(2018,2017, 7, "AFDPHI") == (2017, True) #WARN 2018 hasn't happened yet
    assert checkYear(2017,2018, 7, "AFDPHI") == (2017, True) #WARN USE TEXT - MORE REALISTIC

    
    assert checkYear(2018,1995, 1, "AFDPHI") == (1995, True) # JAN -1YR EXCEPTION - USE HIGHER
    assert checkYear(2012,2018, 1, "AFDPHI") == (2012, True) # JAN +1YR EXCEPTION - USE HIGHER
    assert checkYear(2018,1998, 12, "AFDPHI") == (1998, True) # DEC -1YR EXCEPTION - USE LOWER
    assert checkYear(2000,2018, 12, "AFDPHI") == (2000, True) # DEC +1YR EXCEPTION - USE LOWER
    assert checkYear(2018,2001, 6, "AFDPHI") == (2001, True) #WARN 2018 hasn't happened yet
    assert checkYear(2017,2019, 6, "AFDPHI") == (2017, True) #WARN USE TEXT - MORE REALISTIC
    assert checkYear(2018,2009, 7, "AFDPHI") == (2009, True) #WARN 2018 hasn't happened yet
    assert checkYear(2013,2017, 7, "AFDPHI") == (2013, True) #WARN USE TEXT - MORE REALISTIC



def test_getDay():
    assert getDay(["1"], 31) == 1
    assert getDay(["1"], 30) == 1
    assert getDay(["1"], 29) == 1
    assert getDay(["1"], 28) == 1
    assert getDay(["28"], 1) == 28
    assert getDay(["28"], 28) == 28
    assert getDay(["29"], 1) == 29
    assert getDay(["29"], 29) == 29
    assert getDay(["30"], 1) == 30
    assert getDay(["30"], 30) == 30
    assert getDay(["31"], 1) == 31
    assert getDay(["31"], 31) == 31
    
    assert getDay(["1"], 1) == 1
    assert getDay(["0"], 10) == None
    assert getDay(["32"], 1) == None
    assert getDay(["54"], 5) == None
    
    assert getDay(["11"], 11) == 11
    assert getDay(["21"], 21) == 21
    assert getDay(["31"], 31) == 31
    
    assert getDay(["15", "1893"], 15) == 15
    assert getDay(["1000","15"], 15) == 15

    assert getDay([], 11) == None 

    assert getDay(["14", "1893"], 15) == 14
    assert getDay(["1000","14"], 15) == 14
    
    assert getDay(["14", "13"], 15) == None
    assert getDay(["14", "15"], 15) == 15
    assert getDay(["16","14","15"], 15) == 15
    
    
    
def test_getFirstGuess():
    assert getFirstGuess(2013, 6, 12, 12, 0, "UTC") == datetime(2013, 6, 12, 12, 0,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 0, 12, 12, 0, "UTC") == None
    assert getFirstGuess(2013, 12, 12, 12, 0, "UTC") == datetime(2013, 12, 12, 12, 0,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 14, 12, 12, 0, "UTC") == None
    
    
    assert getFirstGuess(2013, 6, 12, 0, 0, "UTC") == datetime(2013, 6, 12, 0, 0,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 6, 12, 12, 0, "UTC") == datetime(2013, 6, 12, 12, 0,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 12, 12, 23, 0, "UTC") == datetime(2013, 12, 12, 23, 0,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 12, 12, 24, 0, "UTC") == None
    assert getFirstGuess(2013, 12, 12, 30, 0, "UTC") == None
    assert getFirstGuess(2013, 12, 12, 30, -1., "UTC") == None
    assert getFirstGuess(2013, 12, 12, 30, "00", "UTC") == None

    assert getFirstGuess(2013, 6, 12, 0, 0, "UTC") == datetime(2013, 6, 12, 0, 0,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 6, 12, 12, 30, "UTC") == datetime(2013, 6, 12, 12, 30,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 12, 12, 23, 59, "UTC") == datetime(2013, 12, 12, 23, 59, tzinfo=timezone.utc)
    assert getFirstGuess(2013, 12, 12, 23, 60, "UTC") == None
    assert getFirstGuess(2013, 12, 12, 23, "01", "UTC") == None
    

    assert getFirstGuess(2025, 6, 12, 12, 0, "UTC") == datetime(2025, 6, 12, 12, 0,tzinfo=timezone.utc)
    assert getFirstGuess(-1, 6, 12, 12, 0, "UTC") == None
    
    assert getFirstGuess(2013, 6, 12, 2, 32, "UTC") == datetime(2013, 6, 12, 2, 32, tzinfo=timezone.utc)
    assert getFirstGuess(2013, 6, 12, 2, 32, "UTC") == datetime(2013, 6, 12, 2, 32, tzinfo=timezone.utc)
    assert getFirstGuess(2013, 2, 28, 2, 32, "UTC") == datetime(2013, 2, 28, 2, 32,tzinfo=timezone.utc)
    assert getFirstGuess(2018, 2, 28, 2, 32, "UTC") == datetime(2018, 2, 28, 2, 32,tzinfo=timezone.utc)
    assert getFirstGuess(2013, 2, 29, 2, 32, "UTC") == None
    assert getFirstGuess(2016, 2, 29, 2, 32, "UTC") == datetime(2016, 2, 29, 2, 32,tzinfo=timezone.utc)



def test_guessAMPM():
    assert guessAMPM(datetime(2019, 6, 12, 0, 59, tzinfo=pytz.timezone("UTC")), "US/Eastern") == "PM"
    assert guessAMPM(datetime(2019, 6, 12, 21, 59,tzinfo= pytz.timezone("UTC")), "US/Eastern") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 7, 59, tzinfo=pytz.timezone("UTC")), "US/Eastern") == "AM"
    assert guessAMPM(datetime(2019, 12, 12, 21, 59, tzinfo=pytz.timezone("UTC")), "US/Eastern") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 10, 59, tzinfo=pytz.timezone("UTC")), "US/Eastern") == "AM"
    assert guessAMPM(None, "US/Eastern") == None
    
    assert guessAMPM(datetime(2019, 6, 12, 0, 59, tzinfo=pytz.timezone("UTC")), "UTC") == "AM"
    assert guessAMPM(datetime(2019, 6, 12, 21, 59,tzinfo= pytz.timezone("UTC")), "UTC") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 21, 59, tzinfo=pytz.timezone("UTC")), "UTC") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 10, 59, tzinfo=pytz.timezone("UTC")), "UTC") == "AM"
    assert guessAMPM(None, "UTC") == None
    
    assert guessAMPM(datetime(2019, 6, 12, 0, 59, tzinfo=pytz.timezone("UTC")), "US/Central") == "PM"
    assert guessAMPM(datetime(2019, 6, 12, 21, 59,tzinfo= pytz.timezone("UTC")), "US/Central") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 7, 59, tzinfo=pytz.timezone("UTC")), "US/Central") == "AM"
    assert guessAMPM(datetime(2019, 12, 12, 21, 59, tzinfo=pytz.timezone("UTC")), "US/Central") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 10, 59, tzinfo=pytz.timezone("UTC")), "US/Central") == "AM"
    assert guessAMPM(None, "US/Central") == None
    
    assert guessAMPM(datetime(2019, 6, 12, 0, 59, tzinfo=pytz.timezone("UTC")), "US/Mountain") == "PM"
    assert guessAMPM(datetime(2019, 6, 12, 21, 59,tzinfo= pytz.timezone("UTC")), "US/Mountain") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 7, 59, tzinfo=pytz.timezone("UTC")), "US/Mountain") == "AM"
    assert guessAMPM(datetime(2019, 12, 12, 21, 59, tzinfo=pytz.timezone("UTC")), "US/Mountain") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 10, 59, tzinfo=pytz.timezone("UTC")), "US/Mountain") == "AM"
    assert guessAMPM(None, "US/Mountain") == None
 
    assert guessAMPM(datetime(2019, 6, 12, 0, 59, tzinfo=pytz.timezone("UTC")), "US/Pacific") == "PM"
    assert guessAMPM(datetime(2019, 6, 12, 21, 59,tzinfo= pytz.timezone("UTC")), "US/Pacific") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 8, 59, tzinfo=pytz.timezone("UTC")), "US/Pacific") == "AM"
    assert guessAMPM(datetime(2019, 12, 12, 21, 59, tzinfo=pytz.timezone("UTC")), "US/Pacific") == "PM"
    assert guessAMPM(datetime(2019, 12, 12, 10, 59, tzinfo=pytz.timezone("UTC")), "US/Pacific") == "AM"
    assert guessAMPM(None, "US/Pacific") == None
    
    
    assert guessAMPM(datetime(2009, 4, 13, 16, 55, tzinfo=pytz.timezone("UTC")), "US/Central") == "AM"


def test_getAMPM():
    assert getAMPM("1159",datetime(2013,6,6,3,59,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', False)
    assert getAMPM("1214 AM",datetime(2013,12,6,5,15,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', False)
    assert getAMPM("1130 PM",datetime(2013,12,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', False)
    assert getAMPM("1159 A",datetime(2013,6,6,3,59,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', False)

    assert getAMPM("MIDNIGHT",datetime(2013,6,6,16,00,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', True)
    assert getAMPM("MIDNIGHT",datetime(2013,6,6,4,00,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', False)


    assert getAMPM("NOON",datetime(2013,6,6,16,00,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', False)
    assert getAMPM("NOON",datetime(2013,6,6,4,00,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', True)

    assert getAMPM("1214 PM",datetime(2013,12,6,5,14,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', True) #12:14 am but written as 12:14pm
    assert getAMPM("1130 AM",datetime(2013,12,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', True) #11:30 pm but written as 11:30am
    
    
    assert getAMPM("1159",datetime(2013,6,6,3,59,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', False)
    assert getAMPM("1214 AMPM",datetime(2013,12,6,5,14,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', False)
    assert getAMPM("1130 AMPM",datetime(2013,12,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', True) # 11:30 am being confused with 11:30PM
    #^^ PM BECAUSE OF GUESS TIME AND PM IN THERE EVEN THOUGH AM IS THERE TOO....
    assert getAMPM("1230 PM AM", datetime(2013,6,6,16,30,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('PM', False)
    assert getAMPM("1230 AM PM", datetime(2013,6,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', False)
    assert getAMPM("1130 PMAM",datetime(2013,12,6,5,30,tzinfo=pytz.timezone("UTC")), "US/Eastern") == ('AM', True) # 11:30 PM being confused with 1:30AM
    #^^ AM BECAUSE OF GUESS TIME AND AM IN THERE EVEN THOUGH PM IS THERE TOO....

    assert getAMPM("1230Z", datetime(2013,12,6,12,30,tzinfo=pytz.timezone("UTC")), "UTC") == ('PM', False)
    assert getAMPM("1230 Z", datetime(2013,12,6,12,30, tzinfo=pytz.timezone("UTC")), "UTC") == ('PM', False)
    assert getAMPM("0030 Z", datetime(2013,12,6,0,30,tzinfo=pytz.timezone("UTC")), "UTC") == ('AM', False)
    assert getAMPM("500 Z", datetime(2013,12,6,5,0,tzinfo=pytz.timezone("UTC")), "UTC") == ('AM', False)
    assert getAMPM("1500 Z", datetime(2013,12,6,15,0,tzinfo=pytz.timezone("UTC")), "UTC") == ('PM', False)
    assert getAMPM("15OO Z", datetime(2013,12,6,15,0,tzinfo=pytz.timezone("UTC")), "UTC") == ('PM', False)
    assert getAMPM("NMLT Z", datetime(2013,12,6,5,30,tzinfo=pytz.timezone("UTC")), "UTC") == ("AM", True)
    assert getAMPM("15TH Z", datetime(2013,12,6,15,30,tzinfo=pytz.timezone("UTC")), "UTC") == ("PM", True)
    assert getAMPM("2789 Z", datetime(2013,12,6,5,30,tzinfo=pytz.timezone("UTC")), "UTC") == ("AM", True)
    

    assert getAMPM("1230 AM", None, "US/Eastern") == ('AM', False)
    assert getAMPM("1230 PM", None, "US/Eastern") == ('PM', False)

    assert getAMPM("1230 AMPM", None, "US/Eastern") == ('AM', True)
    assert getAMPM("1230 PMAM", None, "US/Eastern") == ('PM', True)
    assert getAMPM("1230 PM AM", None, "US/Eastern") == ('PM', True)
    assert getAMPM("1230 AM PM", None, "US/Eastern") == ('AM', True)
    
    assert getAMPM("1230Z", None, "UTC") == ('PM', False)
    assert getAMPM("1230 Z", None, "UTC") == ('PM', False)
    assert getAMPM("0030 Z", None, "UTC") == ('AM', False)
    assert getAMPM("500 Z", None, "UTC") == ('AM', False)
    assert getAMPM("1500 Z", None, "UTC") == ('PM', False)
    assert getAMPM("15OO Z", None, "UTC") == ('PM', False)
    assert getAMPM("NMLT Z", None, "UTC") == (None, True)
    assert getAMPM("15TH Z", None, "UTC") == (None, True)
    assert getAMPM("2789 Z", None, "UTC") == (None, True)
    
    assert getAMPM("NOON", None, "US/Eastern") == ('PM', True)
    assert getAMPM("N00N", None, "US/Eastern") == ('PM', True)
    assert getAMPM("MIDNIGHT", None, "US/Eastern") == ('AM', True)

    assert getAMPM("1230 PAM", None, "US/Eastern") == ('AM', True)
    assert getAMPM("1230 APM", None, "US/Eastern") == ('PM', True)
    assert getAMPM("130", None, "US/Eastern") == (None, True)
    assert getAMPM("1230", None, "US/Eastern") == (None, True)
    assert getAMPM("1700", None, "US/Eastern") == (None, True)

    assert getAMPM("1200 PM", datetime(2009, 4, 13, 16, 55, tzinfo=pytz.timezone("UTC")), "US/Central") == ("PM", True)


def test_checkMinute():
    assert checkMinute(-1) == None
    assert checkMinute(2) == "02"
    assert checkMinute(52) == "52"
    assert checkMinute(28) == "28"
    assert checkMinute(11) == "11"
    assert checkMinute(30) == "30"
    assert checkMinute(9) == "09"
    assert checkMinute(10) == "10"
    assert checkMinute(59) == "59"
    assert checkMinute(60) == None
    assert checkMinute(100) == None
    assert checkMinute(0) == "00"



def test_checkHour():
    assert checkHour(-1,"AM") == None
    assert checkHour(-1,"PM") == None
    assert checkHour(-1, None) == None
    assert checkHour(24,None) == None
    assert checkHour(32,None) == None
    assert checkHour(24,"AM") == None
    assert checkHour(32,"PM") == None
    
    assert checkHour(11,None) == "11"
    assert checkHour(8,None) == "08"
    assert checkHour(23,"AM") == None
    assert checkHour(23,"PM") == "23"

    assert checkHour(18,"PM") == "18"    
    
    assert checkHour(9,"AM") == "09"
    assert checkHour(1,"AM") == "01"
    assert checkHour(5,"AM") == "05"
    assert checkHour(11,"AM") == "11"
    assert checkHour(30,"AM") == None
    assert checkHour(10,"AM") == "10"
    assert checkHour(59,"AM") == None
    assert checkHour(60,"AM") == None
    assert checkHour(100,"AM") == None
    assert checkHour(0,"AM") == "00"
    assert checkHour(12,"AM") == "00"

    assert checkHour(0,"PM") == "12"
    assert checkHour(9,"PM") == "21"
    assert checkHour(11,"PM") == "23"
    assert checkHour(12,"PM") == "12"
    assert checkHour(10,"PM") == "22"
    assert checkHour(23,"PM") == "23"
    assert checkHour(20,"PM") == "20"
    assert checkHour(18,"PM") == "18"  



def test_getHHMM():
    assert getHHMM("1200","AM") == (12, 0)
    assert getHHMM("1200","PM") == (12, 0)
    assert getHHMM("0030","AM") == (0, 30)
    assert getHHMM("0003","AM") == (0, 3)
    assert getHHMM("12","PM") == (12, 0)
    assert getHHMM("23","PM") == (23 ,0)
    assert getHHMM("23", None) == (None,None)
    assert getHHMM("23", None) == (None,None)
    assert getHHMM("1135","AM") == (11,35)
    assert getHHMM("1135","PM") == (11,35)
    assert getHHMM("135","AM") == (1,35)
    assert getHHMM("135","PM") == (1,35)
    assert getHHMM("1","AM") == (1, 0)
    assert getHHMM("2","PM") == (2 ,0)
    assert getHHMM("12000","AM") == (None,None)



def test_get_Issuing_Date_text():
    #FULL NAME
    assert get_Issuing_Date_text("SUN JANUARY 7 1902",2002,"PMDTHR","070534")  == (2002, 1, 7, False)
    assert get_Issuing_Date_text("SUN JANUARY 5 1901",2001,"PMDTHR","050534") == (2001, 1, 5, False)
    assert get_Issuing_Date_text("SUN DECEMBER 23 1900",2000,"PMDTHR","230534")== (2000, 12, 23, False)
    
    assert get_Issuing_Date_text("SUN JANUARY 7 1902",2002,"AFDLWX","070534")  == (None, None , None ,None)
    assert get_Issuing_Date_text("SUN JANUARY 5 1901",2001,"AFDLWX","050534") == (None, None , None ,None)
    assert get_Issuing_Date_text("SUN DECEMBER 23 1900",2000,"AFDLWX","230534")== (None, None , None ,None)
    
    assert get_Issuing_Date_text("SUN JANUARY 1 2018",2017,"PMDTHR","010534") == (2018, 1, 1, False) # JAN -1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN JANUARY 7 2017",2017,"PMDTHR","070534")  == (2017, 1, 7, False)
    assert get_Issuing_Date_text("SUN JANUARY 5 2017",2018,"PMDTHR","050534") == (2017, 1, 5, True)
    assert get_Issuing_Date_text("SUN DECEMBER 23 2017",2017,"PMDTHR","230534")== (2017, 12, 23, False)
    assert get_Issuing_Date_text("SUN DECEMBER 15 2018",2017,"PMDTHR","150534") == (2017, 12, 15, True) # DEC -1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN DECEMBER 19 2017",2018,"PMDTHR","190534") == (2017, 12, 19, False) # DEC +1YR EXCEPTION - USE LOWER
    
    assert get_Issuing_Date_text("SUN JULY 21 2018",2017,"PMDTHR","210534") == (2017, 7, 21, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017",2018,"PMDTHR","280534") == (2017,7, 28, True) #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018",2017,"PMDTHR","300534") == (2017,7, 30, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2017",2018,"PMDTHR","310534") == (2017,7, 31, True) #WARN USE TEXT - MORE REALISTIC
    
    assert get_Issuing_Date_text("SUN JANUARY 1 2018",2017,"AFDPHI","010534")  == (2018, 1, 1, False) # JAN -1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN JANUARY 7 2017",2017,"AFDPHI","070534") == (2017, 1, 7, False)
    assert get_Issuing_Date_text("SUN JANUARY 5 2017",2018,"AFDPHI","050534") == (2017, 1, 5, True)
    assert get_Issuing_Date_text("SUN DECEMBER 23 2017",2017,"AFDPHI","230534") == (2017, 12, 23, False)
    assert get_Issuing_Date_text("SUN DECEMBER 15 2018",2017,"AFDPHI","150534") == (2017, 12, 15, True) # DEC -1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN DECEMBER 19 2017",2018,"AFDPHI","190534") == (2017, 12, 19, False) # DEC +1YR EXCEPTION - USE LOWER
    
    assert get_Issuing_Date_text("SUN JULY 21 2018",2017,"AFDMHX","210534") == (2017, 7, 21, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017",2018,"AFDMHX","280534") == (2017,7, 28, True) #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018",2017,"AFDMHX","300534") == (2017,7, 30, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2017",2018,"AFDMHX","310534") == (2017,7, 31, True) #WARN USE TEXT - MORE REALISTIC
    
    #"HPC FORECAST VALID 00 UTC 9 FEB THRU 00 UTC 16 FEB 2001"  - NO ASSUMPTIONS
    assert get_Issuing_Date_text("9 FEB 2001",2001,"PMDHI","090000") == (2001, 2, 9, False)
    
    #HPC FORECAST VALID 00 UTC 06 JAN 2001 THRU 00 UTC 13 JAN  2001  - NO ASSUMPTIONS (DOUBLE YEAR)
    assert get_Issuing_Date_text("06 JAN 2001 2001",2001,"PMDHI","060000") == (2001, 1, 6, False)
    
    assert get_Issuing_Date_text("WED APR 15 1980",1980,"AFDPHI","150345") == (1980,  4,  15,False)
    assert get_Issuing_Date_text("TUR MAY 15 2013", 2013,"AFDPHI","150345") == (2013, 5 , 15 ,False)
    assert get_Issuing_Date_text("FRI JUN 15 2015", 2015,"AFDPHI","150345") == (2015, 6 , 15 ,False)
    assert get_Issuing_Date_text("WED AUG 15 2014", 2014,"AFDPHI","150345") == (2014, 8 , 15 ,False)
    assert get_Issuing_Date_text("SUN OCT 152018", 2018,"AFDPHI","150345") == (2018, 10 , 15 ,False)
    assert get_Issuing_Date_text("SUN DEC 152000", 2000,"AFDPHI","150345") == (2000,12 , 15 ,False)
    assert get_Issuing_Date_text("SUN JANUARY 15 2001", 2001,"AFDPHI","150345") == (2001,1  , 15 ,False)
    assert get_Issuing_Date_text("MON FEBRUARY 15 2003", 2003,"AFDPHI","150345") == (2003,2  , 15 ,False)
    assert get_Issuing_Date_text("MARCH 15 2005", 2005,"AFDPHI","150345") == (2005, 3 , 15 ,False)
    assert get_Issuing_Date_text("SUN APRIL 15 2012", 2012,"AFDPHI","150345") == (2012, 4 , 15 ,False)
    assert get_Issuing_Date_text(" MAY 15 2007", 2007,"AFDPHI","150345") == (2007, 5 , 15 ,False)
    assert get_Issuing_Date_text("FRI JUNE 15 2009", 2009,"AFDPHI","150345") == (2009, 6,15 ,False)
    assert get_Issuing_Date_text("JULY 15 2010", 2010,"AFDPHI","150345") == (2010, 7 , 15 ,False)
    assert get_Issuing_Date_text("THU AUGUST 15 2011", 2011,"AFDPHI","150345") == (2011,  8, 15 ,False)
    assert get_Issuing_Date_text("TUE SEPTEMBER 15 2004", 2004,"AFDPHI","150345") == (2004, 9 ,  15,False)
    assert get_Issuing_Date_text("OCTOBER 15 2002", 2002,"AFDPHI","150345") == (2002, 10 , 15 ,False)
    assert get_Issuing_Date_text("SAT NOV 1520000", 2000,"AFDPHI","150345") == (2000, 11 , 15 ,False)
    assert get_Issuing_Date_text("FRIDAY SEP 152019", 2019,"AFDPHI","150345") == (2019, 9 , 15 ,False)
    assert get_Issuing_Date_text("1000 AM TUE MAR 15 2020", 2020,"AFDPHI","150345") == (2020, 3 , 15 ,False)
    assert get_Issuing_Date_text("TUE MAR 15 2020", 2020,"AFDPHI","150345") == (2020, 3 , 15 ,False)
    assert get_Issuing_Date_text("TUE DEC 31 2020", 2019,"AFDPHI","150345") == (2019, 12 , 31 ,True)  # USE iYEAR #MOVED YEAR AHEAD TOO EARLY

    assert get_Issuing_Date_text("SUN AFA 15 2013", 2013,"AFDPHI","150345") == (None, None , None ,None)
    assert get_Issuing_Date_text("SUN JAN 15 1903",2003,"AFDPHI","150345") == (None, None , None ,None)
    assert get_Issuing_Date_text("MON FEB 15 1900", 2000,"AFDPHI","150345") == (None, None , None ,None)
    assert get_Issuing_Date_text("TUE DEC 2019", 2019,"AFDPHI","150345") == (2019, 12 , None ,True)
    assert get_Issuing_Date_text("MON N0VEMBER 15 1893", 2013,"AFDPHI","150345") == (2013, 11 , 15 ,False) # USE iYEAR... False since year == None
    assert get_Issuing_Date_text(" DECEMBER 15 1133", 2015,"AFDPHI","150345") == (2015, 12 , 15 ,False) # USE iYEAR
    assert get_Issuing_Date_text("TUE DEC 31", 2019,"AFDPHI","150345") == (2019, 12 , 31 ,False) # USE iYEAR
    
    assert get_Issuing_Date_text("SUN JULY 21 2018",2017,"AFDPHI","210534") == (2017, 7, 21, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017",2018,"AFDPHI","280534") == (2017, 7, 28, True) #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018",2017,"AFDPHI","300534") == (2017, 7, 30, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2017",2018,"AFDPHI","310534") == (2017, 7, 31, True) #WARN USE TEXT - MORE REALISTIC    
    assert get_Issuing_Date_text("SUN JANUARY 1 2018",1995,"AFDPHI","010534") == (1995,1, 1, True) # JAN -1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN JANUARY 5 2012",2018,"AFDPHI","050534") == (2012,1, 5, True) # JAN +1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN DECEMBER 12 2018",1998,"AFDPHI","120534") == (1998,12, 12, True) # DEC -1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN DECEMBER 15 2000",2018,"AFDPHI","150534") == (2000,12, 15, True) # DEC +1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN JULY 21 2018",2001,"AFDPHI","210534") == (2001,7, 21, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017",2019,"AFDPHI","280534") == (2017,7, 28, True) #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018",2009,"AFDPHI","300534") == (2009,7, 30, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2013",2017,"AFDPHI","310534") == (2013,7, 31, True) #WARN USE TEXT - MORE REALISTIC

    assert get_Issuing_Date_text("SUN JAN 15",2019,"AFDPHI","150345") == (2019, 1,15, False)  #MISSING YEAR
    assert get_Issuing_Date_text("SUN FEB 15",1996,"AFDPHI","150345") == (1996,2, 15, False)  #MISSING YEAR
    
    #assert get_Issuing_Date_text(,"AFDPHI","150345") == 
    assert get_Issuing_Date_text("SUN JAN 15 2019",2019,"AFDPHI","150345") == (2019, 1, 15 ,False)
    assert get_Issuing_Date_text("SUN FEB 15 2019",2019,"AFDPHI","150345") == (2019, 2, 15 ,False)
    assert get_Issuing_Date_text("SUN MAR 15 2019",2019,"AFDPHI","150345") == (2019, 3,  15,False)
    assert get_Issuing_Date_text("SUN APR 15 2019",2019,"AFDPHI","150345") == (2019, 4, 15 ,False)
    assert get_Issuing_Date_text("SUN MAY 15 2019",2019,"AFDPHI","150345") == (2019, 5, 15 ,False)
    assert get_Issuing_Date_text("SUN JUN 15 2019",2019,"AFDPHI","150345") == (2019, 6, 15 ,False)
    assert get_Issuing_Date_text("SUN JUL 15 2019",2019,"AFDPHI","150345") == (2019, 7, 15 ,False)
    assert get_Issuing_Date_text("SUN AUG 15 2019",2019,"AFDPHI","150345") == (2019, 8, 15 ,False)
    assert get_Issuing_Date_text("SUN SEP 15 2019",2019,"AFDPHI","150345") == (2019, 9, 15 ,False)
    assert get_Issuing_Date_text("SUN OCT 15 2019",2019,"AFDPHI","150345") == (2019,10, 15 ,False)
    assert get_Issuing_Date_text("SUN NOV 15 2019",2019,"AFDPHI","150345") == (2019,11, 15 ,False)
    assert get_Issuing_Date_text("SUN DEC 15 2019",2019,"AFDPHI","150345") == (2019, 12 , 15 ,False)
    #FULL NAME
    assert get_Issuing_Date_text("MON JANUARY 15 2019",2019,"AFDPHI","150345") == (2019,  1, 15 ,False)
    assert get_Issuing_Date_text("MON FEBRUARY 15 2019",2019,"AFDPHI","150345") == (2019,  2, 15 ,False)
    assert get_Issuing_Date_text("MON MARCH 15 2019",2019,"AFDPHI","150345") == (2019,  3, 15 ,False)
    assert get_Issuing_Date_text("MON APRIL 15 2019",2019,"AFDPHI","150345") == (2019,  4,  15,False)
    assert get_Issuing_Date_text("MON MAY 15 2019",2019,"AFDPHI","150345") == (2019,  5, 15 ,False)
    assert get_Issuing_Date_text("MON JUNE 15 2019",2019,"AFDPHI","150345") == (2019, 6 , 15 ,False)
    assert get_Issuing_Date_text("MON JULY 15 2019",2019,"AFDPHI","150345") == (2019, 7 , 15 ,False)
    assert get_Issuing_Date_text("MON AUGUST 15 2019",2019,"AFDPHI","150345") == (2019, 8 , 15 ,False)
    assert get_Issuing_Date_text("MON SEPTEMBER 15 2019",2019,"AFDPHI","150345") == (2019,  9, 15 ,False)
    assert get_Issuing_Date_text("MON OCTOBER 15 2019",2019,"AFDPHI","150345") == (2019,  10, 15 ,False)
    assert get_Issuing_Date_text("MON NOVEMBER 15 2019",2019,"AFDPHI","150345") == (2019, 11 ,15  ,False)
    assert get_Issuing_Date_text("MON DECEMBER 15 2019",2019,"AFDPHI","150345") == (2019,  12, 15 ,False)
    #0's
    assert get_Issuing_Date_text("SUN SEPT 15 2019",2019,"AFDPHI","150345") == (2019,  9, 15 ,False)
    assert get_Issuing_Date_text("SUN 0CT 15 2019",2019,"AFDPHI","150345") == (2019,  10, 15 ,False)
    assert get_Issuing_Date_text("SUN N0V 15 2019",2019,"AFDPHI","150345") == (2019,  11, 15 ,False)
    assert get_Issuing_Date_text("SUN OCT0BER 15 2019",2019,"AFDPHI","150345") == (2019, 10 ,  15,False)
    assert get_Issuing_Date_text("SUN N0VEMBER 15 2019",2019,"AFDPHI","150345") == (2019, 11 , 15 ,False)
    #no space between week day and month
    assert get_Issuing_Date_text("SUNSEPT 15 2019",2019,"AFDPHI","150345") == (2019,  9,  15,False)
    assert get_Issuing_Date_text("MONJAN 15 2019",2019,"AFDPHI","150345") == (2019,  1, 15 ,False)
    assert get_Issuing_Date_text("SATJUL 15 2019",2019,"AFDPHI","150345") == (2019,  7,  15,False)
    assert get_Issuing_Date_text("SUNSEPTEMBER 15 2019",2019,"AFDPHI","150345") == (2019, 9 ,  15,False)
    #INCORRECT ABBRIVIATIONS/WORDING
    assert get_Issuing_Date_text("SUN OCTO 15 2019",2019,"AFDPHI","150345") == (2019, 10 , 15,False)
    assert get_Issuing_Date_text("SUN NOVEM 15 2019",2019,"AFDPHI","150345") == (2019, 11 , 15 ,False)

    #no space between month and day
    assert get_Issuing_Date_text("SUN SEPT15 2019",2019,"AFDPHI","150345") == (2019,  9, 15 ,False)
    assert get_Issuing_Date_text("MON JAN5 2019",2019,"AFDPHI","150345") == (2019,  1,  5,False)
    assert get_Issuing_Date_text("SAT JUL12 2019",2019,"AFDPHI","150345") == (2019,  7, 12 ,False)
    assert get_Issuing_Date_text("SUN SEPTEMBER15 2019",2019,"AFDPHI","150345") == (2019, 9 , 15 ,False)
    assert get_Issuing_Date_text("SUN AUG15 2019",2019,"AFDPHI","150345") == (2019,  8, 15 ,False)
    assert get_Issuing_Date_text("SUN OCT15 2019",2019,"AFDPHI","150345") == (2019,  10,  15,False)
    assert get_Issuing_Date_text("SUN NOVEMBER15 2019",2019,"AFDPHI","150345") == (2019, 11 ,  15,False)
    assert get_Issuing_Date_text("SUN DECEMBER15 2019",2019,"AFDPHI","150345") == (2019,  12, 15 ,False)

    #OTHER
    assert get_Issuing_Date_text("TUEJAN 15 2019",2019,"AFDPHI","150345") == (2019, 1 ,  15,False)
    assert get_Issuing_Date_text("TUEFEB 15 2019",2019,"AFDPHI","150345") == (2019, 2 ,  15,False)
    assert get_Issuing_Date_text("TUEMAR 15 2019",2019,"AFDPHI","150345") == (2019, 3 ,  15,False)
    assert get_Issuing_Date_text("TUEAPR 15 2019",2019,"AFDPHI","150345") == (2019,  4,  15,False)
    assert get_Issuing_Date_text("TUEMAY 15 2019",2019,"AFDPHI","150345") == (2019, 5 , 15 ,False)
    assert get_Issuing_Date_text("TUEJUN 15 2019",2019,"AFDPHI","150345") == (2019,  6,  15,False)
    assert get_Issuing_Date_text("TUEJUL 15 2019",2019,"AFDPHI","150345") == (2019, 7 ,  15,False)
    assert get_Issuing_Date_text("TUEAUG 15 2019",2019,"AFDPHI","150345") == (2019,  8, 15 ,False)
    assert get_Issuing_Date_text("TUESEP 15 2019",2019,"AFDPHI","150345") == (2019,  9, 15 ,False)
    assert get_Issuing_Date_text("SATURDAYOCT 15 2019",2019,"AFDPHI","150345") == (2019, 10 , 15 ,False)
    assert get_Issuing_Date_text("MONDAYNOV 15 2019",2019,"AFDPHI","150345") == (2019,  11, 15 ,False)
    assert get_Issuing_Date_text("WEDNESDAYDEC 15 2019",2019,"AFDPHI","150345") == (2019, 12 , 15 ,False)    
    
    #No space between day and year
    assert get_Issuing_Date_text("SATJAN 12019",2019,"AFDPHI","150345") == (2019,  1, 1 ,False)
    assert get_Issuing_Date_text("MONFEB 22019",2019,"AFDPHI","150345") == (2019,  2,  2,False)
    assert get_Issuing_Date_text("TUEMAR 202019",2019,"AFDPHI","150345") == (2019,  3, 20 ,False)
    assert get_Issuing_Date_text("WEDAPR 102019",2019,"AFDPHI","150345") == (2019,  4,  10,False)
    assert get_Issuing_Date_text("THURMAY 302009",2009,"AFDPHI","150345") == (2009, 5 ,  30,False)
    assert get_Issuing_Date_text("FRIJUN 312019",2019,"AFDPHI","150345") == (2019,  6,  31,False)
    assert get_Issuing_Date_text("SATJUL 282019",2019,"AFDPHI","150345") == (2019, 7 ,  28,False)
    assert get_Issuing_Date_text("SUNAUG 292019",2019,"AFDPHI","150345") == (2019, 8 ,  29,False)
    assert get_Issuing_Date_text("THUSEP 51999",1999,"AFDPHI","150345") == (1999,  9,  5,False)
    
    #NO SPACES AT ALL
    assert get_Issuing_Date_text("SATURDAY0CT152019",2019,"AFDPHI","150345") == (2019,  10,  15,False) #WITH A 0 in OCT
    assert get_Issuing_Date_text("MONDAYNOV102019",2019,"AFDPHI","150345") == (2019, 11 ,  10,False)
    assert get_Issuing_Date_text("WEDNESDAYDEC152019",2019,"AFDPHI","150345") == (2019, 12 , 15 ,False)   
    
    # NO MONTH INFO   
    assert get_Issuing_Date_text("SUN     15 2019",2019,"AFDPHI","150345") == (None, None, None,None)
    assert get_Issuing_Date_text("SUN15 2019",2019,"AFDPHI","150345") == (None, None ,  None,None)
    assert get_Issuing_Date_text("SUN  15 2019",2019,"AFDPHI","150345") == (None, None , None ,None)
    assert get_Issuing_Date_text("SUN  15 2019",2019,"AFDPHI","150345") == (None,  None, None ,None)
    assert get_Issuing_Date_text("SUN 15 2019",2019,"AFDPHI","150345") == (None, None , None ,None)
    #INCORRECT ABBRIVIATIONS
    assert get_Issuing_Date_text("NEW YEARS 2019",2019,"AFDPHI","150345") == (None,  None, None,None)
    assert get_Issuing_Date_text("CHRISTMAS 2014",2014,"AFDPHI","150345") == (None, None , None,None)
    
    
    
    
def test_get_Issuing_Time_text():
    
    assert get_Issuing_Time_text("1159",datetime(2013,6,6,3,59,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("23","59",'PM', False)
    assert get_Issuing_Time_text("1214 AM",datetime(2013,12,6,5,14,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("00","14",'AM', False)
    assert get_Issuing_Time_text("1130 PM",datetime(2013,12,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("23","30",'PM', False)
    assert get_Issuing_Time_text("1159 A",datetime(2013,6,6,3,59,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("23","59",'PM', False)

    assert get_Issuing_Time_text("NOON",datetime(2013,6,6,16,00,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("12","00",'PM', False)
    assert get_Issuing_Time_text("NOON",datetime(2013,6,6,4,00,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("00","00",'AM', True)
    assert get_Issuing_Time_text("AFTERNOON",datetime(2013,6,6,4,00,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == (None,None,None, None)

    assert get_Issuing_Time_text("1004 PM",datetime(2013,6,6,2,4,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("22","04",'PM', False)
    assert get_Issuing_Time_text("104 AM",datetime(2013,6,6,5,4,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("01","04",'AM', False)
    assert get_Issuing_Time_text("1214 AMPM",datetime(2013,12,6,5,14,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("00","14",'AM', False)
    assert get_Issuing_Time_text("1230 PM AM", datetime(2013,6,6,16,30,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("12","30",'PM', False)
    assert get_Issuing_Time_text("1230 AM PM", datetime(2013,6,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("00","30",'AM', False)
    assert get_Issuing_Time_text("0003 AM",datetime(2013,12,6,5,3,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("00","03",'AM', False) 

    assert get_Issuing_Time_text("1230Z", datetime(2013,12,6,12,30,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("12","30",'PM', False)
    assert get_Issuing_Time_text("1230 Z", datetime(2013,12,6,12,30, tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("12","30",'PM', False)
    assert get_Issuing_Time_text("0030 Z", datetime(2013,12,6,0,30,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("00","30",'AM', False)
    assert get_Issuing_Time_text("500 Z", datetime(2013,12,6,5,0,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("05","00",'AM', False)
    assert get_Issuing_Time_text("1500 Z", datetime(2013,12,6,15,0,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("15","00",'PM', False)
    assert get_Issuing_Time_text("15OO Z", datetime(2013,12,6,15,0,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("15","00",'PM', False)
    assert get_Issuing_Time_text("NMLT Z", datetime(2013,12,6,5,30,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == (None,None,None, None)
    assert get_Issuing_Time_text("2789 Z", datetime(2013,12,6,5,30,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == (None,None,None, None)
    
    assert get_Issuing_Time_text("1230 AM", None, "US/Eastern", "AFDLWX") == ("00","30",'AM', False)
    assert get_Issuing_Time_text("1230 PM", None, "US/Eastern", "AFDLWX") == ("12","30",'PM', False)

    assert get_Issuing_Time_text("1230 AMPM", None, "US/Eastern", "AFDLWX") == ("00","30",'AM', True)
    assert get_Issuing_Time_text("1230 PMAM", None, "US/Eastern", "AFDLWX") == ("12","30",'PM', True)
    assert get_Issuing_Time_text("1230 PM AM", None, "US/Eastern", "AFDLWX") == ("12","30",'PM', True)
    assert get_Issuing_Time_text("1230 AM PM", None, "US/Eastern", "AFDLWX") == ("00","30",'AM', True)
    
    assert get_Issuing_Time_text("1230Z", None, "UTC", "AFDLWX") == ("12","30",'PM', False)
    assert get_Issuing_Time_text("1230 Z", None, "UTC", "AFDLWX") == ("12","30",'PM', False)
    assert get_Issuing_Time_text("0030 Z", None, "UTC", "AFDLWX") == ("00","30",'AM', False)
    assert get_Issuing_Time_text("500 Z", None, "UTC", "AFDLWX") == ("05","00",'AM', False)
    assert get_Issuing_Time_text("1500 Z", None, "UTC", "AFDLWX") == ("15","00",'PM', False)
    assert get_Issuing_Time_text("15OO Z", None, "UTC", "AFDLWX") == ("15","00",'PM', False)
    assert get_Issuing_Time_text("NMLT Z", None, "UTC", "AFDLWX") == (None,None,None, None)
    assert get_Issuing_Time_text("2789 Z", None, "UTC", "AFDLWX") == (None,None,None, None)
    
    assert get_Issuing_Time_text("NOON", None, "US/Eastern", "AFDLWX") == ("12","00",'PM', True)
    assert get_Issuing_Time_text("N00N", None, "US/Eastern", "AFDLWX") == ("12","00",'PM', True)
    assert get_Issuing_Time_text("MIDNIGHT", None, "US/Eastern", "AFDLWX") == ("00","00",'AM', True)
    assert get_Issuing_Time_text("AFTERNOON", None, "US/Eastern", "AFDLWX") == (None,None,None, None)
    assert get_Issuing_Time_text("   ", None, "US/Eastern", "AFDLWX") == (None,None,None, None)
    assert get_Issuing_Time_text("", datetime(2013,12,6,5,30,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == (None,None,None, None)


    assert get_Issuing_Time_text("   ", None, "US/Eastern", "AFDLWX") == (None,None,None, None)
    assert get_Issuing_Time_text(" 12000 PM", datetime(2013,12,6,16,00,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("12","00","PM", False)
    
    
    assert get_Issuing_Time_text("1230 PAM", None, "US/Eastern", "AFDLWX") == ("00","30",'AM', True)
    assert get_Issuing_Time_text("1230 APM", None, "US/Eastern", "AFDLWX") == ("12","30",'PM', True)
    assert get_Issuing_Time_text("130", None, "US/Eastern", "AFDLWX") == ("01","30","AM", True)
    assert get_Issuing_Time_text("1230", None, "US/Eastern", "AFDLWX") == ("12","30","PM", True)
    assert get_Issuing_Time_text("1700", None, "US/Eastern", "AFDLWX") == ("17","00","PM", True)
    
    #KEEP AN EYE ON THIS ONE...
    assert get_Issuing_Time_text("15TH Z", datetime(2013,12,6,15,30,tzinfo=pytz.timezone("UTC")), "UTC", "AFDLWX") == ("15","00","PM", True)
    assert get_Issuing_Time_text("15TH Z", None, "UTC", "AFDLWX") == (None, None, None, None) # BECAUSE AM ANDPM DO NOT MATCH SINCE AMPM is NONE-TYPE
    
    assert get_Issuing_Time_text("MIDNIGHT",datetime(2013,6,6,16,00,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("12","00",'PM', True) # THIS IS CORRECTED IN THE FUNCTION 
    assert get_Issuing_Time_text("MIDNIGHT",datetime(2013,6,6,4,00,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("00","00",'AM', False) # THIS IS CORRECTED IN THE FUNCTION 

    
    # THIS IS AN EXAMPLE OF WRONG TIME BEING PROVIDED -- 11:30 PM being confused with 1:30AM
    assert get_Issuing_Time_text("1130 PMAM",datetime(2013,6,6,5,30,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("11","30",'AM', True)
    assert get_Issuing_Time_text("1130 PMAM",datetime(2013,6,6,3,30,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("23","30",'PM', False) # 11:30 PM being confused with 1:30AM
    assert get_Issuing_Time_text("1159 AMPM",datetime(2013,12,6,4,59,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("23","59",'PM', True) # 12:59 am being confused with 11:59PM
    assert get_Issuing_Time_text("1214 PM",datetime(2013,12,6,5,14,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("12","14",'PM', True) #12:14 am but written as 12:14pm
    assert get_Issuing_Time_text("1130 AM",datetime(2013,12,6,4,30,tzinfo=pytz.timezone("UTC")), "US/Eastern", "AFDLWX") == ("11","30",'AM', True) #11:30 pm but written as 11:30am
    
    
    assert get_Issuing_Time_text("1200 PM",datetime(2009, 4, 13, 16, 55, tzinfo=pytz.timezone("UTC")), "US/Central", "AFDHUN") == ("12","00",'PM', True) #11:30 pm but written as 11:30am
    #THIS IS NOTABLY WRONG ^^^^^^^^^^^^^^^ BASED ON DDHHMM it shouldbe like 11:55 AM not 1200 PM}
    
def test_checkEverything():
    
   #REGULAR
   assert checkEverything("310623", 2018, 6, 31, 2018) ==  (2018, 6, 31, "06", "23", False)
   assert checkEverything("310623", 2018, 12, 31, 2018) ==  (2018, 12, 31, "06", "23", False)
   assert checkEverything("010623", 2018, 1, 1, 2018) ==  (2018, 1, 1, "06", "23", False)
   assert checkEverything("010623", 2018, 12, 31, 2018) == (2019, 1, 1, "06", "23", False)
   assert checkEverything("310623", 2019, 1, 1, 2019) ==  (2018, 12, 31, "06", "23", False)
      
   ## DECEMBER TO JANUARY
   assert checkEverything("010623", 2018, 12, 31, 2018) ==  (2019, 1, 1, "06", "23", False) #Go forward a day to Jan 1 from last day of december. no year change IEM
   assert checkEverything("010623", 1995, 12, 31, 1995) ==  (1996, 1, 1, "06", "23", False)
   
   assert checkEverything("010623", 2018, 12, 31, 2019) ==  (2019, 1, 1, "06", "23", False) #Go forward a day to Jan 1 from last day of december. +1 year change IEM
   
   assert checkEverything("010623", 2018, 12, 31, 2017) ==  (2019, 1, 1, "06", "23", True) #Go forward a day to Jan 1 from last day of december. -1 year IEM plus move to next year

   assert checkEverything("010623", 2019, 12, 31, 2018) ==  (2020, 1, 1, "06", "23", True) #Go forward a day to Jan 1 from last day of december. +1 year change IEM - SHOULD NEVER HAPPEN - REACH THIS POINT
   assert checkEverything("010623", 2017, 12, 31, 2018) ==  (2018, 1, 1, "06", "23", False) #Go forward a day to Jan 1 from last day of december. -1 year IEM plus move to next year

   assert checkEverything("010623", 2016, 12, 31, 2018) ==  (2017, 1, 1, "06", "23", False)
   assert checkEverything("010623", 2018, 12, 31, 2016) ==  (2019, 1, 1, "06", "23", True)
   assert checkEverything("010623", 1995, 12, 31, 1990) == (1996, 1, 1, "06", "23", True)   
   
   #JANUARY BACK TO DECEMBER
   assert checkEverything("310623", 2018, 1, 1, 2018) ==  (2017, 12, 31, "06", "23", False) #Go backwards a day from Jan 1 to last day of december. no year change IEM
   assert checkEverything("310623", 2018, 1, 1, 2019) ==  (2017, 12, 31, "06", "23", True) #Go backwards a day from Jan 1 to last day of december. +1 year change IEM
   
   assert checkEverything("310623", 2018, 1, 1, 2017) ==  (2017, 12, 31, "06", "23", False) #Go backwards a day from Jan 1 to last day of december. -1 year IEM plus move to next year

   assert checkEverything("310623", 2019, 1, 1, 2018) ==  (2018, 12, 31, "06", "23", False) #Go backwards a day from Jan 1 to last day of december. +1 year change IEM
   assert checkEverything("310623", 2017, 1, 1, 2018) ==  (2016, 12, 31, "06", "23", True) #Go backwards a day from Jan 1 to last day of december. -1 year IEM plus move to next year

   assert checkEverything("310623", 1995, 1, 1, 1995) ==  (1994, 12, 31, "06", "23", False)
   assert checkEverything("310623", 2016, 1, 1, 2018) ==  (2015, 12, 31, "06", "23", True)
   assert checkEverything("310623", 2018, 1, 1, 2016) ==  (2017, 12, 31, "06", "23", False)
   assert checkEverything("310623", 1993, 1, 1, 1995) ==  (1992, 12, 31, "06", "23", True)
   assert checkEverything("310623", 1996, 1, 1, 1993) ==  (1995, 12, 31, "06", "23", True)
   
   #MID-YEAR
   assert checkEverything("310623", 2018, 7, 1, 2018) ==  (2018, 6, 31, "06", "23", False) #Go backwards a day from Jan 1 to last day of december. no year change IEM
   assert checkEverything("310623", 2018, 7, 1, 2019) ==  (None, None, None, None, None, None) #Go backwards a day from Jan 1 to last day of december. +1 year change IEM
   
   assert checkEverything("310623", 2018, 7, 1, 2017) ==  (None, None, None, None, None, None) #Go backwards a day from Jan 1 to last day of december. -1 year IEM plus move to next year

   assert checkEverything("310623", 2019, 7, 1, 2018) ==  (None, None, None, None, None, None) #Go backwards a day from Jan 1 to last day of december. +1 year change IEM
   assert checkEverything("310623", 2017, 7, 1, 2018) ==  (None, None, None, None, None, None) #Go backwards a day from Jan 1 to last day of december. -1 year IEM plus move to next year
   
   assert checkEverything("010623", 2018, 6, 31, 2018) ==  (2018, 7, 1, "06", "23", False) #Go forward a day to Jan 1 from last day of december. no year change IEM
   assert checkEverything("010623", 2018, 6, 31, 2019) ==  (None, None, None, None, None, None)#Go forward a day to Jan 1 from last day of december. +1 year change IEM
   
   assert checkEverything("010623", 2018, 6, 31, 2017) ==  (None, None, None, None, None, None) #Go forward a day to Jan 1 from last day of december. -1 year IEM plus move to next year

   assert checkEverything("010623", 2019, 6, 31, 2018) ==  (None, None, None, None, None, None) #Go forward a day to Jan 1 from last day of december. +1 year change IEM
   assert checkEverything("010623", 2017, 6, 31, 2018) ==  (None, None, None, None, None, None) #Go forward a day to Jan 1 from last day of december. -1 year IEM plus move to next year
   
   #MID-YEAR NOT END-TO-START or START-TO-END
   assert checkEverything("010623", 2016, 6, 31, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("300623", 2018, 2, 28, 2018) ==  (None, None, None, None, None, None) # clearly the wrong month...

   assert checkEverything("010623", 2017, 6, 31, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("010623", 2018, 6, 31, 2017) ==  (None, None, None, None, None, None)
   assert checkEverything("010623", 1995, 6, 31, 1994) ==  (None, None, None, None, None, None)

   assert checkEverything("010623", 2018, 6, 27, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("020623", 2018, 6, 31, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("010623", 2018, 6, 3, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("020623", 2018, 6, 10, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("110623", 2018, 6, 8, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("090623", 2018, 6, 2, 2018) ==  (None, None, None, None, None, None)
   
   # iYear/Year don't matchs - DON'T RESOLVE
   assert checkEverything("120623", 2017, 12, 12, 2019) ==  (None, None, None, None, None, None)
   assert checkEverything("050623", 2001, 1, 5, 2003) ==  (None, None, None, None, None, None)
   
   assert checkEverything("120623", 2019, 12, 12, 2017) ==  (None, None, None, None, None, None)
   assert checkEverything("050623", 2003, 1, 5, 2001) ==  (None, None, None, None, None, None)
   
   
   # SHOULD NEVER GET TO HERE....
   assert checkEverything("120623", 2017, 12, 12, 2018) ==  (2017, 12, 12, "06", "23", False)
   assert checkEverything("050623", 2001, 1, 5, 2002) ==  (2002, 1, 5, "06", "23", False)
   
   assert checkEverything("120623", 2018, 12, 12, 2017) ==  (2017, 12, 12, "06", "23", False)
   assert checkEverything("050623", 2002, 1, 5, 2001) ==  (2002, 1, 5, "06", "23", False)
   
   
   assert checkEverything("310623", 2017, 6, 31, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("310623", 2001, 6, 31, 2002) ==  (None, None, None, None, None, None)
   
   assert checkEverything("310623", 2017, 6, 31, 2018) ==  (None, None, None, None, None, None)
   assert checkEverything("310623", 2001, 6, 31, 2002) ==  (None, None, None, None, None, None)