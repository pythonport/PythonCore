'''
Created on Oct 8, 2024

@author: admin
'''
import csv
efile  = open('employees.csv','a', newline='')
ewriter = csv.writer(efile)

flag = 'y'
while flag == 'y' :
    eid=input('Employee id - ')
    ename=input('Employee name - ')
    salary=input('Employee salary - ')
    employee = [eid, ename, salary]
    ewriter.writerow(employee)
    flag = input('Do you want to continue [y/n] - ')
    
print('success')
efile.close()