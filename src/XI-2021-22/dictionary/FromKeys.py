'''
Created on Mar 9, 2022

@author: admin
'''
lsubject = ('hindi', 'english', 'maths', 'sst', 'science')
lmarks = (67, 88, 77, 98, 67)
dmarks1 = dict.fromkeys(lsubject, 90)
print(dmarks1)

dmarks2 = dict.fromkeys(lsubject, lmarks)
print(dmarks2)

dmarks3 = dict.fromkeys(lsubject)
print(dmarks3)