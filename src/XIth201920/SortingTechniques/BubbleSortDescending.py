'''
Created on Jan 13, 2020

@author: admin
'''
#lst = [56, 778, 33, 55, 11, 87, 97]
a = -12

lst = [3, 14, 10, a, 9, 15, 35]
print('Original list is - ', lst)
n = len(lst)
# Traverse throught all list elements

for i in range(n):
    # last i elements are already  in place
    for j in range(0, n - i - 1):
        # traverse the list from 0 to n-i-1
        # swap if the element found is greater
        # then the next element
        if lst[j] < lst[j + 1] :
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print('Sorted list after every pass - ', lst)
    print('*'*20)
print('Sorted list is - ', lst)