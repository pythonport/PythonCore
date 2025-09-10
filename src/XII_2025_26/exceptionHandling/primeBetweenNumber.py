'''
Created on Sep 4, 2025

@author: admin
'''
m = int(input('First Number - '))
n = int(input('Second Number - '))
for num in range(m,n+1) :
    for i in range(2, num//2+1) :
        if num%i ==0 :
            break
    else :
        print(num,end =' ')