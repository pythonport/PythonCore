'''
Created on Jul 26, 2025

@author: admin
'''
fout = open('jangalbook.txt', 'r')
str = ' '
while str :
    str = fout.readline()
    print(str)
fout.close()