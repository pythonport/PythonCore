'''
Created on Aug 23, 2023

@author: Admin
'''
import pickle
fh = open('employeedata.dat', 'ab')
emp ={}
ans='y'
while ans=='y':
    eid = int(input('Employee id - '))
    ename = input('Employee name - ')
    salary = float(input('Employee salary - '))
    emp['eid']=eid;
    emp['ename']=ename;
    emp['salary']=salary;
    pickle.dump(emp, fh)
    ans = input('Do you want to store more record [y/n] - ')

print('writing done')
fh.close()