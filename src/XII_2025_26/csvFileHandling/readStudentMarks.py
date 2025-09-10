'''
Created on Aug 29, 2025

@author: admin
'''
import csv
fh = open('studentMarks.csv','r', newline='')
myreader = csv.reader(fh)
for row in myreader :
    print(row)

fh.close()