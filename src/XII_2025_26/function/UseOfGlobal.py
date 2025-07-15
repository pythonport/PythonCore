'''
Created on Jul 10, 2025
Use of global keyword to use only global variable in place of local variable
@author: admin
'''

def changeValue():
    global r 
    r = 50
    print('value of r in function- ', r)


r = 100
print('Value before function Call - ', r)
changeValue()
print('Value after function Call - ',r)