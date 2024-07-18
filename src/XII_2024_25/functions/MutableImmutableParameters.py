'''
Created on Jul 13, 2024

@author: admin
'''

#immutable parameter passed to function
def function1(x):
    print('inside function1 ')
    print('received value ',x)
    x+=2
    print('changed value ',x)
    print('returning from function')

a = 3
print('a before calling function - ',a)
function1(a)
print('a after calling function - ',a)

#mutable parameter passed to function
def function2(x):
    print('inside function1 ')
    print('received value ',x)
    x.append(33)
    print('changed value ',x)
    print('id of x ',id(x))
    print('returning from function')

a = [3]
print('a before calling function - ',a)
function2(a)
print('a after calling function - ',a)
print('id of a ',id(a))

#mutable parameter passed and created new list out of existing list
def function3(x):
    print('inside function1 ')
    x = list(a)
    print('received value ',x)
    x.append(33)
    print('changed value ',x)
    print('id of x ',id(x))
    print('returning from function')

a = [3]
print('a before calling function - ',a)
function3(a)
print('a after calling function - ',a)
print('id of a ',id(a))