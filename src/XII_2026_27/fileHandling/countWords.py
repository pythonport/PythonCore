'''
Created on Aug 13, 2026
Program for word count
@author: admin
'''
fh = open('mydata.txt','r')
wordcount =  0
str = ' '
while str :
    str = fh.readline()
    words = str.split()
    wordcount += len(words)

print('Total Words are - ',wordcount)