'''
Created on Aug 30, 2024

@author: admin
'''
num = int(input("Number to get factorial - "))
fact = 1
for i in range(num, 0, -1) :
    fact *=  i

print('factorial of ',num,' is - ',fact)