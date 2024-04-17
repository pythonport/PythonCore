'''
Created on Aug 16, 2023

@author: Admin
'''

import pickle

fh = open('studentList.dat','rb')
try :
 stulist = pickle.load(fh)
except e :
    print(e)
print("Printing the student list")
print(stulist)
fh.close()

'''
stulist = ''
with open('studentList.dat','rb') as fh :
    stulist = pickle.load(fh)

print(stulist)
'''