'''
Created on Mar 3, 2021
Vowel count in a file called story.txt
@author: admin
'''

def vowelcount():
    fout = open('story.txt','r')
    sval = fout.read()
    lst = ['a','e','i','o','u','A','E','I','O','U']
    vcount = 0
    for i in sval : 
        if i in lst :
            vcount+=1    
    print("Total Vowel count is -",vcount)
    fout.close()
    
vowelcount()