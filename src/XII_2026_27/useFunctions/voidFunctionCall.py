'''
Created on Apr 23, 2026
Python program to demonstrate the use of return statement and function without return statement
@author: admin
'''
import math

def calcArea(r):
    a = math.pi*r**2
    print('at line 10 - ',a)
    return a

r = float(input('Enter radius - '))
area = calcArea(r)
print(f'Area of circle is {area} \nwhose radius is {r}')