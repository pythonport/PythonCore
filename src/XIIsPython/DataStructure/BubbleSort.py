'''
Created on Aug 23, 2019

@author: admin
'''

def bsort(aList):
    n = len(aList)
    for i in range(n):
        for j in range(0, n - i - 1) :        
            if aList[j] >= aList[j + 1] :
                aList[j], aList[j + 1] = aList[j + 1], aList[j]

aList = [15, 6, 13, 22, 3, 52, 3]
print('Orignal list is - ', aList)
bsort(aList)
print("Sorted list is - ", aList)
