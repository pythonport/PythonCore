'''
Created on Jan 4, 2021
Write a function LShift(Arr,n) in Python, 
which accepts a list Arr of numbers and n 
is a numeric value by which all elements of 
the list are shifted to left.
@author: admin
'''


def LShift(arr, n):
    l = len(arr)
    for x in range(0, n):
        y = arr[0]
        for i in range(0, l - 1) :
            arr[i] = arr[i + 1]
        arr[l - 1] = y
        #print(arr)
        #print('Iteration ========= ', x)
    print(arr)
    

lst = [11, 22, 33, 44, 55, 66, 77]
LShift(lst, 3)
