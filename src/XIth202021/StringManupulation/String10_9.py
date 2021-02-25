'''
Created on Feb 3, 2021
Palindrome String
@author: admin
'''
str = input("Enter any string to check palindrome - ")

if (str==str[::-1]) :
    print(str," is a palindrome string")
else :
    print(str," is a not palindrome string")