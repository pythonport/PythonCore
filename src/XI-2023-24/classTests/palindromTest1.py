'''
Created on Mar 27, 2024

@author: Admin
'''
str = input('Enter palindrome string - ')
strrev = str[::-1]
if str == strrev:
    print('string is palindrome')
else :
    print('not palindrome')