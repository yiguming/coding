#!/usr/bin/python
def returnlist(n,alist):
    newlist =[]
    i =0
    while (i < n):
        newlist.append(alist[i])
	i +=1
    return newlist

list1= [1,2,3,4,5,6,1,2,3,5]
print returnlist(4,list1)
print returnlist(5,list1)
