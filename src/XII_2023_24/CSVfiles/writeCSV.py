'''
Created on Sep 9, 2023

@author: Admin
'''
import csv

file = open('contacts.csv','w', newline='')

mobileheader = ['Name','Mobile No']
mobilelist=[]

m1 = ['vijay',7788445511]
m2 = ['ajay',7788446655]
m3 = ['digvijay',7788441122]
mobilelist.append(m1)
mobilelist.append(m2)
mobilelist.append(m3)

mwriter= csv.writer(file)

mwriter.writerow(mobileheader)  #write single row
mwriter.writerows(mobilelist) #write multiple row

print('ok done')