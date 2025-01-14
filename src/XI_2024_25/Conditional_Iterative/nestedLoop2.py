'''
Created on Jan 8, 2025

@author: admin
'''
for i in range(1, 27):
    num = 65
    for j in range(1, i + 1):
        print(chr(num), end=' ')
        num += 1
    print()

print('------------')
num = 65
for i in range(1, 27):
    for j in range(1, i + 1):
        print(chr(num), end=' ')
    num += 1
    print()