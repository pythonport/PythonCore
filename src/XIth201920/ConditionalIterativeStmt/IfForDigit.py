'''
Created on Sep 14, 2019

@author: admin
'''
val = input("Enter any character - ")
if '0'<=val<='9':       #val>='0' and val<='9'
    print(val, ' is a digit')
else:
    print(val, ' is not a digit')