'''
Created on Apr 19, 2021
Calculation of sqrt of any number using math module
and new style of string formating
@author: admin
'''
import math

num = int(input("Enter any number - "))
sqnum = math.sqrt(num)
print('square root of ', num, ' is - ', sqnum)
print('square root of {0} is - {1}'.format(num,sqnum))