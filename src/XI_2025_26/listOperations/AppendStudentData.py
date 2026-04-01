'''
Created on Feb 26, 2026
Python code to append data into empty list
@author: admin
'''
stulist = []
for i in range(5):
    sname = input('Student Name - ')
    stulist.append(sname)

print('StuList - ',stulist)
stulist.reverse()