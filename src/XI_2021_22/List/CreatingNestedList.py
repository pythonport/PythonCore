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
        #ele = int(input('input element ',str[i],' , ',str[j],' : - '))
        ele = int(input("Enter element - "))
        row.append(ele)
    print('Element at ',i, 'is - ',row)
    lst.append(row)
    
print("New list is - ", lst)
