#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:07:08 2019

@author: ericallen
"""
from datetime import datetime
def checkEverything(LST, GMT, year, month, text_day, iYear):
    """doc-string"""
    fday = -1
    fmon = -1
    fyr = -1
    is_assumed = False

    dt_lst = datetime.strptime(LST, "%d%H%M")
    if GMT != "999999":
        try:
            dt_gmt = datetime.strptime(GMT, "%d%H%M")
        except:
            dt_gmt = datetime.strptime(LST, "%d%H%M")
            is_assumed = True

        if dt_gmt >= dt_lst:
            if dt_gmt.day == text_day:
                fday = text_day
            elif abs((dt_gmt - dt_lst).days) == 1:
                fday = text_day + 1
            else:
                #if abs((dt_gmt - dt_lst).days) > 1:
                if dt_gmt.day >= 28 and text_day == 1:
                    fday = dt_gmt.day
                    #is_assumed = True # assumed because 28 is February no 30/31
                    month = month - 1
                    if month == 0:
                        month = 12
                        fyr = year - 1
                else:
                    return None, None, None, None, None, None
        else:
            if dt_gmt.day == text_day:
                fday = text_day
            elif abs((dt_lst - dt_gmt).days) == 1:
                fday = dt_gmt.day
            else:
                #if abs((dt_gmt - dt_lst).days) > 1:
                if dt_gmt.day == 1 and text_day >= 28:
                    fday = dt_gmt.day
                    #is_assumed = True # assumed because 28 is February no 30/31
                    month = month + 1
                    if month > 12:
                        month = 1
                        fyr = year + 1
                else:
                    return None, None, None, None, None, None

        fhour = dt_gmt.hour
        fminute = dt_gmt.minute

    else:
        fday = text_day
        fhour = dt_lst.hour
        fminute = dt_lst.minute


    if fyr == -1:
        if year == iYear:
            fyr = year
        elif year == iYear + 1:
            if month == 1:
                fyr = year
            elif month == 12:
                fyr = iYear
            else:
                return None, None, None, None, None, None

        elif year == iYear - 1:
            if month == 12:
                fyr = year
            elif month == 1:
                fyr = iYear
            else:
                return None, None, None, None, None, None
        else:
            return None, None, None, None, None, None

    else:
        if abs(fyr - iYear) <= 1 and month in (1, 12):
            pass
        else:
            is_assumed = True
            fyr = year

    if abs(fyr-iYear) > 1:
        fyr = year
        is_assumed = True


    fmon = month

    return fyr, fmon, fday, fhour, fminute, is_assumed
