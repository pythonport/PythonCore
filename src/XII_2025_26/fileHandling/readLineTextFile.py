'''
Created on Jul 25, 2025
Program to print data using readline() function
@author: admin
'''
fout = open('jangalbook.txt', 'r')
line1= fout.readline()
print(line1)
print(fout.readline(7))