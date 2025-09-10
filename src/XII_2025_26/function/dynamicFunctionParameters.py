'''
Created on Jul 31, 2025
Function with dynamic arguments
@author: admin
'''
def add(*nums):
    sum = 0
    for i in nums:
        sum += i
    print('Sum after addition -',sum)

add(12,15,14,15,14,16)
add(12,15,14,15,14,16,12,15,14,15,14,16,12,15,14,15,14,16)
add()