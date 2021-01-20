'''
Created on Sep 3, 2020
2-D array using user input
@author: admin
'''
lst=[]
r = int(input("how many row - "))
c = int(input("how many column - "))
for i in range(r) :
    row = []
    for j in range(c):
        ele = int(input('Element '+str(i)+','+str(j)+' : '))
        row.append(ele)
    lst.append(row)
    
print("List is  - ",lst)