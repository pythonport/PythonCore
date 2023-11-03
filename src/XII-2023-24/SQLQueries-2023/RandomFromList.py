'''
Created on Apr 11, 2022

@author: admin
'''
import random
list = ['Karan','amit','anup','soni','sadhna']

num = random.randint(0, (len(list)-1))
print("First Lucky person is - ", list[num])

print("======== Second way =======")
print("Second Lucky person is - ", random.choice(list))    