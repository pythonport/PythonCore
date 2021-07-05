'''
Created on Mar 31, 2021
Write a Program that reads a text file and 
prints its statistics like
     Number of uppercase letters
     Number of lowercase letters
     Number of vowels
     Number of consonant
@author: admin
'''

# opening story.txt file in read mode
fout = open('story.txt', 'r')
uc = lc = vo = co = 0
vlist = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

val = fout.read()

for i in val :
    if i.isupper() :  # checking for upper case
        uc += 1
    
    if i.islower():  # checking for lower case
        lc += 1
    
    if i in vlist :  # checking for vowel
        vo += 1
    
    if i.isalpha():  # checking for alphabet
        if i not in vlist :  # checking for consonant
            co += 1

print("No of upper case letters - ", uc)
print("No of lower case letters - ", lc)
print("No of vowels letters - ", vo)
print("No of consonants letters - ", co)
