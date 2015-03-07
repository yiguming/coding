#!/usr/bin/python
def print_table(alist):
    max_length =0
    for item in alist:
        if len(item) > max_length:
	    max_length = len(item)
    print "*" * (max_length+4)
    for item in alist:
	print "* " + item +(max_length-len(item))*' '+" *"
    print "*" * (max_length+4)	 

testlist = ["Hello", "World", "in", "a", "frame"] 



print_table(testlist)
