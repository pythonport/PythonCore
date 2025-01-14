'''
Created on Jan 11, 2025

@author: admin
'''
num = int(input('number - '))
fact = 1
for i in range(1, num+1):
    fact *= num

print('factorial of {} is {}'.format(num, fact))