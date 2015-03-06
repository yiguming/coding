#!/usr/bin/python
def jiaoti_connect(list1,list2):
    new_list=[]
    for i in range(len(list1)):
	new_list.append(list1[i])
	new_list.append(list2[i]) 
    return new_list


list1 = ['a','b','c']
list2 = [1,2,3]

print jiaoti_connect(list1,list2)
