'''
Created on Sep 9, 2023

@author: Admin
'''
import csv

file = open('mobiles.csv','a', newline='')

mobilelist = ['vijay',7788445511]
mwriter= csv.writer(file)
mwriter.writerow(mobilelist)
print('ok done')