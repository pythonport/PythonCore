'''
Created on Dec 12, 2019
Program to find frequency of all elements of a list. Also,Print the list of
unique elements in the list and duplicate element in the given list.

@author: admin
'''
lst = eval(input("Enter list in format of [] -"))
length = len(lst)
uniq = []
dupl = []
count = i = 0
while i < length:
    element = lst[i]
    count = 1
    if element not in uniq and element not in dupl:
        i += 1
        for j in range(i, length):
            if element == lst[j]:
                count += 1
        else :
            print("Element ", element, 'frequency : ', count)
            if count == 1:
                uniq.append(element)
            else:
                dupl.append(element)
    else :
        i += 1
print("Original ist ", lst)
print('Unique element list : ', uniq)
print('Duplicate element list : ', dupl)
