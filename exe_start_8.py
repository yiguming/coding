#!/usr/bin/python
import math
def isPrime(n):
    res = True
    if n <=1:
        res = True
    for i in range(2,int(math.sqrt(n))+1):
	if n % i == 0:
	   res = False
    return res

n = int(raw_input("Please input a number :"))

lst = [x for x in range(n+1) if isPrime(x)]

#print lst

for i in lst:
   print i,
