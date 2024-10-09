'''
Created on Aug 26, 2024

@author: admin
'''
fout = open('poem.txt','r')
str = ' '
while str :
    str = fout.readline()
    print(str, end='')
fout.close()