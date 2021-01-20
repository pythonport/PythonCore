'''
Created on Dec 14, 2019
Program to find sum of cube of list
@author: admin
'''
lst = [5, 7, 9, 11, 13, 15]
sum = 0
for i in lst :
    sum += i**3
print("sum of cube of all element is - ", sum)


lst = [5, 7, 9, 11, 13, 15]
length = len(lst)
sum = 0
for i in range(0, length ) :
    sum += lst[i]**3
print("sum of cube of all element is - ", sum)



    #cval = i ** 3
    #print("Cube of %d is %d" %(cval, i))