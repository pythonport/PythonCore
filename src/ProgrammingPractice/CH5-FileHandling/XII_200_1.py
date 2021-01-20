'''
Created on Jul 24, 2019

@author: admin
Program that reads a text file and creates another file 
that is identical except that every sequence of consecutive 
blank space is replaced by a single space.
'''
fin = open('source.txt','r')
fout = open('OUTsource.txt','w')
str=' '
while str :
    str = fin.readline()
    str = str.replace(' ', '')
    fout.write(str)

fin.close()
fout.close()

with open('OUTsource.txt','r') as fin :
    print(fin.read())