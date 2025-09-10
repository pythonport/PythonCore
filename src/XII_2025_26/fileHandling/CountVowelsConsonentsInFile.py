'''
Created on Aug 1, 2025

@author: admin
'''
fout = open('jangalbook.txt', 'r')
str = fout.read()
vlist = ['a','A','e','E','i','I','o','O','u','U']
vcount = 0
ccount = 0
special = 0
for ch in str :
    if(ch.isalpha()) :
        if ch in vlist :
            vcount+=1
        else :
            ccount+=1
    else :
        special +=1
print('Vowel count is - ',vcount)
print('Consonent count is - ',ccount)
print('Special count is - ',special)
fout.close()