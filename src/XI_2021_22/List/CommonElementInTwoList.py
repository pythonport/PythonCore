'''
Created on Mar 5, 2022
Program to find common element in two list
@author: admin
'''
lst1 = [2, 33, 4, 66, 33, 4, 11, 2]
lst2 = [2, 3, 4, 66, 6, 4, 11, 2]

comn = []
for i in lst1 :
    for j in lst2 :
        if (i == j and i not in comn):
            comn.append(i)

print("Common elements in two list are - ", comn)
print("-------------------------------")
aset = set(lst1)
bset = set(lst2)
'''
print(aset)
print(bset)
print("And in sets - ", aset & bset)
print("Or in sets - ", aset | bset)
'''
if (aset & bset ) :
    print('common elements are : ',aset & bset)
else :
    print("no common element found")
