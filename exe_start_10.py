#!/usr/bin/env python
def is_leapyear(year):
    res = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100  !=0):
        res = True
    return res

year = 2015
count = 0
while (True):
    year +=1
    if is_leapyear(year):
        print year
        count +=1
    if count == 20:
        break


~                         
