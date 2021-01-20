'''
Created on Dec 14, 2020
Float random number in range
@author: admin
'''
import random
import math
ub = 95
lb = 45
rnum = (ub - lb) * random.random() + lb
nextInt = math.ceil(rnum)

print("random number - ", rnum)
print("Next integer is - ", nextInt)