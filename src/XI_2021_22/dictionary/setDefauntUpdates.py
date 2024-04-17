'''
Created on Mar 9, 2022

@author: admin
'''
dc = {'v1':'a', 'v2':'e', 'v3':'i', 'v4':'o', 'v5':'u'}

print(dc.setdefault('v6', 'aa'))
print(dc)

print(dc.setdefault('v2', 'ee'))
print(dc)

print("update dictionary")
dc1 = {'v1':'a', 'v2':'e', 'v3':'ff', 'v11':'a', 'v22':'e', 'v33':'ff'}
print(dc1)
dc1.update(dc)
print(dc1)

# dc2 = dc1.update(dc)
# print(dc2)
