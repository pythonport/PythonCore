'''
Created on Sep 11, 2024

@author: admin
'''
import pickle

emp1 = {'empid':123, 'ename':'ramesh', 'post':'manager', 'salary':85000}
emp2 = {'empid':111, 'ename':'manish', 'post':'admin', 'salary':75000}
emp3 = {'empid':112, 'ename':'suresh', 'post':'programmer', 'salary':55000}
emp4 = {'empid':133, 'ename':'vinit', 'post':'programmer', 'salary':95000}
emp5 = {'empid':132, 'ename':'nayan', 'post':'analyst', 'salary':105000}

empdump = open('Employee.dat', 'wb')
pickle.dump(emp1, empdump)
pickle.dump(emp2, empdump)
pickle.dump(emp3, empdump)
pickle.dump(emp4, empdump)
pickle.dump(emp5, empdump)
print('Data Written successfully')
empdump.close()

'''
with open('Employee.dat', 'rb') as empload :
    while True :
        emprecord = pickle.load(empload)
        print(emprecord)
'''    

empload = open('Employee.dat', 'rb')
try :
    while True :
        emprecord = pickle.load(empload)
        print(emprecord)
except :
    print('done')