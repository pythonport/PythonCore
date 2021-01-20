'''
Created on Jul 24, 2019

@author: admin
'''
obj1 = open('poemBTH.txt', 'r')
s1 = obj1.readline()
s2 = obj1.readline(10)
s3 = obj1.read(15)
print(s3)
print(obj1.readline())
obj1.close()