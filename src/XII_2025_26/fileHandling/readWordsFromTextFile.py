'''
Created on Aug 1, 2025

@author: admin
'''
fout = open('jangalbook.txt', 'r')
str = fout.read()
for word in str.split():
    print(word, end='#')
    
    
    
    
    