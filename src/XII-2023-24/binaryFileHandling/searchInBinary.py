'''
Created on Aug 24, 2023

@author: Admin
'''
import pickle
fh = open('employeedata.dat', 'rb') 
flag = False
emp = {}
try:
    empid = int(input('Employee id to search - '))
    while True:
        emp = pickle.load(fh)
        if emp['eid'] == empid:
            print(emp)
            flag = True
except EOFError:
    if flag == False:
        print('No such record found')
    else:
        print('Successful search')
    fh.close()
