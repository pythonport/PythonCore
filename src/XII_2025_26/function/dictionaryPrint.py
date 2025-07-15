'''
Created on Apr 12, 2025

@author: admin
'''
'''
Write a program that takes a string and prints a dictionary where keys are characters
and values are their frequencies. For example if string is banana then
dictionary will be {'b':1,'a':3,'n':2}
-------------------------------------------------------------------------

str = 'Jawahar Navodaya Vidyalaya Dhanbad'
dc = {}
for i in str :
    if i in dc :
        dc[i]+=1
    else : 
        dc[i]=1

print(dc)
'''

str = 'Jawahar Navodaya Vidyalaya Dhanbad'
dc = {}
for i in str :
    if i not in dc :
        dc[i]=str.count(i)

print(dc)