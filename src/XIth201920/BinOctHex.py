'''
Created on Jul 22, 2019
Program to convert decimal number into other number format
@author: admin
'''
num = int(input('Enter any number - '))
bnum = bin(num)
onum = oct(num)
hnum = hex(num)

print('Binary of {0} is {1}'.format(num,bnum))
print('Octal of {0} is {1}'.format(num,onum))
print('Hexadecimal of {0} is {1}'.format(num,hnum))