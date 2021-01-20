'''
Created on Jan 11, 2021
Table of number given by user using for loop
@author: admin
'''

num = int(input("Enter number to get table - "))
for i in range(1,11):
    print(num,' X ',i,' = ',num*i)