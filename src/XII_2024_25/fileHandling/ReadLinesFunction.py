'''
Created on Aug 29, 2024

@author: admin
'''
fout = open('poem.txt','r')
s  = fout.readlines()

for i in s :
    print(i, end='')