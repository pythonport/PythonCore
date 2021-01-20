'''
Created on Sep 1, 2020
Insertion in array using traditional algorithm
@author: admin
'''


def findpos(arr, item):
    size = len(arr)
    if item < arr[0] :
        return 0
    else :
        pos = -1
    
    for i in range(size - 1) :
        if(arr[i] <= item and item < arr[i + 1]) :
            pos = i + 1
            break
    if (pos == -1 and i <= size - 1) :
        pos = size
    
    return pos


def shift(arr, pos):
    arr.append(None)
    size = len(arr)
    i = size - 1
    while i > pos :
        arr[i] = arr[i - 1]
        i -= 1


# main
lst = [11, 24, 25, 27, 39, 59]
item = int(input("Enter the element want to add to Array - "))
print('Array is - ', lst)
ind = findpos(lst, item)
print("Item will be inserted at index - ", ind)
shift(lst, ind)
lst[ind] = item
print('Array after addition is - ', lst)