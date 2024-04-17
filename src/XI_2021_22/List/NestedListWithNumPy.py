'''
Created on Feb 14, 2022

@author: admin
'''
import numpy

lst = [[6, 5, 4, 6, 5], [4, 9, 8, 7, 6], [3, 4, 5, 1, 2], [3, 5, 6, 7, 8]]
print(lst)
narray = numpy.asarray(lst)
print(narray)
lst[2][4] =88
lst[2] = 88
print(lst)