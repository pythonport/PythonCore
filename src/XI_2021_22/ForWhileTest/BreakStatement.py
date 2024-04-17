'''
Created on Apr 8, 2022

@author: admin
'''
for a in range(20) :
    if (a == 14):
        break
    print(a, end=' ')

print('\n==============')
for a in range(20) :
    if (a in [7,10,14,18]):
        continue
    print(a, end=' ')