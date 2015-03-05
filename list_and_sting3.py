#!/usr/bin/python
def if_inthelist(item,alist):
    res = False
    for i in alist:
	if item == i:
	    res = True
    return res


list1 = [1,2,3,4,5,6,7,8]
list2 = ['a','b','c','d','e','f','g','h']


print if_inthelist(1,list1)
print if_inthelist(9,list1)


print if_inthelist('a',list2)
print if_inthelist('i',list2)
