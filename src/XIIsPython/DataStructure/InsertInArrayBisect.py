'''
Created on Aug 14, 2019
Inserting in sorted array using bisect module
@author: admin
'''

import bisect
lst =  [11,22,33,55,66,77,78,79,89]
print("Actual list in sorted order is - ")
print(lst)

item = int(input("Enter element to be inserted - "))
pos = bisect.bisect(lst, item)
bisect.insort(lst, item)

print("Item inserted at index - ",pos)
print(lst)