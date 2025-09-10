'''
Created on Aug 26, 2025

@author: admin
'''
#program to calculate the power of 2 till n term
base = 2
power = 4
product = base
counter = 1
while (counter < power):
    product = product * base
    counter += 1
print('power of {} till {} is {}'.format(base, power, product)) 