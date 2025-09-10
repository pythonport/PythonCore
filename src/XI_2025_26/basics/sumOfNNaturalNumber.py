'''
Created on Aug 30, 2025
Program to sum n natural number
@author: admin
'''
n = int(input('Number to get sum - '))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print('Sum of numbers till', n, '=', sum)