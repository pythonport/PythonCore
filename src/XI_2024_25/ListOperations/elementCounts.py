'''
Created on Jan 30, 2025
Program to count he occurrence of every element in a list
@author: admin
'''
lst = [45,45,12,12,6,6,8,7,3,3,3,6]
dc = {}
for i in lst :
    count = lst.count(i)
    dc[i] = count
print(dc)