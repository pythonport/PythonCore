'''
Created on Aug 3, 2026
program to read the file line by line first 3 lines
@author: admin
'''

f1 = open('student.txt','r')
str = f1.readline()
print(str,end='')
str = f1.readline()
print(str,end='')
str = f1.readline()
print(str,end='')
f1.close()