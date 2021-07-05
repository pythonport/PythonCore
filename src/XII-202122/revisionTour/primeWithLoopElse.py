'''
Created on Jul 1, 2021

@author: admin
'''
n = int(input('Enter the number to check prime - '))
for a in range(2, n // 2 + 1) :
    if n % a == 0:
        print('{0} is NOT a prime number'.format(n))
        break
else :
    print('{0} is a prime number'.format(n))

