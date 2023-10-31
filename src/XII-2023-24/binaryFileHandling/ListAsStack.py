'''
Created on Sep 13, 2023

@author: Admin
'''
lst = [1,4,6,7,7,6,5,4,3]
print('top - ',lst[len(lst)-1])
lst.append(8)
lst.append(18)
lst.append(28)
print('List - ',lst)
print('top - ',lst[len(lst)-1])
lst.pop()
lst.pop()
lst.pop()
lst.pop()
print('List - ',lst)
print('top - ',lst[len(lst)-1])