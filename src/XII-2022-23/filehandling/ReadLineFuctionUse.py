'''
Created on Sep 12, 2022

@author: admin
'''
fout = open('jnvaddress.txt','r')
str=' '
while str :
    str = fout.readline()
    print(str, end = '')
fout.close()