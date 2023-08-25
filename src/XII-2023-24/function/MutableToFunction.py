'''
Created on Jul 13, 2023
Passing an Mutable type value to a function.
@author: ACER
'''


def myFunc2(mylist):
    print('\t Inside myFunc2()')
    print("\t list received is", mylist)
    mylist[0] += 2
    print("\t List within function after change - ", mylist)
    

# __main__
list = [1]
print("List before passing function ", list) 
myFunc2(list)
print("List after function call ", list)   
