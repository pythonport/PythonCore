'''
Created on Aug 23, 2019

@author: admin
'''


def insertSort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i - 1
        while j >= 0 and key < alist[j] :
                alist[j + 1] = alist[j]
                j = j - 1
        else :
            alist[j + 1] = key
        #print("ist after ", j , " is ", alist)

        
alist = [15, 6, 13, 22, 3, 52, 3]
print('Orignal list is - ', alist)
insertSort(alist)
print("Sorted list is - ", alist)

