'''
Created on Feb 25, 2022

@author: admin
'''
t = (4, 4, 5, 6, 2, 88, 6)
#First way to get sum of max and min element
t1 = (max(t), min(t))
print(t1)
print(sum(t1))

#second way to get sum of max and min element
print(sum((max(t), min(t))))

#Third way to get sum of max and min element
print(max(t)+min(t))