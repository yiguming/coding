def odd_print(alist):
    oddindexlist=[]
    for i in range(0,len(alist),2):
	oddindexlist.append(alist[i])
    return oddindexlist



list1=[1,2,3,4,5,6,7,8,9,10]
list2=[1,2,3,4,5,6,7,8,9,10,11]


print "list1"
print list1
print "odd index number"
print odd_print(list1)
print "\n"


print "list2"
print list2
print "odd index number"
print odd_print(list2)


