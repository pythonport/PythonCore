'''
Created on Aug 26, 2019

@author: admin
'''
import numpy as np
'''
lst = [i for i in range(23,35,2)]
print(lst)
print(type(lst))

arr = np.array(lst)
print(arr)
print(type(arr))
print(arr.dtype)
'''
ar2 = np.arange(2,12,2)
print(ar2)
print(ar2.dtype)

ar3  = np.linspace(2, 5, 6)
print("Linspace = ",ar3)
print(ar3.dtype)
print(ar3+2)