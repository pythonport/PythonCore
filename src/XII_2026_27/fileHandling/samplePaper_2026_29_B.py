'''
Created on Aug 21, 2026

@author: admin
'''
def lines_print():
    fout = open('prog.txt','r')
    vowels = 'aeiouAEIOU'
    lines = fout.readlines()
    for line in lines :
        if line[0] not in vowels :
            print(line)
            
lines_print()