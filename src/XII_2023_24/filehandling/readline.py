'''
Created on Jul 24, 2023

@author: ACER
'''
fout = open('12science.txt', 'r')

print(fout.readline())
print(fout.readline(3))
print(fout.readline())
fout.close()