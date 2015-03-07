def insertion_sort(n):
    if len(n) == 1:
        return n
    b = insertion_sort(n[1:])
    m = len(b)
    for i in range(m):
        if n[0] <= b[i]:
            return b[:i]+[n[0]]+b[i:]
    return b + [n[0]]

def insertion_sort2(lst):
    if len(lst) == 1:
        return
 
    for i in xrange(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp > lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
print('Before selection sort: {}'.format(testlist))

print('After selection sort:  {}'.format(insertion_sort(testlist)))


print('Before selection sort: {}'.format(testlist))

print('After selection sort:  {}'.format(insertion_sort2(testlist)))






