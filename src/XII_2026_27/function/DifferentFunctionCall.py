'''
Created on Apr 20, 2026

@author: admin
'''
import math

def cube(x):
    res = x**3
    return res

print(cube(5))

a = 15
print(cube(a))

num = int(input('Enter number = '))
print(cube(num))

print(2*cube(10))

rcube = cube(10)
sqroot = math.sqrt(rcube)
print(f'square root of {rcube} is {sqroot}')