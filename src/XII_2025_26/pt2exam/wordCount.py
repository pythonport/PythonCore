'''
Created on Sep 11, 2025

@author: admin
'''

def countWords():
    fh = open('Words.txt','r')
    str = fh.read()
    words = str.split()
    for word in words :
        if len(word) >5 :
            print(word)

countWords()