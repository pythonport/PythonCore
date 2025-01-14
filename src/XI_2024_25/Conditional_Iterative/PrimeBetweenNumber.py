'''
Created on Jan 9, 2025
Program to get prime numbers between 2 to 50
@author: admin
'''
#Program to get prime numbers between 2 to 50
for i in range(2, 50):
    j= 2
    while ( j <= (i/2)):
        if (i % j == 0):
            break
        j += 1
    if ( j > i/j) :
        print ( i, "is a prime number")
print ("Bye Bye!!")





#--------------------------------------
num = int(input("Enter a number: "))
fact = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("factorial of ", num, " is ", fact)