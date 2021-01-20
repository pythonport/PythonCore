'''
Created on Jul 2, 2019

@author: admin
'''

def areaOfT(b,h):
    area = 0.5*b*h
    return area


base  = int(input("Enter base of triangle- "))
height = int(input("Enter height of triange - "))

resultArea  = areaOfT(base, height)

print("Area of triangel is- ",resultArea)

r = areaOfT(23, 12)
print("Area of second triangel is- ",r)