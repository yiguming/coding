#!/usr/bin/python
def nizhuan(alist):
    return alist[::-1]

list1= [1,2,3,4,5,6,7,8,9,10]
print list1

print "After all list ordered ,Method1"
print nizhuan(list1)




#Reverse part of the list
#e.g. a= [1,2,3,4,5,6], reverse "3,4,5" so that a = [1,2,5,4,3,6]
def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

a = [1,2,3,4,5,6]
left = 2
right =4

print a 

mid = (right - left ) /2 + left
for i in range(left,mid+1):
   swap(a,left,right + left -i)


print "after part of list orderd "
print a
