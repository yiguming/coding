#!/usr/bin/python
# while funtion
def sum1(alist):
    i = 0 
    sum =0
    while(i<len(alist)):
	sum +=alist[i]
	i +=1
    return sum




# for funtion 
def sum2(alist):
    sum =0
    for i in range(len(alist)):
	sum +=alist[i]
    return sum    



#def sum3(alist):
#    if len(alist) == 1:
#	alist[0]
#    else:    
#	return [len(alist)-1] + sum3(len(alist)-1)








# digui funtion
#def sum3(alist):
#    if len(alist) == 1:
#	return alist[0]
#    return alist[len(alist)-1] + sum3(len(alist)-1)




list1 =[2,2,3,4,5]
print sum1(list1)
print sum2(list1)
print sum(list1)



