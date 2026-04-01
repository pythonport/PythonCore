'''
Created on Mar 19, 2026

@author: admin
'''
def readPython():
    fout  = open('Prog.txt','r')
    str = fout.read()
    words = str.split()
    count = 0
    for word in words :
        if word =='Python' :
            count+=1
    
    print('Python count is  - ',count) 
    fout.close()
    
readPython()