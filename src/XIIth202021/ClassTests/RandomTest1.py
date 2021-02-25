'''
Created on Feb 15, 2021

@author: admin
'''
import random
pick = random.randint(0, 3)
print("pick value is - ",pick)
city = ['DELHI', 'MUMBAI', 'CHENNAI', 'KOLKATA']
for i in city :
    for j in range(1, pick) :
        print(i, end='')
    print()
