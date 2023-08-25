'''
Created on Aug 12, 2023

@author: Admin
'''
import sys
fh = open('poemToRead.txt')
'''
print(line1)
print(line2)
'''
while True : 
    line  = fh.readline()
    if(line =='') :
        break
    sys.stdout.write(line)
