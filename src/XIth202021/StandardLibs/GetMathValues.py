'''
Created on Dec 11, 2020
Get Sin, Cos, Tan, cot, Sec and Cosec value
using math module.
@author: admin
'''
import math

degree = float(input("Enter value in degree - "))
radianValue = math.radians(degree)
sin = math.sin(radianValue)
cos = math.cos(radianValue)
tan = math.tan(radianValue)
cot = 1/tan
sec = 1/cos
cosec = 1/sin

#print("Sin value of ", degree, " is ",sin)
print("Sin value of {0} is {1}".format(degree, sin))
print("Cos value of {0} is {1}".format(degree, cos))
print("Tan value of {0} is {1}".format(degree, tan))
print("Cot value of {0} is {1}".format(degree, cot))
print("Sec value of {0} is {1}".format(degree, sec))
print("Cosec value of {0} is {1}".format(degree, cosec))
