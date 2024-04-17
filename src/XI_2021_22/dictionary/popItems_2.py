'''
Created on Mar 14, 2022

@author: admin
'''
d = {1:33, 2:44, 5:44, 6:76}
print(d)
popedVal = d.popitem()
print(popedVal)
popedVal = d.clear()
print(popedVal)
print(d)