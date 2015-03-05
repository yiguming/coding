#!/usr/bin/python
def is_huiwen(string):
    if string == string[::-1]:
        return True
    else:
	return False


def is_huiwen2(string):
    res = True
    for i in range(len(string)/2):
        if string[i] != string[len(string) -i -1]:
	    res = False
    return res
	   


string1 = "aaabbbaaa"
string2 = "lenel"
string3 = "abbbcccaa"

print "Function 1"
print is_huiwen(string1)
print is_huiwen(string2)
print is_huiwen(string3)


print "Function 2"
print is_huiwen2(string1)
print is_huiwen2(string2)
print is_huiwen2(string3)
