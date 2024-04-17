'''
Created on Feb 9, 2022

@author: admin
'''
lst1 = [34, 33, 44, 22, 65]
lst2 = []
print('List 1 - ', lst1)

for i in range(len(lst1)) :
    lst2.append(lst1.pop())

print('List 1 - ', lst1)
print('Reverse List 2 - ', lst2)
