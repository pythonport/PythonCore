'''
Created on Jan 15, 2021
Factorial of number using while loop
@author: admin
'''

num = int(input("Enter number to print factorial - "))
fact = 1
a = 1
while a <= num:
    fact = fact * a
    a += 1

print('Factorial of ', num, ' is - ', fact)