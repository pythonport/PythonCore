'''
Created on Aug 18, 2025

@author: admin
'''
def simpleinterest(p,t,r):
    si = (p*t*r)/100
    print('Simple interest is - ',si)

principal = int(input('Principal - '))
time = int(input('Time - '))
rate = int(input('rate - '))
simpleinterest(principal, time, rate)