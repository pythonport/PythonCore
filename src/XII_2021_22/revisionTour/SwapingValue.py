'''
Created on Apr 16, 2021
Swaping value in python
@author: admin
'''

a,b = 90,56
print('a - ',a)
print('b - ',b)
print('-------')

temp = a
a = b
b = temp
print('a - ',a)
print('b - ',b)
print('-------')

#python way of swapping
a,b = b,a
print('a - ',a)
print('b - ',b)
print('-------')