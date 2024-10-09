'''
Created on Oct 9, 2024
Code to demonstrate the use of exception handling in python
using try, except and finally block.
@author: admin
'''

try:
    # code which may cause exception will remain in try block
    a = 10 / 5
    #a = 10 / 0
    print("value is - ", a)
except:
    # exception block will execute one exception occurs in try block
    print('ZERO Division Error')
finally:
    # finally block will execute always, even exception occurs or not.
    print('I am in finally block')
