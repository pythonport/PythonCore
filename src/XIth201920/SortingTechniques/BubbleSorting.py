'''
Created on Jan 10, 2020
Bubble sort implemented in Python in ascending
order using List.
@author: admin@pythonport.com
'''
lst = [56, 778, 87, 55, 11, 33, 97]
print('Original list is - ', lst)
n = len(lst)

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1] :
            lst[j], lst[j + 1] = lst[j + 1], lst[j]    
    print('Sorted list after {0} - {1}'.format(i+1,lst))
print('Sorted list is - ', lst)