'''
Created on Jul 10, 2026

@author: admin
'''
# Void function example
def hello() :
    return "hello to you"

result = hello()
print(result)

def sum(a, b):
    s = a+b
    return s

result = sum(10,15)
print(result)

def helloVoid():
    print("hello to  you from void function")
    
helloVoid()

def helloVoid1(name):
    print(f"hello to {name} from void function ")
    
helloVoid1('python')
