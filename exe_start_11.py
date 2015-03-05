#!/usr/bin/env python
def computer(k):
    beichushu = (-1)**(k+1)
    chushu = 2 * k -1
    result = float(beichushu) / chushu
    return result 
sum =0
for i in range(1,10**6+1):
    sum += computer(i)


print sum
