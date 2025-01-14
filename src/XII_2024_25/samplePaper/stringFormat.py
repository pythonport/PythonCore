'''
Created on Jan 14, 2025

@author: admin

a = 15
sqa = a**2
print(a, sqa)
print('square of {} is {}'.format(a, sqa))
'''

num = int(input('Number to print table - '))
for i in range(1,11):
    print('{} X {}  = {}'.format(num, i, num*i))