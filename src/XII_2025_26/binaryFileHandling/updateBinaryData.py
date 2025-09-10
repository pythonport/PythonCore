'''
Created on Aug 22, 2025
Updating the record in binary file
@author: admin
'''
import pickle
fh = open('emp.dat','rb+')
flag = False
empid = int(input('Enter employee code - '))
salary = int(input('Expeced salary - '))
try :
    while True :
        rpos = fh.tell()
        emp = pickle.load(fh)
        if emp['ecode'] == empid :
            emp['salary'] = salary
            fh.seek(rpos)
            pickle.dump(emp, fh)
            flag = True
            
except EOFError :
    if flag == False :
        print('No record found')
    else :
        print('updation done')
    fh.close()