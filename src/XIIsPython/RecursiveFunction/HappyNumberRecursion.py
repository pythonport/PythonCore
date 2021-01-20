'''
Created on Sep 18, 2019

@author: admin
'''


def sum_sq_digits(n):
    b = len(str(n)) - 1
    x = 10 ** b
    if b == 0:
        return n ** 2
    else:
        return (n // x) ** 2 + sum_sq_digits(n - (n // x) * x)
    
def ishappy(num):
    rval = sum_sq_digits(num)
    if len(str(rval)) == 1:
        if rval == 1:
            return True
        else :
            return False
    else :
        return ishappy(rval)

    
num = int(input("Enter number to check happy number - "))
if ishappy(num):
    print(num, " is a happy number and final output is 1")
else :
    print(num, " is not a happy number and final output is not 1")
    
