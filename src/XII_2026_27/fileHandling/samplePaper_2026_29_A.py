'''
Created on Aug 21, 2026

@author: admin
'''
def pythonCount():
    fout = open('prog.txt','r')
    str = fout.read()
    words = str.split()
    count = 0
    for word in words :
        if word =='python':
            count+=1
    print('total python count is - ',count)
    
def pythonCount1():
    fout = open('prog.txt','r')
    str = fout.read()
    count = str.count('python')
    print('total python count is - ',count)
    
pythonCount()
pythonCount1()