'''
Created on Aug 13, 2026
Vowel and consonants count in a file.
@author: admin
'''
fh = open('mydata.txt','r')
vcount =  0
ccount =  0
str = fh.read()
for chr in str :
    if chr in 'aeiouAEIOU' :
        vcount+=1
    else :
        ccount+=1  

print('Total consonant - ',ccount)
print('Total vowel- ',vcount)