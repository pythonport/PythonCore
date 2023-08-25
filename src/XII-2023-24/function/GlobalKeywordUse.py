'''
Created on Aug 9, 2023

@author: Admin
'''
a = 10


def abc():
    global a
    a = 20
    print('A from 9 - ', a)
    a += 5
    print('A from 11 - ', a)


abc()
print('A from 14 - ', a)
