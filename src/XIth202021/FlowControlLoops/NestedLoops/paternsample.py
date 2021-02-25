'''
Created on Jan 25, 2021

@author: admin
'''
A = 65
for i in range(1, 6):
    for j in range(0, i):
        print(chr(A), end=' ')
    print()
    A+=1
    
print("--------------")
for i in range(1, 6):
    A = 65
    for j in range(0, i):
        print(chr(A), end=' ')
        A+=1
    print()