'''
Created on Aug 17, 2023

@author: Admin
'''
import pickle

fh = open('employeedata.dat', 'rb') 
try :
    while True : 
        empdata = pickle.load(fh)
        print(empdata)
except EOFError :
    fh.close()
    #print('error...')
    
    
'''
print('Employee id - ',empdata['eid'])
        print('Employee Name - ',empdata['ename'])
        print('Employee Salary - ',empdata['salary'])
        print('---------------------------')
'''