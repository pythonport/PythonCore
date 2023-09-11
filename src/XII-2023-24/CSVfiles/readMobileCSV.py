'''
Created on Sep 9, 2023

@author: Admin
'''
import csv
file = open('mobiles.csv','r', newline='')
rec = csv.reader(file)
for a in rec :
    print(a)