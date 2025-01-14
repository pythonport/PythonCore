'''
Created on Jan 6, 2025

@author: admin
'''

num = int(input('Number to get factors - '))
print(1, end=' ')
factor = 2
while factor <= num / 2:
    if num % factor == 0:
        print(factor, end=' ')
    factor += 1   
print(num)
print('done')
    
