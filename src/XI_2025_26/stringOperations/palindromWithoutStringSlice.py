'''
Created on Jan 24, 2026

@author: admin
'''
str = input('Strint to check Palindrome - ')
length = len(str)
mid = length//2
rev = -1

for a in range(mid):
    if str[a] == str[rev] :
        a+=1
        rev-=1
    else :
        print(str,' is not a palindrome')
        break
else :
    print(str,' is a palindrome')