'''
Created on Dec 28, 2019

program to rotate the element of a list so that the element at the first index
moves to the second index,the element of the second index moves to third and 
the last will to first index.

@author: admin
'''
lst = [34, 55, 66, 44, 33]
length = len(lst)
lastEle = lst[length - 1]
firstEle = lst[0]
print("List before modification is - ", lst)
for a in range(length - 1, -1, -1):
    #print(a, " value is - ", lst[a])
    if a == length - 1 :
        lst[0] = lastEle
    elif a == 0 :
        lst[a + 1] = firstEle
    else :
        lst[a + 1] = lst[a]

print("List after modification is - ", lst)

print('**'*15)

lst = [34, 55, 66, 44, 33]
print("List before modification is - ", lst)
length = len(lst)
l1 = lst[length-1:length]
print(l1)
l2 = lst[0:length-1]
print(l2)
lst = l1+l2
print("List before modification is - ", lst)

    
