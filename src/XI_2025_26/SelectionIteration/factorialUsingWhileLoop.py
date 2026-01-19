'''
Created on Dec 31, 2025

@author: admin
'''
num = int(input('Number - '))
fact = 1
a = 1
while a<=num :
    fact = fact*a
    a +=1

print(f'factorial of {num} is {fact}')
print('factorial of',num,' is ', fact)