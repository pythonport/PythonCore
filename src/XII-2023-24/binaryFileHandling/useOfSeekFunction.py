'''
Created on Aug 26, 2023

@author: Admin
'''
fh = open('poem.txt', 'rb')
fh.seek(50,0)
st = fh.read()
print(st)