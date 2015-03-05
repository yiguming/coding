def maxnum_oflist(alist):
    max = alist[0]
    for item in alist:
	if item > max:
	    max = item
    return max

list1 = [11,23,12,34,13,24,5,6,34,11,33,44]

print maxnum_oflist(list1)
