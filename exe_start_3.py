#!/usr/bin/env python
while (1):
    name = raw_input("Please input the name and you only can say hello to Alice or Bob:")
    if name == "Alice":
    	print "Hello," + name
	break
    elif name =="Bob":
    	print "Hello," + name
	break
    else:
        print "input error!"



