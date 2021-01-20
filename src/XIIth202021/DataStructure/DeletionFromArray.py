'''
Created on Sep 1, 2020
Deletion from an sorted arrary
@author: admin
'''


def bsearch(arr, item) :
    beg = 0
    last = len(arr) - 1
    while(beg <= last) :
        mid = (beg + last) // 2  # we need floor division of python3
        if(item == arr[mid]) :
            return mid
        elif(item > arr[mid]) :
            beg = mid + 1
        else :
            last = mid - 1  
    else :
        return False   

    
lst = [11, 24, 25, 27, 39, 59]
item = int(input("Enter the element want to delete to Array - "))
print('Array is - ', lst)
index = bsearch(lst, item)
# position = 0
# if index != False :
#     position = index + 1
#     print("Position is - ", position)
# print("Position is  - ", position)
if index:
    del lst[index]  # will delete the element from the position
    print("Array after deletion of element - ", lst)
else :
    print("Sorry no match found.")
