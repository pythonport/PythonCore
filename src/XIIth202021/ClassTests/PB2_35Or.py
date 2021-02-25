'''
Created on Feb 16, 2021
Write a function vowelCount() in python to read each character of a text file
story.txt. Function should count and display the occurance of the vowel
alphabet 'a','e','i','o','u' (including upper case too).
@author: admin
'''


def vowelCount() :
    fout = open(r'story.txt', 'r')
    lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    stmt = fout.read()
    vouwelcount = 0 
    for i in stmt :
        if i in lst :
            vouwelcount += 1

    print("Total vowel count is -", vouwelcount)


vowelCount()
