'''
Created on Feb 9, 2022

@author: admin
'''
lst1 = [34, 33, 44, 22, 33, 65]
print('count of 33 in list - ', lst1.count(33))
print('count of 33 in list - ', lst1.count(22))
print('count of 33 in list - ', lst1.count(122))
'''
print('list before reverse - ',lst1)
lst1.reverse()
print('list after reverse - ',lst1)
'''

print('list before sorting - ',lst1)
lst1.sort(reverse=True)
print('list after sorting in descending - ',lst1)
lst1.sort()
print('list after sorting increasing order- ',lst1)