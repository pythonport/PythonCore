'''
Created on Apr 10, 2024

@author: admin
'''

def hellojnv(name):
    gval = "hello {} from jnv dhanbad".format(name)
    print('line 9 - ',gval)
    return gval
    
 
name= input("Enter name - ")    
a = hellojnv(name)
print('line 15 - ',a)