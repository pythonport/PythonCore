'''
Created on Mar 3, 2021
Word count in a file called story.txt
@author: admin
'''
def vowelcount():
    fout = open('story.txt','r')
    sval = fout.read()
    lstval = sval.split()
    wcount = len(lstval)      
    print("Total Word count is -",wcount) 
    fout.close()
    
vowelcount()