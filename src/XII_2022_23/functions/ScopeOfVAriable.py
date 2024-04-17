'''
Created on Jul 29, 2022

@author: admin
'''
a = 10


def scopeTest():
     x = 90
     global a
     a = 50
     sum = x + a
     print("inside function x - ", x)
     print("inside function a - ", a)
     print('Sum is - ', sum)

     
print("Line 18 outside function a - ", a)
scopeTest()
print("Line 20 outside function a - ", a)
# print("outside function x - ", x)
