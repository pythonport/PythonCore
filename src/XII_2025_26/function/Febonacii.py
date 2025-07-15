'''
Created on Apr 12, 2025

@author: admin
'''
x = 0
y = 1
terms = int(input('Enter n terms for febonacii series - '))
print(x,y,end = ' ')
for i in range(terms) :
    z = x+y
    print(z, end=' ')
    x,y = y,z
