'''
Created on Jan 21, 2021
Program to implement Binary Search in a array
using Python List
@author: admin
'''


# Binary Search
def BSearch(ar, item):
    beg = 0 
    last = len(ar) - 1
    while (beg <= last) :
        mid = (beg + last) // 2
        if(item == ar[mid]) :
            return mid
        elif(item > ar[mid]) :
            beg = mid + 1
        else :
            last = mid - 1
    else :
        return False


#-- Main -----
n = int(input("Enter the length of Array -"))
ar = [0] * n
for i in range(n):
    ar[i] = int(input("Enter element " + str(i) + " - "))

print("Array is - ", ar)

item = int(input("Enter item to search - "))
index = BSearch(ar, item)

if index :
    print(item, " found at index -", index)
else:
    print("Sorry no match found!")
