'''
Created on Apr 8, 2026

@author: admin
'''
tpl = (22, 65, 22, 54, 34, 12)
for i in tpl:
    if tpl.count(i)>1:
        print(f'{i} is duplicate in {tpl}')
        break
