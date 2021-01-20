"""
Linear Search in Array
"""

def lsearch(array, item):
    i = 0
    while i < len(array) and array[i] != item:
        i += 1
    if i < len(array):
        return i
    else:
        return False

#main section - One
narray = [33,23,34,31,65]
item = int(input("Enter item to be searched in the array - "))
index = lsearch(narray, item)
if index:
    print("Item found at index - ", index, ' position - ', index + 1)
else:
    print('Sorry No match found')


# main section - Two
# n = int(input("Enter the length of array - "))
# arr = [0] * n  # create the array of size given.
# print("*** Enter the element of array ***")
# for i in range(len(arr)):
#     arr[i] = int(input('Enter the element for ' + str(i) + ' - '))
# item = int(input("Enter item to be searched in the array - "))
# index = lsearch(arr, item)
# if index:
#     print("Item found at index - ", index, ' position - ', index + 1)
# else:
#     print('Sorry No match found')
