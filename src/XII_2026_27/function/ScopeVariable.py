'''
Created on Jul 13, 2026

@author: admin
'''
def calcSum(x, y):
    print('x -',x )
    print('num1 - ',num1)
    z = x+y
    return z

num1 = int(input('First number - '))
num2 = int(input('Second number - '))
sum = calcSum(num1, num2)
print(f'sum of {num1} and {num2} - {sum}')

'''
Global variable - num1, num2, sum
Local variable - x, y, z
'''