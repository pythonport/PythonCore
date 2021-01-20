'''
Created on Jan 21, 2020

@author: admin
'''
import sys
fh = open('students.txt')

'''
code to write on monitor using stdout
'''
for i in fh.readlines():
    sys.stdout.write(i)

print("Enter line to read line from keyboard - ")    
line = sys.stdin.read(23)
sys.stdout.write(line)