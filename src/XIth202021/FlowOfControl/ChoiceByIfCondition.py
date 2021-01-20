'''
Created on Jan 7, 2021

@author: admin
'''
import math
radius = float(input("Radius of circle is - "))
print('=======================')
print("1. Calculate Area")
print("2. Calculate Perimeter")
print('=======================')
choice = int(input("Enter your choice from [1-2] - "))
if choice == 1 :
    area = math.pi * radius ** 2
    print("area of %f is %f" % (radius, area))
elif choice==2:
    peri = 2*math.pi*radius
    print("Perimeter of %f is %f" % (radius, peri))
else :
    print("WRONG CHOICE....")