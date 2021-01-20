'''
Created on Jul 12, 2019

@author: admin
To generate floatting point number between the range
'''
import random as rn
rnum = rn.randint(5, 10)
print(rnum)

ub = 15
lb = 5
for i in range(3):
    print(rn.random() * (ub - lb) + lb)