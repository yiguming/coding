#!/usr/bin/python
import math
def is_wanquan(n):
    a = (int)(math.sqrt(n) + 0.5)
    if a * a == n:
	return True
    else:
	return False

def top20(alist):
    toplist=[]
    for i in range(len(alist)):
        if is_wanquan(alist[i]):
	   toplist.append( alist[i])
    if len(toplist) >20:
	return toplist[0:20]
    else:
	return toplist
	 	
	
	

#print is_wanquan(9)
#print is_wanquan(5)
alist =[1,4,9,16,33]
alist1 =[1,4,9]
alist2 = [1,4,9,16,25]
alist3 = [1,2,3,4,5,6,7,8,11,2,3,41,5213,545,325,345,3456,6,256,2456,2,534,524,234321,16,1,4,9,16,25,36,49,1,2,3,4,5,6,7,8,11,2,3,41,5213,545,325,345,3456,6,256,2456,2,534,524,234321,16,1,4,9,16,25,36,49]

print top20(alist)
print top20(alist1)
print top20(alist2)
print top20(alist3)
