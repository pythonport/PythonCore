'''
Created on Feb 29, 2024

@author: Admin
'''
str = input('Enter palindrome string - ')
length = len(str)
mid = length//2
rev=-1
for a in range(mid+1) :
    if str[a]==str[rev] :
        rev-=1
    else :
        print(str,' is not palindrome')
        break
else :
        print(str,' is a palindrome')