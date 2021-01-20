'''
Created on Jul 22, 2019

@author: admin
'''
import sys

fh = open('xyz.txt', 'w+')
str1= "Python program using stdin"
str2= 'Internally keyboard is treated as stdin file'
str3 = sys.stdin.read(50)
sys.stdout.write(str3)