'''
Created on Dec 9, 2025

@author: admin
'''
x = y = z = 0

x = int(input('First Number = '))
y = int(input('Second Number = '))
z = int(input('Third Number = '))

max = x

if y > max:
    max = y
if z > max:
    max = z
    
print('Entered value - ', x, y, z)
print('Maximum value is - ', max)
