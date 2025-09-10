'''
Created on Sep 2, 2025

@author: admin
'''
lst  = [2,3,4,5,6]
i = 0
try :
    while True :
        print(lst[i])
        i+=1
except IndexError :
    print('reading data out of index')