'''
Created on Aug 10, 2024

@author: admin
'''
import random

#generate random float value between 0.0<=n<1
print(random.random())

#generate random int value between a<=n<=b range
print(random.randint(1,6))

#generate random float value between a<=n<b range
r1 = random.random()*(60-50)+50
print(r1)

#generate random float value between a<=n<b range
print(random.uniform(1,2))