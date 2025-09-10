'''
Created on Sep 6, 2025
Program to demonstrate the use of raise/throw/force exception
@author: admin
'''
try :
    a = int(input('Numerator - '))
    b = int(input('Denominator - '))
    
    if b==0:
        raise ZeroDivisionError('{}/{} is not possible'.format(a,b))
    print(a/b)
except ZeroDivisionError as e:
    print(e)