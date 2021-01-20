'''
Created on Jan 16, 2021

@author: admin
'''
import random
rnum = random.randint(10, 17)
a = 0
while a < 5 :
    gnum = int(input("Enter any number between[10:17] - "))
    if gnum == rnum :
        print("YOU WON ....")
        break
    a += 1

if a >= 5:
    print("you lose.. Actual Number was - ",rnum)
