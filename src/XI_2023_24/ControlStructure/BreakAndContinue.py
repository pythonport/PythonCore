'''
Created on Dec 19, 2023

@author: Admin
'''
for i in range(1,11):
    if i%3 == 0 :
        break
    else :
        print(i)
        
print('==========')
for i in range(1,11):
    if i%3 == 0 :
        continue
    else :
        print(i)