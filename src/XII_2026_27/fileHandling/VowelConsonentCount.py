'''
Created on Aug 13, 2026
Word count starts with vowel and consonants
@author: admin
'''
fh = open('mydata.txt','r')
vwordcount =  0
cwordcount =  0
str = fh.read()
for word in str.split() :
    if word[0] in 'aeiouAEIOU' :
        vwordcount+=1
    else :
        cwordcount+=1  

print('word starts with consonant - ',cwordcount)
print('word starts with vowel- ',vwordcount)