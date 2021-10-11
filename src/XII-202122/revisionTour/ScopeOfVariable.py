'''
Created on Oct 6, 2021
Scope of variable global and local
@author: admin
'''

x = 10


def valueOfLocal():
    y = 20
    print('Local variable y value is - ', y)
    print('Global variable x value is - ', x)


#print('Local variable y value is - ', y)    
print('Global variable x value is - ', x)
print("------Value after function call -----")
valueOfLocal()
