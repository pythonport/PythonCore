'''
Created on Jul 11, 2025
function call with mutable data type (changes done in local will reflect to global variable)
@author: admin
'''


def function1(list):
    print('list in function before change -', list)
    l1 = [77,66]
    list.append(88)
    print('list in function after change -', list)
    list = l1
    list.append(33)
    print('list in function after change -', l1)
    print('list in function after change -', list)


lst = [1, 55, 22]
print('lst before function call -', lst)
function1(lst)
print('lst after function call -', lst)
