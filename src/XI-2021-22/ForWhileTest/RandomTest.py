'''
Created on Apr 11, 2022

@author: admin
'''
import random

for i in range(5) :
    num = random.random()
    print("Random number -", num)
print("================")
for i in range(3) :
    num = random.randint(1, 6)
    print("Random number -", num)
