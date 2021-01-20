'''
Created on Jan 9, 2021

@author: admin
'''
line = input("Enter line - ")
substr = input("Enter substring - ")

if substr in line :
    print(substr," is part of -",line)
else :
    print(substr," is not part of -",line)
    