'''
Created on Jul 27, 2024

@author: admin
'''
x = 12
print('Decimal is - ',x)
bx = bin(x)
print('binary is - ',bx)
ox = oct(x)
print('octal is - ',ox)
hx = hex(x)
print('hexadecimal is - ',hx)

binstr = '1100110011'
intval = int(binstr, 2)
print('Integer of binstr - ',intval)

binput = input('enter binary - ')
intv = int(binput, 2)
print('Integer of binstr - ',intv)