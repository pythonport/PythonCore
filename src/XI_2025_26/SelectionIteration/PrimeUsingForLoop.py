'''
Created on Jan 9, 2026
Prime check using nested for loop
@author: admin
'''
for num in range(5, 50) :
    lim = num//2+1
    for i in range(2, lim) :
        if num%i == 0 :
            print(num,' is not prime divisible by ',i)
            break
    else :
        print(num,' is prime number')