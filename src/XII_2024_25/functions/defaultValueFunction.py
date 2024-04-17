'''
Created on Apr 15, 2024

@author: admin
'''


def interest(principal, time, rate=10):
    sival = (principal * time * rate) / 100
    return sival


sivalue = interest(1000, 5, 8)
print("interest is - ", sivalue) 
   
sivalue = interest(1000, 5)
print("interest with default rate is - ", sivalue)    
