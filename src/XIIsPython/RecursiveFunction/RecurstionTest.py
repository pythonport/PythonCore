'''
Created on Aug 20, 2019

@author: admin
'''
def printn(n):
    if n!=0:
        printn(n-1)
        print(n)

printn(10)