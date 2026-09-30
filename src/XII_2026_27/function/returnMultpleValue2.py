'''
Created on Jul 13, 2026

@author: admin
'''


def calculator(a, b):
    sum = a + b
    diff = a - b
    mult = a * b
    div = a / b
    return sum, diff, mult, div


a = 25
b = 12
w, x, y, z = calculator(a, b)

print(f'sum of {a} and {b} is {w}')
print(f'Diff of {a} and {b} is {x}')
print(f'Mult of {a} and {b} is {y}')
print(f'Div of {a} and {b} is {z}')
