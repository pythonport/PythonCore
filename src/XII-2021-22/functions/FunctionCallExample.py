'''
Created on Jul 23, 2021
Function Call statement
@author: admin
'''

def cube(x):
    res = x**3
    return res

print('Cube value is - ',cube(8))  #passing literal
num = 10
print('Cube value is - ',cube(num))  #passing variable

uinput = int(input('Enter any number to get cube - '))
print('Cube value is - ',cube(uinput))  #taking input and pass

doubleVal = 2*cube(uinput)  #function call in expression
print('Double Cube value is - ',doubleVal)  #taking input and pass