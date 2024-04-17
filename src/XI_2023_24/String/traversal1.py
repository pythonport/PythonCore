'''
Created on Dec 30, 2023

@author: Admin
'''
str = input('Enter a string - ')
lstr = len(str)
for i in range(lstr):
    print(str[i], end=' ')   
print('\n----------') 
for i in range(-1, (-lstr - 1), -1):
    print(str[i], end=' ')
