'''
Created on Jan 6, 2026

@author: admin
'''
n = 1
while n <= 10:
    if n % 2 == 0:
        continue
    print('value of n - ', n)
    n += 1
print('outside loop')
