'''
Created on Sep 8, 2023

@author: Admin
'''
import csv
file = open('funds.csv','r')
data = csv.reader(file)

for row in data :
    print(row)
