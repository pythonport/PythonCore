'''
Created on Apr 11, 2022

@author: admin
'''
import statistics

lst = [45,33,34,44,67,67,22,22,22,55]
meanVal = statistics.mean(lst)
print(meanVal)
medianValue = statistics.median(lst)
print(medianValue)
modeValue = statistics.mode(lst)
print(modeValue)