'''
Created on Oct 10, 2024

@author: admin
'''
a = int(input('Enter nominator - '))
b = int(input('Enter denominator - '))

assert b!=0, (str(b)+' can not be zero')

print(a/b)