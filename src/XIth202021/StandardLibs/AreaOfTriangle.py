'''
Created on Dec 29, 2020

@author: admin
'''
import math
a, b, c = 7, 5, 9

s = (a + b + c) / 2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("S value is - ",s)
print("Area value is - ",area)