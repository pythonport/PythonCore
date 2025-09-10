'''
Created on Aug 6, 2025
Code to demonstrate the use of absolute path and relative path in file handling
@author: admin
'''
fh = open(r'D:\PythonEclipsePrograms\PythonCore\src\XII_2025_26\jnvdhanbad.txt') #absolute path
fh = open(r'..\jnvdhanbad.txt') #relative path of parent folder 
fh = open(r'..\moduleLibraries\jnvdhanbad.txt') #relative path of subfolder of parent folder
str = fh.read()
print(str)