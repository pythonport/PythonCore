'''
Created on Feb 16, 2021
Write a function swap2List(arr,n) in python, that would accept a list
arr of n number. The function should modify the content of the list in 
such a way that the element, which are multiple of 5 swap with the
value present in very next position in the array.
@author: admin
'''


def swap2List(arr, n):
    for i in range(n - 1) :
        if arr[i] % 5 == 0:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print("Array after {i} pass is {arr} - " % (i, arr))
        # print("Array after", i, " pass is - ", arr)
    
    print("Array after swapping - ", arr)


arr = [1, 15, 7, 18, 20, 14]
print("Array before swapping - ", arr)
swap2List(arr, len(arr))
