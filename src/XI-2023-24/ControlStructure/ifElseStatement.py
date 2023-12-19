'''
Created on Nov 29, 2023

@author: Admin
'''
a = int(input('Enter first number - '))
b = int(input('Enter second number - '))
if a > b :
    print("a is greater")
elif b>a :
    print("b is greater")
else :
    print('both are equal')


ch = input('Enter character - ')
if ch >= '0' and ch <= '9' :
    print('You have entered a digit')
    print('Digit is - ',ch)
else :
    print('Something else')
    print('Characer is - ',ch)


a = int(input('First No - '))
b = int(input('Second No - '))
if (a>b) :
    print('A is greater')
else :
    print('B is greater')
    