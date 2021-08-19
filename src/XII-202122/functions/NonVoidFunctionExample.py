'''
Created on Aug 2, 2021

@author: admin
'''
import math


def calculateCircleData(r):
    areac = math.pi * r ** 2
    peri = 2 * math.pi * 2
    dia = 2 * r
    return areac, peri, dia


r = 5
tpldata = calculateCircleData(r)
print("return of calculateCircleData -  ", tpldata)

a , p, d = calculateCircleData(r)
print('Area - ', a)
print('Perimeter - ', p)
print('Diameter  - ', d)
    
