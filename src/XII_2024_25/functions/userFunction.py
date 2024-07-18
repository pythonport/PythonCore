'''
Created on Jul 5, 2024

@author: admin
'''

def calcfx(x, y):
    fx = 5 * x ** 6 + 4 * x * y + 2 * x * y
    return fx


a, b = 10, 20
fx = calcfx(a, b)
print('Calculated fx is - ', fx)

fx = calcfx(22, 24)
print('Calculated fx is - ', fx)
