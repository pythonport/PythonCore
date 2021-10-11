'''
Created on Sep 22, 2021

@author: admin
'''
import sys

fout = open('poem.txt')
line1 = fout.readline()
line2 = fout.readline()

# Standard input from keyboard for 20 characters
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write('No error message')

# Standard input from keyboard for 20 characters
line = sys.stdin.read(20)
sys.stdout.write(line)
