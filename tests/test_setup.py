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
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.check_vars import search_option, input_words, AndTrue_OrFalse, byforecast,\
         set_year_range, makeAssumptions, grep_check, debug_check, check_if_substring
from search_options.search_options import Option


def test_and_true_or_false():
    """docstring"""
    assert AndTrue_OrFalse(True)
    assert AndTrue_OrFalse(False) == False
    assert AndTrue_OrFalse(None) is None
    assert AndTrue_OrFalse("Yes") is None
    assert AndTrue_OrFalse("NO") is None
    assert AndTrue_OrFalse(["True"]) is None
    assert AndTrue_OrFalse("None") is None
    assert AndTrue_OrFalse("True") is None
    assert AndTrue_OrFalse("False") is None
    assert AndTrue_OrFalse("") is None


def test_byforecast():
    """docstring"""
    assert byforecast(True)
    assert byforecast(False) == False
    assert byforecast(None) is None
    assert byforecast("Yes") is None
    assert byforecast("NO") is None
    assert byforecast(["True"]) is None
    assert byforecast("None") is None
    assert byforecast("True") is None
    assert byforecast("False") is None
    assert byforecast("") is None


def test_make_assumptions():
    """docstring"""
    assert makeAssumptions(True)
    assert makeAssumptions(False) == False
    assert makeAssumptions(None) is None
    assert makeAssumptions("Yes") is None
    assert makeAssumptions("NO") is None
    assert makeAssumptions(["True"]) is None
    assert makeAssumptions("None") is None
    assert makeAssumptions("True") is None
    assert makeAssumptions("False") is None
    assert makeAssumptions("") is None

def test_grep_check():
    """docstring"""
    assert grep_check(True)
    assert grep_check(False) == False
    assert grep_check(None) is None
    assert grep_check("Yes") is None
    assert grep_check("NO") is None
    assert grep_check(["True"]) is None
    assert grep_check("None") is None
    assert grep_check("True") is None
    assert grep_check("False") is None
    assert grep_check("") is None


def test_debug_check():
    """docstring"""
    assert debug_check(True)
    assert debug_check(False) == False
    assert debug_check(None) is None
    assert debug_check("Yes") is None
    assert debug_check("NO") is None
    assert debug_check(["True"]) is None
    assert debug_check("None") is None
    assert debug_check("True") is None
    assert debug_check("False") is None
    assert debug_check("") is None

def test_set_year_range():
    """docstring"""
    assert set_year_range(1996, 2019) == (1996, 2019)
    assert set_year_range(1996, 2020) == (None, None)
    assert set_year_range(1995, 2019) == (None, None)
    assert set_year_range(1995, 2020) == (None, None)
    assert set_year_range(1990, 2010) == (None, None)
    assert set_year_range(2015, 2010) == (2010, 2015) # bigger number first
    assert set_year_range(2001, 2008) == (2001, 2008)
    assert set_year_range("2001", "2010") == (2001, 2010) #as string
    assert set_year_range("Hello", "World") == (None, None)
    assert set_year_range(2010, 2030) == (None, None)
    assert set_year_range(2021, 2025) == (None, None)
    assert set_year_range(None, None) == (None, None)
    assert set_year_range(2019, 2019) == (2019, 2019) # same year


def test_search_option():
    """docstring"""
    #VALID
    assert search_option(Option.ALL)
    assert search_option(Option.ALL_SPC)
    assert search_option(["SWOMCD", "VOWLWX", "AFDPHI"])
    assert search_option(["AFDPHI"])
    assert search_option(["AFDPHI", "", "VOWLWX"])
    assert search_option(list(set(Option.ALL) - set(Option.ALL_SPC)))

    #INVALID (not a list, integer value, not a list, empty list, basically empty)
    assert search_option(set(Option.ALL) - set(Option.ALL_SPC)) is None
    assert search_option(["SWOMCD", 1984, "AFDPHI"]) is None
    assert search_option("AFDPHI") is None
    assert search_option([]) is None
    assert search_option([""]) is None


def test_input_words():
    """docstring"""
    is_grep = True
    is_grep2 = False

    assert input_words(["THE"], is_grep) == ["THE"]
    assert input_words(["THE"], is_grep2) == [" THE "]

    assert input_words(["the"], is_grep) == ["THE"]
    assert input_words(["the"], is_grep2) == [" THE "]

    assert input_words(["2000"], is_grep) == ["2000"]
    assert input_words(["2000"], is_grep2) == [" 2000 "]

    assert input_words(["Rain"], is_grep) == ["RAIN"]
    assert input_words(["Rain"], is_grep2) == [" RAIN "]

    lst = ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES",\
           "SEABREEZE", "SEABREAZES", "SEABREAZE", "SEA BREEZES", "SEA BREAZES"]

    assert input_words(lst, is_grep) == ["SEA BREEZE", "SEA BREAZE", "SEABREEZE", "SEABREAZE"]
    assert input_words(lst, is_grep2) == [" SEA BREEZE ", " SEA BREAZE ", " SEABREEZES ", \
                      " SEABREEZE ", " SEABREAZES ", " SEABREAZE ", " SEA BREEZES ", \
                      " SEA BREAZES "]

    lst2 = ["The", "the", "tHe", "thE", "THe", "tHE", "THE", "ThE"]
    assert input_words(lst2, is_grep) == ["THE"]
    assert input_words(lst2, is_grep2) == [" THE "]

    assert input_words("Hello", is_grep) == ["HELLO"]
    assert input_words("Hello", is_grep2) == [" HELLO "]

    assert input_words(["1"], is_grep) == ["1"]
    assert input_words(["1"], is_grep2) == [" 1 "]

    lst5 = ["The", "the", "tHe", "thE", "THESE", "tHE", "THE", "ThE", "there", "them"]
    assert input_words(lst5, is_grep) == ["THE"]
    assert input_words(lst5, is_grep2) == [" THE ", " THESE ", " THERE ", " THEM "]

    assert input_words([], is_grep) is None
    assert input_words([], is_grep2) is None

    assert input_words([" "], is_grep) is None
    assert input_words([" "], is_grep2) is None

    assert input_words([""], is_grep) is None
    assert input_words([""], is_grep2) is None

    lst3 = ["HURRICANE", 1984, "SURGE"]
    assert input_words(lst3, is_grep) is None
    assert input_words(lst3, is_grep2) is None

    lst6 = "HURRICANE", "SURGE"
    assert input_words(lst6, is_grep) is None
    assert input_words(lst6, is_grep2) is None

def test_check_if_substring():
    """docstring"""
    lst5 = ["The", "the", "tHe", "thE", "THESE", "tHE", "THE", "ThE", "there", "them"]

    lst = ["Sea breeze", "Sea breaze", "SEA BREEZE", "SEABREEZES", "SEABREEZE", "SEABREAZES",\
           "SEABREAZE", "SEA BREEZES", "SEA BREAZES"]

    lst2 = ["TEST", "This", "OUT", "BRO"]

    assert check_if_substring(lst5) == ["THE"]
    assert check_if_substring(lst) == ["SEA BREEZE", "SEA BREAZE", "SEABREEZE", "SEABREAZE"]
    assert check_if_substring(lst2) == ["TEST", "THIS", "OUT", "BRO"]
