'''
Created on Sep 4, 2020
Traversing in 2D array
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
print ("==== Traversal in a 2-D array =======")
print('List = [')
for i in range(r) :
    print('\t\t[',end = " ")
    for j in range(c) :
        print(lst[i][j],end=" ")
    print("]")
print('\t ]')