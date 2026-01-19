'''
Created on Jan 2, 2026

@author: admin
'''
n = int(input('Number to check prime - '))
a= 2
while a<n :
    if n%a ==0 :
        print(f'{n} not a prime number divisible by {a}')
        break
    a +=1
else :
    print(f"{n} is a prime number")