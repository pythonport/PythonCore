'''
Created on Dec 21, 2024
Exception Handling in python
@author: admin
'''
try :
    a = int(input('Nominator - '))
    b = int(input('Denominator - '))
    print(a/b)
except ZeroDivisionError :
    print('denominator can not be zero')
except :
    print('Something wrong')