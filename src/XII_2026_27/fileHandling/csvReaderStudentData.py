'''
Created on Sep 12, 2026

@author: admin
'''
import csv
fout = open('studentMarks1.csv','r')
jnvreader = csv.reader(fout)
for row in jnvreader:
    print(row)
fout.close()
print('done')