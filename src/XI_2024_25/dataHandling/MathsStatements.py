'''
Created on Dec 14, 2024

@author: admin
'''
import math
a, b, c = 20, 10, 30
msqrt = math.sqrt(a ** 2 + b ** 2 + c ** 2)
print(msqrt)

print('----------')
y = 2
yexp = 2 - y*math.exp(2*y) +4*y
print(yexp)

print('----------')
p, q,r,s = 2, 4,5,6
mpower = p+q/math.pow(r+s,4)
print(mpower)