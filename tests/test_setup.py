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
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.check_vars import search_option, input_words, AndTrue_OrFalse, byforecast, set_year_range, makeAssumptions, grep_check, debug_check, check_if_substring
from search_options.search_options import Option


def test_AndTrue_OrFalse():
    assert AndTrue_OrFalse(True) ==True
    assert AndTrue_OrFalse(False) == False
    assert AndTrue_OrFalse(None) == None
    assert AndTrue_OrFalse("Yes") == None
    assert AndTrue_OrFalse("NO") == None
    assert AndTrue_OrFalse(["True"]) == None
    assert AndTrue_OrFalse("None") == None
    assert AndTrue_OrFalse("True") == None
    assert AndTrue_OrFalse("False") == None
    assert AndTrue_OrFalse("") == None

def test_byforecast():
    assert byforecast(True) ==True
    assert byforecast(False) == False
    assert byforecast(None) == None
    assert byforecast("Yes") == None
    assert byforecast("NO") == None
    assert byforecast(["True"]) == None
    assert byforecast("None") == None
    assert byforecast("True") == None
    assert byforecast("False") == None
    assert byforecast("") == None


def test_makeAssumptions():
    assert makeAssumptions(True) ==True
    assert makeAssumptions(False) == False
    assert makeAssumptions(None) == None
    assert makeAssumptions("Yes") == None
    assert makeAssumptions("NO") == None
    assert makeAssumptions(["True"]) == None
    assert makeAssumptions("None") == None
    assert makeAssumptions("True") == None
    assert makeAssumptions("False") == None
    assert makeAssumptions("") == None

def test_grep_check():
    assert grep_check(True) ==True
    assert grep_check(False) == False
    assert grep_check(None) == None
    assert grep_check("Yes") == None
    assert grep_check("NO") == None
    assert grep_check(["True"]) == None
    assert grep_check("None") == None
    assert grep_check("True") == None
    assert grep_check("False") == None
    assert grep_check("") == None
    
    
def test_debug_check():
    assert debug_check(True) ==True
    assert debug_check(False) == False
    assert debug_check(None) == None
    assert debug_check("Yes") == None
    assert debug_check("NO") == None
    assert debug_check(["True"]) == None
    assert debug_check("None") == None
    assert debug_check("True") == None
    assert debug_check("False") == None
    assert debug_check("") == None

def test_set_year_range():
    
    assert set_year_range(1996,2019) == (1996, 2019)
    assert set_year_range(1996,2020) == (None, None)
    assert set_year_range(1995,2019) == (None, None)
    assert set_year_range(1995,2020) == (None, None)
    assert set_year_range(1990, 2010) == (None, None)
    assert set_year_range(2015, 2010) == ( 2010, 2015)
    assert set_year_range(2001,2008) == (2001,2008)
    assert set_year_range("2001","2010") == (2001  ,2010)
    assert set_year_range("Hello","World") == (None  ,None)
    assert set_year_range(2010,2030) == (None, None)
    assert set_year_range(2021,2025) == (None, None)
    assert set_year_range(None,None) == (None, None)
    assert set_year_range(2019,2019) == (2019, 2019)

    
def test_search_option():
    lst1 =["SWOMCD", 1984, "AFDPHI"]
    lst2 =["SWOMCD", "VOWLWX", "AFDPHI"]
    lst3 = "AFDPHI"
    lst4 = ["AFDPHI", "", "VOWLWX"]
    assert search_option(Option.ALL) == True
    assert search_option(Option.ALL_SPC) == True
    #assert search_option(Option.ALL - Option.ALL_SPC) == TypeError # PHYSICALLY IMPOSSIBLE - Python crashes anyways...
    assert search_option(set(Option.ALL) - set(Option.ALL_SPC)) == None
    assert search_option(list(set(Option.ALL) - set(Option.ALL_SPC))) == True
    assert search_option(lst1) == None
    assert search_option(lst2) == True
    assert search_option(lst3) == None
    assert search_option([lst3]) == True
    assert search_option([]) == None
    assert search_option([""]) == None
    assert search_option(lst4) == True

        
def test_input_words():
    isGrep = True
    isGrep2 = False

    assert input_words(["THE"], isGrep) == ["THE"]
    assert input_words(["THE"], isGrep2) == [" THE "]

    assert input_words(["the"], isGrep) == ["THE"]
    assert input_words(["the"], isGrep2) ==  [" THE "]
    
    assert input_words(["2000"], isGrep) == ["2000"]
    assert input_words(["2000"], isGrep2) == [" 2000 "]

    assert input_words(["Rain"], isGrep) == ["RAIN"]
    assert input_words(["Rain"], isGrep2) == [" RAIN "]
    
    lst = ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES", "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"]
    ## PASSED WITHOUT check_if Substring IMPLEMENTED
    #assert input_words(lst, isGrep) ==     ["SEA BREEZE", "SEA BREAZE", "SEABREEZES", "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"] # WITHOUT REMOVING DUPLICATE SUBSTRINGS FOR GREP STYLE
    assert input_words(lst, isGrep) ==     ["SEA BREEZE", "SEA BREAZE", "SEABREEZE", "SEABREAZE"]
    assert input_words(lst, isGrep2) ==    [" SEA BREEZE ", " SEA BREAZE ", " SEABREEZES ", " SEABREEZE ", " SEABREAZES ", " SEABREAZE ", " SEA BREEZES ", " SEA BREAZES "]
    
    lst2 = ["The", "the", "tHe", "thE", "THe", "tHE", "THE", "ThE"]
    assert input_words(lst2, isGrep) ==  ["THE"]
    assert input_words(lst2, isGrep2) == [" THE "]
    
    assert input_words([], isGrep) == None
    assert input_words([], isGrep2) == None
    
    assert input_words([" "], isGrep) == None
    assert input_words([" "], isGrep2) == None
    
    assert input_words([""], isGrep) == None
    assert input_words([""], isGrep2) == None
    

    assert input_words("Hello", isGrep) == ["HELLO"]
    assert input_words("Hello", isGrep2) == [" HELLO "]
    
    assert input_words(["1"], isGrep) == ["1"]
    assert input_words(["1"], isGrep2) == [" 1 "]
    
    lst3 =["HURRICANE", 1984, "SURGE"]
    assert input_words(lst3, isGrep) == None
    assert input_words(lst3, isGrep2) == None
    
    lst6 = "HURRICANE", "SURGE"
    assert input_words(lst6, isGrep) == None
    assert input_words(lst6, isGrep2) == None
    
    lst5 = ["The", "the", "tHe", "thE", "THESE", "tHE", "THE", "ThE","there", "them"]
    assert input_words(lst5, isGrep) ==  ["THE"]
    assert input_words(lst5, isGrep2) == [" THE ", " THESE "," THERE "," THEM "]
    

def test_check_if_substring():
    lst5 = ["The", "the", "tHe", "thE", "THESE", "tHE", "THE", "ThE","there", "them"]
    lst = ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES", "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"]
    lst2 = ["TEST","This","OUT","BRO"]
    assert check_if_substring(lst5) ==  ["THE"]
    assert check_if_substring(lst) ==   ["SEA BREEZE", "SEA BREAZE", "SEABREEZE", "SEABREAZE"]
    assert check_if_substring(lst2) ==  ["TEST","THIS","OUT","BRO"]