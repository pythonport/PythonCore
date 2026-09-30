'''
Created on Jul 28, 2026
Program to handle different type of exception with single try block
@author: admin
'''
try :
    lst = [1,2,3]
    lst[4]=33  # lst
    val = lst[2]/0
    num = int('hello')
except IndexError as e :
    print(str(e))
except ZeroDivisionError as e :
    print(str(e))
except ValueError as e :
    print(str(e))
else :
    print('NO error CLEAN Code')