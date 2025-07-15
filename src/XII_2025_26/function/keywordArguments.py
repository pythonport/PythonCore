'''
Created on Apr 24, 2025

@author: admin
'''

def simpleInterest(p, t, r):
    si = p * t * r / 100
    print('Simple Interest is  - ', si)
    
pri,ti, rt = 5000,4,12
simpleInterest(pri, ti, rt)
#simpleInterest(pri=1000, ti=5, rt=6) Invalid as argument name is not same as parameter name
simpleInterest(r=4,p=4000,t=5)