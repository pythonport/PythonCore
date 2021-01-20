'''
Created on Oct 1, 2020
Stander input and output stream
@author: admin
'''
import sys

fout = open('poemBachhan.txt','r')
line1 = fout.readline()
line2 = fout.readline()
line3 = fout.readline()
line4 = fout.readline()
line5 = fout.readline()
'''sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stdout.write(line3)
sys.stdout.write(line4)
sys.stdout.write(line5)'''
print(line1,end='')
print(line2,end='')
print(line3,end='')
print(line4,end='')
print(line5,end='')
fout.close()