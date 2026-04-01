'''
Created on Mar 5, 2026
Find sum and mean value using for loop of a list
@author: admin
'''
mylist = eval(input('Enter list -'))
length = len(mylist)
mean = sum = 0
for i in range(0, length) :
    sum+=mylist[i]

mean = sum/length
print('Given list is - ',mylist)
print('Sum value is ',sum)
print('Mean value is ',mean)