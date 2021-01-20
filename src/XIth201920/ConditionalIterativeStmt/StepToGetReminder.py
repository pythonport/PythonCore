'''
Created on Sep 14, 2019
program to get reminder of numbers
@author: admin
'''
num1 = int(input("Enter first number - "))
num2 = int(input("Enter second number - "))
rem = num1%num2
if rem==0:
    print(num1," is divisible by ",num2)
else :
    print(num1," is not divisible by ",num2)