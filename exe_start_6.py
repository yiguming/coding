#!/usr/bin/python
import random
n = int(raw_input("Please input a number : "))
def he(number):
    sum = 0
    for i in range(number+1):
	sum +=i
    return sum

def ji(number):
    ji = 1
    for i in range(1,number+1):
	ji *= i
    return ji

result = random.random()
if (result < 0.5):
   print "he is :" +str(he(n))
else:
   print "ji is :" +str(ji(n))
	
	
