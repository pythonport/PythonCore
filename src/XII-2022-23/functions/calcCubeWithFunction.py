'''
Created on May 5, 2022

@author: admin
'''
def cube(x):
    cval = x**3
    return cval

#main starts here  __main__
print("Name of block ",__name__)
c1 = cube(4.5)
print("Cube value is - ", c1)

a = 5
c1 = cube(a)
print("Cube value is - ", c1)

b = int(input("Enter number to calculate cube - "))
c1 = cube(b)
print("Cube value is - ", c1)

d1 = 2*cube(8)
print("Cube value is - ", d1)