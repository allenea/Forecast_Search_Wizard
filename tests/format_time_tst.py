#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:21:38 2019

@author: ericallen
"""

def test_get_issuing_date_text1():
    """docstring"""
    #FULL NAME
    assert get_Issuing_Date_text("SUN JANUARY 7 1902", 2002, "PMDTHR", "070534") == \
                (2002, 1, 7, False)
    assert get_Issuing_Date_text("SUN JANUARY 5 1901", 2001, "PMDTHR", "050534") == \
                (2001, 1, 5, False)
    assert get_Issuing_Date_text("SUN DECEMBER 23 1900", 2000, "PMDTHR", "230534") == \
                (2000, 12, 23, False)

    assert get_Issuing_Date_text("SUN JANUARY 7 1902", 2002, "AFDLWX", "070534") == \
                (2002, 1, 7, True)
    assert get_Issuing_Date_text("SUN JANUARY 5 1901", 2001, "AFDLWX", "050534") == \
                (2001, 1, 5, True)
    assert get_Issuing_Date_text("SUN DECEMBER 23 1900", 2000, "AFDLWX", "230534") == \
                (2000, 12, 23, True)

    assert get_Issuing_Date_text("SUN JANUARY 1 2018", 2017, "PMDTHR", "010534") == \
                (2018, 1, 1, False) # JAN -1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN JANUARY 7 2017", 2017, "PMDTHR", "070534") == \
                (2017, 1, 7, False)
    assert get_Issuing_Date_text("SUN JANUARY 5 2017", 2018, "PMDTHR", "050534") == \
                (2017, 1, 5, True)#FORGOT TO CHANGE THE YEAR
    assert get_Issuing_Date_text("SUN DECEMBER 23 2017", 2017, "PMDTHR", "230534") == \
                (2017, 12, 23, False)
    assert get_Issuing_Date_text("SUN DECEMBER 15 2018", 2017, "PMDTHR", "150534") == \
                (2018, 12, 15, True) # DEC -1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN DECEMBER 19 2017", 2018, "PMDTHR", "190534") == \
                (2017, 12, 19, False) # DEC +1YR EXCEPTION - USE LOWER

    assert get_Issuing_Date_text("SUN JULY 21 2018", 2017, "PMDTHR", "210534") == \
                (2018, 7, 21, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017", 2018, "PMDTHR", "280534") == \
                (2017, 7, 28, True) #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018", 2017, "PMDTHR", "300534") == \
                (2018, 7, 30, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2017", 2018, "PMDTHR", "310534") == \
                (2017, 7, 31, True) #WARN USE TEXT - MORE REALISTIC

    assert get_Issuing_Date_text("SUN JANUARY 1 2018", 2017, "AFDPHI", "010534") == \
                (2018, 1, 1, False) # JAN -1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN JANUARY 7 2017", 2017, "AFDPHI", "070534") == \
                (2017, 1, 7, False)
    assert get_Issuing_Date_text("SUN JANUARY 5 2017", 2018, "AFDPHI", "050534") == \
                (2017, 1, 5, True) #FORGOT TO CHANGE THE YEAR
    assert get_Issuing_Date_text("SUN DECEMBER 23 2017", 2017, "AFDPHI", "230534") == \
                (2017, 12, 23, False)
    assert get_Issuing_Date_text("SUN DECEMBER 15 2018", 2017, "AFDPHI", "150534") == \
                (2018, 12, 15, True) # DEC -1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN DECEMBER 19 2017", 2018, "AFDPHI", "190534") == \
                (2017, 12, 19, False) # DEC +1YR EXCEPTION - USE LOWER

    assert get_Issuing_Date_text("SUN JULY 21 2018", 2017, "AFDMHX", "210534") == \
                (2018, 7, 21, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017", 2018, "AFDMHX", "280534") == \
                (2017, 7, 28, True) #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018", 2017, "AFDMHX", "300534") == \
                (2018, 7, 30, True) #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2017", 2018, "AFDMHX", "310534") == \
                (2017, 7, 31, True) #WARN USE TEXT - MORE REALISTIC

    #"HPC FORECAST VALID 00 UTC 9 FEB THRU 00 UTC 16 FEB 2001"  - NO ASSUMPTIONS
    assert get_Issuing_Date_text("9 FEB 2001", 2001, "PMDHI", "090000") == \
                (2001, 2, 9, False)

    #HPC FORECAST VALID 00 UTC 06 JAN 2001 THRU 00 UTC 13 JAN  2001  - NO ASSUMPTIONS (DOUBLE YEAR)
    assert get_Issuing_Date_text("06 JAN 2001 2001", 2001, "PMDHI", "060000") == \
                (2001, 1, 6, False)

    assert get_Issuing_Date_text("WED APR 15 1980", 1980, "AFDPHI", "150345") == \
                (1980, 4, 15, False)
    assert get_Issuing_Date_text("TUR MAY 15 2013", 2013, "AFDPHI", "150345") == \
                (2013, 5, 15, False)
    assert get_Issuing_Date_text("FRI JUN 15 2015", 2015, "AFDPHI", "150345") == \
                (2015, 6, 15, False)
    assert get_Issuing_Date_text("WED AUG 15 2014", 2014, "AFDPHI", "150345") == \
                (2014, 8, 15, False)
    assert get_Issuing_Date_text("SUN OCT 152018", 2018, "AFDPHI", "150345") == \
                (2018, 10, 15, False)
    assert get_Issuing_Date_text("SUN DEC 152000", 2000, "AFDPHI", "150345") == \
                (2000, 12, 15, False)
    assert get_Issuing_Date_text("SUN JANUARY 15 2001", 2001, "AFDPHI", "150345") == \
                (2001, 1, 15, False)
    assert get_Issuing_Date_text("MON FEBRUARY 15 2003", 2003, "AFDPHI", "150345") == \
                (2003, 2, 15, False)
    assert get_Issuing_Date_text("MARCH 15 2005", 2005, "AFDPHI", "150345") == \
                (2005, 3, 15, False)
    assert get_Issuing_Date_text("SUN APRIL 15 2012", 2012, "AFDPHI", "150345") == \
                (2012, 4, 15, False)
    assert get_Issuing_Date_text(" MAY 15 2007", 2007, "AFDPHI", "150345") == \
                (2007, 5, 15, False)
    assert get_Issuing_Date_text("FRI JUNE 15 2009", 2009, "AFDPHI", "150345") == \
                (2009, 6, 15, False)
    assert get_Issuing_Date_text("JULY 15 2010", 2010, "AFDPHI", "150345") == \
                (2010, 7, 15, False)
    assert get_Issuing_Date_text("THU AUGUST 15 2011", 2011, "AFDPHI", "150345") == \
                (2011, 8, 15, False)
    assert get_Issuing_Date_text("TUE SEPTEMBER 15 2004", 2004, "AFDPHI", "150345") == \
                (2004, 9, 15, False)
    assert get_Issuing_Date_text("OCTOBER 15 2002", 2002, "AFDPHI", "150345") == \
                (2002, 10, 15, False)
    assert get_Issuing_Date_text("SAT NOV 1520000", 2000, "AFDPHI", "150345") == \
                (2000, 11, 15, False)
    assert get_Issuing_Date_text("FRIDAY SEP 152019", 2019, "AFDPHI", "150345") == \
                (2019, 9, 15, False)
    assert get_Issuing_Date_text("1000 AM TUE MAR 15 2020", 2020, "AFDPHI", "150345") == \
                (2020, 3, 15, False)
    assert get_Issuing_Date_text("TUE MAR 15 2020", 2020, "AFDPHI", "150345") == \
                (2020, 3, 15, False)
    assert get_Issuing_Date_text("TUE DEC 31 2020", 2019, "AFDPHI", "150345") == \
                (2020, 12, 31, True)  # USE iYEAR #MOVED YEAR AHEAD TOO EARLY


def test_get_issuing_date_text2():
    """docstring"""
    PIL = "AFDPHI"
    F = False
    T = True
    assert get_Issuing_Date_text("SUN AFA 15 2013", 2013, PIL, "150345") == (None, None, None, None)
    assert get_Issuing_Date_text("SUN JAN 15 1903", 2003, PIL, "150345") == (2003, 1, 15, T)
    assert get_Issuing_Date_text("MON FEB 15 1900", 2000, PIL, "150345") == (2000, 2, 15, T)
    assert get_Issuing_Date_text("TUE DEC 2019", 2019, PIL, "150345") == (2019, 12, None, T)
    assert get_Issuing_Date_text("MON N0VEMBER 15 1893", 2013, PIL, "150345") == (2013, 11, 15, T)
    # USE iYEAR...
    assert get_Issuing_Date_text(" DECEMBER 15 1133", 2015, PIL, "150345") == (2015, 12, 15, T)
    assert get_Issuing_Date_text("TUE DEC 31", 2019, PIL, "150345") == (2019, 12, 31, T)

    #GO WITH SMALLER YEAR
    assert get_Issuing_Date_text("SUN JULY 21 2018", 2017, PIL, "210534") == (2018, 7, 21, T)
    #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017", 2018, PIL, "280534") == (2017, 7, 28, T)
    #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018", 2017, PIL, "300534") == (2018, 7, 30, T)
    #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2017", 2018, PIL, "310534") == (2017, 7, 31, T)
    #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JANUARY 1 2018", 1995, PIL, "010534") == (1995, 1, 1, T)
    # JAN -1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN JANUARY 5 2012", 2018, PIL, "050534") == (2012, 1, 5, T)
    # JAN +1YR EXCEPTION - USE HIGHER
    assert get_Issuing_Date_text("SUN DECEMBER 12 2018", 1998, PIL, "120534") == (1998, 12, 12, T)
    # DEC -1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN DECEMBER 15 2000", 2018, PIL, "150534") == (2000, 12, 15, T)
    # DEC +1YR EXCEPTION - USE LOWER
    assert get_Issuing_Date_text("SUN JULY 21 2018", 2001, PIL, "210534") == (2001, 7, 21, T)
    #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 28 2017", 2019, PIL, "280534") == (2017, 7, 28, T)
    #WARN USE TEXT - MORE REALISTIC
    assert get_Issuing_Date_text("SUN JULY 30 2018", 2009, PIL, "300534") == (2009, 7, 30, T)
    #WARN 2018 hasn't happened yet
    assert get_Issuing_Date_text("SUN JULY 31 2013", 2017, PIL, "310534") == (2013, 7, 31, T)
    #WARN USE TEXT - MORE REALISTIC

    #MISSING YEAR
    assert get_Issuing_Date_text("SUN JAN 15", 2019, PIL, "150345") == (2019, 1, 15, T)
    assert get_Issuing_Date_text("SUN FEB 15", 1996, PIL, "150345") == (1996, 2, 15, T)

    assert get_Issuing_Date_text("SUN JAN 15 2019", 2019, PIL, "150345") == (2019, 1, 15, F)
    assert get_Issuing_Date_text("SUN FEB 15 2019", 2019, PIL, "150345") == (2019, 2, 15, F)
    assert get_Issuing_Date_text("SUN MAR 15 2019", 2019, PIL, "150345") == (2019, 3, 15, F)
    assert get_Issuing_Date_text("SUN APR 15 2019", 2019, PIL, "150345") == (2019, 4, 15, F)
    assert get_Issuing_Date_text("SUN MAY 15 2019", 2019, PIL, "150345") == (2019, 5, 15, F)
    assert get_Issuing_Date_text("SUN JUN 15 2019", 2019, PIL, "150345") == (2019, 6, 15, F)
    assert get_Issuing_Date_text("SUN JUL 15 2019", 2019, PIL, "150345") == (2019, 7, 15, F)
    assert get_Issuing_Date_text("SUN AUG 15 2019", 2019, PIL, "150345") == (2019, 8, 15, F)
    assert get_Issuing_Date_text("SUN SEP 15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    assert get_Issuing_Date_text("SUN OCT 15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("SUN NOV 15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)
    assert get_Issuing_Date_text("SUN DEC 15 2019", 2019, PIL, "150345") == (2019, 12, 15, F)
    #FULL NAME
    assert get_Issuing_Date_text("MON JANUARY 15 2019", 2019, PIL, "150345") == (2019, 1, 15, F)
    assert get_Issuing_Date_text("MON FEBRUARY 15 2019", 2019, PIL, "150345") == (2019, 2, 15, F)
    assert get_Issuing_Date_text("MON MARCH 15 2019", 2019, PIL, "150345") == (2019, 3, 15, F)
    assert get_Issuing_Date_text("MON APRIL 15 2019", 2019, PIL, "150345") == (2019, 4, 15, F)
    assert get_Issuing_Date_text("MON MAY 15 2019", 2019, PIL, "150345") == (2019, 5, 15, F)
    assert get_Issuing_Date_text("MON JUNE 15 2019", 2019, PIL, "150345") == (2019, 6, 15, F)
    assert get_Issuing_Date_text("MON JULY 15 2019", 2019, PIL, "150345") == (2019, 7, 15, F)
    assert get_Issuing_Date_text("MON AUGUST 15 2019", 2019, PIL, "150345") == (2019, 8, 15, F)
    assert get_Issuing_Date_text("MON SEPTEMBER 15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    assert get_Issuing_Date_text("MON OCTOBER 15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("MON NOVEMBER 15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)
    assert get_Issuing_Date_text("MON DECEMBER 15 2019", 2019, PIL, "150345") == (2019, 12, 15, F)
    assert get_Issuing_Date_text("SUN SEPT 15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)

def test_get_issuing_date_text3():
    """docstring"""
    #0's
    PIL = "AFDPHI"
    F = False
    assert get_Issuing_Date_text("SUN 0CT 15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("SUN N0V 15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)
    assert get_Issuing_Date_text("SUN OCT0BER 15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("SUN N0VEMBER 15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)
    #no space between week day and month
    assert get_Issuing_Date_text("SUNSEPT 15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    assert get_Issuing_Date_text("MONJAN 15 2019", 2019, PIL, "150345") == (2019, 1, 15, F)
    assert get_Issuing_Date_text("SATJUL 15 2019", 2019, PIL, "150345") == (2019, 7, 15, F)
    assert get_Issuing_Date_text("SUNSEPTEMBER 15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    #INCORRECT ABBRIVIATIONS/WORDING
    assert get_Issuing_Date_text("SUN OCTO 15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("SUN NOVEM 15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)

    #no space between month and day
    assert get_Issuing_Date_text("SUN SEPT15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    assert get_Issuing_Date_text("MON JAN5 2019", 2019, PIL, "150345") == (2019, 1, 5, F)
    assert get_Issuing_Date_text("SAT JUL12 2019", 2019, PIL, "150345") == (2019, 7, 12, F)
    assert get_Issuing_Date_text("SUN SEPTEMBER15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    assert get_Issuing_Date_text("SUN AUG15 2019", 2019, PIL, "150345") == (2019, 8, 15, F)
    assert get_Issuing_Date_text("SUN OCT15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("SUN NOVEMBER15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)
    assert get_Issuing_Date_text("SUN DECEMBER15 2019", 2019, PIL, "150345") == (2019, 12, 15, F)

    #OTHER
    assert get_Issuing_Date_text("TUEJAN 15 2019", 2019, PIL, "150345") == (2019, 1, 15, F)
    assert get_Issuing_Date_text("TUEFEB 15 2019", 2019, PIL, "150345") == (2019, 2, 15, F)
    assert get_Issuing_Date_text("TUEMAR 15 2019", 2019, PIL, "150345") == (2019, 3, 15, F)
    assert get_Issuing_Date_text("TUEAPR 15 2019", 2019, PIL, "150345") == (2019, 4, 15, F)
    assert get_Issuing_Date_text("TUEMAY 15 2019", 2019, PIL, "150345") == (2019, 5, 15, F)
    assert get_Issuing_Date_text("TUEJUN 15 2019", 2019, PIL, "150345") == (2019, 6, 15, F)
    assert get_Issuing_Date_text("TUEJUL 15 2019", 2019, PIL, "150345") == (2019, 7, 15, F)
    assert get_Issuing_Date_text("TUEAUG 15 2019", 2019, PIL, "150345") == (2019, 8, 15, F)
    assert get_Issuing_Date_text("TUESEP 15 2019", 2019, PIL, "150345") == (2019, 9, 15, F)
    assert get_Issuing_Date_text("SATURDAYOCT 15 2019", 2019, PIL, "150345") == (2019, 10, 15, F)
    assert get_Issuing_Date_text("MONDAYNOV 15 2019", 2019, PIL, "150345") == (2019, 11, 15, F)
    assert get_Issuing_Date_text("WEDNESDAYDEC 15 2019", 2019, PIL, "150345") == (2019, 12, 15, F)

    #No space between day and year
    assert get_Issuing_Date_text("SATJAN 12019", 2019, PIL, "150345") == (2019, 1, 1, F)
    assert get_Issuing_Date_text("MONFEB 22019", 2019, PIL, "150345") == (2019, 2, 2, F)
    assert get_Issuing_Date_text("TUEMAR 202019", 2019, PIL, "150345") == (2019, 3, 20, F)
    assert get_Issuing_Date_text("WEDAPR 102019", 2019, PIL, "150345") == (2019, 4, 10, F)
    assert get_Issuing_Date_text("THURMAY 302009", 2009, PIL, "150345") == (2009, 5, 30, F)
    assert get_Issuing_Date_text("FRIJUN 312019", 2019, PIL, "150345") == (2019, 6, 31, F)
    assert get_Issuing_Date_text("SATJUL 282019", 2019, PIL, "150345") == (2019, 7, 28, F)
    assert get_Issuing_Date_text("SUNAUG 292019", 2019, PIL, "150345") == (2019, 8, 29, F)
    assert get_Issuing_Date_text("THUSEP 51999", 1999, PIL, "150345") == (1999, 9, 5, F)

    #NO SPACES AT ALL
    assert get_Issuing_Date_text("SATURDAY0CT152019", 2019, PIL, "150345") == (2019, 10, 15, F)
        #WITH A 0 in OCT
    assert get_Issuing_Date_text("MONDAYNOV102019", 2019, PIL, "150345") == (2019, 11, 10, F)
    assert get_Issuing_Date_text("WEDNESDAYDEC152019", 2019, PIL, "150345") == (2019, 12, 15, F)

    # NO MONTH INFO
    assert get_Issuing_Date_text("SUN     15 2019", 2019, PIL, "150345") == (None, None, None, None)
    assert get_Issuing_Date_text("SUN15 2019", 2019, PIL, "150345") == (None, None, None, None)
    assert get_Issuing_Date_text("SUN 15 2019", 2019, PIL, "150345") == (None, None, None, None)

    #INCORRECT ABBRIVIATIONS
    assert get_Issuing_Date_text("NEW YEARS 2019", 2019, PIL, "150345") == (None, None, None, None)
    assert get_Issuing_Date_text("CHRISTMAS 2014", 2014, PIL, "150345") == (None, None, None, None)
