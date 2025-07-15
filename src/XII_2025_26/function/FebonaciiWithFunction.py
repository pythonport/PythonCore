'''
Created on Apr 16, 2025

@author: admin
'''


def printFebo(terms):
    x = 0
    y = 1
    print(x, y, end=' ')
    for i in range(terms):
        z = x + y
        print(z, end=' ')
        x, y = y, z
    print()

printFebo(8)
printFebo(18)
printFebo(28)
printFebo(38)