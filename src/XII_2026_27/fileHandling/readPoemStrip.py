'''
Created on Aug 20, 2026

@author: admin
'''
fout = open('poem.txt','r')
str = fout.readline()
print(str)
print(len(str))
rstrip = str.rstrip()
print(len(rstrip))
lstrip = str.lstrip()
print(len(lstrip))
strip = str.strip()
print(len(strip))