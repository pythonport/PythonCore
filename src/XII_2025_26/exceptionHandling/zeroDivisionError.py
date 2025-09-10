'''
Created on Sep 1, 2025
Program to demonstrate the use of exception handling for zeroDivisionError
@author: admin
'''

num = int(input('Enter numerator - '))
dnum = int(input('Enter denominator - '))
try :
    div = num/dnum
    print('Value after division of {} and {} is {}'.format(num, dnum, div))
except ZeroDivisionError:
    print('Denominator can not be zero')
