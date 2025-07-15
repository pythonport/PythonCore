'''
Created on Apr 17, 2025

@author: admin
'''


def sum1(a, b):  # outer function
    sum = a ** 2 + b ** 2
    print('Square sum of {} and {} is {}'.format(a, b, sum))


n1 = 4
n2 = 6
sum1(3.5, 5.5)
sum1(n1, n2)
sum1(n1 + 3, n2 * 2)
