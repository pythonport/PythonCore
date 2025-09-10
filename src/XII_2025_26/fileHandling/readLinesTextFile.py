'''
Created on Jul 25, 2025
program to read text data using readlines() medhod, it will return list of lines
@author: admin
'''
fout = open('jangalbook.txt', 'r')
lines= fout.readlines()
print(lines)
print('no of lines - ',len(lines))
