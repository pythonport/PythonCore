'''
Created on Jul 27, 2019
GCD using recursion
@author: admin
'''


def getGCD(a, b):
    if b == 0:
        return a
    return getGCD(b, a % b)


fnum = int(input("Enter first number - "))
snum = int(input("Enter second number - "))

gcd = getGCD(fnum, snum)

print('GCD of %d and %d is - %d' % (fnum, snum, gcd))
