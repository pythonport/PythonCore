'''
Created on Oct 21, 2020
Program to calculate first 5 multiples of 
any number
@author: admin
'''

def First5Multiples(x):
    print(x,'* 1 = ',x*1)
    print(x,'* 2 = ',x*2)
    print(x,'* 3 = ',x*3)
    print(x,'* 4 = ',x*4)
    print(x,'* 5 = ',x*5)

num = int(input("Enter any number to get 5 multiples - "))
First5Multiples(num)