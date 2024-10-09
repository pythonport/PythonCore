'''
Created on Sep 9, 2024

@author: admin
'''
import sys
fout=open('namesfromkeyboard.txt','w')
print('Write here - ')
line = sys.stdin.read()
fout.write(line)
print('done')