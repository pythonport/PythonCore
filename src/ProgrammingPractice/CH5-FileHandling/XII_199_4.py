'''
Created on Jul 24, 2019

@author: admin
'''
fin = open('poemBTH.txt', 'r+')
print('A : output 1')
print(fin.read())
print()

print('b : output 2')
print(fin.readline())
print()

print('c : output 3')
print(fin.read(9))
print()

print('d : output 4')
print(fin.readline(9))
print()

print('e : output 5')
print(fin.readlines())
print()
