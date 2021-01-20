'''
Created on Sep 14, 2019

@author: admin
'''
import math
radius = float(input("Enter radius of circle - "))
print('1. Area of Circle')
print('2. Perimeter of Circle')
ch = int(input("Enter your choice [1,2]-"))

if ch==1 :
    #area = math.pi*math.pow(radius, 2)

    area= 3.14*radius**2
    print("Area of circle - ", area)
else :
    perimeter = 2*math.pi*radius
    print("Perimeter of circle - ", perimeter)