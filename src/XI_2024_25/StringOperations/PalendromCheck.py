'''
Created on Jan 21, 2025

@author: admin
'''
str = input('String to check palendrom - ')
rev = -1
for i in range(len(str)) :
    if str[i]!=str[rev] :
        print("STRING IS not PALENDROM")
        break
    rev -=1
else :
    print("STRING IS PALENDROM")
'''
str = input('String to check palendrom - ')
rev = -1
flag = 0
for i in range(len(str)) :
    if str[i]!=str[rev] :
        print("STRING IS not PALENDROM")
        flag = 1
        break
    rev -=1
if flag ==0 :
    print("STRING IS PALENDROM")
'''