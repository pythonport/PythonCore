'''
Created on Jan 23, 2025

@author: admin
'''
lst = [23,24,21,24,23,22,25]
print(lst)
print(lst[2])  #21
print(lst[6]) #25

n = len(lst)
print(lst[n-1]) #25
print(lst[-n])  #23

lst[6] = 30 #list value can be changed so it is mutable
print(lst)