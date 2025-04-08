'''
Created on Jan 28, 2025

@author: admin
'''
a = [1,2,3,44,33]
num = int(input('Number to get index - '))

if num in a :
    print(a.index(num))
else :
    print('Not present')