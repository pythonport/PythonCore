'''
Created on Sep 13, 2023

@author: Admin
'''
import csv
fout = open('contacts.csv','r')
creader = csv.reader(fout)

for row in creader :
    print(row)