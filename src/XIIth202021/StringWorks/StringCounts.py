'''
Created on Jun 23, 2020
Program that reads a line and prints its statics likeuppercase,
 lowercase, alphabets and digits.
@author: admin
'''
line = input('Enter a line - ')
lowercount = uppercount = 0
digitcount = alphacount = 0
specialcount = 0

for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
    if a.isalpha():
        alphacount += 1
    if a.isalnum()==False :
        specialcount+=1
        
print('Number of uppercase letters - ', uppercount)
print('Number of lowercase letters - ', lowercount)
print('Number of alphabets letters - ', alphacount)
print('Number of digits - ', digitcount)
print('Number of Special Characters - ', specialcount)