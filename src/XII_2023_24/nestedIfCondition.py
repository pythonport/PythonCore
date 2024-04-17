'''
Created on Dec 5, 2023

@author: Admin
'''
x = int(input("Enter first number - "))
y = int(input("Enter second number - "))
z = int(input("Enter third number - "))
min = mid = max = None

if x <= y and x <= z:
    print('in if')
    if y <= z:
        min, mid, max = x, y, z
    else:
        min, mid, max = x, z, y
elif y <= x and y <= z:
    print('in elif')
    if x <= z:
        min, mid, max = y, x, z
    else:
        min, mid, max = y, z, x
else:
    print('in else')
    if x <= y:
        min, mid, max = z, x, y
    else:
        min, mid, max = z, y, x   
        
print("Number in ascending order is - ", min, mid, max)
