'''
Created on Jul 1, 2021

@author: admin
'''
a = b = c = 0

for i in range(1, 6) :
    a = int(input("Value of a - "))
    b = int(input("Value of b - "))
    if b == 0 :
        print("Divisor can not be zero! Aborting...")
        continue #break
    else :
        c = a / b
        print('Value of c is : ', c)
        
print("Outside of loop body")
