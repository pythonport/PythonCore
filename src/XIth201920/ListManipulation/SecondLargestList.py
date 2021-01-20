'''
Created on Jan 3, 2020

@author: admin
'''
lst = [34, 55, 66, 44, 33]
print(lst)

lst.sort()
print(lst)
print('Second largest - ',lst[len(lst)-2])

lst.sort(reverse=True)
print(lst)
print('Second largest - ',lst[1])