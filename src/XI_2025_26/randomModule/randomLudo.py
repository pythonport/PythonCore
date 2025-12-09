'''
Created on Nov 29, 2025

@author: admin
'''
import random

name = input('user name - ')
for i in range(1, 4):
    num = random.randint(1, 6)
    print('number is - ',num)
    if num == 6:
        print(name,' WON... at ', i, 'times')
        break
else:
    print(name,' Sorry better luck next time')
    
