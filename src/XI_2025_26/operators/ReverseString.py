'''
Created on Nov 8, 2025

@author: admin
'''
 
#program to get index and character of a string
st = 'python'
for i in range(len(st)) :
    print(i, '-', st[i])
    
print('---------')    
print(st)
for i in range(-1, -(len(st)+1), -1) :
    print(st[i], end='')