'''
Created on Aug 29, 2023

@author: Admin
'''
import pickle
fh = open('employeedata.dat', 'rb+') 
flag = False
emp = {}
try:
    while True:
        pos = fh.tell()
        print('file pointer - ', pos)
        emp = pickle.load(fh)
        print(emp)
        if emp['ename'] == 'anju':
            emp['ename'] = 'MANJU'
            fh.seek(pos)
            pickle.dump(emp, fh)
            flag = True
except EOFError:
    if flag == False:
        print('No such record found')
    else:
        print('Successful search')
    fh.close()
