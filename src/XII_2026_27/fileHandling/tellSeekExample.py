'''
Created on Sep 7, 2026

@author: admin
'''
fin = open('testData.txt','r')
print(fin.tell())
print(fin.read(20))
print(fin.tell())
fin.seek(0)
print(fin.read(30))
#fin.seek(-50,0)
print(fin.read(30))
fin.seek(2)
fin.seek(50,2)

