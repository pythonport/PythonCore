'''
Created on Aug 19, 2021
function passing and receiving immutable data type
@author: admin
'''


def myfunction1(a):
    print("inside the function value received is  - ", a)
    a = a + 2
    print("Value now changed to   - ", a)
    print("Returning from the function")

    
# __main__
num = 3
print("calling myfunction1(a) by passing 'num' with value - ", num)
myfunction1(num)
print("After returning to main function - ", num)
