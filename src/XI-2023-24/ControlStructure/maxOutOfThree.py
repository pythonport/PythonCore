'''
Created on Dec 1, 2023

@author: Admin
'''
x = y = z = 0
x = int(input('Value of x - '))
y = int(input('Value of y - '))
z = int(input('Value of z - '))

max = x

if y > max:
    max = y
if z > max:
    max = z

print('largest number is - ', max)
