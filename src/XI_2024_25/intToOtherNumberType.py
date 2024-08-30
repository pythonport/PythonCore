'''
Created on Aug 13, 2024

@author: admin
'''
print('Any Integer number to Other Number system')
number = int(input('Integer Number - '))
bnum = bin(number)
onum = oct(number)
hnum = hex(number)

print('Binary is - ',bnum)
print('Octal is - ',onum)
print('Hexa is - ',hnum)