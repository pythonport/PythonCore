'''
Created on Dec 29, 2020
generate two integer number 
and print their aveage
@author: admin
'''

import random

rnum1 = random.randint(450,950)
rnum2 = random.randint(450,950)
avg = (rnum1+rnum2)/2

print("Random 1 - ",rnum1)
print("Random 2 - ",rnum2)
print("Average of these two are - ",avg)