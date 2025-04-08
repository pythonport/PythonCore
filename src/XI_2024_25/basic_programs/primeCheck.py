'''
Created on Mar 1, 2025

@author: admin
'''

n = 1665877981
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print(n, 'is not a prime number divisable by - ',i)
        break
else:
    print(n, 'is a prime number')
