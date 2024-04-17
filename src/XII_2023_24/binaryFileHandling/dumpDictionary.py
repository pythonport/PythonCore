'''
Created on Aug 17, 2023

@author: Admin
'''
import pickle
fh = open('employeedata.dat', 'wb')
emp1 = {'eid':'01', 'ename':'anish', 'salary':65000}
emp2 = {'eid':'02', 'ename':'manish', 'salary':75000}
emp3 = {'eid':'03', 'ename':'harish', 'salary':56228}
emp4 = {'eid':'04', 'ename':'anju', 'salary':89555}

pickle.dump(emp1, fh)
pickle.dump(emp2, fh)
pickle.dump(emp3, fh)
pickle.dump(emp4, fh)

print('done')

