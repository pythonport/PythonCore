'''
Created on Jul 27, 2021

@author: admin
'''
print("Before Function definition")
print('At line no 7 - ',__name__)

def perimeterOfRactangle(x,y):
    return 2*(x+y)

def cubeOfNum(a):
    return a**3

def getArea(a):
    areaOfCircle(a)
    
def areaOfCircle(r):
    area = 3.14*r*r
    print('Area is - ',area)

rval = perimeterOfRactangle(5, 6)
print("Perimeter of Ractangle is - ",rval)

getArea(4)
print("After Function definition")