'''
Created on Jul 22, 2021

@author: admin
'''
# x = 5

'''
function definition.
'''
def calcSomething(x):
    fx = 2 * x ** 2
    # print('fx of ',x,' is - ',fx)
    return fx

#function call    
print(calcSomething(4))
print(calcSomething(5))
print(calcSomething(6))
print(calcSomething(234))

num = 9
rval = calcSomething(num)
print('Return value is - ',rval)
