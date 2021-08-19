import math

def calcSum(a,b,c): 
    s = a+b+c
    return s

def average(x, y, z):
    sm = calcSum1(x, y, z)
    return sm/3

num1 = int(input("Enter first value - "))
num2 = int(input("Enter second value - "))
num3 = int(input("Enter third value - "))
print('Average of three number - ',average(num1, num2, num3))