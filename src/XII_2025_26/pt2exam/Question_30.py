'''
Created on Sep 30, 2025

@author: admin
'''
def mystery(n):
    if n== 0:
        return 0
    elif n%2 == 0 :
        print('Inside n%2 - ',n//2)
        return mystery(n//2)
    else :
        print('Inside else - ',n//2)
        return 1+mystery(n//2)

print(mystery(11))