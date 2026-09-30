'''
Created on Jul 29, 2026

@author: admin
'''
try :
    num1 = int(input('First number - '))
    num2 = int(input('Second number - '))
    if num2== 0 :
        raise ZeroDivisionError(f'{num1}/{num2} is not possible')
    res = num1/num2
    print(f'{num1} / {num2} = {res}')
except ZeroDivisionError as e:
    print(str(e))