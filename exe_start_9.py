#!/usr/bin/python
import random
secret_num =  random.randint(1,10)
count = 0
while (1):
    number_input = int(raw_input("Please input a number range from 1 to 100: (include 1 and 100): "))
    if number_input > secret_num :
	print "Sorry,you guess is too big!the right number is a small one!"
        count +=1
    elif number_input < secret_num :
	print "Sorry,you guess is too small! the right number is a big one!"
	count +=1 
    else:
	print "Congraulation!"
	count +=1
	break

print "The right number is " + str(secret_num) 
print "You have guess " +str(count) + " times " 
