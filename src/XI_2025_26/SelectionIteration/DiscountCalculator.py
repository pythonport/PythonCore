'''
Created on Dec 9, 2025

@author: admin
'''

#code to demonstrate the use of if-else statement using discount calculator

discount = 0
sales = int(input('Enter sales - '))

if sales > 10000 :
    discount = sales*0.10
else :
    discount = sales*0.05

print('Sales amount is  - ',sales)
print('Disocunt amount is  - ',discount)