'''
Created on Sep 11, 2025

@author: admin
'''

def countcmail():
    fh = open('Emails.txt', 'r')
    str = fh.read()
    lstr = str.split()
    for word in lstr :
        if '@cmail' in word :
            print(word)

countcmail()