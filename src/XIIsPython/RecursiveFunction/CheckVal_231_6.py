'''
Created on Sep 18, 2019

@author: admin
'''


def check(n):
    if n <= 1:
        return True
    elif n % 2 == 0:
        return check(n / 2)
    else:
        return check(n / 1)

    
def express(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return express(n * x, n / 2)
    else:
        return x * express(x, n - 1)
    
# print(check(8))
print(express(2,5))
