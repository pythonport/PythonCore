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
st = fh.read()
print('last position -', fh.tell())
st = fh.read(25,2)
post= fh.seek(-20,2)
st = fh.read(50,pos)
print('data-',st)
