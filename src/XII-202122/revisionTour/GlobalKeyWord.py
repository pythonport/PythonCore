'''
Created on Oct 6, 2021

@author: admin
'''
x = 10

def useOfGlobal():
    global x
    x = 20
    print("Value of x first time - ", x)
    x = x + 5
    print("Value of x second time - ", x)
    

print("Value of x outside 1 - ", x)
useOfGlobal()
print("Value of x outside 2 - ", x)
