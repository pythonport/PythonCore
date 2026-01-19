'''
Created on Dec 31, 2025

@author: admin
'''
factorial = 1
num = int(input('Number to print factorial - '))

for a in range(1, num+1):
    factorial = factorial * a
    print('factorial of number',a,' is - ',factorial)