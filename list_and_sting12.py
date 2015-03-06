#!/usr/bin/python
def Fibonacci(n):
    fib_list = []
    a,b = 0,1
    count =0
    while (1):
	fib_list.append(b)
	count +=1
	a,b = b,a+b
	if count >n-1:
	    break
    return fib_list


print Fibonacci(5)
print "-------------"
print Fibonacci(100)
