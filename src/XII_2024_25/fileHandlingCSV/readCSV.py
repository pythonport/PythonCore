'''
Created on Oct 5, 2024

@author: admin
'''
import csv
file = open('sturesult.csv','r')
data = csv.reader(file)

for row in data :
    print(row)
