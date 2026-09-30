'''
Created on Jul 16, 2026
Code to demonstrate the use of same name variable in global and local scope.
@author: admin
'''
tigers  = 95

def gujratTigers():
    global tigers 
    tigers = 150
    print('count of Tigers -',tigers)


print('count of Tigers -',tigers)
gujratTigers()
print('count of Tigers -',tigers)
gujratTigers()
