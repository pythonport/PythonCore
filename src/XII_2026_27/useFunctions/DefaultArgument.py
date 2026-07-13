'''
Created on Jul 8, 2026

@author: admin
'''


def simpleInterest(princ, time, rate= 5):
    si = princ * time * rate / 100
    print('Simple Interest  - ',si)


princ = 1000
time = 5
rate =  7

simpleInterest(princ, time, rate)

simpleInterest(time = 20, rate = 6, princ = 10000)
