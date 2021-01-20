'''
Created on Dec 29, 2020

@author: admin
'''

import statistics
l = [34, 3, 4, 5, 4, 4, 4, 4, 4, 67, 44, 33, 33, 78, 12]

mean = statistics.mean(l)
median = statistics.median(l)
mode = statistics.mode(l)

print("Mean value - ", mean)
print("Median value - ", median)
print("Mode value - ", mode)
