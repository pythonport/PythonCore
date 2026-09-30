'''
Created on Aug 6, 2026
Progtam to show the number of byte and number of lines in a file.
@author: admin
'''
fout = open('student.txt','r')
str  = fout.read()
print(f'Length of file is - {len(str)} bytes')

fout.seek(0) #take cursor to begining of file
lines = fout.readlines()
print(f'No of lines in file is - {len(lines)}')