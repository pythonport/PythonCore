'''
Created on Dec 24, 2025

@author: admin
'''
# example of nested if else
marks = int(input('Enter marks - '))
if marks>= 60 :
    if marks >=80:
        print('first division with distinction')
    else :
        print('first division')
else :
    if marks >=33 :
        print('pass')
    else :
        print('fail')