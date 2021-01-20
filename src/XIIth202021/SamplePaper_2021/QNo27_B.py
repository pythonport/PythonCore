'''
Created on Jan 2, 2021

@author: admin
'''
a = 5

def useGlobal():   
    global a 
    a = 10
    print(a)

print(a)    
useGlobal()
print(a)   