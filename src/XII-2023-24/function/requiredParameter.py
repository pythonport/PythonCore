'''
Created on Jul 6, 2023

@author: ACER
'''


def calcinterest(p, t=4, r=5):
    interest = (p * t * r) / 100
    return interest


it = calcinterest(5000, 5, 10)
print('Interest - ', it)

#value if default paramenter available
it = calcinterest(5000, 5)
print('Interest - ', it)

it = calcinterest(5000)
print('Interest - ', it)

#keyword parameter
it = calcinterest(r=15, p=4000, t=3)
print('Interest - ', it)
