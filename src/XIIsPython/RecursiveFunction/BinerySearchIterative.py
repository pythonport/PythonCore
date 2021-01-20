'''
Created on Jul 29, 2019
Binary Search uisng iteration and recursion.
@author: admin
'''

def leanierSearch(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high   :
        mid = int((low + high) / 2)
        print("Index - ",mid," value - ", lst[mid])
        if item == lst[mid] :
            return mid
        elif item < lst[mid] :
            high = mid - 1
        else :
            low = mid + 1
    else :
        return -1     


lst = [1, 2, 14, 5, 77, 91, 34, 66]
item = 1
      
index = leanierSearch(lst, item)

if index != -1 :
    print("%d is at index - %d" % (item, index))
else :
    print("Sorry no match")
