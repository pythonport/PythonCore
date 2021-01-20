'''
Created on Dec 14, 2020
use of randint function
will generate number a<=n<=b
@author: admin
'''
import random

rnum1 = random.randint(1,6)
rnum2 = random.randint(1,6)
rnum3 = random.randint(1,6)

if(rnum1==6 or rnum2==6 or rnum3==6) :
    print('***YOU WON***')
else :
    print('YOU LOSE')