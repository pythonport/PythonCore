'''
Created on Feb 2, 2021

@author: admin
'''
for i in range(6):
    for j in range(0, i):
        print('#', end='')
    print()

print('--------------')

strval = '#'
for i in range(5):
    print(strval)
    strval +='#'
    