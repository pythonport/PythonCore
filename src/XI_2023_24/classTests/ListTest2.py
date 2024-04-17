'''
Created on Mar 1, 2024

@author: Admin
Create list of alphabets like
['a','bb','ccc',....]
'''
lst = []
for i in range(1, 27):
    ch = 65
    str = ''
    for j in range(0, i) :
        str+=chr(ch)
        ch+=1
    lst.append(str)
        
print(lst)

print('===========')
lst = []
ch = 65
for i in range(1, 27):
    str = ''
    for j in range(0, i) :
        str+=chr(ch)
    ch+=1
    lst.append(str)
        
print(lst)