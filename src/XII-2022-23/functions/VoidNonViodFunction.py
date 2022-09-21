'''
Created on Jul 26, 2022

@author: admin
'''


def calcSumVoid(x, y):
    print(x + y)

    
def calcSumNonVoid(x, y):
    s = x + y
    return s
    
calcSumVoid(20, 40)
sum = calcSumNonVoid(40, 140)
print("sum value is - ", sum)

print(calcSumNonVoid(40, 10))