'''
Created on Sep 4, 2025
Code to check the prime number
@author: admin
'''
num = int(input('Number to check prime - '))
for i in range(2, num//2+1) :
    if num%i ==0 :
        print('{} is divisible by {}, NOT PRIME'.format(num,i))
        break
else :
    print(num, 'IS A PRIME NUMBER')