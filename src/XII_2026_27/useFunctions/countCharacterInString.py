'''
Created on Apr 16, 2026
Program to count the character in string and store in dictionary
@author: admin
'''

#str = 'sdafasdfasdfasuowerwqelkjldxzbvzxmncbmnh3y234534tekddskllk'
str = 'Maine aaj dictionary padha hai. saath in turtle art bhi padha'
dcchr = {}
for i in str :
    dcchr[i]=str.count(i)

for key,value in dcchr.items():
    print(f'{key}->{value}')