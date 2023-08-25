'''
Created on Aug 7, 2023

@author: Admin
'''
fh = open('poem.txt', 'r')
str = ' '
scount = 0
tcount = 0
while str:
    str = fh.readline()
    tcount += len(str)
    scount += len(str.strip())
    
print("Total character count - ",tcount)
print('Stripped count - ',scount)