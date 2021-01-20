'''
import random

a,b = 1,30
for i in range(3):
    rnum = random.randint(a,b)
    print(rnum, end=" ")
'''
a,b,c = 3,4,5

flag = False  
  
if (a**2==b**2+c**2) :
    flag = True
elif(b**2==a**2+c**2) :
    flag = True
elif(c**2==a**2+b**2) :
    flag = True

if flag :
    print("Given data is making a RIGHT ANGLE TRIANGLE")
else :
    print("NOT A RIGHT ANGLE TRIANGLE")