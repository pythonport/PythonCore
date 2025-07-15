'''
Created on Jul 9, 2025

@author: admin
'''


def calcsum(a, b):
    s = a + b
    r =100
    print('ID Inside - ',id(r))
    print('value of r - ', r)
    return s


r = 100
print('ID outside - ',id(r))
num1 = int(input('Enter first - '))
num2 = int(input('Enter second - '))


print('sum is - ', calcsum(num1, num2))
print('value of r - ', r)
