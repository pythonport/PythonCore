'''
Created on Aug 7, 2026

@author: admin
'''
fout  = open('datawithhash.txt','r')
str = fout.read()
lststr = str.split()
for s in lststr :
    print(s+'#',end='')