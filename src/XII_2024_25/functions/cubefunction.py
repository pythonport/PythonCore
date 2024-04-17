'''
Created on Apr 9, 2024

@author: admin
'''

def cube(a):
    return a*a*a

print(cube(10))


x = 9999999999400000000059999999998
print(cube(x))

xval = int(input('Enter data to calculate cube - '))
print(cube(xval))

doublecube = 2*cube(x)
print(doublecube)