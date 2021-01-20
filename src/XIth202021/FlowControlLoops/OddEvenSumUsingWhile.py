'''
Created on Jan 15, 2021
Odd sum and even sum of n natural number
@author: admin
'''

n = int(input("Enter any number - "))
ctr = 1
odd = even = 0
while ctr <= n :
    if ctr % 2 == 0:
        even+=ctr
    else :
        odd+=ctr
    ctr+=1

print("sum of even numbers are - ", even)
print("sum of odd numbers are - ", odd)