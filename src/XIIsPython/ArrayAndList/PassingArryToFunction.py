'''
Created on Jul 4, 2019
Program to sumofArry using function
@author: admin
'''


def sumOfLst(numlst):
    sum = 0 
    for i in numlst:
        sum += i
    return sum


def getSquaredLst(numlst):
    for i in range(len(numlst)):
        numlst[i] = numlst[i] ** 2
    return numlst


lst = [3, 4, 5, 2, 3, 6] 

sumVel = sumOfLst(lst)

print("Sum of list is -", sumVel)
print("Squared list is -",getSquaredLst(lst))
