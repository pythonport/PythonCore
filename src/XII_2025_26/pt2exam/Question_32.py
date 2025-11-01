'''
Created on Sep 30, 2025

@author: admin
'''
def countPython():
    pythonCount = 0
    fout = open('Prog.txt')
    rec = fout.read()
    listrec = rec.split()
    for word in listrec :
        if word =='python' :
            pythonCount+=1
    print('total python count is  - ',pythonCount)
    
countPython()