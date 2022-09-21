'''
Created on Sep 12, 2022

@author: admin
'''
fout = open('jnvaddress.txt','r')
str = fout.read(20)
print(str)
print('-----------')
str = fout.read(10)
print(str)
fout.close()