'''
Created on Sep 9, 2024

@author: admin
'''
import sys
fout = open('poem.txt')
line1 = fout.readline()
line2 = fout.readline()
#print(line1)
#print(line2)
sys.stdout.write(line1)
sys.stdout.write(line2)
fout.close()