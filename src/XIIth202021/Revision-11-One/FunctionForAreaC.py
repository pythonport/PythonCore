'''
Created on Mar 2, 2021

@author: admin
'''
import math

def calcarea(radius):
    area = math.pi*radius**2
    return area
    
r = float(input("Enter radius - "))
a = calcarea(r)
print("Area of circle is - ",a)
print("Area of circle is - ",calcarea(r))