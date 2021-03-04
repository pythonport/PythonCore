'''
Created on Feb 26, 2021

@author: admin
'''
n = int(input("Number till you want fibonacci series - "))
first = 0
second = 1
print(first, end=' ')
print(second, end=' ')
for i in range(1, n):
    third = first + second
    print(third, end=' ')
    first, second = second, third
