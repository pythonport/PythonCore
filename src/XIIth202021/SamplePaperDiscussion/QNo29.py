'''
Created on Dec 17, 2020
Get the correct output and find the value of 
LOWER AND UPPER    
@author: admin
'''
import random

AR=[20,30,40,50,60,70]
Lower =random.randint(1,3)  #MAX VALUE = 3
Upper =random.randint(2,4)  #MAX VALUE = 4
for K in range(Lower, Upper +1):
    print (AR[K],end='#')