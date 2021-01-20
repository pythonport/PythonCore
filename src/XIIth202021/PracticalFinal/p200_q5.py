'''
Created on Jan 20, 2021
Write a program to count the number of 
upper-case alphabets present in a text file Article.txt
@author: admin
'''

fout = open("Article.txt", 'r')
chars = fout.read()
countupper = 0
for a in chars :
    if a.isupper() :
        countupper += 1

print("Total upper case character is  - ", countupper)
fout.close()
