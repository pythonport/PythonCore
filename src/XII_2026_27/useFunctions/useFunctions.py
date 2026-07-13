'''
Created on Apr 1, 2026
use of user defined function
@author: admin
'''
def generateCube(num):
    cube = num**3
    print('cube of',num,'is ',cube)
    
num = int(input('Number to get cube value - '))
generateCube(num)

num1 = 5.5
generateCube(num1)

generateCube(6)