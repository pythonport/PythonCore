'''
Created on Aug 4, 2025

@author: admin
'''
file = open('stumarks.txt','r')
print('File pointer location - ',file.tell())
s = file.read(3)
print(s)
print('File pointer location - ',file.tell())
s = file.read(5)
print(s)
print('File pointer location - ',file.tell())