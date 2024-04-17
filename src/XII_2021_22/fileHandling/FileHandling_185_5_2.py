'''
Created on Sep 17, 2021

@author: admin
'''
fout = open('poem.txt','r')
lines = fout.readlines()
noOfLines = len(lines)
print("Total no of Lines are - ",noOfLines)