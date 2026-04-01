'''
Created on Feb 18, 2026

@author: admin
'''
str = 'Python is most popular language in 2026'
lower = upper = digits = 0
for a in str :
    if a.isupper():
        upper+=1
    elif a.islower():
        lower+=1
    elif a.isdigit():
        digits+=1

print("Lowers - ",lower)
print("Uppers - ",upper)
print("Digits - ",digits)