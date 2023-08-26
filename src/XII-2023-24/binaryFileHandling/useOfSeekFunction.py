'''
Created on Aug 26, 2023

@author: Admin
'''
fh = open('poem.txt', 'r')
print('cursor position - ',fh.tell())
st = fh.read(10)
print(st)
print('cursor position - ',fh.tell())
fh.seek(20,1)
print('cursor position - ',fh.tell())
fh.seek(20,2)
print('cursor position - ',fh.tell())