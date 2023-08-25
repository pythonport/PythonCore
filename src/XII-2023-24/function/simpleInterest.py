'''
Created on Aug 9, 2023

@author: Admin
'''


def simpleInterest(p, t, r):
    si = (p * t * r) / 100
    return si


p = float(input("Principal - "))
t = float(input("Time - "))
r = float(input("Rate - "))
sivalue = simpleInterest(p, t, r)
print('Interest amount is - ', sivalue)
print('Principal - {0}, Time - {1}, Rate - {2}, Interest - {3}'.format(p, t, r, sivalue))
