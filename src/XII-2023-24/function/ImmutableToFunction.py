'''
Created on Jul 13, 2023
Passing an Immutable type value to a function.
@author: ACER
'''


def myFunc1(a):
    print('\t Inside myFunc1()')
    print("\t Value received in 'a' as", a)
    a = a + 2
    print("\t Value of 'a' changed to - ", a)
    print("\t returning from the function")
    

# __main__
num = 3
print("Calling myFunc1() by passing 'num' with value ", num) 
myFunc1(num)
print("back from myFunc1(). Value of 'num' is ", num)   
