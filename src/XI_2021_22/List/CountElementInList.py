'''
Created on Feb 11, 2022

@author: admin
'''
lst = [55, 66, 44, 67, 34, 99, 66, 34]
countMax = 0
for i in lst :
    if i > 50 :
        countMax += 1

print("Count greater then 50 is -", countMax)
