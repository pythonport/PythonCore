'''
Created on Oct 8, 2024

@author: admin
'''
import csv
efile  = open('employees.csv','a', newline='')
ewriter = csv.writer(efile)

employees= [['eid','ename','salary'],
            ['1','aman','80k'],
            ['2','naman','85k'],
            ['3','vivek','90k'],
            ['4','kundan','91k'],
            ]

ewriter.writerows(employees)
print('success')
efile.close()

#---------------------------
try:
    a = 10 / 5
    print("value is - ", a)
except:
    print('ZERO Division Error')
finally:
    print('I am in finally block')