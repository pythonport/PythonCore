'''
Created on Aug 30, 2024

@author: admin
'''
fout = open('poem.txt','r')

lstlines = fout.readlines()
linecount = len(lstlines)
'''
linecount = 0
str = ' '
while str :
    str = fout.readline()
    linecount += 1
'''
print("Number of lines are - ",linecount)