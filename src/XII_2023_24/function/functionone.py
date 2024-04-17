'''
Created on ৪ জুলাই, ২০২৩

@author: ACER
'''


def calcsum(x, y):
    s = x + y
    return s


num1 = float(input('first number - '))
num2 = float(input('second number - '))
sum = calcsum(num1, num2)
print('sum of two numbers are  - ', sum)
sum = calcsum(10, 12)
print('sum of two numbers are  - ', sum)
sum = calcsum(12*2, 14-4)
print('sum of two numbers are  - ', sum)