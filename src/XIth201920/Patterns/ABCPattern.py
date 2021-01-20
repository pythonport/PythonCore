'''
Created on Nov 28, 2019

@author: admin
'''
num=65
for i in range(6):
    for j in range(i):
        print(chr(num+j), end=' ')
    print()
    
print('=================')
num=65
for i in range(6):
    for j in range(i):
        print(chr(num), end=' ')
        num+=1
    print()