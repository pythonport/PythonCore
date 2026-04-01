'''
Created on Mar 19, 2026

@author: admin
'''
def readStoryWithList():
    fout = open('STORY.TXT','r')
    listLines = fout.readlines()
    vlist = ['a','A','e','E','i','I','o','O','u','U']
    for line in listLines :
        if line[0] not in vlist :
            print(line)
    fout.close()
    
    
def readStoryWithString():
    fout = open('STORY.TXT','r')
    listLines = fout.readlines()
    vowels = 'aeiou'
    for line in listLines :
        if line[0].lower() not in vowels :
            print(line)
    fout.close()
            
readStoryWithString()
