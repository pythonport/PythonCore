'''
Created on Apr 24, 2026
program to demonstrate the different value being passed as argument in function call.
@author: admin
'''
import math

def calcfx(x, y):
    fx = x + y + 2 * x * y
    return fx


print('1. fx ->', calcfx(2, 3))  # passing literal
a, b = 1, 2
print('2. fx ->', calcfx(a, b))  # passing variable
print('2. fx ->', calcfx(a + 2, b + 3))  # passing expression
print('2. fx ->', calcfx(2 + 2, 7/2))  # passing expression
print('3. fx ->', calcfx(math.sqrt(2), math.pow(3,2)))  # passing expression