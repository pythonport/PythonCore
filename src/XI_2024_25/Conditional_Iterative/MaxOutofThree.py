'''
Created on Dec 30, 2024

@author: admin
'''
num1 = int(input('Enter first number - '))
num2 = int(input('Enter second number - '))
num3 = int(input('Enter third number - '))
min = mid = max = 0

if num1 < num2 and num1 < num3:
    if num2 < num3:
        min, mid, max = num1, num2, num3
    else: 
        min, mid, max = num1, num3, num2
elif num2 < num1 and num2 < num3: 
    if num1 < num3:
        min, mid, max = num2, num1, num3
    else: 
        min, mid, max = num2, num3, num1
else:
    if num1 < num2:
        min, mid, max = num3, num1, num2
    else: 
        min, mid, max = num3, num2, num1

print(min, mid, max)
