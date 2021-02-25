'''
Created on Jan 21, 2021
Program to implement Leanear Search in a array
using Python List
@author: admin
'''


# Linear Search
def LSearch(ar, item):
    i = 0
    while i < len(ar) and ar[i] != item :
        i += 1
    if i < len(ar):
        return i
    else :
        return False


#-- Main -----
n = int(input("Enter the length of Array -"))
ar = [0] * n
for i in range(n):
    ar[i] = int(input("Enter element " + str(i) + " - "))

print("Array is - ", ar)

item = int(input("Enter item to search - "))
index = LSearch(ar, item)

if index :
    print(item, " found at index -", index)
else:
    print("Sorry no match found!")
