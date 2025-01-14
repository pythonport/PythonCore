'''
Created on Jan 9, 2025

@author: admin
'''
primeList = []
for i in range(2,20):
    j= 2
    while ( j <= (i/2)):
        if (i % j == 0):
            break
        j += 1
    else :
        primeList.append(i)  
print(primeList)
print ("Bye Bye!!")