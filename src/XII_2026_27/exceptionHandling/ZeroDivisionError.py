'''
Created on Jul 23, 2026

@author: admin
'''
try :
    num1 = int(input('First number - '))
    num2 = int(input('Second number - '))

    res = num1/num2
    print(f'{num1} / {num2} = {res}')
except Exception as e:
    print(e)
    print('Something went wrong! try again.')

print('I am outside try and except block')