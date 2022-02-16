'''
Created on Feb 12, 2022

@author: admin
'''
lst = []
r = int(input("Enter the number of rows - "))
c = int(input("Enter the number of columns - "))

for i in range(r) :
    row = []
    for j in range(c):
        ele = int(input("Enter element - "))
        row.append(ele)
    lst.append(row)
print(lst)    
#List printed format is
print("List printed is ")
for i in range(r) :
    for j in range(c):
        print(lst[i][j], end=' ')
    print()