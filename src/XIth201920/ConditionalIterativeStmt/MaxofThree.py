'''
Created on Sep 14, 2019

@author: admin
'''
x = int(input("Enter first number - "))
y = int(input("Enter second number - "))
z = int(input("Enter three number - "))

max = x
if y>max:
    max= y
if z>max :
    max = z

print("Largest value is - ",max)