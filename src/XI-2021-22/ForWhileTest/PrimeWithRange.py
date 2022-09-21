'''
Created on Apr 6, 2022

@author: admin
'''

lstPrime = []
for num in range(30,70) :
    a = 2
    while a<=(num//2+1) :
        if (num==1 or num%a == 0) :
            break
        a+=1
    else :
        lstPrime.append(num)
        
print("prime numbers are - ",lstPrime)