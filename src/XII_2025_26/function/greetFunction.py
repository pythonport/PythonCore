'''
Created on Apr 11, 2025

@author: admin
'''
import math
def perimeterCircle(r):
    peri = 2*math.pi*r
    return peri

r = 5
peri = perimeterCircle(r)
print('Perimeter of {} is {}'.format(r, peri))