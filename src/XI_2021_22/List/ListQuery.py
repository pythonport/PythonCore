'''
Created on Mar 8, 2022

@author: admin
'''
a = [18, 23, 69, [73]]
b = list(a)
a[3][0] = 110
a[1] = 34
print('a - ',a)
print('b - ',b)