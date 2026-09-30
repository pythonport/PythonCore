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

a = 25
b = 12
tval = calculator(a, b)
print(tval)
print(f'sum of {a} and {b} is {tval[0]}')
print(f'Diff of {a} and {b} is {tval[1]}')
print(f'Mult of {a} and {b} is {tval[2]}')
print(f'Div of {a} and {b} is {tval[3]}')