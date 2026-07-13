'''
Created on Apr 23, 2026

@author: admin
'''
def calcSum(x,y):
    s = x+y
    print(x,y,s)
    print('I am going back from function')
    return s

num1 = float(input('First number - '))
num2 = float(input('Second number - '))
sum = calcSum(num1, num2)
print(f'Sum of {num1} and {num2} is {sum}')