'''
Created on Nov 28, 2019
All Star patterns
@author: admin
'''
for i in range(6):
    for j in range(i):
        print('*', end=' ')
    print()
    
print('================')

for i in range(6, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
    
print('===================')

for i in range(6):
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(6, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
    
print('===================')

for i in range(6):
    for j in range(i):
        if(j == 0 or j == i - 1) :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(6, 0, -1):
    for j in range(i):
        if(j == 0 or j == i - 1) :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
