'''
Created on Dec 30, 2024

@author: admin
'''


def Puzzle(w, n):
    for i in range(len(w)):
        if w[i] == n:
            nw = w.replace(w[i], '_')
            print(nw)


str = 'pythonprogramming'
Puzzle(str, 3)
