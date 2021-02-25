'''
Created on Jan 25, 2021
Pattern using for loop from inner to outer
@author: admin
'''

for a in range(8):
    for b in range(0, a):
        print(a,b , end='   ')
    print()
