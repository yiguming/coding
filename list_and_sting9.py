#!/usr/bin/python
def connectlist(list1,list2):
    for item in list2:
	list1.append(item)
    return list1



list1=[1,2,3,4,5]
list2=[2,3,4,5,1,2]


print connectlist(list1,list2)
