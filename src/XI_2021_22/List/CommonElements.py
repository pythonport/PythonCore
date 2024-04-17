'''
Created on Mar 5, 2022
Program to find the common element in python list
@author: admin
'''
lst = [2,33,4,66,33,4,11,2]

comn = []
for i in lst :
    if (lst.count(i) >1 and i not in comn) :
        comn.append(i)

print("Common elements are - ",comn)
        