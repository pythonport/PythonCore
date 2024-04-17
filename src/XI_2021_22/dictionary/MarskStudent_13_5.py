'''
Created on Mar 7, 2022

@author: admin
'''
marks = {}
for a in range(2) :
    r, m = eval(input("Rollnumber, marks in form of list - "))
    marks[r] = m

print("Dictionary created")
print(marks)

r, m = eval(input("Enter roll and marks to change its value - "))
marks[r] = m
print(marks)
