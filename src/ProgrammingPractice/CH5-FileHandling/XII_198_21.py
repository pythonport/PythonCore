'''
Created on Jul 23, 2019

@author: admin
Write a program that copies a text file 'source.txt' onto
'target.txt' barring the line starting wht a '@'
'''


def filterLine(oldfile, newfile):
    fin = open(oldfile, 'r')
    fout = open(newfile, 'w')
    while True :
        txt = fin.readline()
        if len(txt) == 0:
            break
        if txt[0] == '@':            
            continue  
        fout.write(txt)      
    fin.close()
    fout.close()


oldfile = 'source.txt'
newfile = 'target.txt'
filterLine(oldfile, newfile)

with open(newfile, 'r') as fin :
    str1 = fin.read()
    print(str1)
    
