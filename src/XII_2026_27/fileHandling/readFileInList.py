'''
Created on Aug 4, 2026
Program to read complete file using readlines()
@author: admin
'''
f1 = open('student.txt','r')
lstLine = f1.readlines()
#print(lstLine)
for i in range(len(lstLine)) :
    print(lstLine[i])
f1.close()