'''
Created on Jul 10, 2023

@author: ACER
'''
a = 10
def calccube(x):
    cval = x**3
    print('x in local -',x)
    print('A in local -',a)
    print('cval is - ',cval)
    
print('A in global -',a)
calccube(10)
#print('x in local -',x)
print('cval is - ',cval)