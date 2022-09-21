'''
Created on Mar 28, 2022

@author: admin
'''
num = 146

a = 2
while a<=(num//2+1) :
    if (num==1 or num%a == 0) :
        print(num, " is not a prime number")
        print("is divisible by ",a)
        break
    a+=1
else :
    print(num, " is a prime number")
    