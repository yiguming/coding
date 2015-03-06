#!/usr/bin/python
def hebing(list1,list2):
    new_list = []
    for i in list1:
	new_list.append(i)
    for i in list2:
	new_list.append(i)
    new_list.sort()
    return new_list




list1 = [1,2,3,4,5]

list2 = [3,4,5,7,9,11]

print hebing(list1,list2)
