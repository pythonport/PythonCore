'''
Created on Feb 7, 2022

@author: admin
'''
lst = [1, [1, 2, 3], [1, 2], 'hello']
print('length of list - ', len(lst))
print(lst[1])
print(lst[1][1])
print(lst[2][1])
print('--------------')
a = [1, 4, 5, 2, 3, 2, 4, 5, 1]

print(a.index(4))
a.append([7,3])
print(a)

a.extend([7,3,5,6,8])
print(a)