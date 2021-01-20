'''
Created on Sep 2, 2020
Traversal in array
@author: admin
'''

def traversal(arr):
    size = len(arr)
    for i in range(size) :
        print(arr[i]*2, end=' ')

size = int(input("Enter the size of array - "))
lst = [None]*size
print("Enter element for the leaner list")
for i in range(size) :
    lst[i]=int(input("Enter the int element for index "+str(i)+" - "))

print("Arrary is - ",lst)
print("Traversal in list - ")
traversal(lst)