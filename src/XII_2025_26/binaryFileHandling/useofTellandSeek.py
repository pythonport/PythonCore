'''
Created on Aug 21, 2025

@author: admin
'''
fh = open('example.txt','r')
rpos = fh.tell()
print(rpos)
print(fh.read(5))
rpos = fh.tell()
print(rpos)
print(fh.read(7))
fh.seek(2)
print(fh.read())