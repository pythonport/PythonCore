'''
Created on Jan 21, 2025

@author: admin
'''
str = input('enter string - ')
uppers = 0
lowers = 0
digits = 0
spaces = 0
specials = 0

for ch in str :
    if ch.isupper() :
        uppers +=1
    elif ch.islower():
        lowers +=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces +=1
    else :
        specials +=1

print('upper cases are - ', uppers)
print('lower cases are - ', lowers)
print('digits are - ', digits)
print('spaces are - ', spaces)
print('specials are - ',specials)