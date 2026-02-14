'''
Created on Feb 6, 2026

@author: admin
'''
line = input('Enter line - ')
lowers = uppers = digits = alphas = symbols = 0
for a in line:
    if a.islower(): 
        lowers += 1
    elif a.isupper():
        uppers += 1
    elif a.isdigit():
        digits += 1
    elif a.isalnum() != True and a != ' ':
        symbols += 1
        
    if a.isalpha():
        alphas += 1

print('Lowers count -', lowers)
print('Uppers count -', uppers)
print('Digits count -', digits)
print('Alphabets count -', alphas)
print('Symbols count -', symbols)
