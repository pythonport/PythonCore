'''
Created on Aug 20, 2026

@author: admin
'''
fout = open('poem.txt','r')
str = ' '
while str :
    str = fout.readline()
    print(str)
    print(len(str.rstrip())," ",len(str.lstrip())," ",len(str.strip()))