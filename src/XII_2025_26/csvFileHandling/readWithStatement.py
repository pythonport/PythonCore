'''
Created on Aug 29, 2025

@author: admin
'''
import csv
with open('studentMarks.csv','r') as fh :
    myreader = csv.reader(fh)
    for row in myreader :
        print(row)
print('closed')