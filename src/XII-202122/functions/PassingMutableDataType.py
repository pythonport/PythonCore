'''
Created on Aug 19, 2021
function passing and receiving mutable data type
@author: admin
'''


def myfunction1(mylist):
    print("inside the function value received is  - ", mylist)
    mylist[0] += 2
    print("Value now changed to   - ", mylist)
    print("Returning from the function")

    
# __main__
lst1 = [1]
print("calling myfunction1(a) by passing 'num' with value - ", lst1)
myfunction1(lst1)
print("After returning to main function - ", lst1)
