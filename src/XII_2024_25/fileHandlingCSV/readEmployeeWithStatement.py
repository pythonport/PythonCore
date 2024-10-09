'''
Created on Oct 9, 2024

@author: admin
'''
import csv
try 
    with open('employee.csv','r') as fh :
        empreader  = csv.reader(fh)
        for emp in empreader :
            print(emp)

except IOError as e:
    print(e)
    print('no such employee file exists')