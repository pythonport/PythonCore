'''
Created on Sep 30, 2026

@author: admin
'''
def SHOWWORD():
    fout = open('story.txt','r')
    data = fout.read()
    words = data.split()
    for word in words :
        if len(word)<5:
            print(word)
    fout.close()
    
def SHOWWORDLINES():
    fout = open('story.txt','r')
    data = fout.readlines()
    for line in data :
        words = line.split()
        for word in words :
            if len(word)<5 :
                print(word)
    fout.close()

SHOWWORDLINES()