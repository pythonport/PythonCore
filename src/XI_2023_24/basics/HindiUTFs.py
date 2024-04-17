'''
Created on Sep 20, 2023

@author: Admin
'''
start = 2309
for i in range(60):
    print(chr(start),' ', end='')
    start +=1
    if i%10 == 0 :
        print()