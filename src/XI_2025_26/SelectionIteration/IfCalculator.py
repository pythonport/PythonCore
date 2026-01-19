'''
Created on Dec 22, 2025

@author: admin
'''
n1 = int(input('First number - '))
n2 = int(input('Second number - '))
op = input('Operator [+, - , *, /, %] - ')
result = 0

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    result = n1 / n2
elif op == '%':
    result = n1 % n2
else:
    print('invalid operator')

print(n1, op, n2, '=', result)
