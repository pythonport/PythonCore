'''
Created on Jan 16, 2021

@author: admin
'''
a = b =c = 0
for i in range(1,5):
    a = int(input("Enter a - "))
    b = int(input("Enter b - "))
    if b==0:
        print("Zero division error! Aborting")
        #break
        continue
    else :
        c = a//b
        print("Quotient is - ",c)
    
print("Program over at - ",i," times")