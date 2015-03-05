#!/usr/bin/python
import time
def sumlist(alist):
    sum =0
    for i in alist:
	sum +=i
    return sum 

costime = 0

def computertime(alist):
    #costime = 0
    start = time.clock()
    sumlist(alist)
    end =time.clock()
    print("The function run time is : %.03f seconds" %(end-start))

numberlist =[]
for i in range(10000000):
    numberlist.append(i)


computertime(numberlist)

