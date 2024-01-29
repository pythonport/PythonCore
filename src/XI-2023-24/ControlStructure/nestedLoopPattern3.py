'''
Created on Dec 22, 2023

@author: Admin
'''
for i in range(0,8) :
    ch = 65
    for j in range(0, i) :
        print(chr(ch), end=' ') 
        ch+=1
    print()
    
print('--------')
ch = 65
for i in range(0,8) :
    for j in range(0, i) :
        print(chr(ch), end=' ') 
        ch+=1
    print()
    
print('--------')
ch = 65
for i in range(1,8) :
    for j in range(0, i) :
        print(chr(ch), end=' ') 
    ch+=1
    print()