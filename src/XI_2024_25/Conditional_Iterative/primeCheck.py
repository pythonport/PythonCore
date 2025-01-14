'''
Created on Jan 7, 2025

@author: admin
'''
n = int(input('Number to check prime - '))
flag = 0
div = 0
if n > 1:
    for i in range(2, n//2+1):
        if n % i == 0:
            flag = 1
            div  = i
            break
    if flag == 1:
        print(n, ' is not a prime number divisible by',div)
    else:
        print(n, ' is a prime number')