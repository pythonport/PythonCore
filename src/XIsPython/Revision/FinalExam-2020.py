'''
Created on Mar 19, 2020

@author: admin
'''
n = int(input("Enter value of n - "))
i = 1
sum = 0
while(i < n):
    if(i % 2 == 0) :
        sum = sum + 1
        print(sum)
    i = +1
print(sum)