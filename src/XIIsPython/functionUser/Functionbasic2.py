'''
Created on Apr 4, 2019

@author: admin
'''
''''
print(__name__)
x = int(input("Enter first number - "))    
y = int(input("Enter second number - "))   
'''
def addnum(a, b): #formal parameter 
    print("Value of a is - ", a)
    print('Value of b is - ', b)
    print('sum of ', a, ' and ', b, ' = ', a + b)
    print("inside function - ",__name__)

x = 10, y =20
addnum(x, y)
addnum(5,6) #argument or actual parameter
addnum(44,33)
addnum(66,77)
print("I am done")
print(__name__)

#if __name__ == "__main__":