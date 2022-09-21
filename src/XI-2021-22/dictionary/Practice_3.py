'''
Created on Mar 24, 2022
Write a program to count the number of times 
a character appears in a given string.
@author: admin
'''
str = "abcaabcacd"
dc = {}
for i in str :
    count = str.count(i)
    if i not in dc :
        dc[i] = count
print(dc)