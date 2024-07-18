'''
Created on Jul 8, 2024

@author: admin
'''

#void function
def greet(nm):
    print('Hello to - ',nm)
    
greet('ravi')
greet('suman')

#non void function

def greetone(nm):
    st = 'Hello from greetone - ',nm
    return st

a = greetone('ravi')
print(a)
print(greetone('suman'))