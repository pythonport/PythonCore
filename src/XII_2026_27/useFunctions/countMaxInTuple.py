'''
Created on Apr 7, 2026

@author: admin
'''
tpl = eval(input('Enter tuple - '))
max = max(tpl)
if tpl.count(max) >1 :
    print(f'{max} came {tpl.count(max)} times')
    print('Yes, multiple max element')
else :
    print('No')