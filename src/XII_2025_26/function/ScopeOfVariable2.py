'''
Created on Jul 8, 2025
Code to demonstrate the use of local and global variable
@author: admin
'''
def calcsum(a,b,c) :
    s =  a+b+c
    return s

def average(x,y,z):
    sum = calcsum(x,y,z)
    if sum > 10 :
        doubelSum = sum*2
        print('sum is more then 10 -', sum)
    else :
        print('sum is less then 10 -', sum)
    return sum/3

num1 = int(input('Enter first - '))
num2 = int(input('Enter second - '))
num3 = int(input('Enter third - '))
avg = average(num1, num2, num3)
print('Average  -- ', avg)