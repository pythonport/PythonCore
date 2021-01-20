'''
Created on Aug 9, 2019

@author: admin
'''
n = int(input('Enter number to check prime - '))


def primeCheckMethod1(n):
    prime_flag = 1    
    for i in range(2, n):
        if (n % i == 0):
            prime_flag = 0
            break
    return prime_flag


def primeCheckMethod2(n):
    prime_flag = 0   
    i=2 
    while (i*i<=n):
        if (n % i == 0):
            prime_flag = 1
            break
        i=+1
    return prime_flag

#pf = primeCheckMethod1(n)

pf = primeCheckMethod2(n)
if pf:
    print(n, ' is a prime number')
else :
    print(n, ' is not a prime number')    
