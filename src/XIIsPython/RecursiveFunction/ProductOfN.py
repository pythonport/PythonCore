'''
Created on Sep 18, 2019

@author: admin
'''
def product(n,m):
    pro=0
    if m==0 :
        return pro
    return n+product(n,m-1)

prodnum = product(7,5)
print("Product Val - :",prodnum)