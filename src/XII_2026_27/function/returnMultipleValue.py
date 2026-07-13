'''
Created on Jul 10, 2026

@author: admin
'''
def calculator(a,b):
    sum = a+b
    diff = a-b
    mult = a*b
    div = a/b
    return (sum, diff, mult, div)

tval = calculator(25, 10)
print(tval)