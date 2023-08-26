'''
Created on Aug 26, 2023

@author: Admin
'''
fh = open('poem.txt', 'r')
print('cursor position -', fh.tell())
st = fh.read(10)
print(st)
print('cursor position -', fh.tell())
st = fh.read(7)
print(st)
print('cursor position -', fh.tell())
