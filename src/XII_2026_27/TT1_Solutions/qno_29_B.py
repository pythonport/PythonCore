'''
Created on Sep 30, 2026

@author: admin
'''
def linecount():
    fout = open('para.txt','r')
    lcount = 0
    lines = fout.readlines()
    for line in lines :
        if line[0] =='H' :
            lcount+=1
    print('Line starts with H - ',lcount)

linecount()