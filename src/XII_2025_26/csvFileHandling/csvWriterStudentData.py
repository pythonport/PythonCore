'''
Created on Aug 27, 2025
program to write data to csv file
@author: admin
'''
import csv
fh = open('studentFee.csv','w',newline='')
jnvwriter = csv.writer(fh)
header = ['roll','name','marks']
jnvwriter.writerow(header)

for i in range(3):
    roll  = int(input('Roll no - '))
    name  = input('Name - ')
    marks  = float(input('Marks - '))
    student = [roll,name,marks]
    jnvwriter.writerow(student)

print('done')
fh.close()
