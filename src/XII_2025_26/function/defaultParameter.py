'''
Created on Apr 23, 2025

@author: admin
Code to demonstrate the use of default parameter in function call.
'''


def simpleInterest(p, t=4, r=10):
    si = p * t * r / 100
    print('Simple Interest is  - ', si)


simpleInterest(1000, 5, 8)
simpleInterest(1000, 5)
simpleInterest(1000, 5, 4.5)
simpleInterest(1000)

simpleInterest(5000, r = 15)