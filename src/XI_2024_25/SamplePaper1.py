'''
Created on Mar 13, 2025

@author: admin
'''
st = 'JawaharNavodayaVidyalaya-82825'
uppers = 0
lowers = 0
alphabets = 0
digits = 0

for i in st :
    if i.isupper() :
        uppers+=1
    if i.islower() :
        lowers+=1
    if i.isalpha() :
        alphabets += 1
    if i.isdigit() :
        digits+=1

print('Uppers - ',uppers)
print('Lowers - ',lowers)
print('Alphabets - ',alphabets)
print('Digits - ',digits)