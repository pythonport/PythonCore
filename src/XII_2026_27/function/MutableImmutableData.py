'''
Created on Jul 18, 2026
Code to demonstrate the use of mutable(list) data in function call statement.
@author: admin
'''
lstg = [2,4,6]

def listManupulation(lstl):
    print('lstl - ',lstl)
    lstl[0]=222
    print('lstl - ',lstl)
    
print('lstG - ',lstg)
listManupulation(lstg)
print('lstG - ',lstg)