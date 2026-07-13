'''
Created on Apr 22, 2026

@author: admin
'''
import math

def calcArea(r):
    area = math.pi*r**2
    return area

def CalcPerimeter(r):
    peri = 2*math.pi*r
    return area

r = float(input('Enter radius - '))
area = calcArea(r)
peri = CalcPerimeter(r)
print(f'Area of circle is {area} \nwhose radius is {r}')
print('========')
print(f'Perimeter of circle is {peri} \nwhose radius is {r}')