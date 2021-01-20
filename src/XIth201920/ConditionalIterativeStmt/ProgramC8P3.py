'''
Created on Nov 7, 2019
Program that inputs three numbers and calculates two sum as per this :
sum1 : as the sum of all input numbers.
sum2 : as the sum of non-duplicate numbers.
@author: admin
'''

s1 = s2 = 0
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))

s1 = n1 + n2 + n3

if n1 != n2 and n1 != n3:
    s2 += n1
if n2 != n1 and n2 != n3:
    s2 += n2
if n3 != n1 and n3 != n2:
    s2 +=n3

print('Numbers are ', n1, n2, n3)
print('Sum of numbers are ', s1)
print('Sum of non duplicate numbers are ', s2)