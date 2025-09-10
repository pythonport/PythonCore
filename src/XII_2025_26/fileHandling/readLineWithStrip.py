'''
Created on Jul 28, 2025

@author: admin
'''
fout = open('jangalbook.txt', 'r')
line = fout.readline()
print(line)
print('Length before strip - ',len(line))
sline = line.strip()
print('Length before strip - ',len(sline))