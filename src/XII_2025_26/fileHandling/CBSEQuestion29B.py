'''
Created on Jul 8, 2025
Write a program to print the word start and ends with vowel
@author: admin
'''

fout = open('story.txt')
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowstr = ''
str = fout.read()
words = str.split()
for word in words :
    length = len(word)
    if word[0] in vowels and word[length-1] in vowels :
        vowstr += word+' '

print(vowstr) 