'''
Created on Aug 4, 2026
Program for byte count before and after removing new line character.
@author: admin
'''
f1 = open('student.txt','r')
str = ' '
totalSize = 0
size = 0
while str : 
    str = f1.readline()
    #print(f"{len(str)} -> {len(str.strip())}")
    totalSize = totalSize+len(str)
    size = size+len(str.strip())

print('Total byte size - ',totalSize)
print('Size after removing \n - ',size)