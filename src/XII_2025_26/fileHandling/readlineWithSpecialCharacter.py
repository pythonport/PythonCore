'''
Created on Aug 1, 2025
write a program to tead text file line by line and display each word separated by a '#' sign
@author: admin
'''
fout = open('jangalbook.txt', 'r')
str = ' '
while str :
    str = fout.readline()
    for word in str.split() :
        print(word, end='$')
    print()
fout.close()