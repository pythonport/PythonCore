'''
Created on Jul 27, 2019
Factorial using recursion
@author: admin
'''


def factorialRecursion(n):
    if n <= 0 :
        return 1
    else :
        return n * factorialRecursion(n - 1)
    

num = int(input("Enter number for calculage factorial - "))
fact = factorialRecursion(num)

print('Factorial of %d is - %d'%(num,fact))
