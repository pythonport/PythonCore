'''
Created on Aug 14, 2019
Insert using Traditional method of insert
@author: admin
'''


def FindPos(ar, item):
    size = len(ar)
    if item < ar[0]:
        return 0
    else :
        pos = -1
    for i in range(size - 1):
        if(ar[i] <= item and item < ar[i + 1]):
            pos = i + 1
            break
    if(pos == -1 and i <= size - 1) :
        pos = size
    return pos       


def Shift(ar, pos):
    ar.append(None)
    size = len(ar)
    i = size - 1
    while i >= pos :
        ar[i] = ar[i - 1]
        i = i - 1


lst = [11, 22, 33, 55, 66, 77, 78, 79, 89]
print("Actual list in sorted order is - ")
print(lst)

item = int(input("Enter element to be inserted - "))
pos = FindPos(lst, item)
print("Item to be inserted at - ", pos)
Shift(lst, pos)
lst[pos] = item
print(lst)
