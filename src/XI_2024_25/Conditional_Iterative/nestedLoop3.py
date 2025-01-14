'''
Created on Jan 8, 2025

@author: admin
'''
num = 5
for i in range(num + 1, 1, -1):
    for j in range(i + 1, 0, -1):
        print(j, end=' ')
    print()


"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
#print('*', end=' ')
#print(i, end=' ')
#print(j, end=' ')