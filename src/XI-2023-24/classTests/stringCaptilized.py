'''
Created on Feb 29, 2024

@author: Admin
'''
str = 'this is my first python string and list program'
lst = str.split()
strnew = ''
for i in range(len(lst)) :
    strnew += lst[i].capitalize()+' '
print(str)
print(strnew)
