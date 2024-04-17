'''
Created on Mar 7, 2022

@author: admin
'''
from timeitd import timeit

@timeit(number=10000, unit="ns")
def generateList():
    a = (x in range(10))
    print(a)

