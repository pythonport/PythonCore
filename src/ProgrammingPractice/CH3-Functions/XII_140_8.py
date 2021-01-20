'''
Created on Jul 11, 2019

@author: admin
Program to write function to take input of two number and return the 
number whose one place having small number as 431 and 234 then value
returned by function should 431
'''


def getSmallestOnes(a, b):
    '''
    if a % 10 <= b % 10 :
        return a
    else :
        return b
    '''
    return a if (a % 10 <= b % 10) else b

    
a = int(input('Enter first number - '))
b = int(input('Enter second number - '))
smallOne = getSmallestOnes(a, b)
print("Number with smallest one is  - ", smallOne)
