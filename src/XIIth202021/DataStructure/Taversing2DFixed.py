'''
Created on Sep 4, 2020
Traversing in 2D array
@author: admin
'''
lst = [[2, 3, 4], [5, 6, 2], [3, 4, 5], [6, 7, 8]]
row = len(lst)
col = len(lst[0])
print("Row - " + str(row) + " Column - ", col)
for i in range(row):
    print(str(i + 1) + " Row is - [", end=" ")
    for j in range(col):
        print(lst[i][j], end=' ')
    print(']')    
    print()    
print("done")
