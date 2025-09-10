'''
Created on Aug 29, 2025

@author: admin
'''
import csv
fh = open('studentMarks.csv','w', newline='')
mywriter = csv.writer(fh)
classMarks = [['roll','name','marks'],[1,'amit',45],[2,'aman',56],[3,'anita',78]]
mywriter.writerows(classMarks)
fh.close()
print('done')