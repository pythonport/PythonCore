'''
Created on Dec 16, 2023

@author: Admin
'''
import random
num = 5
for j in range (3):
    for i in range(5):
        rnum = random.randint(1, 6)
        print(num + rnum, end=' ')
    print()
