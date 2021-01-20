'''
Created on Jan 8, 2021
find the min, mid max out of three number
@author: admin
'''

a = int(input("Enter first number - "))
b = int(input("Enter second number - "))
c = int(input("Enter third number - "))

min = mid = max = None

if a < b and a < c :
    if b < c :
        min, mid, max = a, b, c
    else:
        min, mid, max = a, c, b
elif b < a and b < c :    
    if a<c :
        min, mid, max = b, a, c
    else :
        min, mid, max = b, c, a
else :
    if a <b :
        min, mid, max = c, a, b
    else :
        min, mid, max = c, b, a
            
print('Min = ',min)           
print('Mid = ',mid)           
print('Max = ',max)           
