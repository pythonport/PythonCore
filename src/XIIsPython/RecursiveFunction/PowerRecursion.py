'''
Created on Jul 27, 2019

@author: admin

Calculate power uisng recursion
'''


def power(x, a):
    if a == 0 :
        return 1
    else :
        return x * power(x, a - 1)


def pewerNonRecursive(x, a):
    res = 1
    if a == 0 :
        return 1
    else :
        for i in range(a) :
           res = res * x
        return res


power5 = power(5, 3)
power6 = pewerNonRecursive(5, 3)
print(power5)
print(power6)
