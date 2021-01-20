'''
Created on Jul 22, 2019

@author: admin
'''
fout=open(r'C:\Users\admin\Documents\PyDevPrograms\PythonCore\src\XIIsPython\FileHandling\students.txt')
str  = fout.read()
print(str)


with open('students.txt') as fout :
    str  = fout.read()
    print(str)