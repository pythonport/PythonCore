'''
Created on Sep 1, 2020
Insertion in array sorted in descending order.
@author: admin
'''
import bisect

lst = [98,78,65,54,32,11]
print("Array in descending - ",lst)
lst.reverse()
print("Array in Ascending - ",lst)
item = int(input("Enter the element want to add to Array - "))
bisect.insort(lst, item)
print("Array in Ascending after adding element- ",lst)
lst.reverse()
print("Array in Descending after adding element- ",lst)