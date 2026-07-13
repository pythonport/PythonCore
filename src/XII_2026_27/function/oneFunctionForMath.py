'''
Created on Apr 21, 2026
Code for calculator function where one function work differently depend up on operator
@author: admin
'''
def calculator(x,y,op):
    if op=='+' :
        res = x+y
    elif op=='-' :
        res = x-y
    elif op=='*' :
        res = x*y
    elif op=='/' :
        res = x/y
    elif op=='%' :
        res = x%y
    else :
        return 'Something wrong'
    return res

a = int(input('First number -'))
b = int(input('Second number -'))
op = input('Enter operator [+,-,*,/,%] - ')

res = calculator(a, b, op)
print(f'{a}{op}{b} = {res}')