'''
Created on Aug 5, 2019
Binary search by recursion.
@author: admin
'''
def binarySearchWithRecursion(lst, item, low, high):
    if low > high :     #base condition
        return -1
    
    mid = int((low + high) / 2)
    
    if item == lst[mid] :
        return mid
    elif item < lst[mid] :
        high = mid - 1
        return binarySearchWithRecursion(lst, item, low, high)
    else :
        low = mid + 1
        return binarySearchWithRecursion(lst, item, low, high)


lst = [1, 2, 114, 5, 77, 9, 34, 66]
lst.sort()
print('Sorted List - ', lst)
item = 77

index = binarySearchWithRecursion(lst, item, 0, len(lst)-1)

if index != -1 :
    print("%d is at index - %d" % (item, index))
else :
    print("Sorry no match")