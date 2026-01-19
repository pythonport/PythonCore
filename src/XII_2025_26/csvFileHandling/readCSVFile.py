'''
Created on Aug 27, 2025
Code to demonstrate the use of reading csv file
@author: admin
'''
import csv
fh = open('studentFee.csv','r')
jnvreader = csv.reader(fh)
#next(jnvreader)
for data in jnvreader :
    print(data)