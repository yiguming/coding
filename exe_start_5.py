#!/usr/bin/env python
#input a number and print the sum of the 3 or 5 de beishu 
n = int(raw_input("Please input a number: "))
sum = 0
i=1
for i in range(1,n+1):
    if (i % 3 == 0) or (i % 5 ==0):  
	sum += i

print sum



