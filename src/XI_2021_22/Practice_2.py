'''
Created on Mar 24, 2022
2. Write a program to enter name of employee and their 
salary of 5 employees as input and store them in a dictionary.
@author: admin
'''
import json
dc = {}
for i in range(2) :
    name = input('Enter name of employee - ')
    salary = float(input('Enter salary of employee - '))
    dc[name] = salary
print("employee list is - ", json.dumps(dc, indent=2))
