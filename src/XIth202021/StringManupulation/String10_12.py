'''
Created on Feb 10, 2021

@author: admin
'''
s = input("Enter any decimal string to get fraction part - ")
tpl = s.partition('.')
print("Actual String is - ",s)
print("fractional Part of String is - ",tpl[2])