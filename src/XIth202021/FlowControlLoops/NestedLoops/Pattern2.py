'''
Created on Jan 25, 2021
Pattern using for loop from inner to outer
@author: admin
'''
n = 5  # no of lines
s = 0  # for initial value

for i in range(n, 0 , -1):
    for j in range(1, s + 1) :
        print(end=" ") #end with space and without space both need to test
    for j in range(1, i + 1):
        print(j, end="")
    s += 1
    print()
