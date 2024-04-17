'''
Created on Jan 27, 2022
Test mutablity of list
@author: admin
'''
str = 'python'
print(str)

lst = list(str)
print(lst)
lst[1] = 'YY'
print(lst)