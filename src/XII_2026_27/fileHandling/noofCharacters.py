'''
Created on Aug 6, 2026

@author: admin
'''
file1 = open('contacts.dat','r')
str = ' '
count = 1
while str :
    str = file1.readline()
    print('Characters - ',len(str))