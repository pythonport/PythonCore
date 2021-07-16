'''
Created on Jul 16, 2021

@author: admin
'''
lst1 = [1,2,3]
lst2 = [4,5,6,7]
lst3 = [6,7]
print('Original List is - ')
print(lst1)
print(lst2)
print(lst3)
lst3.extend(lst1)
print(lst3)
lst3.extend(lst2)
print(lst3)