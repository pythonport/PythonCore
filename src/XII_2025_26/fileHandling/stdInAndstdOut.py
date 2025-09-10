'''
Created on Aug 5, 2025

@author: admin
'''
import sys
fh = open('friendlist.txt','r')
l1  = fh.readline()
l2 = fh.readline()
sys.stdout.write(l1)
sys.stdout.write(l2)
print('Sys module stdout uses')