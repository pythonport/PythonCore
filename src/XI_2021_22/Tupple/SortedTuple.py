'''
Created on Feb 25, 2022

@author: admin
'''
t = (3, 3, 3, 54, 33, 44, 22, 22, 11)
print("Tuple before sorting - ", t)
temp = sorted(t)
t = tuple(temp)
print("Tuple after sorting - ", t)
