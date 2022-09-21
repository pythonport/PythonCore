'''
Created on Apr 16, 2022

@author: admin
'''
lst = [34, 22, 3, 44, 33, 12]
print("Before shifting - ", lst)
lst = lst[-1:]+lst[:-1]
print("After shifting - ", lst)
'''
lastValue = lst[-1]
for i in range(-1, -len(lst)+1, -1) :
    if(lst[i] == -len(lst)) :
        lst[i] = lst[i - 1]
        lst[i] == lastValue
    else :
        lst[i] = lst[i - 1]
    
print("After shifting - ", lst)
'''