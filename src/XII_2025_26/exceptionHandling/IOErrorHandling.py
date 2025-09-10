'''
Created on Sep 2, 2025

@author: admin
'''
try :
    fh = open('studentlist.txt','r')
    print(fh.read())
except IOError :
    print('no such file exist')