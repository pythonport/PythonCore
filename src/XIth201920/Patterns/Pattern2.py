'''
Created on Dec 3, 2019

@author: admin
'''
for i in range(6):
    for j in range(i):
        if(j == 0 or j == i - 1) :
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()
for i in range(6, 0, -1):
    for j in range(i):
        if(j == 0 or j == i - 1) :
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()
    