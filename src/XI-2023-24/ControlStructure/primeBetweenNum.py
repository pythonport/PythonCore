'''
Created on Dec 19, 2023

@author: Admin
'''
'''
pnums = []
m = int(input('Prime from - '))
n = int(input('Prime upto - '))
for num in range(m, n):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            break
    else:
        pnums.append(num)

print('Primes between {} and {} is {}'.format(m, n, pnums))
'''
m = int(input('Prime from - '))
n = int(input('Prime upto - '))
for num in range(m, n):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            break
    else:
        print(num,end=' ')