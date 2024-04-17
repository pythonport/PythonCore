'''
Created on Feb 18, 2022

@author: admin
'''
tpl = (3, 4, 5, 2, 3)
print('New tuple is - ', tpl)
lst = list(tpl)
lst[1] = 44
tpl = tuple(lst)
print('updated tuple is - ', tpl)
