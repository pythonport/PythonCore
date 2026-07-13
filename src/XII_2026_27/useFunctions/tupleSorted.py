'''
Created on Apr 6, 2026
Write a python program to input a tuple t1 and sort its elements. At the end of the program,
all the elements of the tuple t1 should be sorted in ascending order.
@author: admin
'''

t1 = eval(input('Enter tuple - '))
print(f'Unsorted tuple is {t1}')
sortedlist = sorted(t1)
print(sortedlist)
t1 = tuple(sortedlist)
print(f'Sorted tuple is {t1}')
