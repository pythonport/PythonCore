'''
Created on Jun 19, 2020

@author: admin
'''
x = int(input("Enter first number - "))
y = int(input("Enter second number - "))
z = int(input("Enter third number - "))
min = mid = max = None

minx = x < y and x < z #named condition
miny = y < x and y < z #named condtion

if minx :           #use of named conditon
    if y < z :
        min, mid, max = x, y, z
    else :
        min, mid, max = x, z, y
elif miny :
    if x < z :
        min, mid, max = y, x, z
    else :
        min, mid, max = y, z, x
else :
    if x < y :
        min, mid, max = z, x, y
    else :
        min, mid, max = z, y, x   
        
print("Numer in ascending order is - ",min,mid,max)