'''
Created on Jan 14, 2025

@author: admin
'''
str = 'jnv dhanbad'
for i in str:
    print(i)

print('---')    
for i in range(len(str)):
    print(i,'->',str[i])

print('----')
ind=0
while ind<len(str):
    print(str[ind], end= '')
    ind+=1