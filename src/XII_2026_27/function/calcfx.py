'''
Created on Apr 17, 2026

@author: admin
'''

def calcfx(x):
    result = 2*x**2
    return result

a = 100
res  = calcfx(a)   
print(f'fx value of {a} is {res}') 


res  = calcfx(200)   
print(f'fx value of {200} is {res}') 

res  = calcfx(a+10)   
print(f'fx value of {a+10} is {res}') 