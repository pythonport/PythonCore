'''
Created on Mar 3, 2026
Find the minimum value using for loop
@author: admin
'''
mylist = eval(input('Enter list -'))
minval = mylist[0]
minindex = 0

for a in range(1, len(mylist)):
    if mylist[a] < minval :
        minval = mylist[a]
        minindex = a

print('Actual list - ',mylist)
print('Minimum value - ',minval)
print('Minimum index - ',minindex)