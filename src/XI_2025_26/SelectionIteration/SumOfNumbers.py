'''
Created on Dec 30, 2025
Sum of numbers from 1 to 7
@author: admin
'''

sum = 0
num = int(input('Number to print sum - '))
for a in range(1, num+1):
    sum = sum+a
print('sum of natural numbers <= ',a,'is - ',sum)
print('average of natural numbers <= ',num,'is - ',sum/num)