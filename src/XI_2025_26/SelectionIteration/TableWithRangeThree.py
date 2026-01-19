'''
Created on Dec 29, 2025
Print table using range function three parameter itself.
@author: admin
'''
n = int(input('Table of - '))
print('----')    
for i in range(n, n * 10 + 1, n):
    print(i)
