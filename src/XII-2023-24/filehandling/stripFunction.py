'''
Created on Aug 7, 2023

@author: Admin
'''
fh = open('exam.txt', 'r')
line = fh.readline()
print(line)
print('Length of line - ', len(line))
print('Length of line - ', len(line.strip()))
