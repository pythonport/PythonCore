'''
Created on Aug 29, 2024

@author: admin
'''
fout = open('poem.txt','r')
str = ' '
totalsize = 0
stripsize = 0
while str :
    str = fout.readline()
    totalsize += len(str)
    stripsize += len(str.strip())

print('Total size of file - ',totalsize)
print('Size after striping file - ',stripsize)
fout.close()