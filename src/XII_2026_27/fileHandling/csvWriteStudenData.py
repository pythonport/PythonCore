'''
Created on Sep 11, 2026

@author: admin
'''
import csv
fout = open('studentMarks1.csv','w',newline='')
jnvwriter = csv.writer(fout)
header = ['roll','name','marks']
jnvwriter.writerow(header)
for i in range(5):
    roll = int(input('Roll - '))
    name = input('Name - ')
    marks = float(input('Marks - '))
    studata = [roll, name, marks]
    jnvwriter.writerow(studata)
fout.close()
print('done')