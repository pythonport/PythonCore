'''
Created on Aug 13, 2026
program for line count
@author: admin
'''
fh = open('mydata.txt','r')
lines = fh.readlines()
print('Number of lines are - ',len(lines))