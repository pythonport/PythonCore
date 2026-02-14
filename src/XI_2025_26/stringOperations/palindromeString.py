'''
Created on Jan 22, 2026

@author: admin
'''
str = input('Check Palindrome - ')

if str==str[::-1] :
    print(str,' is a palindrome string')
else :
    print(str,' is not a palindrome string')