'''
Created on Dec 24, 2025

@author: admin
'''
x = int(input('First number - '))
y = int(input('Second number - '))
z = int(input('Third number - '))

min = mid = max = None

if x<y and x<z :
    if y<z :
        min, mid, max = x, y, z
    else :
        min, mid, max = x, z, y
        
elif y<x and y<z :
    if x<z :
        min, mid, max = y, x, z
    else :
        min, mid, max = y, z, x
        
else :
    if x<y :
        min, mid, max = z, x, y
    else :
        min, mid, max = z, y, x

print('Actual order data  - ',x, y, z)
print('Assending order data  - ',min, mid, max)