'''
Created on Nov 30, 2023

@author: Admin
'''
print('='*40)
print('Guess a number game, 3 attempt max')
import random
rnum = random.randint(1,6)
for i in range(3) :
    num = int(input('Number between 1 to 6 - '))
    if rnum == num :
        print('You won')
        break
else :
    print("Sorry! Bad Luck!")
    print('The number is - ',rnum)
print('='*40)
input('Press ENTER to exit') 