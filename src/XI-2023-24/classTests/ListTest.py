'''
Created on Mar 1, 2024

@author: Admin

Write a python program to reverse an array of integer in place.
like [3,4,2,1]  will convert into [1,2,4,3]
'''

lst = [3, 4, 2, 1]
lst1 = []
for i in range(-1, -len(lst) - 1, -1):
    lst1.append(lst[i])

print(lst)
print(lst1)
