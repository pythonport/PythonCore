'''
Created on Jan 9, 2026

@author: admin
'''
# Nested - one
for outer in range(5, 10, 4):
    for inner in range(1, outer, 2):
        print(outer, inner)
    print()

#nested  - two
for i in range(10):
    for j in range(i):
        print('*', end = ' ')
    print()