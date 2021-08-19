'''
Created on Aug 13, 2021

@author: admin
'''


def calcSum(x, y):
    z = x + y
    print('Local values are -',x, y, z)
    print("Global variable - ",num1)
    print("Global variable sum - ",sum)
    return z


num1 = int(input("Enter first value - "))
num2 = int(input("Enter second value - "))
sum = calcSum(num1, num2)
print('Global values are -',num1, num2, sum)
#print('Local values are -',x, y, z)
