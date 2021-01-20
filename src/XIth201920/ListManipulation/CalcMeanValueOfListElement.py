'''
Created on Jan 3, 2020

@author: admin
'''
lst = [77, 88, 66, 54, 65, 34, 23]
mean = sum = 0

for a in lst :
    sum += a
 
mean = sum / len(lst)
print("total of list is - ", sum)
print("Mean value of list item is - ", mean)    
