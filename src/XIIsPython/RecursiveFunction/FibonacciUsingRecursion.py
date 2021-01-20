'''
Created on Jul 27, 2019

@author: admin
'''


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else :
        return fib(n - 1) + fib(n - 2)


num = int(input("Enter number for calculage febonacii Term - "))
for i in range(1, num):
    print(fib(i), end=',')
