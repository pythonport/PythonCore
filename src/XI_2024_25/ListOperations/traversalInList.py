'''
Created on Jan 25, 2025
Traveral through List
@author: admin
'''
lst = ['ravi', 'kiran', 'aman', 'vinay', 'dayal', 'naman']
for i in lst:
    print(i)

print('---')    
for i in range(len(lst)):
    print(i, '->', lst[i])

print('----')
ind = 0
while ind < len(lst):
    print(lst[ind], end=' ')
    ind += 1
