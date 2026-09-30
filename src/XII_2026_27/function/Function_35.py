'''
Created on Jul 21, 2026

@author: admin
'''
def EOReplace():
    for i in range(len(L)) :
        if L[i]%2 ==0 :
            L[i] +=1
        else :
            L[i] -=1

L = [10,20,30,40,35,55]
print('List before update - ',L)
EOReplace()
print('List after update - ',L)