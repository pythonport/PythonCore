'''
Created on Jan 15, 2020
Insertion sort implemented in Python in ascending
order using List.
@author: admin@pythonport.com
'''
lst = [15, 6, 13, 22, 3, 52, 2]
print("original list is - ", lst)
for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and key < lst[j] :
        lst[j + 1] = lst[j]
        j = j - 1        
    else :
        lst[j + 1] = key
        print("List after {0} pass - ".format(i),lst)
print('Now sorted list is - ', lst)
