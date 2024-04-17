'''
Created on Mar 24, 2022
1. Write a python program to find the highest 2 values in a dictionary.
@author: admin
'''

dc = {1:54, 2:57, 3:67, 4:12, 8:17}
vlist = sorted(dc.values(), reverse=True)
print(vlist)
print('Max two values are  ', vlist[0], vlist[1])
