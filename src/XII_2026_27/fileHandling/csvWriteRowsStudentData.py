'''
Created on Sep 11, 2026

@author: admin
'''
import csv
fout = open('studentMarks1.csv','a',newline='')
jnvwriter = csv.writer(fout)
students = []
for i in range(3):
    roll = int(input('Roll - '))
    name = input('Name - ')
    marks = float(input('Marks - '))
    studata = [roll, name, marks]
    students.append(studata)

jnvwriter.writerows(students)
fout.close()
print('done')