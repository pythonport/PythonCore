'''
Created on Jan 15, 2020

@author: pythonport.com
'''

n = 14
for i in range(2,n-1):
    if n%i==0 :
        print('{0} is not a prime number.'.format(n))
        break
else :
    print('{0} is a prime number.'.format(n))