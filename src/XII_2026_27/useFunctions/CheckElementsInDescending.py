'''
Created on Apr 8, 2026

@author: admin
'''
tpl = (12,9,8,7,3)
a = sorted(tpl, reverse=True)
print(tpl)
print(a)

if a==list(tpl) :
    print('In Descending order')
else :
    print('Not In Descending order')
    