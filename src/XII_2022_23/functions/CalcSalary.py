'''
Created on May 7, 2022

@author: admin
'''
def empoyeeDetails(id,name, msalary):
    print("Employee id is - ",id)
    print("Employee name is - ",name)
    print("Employee monthly salary is - ",msalary)
    print("Employee yearly salary is - ",msalary*12)
    

id = input("Enter id - ")
name = input("Enter name - ")
msalary = int(input("Enter salary - "))
empoyeeDetails(id, name, msalary)