'''
Created on Jul 5, 2019

@author: admin
'''
a = 10
def f():
    global a
    a = 4
    print(a)

f()
print(a)
