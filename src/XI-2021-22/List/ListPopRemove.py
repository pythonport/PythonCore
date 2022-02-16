'''
Created on Feb 9, 2022

@author: admin
'''
lst = [34, 33, 44, 22, 65]
print("list before pop - ", lst)
a = lst.pop(1)
print("list after pop - ", lst)
print("popped value -", a)
print('removing last element - ', lst.pop())
print("list after poping last element - ", lst)