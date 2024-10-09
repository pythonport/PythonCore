'''
Created on Oct 9, 2024
Read csv file using csv reader()
@author: admin
'''
import csv
fh= open('employees.csv','r')
empreader  = csv.reader(fh)

for emp in empreader :
    print(emp)
