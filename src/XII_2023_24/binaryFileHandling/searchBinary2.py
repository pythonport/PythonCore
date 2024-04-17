'''
Created on Aug 26, 2023

@author: Admin
'''
import pickle
fh = open('employeedata.dat', 'rb') 
flag = False
emp = {}
try:
    while True:
        emp = pickle.load(fh)
        if emp['salary'] > 70000:
            print(emp)
            flag = True
except EOFError:
    if flag == False:
        print('No such record found')
    else:
        print('Successful search')
    fh.close()
