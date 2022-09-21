'''
Created on May 5, 2022
Calculate the fx value where x is given
@author: admin
'''

def calculator(x):
    res = 2*x**2+2*x
    print("f(x) value is - ",res)
    
def calculatorWithReturn(x):
    res = 2*x**2+2*x
    return res
    
#calculator(5)
#calculator(7)

r1 = calculatorWithReturn(4)
print("f(x) value is - ",r1)
r2 = calculatorWithReturn(6)
print("f(x) value is - ",r2)
print("f(x) value is - ",calculatorWithReturn(8))