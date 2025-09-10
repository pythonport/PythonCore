'''
Created on Aug 8, 2025

@author: admin
'''
try :
    a = int(input('input nominator - '))
    b = int(input('input denominator - '))
    div = a/b
    
    print('{}/{} is - {}'.format(a,b,div))
except ZeroDivisionError :
    print('Sabdhan! math skill sudharen')