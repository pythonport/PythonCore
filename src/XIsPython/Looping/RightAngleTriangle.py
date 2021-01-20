'''
Created on Mar 28, 2019
Program to check right angle triangle based on three
sides given by user.
@author: admin
'''


def getRightAngleTriangle(a, b, c) :
    flag = False  
      
    if (a ** 2 == b ** 2 + c ** 2) :
        flag = True
    elif(b ** 2 == a ** 2 + c ** 2) :
        flag = True
    elif(c ** 2 == a ** 2 + b ** 2) :
        flag = True
    
    if flag :
        print("Given data is making a RIGHT ANGLE TRIANGLE")
    else :
        print("NOT A RIGHT ANGLE TRIANGLE")

        
def getRightBySecondMethod(a, b, c):
    x, y, z = a ** 2, b ** 2, c ** 2
    if max(x, y, z) == (x + y + z - max(x, y, z)) :
        print("Given data is making a RIGHT ANGLE TRIANGLE")
    else :
        print("NOT A RIGHT ANGLE TRIANGLE")
        

a = int(input("First Side - "))
b = int(input("Scond Side - "))
c = int(input("Third Side - "))
getRightBySecondMethod(a, b, c)
# getRightAngleTriangle(a,b,c) 
