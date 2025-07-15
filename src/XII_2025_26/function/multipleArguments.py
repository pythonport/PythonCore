'''
Created on Apr 15, 2025

@author: admin
'''
#Arbitrary Arguments, *args
def sum(*args):
    s = 0
    for i in args :
        s +=i
    print('Sum value is - ',s)

sum(4,5)
sum(4,5,6)